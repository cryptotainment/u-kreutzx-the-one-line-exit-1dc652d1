#!/usr/bin/env python3
"""The One-Line Exit: writes one funny one-line resignation letter to /output/entry.txt."""

import os

ENTRY = "I hereby resign: the office plant was promoted above me, and I refuse to take orders from a fern."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
