#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt. No network, no input, deterministic.
"""
import os

POEM = """Can I come home? I asked.
The porch light was already on.
She opened the door before I knocked,
set my old plate on the table,
and said, your room is still yours."""

def main() -> None:
    # The bounty requires 1 to 280 characters, counted as Unicode code points.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError("poem must be 1 to 280 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
