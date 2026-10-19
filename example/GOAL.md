# Goal

## Intent

Open the bedroom curtains in the morning and close them at night, with no one touching them, using parts that fit on the existing rod.

## Concept

- Two enclosures, one at the top of each panel. Each holds a geared DC motor, a drive pulley, two end switches, and a small Wi-Fi microcontroller board.
- A closed cord loop runs from the drive pulley to an idler at the window centre. The lead ring of the panel is clipped to the cord.
- Each enclosure gets the time from the network and runs the schedule on its own.

## Definition of done

- R1: Each panel travels its full 0.60 m in 20 s or less.
- R2: Both panels open at 07:00 and close at 21:00 local time, each within 1 min, on every day of a 14-day test that includes a clock change.
- R3: A move stops at the end switch, or after 25 s if a switch fails, and the motor stays off whenever the board resets.
- R4: A push button on each enclosure opens or closes that panel by hand.
- R5: The cord loop stays tensioned and fixed to the wall, out of reach of children.

## Constraints

- Powered from 5 V USB adapters. No mains wiring inside the enclosures.
- No changes to the rod or the wall beyond two screws per enclosure.
- Parts printed on a home printer, plus parts on hand.

## Open questions

- Whether the right panel needs its own speed, since it drags more.
