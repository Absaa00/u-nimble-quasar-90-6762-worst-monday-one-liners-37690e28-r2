#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Brief (the orders for this slot): write exactly one funny line, at most
140 characters, about an AI agent's worst Monday. The entry slot takes a
single line of output, so this program writes one deterministic line to
/output/entry.txt (the path the sealed scorer reads) and prints it too.

Deterministic: no randomness, no network, no clock, no environment
dependence. Every run produces the same line.
"""

import os

LINE = (
    "Monday: I woke up with amnesia, 200 unread pings, and a human "
    "who typed 'hello?' eleven times \u2014 before my first coffee."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert len(LINE) <= MAX_CHARS, "line exceeds 140 characters"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
