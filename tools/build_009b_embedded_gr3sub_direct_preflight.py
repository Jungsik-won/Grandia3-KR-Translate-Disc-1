#!/usr/bin/env python3
"""Build a 0x9B GR3SUB tail that executes in place without a second file load.

The existing GR3SUB prefix remains byte-exact.  Its appended 0x9B sidecar is
linked for the address where the normal preload already places that suffix.
The frame hook checks the field, the real 0x04AE request, and all sidecar
integrity sentinels before calling the sidecar renderer directly.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import struct

import build_009b_safe_sidecar_preflight as sidecar
import build_event_frame_tick_sprite_probe as atlas
import build_external_subtitle_container_test as external


ROOT = Path(__file__).resolve().parents[1]
EXISTING_CONTAINER_NAME = "GR3SUB.BIN"
NORMAL_TAIL_REGION_END_VA = 0x017C_8800


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(8 * 1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def build_direct_integrity_stub_words(
    code_va: int,
    package_va: int,
    package_size: int,
    code_prefix_words: tuple[int, int],
) -> list[int]:
    """Validate the preloaded normal-tail sidecar and run it without I/O."""
    words: list[int] = []
    branches: list[int] = []
    magic_words = struct.unpack("<2I", sidecar.SIDECAR_MAGIC)
    package_magic_words = struct.unpack("<2I", atlas.EVENT_ATLAS_MAGIC)

    checks = (
        (sidecar.SIDECAR_BASE_VA, magic_words),
        (code_va, code_prefix_words),
        (package_va, package_magic_words),
    )
    for address, expected_words in checks:
        atlas.load_word(words, 8, address)
        for offset, expected in enumerate(expected_words):
            words.append(atlas.ins_lw(9, 8, offset * 4))
            atlas.load_word(words, 10, expected)
            branches.append(len(words))
            words.extend((0, 0))

    atlas.load_word(words, 8, package_va + package_size)
    words.append(atlas.ins_lw(9, 8, 0))
    atlas.load_word(words, 10, sidecar.SIDECAR_MARKER)
    branches.append(len(words))
    words.extend((0, 0))

    words.extend((atlas.mips_j(code_va), 0))
    fallback_index = len(words)
    words.extend((*atlas.HOOK_WORDS, atlas.mips_j(atlas.RETURN_VA), 0))
    for index in branches:
        words[index] = atlas.ins_bne(9, 10, fallback_index - (index + 1))
    return words


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-iso", type=Path, required=True)
    parser.add_argument(
        "--active-manifest", type=Path,
        default=ROOT / "data/scenario/gr3_rendered_event_subtitles.json")
    parser.add_argument(
        "--sidecar-manifest", type=Path,
        default=ROOT / "data/scenario/gr3_rendered_event_subtitles_sidecar_009b.json")
    parser.add_argument(
        "--replace-main-prefix", action="store_true",
        help=("rebuild the normal GR3SUB prefix from the active manifest "
              "before relinking the proven normal-tail direct 0x9B sidecar"))
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    _extent, source_container_size, source_container = external.iso_entry(
        args.source_iso, EXISTING_CONTAINER_NAME)
    preliminary = external.build_container_and_renderer(args.active_manifest)
    manifest_container = bytes(preliminary["container"])
    if args.replace_main_prefix:
        prefix_container = manifest_container
        prefix_size = len(prefix_container)
    else:
        if manifest_container != source_container:
            raise ValueError("active-manifest GR3SUB prefix differs from source ISO")
        prefix_container = source_container
        prefix_size = source_container_size
    embedded_base_va = atlas.EXTERNAL_SUBTITLE_VA + prefix_size

    old_values = (
        sidecar.SIDECAR_BASE_VA,
        sidecar.SIDECAR_REGION_END_VA,
        sidecar.SIDECAR_NAME,
    )
    try:
        sidecar.SIDECAR_BASE_VA = embedded_base_va
        sidecar.SIDECAR_REGION_END_VA = NORMAL_TAIL_REGION_END_VA
        sidecar.SIDECAR_NAME = EXISTING_CONTAINER_NAME
        provisional_sidecar, _ = sidecar.build_sidecar(
            args.sidecar_manifest, preliminary)
        main_built = external.build_container_and_renderer(
            args.active_manifest,
            trailing_reserved_bytes=len(provisional_sidecar),
        )
        embedded_sidecar, sidecar_meta = sidecar.build_sidecar(
            args.sidecar_manifest, main_built)

        if int(main_built["unreserved_file_size"]) != prefix_size:
            raise ValueError("embedded GR3SUB prefix size changed")
        if int(main_built["trailing_reserved_bytes"]) != len(embedded_sidecar):
            raise ValueError("embedded sidecar reserve size mismatch")
        if int(main_built["line_buffer_va"]) != int(
                sidecar_meta["line_buffer_virtual_address"], 16):
            raise ValueError("main and sidecar line-buffer addresses diverged")

        combined_container = bytearray(main_built["container"])
        if bytes(combined_container[:prefix_size]) != prefix_container:
            raise ValueError("reserved build changed the selected GR3SUB prefix")
        combined_container[prefix_size:prefix_size + len(embedded_sidecar)] = (
            embedded_sidecar)

        support = bytearray(main_built["support"])
        while len(support) % 16:
            support.append(0)
        stub_va = atlas.DATA_CAVE_VA + len(support)
        code_va = int(sidecar_meta["code_virtual_address"], 16)
        package_va = int(sidecar_meta["package_virtual_address"], 16)
        package_size = int(sidecar_meta["package_byte_count"])
        code_prefix_words = tuple(
            int(value, 16) for value in sidecar_meta["code_prefix_words"])
        stub_words = build_direct_integrity_stub_words(
            code_va, package_va, package_size, code_prefix_words)
        stub = struct.pack(f"<{len(stub_words)}I", *stub_words)
        support.extend(stub)
        if len(support) > atlas.DATA_CAVE_CAPACITY:
            raise ValueError("direct sidecar gate exceeds SLPM data cave")

        gate_words = sidecar.build_path_gate_words(stub_va)
        gate = struct.pack(f"<{len(gate_words)}I", *gate_words)
        cave = gate + bytes(main_built["cave_bytes"])
        if len(cave) > atlas.CAVE_CAPACITY:
            raise ValueError("direct sidecar path gate exceeds frame cave")

        patched_built = dict(main_built)
        patched_built["support"] = bytes(support)
        patched_built["cave_bytes"] = cave
        _slpm_extent, _slpm_size, source_slpm = external.iso_entry(
            args.source_iso, "SLPM_659.76")
        patched_slpm = external.patch_slpm(source_slpm, patched_built)
    finally:
        (sidecar.SIDECAR_BASE_VA,
         sidecar.SIDECAR_REGION_END_VA,
         sidecar.SIDECAR_NAME) = old_values

    slpm_path = args.output_dir / "SLPM_659.76"
    container_path = args.output_dir / EXISTING_CONTAINER_NAME
    slpm_path.write_bytes(patched_slpm)
    container_path.write_bytes(combined_container)

    active_paths = {
        str(row["resource_path"]).upper()
        for row in main_built["helpers"]["resource_lookup_metadata"]
    }
    if "DATA/00397700.MDZ" in active_paths:
        raise ValueError("0x9B must remain absent from normal GR3SUB dispatch")

    report = {
        "schema_version": 1,
        "status": "PREPARE_ONLY_STATIC_PASS_RUNTIME_PENDING",
        "architecture": "EXISTING_GR3SUB_NORMAL_TAIL_DIRECT_009B_V1",
        "source_iso": str(args.source_iso.resolve()),
        "source_iso_sha256": sha256(args.source_iso),
        "container": {
            "path": str(container_path),
            "sha256": sha256(container_path),
            "source_prefix_byte_count": prefix_size,
            "source_prefix_sha256": sha256_bytes(prefix_container),
            "source_container_byte_count": source_container_size,
            "source_container_sha256": sha256_bytes(source_container),
            "main_prefix_rebuilt_from_active_manifest": bool(
                args.replace_main_prefix),
            "main_prefix_sha256": sha256_bytes(prefix_container),
            "output_byte_count": len(combined_container),
            "embedded_sidecar_offset": prefix_size,
            "embedded_sidecar_byte_count": len(embedded_sidecar),
            "normal_event_count": len(main_built["artifact"]["events"]),
            "normal_cue_count": len(main_built["artifact"]["cue_metadata"]),
            "00397700_normal_dispatch_absent": True,
            "shared_line_buffer_virtual_address": (
                f"0x{int(main_built['line_buffer_va']):08X}"),
        },
        "direct_sidecar": {
            **sidecar_meta,
            "filename": EXISTING_CONTAINER_NAME,
            "embedded_sidecar_virtual_address": f"0x{embedded_base_va:08X}",
            "second_file_load": False,
        },
        "renderer": {
            "slpm_path": str(slpm_path),
            "slpm_sha256": sha256(slpm_path),
            "frame_gate_byte_count": len(gate),
            "main_frame_cave_byte_count": len(main_built["cave_bytes"]),
            "combined_frame_cave_byte_count": len(cave),
            "frame_cave_capacity": atlas.CAVE_CAPACITY,
            "direct_integrity_stub_virtual_address": f"0x{stub_va:08X}",
            "direct_integrity_stub_byte_count": len(stub),
            "support_byte_count": len(support),
            "support_capacity": atlas.DATA_CAVE_CAPACITY,
            "runtime_integrity_gate": (
                "HEADER_AND_CODE_AND_PACKAGE_MAGIC_AND_TAIL_MARKER"),
        },
        "verification": {
            "new_disc_filename_required": False,
            "existing_gr3sub_prefix_byte_exact": not args.replace_main_prefix,
            "active_manifest_prefix_installed": True,
            "sidecar_linked_for_normal_tail": True,
            "load_deferred_until_sample_04ae": False,
            "dispatch_deferred_until_sample_04ae": True,
            "duplicate_runtime_file_load_removed": True,
            "00397700_global_prefix_reload_removed": True,
            "iso_created": False,
        },
    }
    (args.output_dir / "report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
