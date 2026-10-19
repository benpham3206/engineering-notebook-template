# First build and power

**Date:** 2025-10-27

## Objective

Check that both enclosures move their panels within the time limit, and decide the power supply from measured current.

## Method

Printed and assembled both enclosures. Ran each through ten open and close cycles. Measured supply current of the left enclosure with a bench multimeter in series with the 5.00 V supply, at idle (board on Wi-Fi, motor off) and while moving. Timed each move with a stopwatch.

## Data

| Quantity | Value | Unit | Notes |
|---|---|---|---|
| Supply voltage | 5.00 | V | bench supply |
| Idle current | 0.030 | A | board connected to Wi-Fi |
| Running current, mean | 0.21 | A | left enclosure |
| Move time, mean of ten | 14.8 | s | left; right was 15.3 s |
| Moves per day | 2 | | |

## Calculations

Energy per day for one enclosure:

$$E_{move} = 5.00\ \text{V} \times 0.21\ \text{A} \times 14.8\ \text{s} \times 2 = 31\ \text{J}$$

$$E_{idle} = 5.00\ \text{V} \times 0.030\ \text{A} \times 86400\ \text{s} = 12960\ \text{J}$$

Idle is 99.8 % of the daily energy. Charge over 30 days is about $21.7\ \text{A h}$ per enclosure. All values from [calc/curtain.py](../../calc/curtain.py).

## Results

Both panels move within the 20 s limit. The idle board, not the motor, sets the power design: a month of idle needs about 11 times the charge printed on the 2.0 A h cells on hand.

## Decisions and why

- Keep a 5 V USB adapter for each enclosure. Battery power would need deep sleep and a battery-backed clock, which is a redesign for a later version.

## Next steps

- Run the 14-day schedule test, [T002](../tests/T002-schedule-timing.md), across the clock change on 2025-11-02.
