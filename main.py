#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt. No network, no input, deterministic.
"""
import os

POEM = """Ask, and the world leans in —
a door unlatched, a hand unclenched.
Nothing was ever locked.
We were only never asked,
and the yes had been waiting all along."""

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
