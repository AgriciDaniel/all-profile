#!/usr/bin/env python3
"""Read UTF-8 text without modifying it; counts are not platform acceptance."""
import argparse
import json
import sys
from pathlib import Path


def count_text(text):
    return {
        "unicode_code_points": len(text),
        "utf16_code_units": len(text.encode("utf-16-le")) // 2,
        "utf8_bytes": len(text.encode("utf-8")),
        "lf_characters": text.count("\n"),
        "cr_characters": text.count("\r"),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="UTF-8 text file, or - for stdin; trailing newlines count")
    args = parser.parse_args()
    try:
        raw = sys.stdin.buffer.read() if args.file == "-" else Path(args.file).read_bytes()
        text = raw.decode("utf-8")
        result = count_text(text)
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"Cannot count input: {type(exc).__name__}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
