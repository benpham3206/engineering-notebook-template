"""Check that every notebook file has a valid name and its required headings.

Run from the repo root:  python verify.py
Exits 0 when every file passes, 1 otherwise. Needs Python 3.9 or later.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATE = r"\d{4}-\d{2}-\d{2}"

NOTEBOOKS = ["notebook", "example/notebook"]

# folder in notebook/ -> (template, file name pattern, required headings in order)
KINDS = {
    "entries": ("entry.md", rf"{DATE}-[a-z0-9-]+\.md",
                ["Objective", "Method", "Data", "Calculations", "Results",
                 "Decisions and why", "Next steps"]),
    "decisions": ("decision.md", r"D\d{3}-[a-z0-9-]+\.md",
                  ["Context", "Options", "Decision", "Why", "Revisit if"]),
    "tests": ("test-log.md", r"T\d{3}-[a-z0-9-]+\.md",
              ["Objective", "Pass criteria", "Setup", "Procedure", "Data",
               "Results", "Notes"]),
}

# one bill of materials per project, at the project root
BOM = ("bom.md", ["Parts", "Totals", "Notes", "Changes"])


def check(path, headings, is_template):
    """Return a list of problems with one file."""
    text = path.read_text(encoding="utf-8")
    problems = []
    found = re.findall(r"^## (.+?)\s*$", text, flags=re.M)
    missing = [h for h in headings if h not in found]
    if missing:
        problems.append("missing headings: " + ", ".join(missing))
    elif [h for h in found if h in headings] != headings:
        problems.append("headings out of order; expected " + ", ".join(headings))
    if not is_template and not re.search(rf"^\*\*Date:\*\* {DATE}\s*$", text, flags=re.M):
        problems.append("missing a '**Date:** YYYY-MM-DD' line")
    return problems


def main():
    failures = 0
    checked = 0
    for folder, (template, pattern, headings) in KINDS.items():
        files = [(ROOT / "templates" / template, True)]
        for notebook in NOTEBOOKS:
            files += [(p, False) for p in sorted((ROOT / notebook / folder).glob("*.md"))]
        for path, is_template in files:
            checked += 1
            problems = check(path, headings, is_template) if path.exists() else ["file not found"]
            if not is_template and not re.fullmatch(pattern, path.name):
                problems.append(f"name does not match {pattern}")
            for p in problems:
                print(f"{path.relative_to(ROOT).as_posix()}: {p}")
            failures += bool(problems)
    template, headings = BOM
    files = [(ROOT / "templates" / template, True)]
    files += [(ROOT / n / ".." / "BOM.md", False) for n in NOTEBOOKS]
    for path, is_template in files:
        path = path.resolve()
        if not path.exists():
            continue
        checked += 1
        problems = check(path, headings, is_template)
        for p in problems:
            print(f"{path.relative_to(ROOT).as_posix()}: {p}")
        failures += bool(problems)
    print(f"{checked} files checked, {failures} with problems")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
