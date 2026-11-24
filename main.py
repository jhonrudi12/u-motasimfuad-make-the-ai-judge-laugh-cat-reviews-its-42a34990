#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one single-line one-star review, written by a house cat about
its human, to entry.txt in the output directory.

The grader runs this as ``python3 main.py`` with a read-only repository
and a writable output directory (``$MAKEFUN_OUTPUT_DIR`` or ``/output``).
The program is deterministic: it always writes the same line.
"""

import os

ENTRY = "One star. He refills my bowl, then hogs MY warm laptop for eight hours like his job pays the rent. I have filed a formal complaint with the sunbeam."

OUTPUT_FILENAME = "entry.txt"


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 200 characters, a
    # single line, and not only white space. Fail loudly here rather
    # than handing the grader an invalid entry.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
