"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast of a smart fridge to /output/entry.txt.
Standard library only.
"""

import os
import stat

ENTRY = (
    "My fridge's touchscreen suggested a recipe for the leftovers it "
    "already threw out, then asked me to rate its helpfulness."
)

MAX_CHARS = 200


def validate(text):
    """Check the entry line against the competition gate.

    Returns True when the text is UTF-8, 1 to 200 characters long,
    and not only whitespace.
    """
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    text.encode("utf-8")
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit("entry failed validation")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
