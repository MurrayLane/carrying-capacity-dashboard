# Sensitivity of the 2025 result to its uncertain choices

A sensitivity run is the model run again with ONE uncertain choice changed and everything else left as it is, to see how far the answer moves.
The base is release `2025-organic`: Australia **48.0 million people** in the short term, **12.3 million** in the long term (2011: 40.5 and 9.4 million).
35 variants; `results.csv` has every figure (Australia and the seven state zones, both settings). Reproduce:
`python3 analysis/sensitivity_2025/build_variants.py WORK_DIR ABS_DIR` (runs the two yield scripts with each alternative, needs the ABS files of `analysis/recent_data/fetch_recent.py`), then
`node analysis/sensitivity_2025/evaluate.mjs WORK_DIR/variants.json analysis/sensitivity_2025/results.csv` (needs `cd web && node scripts/build-data.mjs` first), then this script.

## What it shows

* **Direction holds one change at a time.** Every single variant stays above 2011: the lowest short-term figure is 43.4 million (diet back at 2011 shares) against 40.5, the lowest long-term 10.6 million (no group trend) against 9.4.
  **Two pessimistic choices together do not hold it in the short term:** the early meat window with both diet shares at 2011 gives 39.6 million, below 2011's 40.5 (`results.csv`, group `combination`; the long term for the same choices is 12.3).
  Against 2011 (40.5 and 9.4 million) the base is +19% short term and +30% long term; across the defensible single choices (land raster excluded) and the two combinations the range is -2% to +37% short term and +9% to +38% long term.
* **Short term turns on meat, not crops.** The diet shares and the meat window move it 6% to 15%; every crop choice moves it under 0.3%. Reason: red meat is most of the land in today's diet, so the pasture and the meat yields decide the answer.
  The red-meat share (a proxy from FAO food balance sheets, 64% to 57.8%) is the most consequential single default: five points either way is about 6%.
* **Long term turns on the crop factors.** The 100% plant-based, organic diet is cropping-land limited. Letting the crops the ABS no longer reports keep their 2011 yields costs 13.8%; the field-crop group factor's measured error (14%) moves it 6%;
  the vegetable, fruit and nut factors (error 20%) move it 3% to 4%; the organic factor range of Ponisio et al. 3%; the choice of crop years under 4%.
* **Reserve, infrastructure and the non-agricultural remainder do not enter capacity at all.** Changing them, or the reserve definition, changes the land-use display and nothing else. Only cropping and pasture land count. This is how the 2011 workbook works, and why recovering the 2011 land method mattered only for those two items.
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
| organic | organic factors of the five crops at the commercial ratios of Kniss et al. alone | +0.0% | -0.9% | 0% |
| organic | organic factors of the five crops back at 2011 values | +0.0% | +0.7% | 0% |
| diet and consumption | fuel, biofuel and timber at 2011 values (2520 L, 0.5%, 1 m3) | -0.3% | +0.0% | 13% |
| crop rules | strict rules: remove zone yields over 2 or under 0.2 times the national yield | +0.0% | +0.0% | 2% |
| crop rules | no plausibility cap or floor (only the 10 ha, 10 t and seed rules) | +0.0% | +0.0% | 2% |
| land | reserve = classes 1.1 and 1.2.5 (conservation and Indigenous uses) | +0.0% | +0.0% | 0% |
| land | reserve = class 1.1 only (nature conservation) | +0.0% | +0.0% | 0% |
| land | infrastructure measured on the raster (classes 5.3 to 5.7, 5.9) instead of 730 m2 a person | +0.0% | +0.0% | 0% |

## Limits

* Changes are made one at a time, apart from the two combinations at the foot of `results.csv`: early meat window with 2011 diet shares (short term 39.6 million) and no group trend with the low organic factor (long term 10.3 million, against 9.4). Other pairs are not the sum of their parts.
* The ranges are the ones we could defend (a measured error, an alternative source, a published range). They are not confidence intervals.
* Wool, milk and feedlot grain placeholders (SCOPE.md B12) are not varied; they enter through the livestock rows and are one of the data items we are waiting for.
