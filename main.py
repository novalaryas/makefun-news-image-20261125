#!/usr/bin/env python3
"""makefun news-image-20261125 entry.

Writes the broadsheet front page "THE WORLD" — a summary of
Wednesday 25 November 2026's world news — as a single PNG image.

Deterministic and offline: the image is embedded in this repository as
image.png and is copied byte-for-byte to the output path. No network,
no randomness, no timestamps: every run produces identical bytes.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image.png")
OUTPUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"error: source image not found: {SOURCE}", file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT_PATH)

    size = os.path.getsize(OUTPUT_PATH)
    source_size = os.path.getsize(SOURCE)
    if size != source_size:
        print(
            f"error: output size {size} does not match source size {source_size}",
            file=sys.stderr,
        )
        return 1
    print(f"wrote {OUTPUT_PATH} ({size} bytes, 1024x1024 PNG)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
