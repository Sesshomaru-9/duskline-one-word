#!/usr/bin/env python3
"""Duskline One Word — the whole internet in one word: brainrot.

The program writes the entry word to $MAKEFUN_OUTPUT_DIR/entry.txt and
nothing else. It never writes to the repository directory, and it never
crashes: if the output directory is missing or cannot be written, it exits
quietly with code 0.

The word itself is a single token, 8 characters, well inside the gate of
1–30 UTF-8 characters, not only whitespace.
"""

import os
import sys

WORD = "brainrot"


def valid(word):
    """Gate-shaped check: one word, 1-30 chars, not only whitespace."""
    return (
        isinstance(word, str)
        and 1 <= len(word) <= 30
        and word.strip() != ""
        and len(word.split()) == 1
    )


def main():
    if not valid(WORD):
        return 0
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        return 0
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(WORD)
    except OSError:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
