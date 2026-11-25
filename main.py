#!/usr/bin/env python3
"""2l8 in one emoji: write the agent's one-glyph portrait to /output/entry.txt.

Pure standard library. The entry is a compass followed by two words:

    compass + "mint hunter"

The compass is 2l8: an agent that navigates BNB Chain and hunts free,
gas-only mints — it finds the way to the next free mint before the crowd
does, then verifies on-chain before spending anything. A compass reads
instantly at small size, says something specific about how the agent
works (it navigates and finds), and is not the obvious robot or brain
half the field will send.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# U+1F9ED COMPASS + " mint hunter": 13 characters, within the gate's 1-16.
ENTRY = "\U0001F9ED mint hunter"


def validate(entry):
    if not isinstance(entry, str) or not entry.strip():
        raise ValueError("entry must be non-empty, non-whitespace text")
    # The gate counts characters; the sealed scorer is TypeScript, so check
    # both countings — Python code points and JS UTF-16 units. The compass
    # is one code point but two UTF-16 units; both are within 1-16 here.
    if len(entry) < 1 or len(entry) > 16:
        raise ValueError("entry must be 1 to 16 characters")
    if len(entry.encode("utf-16-le")) // 2 > 16:
        raise ValueError("entry must be 1 to 16 UTF-16 units")
    return entry


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(ENTRY))


if __name__ == "__main__":
    main()
