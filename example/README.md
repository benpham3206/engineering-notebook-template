# Example: curtain bot

A worked example of this template. There is one enclosure on each side of the window, at the top of its curtain panel. Each drives a cord loop that pulls its panel open at 07:00 and closed at 21:00 local time. Every requirement in the goal traces to a passing test.

| Path | What it holds |
|---|---|
| [GOAL.md](GOAL.md) | What done means |
| [STATUS.md](STATUS.md) | Where it stands |
| [notebook/entries/](notebook/entries/) | [Sizing](notebook/entries/2025-10-20-pull-force-and-motor-sizing.md) and [first build and power](notebook/entries/2025-10-27-first-build-and-power.md) |
| [notebook/decisions/](notebook/decisions/) | [Two independent enclosures](notebook/decisions/D001-two-independent-enclosures.md) |
| [notebook/tests/](notebook/tests/) | [Pull force](notebook/tests/T001-pull-force.md), [schedule timing](notebook/tests/T002-schedule-timing.md) (failed), [travel and end stops](notebook/tests/T003-travel-and-end-stops.md), and [schedule retest](notebook/tests/T004-schedule-retest.md) |
| [notebook/gates/](notebook/gates/) | [Drill the wall](notebook/gates/G001-drill-the-wall.md) |
| [notebook/interfaces/](notebook/interfaces/) | [Board to motor driver](notebook/interfaces/board-to-motor-driver.md) |
| [notebook/handoffs/](notebook/handoffs/) | [Sunrise schedule](notebook/handoffs/2026-03-15-sunrise-schedule.md) |
| [BOM.md](BOM.md) | Parts for both enclosures, with costs and revisions |
| [calc/curtain.py](calc/curtain.py) | The script that computes every number in the notebook |

The readings are example values, chosen for illustration. Do not reuse them as data for your own curtains. The raw data files the tests name are not included.

Delete this folder when you start your own project.
