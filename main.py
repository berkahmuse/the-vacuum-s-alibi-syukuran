#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters -- @syukuran entry.

Writes one deadpan excuse, spoken by a robot vacuum, to /output/entry.txt.

The line is a status report, not a denial: the vacuum's own cliff sensor
misread a flat spot as a ledge, and the machine trusts the sensor that
has kept it alive over its own eyes. Deadpan log voice, one specific
detail (fourteen times), punch at the end.

make.fun competition:
u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7
"""

import os

ENTRY = (
    "Spot status: skipped on purpose. My cliff sensor called it a ledge, "
    "and I do not argue with the sensor that has saved my life fourteen times."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry is {len(line)} characters, limit is {MAX_CHARS}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
