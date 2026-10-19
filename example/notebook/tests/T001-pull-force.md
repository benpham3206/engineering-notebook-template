# T001: Pull force

**Date:** 2025-10-20
**Status:** pass

## Objective

Measure the force needed to start and to keep each curtain panel moving, as the input to motor sizing.

## Pass criteria

Five readings per panel per force, with a spread under 0.5 N, so the mean is usable for sizing.

## Setup

- Spring scale, 0 to 10 N, 0.1 N divisions.
- Curtains as hung, rings on the existing rod, room at about 21 degrees Celsius.
- Scale hooked to the lead ring of each panel and pulled level along the rod.

## Procedure

1. Close the panel fully.
2. Pull slowly and record the highest reading before the panel moves (start force).
3. Keep pulling at a steady walk and record the steady reading at mid-travel (running force).
4. Repeat five times per panel.

## Data

| Run | Left start (N) | Left running (N) | Right start (N) | Right running (N) |
|---|---|---|---|---|
| 1 | 3.4 | 2.1 | 3.9 | 2.6 |
| 2 | 3.6 | 2.0 | 4.1 | 2.4 |
| 3 | 3.3 | 2.2 | 3.8 | 2.5 |
| 4 | 3.5 | 1.9 | 4.0 | 2.7 |
| 5 | 3.4 | 2.0 | 3.9 | 2.5 |

## Results

| Panel | Start force, mean (N) | Largest start (N) | Running force, mean (N) |
|---|---|---|---|
| Left | $3.44 \pm 0.05$ | 3.6 | 2.04 |
| Right | $3.94 \pm 0.05$ | 4.1 | 2.54 |

Uncertainty is one standard uncertainty of the mean of five pulls. Spread is 0.3 N on every set, under the 0.5 N limit: pass. Values from [calc/curtain.py](../../calc/curtain.py).

## Notes

The right panel's rings catch on the wall bracket near the end of travel. Cleaning the rod may lower both forces; re-run this test if the rod is cleaned or the curtains are changed.
