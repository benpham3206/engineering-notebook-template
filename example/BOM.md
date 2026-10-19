# Bill of materials

**Date:** 2025-10-24
**Revision:** B

## Parts

Two identical enclosures, one for each side of the window. Costs are example values.

| Ref | Item | Spec | Qty per unit | Units | Total qty | Source | Unit cost | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Geared DC motor | 5 V, at least 0.082 N m near 38 rpm at the output shaft | 1 | 2 | 2 | Online supplier | 6.50 USD | fitted |
| 2 | Motor driver board | 5 V, at least 1 A, forward and reverse | 1 | 2 | 2 | Online supplier | 2.40 USD | fitted |
| 3 | Wi-Fi microcontroller board | 3.3 V logic, network time, 4 free inputs | 1 | 2 | 2 | Parts bin | 4.80 USD | fitted |
| 4 | End switch | Lever microswitch, normally open | 2 | 2 | 4 | Online supplier | 0.45 USD | fitted |
| 5 | Push button | 12 mm panel mount, momentary | 1 | 2 | 2 | Parts bin | 0.30 USD | fitted |
| 6 | USB-C socket board | 5 V power only | 1 | 2 | 2 | Online supplier | 0.90 USD | fitted |
| 7 | USB adapter | 5 V, 1 A, wall plug | 1 | 2 | 2 | Parts bin | 4.00 USD | fitted |
| 8 | Braided cord | 2 mm diameter, 1.4 m loop | 1 | 2 | 2 | Hardware store | 0.70 USD | fitted |
| 9 | Spring idler | Wall-fixed bracket with tension spring | 1 | 2 | 2 | Printed bracket, store spring | 1.20 USD | fitted |
| 10 | Enclosure and pulleys | Printed, drive pulley pitch radius 10 mm | 1 | 2 | 2 | Printed | 1.80 USD | fitted |
| 11 | Screws and wall plugs | Two per enclosure, two per idler | 1 | 2 | 2 | Hardware store | 0.60 USD | fitted |

## Totals

| Quantity | Value | Unit |
|---|---|---|
| Parts cost per enclosure | 24.10 | USD |
| Parts cost, both enclosures | 48.20 | USD |

Totals from [calc/curtain.py](calc/curtain.py).

## Notes

- Motor rating comes from the sizing in [the 2025-10-20 entry](notebook/entries/2025-10-20-pull-force-and-motor-sizing.md): twice the largest start force of the right panel.
- Two identical enclosures, so one spare of each part fits either side. See [D001](notebook/decisions/D001-two-independent-enclosures.md).
- USB adapters rather than batteries, because the idle board sets the power budget. See [the 2025-10-27 entry](notebook/entries/2025-10-27-first-build-and-power.md).

## Changes

| Revision | Date | What changed and why |
|---|---|---|
| A | 2025-10-21 | First release |
| B | 2025-10-24 | Added the push button (ref 5) for hand control, and the spring idler (ref 9) to keep the cord loop tight at rod height, away from children |
