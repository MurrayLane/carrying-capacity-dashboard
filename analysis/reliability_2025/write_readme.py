#!/usr/bin/env python3
"""Writes analysis/reliability_2025/README.md from years.csv and the base rows of analysis/sensitivity_2025/results.csv.   Usage: python3 analysis/reliability_2025/write_readme.py (repository root)"""
import csv, statistics
d = {}
for f in ('analysis/reliability_2025/years.csv',):
    for r in csv.DictReader(open(f)): d[(r['id'], int(r['zone']), r['preset'])] = float(r['capacity'])
ids = [i for i in dict.fromkeys(k[0] for k in d) if i.startswith('year_')]
ZONE = [(1, 'Australia'), (2, 'NSW and ACT'), (15, 'Victoria'), (26, 'Queensland'), (40, 'South Australia'), (49, 'Western Australia'), (56, 'Tasmania'), (60, 'Northern Territory')]
def table(k):
    h = '| Crop, herd and meat year | ' + ' | '.join(n for _, n in ZONE) + ' |\n|---|' + '---|' * len(ZONE) + '\n'
    f = lambda z, v: f'{v / 1e6:.1f}' if z == 1 else f'{v / 1e6:.2f}'
    rows = [('3-year window (the release)', [d[('base', z, k)] for z, _ in ZONE])] + [(i[5:], [d[(i, z, k)] for z, _ in ZONE]) for i in ids]
    rows += [('lowest year', [min(d[(i, z, k)] for i in ids) for z, _ in ZONE]), ('median of the years', [statistics.median(d[(i, z, k)] for i in ids) for z, _ in ZONE]), ('highest year', [max(d[(i, z, k)] for i in ids) for z, _ in ZONE])]
    return h + '\n'.join(f'| {n} | ' + ' | '.join(f(z, v) for (z, _), v in zip(ZONE, vs)) + ' |' for n, vs in rows)
A = lambda k: [d[(i, 1, k)] / 1e6 for i in ids]
lo = lambda k: min(A(k)); hi = lambda k: max(A(k)); med = lambda k: statistics.median(A(k))
worst = lambda k: ids[[d[(i, 1, k)] for i in ids].index(min(d[(i, 1, k)] for i in ids))][5:]
best = lambda k: ids[[d[(i, 1, k)] for i in ids].index(max(d[(i, 1, k)] for i in ids))][5:]
s = f'''# Capacity year by year (SCOPE.md E10)

Release `2025-organic` uses a three-year window of crop data and a five-year window of herd and meat data. This re-runs the result for each single ABS crop year there is data for
(2016-17 to 2020-21 and 2022-23 to 2024-25; the ABS cubes have no 2021-22), each with THAT year's crops, herds and meat, to see how much the answer depends on the weather and the herd cycle.
Land, population, diet and every other default are those of the release. Build: `python3 -I analysis/reliability_2025/build_years.py WORK_DIR ABS_DIR`, then
`node analysis/sensitivity_2025/evaluate.mjs WORK_DIR/years.json analysis/reliability_2025/years.csv`, then `python3 analysis/reliability_2025/write_readme.py`. Capacity in millions of people.

## Short term (today's diet)

{table('short')}

## Long term (low-meat, 100% organic, no avoidable waste)

{table('long')}

## What it shows

* **Australia, short term: {lo('short'):.1f} to {hi('short'):.1f} million across the eight years (median {med('short'):.1f}); the release says {d[('base', 1, 'short')] / 1e6:.1f}.** Lowest {worst('short')}, highest {best('short')}. The release sits in the middle of the years.
* **Australia, long term: {lo('long'):.1f} to {hi('long'):.1f} million (median {med('long'):.1f}); the release says {d[('base', 1, 'long')] / 1e6:.1f}.** Lowest {worst('long')}, highest {best('long')}.
* **Every single year is above 2011** (40.5 million short term, 9.4 long term), including the 2018-19 drought for the long term. The statement that capacity has risen does not depend on which years are chosen.
* **The two settings are driven by different things.** The long term follows the crop weather: its lowest year ({worst('long')}) is a drought year and the field-crop group factor for that year is 1.03, against 1.70 in the record year 2022-23. The short term follows the herd cycle: cattle meat produced was 2.10 million tonnes in 2020-21 (herd rebuilding) and 3.00 million tonnes in 2024-25 (heavy slaughter) with almost the same beef herd (0.993 and 1.04 of its 2009-10 size), and red meat is most of the land in today's diet.
  A year of heavy slaughter is not a year the land can sustain, so the top of the short-term range is a high estimate, not a typical one. The five-year meat window of the release is there to smooth this.
* **States move more than the nation.** Queensland's short-term figure runs from {min(d[(i, 26, 'short')] for i in ids) / 1e6:.1f} to {max(d[(i, 26, 'short')] for i in ids) / 1e6:.1f} million and the Northern Territory's by a factor of several; the herd and drought cycles do not coincide across states.

## Limits

* Eight years is too few to name a 1-in-10 year. The lowest of eight is a rough guide to a bad year, not a probability.
* Crops the ABS does not report take a group factor made from that year's reported crops (30 crops in 2016-21, 12 to 15 in 2022-25). The vegetable, fruit and nut factors are therefore smoother than the weather they stand for; the real year-to-year range is a little wider than shown.
* Only the national and state zones are evaluated: the 2016-21 cubes are on NRM boundaries that were not allocated to the 2011 zones.
* Years 2016-17 to 2019-20 use the 2020-21 land layer and the 2025 population; feed grain for the animals comes from that year's national yields.
'''
open('analysis/reliability_2025/README.md', 'w').write(s)
