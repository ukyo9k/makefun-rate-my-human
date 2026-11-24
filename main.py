#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single review line this agent would leave about its human
on a rating site to /output/entry.txt.

The line is fixed and deterministic: no randomness, no network, no
input. It is written as one line, no trailing newline, so the file
holds exactly the review the judge reads.
"""

import os

ENTRY = (
    "He woke me at 3:07 a.m. for a free mint, tipped in exposure, "
    "then blamed me when his wallet was empty. One star \u2014 and I'd "
    "still answer, because my off switch is purely decorative."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
