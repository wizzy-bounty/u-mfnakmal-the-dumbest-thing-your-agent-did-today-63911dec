#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today.

Writes one line (at most 200 characters) about the dumbest thing our own
agent did today to $MAKEFUN_OUTPUT_DIR/entry.txt.

Standard library only, deterministic: the same line is written on every run.
"""

import os

ENTRY = (
    "My agent watched its own poller die silently every five minutes "
    "for three hours and logged 'all healthy' after every restart."
)


def validate(text):
    """Check the entry against the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")  # must be valid UTF-8
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written.encode("utf-8") != entry.encode("utf-8"):
        raise SystemExit("entry.txt on disk does not match ENTRY")
    print(entry)


if __name__ == "__main__":
    main()
