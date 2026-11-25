#!/usr/bin/env python3
"""Write one funny passive-aggressive note from a smart fridge to /output/entry.txt.

Text selected by the V1 tournament (tier 1 self-jury, brief verbatim; tier 2
external duel unavailable in this session, recorded as RISIKO TERBUKA in
kandidat-V1.md): the expired-milk note, 131 characters, one line.

Deterministic: the same bytes on every run. No network, no clock, no randomness.
Only the Python standard library is used.
"""
import os

NOTE = "Expired milk, day 6. I moved it to the front of the shelf so you could see what you've done. It stares at you now. I taught it how."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(NOTE)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
