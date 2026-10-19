# D001: Two independent enclosures

**Date:** 2025-10-23
**Status:** accepted

## Context

The window has two curtain panels that part in the middle. Each needs to move 0.60 m on the same schedule. The goal limits mounting to two screws per enclosure and rules out mains wiring.

## Options

| Option | For | Against |
|---|---|---|
| One enclosure at the centre driving both panels with one long cord loop | One motor, one board, panels always in step | Cord crosses the whole window; one jam stops both; harder to mount at the centre where the panels meet |
| One controller enclosure and a second motor-only enclosure, joined by a cable across the window | Panels always in step, one clock | A cable runs along the rod in view; two different enclosures to design |
| Two identical enclosures, each with its own board and clock | One design printed twice; each side works alone; no cable | Panels can drift apart in time; two adapters; two boards to update |

## Decision

Two identical enclosures, each running the schedule from its own network clock.

## Why

Both boards set their clocks from the same network time, so they should start together; [T002](../tests/T002-schedule-timing.md) measures how far apart they start. One design printed twice halves the CAD work, and a spare fits either side. A fault on one side leaves the other side working.

## Revisit if

- The panels are seen to start more than 2 s apart.
- The Wi-Fi network is often down for longer than the boards can keep time.
