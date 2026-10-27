# Sensitivity of the 2025 result to its uncertain choices

A sensitivity run is the model run again with ONE uncertain choice changed and everything else left as it is, to see how far the answer moves.
The base is release `2025-organic`: Australia **48.0 million people** in the short term, **12.3 million** in the long term (2011: 40.5 and 9.4 million).
39 variants; `results.csv` has every figure (Australia and the seven state zones, both settings). Reproduce:
`python3 analysis/sensitivity_2025/build_variants.py WORK_DIR ABS_DIR` (runs the two yield scripts with each alternative, needs the ABS files of `analysis/recent_data/fetch_recent.py`), then
`node analysis/sensitivity_2025/evaluate.mjs WORK_DIR/variants.json analysis/sensitivity_2025/results.csv` (needs `cd web && node scripts/build-data.mjs` first), then this script.

## What it shows

* **Direction holds one change at a time.** Every single variant stays above 2011: the lowest short-term figure is 43.4 million (diet back at 2011 shares) against 40.5, the lowest long-term 10.6 million (no group trend) against 9.4.
  **Two pessimistic choices together do not hold it in the short term:** the early meat window with both diet shares at 2011 gives 39.6 million, below 2011's 40.5 (`results.csv`, group `combination`; the long term for the same choices is 12.3).
  Against 2011 (40.5 and 9.4 million) the base is +19% short term and +30% long term; across the defensible single choices (land raster excluded) and the two combinations the range is -2% to +37% short term and +9% to +38% long term.
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
| land | cropping and pasture measured on the land-use raster instead of the ABS holdings | +17.3% | +38.2% | 53% |
| meat window | meat and herd data of 2024-25 only | +15.4% | -0.1% | 13% |
| group trend | crops the ABS no longer reports keep their 2011 yields (factor 1.0) | -0.2% | -13.8% | 4% |
| diet and consumption | both diet shares at 2011 (13% and 64%) | -9.5% | +0.0% | 9% |
| meat window | meat and herd data of 2020-21 to 2022-23 only (before the heavy slaughter) | -8.5% | -0.0% | 8% |
| meat window | ABS meat tables not calibrated to the archive (cattle x1.0 instead of x1.086, sheep x1.0 instead of x1.155) | -7.0% | +0.0% | 7% |
| diet and consumption | red meat share back at 64% (no change since 2011) | -6.9% | +0.0% | 6% |
| group trend | field-crop factor 14% lower (the measured error of the rule) | -0.1% | -6.6% | 1% |
| meat window | meat and herd data of 2022-23 to 2024-25 only (three years, the years of heavy slaughter) | +6.4% | +0.1% | 7% |
| diet and consumption | red meat share 52.8% (5 points below the proxy) | +6.4% | +0.0% | 6% |
| diet and consumption | red meat share 62.8% (5 points above the proxy) | -5.7% | +0.0% | 5% |
| group trend | field-crop factor 14% higher | +0.1% | +5.6% | 1% |
| group trend | vegetable, fruit and nut factors 20% lower (the measured error of the rule is 20 to 22%) | -0.1% | -4.3% | 8% |
| crop window | crop data of 2024-25 only | +0.0% | -3.8% | 1% |
| organic | default organic factor 0.771 (lower end of Ponisio et al. 2015) on the 119 rows that use it | +0.0% | -3.3% | 0% |
| organic | default organic factor 0.845 (upper end of Ponisio et al. 2015) | +0.0% | +3.2% | 0% |
| group trend | vegetable, fruit and nut factors 20% higher | +0.1% | +3.1% | 6% |
| diet and consumption | meat and egg share back at 13% (no change since 2011) | -2.6% | +0.0% | 2% |
| group trend | field-crop factor from 2016-21 (1.29) instead of 2022-25 (1.36) | -0.0% | -2.2% | 0% |
| crop window | crop data of 2022-23 only | +0.0% | +2.0% | 2% |
| diet and consumption | meat and egg share 11.5% (one step below the proxy) | +1.4% | +0.0% | 1% |
| diet and consumption | meat and egg share 12.5% (one step above the proxy) | -1.3% | +0.0% | 1% |
| organic | organic default share 2% and baseline 2% (no change since 2011) | +0.0% | -1.3% | 0% |
| organic | organic baseline left at 2% (the constant in Yield!E2 not moved) with the 7% default | -1.0% | -1.3% | 1% |
| organic | organic default share and baseline 12% (the share of agricultural land the 2026 report gives) | +0.0% | +1.3% | 0% |
| crop window | drop the record year 2022-23 (mean of 2023-24 and 2024-25) | -0.0% | -1.2% | 1% |
| crop window | crop data of 2023-24 only (the poor year) | -0.1% | +1.0% | 2% |
| meat window | meat and herd data of a full herd cycle or longer (2010-11 to 2024-25) | +0.9% | +0.1% | 4% |
| organic | organic factors of the five crops at the commercial ratios of Kniss et al. alone | +0.0% | -0.9% | 0% |
| meat window | meat and herd data of a full herd cycle or longer (2018-19 to 2024-25) | +0.8% | -0.0% | 3% |
| organic | organic factors of the five crops back at 2011 values | +0.0% | +0.7% | 0% |
| meat window | meat and herd data of a full herd cycle or longer (2015-16 to 2024-25) | +0.6% | +0.0% | 4% |
| diet and consumption | fuel, biofuel and timber at 2011 values (2520 L, 0.5%, 1 m3) | -0.3% | +0.0% | 13% |
| meat window | meat and herd data of a full herd cycle or longer (2005-06 to 2024-25) | -0.1% | +0.2% | 7% |
| crop rules | strict rules: remove zone yields over 2 or under 0.2 times the national yield | +0.0% | +0.0% | 2% |
| crop rules | no plausibility cap or floor (only the 10 ha, 10 t and seed rules) | +0.0% | +0.0% | 2% |
| land | reserve = classes 1.1 and 1.2.5 (conservation and Indigenous uses) | +0.0% | +0.0% | 0% |
| land | reserve = class 1.1 only (nature conservation) | +0.0% | +0.0% | 0% |
| land | infrastructure measured on the raster (classes 5.3 to 5.7, 5.9) instead of 730 m2 a person | +0.0% | +0.0% | 0% |

## Ranges from random draws (SCOPE.md E8)

The single changes above are combined: ten uncertain choices are drawn together, 2,000 times (`monte_carlo.mjs`; draws in `monte_carlo_draws.csv`, summary in `monte_carlo_summary.csv`). The ranges drawn are listed at the top of `monte_carlo.mjs`. Reproduce: `node analysis/sensitivity_2025/monte_carlo.mjs WORK_DIR analysis/sensitivity_2025/monte_carlo_draws.csv 2000`, then `python3 analysis/sensitivity_2025/summarise_mc.py`.

2000 random draws (Latin hypercube) of the ten uncertain choices. Capacity in millions of people; the 90% range is the 5th to the 95th percentile of the draws.

| Zone | Short term: median | 90% range | base | Long term: median | 90% range | base |
|---|---|---|---|---|---|---|
| Australia | 47.8 | 42.3 to 52.5 | 48.0 | 12.2 | 11.4 to 13.2 | 12.3 |
| NSW and ACT | 11.93 | 10.64 to 13.10 | 11.99 | 2.11 | 1.95 to 2.29 | 2.13 |
| Victoria | 6.90 | 6.55 to 7.18 | 6.96 | 0.82 | 0.75 to 0.89 | 0.82 |
| Queensland | 8.54 | 8.04 to 9.04 | 8.84 | 0.74 | 0.68 to 0.81 | 0.75 |
| South Australia | 2.37 | 2.21 to 2.51 | 2.38 | 0.88 | 0.84 to 0.93 | 0.89 |
| Western Australia | 3.54 | 3.34 to 3.71 | 3.56 | 1.85 | 1.79 to 1.92 | 1.86 |
| Tasmania | 0.28 | 0.26 to 0.31 | 0.30 | 0.03 | 0.02 to 0.03 | 0.03 |
| Northern Territory | 0.06 | 0.05 to 0.07 | 0.06 | 0.01 | 0.01 to 0.01 | 0.01 |

Share of the variance of Australia's capacity explained by each choice alone:

| Choice | Short term | Long term |
|---|---|---|
| window of herd and meat data | 82% | 0% |
| field-crop group factor (±14%) | 0% | 60% |
| vegetable, fruit and nut factors (±20%) | 0% | 20% |
| default organic yield factor | 0% | 18% |
| red meat share of the diet | 17% | 0% |
| meat and egg share of the diet | 2% | 0% |
| organic share of land (default and baseline) | 0% | 1% |
| liquid fuel per person | 0% | 1% |
| biofuel share | 0% | 0% |
| timber per person | 0% | 0% |

The ten choices alone explain 102% of the short-term and 100% of the long-term variance; the rest is interaction.

How to read it:

* **Australia: short term 47.8 million (90% range 42.3 to 52.5); long term 12.2 million (11.4 to 13.2).** The 5th percentile of both is above 2011's 40.5 and 9.4 million; the short-term lower end is above it, but not by much.
* **The short term is set by one judgement.** The window of herd and meat data explains most of the spread, and it is a three-way choice with equal chances that I made (the five-year base window, the early three years, the late three years). Different chances would give a different range. The red-meat share is next.
* **The long term is set by the crop factors:** the field-crop group factor, then the vegetable, fruit and nut factors, then the organic yield factor.
* **The base case sits slightly above the middle** of the short-term draws because the pessimistic choices (early meat window, lower red-meat share) pull further than the optimistic ones.
* **What the ranges leave out:** the land source (a method choice, above), the crop years (E10), the error of thin-zone yields (E9), the calibration of the ABS meat tables, and the wool, milk and feedlot placeholders. The ranges are what we can defend, not confidence intervals.
* **With only full-cycle meat windows the short-term range narrows.** The first run includes two three-year windows (the early and the late years of the herd cycle), which is what makes the short-term range wide. Repeating the draws with the meat window chosen from the base window and four windows of 8, 10, 15 and 20 years (`monte_carlo_draws_longwindow.csv`, `MC_WIN_DIR=WORK_DIR node monte_carlo.mjs ...`), Australia's short term is 48.1 million (45.8 to 50.5), against 47.8 (42.3 to 52.5); the long term is unchanged (12.2, 11.4 to 13.2). A window that covers the herd cycle is the better basis for a published range, and the red-meat share is then the main short-term uncertainty. Northern Territory figures stay unreliable (0.01 to 0.06 million).
* The additive shortcut the draws use (group factors and meat window added to the base yield matrix) reproduced two full re-runs at the corners of the ranges to the unit.

## Limits

* Changes are made one at a time, apart from the two combinations at the foot of `results.csv`: early meat window with 2011 diet shares (short term 39.6 million) and no group trend with the low organic factor (long term 10.3 million, against 9.4). Other pairs are not the sum of their parts.
* The ranges are the ones we could defend (a measured error, an alternative source, a published range). They are not confidence intervals.
* Wool, milk and feedlot grain placeholders (SCOPE.md B12) are not varied; they enter through the livestock rows and are one of the data items we are waiting for.
