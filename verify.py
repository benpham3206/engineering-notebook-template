"""Check the notebook's structure and requirement trace.

Run from the repo root:  python verify.py
Exits 0 when every file passes, 1 otherwise. Needs Python 3.9 or later.

Checks, for each project (the repo root and example/):
- every notebook file has a valid name, a date line, and its required headings in order;
- BOM.md, if present, has its required headings;
- every requirement ID in GOAL.md is unique, and every ID a test log checks exists.
It also lists requirements with no passing test yet. That is a report, not a failure.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATE = r"\d{4}-\d{2}-\d{2}"
NAME = r"[a-z0-9-]+\.md"

PROJECTS = [".", "example"]

# folder in notebook/ -> (template, file name pattern, required headings in order)
KINDS = {
    "entries": ("entry.md", rf"{DATE}-{NAME}",
                ["Objective", "Method", "Data", "Calculations", "Results",
                 "Decisions and why", "Next steps"]),
    "decisions": ("decision.md", rf"D\d{{3}}-{NAME}",
                  ["Context", "Options", "Decision", "Why", "Revisit if"]),
    "tests": ("test-log.md", rf"T\d{{3}}-{NAME}",
              ["Objective", "Pass criteria", "Setup", "Procedure", "Data",
               "Results", "Notes"]),
    "gates": ("gate.md", rf"G\d{{3}}-{NAME}",
              ["Step", "Cost if wrong", "Checklist", "Decision"]),
    "interfaces": ("interface.md", NAME,
                   ["Sides", "What crosses", "Limits", "Failure behavior",
                    "How it is checked"]),
    "handoffs": ("handoff.md", rf"{DATE}-{NAME}",
                 ["State", "Done", "Open", "Next step", "Hazards"]),
}

# one bill of materials per project, at the project root
BOM = ("bom.md", ["Parts", "Totals", "Notes", "Changes"])

REQ = re.compile(r"^- (R\d+):", flags=re.M)
CHECKS = re.compile(r"^\*\*Checks:\*\*(.*)$", flags=re.M)
STATUS = re.compile(r"^\*\*Status:\*\* (\w+)", flags=re.M)


def check(path, headings, is_template):
    """Return a list of problems with one file's headings and date line."""
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


def trace(project):
    """Return (problems, report lines) for the requirement trace of one project."""
    goal = project / "GOAL.md"
    if not goal.exists():
        return [], []
    ids = REQ.findall(goal.read_text(encoding="utf-8"))
    problems = [f"GOAL.md: requirement {r} is listed twice"
                for r in sorted(set(ids)) if ids.count(r) > 1]
    passed = set()
    for test in sorted((project / "notebook" / "tests").glob("*.md")):
        text = test.read_text(encoding="utf-8")
        m = CHECKS.search(text)
        cited = re.findall(r"R\d+", m.group(1)) if m else []
        for r in cited:
            if r not in ids:
                problems.append(f"{test.name}: checks {r}, which is not in GOAL.md")
        status = STATUS.search(text)
        if status and status.group(1) == "pass":
            passed.update(cited)
    report = [f"{r} has no passing test yet" for r in dict.fromkeys(ids) if r not in passed]
    return problems, report


def main():
    failures = 0
    checked = 0

    def show(path, problems):
        nonlocal failures, checked
        checked += 1
        for p in problems:
            print(f"{path.relative_to(ROOT).as_posix()}: {p}")
        failures += bool(problems)

    for template, _, headings in KINDS.values():
        show(ROOT / "templates" / template, check(ROOT / "templates" / template, headings, True))
    show(ROOT / "templates" / BOM[0], check(ROOT / "templates" / BOM[0], BOM[1], True))

    for name in PROJECTS:
        project = (ROOT / name).resolve()
        for folder, (_, pattern, headings) in KINDS.items():
            for path in sorted((project / "notebook" / folder).glob("*.md")):
                problems = check(path, headings, False)
                if not re.fullmatch(pattern, path.name):
                    problems.append(f"name does not match {pattern}")
                show(path, problems)
        bom = project / "BOM.md"
        if bom.exists():
            show(bom, check(bom, BOM[1], False))
        problems, report = trace(project)
        for p in problems:
            print(f"{(project / 'GOAL.md').relative_to(ROOT).as_posix()} trace: {p}")
        failures += len(problems)
        label = "root" if name == "." else name
        for line in report:
            print(f"  [{label}] {line}")

    print(f"{checked} files checked, {failures} with problems")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
