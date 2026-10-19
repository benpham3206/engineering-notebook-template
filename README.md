# Engineering notebook template

An **engineering notebook** is a dated, permanent record of what you set out to do, what you did, what you measured, what you decided, and why. Use this template for one project per repo. It works for a weekend gadget, and it also works for a product with a case, a circuit board, and firmware.

Engineers keep one because:

- every number in a drawing, a parts list, or firmware traces back to the measurement or calculation that produced it;
- decisions keep their reasons, so nobody has to guess later why a part is the way it is;
- a dated record can be evidence of what was known and invented, and when (how much weight it carries depends on your employer and jurisdiction);
- writing what you expected before a test, then what happened, is how judgment grows.

## Use it

1. Click "Use this template", name the repo for the project, then replace this README with a short one about the project.
2. Fill in [GOAL.md](GOAL.md) and add a first dated line to [STATUS.md](STATUS.md).
3. For each work session, copy a template from [templates/](templates/) to the place below and fill it in as you work:

| Template | Copy to | Name |
|---|---|---|
| [entry.md](templates/entry.md) | `notebook/entries/` | `YYYY-MM-DD-short-name.md` |
| [decision.md](templates/decision.md) | `notebook/decisions/` | `DNNN-short-name.md` |
| [test-log.md](templates/test-log.md) | `notebook/tests/` | `TNNN-short-name.md` |
| [bom.md](templates/bom.md) | repo root | `BOM.md`, one per project, revised in place |

4. Run `python verify.py` before you commit. It checks that each notebook file and the BOM have their required headings and a valid name. It needs Python 3.9 or later and nothing else.

[example/](example/) shows every template filled in for a small build: a curtain bot with one enclosure on each side of the window, each with a motor, a cord loop, and a Wi-Fi board that opens the curtains at 07:00 and closes them at 21:00. Delete it when you start your own project.

Add folders such as `cad/`, `electronics/`, `firmware/`, `calc/`, `data/`, and `media/` beside `notebook/` when the project needs them. [CONVENTIONS.md](CONVENTIONS.md) covers units, significant figures, uncertainty, corrections, and citations.
