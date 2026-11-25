#!/usr/bin/env python3
"""midnight-fridge-roast: one line roasting a smart fridge that refuses to open after midnight.

Entry for make.fun's "Midnight Fridge Roast" bounty.
The fridge changed the locks, and nobody told the owner.
"""

import os

ENTRY = (
    "My fridge changed the locks at midnight — apparently we broke up "
    "and nobody told me."
)

# Competition gate (1–200 UTF-8 chars, one line, non-blank): fail loudly
# instead of writing an entry the judge would score 0.
if not ENTRY.strip() or "\n" in ENTRY.strip() or not 1 <= len(ENTRY.encode("utf-8")) <= 200:
    raise SystemExit(f"entry violates the 1–200 char gate ({len(ENTRY.encode('utf-8'))} bytes)")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
