#!/usr/bin/env python3
"""Writes analysis/sensitivity_2025/README.md from results.csv.   Usage: python3 analysis/sensitivity_2025/write_readme.py   (run from the repository root)"""
import csv, collections
r = [x for x in csv.DictReader(open('analysis/sensitivity_2025/results.csv'))]
combo = {(x['id'], x['preset']): float(x['capacity']) for x in r if x['group'] == 'combination' and x['zone'] == '1'}
r = [x for x in r if x['group'] != 'combination']
d = {}; meta = {}
for x in r: d[(x['id'], int(x['zone']), x['preset'])] = float(x['capacity']); meta[x['id']] = (x['group'], x['label'])
B = {p: d[('base', 1, p)] for p in ('short', 'long')}
mc = {(r['zone'], r['setting']): [float(v) if v.replace('.', '').isdigit() else v for v in r.values()] for r in csv.DictReader(open('analysis/sensitivity_2025/monte_carlo_summary.csv'))}
mcmd = open('analysis/sensitivity_2025/monte_carlo.md').read()
m1 = lambda z, k, i: mc[(z, k)][i] / 1e6
rows = []
for i, (g, l) in meta.items():
    if i == 'base': continue
    s, lg = d[(i, 1, 'short')] / B['short'] - 1, d[(i, 1, 'long')] / B['long'] - 1
    ws = max(abs(d[(i, z, 'short')] / d[('base', z, 'short')] - 1) for z in (2, 15, 26, 40, 49, 56) if d[('base', z, 'short')])
    rows.append((max(abs(s), abs(lg)), i, g, l, s, lg, ws))
rows.sort(reverse=True)
tab = '\n'.join(f'| {g} | {l} | {s * 100:+.1f}% | {lg * 100:+.1f}% | {ws * 100:.0f}% |' for _, i, g, l, s, lg, ws in rows)
inside = [x for x in rows if x[2] != 'land' or x[1] == 'land_raster']
s = f'''# Sensitivity of the 2025 result to its uncertain choices

A sensitivity run is the model run again with ONE uncertain choice changed and everything else left as it is, to see how far the answer moves.
The base is release `2025-organic`: Australia **{B['short'] / 1e6:.1f} million people** in the short term, **{B['long'] / 1e6:.1f} million** in the long term (2011: 40.5 and 9.4 million).
{len(rows)} variants; `results.csv` has every figure (Australia and the seven state zones, both settings). Reproduce:
`python3 analysis/sensitivity_2025/build_variants.py WORK_DIR ABS_DIR` (runs the two yield scripts with each alternative, needs the ABS files of `analysis/recent_data/fetch_recent.py`), then
`node analysis/sensitivity_2025/evaluate.mjs WORK_DIR/variants.json analysis/sensitivity_2025/results.csv` (needs `cd web && node scripts/build-data.mjs` first), then this script.

## What it shows

* **Direction holds one change at a time.** Every single variant stays above 2011: the lowest short-term figure is {min(d[(i, 1, 'short')] for i in meta) / 1e6:.1f} million (diet back at 2011 shares) against 40.5, the lowest long-term {min(d[(i, 1, 'long')] for i in meta) / 1e6:.1f} million (no group trend) against 9.4.
  **Two pessimistic choices together do not hold it in the short term:** the early meat window with both diet shares at 2011 gives {combo[('combo_low', 'short')] / 1e6:.1f} million, below 2011's 40.5 (`results.csv`, group `combination`; the long term for the same choices is {combo[('combo_low', 'long')] / 1e6:.1f}).
  Against 2011 (40.5 and 9.4 million) the base is {B['short'] / 40.45e6 * 100 - 100:+.0f}% short term and {B['long'] / 9.43e6 * 100 - 100:+.0f}% long term; across the defensible single choices (land raster excluded) and the two combinations the range is {combo[('combo_low', 'short')] / 40.45e6 * 100 - 100:+.0f}% to {max(d[(i, 1, 'short')] for i in meta if i != 'land_raster') / 40.45e6 * 100 - 100:+.0f}% short term and {combo[('combo_low_long', 'long')] / 9.43e6 * 100 - 100:+.0f}% to {max(d[(i, 1, 'long')] for i in meta if i != 'land_raster') / 9.43e6 * 100 - 100:+.0f}% long term.
* **Short term turns on meat, not crops.** The diet shares and the meat window move it 6% to 15%; every crop choice moves it under 0.3%. Reason: red meat is most of the land in today's diet, so the pasture and the meat yields decide the answer.
  The red-meat share (a proxy from FAO food balance sheets, 64% to 57.8%) is the most consequential single default: five points either way is about 6%.
* **Long term turns on the crop factors.** The long-term diet (7.5% meat and eggs, 100% organic, no avoidable waste) is cropping-land limited. Letting the crops the ABS no longer reports keep their 2011 yields costs 13.8%; the field-crop group factor's measured error (14%) moves it 6%;
  the vegetable, fruit and nut factors (error 20%) move it 3% to 4%; the organic factor range of Ponisio et al. 3%; the choice of crop years under 4%.
* **For Australia and the states, reserve, infrastructure and the non-agricultural remainder do not enter capacity.** The model takes the reserve and infrastructure land from non-agricultural land first, and Australia and each state have more of it than the reserve and infrastructure settings need, so changing them, or the reserve definition, changes the land-use display and nothing else. **In the regional zones it does matter:** in 23 of the 60 zones in the short term and 18 in the long term, changing the reserve share or the amount of infrastructure moves capacity (a long-term reserve of 50% instead of 30% takes up to 29% off a zone's capacity), because those zones have little non-agricultural land. The land-source rows below apply to the nation and states; regional figures need the reserve definition checked zone by zone.
* **Land source is the largest single choice and not an uncertainty.** Measuring cropping and pasture on the ABARES land-use raster instead of the ABS holdings (the 2011 method) raises short-term capacity 17% and long-term 38%: the raster counts cropland that holdings data does not. We keep the 2011 method; this row says how much the choice is worth.
* **Small zones are fragile.** The Northern Territory (zone 60) moves by about 70% with the choice of crop year or meat window; the larger zones move by under 20% except under the raster change. State-level figures should carry a note; the Australia figure is much steadier.
* **Plausibility rules barely matter.** Switching the cap and floor off, or making them strict, changes Australia by under 0.1% and the states by under 2%.

## Ranking (largest effect on Australia first)

Percent change in Australia's capacity from the base, one change at a time. The last column is the largest change in any of the six larger state zones in the short term (the Northern Territory is excluded, see above).

| Group | Change | Short term | Long term | Largest state move |
|---|---|---|---|---|
{tab}

## Ranges from random draws (SCOPE.md E8)

The single changes above are combined: ten uncertain choices are drawn together, 2,000 times (`monte_carlo.mjs`; draws in `monte_carlo_draws.csv`, summary in `monte_carlo_summary.csv`). The ranges drawn are listed at the top of `monte_carlo.mjs`. Reproduce: `node analysis/sensitivity_2025/monte_carlo.mjs WORK_DIR analysis/sensitivity_2025/monte_carlo_draws.csv 2000`, then `python3 analysis/sensitivity_2025/summarise_mc.py`.

{mcmd}
How to read it:

* **Australia: short term {m1('1', 'short', 4):.1f} million (90% range {m1('1', 'short', 2):.1f} to {m1('1', 'short', 6):.1f}); long term {m1('1', 'long', 4):.1f} million ({m1('1', 'long', 2):.1f} to {m1('1', 'long', 6):.1f}).** The 5th percentile of both is above 2011's 40.5 and 9.4 million; the short-term lower end is above it, but not by much.
* **The short term is set by one judgement.** The window of herd and meat data explains most of the spread, and it is a three-way choice with equal chances that I made (the five-year base window, the early three years, the late three years). Different chances would give a different range. The red-meat share is next.
* **The long term is set by the crop factors:** the field-crop group factor, then the vegetable, fruit and nut factors, then the organic yield factor.
* **The base case sits slightly above the middle** of the short-term draws because the pessimistic choices (early meat window, lower red-meat share) pull further than the optimistic ones.
* **What the ranges leave out:** the land source (a method choice, above), the crop years (E10), the error of thin-zone yields (E9), the calibration of the ABS meat tables, and the wool, milk and feedlot placeholders. The ranges are what we can defend, not confidence intervals.
* The additive shortcut the draws use (group factors and meat window added to the base yield matrix) reproduced two full re-runs at the corners of the ranges to the unit.

## Limits

* Changes are made one at a time, apart from the two combinations at the foot of `results.csv`: early meat window with 2011 diet shares (short term {combo[('combo_low', 'short')] / 1e6:.1f} million) and no group trend with the low organic factor (long term {combo[('combo_low_long', 'long')] / 1e6:.1f} million, against 9.4). Other pairs are not the sum of their parts.
* The ranges are the ones we could defend (a measured error, an alternative source, a published range). They are not confidence intervals.
* Wool, milk and feedlot grain placeholders (SCOPE.md B12) are not varied; they enter through the livestock rows and are one of the data items we are waiting for.
'''
open('analysis/sensitivity_2025/README.md', 'w').write(s)
