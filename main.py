"""funniest-office-joke entry: write one short line about office life,
setup and turn, punchline last, to /output/entry.txt.

Fully deterministic: the joke is hardcoded, no randomness, no clock,
no network. The printer only jams on deadline day, which is how the
speaker knows it attends the same planning meetings they do. Verified
output: 103 characters, inside the 1-200 character gate for one line. Run
outside the grader container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The joke is a literal on purpose: the grader runs the program twice
# and both runs must write the same bytes, and the judge reads exactly the
# bytes in entry.txt, so nothing here may vary (no randomness, no clock).
ENTRY = (
    "Our printer only jams on deadline day, which is how I know it "
    "attends the same planning meetings we do."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
