#!/usr/bin/env python3
"""The Moon Finally Answers Back -- make.fun entry.

The Moon answers every wish, howl and 2 a.m. promise ever aimed
at it, in a single line. The program writes that line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
import sys

# The line itself: the Moon, wry and four billion years tired of
# being wished upon, finally answering back. The comeback -- that
# the wisher is the one who is full -- lands in the last clause,
# before the line ends.
LINE = (
    "You wished on me, howled at me, and promised me you'd change "
    "at 2 a.m. \u2014 for four billion years. My answer is still no. "
    "And for the record, you're the one who's full."
)

MIN_CHARS = 1
MAX_CHARS = 240


def build_line() -> str:
    """Collapse the line to single-spaced text and enforce the cap."""
    text = " ".join(LINE.split())
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        raise ValueError("entry line must be 1-240 characters")
    if not text.strip():
        raise ValueError("entry line must not be only whitespace")
    return text


def output_dir() -> str:
    """Grader output dir, honouring the harness variable."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return configured or "/output"


def write_entry(path: str, text: str) -> None:
    """Write the line as plain bytes, readable by the collector."""
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    os.chmod(path, 0o644)


def verify(path: str, text: str) -> None:
    """Read the file back and prove it is one valid line."""
    with open(path, "rb") as handle:
        raw = handle.read()
    back = raw.decode("utf-8")
    if back != text or "\n" in back or not back.strip():
        raise ValueError("entry.txt does not round-trip as one line")


def main() -> int:
    text = build_line()
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path, text)
    verify(path, text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
