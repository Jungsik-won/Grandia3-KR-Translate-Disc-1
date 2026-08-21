# Scenario text decoding data

Active scenario extraction uses the files in this directory. The historical
`legacy/` tree is reference-only.

- `grandia3_codebook_v9.csv` is a byte-identical working copy of the historical
  codebook. SHA-256: `672266ce1dff18716420b7ad2e86ea82a23daf6dfaebceea11201bb2239b608c`.
- `runtime_verified_glyph_overrides.csv` contains only glyph mappings proven by
  the 2026-08-21 Miranda dialogue capture and absent from that codebook.
- `face_speaker_map.csv` is generated from the ordered 83-texture table in
  `SYS/FACE.MDZ`. Scenario message header arguments index this table directly;
  the runtime-proven `0x1E` entry is `face_miranda_05`.

The codebook's `encoded_hex` values describe glyph indices. Scenario script
storage adds `0x20` to the low byte before the runtime converter writes the
16-bit glyph index. Page bytes remain `0xF0..0xF9`.
