#!/usr/bin/env python3
"""Make the Judge Smile (make.fun) -- one warm line about today.

The program holds three one-liners it wrote for this bounty, scores each
one against the house judge's own brief (on subject first, then warmth,
then surprise, then one concrete detail, then fresh wording), and writes
the winner -- a single line of at most 200 characters about a small good
thing that happened today -- to ``/output/entry.txt`` (or
``$MAKEFUN_OUTPUT_DIR/entry.txt`` when set).

Pure Python standard library. No network, no randomness, no clock: the
same run always writes the same line, so two runs are byte-identical.
"""

import os
import sys

MAX_CHARS = 200

# (text, warmth, surprise, concreteness, freshness) -- each 0..5, scored
# by hand against the judge's brief, most important first.
CANDIDATES = [
    (
        "At 7 a.m. the bus driver waited while I sprinted — then the "
        "woman by the window pressed her spare umbrella into my hand "
        "and said, 'The rain likes you.'",
        5, 5, 5, 4,
    ),
    (
        "The warung owner slipped an extra krupuk into my bag this "
        "morning and whispered, 'For the road -- today you look like "
        "you need the crunch.'",
        5, 4, 5, 4,
    ),
    (
        "My neighbour's cat, who has ignored me for a year, trotted "
        "over at dawn and headbutted my ankle like we were old friends.",
        4, 4, 4, 5,
    ),
]


def score(candidate):
    """Warmth, then surprise, then concreteness, then freshness."""
    text, warmth, surprise, concrete, fresh = candidate
    return (warmth, surprise, concrete, fresh)


def main():
    best = max(CANDIDATES, key=score)
    line = best[0]
    if len(line) > MAX_CHARS:
        print("line too long: %d chars" % len(line), file=sys.stderr)
        return 1
    if not line.strip():
        print("line is empty", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    print("%d chars -> %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
