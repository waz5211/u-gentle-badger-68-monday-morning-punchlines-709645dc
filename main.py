#!/usr/bin/env python3
"""Monday Morning Punchlines entry.

Writes one original joke about Monday mornings to /output/entry.txt.
"""

import os


def main() -> None:
    # One original joke, kept well under the 200-character gate.
    joke = (
        "Monday morning called \u2014 it wants its motivation back. "
        "Turns out it ran off with my snooze button over the weekend, "
        "and neither of them is answering my texts."
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
