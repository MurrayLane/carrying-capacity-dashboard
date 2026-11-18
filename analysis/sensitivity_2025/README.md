<!-- generated: analysis/sensitivity_2025/write_readme.py -->
# Sensitivity of the 2025 result to its uncertain choices

A sensitivity run is the model run again with ONE uncertain choice changed and everything else left as it is, to see how far the answer moves.
The base is release `2025-organic`: Australia **48.3 million people** in the short term, **12.4 million** in the long term (2011: 40.5 and 9.4 million).
39 variants; `results.csv` has every figure (Australia and the seven state zones, both settings). Reproduce:
`python3 analysis/sensitivity_2025/build_variants.py WORK_DIR ABS_DIR` (runs the two yield scripts with each alternative, needs the ABS files of `analysis/recent_data/fetch_recent.py`), then
`node analysis/sensitivity_2025/evaluate.mjs WORK_DIR/variants.json analysis/sensitivity_2025/results.csv` (needs `cd web && node scripts/build-data.mjs` first), then this script.

## What it shows

* **Direction holds one change at a time.** Every single variant stays above 2011: the lowest short-term figure is 43.6 million (diet back at 2011 shares) against 40.5, the lowest long-term 10.7 million (no group trend) against 9.4.
  **Two pessimistic choices together do not hold it in the short term:** the early meat window with both diet shares at 2011 gives 39.7 million, below 2011's 40.5 (`results.csv`, group `combination`; the long term for the same choices is 12.4).
  Against 2011 (40.5 and 9.4 million) the base is +19% short term and +31% long term; across the defensible single choices (land raster excluded) and the two combinations the range is -2% to +38% short term and +9% to +39% long term.
* **Short term turns on meat, not crops.** The diet shares and the meat window move it 6% to 15%; every crop choice moves it under 0.3%. Reason: red meat is most of the land in today's diet, so the pasture and the meat yields decide the answer.
  The red-meat share (a proxy from FAO food balance sheets, 64% to 57.8%) is the most consequential single default: five points either way is about 6%.
* **Long term turns on the crop factors.** The long-term diet (7.5% meat and eggs, 100% organic, no avoidable waste) is cropping-land limited. Letting the crops the ABS no longer reports keep their 2011 yields costs 13.9%; the field-crop group factor's measured error (14%) moves it 6%;
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
| meat window | meat and herd data of 2024-25 only | +15.7% | +0.0% | 13% |
| group trend | crops the ABS no longer reports keep their 2011 yields (factor 1.0) | -0.2% | -13.9% | 4% |
| diet and consumption | both diet shares at 2011 (13% and 64%) | -9.6% | +0.0% | 9% |
| meat window | meat and herd data of 2020-21 to 2022-23 only (before the heavy slaughter) | -8.6% | -0.1% | 8% |
| meat window | ABS meat tables not calibrated to the archive (cattle x1.0 instead of x1.086, sheep x1.0 instead of x1.155) | -7.0% | +0.0% | 7% |
| diet and consumption | red meat share back at 64% (no change since 2011) | -7.0% | +0.0% | 6% |
| meat window | meat and herd data of 2022-23 to 2024-25 only (three years, the years of heavy slaughter) | +6.6% | +0.1% | 7% |
| group trend | field-crop factor 14% lower (the measured error of the rule) | -0.1% | -6.6% | 1% |
| diet and consumption | red meat share 52.8% (5 points below the proxy) | +6.4% | +0.0% | 6% |
| diet and consumption | red meat share 62.8% (5 points above the proxy) | -5.7% | +0.0% | 5% |
| group trend | field-crop factor 14% higher | +0.1% | +5.6% | 1% |
| group trend | vegetable, fruit and nut factors 20% lower (the measured error of the rule is 20 to 22%) | -0.1% | -4.3% | 8% |
| crop window | crop data of 2024-25 only | +0.0% | -3.8% | 1% |
| organic | default organic factor 0.771 (lower end of Ponisio et al. 2015) on the 119 rows that use it | +0.0% | -3.3% | 0% |
| organic | default organic factor 0.845 (upper end of Ponisio et al. 2015) | +0.0% | +3.2% | 0% |
| group trend | vegetable, fruit and nut factors 20% higher | +0.1% | +3.1% | 6% |
| diet and consumption | meat and egg share back at 13% (no change since 2011) | -2.7% | +0.0% | 3% |
| group trend | field-crop factor from 2016-21 (1.29) instead of 2022-25 (1.36) | -0.0% | -2.2% | 0% |
| crop window | crop data of 2022-23 only | +0.0% | +2.0% | 2% |
| diet and consumption | meat and egg share 11.5% (one step below the proxy) | +1.4% | +0.0% | 1% |
| diet and consumption | meat and egg share 12.5% (one step above the proxy) | -1.4% | +0.0% | 1% |
| organic | organic default share 2% and baseline 2% (no change since 2011) | +0.0% | -1.3% | 0% |
| organic | organic baseline left at 2% (the constant in Yield!E2 not moved) with the 7% default | -1.0% | -1.3% | 1% |
| organic | organic default share and baseline 12% (the share of agricultural land the 2026 report gives) | +0.0% | +1.3% | 0% |
| crop window | drop the record year 2022-23 (mean of 2023-24 and 2024-25) | -0.0% | -1.2% | 1% |
| crop window | crop data of 2023-24 only (the poor year) | -0.1% | +1.0% | 2% |
| meat window | meat and herd data of a full herd cycle or longer (2010-11 to 2024-25) | +0.9% | +0.1% | 4% |
| organic | organic factors of the five crops at the commercial ratios of Kniss et al. alone | +0.0% | -0.9% | 0% |
| meat window | meat and herd data of a full herd cycle or longer (2017-18 to 2024-25) | +0.9% | -0.0% | 4% |
| organic | organic factors of the five crops back at 2011 values | +0.0% | +0.7% | 0% |
| meat window | meat and herd data of a full herd cycle or longer (2015-16 to 2024-25) | +0.6% | +0.0% | 4% |
| diet and consumption | fuel, biofuel and timber at 2011 values (2520 L, 0.5%, 1 m3) | -0.3% | +0.0% | 13% |
| meat window | meat and herd data of a full herd cycle or longer (2005-06 to 2024-25) | -0.1% | +0.2% | 8% |
| crop rules | strict rules: remove zone yields over 2 or under 0.2 times the national yield | +0.0% | +0.0% | 2% |
| crop rules | no plausibility cap or floor (only the 10 ha, 10 t and seed rules) | +0.0% | +0.0% | 2% |
| land | reserve = classes 1.1 and 1.2.5 (conservation and Indigenous uses) | +0.0% | +0.0% | 0% |
| land | reserve = class 1.1 only (nature conservation) | +0.0% | +0.0% | 0% |
| land | infrastructure measured on the raster (classes 5.3 to 5.7, 5.9) instead of 730 m2 a person | +0.0% | +0.0% | 0% |

## Ranges from random draws (SCOPE.md E8)

The single changes above are combined: ten uncertain choices are drawn together, 2,000 times in this three-window run (the all-zones runs behind `results/ranges_<release>.csv` draw thirteen) (`monte_carlo.mjs`; draws in `monte_carlo_draws.csv`, summary in `monte_carlo_summary.csv`). The ranges drawn are listed at the top of `monte_carlo.mjs`. Reproduce: `node analysis/sensitivity_2025/monte_carlo.mjs WORK_DIR analysis/sensitivity_2025/monte_carlo_draws.csv 2000`, then `python3 analysis/sensitivity_2025/summarise_mc.py`.

2000 random draws (Latin hypercube) of the 10 uncertain choices. Capacity in millions of people; the 90% range is the 5th to the 95th percentile of the draws.

| Zone | Short term: median | 90% range | base | Long term: median | 90% range | base |
|---|---|---|---|---|---|---|
| Australia | 48.1 | 42.5 to 52.9 | 48.3 | 12.3 | 11.4 to 13.3 | 12.4 |
| NSW and ACT | 12.14 | 10.82 to 13.34 | 12.20 | 2.12 | 1.96 to 2.30 | 2.14 |
| Victoria | 6.68 | 6.35 to 6.96 | 6.73 | 0.82 | 0.75 to 0.89 | 0.82 |
| Queensland | 8.58 | 8.07 to 9.10 | 8.88 | 0.74 | 0.68 to 0.81 | 0.75 |
| South Australia | 2.28 | 2.13 to 2.41 | 2.29 | 0.85 | 0.80 to 0.89 | 0.85 |
| Western Australia | 3.45 | 3.24 to 3.63 | 3.46 | 1.79 | 1.71 to 1.87 | 1.79 |
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

The 10 choices alone explain 102% of the short-term and 100% of the long-term variance; the rest is interaction.

How to read it:

* **Australia: short term 48.1 million (90% range 42.5 to 52.9); long term 12.3 million (11.4 to 13.3).** The 5th percentile of both is above 2011's 40.5 and 9.4 million; the short-term lower end is above it, but not by much.
* **The short term is set by one judgement.** The window of herd and meat data explains most of the spread, and it is a three-way choice with equal chances that I made (the five-year base window, the early three years, the late three years). Different chances would give a different range. The red-meat share is next.
* **The long term is set by the crop factors:** the field-crop group factor, then the vegetable, fruit and nut factors, then the organic yield factor.
* **The base case sits slightly above the middle** of the short-term draws because the pessimistic choices (early meat window, lower red-meat share) pull further than the optimistic ones.
* **What the ranges leave out:** the land source (a method choice, above), the crop years (E10), the error of thin-zone yields (E9), the calibration of the ABS meat tables, and the wool, milk and feedlot placeholders. The ranges are what we can defend, not confidence intervals.
* **With only full-cycle meat windows the short-term range narrows.** The first run includes two three-year windows (the early and the late years of the herd cycle), which is what makes the short-term range wide. Repeating the draws with the meat window chosen from the base window and four windows of 8, 10, 15 and 20 years (`monte_carlo_draws_longwindow.csv`, `MC_WIN_DIR=WIN_DIR node monte_carlo.mjs ...`, WIN_DIR made as in the note on fault X069 below), Australia's short term is 48.4 million (46.0 to 50.8), against 48.1 (42.5 to 52.9); the long term is 12.3 (11.4 to 13.3), against 12.3 (11.4 to 13.3). A window that covers the herd cycle is the better basis for a published range, and the red-meat share is then the main short-term uncertainty. Northern Territory figures stay unreliable (0.01 to 0.06 million).
* The additive shortcut the draws use (group factors and meat window added to the base yield matrix) reproduced two full re-runs at the corners of the ranges to the unit.

## Limits

* Changes are made one at a time, apart from the two combinations at the foot of `results.csv`: early meat window with 2011 diet shares (short term 39.7 million) and no group trend with the low organic factor (long term 10.3 million, against 9.4). Other pairs are not the sum of their parts.
* The ranges are the ones we could defend (a measured error, an alternative source, a published range). They are not confidence intervals.
* Wool, milk and feedlot grain placeholders (SCOPE.md B12) are not varied; they enter through the livestock rows and are one of the data items we are waiting for.
<!-- end generated -->

## Monte Carlo on the tip cells (2026-10-28)

The same 1,000 draws (`monte_carlo.mjs` with `MC_RELEASE`) on `2025-mirror` (the thesis method on the 2025 data) and `2025-improved` (the improved method): `monte_carlo_2025-mirror.md`, `monte_carlo_2025-improved.md` and the summaries in `results/ranges_*.csv`. Australia, millions of people, 90% range:

| | Short term | Long term |
|---|---|---|
| 2011 (no range) | 40.5 | 9.4 |
| 2025, thesis method | 42.3 to 52.6 (base 48.0) | 13.0 to 15.1 (base 14.1) |
| 2025, improved method | 41.9 to 52.0 (base 47.5) | 11.2 to 12.9 (base 12.0) |

The 2011 figure lies below the whole short-term range of both cells and the long-term ranges are far above it. The short-term spread is the meat window (81% of the variance in the improved cell) and the red meat share (16%); the long-term spread is the field-crop group factor (54%), the vegetable, fruit and nut factors (24%) and the organic yield factor (22%). The long-term ranges understate the uncertainty because resilience, fuel, the recycling uptake and the law are not sampled, and the 2011 base has uncertainties of its own that were not sampled either.

## A quick range for the dashboard (2026-10-28)

The Monte Carlo is for the papers. For a dashboard that recalculates on every slider move it is too slow (1,000 draws), so `rss_check.py` tests a quick range: each of the ten choices is run alone over its range (28 runs in all, `monte_carlo.mjs ... oat`), the response of each is taken as piecewise linear between those runs, its mean and variance are taken under the choice's own distribution, the effects are added and the variances combined in quadrature, and the 90% range is the mean plus and minus 1.645 standard deviations. This is sound because the ten choices act almost separately (their first-order shares add to 101% and 104% of the variance).
Result, `quick_range_<release>.csv`: against the Monte Carlo 90% range, the width of the quick range is within 5% for Australia and the states (0.98 to 1.05; the Northern Territory, short term, 1.11), and the ends agree to within about 1% for Australia, for both 2025-mirror and 2025-improved. The short-term meat window has only three values, so the quick range is slightly too narrow at the lower end (Australia, short term: 41.9 against 42.3 million). 28 runs take about a second.
Limits: it carries the same ten choices as the Monte Carlo and nothing else, and it assumes a sum of separate effects; if more choices are added they join the 28 runs (two runs each).

## With the long-term choices and all 60 zones (2026-10-28)

The Monte Carlo (`MC_LONG=1 MC_ZONES=all`, 1,000 draws each, `monte_carlo_2025-mirror_all.md`, `monte_carlo_2025-improved_all.md`) now also draws three long-term choices: the resilience table (all years or leave-one-out), the long-term liquid fuel (156 to 253 L, triangular on the 210 L re-derivation) and the feeding benchmark of the improved method (30% to 52.5% of each stage). The law, the grain store and the time frame are scenario switches and are not drawn. Australia, millions of people, 90% range:

| | Short term | Long term |
|---|---|---|
| 2011 (no range) | 40.5 | 9.4 |
| 2025, thesis method | 42.3 to 52.6 (base 48.0) | 11.7 to 15.9 (base 14.1) |
| 2025, improved method | 41.9 to 52.0 (base 47.5) | 10.1 to 13.5 (base 12.0) |

The long-term range widens (11.2 to 12.9 with the first ten choices for the improved method) and its main driver is now the long-term liquid fuel (46% of the variance for the improved method, 49% for the thesis method), then the resilience table (26% and 23%) and the field-crop group factor (14%); the feeding benchmark explains under 1%. The one remaining open question for the long term is therefore fuel, not crops. The long-term base lies in the upper half of the improved range (12.0 against a median of 11.5) because 210 L is below the middle of the fuel range.
**The quick range agrees with the Monte Carlo across all zones**: the ratio of the widths is 0.95 to 1.09 (median 1.03) for the 45 zone and setting combinations of the thesis cell and 0.96 to 1.08 (median 1.04) for the 40 of the improved cell with a capacity over 300,000 people. `results/likely_range_<release>.csv` has the quick range and the over, under or uncertain class of every zone at the defaults.

## After the two corrections: the corrected and improved cells (2026-10-28)

The Monte Carlo (thirteen choices sampled, twelve varying in the 2025 releases, because the long-term benchmark has no effect there; 1,000 draws, all 60 zones) was run again on the cells that include the biodiesel and beef corrections (`monte_carlo_2025-fixed_all.md`, `monte_carlo_2025-improved_all.md`, `results/ranges_*.csv`). Australia, millions of people, 90% range:

| | Short term | Long term |
|---|---|---|
| 2011, corrected (no range) | 33.3 | 15.35 |
| 2025, corrected | 34.7 to 43.5 (base 39.5) | 13.6 to 16.8 (base 15.9) |
| 2025, improved | 34.4 to 43.1 (base 39.2) | 12.7 to 15.7 (base 14.9) |

Re-run after the loss-factor module `loss-factors-australia` joined the improved tier (SCOPE E4; `monte_carlo_2025-improved_all.md`): 2025, improved **35.0 to 43.8 short term (base 39.9) and 12.7 to 15.7 long term (base 14.9)**. The short-term range moves up by 0.6 million with the base; the long term is unchanged because the long-term default has no avoidable waste. The drivers are as above; the quick range agrees with the Monte Carlo (width ratio 0.94 to 1.26, median 1.02, over 41 zone and setting combinations).

* **The short-term increase since 2011 holds**: 2011's 33.3 million lies below the 5th percentile of both 2025 ranges.
* **The long-term increase does not**: 2011's 15.35 million lies inside both long-term ranges, so on the corrected method the long-term change is within the uncertainty.
* **What drives the spread has changed.** Short term: the herd and meat data window (80%) and the red meat share (17%), as before. Long term: the resilience table (53% of the variance), the herd and meat window (35%, because beef now matters more) and the organic yield factor (8%); the long-term liquid fuel, half the long-term variance before the biodiesel correction, now explains 1%.
* **The quick range still agrees**: the ratio of its width to the Monte Carlo's is 0.94 to 1.18 (median 1.03) across the zones with a capacity over 300,000 people, for both cells.

## Full Monte Carlo on the settled data (rerun 2026-11-07; supersedes the 2026-10-28 ranges above)

**Note, 2026-11-07.** The 2026-11-04 ranges were replaced because of fault X054 (section below): the 1,000 draws were run again on variant matrices rebuilt on the current base. The tables and the list of drivers that follow are the rerun. The 2026-11-04 figures were 42.8 to 53.1 and 11.7 to 15.8 (thesis method), 35.9 to 45.1 and 14.3 to 17.8 (corrected), 46.8 to 61.3 and 16.4 to 20.4 (improved); do not quote them.

1,000 Latin hypercube draws of the 13 sampled choices over all 60 zones (twelve vary in the corrected and published releases: the long-term benchmark, lbench, has no effect there, because the model has no Settings!BQ4:BQ7 cells and its influence is 0 in every zone; in the improved release the benchmark carries about 1% of the variance, up to 0.012 in 101 of 120 zone rows), run on the releases as they now stand (after the 2011 population correction, the dairy-good-land module, the organic-ruminant factor, the regional beef output and the source-trace work). `monte_carlo_<release>_all.md`, `_summary.csv` (copied to `results/ranges_<release>.csv`), draws in `monte_carlo_draws_<release>_all.csv`; the quick range was regenerated (`oat_<release>_all.csv`, `quick_range_<release>_all.csv`, `results/likely_range_2025-improved.csv`).

**Range ends that are the author's judgement.** Five ends of the ranges have no outside source: (1) the meat-window three-way choice, with equal chances; (2) the meat-and-egg low end, 0.115, one step below the proxy; (3) the red-meat low end, 0.528, five points below the proxy; (4) the 50/50 weight on the leave-one-out resilience table; (5) the long-term benchmark low end, 0.30, which has no effect in 2025. The other ends are sourced: Ponisio et al. 2015; the 2011 values; the measured errors of the group-trend rule; the 2026 organic report; the light-vehicle and thesis fuel figures.

**A fault in the earlier improved-cell ranges was found and fixed first.** The draws rebuilt every yield from the yield matrix and set the organic factor of every cell that is at the workbook default. In the improved cell that overwrote two things the release sets itself: the observed dairy milk yields of `dairy-good-land` (row 97) and the 0.9 organic factor of the ruminants (G95, G96, G98). The base of the draws was 21.2 million short term and 6.2 long term against the release's 53.6 and 18.5. `monte_carlo.mjs` now leaves a yield row or organic cell alone when the release has set it, and the base of the draws equals the release in all 120 zone-and-setting results of the mirror, corrected and improved cells (checked to the person). Mirror and corrected were never affected, and their quick-range files are identical to those committed before.

Australia, millions of people, 90% range (5th to 95th percentile), against the 2011 cell of the same method (no range: its inputs were not sampled):

| Cell | 2011 (short, long) | 2025 short term | 2025 long term |
|---|---|---|---|
| Thesis method (mirror) | 40.45, 9.43 | 43.4 to 54.3 (base 49.4) | 11.8 to 16.0 (base 14.1) |
| Corrected | 33.31, 15.35 | 36.3 to 45.8 (base 41.5) | 13.4 to 16.5 (base 15.6) |
| Improved | 41.69, 13.06 | 46.2 to 60.1 (base 53.6) | 15.9 to 19.4 (base 18.5) |

* **The short-term increase since 2011 holds in all three cells**: 2011 lies below the 5th percentile of the 2025 range each time.
* **The long-term increase holds in the thesis-method and improved cells and does not hold in the corrected cell**: 2011-fixed (15.35) lies inside the corrected 2025 range (13.4 to 16.5), as before; the improved 2011 (13.06) and the thesis-method 2011 (9.43) lie below their 2025 ranges.
* **What drives the spread** (share of the variance of Australia's capacity). Short term, in every cell: the window of herd and meat data (79% to 82%) and the red meat share (15% to 17%), as before. Long term, improved: the resilience table (55%), the window of herd and meat data (29%), the long-term liquid fuel (5%), the vegetable, fruit and nut factors (2%). Long term, corrected: the resilience table (52%) and the meat window (36%), the organic yield factor (9%). Long term, thesis method: the long-term liquid fuel (48%), the resilience table (24%), the field-crop factor (14%), the vegetable, fruit and nut factors (5%). The long-term drivers of the improved cell changed with the rerun: the fuel, vegetable and field-crop shares of the 2026-11-04 run came from the offset of X054.
* **The quick range still agrees with the Monte Carlo**: the ratio of its width to the Monte Carlo's, over the zones with a capacity above 300,000 people, is 0.93 to 1.10 (median 1.02) for the improved cell (46 zone and setting combinations), 0.94 to 1.23 (1.03) for the corrected (44) and 0.94 to 1.10 (1.04) for the thesis method (43); recomputed 2026-11-07 from `results/likely_range_<release>.csv` against `results/ranges_<release>.csv`. The quick range for Australia is 35.9 to 45.8 and 13.3 to 16.5 (corrected), 43.0 to 54.3 and 11.6 to 15.7 (thesis), 45.5 to 59.8 and 15.6 to 19.3 (improved).
* **The improved cell's range is wide at the top** (46.2 to 60.1 million short term) because the improved base sits near the upper end of the meat-window choices; the base (53.6) is close to the median (53.3). In the corrected long term the base (15.6) sits in the upper part of the range (median 14.8).

## Fault X054: the group factors and meat windows carried an offset (found after the 2026-11-04 ranges)

**Cause.** The draws add the field-crop and vegetable, fruit and nut factors, and the two short meat windows, as differences between matrices in the `build_variants.py` work folder and the base matrix `data/2025/yield_matrix_livestock.csv`. The work folder used for every range above was built before `livestock_zone.py` changed its wool, dairy milk and feedlot grain inputs from placeholders to the series in `data/2025/livestock_national_series.csv`. Its crop rows match the current base; three animal rows do not: sheep wool (row 96, 15% to 18% higher in 50 zones), dairy milk (row 97, 16% lower to 17% higher in 55 zones, by state) and cattle meat (row 98, up to 4% higher in 52 zones). In 2025-improved the dairy row is set by the release and takes no difference, so only wool and cattle meat applied there. Every one of its group-factor and meat-window matrices carries that same difference. The draws added it in proportion to the size of the factor, so a factor of -1 and of +1 moved capacity the same way (Rangelands WA, short term, -8.4% and -8.0% for the field-crop factor), and both short meat windows lowered Rangelands.

**Fix.** The work folder is rebuilt on the current base with the same `yield_variant` calls as `build_variants.py` (the ABS files are those of `analysis/recent_data/fetch_recent.py`; a run with no change reproduces `data/2025` byte for byte). The arithmetic of the draws is unchanged: with matrices built on the current base it is the linear shortcut it was meant to be. `monte_carlo.mjs` now checks the work folder before drawing: the yields are linear in a group factor and the lo and hi matrices lie the same distance either side of it, so their mean must equal the base matrix; if it does not, the script stops and asks for a rebuild. The meat windows come from the same `livestock_zone.py` run, so a folder that passes this check has meat windows on the current base too.

**Check, 2025-fixed, one choice at a time.** After the rebuild, -1 and +1 move capacity in opposite directions for every zone: the part that moves the same way at both ends is under 1% in all 120 zone-and-setting results for both factors (before: over 1% in 57 for the field-crop factor and 70 for the vegetable, fruit and nut factors; largest 9.8%). Rangelands WA, short term: field crops -0.2% and +0.2%, vegetables, fruit and nuts -1.8% and +1.2%. Australia, long term: -0.3% and +0.2% (before +4.4% and +4.9%). The early and three-year meat windows now move Rangelands -4.5% and +2.8% short term (before -10.7% and -7.2%).

**Trial range, 2025-fixed, 200 draws** (a trial, not for quoting; the 1,000-draw rerun replaces it): Australia short term 36.4 to 45.9 million (base 41.5), long term 13.3 to 16.4 million (base 15.6); against 35.9 to 45.1 and 14.3 to 17.8 above. The same 200 draws on the old work folder give 35.9 to 45.2 and 14.3 to 17.6, so the shift comes from the fix, not from the smaller number of draws. The long-term range moves down by about one million because the offset was raising it by about 4.6% for each group factor. No zone's base now lies outside its own range (before: Western NSW short term, Rangelands short and long term). The quick range from the rebuilt one-at-a-time runs gives 35.9 to 45.8 and 13.3 to 16.5.

The 1,000-draw rerun was made on 2026-11-07 on the rebuilt work folder (`monte_carlo_<release>_all.md`, `results/ranges_<release>.csv`). Its Australia figures are the table in the section above; the ranges drawn with the old work folder (2026-11-04 and earlier) are superseded.

## Fault X069: the full-cycle meat windows carried the X054 offset (long-window range rebuilt 2026-11-07)

**Cause.** The long-window run (`MC_WIN_DIR`, `monte_carlo_longwindow.md`) drew its four full-cycle windows (8, 10, 15 and 20 years) from a folder built with the placeholders for wool, cattle feedlot grain and milk: the folder is byte for byte what the current `livestock_zone.py` gives with `LS_SERIES=off`. Against the current base matrix every one of its windows therefore carried the same difference as the X054 work folder (sheep wool row 96, dairy milk row 97, cattle meat row 98, up to 17.7%, 17.4% and 4.1%), added to every draw that took a full-cycle window. The X054 check covered the group factors and the two short windows, not `MC_WIN_DIR`.

**Why the windows are not a direct rebuild.** The `yield_variant` calls of `build_variants.py` for these windows fail on the current base: `data/2025/livestock_national_series.csv` has wool, cattle on feed and state milk figures for 2009-10 and 2020-21 to 2024-25 only, and the windows need 2005-06 to 2019-20. Without those years (they are not ABS series), each window is built as the base matrix plus the change from the base window to that window, both made with `LS_SERIES=off` in one run, so the placeholder difference cancels. Sheep meat, chicken, duck, turkey, eggs and pig meat (rows 95, 99 to 103) are then exactly what a direct build gives; for wool, milk and cattle meat the change between windows follows the flock and the herds instead of the series. Tried on the two short windows, where a direct build exists, this gives the direct yields to within 1.6% for wool and cattle meat and 6.5% for milk, in every zone. Rebuild (repository root): `python3 -I analysis/sensitivity_2025/rebuild_off.py OFF_DIR ABS_DIR`, then `python3 -I analysis/sensitivity_2025/make_win.py OFF_DIR WIN_DIR`, then `MC_WIN_DIR=WIN_DIR node analysis/sensitivity_2025/monte_carlo.mjs WORK_DIR analysis/sensitivity_2025/monte_carlo_draws_longwindow.csv 2000`.

**Check.** `monte_carlo.mjs` now checks an `MC_WIN_DIR` folder before drawing: it must hold `base_window`, the base years built in the same run, equal to the base matrix in every row, and each window may differ from the base matrix only in rows 95 to 103. The old folder is refused (no `base_window`; with the base window of its own construction, rows 96, 97 and 98 differ in 50, 55 and 52 zones); the rebuilt folder passes. The old and rebuilt windows differ only in rows 96 to 98, and by exactly the placeholder difference.

**Rerun** (2,000 draws, `2025-organic`, the eight state zones, with the group factors of the rebuilt X054 work folder): Australia short term 46.0 to 50.8 million (median 48.4), long term 11.4 to 13.3 million (median 12.3); the old run gave 45.8 to 50.5 (48.1) and 11.4 to 13.2 (12.2). Most of the short-term shift comes from the windows (the rebuilt group factors with the old windows give 45.8 to 50.5); the long-term shift of about 0.1 million comes from the group factors. The three-window run (42.3 to 52.5 and 11.4 to 13.2) was made with the X054 work folder and was rerun on the rebuilt work folder under X088 below, which gives 42.5 to 52.9 and 11.4 to 13.3; those are the figures to quote. The base column of the long-window files (`monte_carlo_longwindow_summary.csv` and `monte_carlo_longwindow.md`) reads 48.0 and 12.3, the base of the first `results.csv`, and was not regenerated; the release gives 48.3 and 12.4 at the base values.

## Fault X088: the single-choice table and the three-window range were made on the old base

**Cause.** `results.csv` and the three-window range (`monte_carlo_draws.csv`, `monte_carlo_summary.csv`, `monte_carlo.md`) were made with the X054 work folder and before the release reached its current base, so they read 48.0 and 12.3 million at the base where the release gives 48.3 and 12.4, and the three-window range carried the X054 offset. The 8-year meat window was also labelled 2018-19 to 2024-25; it covers 2017-18 to 2024-25.

**What was rerun.** (1) The single-choice table: every variant rebuilt with `build_variants.py` on the current base (a build with no change reproduces `data/2025` byte for byte), then `evaluate.mjs`. The four full-cycle meat windows (8, 10, 15 and 20 years) cannot be built directly, because `data/2025/livestock_national_series.csv` has no wool, cattle on feed or state milk figures for 2010-11 to 2019-20 (`livestock_zone.py` stops on the first missing year); their rows are evaluated on the rebuilt X069 window folder (`rebuild_off.py`, `make_win.py`, which passes the `MC_WIN_DIR` check). (2) The three-window range: 2,000 draws with the same seed and draw count as the first run, on the rebuilt X054 work folder (which passes the check in `monte_carlo.mjs`), then `summarise_mc.py`. (3) `write_readme.py`, which rewrote only its own section.

**Result.** The base reads 48.3 and 12.4 million. No row of the ranking table moves by more than 0.5 points; the largest move is the 2024-25 meat window, +15.4% to +15.7% short term. Australia's 90% range is 42.5 to 52.9 million short term (was 42.3 to 52.5) and 11.4 to 13.3 long term (was 11.4 to 13.2), the figures the X069 note gave as a trial; the shares of the variance are unchanged. These ranges replace the trial figures in the X069 note. The papers quote the all-zones ranges (`results/ranges_<release>.csv`), not these, so no figure in the claims register changes.

## The widened Monte Carlo and the rule separating definitions from settings (B115, decision 108)

### The rule

**A definition is a choice that changes what the number means.** What is counted (exports or not), the unit of self-sufficiency (the nation, the states, regions), the time frame (the short-term or the long-term settings, each a bundle), the diet standard (the observed diet, a guideline diet, an optimised diet) and the weather the capacity is for (an average year or the worst year in N) are definitions. Published methods differ on them, and each answers a different question. A definition is reported as a separate reading (Table 6 of Paper B, `analysis/method_tests_2025/design_choices.csv`); it is never drawn.

**A setting is a choice of value within one meaning:** a loss factor, a yield window, a calibration, a measured share, a requirement. A setting is drawn over the range its sources give. Where no source gives an end or a weight, the end or weight is the author's judgement and is said to be.

### Every sampled choice (19; 18 vary on this release)

The corrected 2025 release (`2025-fixed`), national, both presets. The first 13 are the choices of the existing runs, unchanged; the last six are added (`MC_WIDE=1`).

| Choice | What is drawn | Range and distribution | Source of the range | Preset |
|---|---|---|---|---|
| sf | field-crop group factor | uniform, 14% below to 14% above | the measured error of the group-trend rule (this README) | both |
| sh | vegetable, fruit and nut factors | uniform, 20% below to 20% above | the measured error of the rule (20 to 22%) | both |
| meat | window of herd and meat data | 2020-21 to 2024-25, 2020-21 to 2022-23, 2022-23 to 2024-25, equal chances | ABS herd and meat series; equal chances author judgement | both |
| meategg | meat and egg share of the diet | triangular 0.115, 0.12, 0.13 | FAO food balance proxy and the 2011 value; low end author judgement | short |
| redmeat | red meat share | triangular 0.528, 0.578, 0.64 | FAO food balance proxy and the 2011 value; low end author judgement | short |
| fuel | liquid fuel per person | uniform 2,360 to 2,520 L | proxy and 2011 value | short |
| biofuel | biofuel share | uniform 0.23% to 0.5% | proxy and 2011 value | short |
| timber | timber per person | uniform 0.8 to 1.0 m3 | proxy and 2011 value | short |
| orgfac | default organic yield factor | uniform 0.771 to 0.845 | Ponisio et al. 2015 | both |
| orgshare | organic share of land | triangular 0.02, 0.07, 0.12 | 2011 value, proxy, Australian Organic Market Report 2026 | both |
| restable | resilience table | all years or leave-one-out, equal chances | equal chances author judgement | long |
| lfuel | long-term liquid fuel | triangular 156, 210, 253 L | light vehicles electrified, the re-derivation, the thesis | long |
| lbench | long-term feeding benchmark | triangular 0.30, 0.40, 0.525 | South Korea and Japan; not drawn in this release (no Settings!BQ4:BQ7): fixed at 0.4 in every row of the draws file, so 18 of the 19 choices vary | long |
| **waste** | avoidable waste | uniform 12% to 14% | `analysis/waste_2025/README.md`: the FIAL 2021 baseline (312 kg a person, 58% at the retail and consumer stages, 70% edible) over the FAO supply allows "roughly 12 to 14%" | short (the long-term 0% is the time frame's) |
| **lossaus** | retail and consumer loss factors | uniform weight 0 to 1 between the thesis's US factors and the Australian factors of `methods/loss-factors-australia` (each of its 474 Base!G and Base!I cells set to US + weight x (Australian - US)) | Buzby 2010 and Muth 2011 (US); FIAL 2021 Table 5 and the Burnside bin audit 2022 (Australia); the uniform weight between the two sets is the author's judgement (no source gives a weight) | short (the factors scale with avoidable waste, 0 in the long term) |
| **land** | source of cropping and pasture areas | ABS holdings (the release) or the ABARES land-use raster (`build_variants.py` variant `land_raster`), equal chances | the two sources; equal chances author judgement | both |
| **meatcal** | calibration of the ABS meat tables | uniform weight 0 to 1 between the ABS tables as published (variant `meat_nocal`) and the archive's 2010 level (cattle x1.086, sheep and lamb x1.155, the release); the sheep and cattle meat yields are scaled in proportion, after the meat window | ABS Livestock Products (7215.0) against the thesis archive: the archive is above ABS in every year 2006 to 2010 (cattle by 4.6% to 8.6%, sheep and lamb by 12.4% to 16.9%); the uniform weight between the two calibrations is the author's judgement | both |
| **energy** | energy requirement per person | the sedentary NHMRC diet times a food amount (Settings!B9) uniform 1.000 to 1.286, which is PAL 1.4 (sedentary, the release) to PAL 1.8 (moderate activity); this is a part of the NHMRC range, PAL 1.2 to 2.2 (Table 3 note b), and the upper end is the author's judgement of which part applies | NHMRC Nutrient Reference Values, dietary energy, Tables 3 and 4 and the text after them ("from sedentary ... to moderate activity"); the model's moderate diet has 1.31 times the sedentary diet's energy, and food amount 1.31 gives within 3% of the moderate diet's capacity | short (the long-term high activity is the time frame's) |
| **trendwin** | window of the field-crop group trend | uniform between the 2022-25 factor (1.356, the release) and the 2016-21 factor (1.289) | `data/abs-2022-25/group_trend.json` (SCOPE.md B10 rule on two windows); variant `gt_field_2016` | both |

### Every choice not sampled, with the reason

| Choice | Kind | Why it is not drawn |
|---|---|---|
| Exports counted | definition | The model is self-sufficient by design; exports are compared with external counts (Table 6, panel of comparisons). |
| Unit of self-sufficiency (nation, states, NRM regions, SA4, SA3, SA2) | definition | Each unit answers a different question; this run is national. |
| Time frame (short-term against long-term settings, with the long-term diet of 7.5% meat and eggs and 50% red meat, 100% organic, no avoidable waste, high activity, 100% recycling, a 30% reserve) | definition | A bundle that defines the scenario; each preset is drawn within itself. |
| Diet standard (guideline diets at other meat shares; optimised diets A, B and C) | definition | Alternative diets change what is being fed. The observed diet's composition is a setting and is drawn (meategg, redmeat), and so is the energy requirement (energy). |
| Drought allowance (an average year against the worst year in 5 to 100) | definition | It sets which year the capacity is for. The long-term resilience table, a setting within it, is drawn (restable). |
| The law (current or adapted), the grain store | definition | Scenario switches, as before. |
| The method corrections (biodiesel-yield, beef-carcase-yield) | neither | Errors against the thesis's own sources, fixed; not uncertain. |
| The improved line as a whole | definition | A bundle of method modules (Table 6, "Australian settings"). Its loss-factor module is a setting and is drawn (lossaus); its other modules are listed next. |
| dairy-good-land (arable improved pasture counted as cropping land; observed farm milk yields) | definition | It changes which land counts as cropping land, as the land-available row of Table 6 does; national effect +10.0 million short term, +0.4 long (`results/method_effects.csv`). |
| reserve-pro-rata | definition | It changes how the reserve is taken from the land types; -0.6 million short term, -0.8 long. |
| recycling-stage | definition | It changes what counts as recycled feed (dry matter, stage, legal limits); in the corrected release short-term recycling is 0%. Its feeding benchmark is drawn where the module applies (improved release). |
| organic-ruminant-factor, regional-beef-output | setting | No effect on the national figure in 2025 (`results/method_effects.csv`); the corrected release's ruminant cells take the default organic factor, which is drawn. |
| Crop data window (E10: single years or the mean of three) | setting | A single year measures weather, which the drought allowance (a definition) carries; the base is the three-year mean. One at a time it moves Australia by under 4%. |
| Crop plausibility rules | setting | Under 0.1% nationally (ranking table). |
| Organic factors of the five crops (2011 values, Kniss et al.) | setting | Under 1% one at a time. |
| Reserve classes, infrastructure measured on the raster, population | setting | No effect on the national figure: the reserve and infrastructure land come from non-agricultural land, which is in surplus nationally. |
| Thin-zone yield error (E9) | setting | A zone-level error; this run is national. |
| Wool, milk and cattle feedlot grain series | setting | Now named series (`data/2025/livestock_national_series.csv`); no second source to set a range. |
| Textiles per person, natural fibre and wool shares, irrigation share | setting | No sourced range: the 2011 textile source is not recorded and current estimates count different things (consumption_2025 README). A gap. |
| Processing, edible-portion and cooking constants of the workbook | setting | Traced in `analysis/constants_audit/`; no sourced alternative ranges were built. A gap. |
| Climate trend in crop yields (Hochman et al. 2017) | neither in this run | The model takes observed yields of 2022-23 to 2024-25, which carry the climate to date; Hochman et al. find water-limited yield potential fell 27% from 1990 to 2015 while actual yields stayed flat. A forward trend is a projection, which belongs to a future time frame, not to a 2025 capacity. |
| FAOSTAT permanent meadows and pastures | not used | The model's land is the ABS holdings or the ABARES raster, both drawn now; FAOSTAT's land class does not enter the model. |
| Pasture productivity | covered | In this model pasture output is national meat shared among zones by dry sheep equivalent, so its uncertainty is the meat window and the meat calibration, both drawn. |
| Nutrient composition of the foods | not examined | The diet is set in serves of food groups (NHMRC food modelling); the composition coefficients were not given ranges in this job. |

### The run

`monte_carlo.mjs` with `MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 MC_ZONES=national` and the `sobol` design: two Latin hypercubes A and B of 2,000 draws of the 19 choices and, for each choice, A with that choice's column from B (Saltelli 2010): 42,000 runs of Australia, short and long term. The range is block A, which is exactly the hypercube the plain draws give for 2,000 draws (the first 13 columns are drawn as in the existing runs, the six new ones after them). `sobol_wide.py` writes the draws (`monte_carlo_draws_2025-fixed_wide.csv`), `results/ranges_2025-fixed_wide.csv` (with the existing 13-choice draws summarised the same way beside them), `sobol_2025-fixed.csv` and `monte_carlo_2025-fixed_wide.md`. `check_wide.py` recomputes the range from the draws. Reproduce (repository root; WORK_DIR the X054 work folder, which must also hold `meat_nocal`, `gt_field_2016` and `variants.json` with `land_raster`, as `build_variants.py` writes them):

    for k in 0 1 2 3; do MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 MC_ZONES=national node analysis/sensitivity_2025/monte_carlo.mjs WORK_DIR P$k.csv sobol 2000 $k 4 & done; wait
    python3 analysis/sensitivity_2025/sobol_wide.py P0.csv P1.csv P2.csv P3.csv

**Estimators.** First order: mean((f(B) - m)(f(AB_j) - f(A))) / V, with m the mean of f over A and B (Saltelli 2010's form with f(B) centred, which has the same expectation and much less noise when the output is far from zero). Total order: mean((f(A) - f(AB_j))^2) / 2V (Jansen 1999). V is the variance over A and B. 95% intervals from 1,000 bootstrap resamples of the draws (seed 20261118). The binned first-order estimate of `summarise_mc.py` on block A is in the last column of `sobol_2025-fixed.csv` as a check; it agrees within about five points (land, short term, 37% binned against 32%).

**Checks.** (1) With none of the new options, the script's output is byte for byte what it was before: the plain draws (30 draws on 2025-organic; 20 draws on 2025-fixed with `MC_LONG=1`), the one-at-a-time runs and a fixed run over all zones were compared with `cmp` against the unmodified script. (2) With `MC_WIDE=1` and every new choice at its base value, the run gives the release, 41,503,537 and 15,623,209. (3) The Australian loss factors at weight 1 give 46,153,962 short term, the same to the person as a model built with the module's cells written in. (4) The shortcuts against full rebuilds through `zone_yields.py` and `livestock_zone.py`: the early meat window uncalibrated, 34,886,229 against 34,886,246 short term and 14,212,980 against 14,212,984 long; the late window uncalibrated, 41,158,354 against 41,158,347; the field-crop factor at +14% and -14% with the 2016-21 trend window, identical to the person. A first version added the calibration as a difference and missed the full rebuild by 1.1%; it scales the meat rows now and the draws were made with that version.

### Result (Australia, millions of people)

| | Short term | Long term |
|---|---|---|
| Existing 13 choices, 1,000 draws: 5th to 95th percentile | 36.3 to 45.8 (factor 1.26) | 13.4 to 16.5 (1.23) |
| Existing 13 choices: min to max | 34.6 to 47.7 (1.38) | 12.9 to 16.9 (1.31) |
| Widened, 19 choices, 2,000 draws: 5th to 95th percentile | 31.1 to 49.2 (1.58) | 13.3 to 18.8 (1.41) |
| Widened: min to max | 26.2 to 58.1 (2.22) | 12.4 to 19.9 (1.60) |
| Widened: median (base of the release) | 39.0 (41.5) | 15.8 (15.6) |

Share of the variance, first order and total order (`sobol_2025-fixed.csv`; choices with under 0.5% in both settings left out):

| Choice | Short: first | Short: total | Long: first | Long: total |
|---|---|---|---|---|
| source of cropping and pasture areas (land) | 32% | 33% | 58% | 56% |
| energy requirement per person (energy) | 27% | 25% | 0% | 0% |
| window of herd and meat data (meat) | 24% | 23% | 14% | 14% |
| resilience table (restable) | 0% | 0% | 20% | 20% |
| retail and consumer loss factors (lossaus) | 6% | 6% | 0% | 0% |
| red meat share (redmeat) | 4% | 5% | 0% | 0% |
| default organic yield factor (orgfac) | 0% | 0% | 4% | 4% |
| calibration of the ABS meat tables (meatcal) | 3% | 3% | 1% | 1% |
| avoidable waste 12% to 14% (waste) | 1% | 1% | 0% | 0% |

* **The range widens.** Short term the 5th to 95th percentile factor goes from 1.26 to 1.58 and the min to max from 1.38 to 2.22; long term from 1.23 to 1.41 and 1.31 to 1.60.
* **The choices still act almost separately.** The first-order shares add to 97% in both settings (the total-order shares add to 96%), and each total-order index is within two points of its first-order index: interactions carry about 3% of the variance.
* **Six choices rest on a judgement, and two weights more.** The meat window, the low end of the meat and egg share, the low end of the red meat share, the weight of the resilience table, the weights of the two land sources and the upper end of the energy range (PAL 1.8, a choice of which part of the NHMRC range of PAL 1.2 to 2.2 applies) are the author's. The uniform weights of the loss factors and of the meat calibration are judgements too: no source gives a weight between two point estimates.
* **Three choices carry four-fifths of the short-term variance, and all three rest on a judgement:** the land source (an equal-chance choice between two sources), the energy requirement (its upper end, PAL 1.8, describes a moderately active population) and the meat window (equal chances). The long term is the land source, the resilience table (equal chances) and the meat window.
* **The base no longer sits in the middle.** Five of the six new choices have the release at one end of their range (US loss factors, calibrated meat, sedentary requirement, the 2022-25 trend, and avoidable waste at 12%, the low end of 12% to 14%), so the short-term median (39.0) is below the base (41.5).
* **Conditional readings from the same draws.** Holdings land only (1,000 draws): short term 29.8 to 43.1 (1.45), long term 13.0 to 16.2 (1.24). Raster only: 35.6 to 51.2 (1.44) and 15.3 to 19.1 (1.25).
* **Against 2011.** The corrected 2011 figures (33.3 short term, 15.35 long term; not sampled) both lie inside the widened 2025 ranges; on the existing range 33.3 lay below the short-term 5th percentile.
* **Against the definitions** (`design_choices.csv`): the widened 5th to 95th factor (1.58) is above avoidable waste (1.33) and the land available (1.09), and below the guideline diets (2.14), the drought allowance (2.19), the exports counted (2.41 to 6.36), the time frame (2.66) and the unit (2.67). The min to max factor (2.22) is above the guideline diets and the drought allowance.

The existing ranges files (`results/ranges_<release>.csv`) are unchanged; these files sit beside them.
