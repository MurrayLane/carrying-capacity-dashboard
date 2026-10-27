#!/usr/bin/env python3
"""Writes analysis/resilience_2025/README.md from tables.csv, bootstrap.csv, storage.csv, capacity_by_table.csv.   Usage: python3 analysis/resilience_2025/write_readme.py (repository root)"""
import csv
T = {(r[0], r[1]): [float(x) for x in r[2:]] for r in list(csv.reader(open('analysis/resilience_2025/tables.csv')))[1:]}
B = {(r['location'], int(r['years'])): (float(r['p5']), float(r['p95'])) for r in csv.DictReader(open('analysis/resilience_2025/bootstrap.csv'))}
ST = [r for r in csv.DictReader(open('analysis/resilience_2025/storage.csv'))]
C = {(r['method'], int(r['zone']), int(r['years'])): int(r['capacity']) for r in csv.DictReader(open('analysis/resilience_2025/capacity_by_table.csv'))}
LOC = ['Australia', 'New South Wales', 'Victoria', 'Queensland', 'South Australia', 'Western Australia', 'Tasmania']
ZONE = {'Australia': 1, 'New South Wales': 2, 'Victoria': 15, 'Queensland': 26, 'South Australia': 40, 'Western Australia': 49, 'Tasmania': 56}
YRS = (5, 10, 20, 50, 100, 150)
M1, M2, M3, M4 = 'thesis (archive data)', 'data: ABS to 2024-25', 'loo reference', 'loo reference and fitted tail'
def tab(method): return '| Location | ' + ' | '.join(f'{y} yr' for y in YRS) + ' |\n|---|' + '---|' * len(YRS) + '\n' + '\n'.join(f'| {l} | ' + ' | '.join(f'{T[(l, method)][y - 1]:.3f}' for y in YRS) + ' |' for l in LOC)
cap = lambda m, z: C[(m, z, 100)] / 1e6
cap_tab = '| Zone | Model today (thesis table) | Data to 2024-25 (release `2025-resilience`) | Leave-one-out reference | Reference and fitted tail |\n|---|---|---|---|---|\n' + '\n'.join(
    f'| {l} | {cap("model table", ZONE[l]):.2f} | {cap(M2, ZONE[l]):.2f} | {cap(M3, ZONE[l]):.2f} | {cap(M4, ZONE[l]):.2f} |' for l in LOC)
iv = '| Location | Thesis table, 100 yr | 90% interval for a fitted tail, 100 yr |\n|---|---|---|\n' + '\n'.join(f'| {l} | {T[(l, M1)][99]:.2f} | {B[(l, 100)][0]:.2f} to {B[(l, 100)][1]:.2f} |' for l in LOC)
au1 = 26997189 / 1e6
sto = '| Location | Single worst year (no store) | worst 2 years (1 year of store) | worst 3 years | worst 5 years |\n|---|---|---|---|---|\n' + '\n'.join(
    f'| {l} | ' + ' | '.join(next(r['factor_at_100_years'] for r in ST if r['location'] == l and r['run_of_years'] == str(d)) for d in (1, 2, 3, 5)) + ' |' for l in LOC)
au = {d: float(next(r['factor_at_100_years'] for r in ST if r['location'] == 'Australia' and r['run_of_years'] == str(d))) for d in (1, 2, 3, 5)}
s = f'''# The resilience (climate variability) table, reproduced and updated (SCOPE.md E14)

The long-term settings ask the land to feed the population through a given number of years of weather: the setting is 100 years, and the harvest is scaled to the worst year expected once in that time. Without the setting the long-term figure for Australia would be 27.0 million instead of 12.3 (`analysis/long_term_2025/`), so the table behind it is the largest single lever of the long term.
It is the `resilience` sheet of the workbook: for Australia and each state, a factor for return periods of 1 to 150 years. This folder reproduces it from the thesis workings, updates its data to 2024-25, tests alternatives, and quantifies its uncertainty.
Reproduce: `python3 -I analysis/resilience_2025/resilience.py ARCHIVE_XLS HISTORIC_XLSX` (the archive workbook `prelim models/resilience 150 years.xls`, and the ABS `Historic Ag Commodities_1860 to 2022.xlsx` from the Agricultural Commodities, Australia 2021-22 release), `node analysis/resilience_2025/evaluate_tables.mjs analysis/resilience_2025/capacity_by_table.csv`, `python3 analysis/resilience_2025/write_readme.py`.

## 1. The thesis method is reproduced exactly

From the archive workbook: for each location and year, the unweighted mean of the wheat, oats and barley yields (t/ha); a reference that is the mean of the 10 observations from 5 before to 4 after the year (the window is held at the first or last 10 observations at the ends); the ratio of yield to reference; the ratios ranked from worst, rank k read as a one-in-(n+1)/k year event; anchors at 1, 3, 5, 10, 20, 30, 50 and 150 years, and straight-line interpolation between them (so the 100-year factor is the midpoint of the 50 and 150 year anchors).
`resilience.py` reproduces every anchor of the archive's table for Australia and the six states to machine precision (`replication.txt`), and the workbook's 150-year table exactly (a model evaluation with the reproduced table gives 12,305,891 for Australia, the same as the workbook).

## 2. The data update changes little

The ABS historical series (to 2021-22) and the three recent cubes extend the record from 138 to 153 observations. The same method on this data (release `2025-resilience`; the other tables are shown for comparison):

{tab(M1)}

Thesis table above; data to 2024-25 below.

{tab(M2)}

* **Australia's 100-year and 150-year factors do not change** (0.456 and 0.359): the worst year in the record is still 1915, and the second worst is old. The 5 and 20 year factors rise (0.866 to 0.892 and 0.599 to 0.634): the record now holds recent good years.
* Western Australia's 50 and 100-year factors fall (0.689 to 0.648, 0.491 to 0.471); South Australia's and Queensland's move by a few hundredths.
* Long-term capacity at 100 years (millions): Australia unchanged, Western Australia {cap("model table", 49):.2f} to {cap(M2, 49):.2f}, South Australia {cap("model table", 40):.2f} to {cap(M2, 40):.2f}; the short term is unchanged (resilience of one year is a factor of 1).
* The recent years are consistent with the table: the worst of eight recent single years gives a long-term capacity about 85% of their mean (`analysis/reliability_2025/`), between the table's 0.87 at five years and 0.74 at ten.

## 3. How uncertain the 100-year factor is

A one-in-100-year event estimated from about 150 years is an extrapolation, and the table hides how uncertain it is. Fitting a generalised Pareto distribution to the worst 20% of years (on the leave-one-out ratios below) and resampling the years 500 times gives:

{iv}

For Australia the 100-year factor could plausibly lie anywhere from {B[('Australia', 100)][0]:.2f} to {B[('Australia', 100)][1]:.2f}, which scales the long-term capacity at 100 years from about {B[('Australia', 100)][0] * au1:.1f} to {B[('Australia', 100)][1] * au1:.1f} million (the figure is {C[("model table", 1, 100)] / 1e6:.1f}). The state intervals are wider still (New South Wales 0.02 to 0.27). **The fitted tail should be used to state the uncertainty, not to replace the table**: its point estimates are unstable by state (New South Wales falls from 0.30 to 0.19, Western Australia rises from 0.49 to 0.54).

## 4. Alternatives tested, not adopted

* **Leave-one-out reference.** The thesis reference includes the year itself, so a very bad year pulls its own reference down by a tenth of its shortfall and the ratio is closer to 1 than the year deserves. A reference from the 20 other nearest observations removes that. It lowers Australia's 100-year factor from 0.456 to {T[(chr(65)+'ustralia', M3)][99]:.3f} (long-term capacity {cap(M3, 1):.2f} million, {cap(M3, 1) / cap("model table", 1) * 100 - 100:+.0f}%) and the state capacities by 7% to 10%. The effect is real but is a method change, so it is recorded here and left for a decision.
* **A fitted tail as the table**: see section 3; unstable.
* **Weighting the three grains by area**, **dropping the artefacts** (an unplanted grain counted as a yield of 0 in the early years, Queensland barley before 1871), and **a smoother trend** than a moving average were not tested.

## 5. Storage and the length of a drought

The table asks the population to meet its needs in the single worst year. A population holding a store of grain is bound instead by the worst run of consecutive years, whose average yield is higher. With the leave-one-out reference, the 100-year factor for the worst run of d consecutive years (a store of d-1 years of consumption):

{sto}

For Australia a store of one year of consumption lifts the 100-year factor from {au[1]:.2f} to {au[2]:.2f}, and two years to {au[3]:.2f}; as capacity is proportional to the factor that is {au[1] * au1:.1f}, {au[2] * au1:.1f} and {au[3] * au1:.1f} million. The model has no store input, so the 100-year setting is implicitly a population with no reserves of food. Offering a storage input is a design choice (SCOPE.md E15), not an update of data.

## Limits

* The series is three grains, yield only. Pasture, livestock, horticulture and the correlation of failures between crops are not in it; the factor scales all of the harvest.
* State series are for the states; regional zones use their state's row, so a small region's own variability is understated.
* Early observations (1861, 1866, 1871, then annual from 1876) are sparse, and early yields reflect the farming of the time.
* NSW in the 2022-23 to 2024-25 cubes includes the ACT; the historical series is NSW alone. The Northern Territory takes South Australia's row, as in the thesis.
'''
open('analysis/resilience_2025/README.md', 'w').write(s)
