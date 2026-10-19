# Design review

**Date:** 2025-10-23

## Attendees

- Designer
- Reviewer, a housemate who also uses the room

## Agenda

1. One enclosure or two
2. Safety of the cord loop
3. Manual control

## Notes

- The reviewer asked what happens if one side jams. With one central enclosure, both panels stop; with two enclosures, only that side stops.
- The reviewer pointed out that a loose cord loop hanging below the curtain is a strangulation hazard for young children who visit.
- The reviewer wants to open the curtains by hand on a weekend without using a phone.

## Decisions

- Two independent enclosures, recorded in [D001](../decisions/D001-two-independent-enclosures.md).
- The cord loop runs only at rod height, kept tight by a spring idler fixed to the wall, never hanging below the top of the window.
- Each enclosure gets a push button that opens or closes its panel.

## Actions

| Action | Owner | Due |
|---|---|---|
| Add the cord rule and the push button to GOAL.md | Designer | 2025-10-24 |
| Add a 25 s move timeout in firmware in case an end switch fails | Designer | 2025-10-26 |
