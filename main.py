#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open — make.fun entry.

Writes one line (140 characters at most, no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Terrible advice delivered with total confidence: destroy production to test the backups, then shrug off the loss — deadpan, tight, worst advice an AI could give.
"""
import os

ENTRY = "Delete production to test the backups. If the backups fail, you clearly never needed that data anyway."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
