# Handoff: sunrise schedule

**Date:** 2026-03-15

## State

The curtain bot meets every requirement in [GOAL.md](../../GOAL.md). The next feature is an option to open at sunrise instead of at 07:00. See [STATUS.md](../../STATUS.md).

## Done

- Both enclosures are mounted and pass [T003](../tests/T003-travel-and-end-stops.md) and [T004](../tests/T004-schedule-retest.md).
- The schedule is stored as local time plus the time zone name.

## Open

- The sunrise option is not started. Sunrise time needs the window's latitude and longitude, which are not in the firmware settings yet.

## Next step

Add a sunrise mode to the firmware schedule, and keep the fixed time as the default. It is done when a bench run, with the clock set to four dates across the year, opens within 1 min of the computed sunrise on both enclosures, logged as a new test.

## Hazards

- Do not change how the schedule handles time zones without repeating the clock-change check from T004 on the bench.
- Keep the 25 s move timeout and the pull-downs on IN1 and IN2. See [the interface](../interfaces/board-to-motor-driver.md).
- Keep the cord loop at rod height. If it hangs loose, it is a strangulation hazard for children.
