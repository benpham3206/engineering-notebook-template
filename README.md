# Engineering notebook template

An **engineering notebook** is a dated, permanent record of what you set out to do, what you did, what you measured, what you decided, and why. Use this template for one project per repo. It works for a weekend gadget, and it also works for a product with a case, a circuit board, and firmware.

Engineers keep one because:

- every number in a drawing, a parts list, or firmware traces back to the measurement or calculation that produced it;
- decisions keep their reasons, so nobody has to guess later why a part is the way it is;
- a dated record can be evidence of what was known and invented, and when (how much weight it carries depends on your employer and jurisdiction);
- writing what you expected before a test, then what happened, is how judgment grows.

## Use it

1. Click "Use this template", name the repo for the project, then replace this README with a short one about the project.
2. Fill in [GOAL.md](GOAL.md), giving each requirement an ID (R1, R2, ...), and add a first dated line to [STATUS.md](STATUS.md).
3. For each work session, copy a template from [templates/](templates/) to the place below and fill it in as you work:

| Template | Copy to | Name |
|---|---|---|
| [entry.md](templates/entry.md) | `notebook/entries/` | `YYYY-MM-DD-short-name.md` |
| [decision.md](templates/decision.md) | `notebook/decisions/` | `DNNN-short-name.md` |
| [test-log.md](templates/test-log.md) | `notebook/tests/` | `TNNN-short-name.md` |
| [bom.md](templates/bom.md) | repo root | `BOM.md`, one per project, revised in place |
| [gate.md](templates/gate.md) | `notebook/gates/` | `GNNN-short-name.md` |
| [interface.md](templates/interface.md) | `notebook/interfaces/` | `short-name.md` |
| [handoff.md](templates/handoff.md) | `notebook/handoffs/` | `YYYY-MM-DD-short-name.md` |

4. In each test log, list the requirements it checks on its `**Checks:**` line.
5. Run `python verify.py` before you commit. It checks that each notebook file and the BOM have a valid name, a date, and their required headings, and that every requirement a test checks exists in GOAL.md. It also lists the requirements with no passing test yet, which is a live view of how far from done the project is. It needs Python 3.9 or later and nothing else.

[CONVENTIONS.md](CONVENTIONS.md) covers units, significant figures, uncertainty, corrections, and citations.

## Scale it to the project

Start with the core and add a file only when the project needs it.

| Project | For example | Use |
|---|---|---|
| Small | A curtain bot, a phone stand, a sensor logger | GOAL, STATUS, entries, decisions, tests, and a BOM |
| Medium | A desk lamp whose metal plates are both heatsink and touch control | Add a test for every requirement that carries risk (temperature after an hour, false touches over many trials), and an interface where two subsystems share a part, such as the plate that is both heatsink and sensor |
| Large | A split wireless keyboard with two halves, a hub, circuit boards, firmware, and supplier orders | Add an interface for each link between subsystems, a gate before every expensive or irreversible step (ordering boards, cutting acrylic), and a handoff note whenever a person or agent passes work on |

In a large project, start each file's short name with its subsystem, for example `D004-hub-display.md` or `T012-left-half-battery-life.md`, so each subsystem's history sorts together. Keep the sources beside `notebook/`, in folders such as `cad/`, `electronics/`, `firmware/`, `calc/`, `data/`, and `media/`. The notebook records why those files are the way they are.

## The worked example

[example/](example/) is a small project carried from first measurement to done: a curtain bot with one enclosure on each side of the window. Each enclosure has a motor, a cord loop, and a Wi-Fi board, and opens its curtain at 07:00 and closes it at 21:00. The example uses every template, including the scale-up ones. It shows a gate before drilling the wall, the interface between the board and the motor driver, and a handoff for the next feature. It also includes a schedule test that failed on the night the clocks changed, then the retest. Delete the folder when you start your own project.
