"""Snooze Button Roast — make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to the grader's output file and prints it to stdout.

Output resolution (first match wins):
  1. $ENTRY_OUT — a file path, or a directory (entry.txt is written inside)
  2. $ENTRY_OUT_DIR — entry.txt is written inside it
  3. /output/entry.txt — the path the RULES name
"""

import os
import sys

# The roast: one line, at most 200 characters. The alarm clock is the
# target (6 AM, Saturday); the punchline lands in the last few words.
ROAST = (
    "My alarm clock rang at 6 AM on a Saturday like a rooster promoted "
    "to middle management, so I hit snooze and demoted it back to poultry."
)


def resolve_output_path():
    """Pick where the entry text goes, from the environment or the default."""
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            return os.path.join(entry_out, "entry.txt")
        return entry_out
    entry_dir = os.environ.get("ENTRY_OUT_DIR")
    if entry_dir:
        return os.path.join(entry_dir, "entry.txt")
    return "/output/entry.txt"


def validate_roast(text):
    """The gate: 1-200 UTF-8 chars, one line, not only whitespace."""
    if not text or text != text.strip():
        return "entry has leading/trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if not 1 <= len(text) <= 200:
        return f"entry is {len(text)} chars, must be 1-200"
    if not text.strip():
        return "entry is only whitespace"
    return None


def write_entry(path, text):
    """Write the single-line entry, creating parent dirs as needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def main():
    text = ROAST.strip()
    problem = validate_roast(text)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    path = write_entry(resolve_output_path(), text)
    print(text)
    print(f"wrote {len(text)} chars to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
