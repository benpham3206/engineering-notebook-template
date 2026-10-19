# AGENTS.md

These are the rules for anyone, person or agent, who adds to this notebook.

## File map

| Path | What it holds |
|---|---|
| `README.md` | What the project is and where things live |
| `GOAL.md` | Intent, a measurable definition of done, constraints, open questions |
| `STATUS.md` | A dated log and the next steps |
| `notebook/entries/` | One entry per work session |
| `notebook/decisions/` | One record per significant choice |
| `notebook/tests/` | One log per test |
| `BOM.md` | The bill of materials, if the project has one. Revise it in place and log each revision in its Changes table |
| `templates/` | The blank templates for each notebook folder |
| `example/` | A filled-in example project: a two-enclosure curtain bot. Delete it in a real project |
| `CONVENTIONS.md` | Units, significant figures, uncertainty, corrections, citations |
| `verify.py` | The structure check |

## Rules

- Start each new notebook file by copying its template, and name it as the README table says.
- Never erase or rewrite a past entry. Correct it with a strike-through, the date, and the reason, as [CONVENTIONS.md](CONVENTIONS.md) says. Never amend, rebase, or force-push commits that hold notebook files.
- Record only what was actually measured, computed, or decided. Never invent data, readings, or sources. Leave a field empty rather than guess.
- Compute every number with a calculator or a script, and link the script.
- Give every number its unit, SI first, and every measured result its uncertainty.
- Cite every value you did not measure or derive.
- Add a dated line to `STATUS.md` when the state of the project changes.

## Verify

```
python verify.py
```

Run it before every commit. It must report no problems.
