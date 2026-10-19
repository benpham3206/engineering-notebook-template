# Conventions

These rules keep a number written today trustworthy and traceable years from now.

## Dates and times

- Write dates year first: `2026-03-02`.
- Machines log in UTC. Store a schedule people set ("open at 07:00") as local time plus the time zone name, never as a fixed offset.

## Units

- Use SI units first. Give US customary in parentheses only where needed: $8.0\ \text{mm}$ (0.31 in).
- Write a unit with every number that has one. In a table, put the unit in the column header: `Force (N)`.
- Use one consistent unit set per calculation, and say which one.
- Name local constants. Weight is $W = m g$ with $g$ for the place the part works. Standard Earth gravity is $9.80665\ \text{m/s}^2$.

## Significant figures

- Record readings to the full resolution of the instrument: `8.00 mm`, not `8 mm`.
- Carry extra digits through a calculation, and round only the final result.
- Round the result to the decimal place of its uncertainty, and quote the uncertainty to one or two significant figures.

## Uncertainty

- Record each instrument with its resolution and, if known, its calibration date.
- Name each source of uncertainty, and combine independent ones by root sum of squares.
- Write results as value, plus or minus, unit, and what the range means: $6.52 \pm 0.09\ \text{N}$ (one standard uncertainty).
- See [NIST Technical Note 1297](https://www.nist.gov/pml/nist-technical-note-1297) for the method.

## Corrections: never erase

- Strike a wrong value through, write the new one beside it, and add the date and the reason: `~~12 mm~~ 10 mm (2026-03-03: measured the wrong pulley)`.
- Never amend, rebase, or force-push commits that hold notebook entries. Add corrections as new commits.
- A withdrawn decision or test stays in place, with its status changed to `superseded by D002` or `void`.

## Citing sources

- Cite every number you did not measure or derive. Give the author or organization, the title, the edition, the year, and the page, table, or section. Add a link if the source is free.
- Say whether the value applies to your case. For example, a datasheet value for a molded sample is not the value for a printed part.

## Writing

- Use plain words and short sentences.
- Record raw numbers, not only conclusions.
- Write what you expected before what happened.
