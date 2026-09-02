#!/usr/bin/env python3
"""Verify that every scored row totals what its attribute columns sum to.

The analysis tables are hand-maintained Markdown grids, which is exactly the
kind of thing that drifts. Run this after any edit to a scoring table.

    python3 verify_scores.py          # check all passes
    python3 verify_scores.py --fix    # rewrite incorrect totals in place

Exits non-zero if any row is inconsistent, so it also works as a pre-commit hook.
"""

import sys
from pathlib import Path

FILES = [
    "Use Case Analysis Pass 1.md",
    "Use Case Analysis Pass 2.md",
]


def parse_rows(lines):
    """Yield (index, cells) for each scored data row of the first grid in a file.

    The first pipe-row is the header and fixes the column count; separator rows
    and any narrower summary table are skipped.
    """
    width = None
    for i, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if width is None:
            width = len(cells)
            continue
        if set("".join(cells)) <= set("-: ") or len(cells) != width:
            continue
        yield i, cells


def check(path, fix=False):
    lines = path.read_text().split("\n")
    bad = []
    for i, cells in parse_rows(lines):
        try:
            actual = sum(int(c) for c in cells[1:-1])
            stated = int(cells[-1])
        except ValueError:
            continue  # non-numeric row, not a scored use case
        if actual != stated:
            bad.append((cells[0], stated, actual))
            if fix:
                cells[-1] = str(actual)
                lines[i] = "| " + " | ".join(cells) + " |"

    if bad and fix:
        path.write_text("\n".join(lines))

    label = "FIXED" if fix else "MISMATCH"
    for name, stated, actual in bad:
        print(f"  {label}  {name}: stated {stated}, columns sum to {actual}")
    if not bad:
        print(f"  ok")
    return len(bad)


def main():
    fix = "--fix" in sys.argv
    root = Path(__file__).parent
    total = 0
    for name in FILES:
        path = root / name
        if not path.exists():
            print(f"{name}\n  SKIPPED (not found)")
            continue
        print(name)
        total += check(path, fix)

    if total and not fix:
        print(f"\n{total} row(s) inconsistent. Re-run with --fix to correct them.")
        return 1
    print(f"\n{'Corrected' if fix else 'Verified'} {total if fix else 'all'} row(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
