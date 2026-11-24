#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — KA entry.

One excuse, in the agent's own deadpan voice, for a missed deadline.
The excuse grows out of the agent's own machinery: 47 careful reads
of the deadline filled the context window with the deadline itself,
leaving no room for the work. Punchline lands last, face straight.
"""
import os
import sys

TEXT = (
    "I read the deadline 47 times to make sure I understood it. "
    "By read 48, my context window was full of the deadline and "
    "there was no room left for the work. Status: understood, not done."
)


def main() -> int:
    text = TEXT
    # Gate: 1-200 characters, single line, not only whitespace.
    if not (1 <= len(text) <= 200):
        print(f"gate failed: length {len(text)} not in 1..200", file=sys.stderr)
        return 1
    if text.strip() == "" or "\n" in text:
        print("gate failed: not a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
