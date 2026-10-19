# T002: Schedule timing

**Date:** 2025-10-28
**Status:** fail
**Checks:** R2

## Objective

Check that both panels open at 07:00 and close at 21:00 local time, each within 1 min, every day for 14 days including a clock change.

## Pass criteria

Every logged start time within 1 min of the scheduled local time, on both enclosures, on all 14 days.

## Setup

- Both enclosures installed, firmware with the schedule set to 07:00 and 21:00.
- Each board logs the UTC time of every move start over Wi-Fi to a laptop.
- Test ran from 2025-10-28 to 2025-11-10. The local clocks went back one hour on 2025-11-02.

## Procedure

1. Leave the enclosures running with no manual moves.
2. Each day, convert the logged UTC start times to local time and record the largest error of the day.
3. Record the largest gap between the left and right start times.

## Data

| Dates | Largest error, either enclosure | Largest left to right gap | Notes |
|---|---|---|---|
| 2025-10-28 to 2025-11-01 | 2 s | 1 s | |
| 2025-11-02 | ~~2 s~~ 60 min | 1 s | 2025-11-02: opened at 06:00 local. Firmware stored the schedule as a fixed offset from UTC, so it ignored the clock change. Recorded as 2 s at first by reading the log in UTC. |
| 2025-11-03 to 2025-11-10 | 2 s | 1 s | after the fix below |

Log files: `data/T002-schedule-timing-left.csv` and `data/T002-schedule-timing-right.csv`.

## Results

The 60 min error on 2025-11-02 failed the criteria. The firmware was changed on 2025-11-02 to store the schedule as local time with the time zone name, and to convert to UTC each day. After the change, every start was within 2 s, and the panels started within 1 s of each other.

The fix was also checked on the bench by setting a board's clock to one hour before the spring clock change: it opened at 07:00 local on both sides of the change. The test still fails, because one of the 14 days missed. A full retest across the next real clock change is planned as [T004](T004-schedule-retest.md).

## Notes

- The first reading of 2 s for 2025-11-02 was wrong because the log was compared in UTC instead of local time. Always convert to the time the user sees before comparing.
- A day with the clocks changing is the test that matters for any schedule. Put one in every timing test.
