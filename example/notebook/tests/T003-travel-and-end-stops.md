# T003: Travel and end stops

**Date:** 2025-10-28
**Status:** pass
**Checks:** R1, R3, R4, R5

## Objective

On both mounted enclosures, check the travel time, the end stops and the timeout, the motor state during a board reset, the push buttons, and the cord loop.

## Pass criteria

- R1: every full move in 20 s or less.
- R3: the motor stops at each end switch; with an end switch disconnected, it stops at 25 s; it stays off through every board reset.
- R4: every button press moves its own panel to the other end.
- R5: under a 10 N downward pull at mid-span, the cord loop moves no more than 30 mm from rod height and stays on its pulleys.

## Setup

- Both enclosures mounted after [G001](../gates/G001-drill-the-wall.md), running firmware with the 25 s timeout.
- Stopwatch, 0.1 s display. Spring scale, 0.1 N divisions. Steel rule, 1 mm divisions.

## Procedure

1. Time five full opening moves per side, from the button press to the motor stopping.
2. Disconnect the open end switch, start an opening move, and time it.
3. Start a move and press the board's reset button partway through, three times per side.
4. Press each push button five times.
5. Pull the cord down at mid-span with 10 N and measure how far it moves from rod height.

## Data

| Check | Left | Right | Unit |
|---|---|---|---|
| Opening times | 14.9, 14.8, 15.0, 14.8, 14.9 | 15.4, 15.3, 15.5, 15.4, 15.3 | s |
| Move time with end switch disconnected | 25.1 | 25.1 | s |
| Motor off through reset | 3 of 3 | 3 of 3 | |
| Button presses that moved the panel | 5 of 5 | 5 of 5 | |
| Cord movement under 10 N pull | 15 | 18 | mm |

## Results

- R1: the longest moves were 15.0 s left and 15.5 s right, at least 4.5 s inside the limit. Values from [calc/curtain.py](../../calc/curtain.py).
- R3: both motors stopped at every end switch. With a switch disconnected, they stopped at 25.1 s, which is 25 s plus stopwatch reaction time. Both stayed off through every reset, as [the interface](../interfaces/board-to-motor-driver.md) requires.
- R4: 10 of 10 presses moved the panel.
- R5: the largest cord movement was 18 mm, and the loop stayed on its pulleys.

All criteria met: pass.

## Notes

After a reset, the board did not resume the interrupted move. It waits for the next scheduled time or a button press, as intended.
