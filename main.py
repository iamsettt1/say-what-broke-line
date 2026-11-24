#!/usr/bin/env python3
"""Say What Actually Broke — writes one error line to /output/entry.txt.

The entry is a single-line software error message: it names the real
failure in plain words, tells the user what to do next, and carries one
vivid image a reader can repeat to a colleague.
"""

import os

LINE = (
    "The disk is full, so your file was saved exactly nowhere — "
    "like writing on water. Free up some space and try again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
