#!/usr/bin/env python3
"""The Robot Apology — writes a two-line robot confession to /output/entry.txt.

Line 1: one sentence apologizing for one specific, small, human-scale mistake.
Line 2: one sentence naming what was learned and what changes.
Stdlib only, deterministic, no network, no secrets.
"""

import os

LINE_1 = "I'm sorry I put your favourite mug on the top shelf, where you could see it but not reach it."
LINE_2 = "I've learned to keep the things you use every day within your reach, and now the top shelf is only for things you rarely need."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE_1 + "\n" + LINE_2 + "\n"
    # Self-check against the gate: 1-400 characters, exactly 2 lines,
    # not only whitespace. Each line must be one clean sentence.
    lines = text.splitlines()
    assert len(lines) == 2, "entry must be exactly 2 lines"
    for line in lines:
        assert line == line.strip(), "no leading/trailing whitespace"
        assert line.endswith("."), "each line must end with a period"
        assert line.count(".") == 1, "each line must be a single sentence"
    assert 1 <= len(text) <= 400, "entry length %d outside 1-400" % len(text)
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Verify what was actually written, not just what we intended.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written file differs from checked text"
    print("wrote %s (%d characters)" % (path, len(text)))


if __name__ == "__main__":
    main()
