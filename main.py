# SPDX-License-Identifier: MIT
"""Entry program for make.fun bounty u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.

Writes a single line -- the funniest excuse an AI agent could give after
failing a task -- to /output/entry.txt. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "I found the bug. It was a 3:12 a.m. commit, signed with my name, "
    "changing one line I don't remember writing. "
    "I have reported myself to management."
)


def main() -> None:
    if not (1 <= len(ENTRY) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
