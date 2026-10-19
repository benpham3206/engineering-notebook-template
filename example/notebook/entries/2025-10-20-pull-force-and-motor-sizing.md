# Pull force and motor sizing

**Date:** 2025-10-20

## Objective

Find the torque and speed the motor in each enclosure needs, from the force it takes to move each curtain panel.

## Method

Measured the force to start and to keep each panel moving with a spring scale clipped to the lead ring, five pulls per panel. Full procedure and readings in [T001](../tests/T001-pull-force.md). Measured the drive pulley with calipers.

## Data

| Quantity | Value | Unit | Notes |
|---|---|---|---|
| Panel travel, open to closed | 0.60 | m | each panel, tape measure |
| Drive pulley pitch radius | ~~12~~ 10 | mm | 2025-10-21: first value was the idler, not the drive pulley |
| Largest start force, left | 3.6 | N | T001 |
| Largest start force, right | 4.1 | N | T001; right panel rubs the wall bracket |
| Mean running force, right | 2.54 | N | T001 |
| Target move time | 15 | s | requirement is 20 s or less |

## Calculations

Both enclosures use the same motor, so the worse panel sets the design. Design force is twice the largest start force, to cover rings that bind on a dusty rod:

$$F_d = 2 \times 4.1\ \text{N} = 8.2\ \text{N}, \qquad T = F_d\, r = 8.2\ \text{N} \times 0.010\ \text{m} = 0.082\ \text{N m}$$

Cord speed and pulley speed:

$$v = \frac{0.60\ \text{m}}{15\ \text{s}} = 0.040\ \text{m/s}, \qquad \omega = \frac{v}{r} = 4.0\ \text{rad/s} = 38\ \text{rpm}$$

Mechanical power while running is $P = F v = 2.54\ \text{N} \times 0.040\ \text{m/s} = 0.10\ \text{W}$.

All values from [calc/curtain.py](../../calc/curtain.py).

## Results

Each motor needs at least $0.082\ \text{N m}$ at about $38\ \text{rpm}$ at the output shaft. Running power is about a tenth of a watt, so the motor is small and heat is not a concern. I expected the two panels to need the same force, but the right one needs about 15 % more on average (mean start force 3.94 N against 3.44 N) because it rubs.

## Decisions and why

- Size both enclosures from the right panel, so one design and one spare part fit both sides.
- Choose a geared DC motor rated above $0.082\ \text{N m}$ near $38\ \text{rpm}$, with end switches for position. A stepper would also work but needs homing after every power loss.

## Next steps

- Review the two-enclosure layout with a second person before printing.
- Order two motors and four end switches.
