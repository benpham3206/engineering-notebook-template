# Interface: board to motor driver

**Date:** 2025-10-25
**Revision:** A

## Sides

The Wi-Fi microcontroller board (firmware) commands the motor driver board (electrical), which powers the motor. Both enclosures use this same interface.

## What crosses

| Item | Direction | Value | Unit | Notes |
|---|---|---|---|---|
| IN1, IN2 | board to driver | 0 or 3.3 | V | IN1 high opens, IN2 high closes, both low is off |
| Logic ground | shared | 0 | V | one ground point at the USB socket board |
| Motor supply | USB socket to driver | 5.00 | V | not through the board |
| End switches | switch to board | 0 or 3.3 | V | board pull-ups; a closed switch reads low |

## Limits

- The driver must read 3.3 V as high. This was checked against the driver board's input rating before ordering.
- Motor current must stay within the driver's 1 A rating in the [BOM](../../BOM.md). The running current measured in [the 2025-10-27 entry](../entries/2025-10-27-first-build-and-power.md) is 0.21 A for the whole enclosure.

## Failure behavior

- While the board resets, its pins float. A 10 kOhm pull-down on IN1 and IN2 holds both low, so the motor stays off.
- Firmware never sets IN1 and IN2 high together.
- A broken end switch wire reads as not pressed, so the 25 s move timeout stops the motor.

## How it is checked

[T003](../tests/T003-travel-and-end-stops.md) resets the board mid-move and disconnects an end switch, on both enclosures.
