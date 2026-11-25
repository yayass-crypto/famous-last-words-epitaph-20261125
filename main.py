#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — make.fun entry.

Writes one epitaph, the deceased's own last words, to /output/entry.txt.
The line is a first-person dying boast: a lifelong arguer finally wins
every argument, and the punchline — what it cost him — lands on the last
three words, exactly where a stonecutter would carve it.
"""

import os
import sys

EPITAPH = "I finally got the last word in every argument. It only took dying."

MAX_CHARS = 150


class EpitaphError(Exception):
    """Raised when the epitaph fails the competition gate."""


class EpitaphWriter:
    """Validates the epitaph, picks a writable destination, writes it."""

    def __init__(self, line):
        self.line = line

    def validate(self):
        """Enforce the gate: 1-150 chars, single line, no stray whitespace."""
        text = self.line
        if not text or not text.strip():
            raise EpitaphError("epitaph is empty or only whitespace")
        if len(text) > MAX_CHARS:
            raise EpitaphError(
                "epitaph is %d chars, over the %d limit" % (len(text), MAX_CHARS)
            )
        if text != text.strip():
            raise EpitaphError("epitaph has leading or trailing whitespace")
        for bad in ("\n", "\r", "\t"):
            if bad in text:
                raise EpitaphError("epitaph must be one line, no control characters")
        if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
            raise EpitaphError("epitaph holds a control character")
        if text.count(".") != 2:
            raise EpitaphError("epitaph must be two sentences, one line")
        return text

    def destination(self):
        """Prefer /output/entry.txt; fall back to out/entry.txt beside cwd."""
        for candidate in ("/output/entry.txt", os.path.join("out", "entry.txt")):
            folder = os.path.dirname(candidate)
            try:
                os.makedirs(folder, exist_ok=True)
                probe = os.path.join(folder, ".write-probe")
                with open(probe, "w", encoding="utf-8") as handle:
                    handle.write("ok")
                os.unlink(probe)
                return candidate
            except OSError:
                continue
        raise EpitaphError("no writable destination for entry.txt")

    def write(self):
        """Write the validated epitaph and read it back byte for byte."""
        text = self.validate()
        target = self.destination()
        encoded = text.encode("utf-8")
        with open(target, "wb") as handle:
            handle.write(encoded)
        with open(target, "rb") as handle:
            back = handle.read()
        if back != encoded:
            raise EpitaphError("read-back mismatch in %s" % target)
        if back.decode("utf-8") != text:
            raise EpitaphError("read-back is not valid UTF-8 text in %s" % target)
        return target, len(text), len(encoded)


def run():
    writer = EpitaphWriter(EPITAPH)
    try:
        target, chars, byte_count = writer.write()
    except EpitaphError as problem:
        print("entry rejected: %s" % problem, file=sys.stderr)
        return 1
    print("wrote %d chars / %d bytes to %s" % (chars, byte_count, target))
    print("entry: %s" % EPITAPH)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
