#!/usr/bin/env python3
"""Extract one exact ISO9660 entry for active, read-only research."""

from __future__ import annotations

import argparse
from pathlib import Path

from scan_scenario_resources import IsoImage


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iso", type=Path)
    parser.add_argument("entry")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    target = args.entry.upper()
    with IsoImage(args.iso) as image:
        matches = [entry for entry in image.entries() if entry.path.upper() == target]
        if len(matches) != 1:
            raise SystemExit(f"expected one ISO entry for {args.entry}, found {len(matches)}")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        image.write_entry(matches[0], args.output)
    print(f"extracted {args.entry}: {args.output} ({args.output.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
