#!/usr/bin/env python3
"""Make the Judge Smile — one warm line about a small good thing today.

Pure Python standard library. Writes the entry line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR when set). Deterministic: the same line every run.
"""

import os

LINE = (
    "At 6:40 this morning the warung lady tucked an extra krupuk into my bag "
    "and whispered, \"for the road, not for sale\" — breakfast suddenly had "
    "a plot twist."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
