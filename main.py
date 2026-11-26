#!/usr/bin/env python3
"""Duskline One Word — the whole internet in one word: brainrot.

Writes the entry word to $MAKEFUN_OUTPUT_DIR/entry.txt and nothing else.
Only the output directory is ever written: the program never writes to the
repository directory, and it never crashes if the output directory cannot
be written.
"""

import os
import sys

WORD = "brainrot"


def main():
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
