# T004: Schedule retest

**Date:** 2026-03-01
**Status:** pass
**Checks:** R2

## Objective

Repeat [T002](T002-schedule-timing.md) with the clock-change fix, across a real clock change.

## Pass criteria

Every logged start time within 1 min of the scheduled local time, on both enclosures, on all 14 days.

## Setup

As in T002, with firmware that stores the schedule as local time plus the time zone name. The test ran from 2026-03-01 to 2026-03-14. The local clocks went forward one hour on 2026-03-08.

## Procedure

As in T002.

## Data

| Dates | Largest error, either enclosure | Largest left to right gap | Notes |
|---|---|---|---|
| 2026-03-01 to 2026-03-07 | 2 s | 1 s | |
| 2026-03-08 | 2 s | 1 s | clock change day; opened at 07:00 local |
| 2026-03-09 to 2026-03-14 | 2 s | 1 s | |

Log files: `data/T004-schedule-retest-left.csv` and `data/T004-schedule-retest-right.csv`.

## Results

On all 14 days, including the clock change, every start was within 2 s of the scheduled local time, and the panels started within 1 s of each other. Pass. R2 is now met.

## Notes

Errors were compared in local time, as the T002 notes require.
