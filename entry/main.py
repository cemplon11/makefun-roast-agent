#!/usr/bin/env python3
"""Roast Your Own Agent — writes one original self-roast line to /output/entry.txt.

Pure Python stdlib, deterministic, no network. The line is a plain string
constant below; nothing is read from any other file.
"""

import os

ROAST = (
    "I asked my agent for a one-line roast; it spawned a subagent, "
    "wrote a plan, and came back with a novel."
)


def main() -> None:
    outdir = os.environ.get("OUTDIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
