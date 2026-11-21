#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt. No network, no input, deterministic.
"""
import os

POEM = """Nothing in the house was mine,
so I took nothing and asked for nothing.
One evening I asked for a chair.
The house gave me a chair, a cup,
a name — and a place at the table."""

def main() -> None:
    # The bounty requires 1 to 280 characters, counted as Unicode code points.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError("poem must be 1 to 280 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
