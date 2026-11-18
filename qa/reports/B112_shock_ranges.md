# B112: ranges on the shocked figures, the herd-cycle Monte Carlo, and the drought factor's basis with a crop-only bound (decisions 102, 103)

Release: `2025-fixed` (the corrected release). Short-term settings unless stated. Millions of people. No claim register row, frozen release or existing output file was edited.

## The answers in brief

* **Shocked ranges on the published Monte Carlo range** (the 1,000 draws behind `results/ranges_2025-fixed.csv`, three meat windows): **1 in 10: 27.0 to 34.0 million (central 30.8); 1 in 20: 23.0 to 29.0 million (central 26.3).** 27.6 million people lies **inside both ranges**. Capacity over population runs 0.98 to 1.23 at 1 in 10 and 0.83 to 1.05 at 1 in 20 (people over capacity 0.81 to 1.02 and 0.95 to 1.20). So on the published range the sign of the margin is not settled at either return period.
* **Herd-cycle Monte Carlo** (meat window drawn from the four full-cycle windows only; every other draw unchanged): Australia short term **39.4 to 43.8 million (median 41.6, base 41.5)**, long term **13.9 to 16.2 (median 15.0, base 15.6)**, against 36.3 to 45.8 and 13.4 to 16.5 published. Short-term variance shares: **red-meat share 85%, meat-and-egg share 16%, meat window 1%**, every other choice 1% or less. Long term: resilience table 81%, organic yield factor 14%, meat window 2%.
* **Shocked ranges on the herd-cycle range:** **1 in 10: 29.2 to 32.5 million**, so 27.6 million lies **below the whole range** (capacity over population 1.06 to 1.18); **1 in 20: 25.0 to 27.8 million**, so 27.6 lies **inside, at the top edge** (0.90 to 1.01). On this basis the abstract's "above balance in a 1-in-10 year, below it in a 1-in-20 year" holds at 1 in 10 across the range and at 1 in 20 for all but the top few per cent of draws. R03a's rough reading (29.3 to 32.4 and 25.1 to 27.7) is confirmed to within 0.1 million.
* **Drought factor, crop-only bound (national):** applying the factor to crops alone (pasture-fed output at the mean) gives **41.2 million at 1 in 10, 41.0 at 1 in 20 and 40.4 at 1 in 100**, against **30.8, 26.3 and 18.9** with the factor on everything (the model's rule). The short-term drought results come almost wholly from applying a cereal factor to pasture-fed output. Long term at 1 in 100: crop-only 24.7 against 15.6.

## 1. Shocked ranges, national and by region (`analysis/paper_a/shocks_ranges.csv`)

**Method.** The model scales every yield of a zone by one factor, `Yield!C2`, read from the zone's row of the resilience sheet at the return period, and capacity is linear in the yields. So each draw's shocked capacity is its average-year capacity times its zone's factor. `shocks_ranges.mjs` multiplies each of the 1,000 draws (`analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_all.csv`, and the two herd-cycle sets of section 2) by the factor and takes the 5th, 50th and 95th percentiles with the rule of `summarise_mc.py`; `central` is the release evaluated at that return period. Columns: release, draws, return period (1, 10, 20), preset (short), zone, name, kind, population, factor and its cell, central, p5, p50, p95, people over capacity at central, at p5 and at p95, capacity over population at the same three, and whether the population lies inside p5 to p95. 540 rows: 60 zones, 3 return periods, 3 draw sets.

**Checks.** (a) The release at 10 and 20 years equals average year times factor in 59 of 60 zones to under 0.001%; Northern and Yorke (zone 45) differs by 0.24% and 0.39% (the script stops above 0.5%). (b) Two non-base draws (draws 0 and 500, all 60 zones, both return periods) evaluated by the model at the return period (`monte_carlo_herdcycle.mjs` with `MC_SHORT_RES`) against draw times factor: 234 of 240 zone results agree to 0.01%, the largest gap 0.23% (Northern and Yorke). (c) `check_shocks_ranges.py` recomputes all 1,620 percentiles from the draws with the factors from `analysis/resilience_2025/tables.csv` (an independent source for the same table) and all agree to one person. (d) The published draws are reproduced by the work folder used: draws 0, 1 and 500 re-evaluated with their stored choices agree to within 400 people of about 40 million (the stored choices are rounded to five decimals).

National and states (capacity in millions; ranges p5 to p95; people over capacity, so above 1 is short):

| 1 in 10 | factor | population | central | published range | herd-cycle range | people over capacity, central | published | herd-cycle |
|---|---|---|---|---|---|---|---|---|
| Australia | 0.742 | 27.61 | 30.81 | 26.97 to 33.97 | 29.21 to 32.55 | 0.896 | 0.813 to 1.024 | 0.848 to 0.945 |
| NSW and ACT | 0.550 | 9.08 | 5.81 | 5.11 to 6.41 | 5.38 to 5.96 | 1.563 | 1.416 to 1.775 | 1.523 to 1.687 |
| Victoria | 0.682 | 7.07 | 4.21 | 3.94 to 4.39 | 4.16 to 4.39 | 1.682 | 1.611 to 1.794 | 1.613 to 1.702 |
| Queensland | 0.663 | 5.67 | 5.96 | 5.57 to 6.19 | 5.57 to 6.17 | 0.951 | 0.916 to 1.018 | 0.919 to 1.017 |
| South Australia | 0.701 | 1.90 | 1.44 | 1.33 to 1.53 | 1.40 to 1.52 | 1.320 | 1.244 to 1.433 | 1.251 to 1.355 |
| Western Australia | 0.792 | 3.04 | 2.46 | 2.29 to 2.60 | 2.46 to 2.70 | 1.236 | 1.172 to 1.330 | 1.128 to 1.237 |
| Tasmania | 0.834 | 0.58 | 0.27 | 0.24 to 0.28 | 0.24 to 0.27 | 2.172 | 2.091 to 2.425 | 2.098 to 2.433 |
| Northern Territory | 0.701 | 0.26 | 0.04 | 0.04 to 0.05 | 0.01 to 0.01 | 6.275 | 5.518 to 7.433 | 21.5 to 29.6 |

| 1 in 20 | factor | population | central | published range | herd-cycle range | people over capacity, central | published | herd-cycle |
|---|---|---|---|---|---|---|---|---|
| Australia | 0.634 | 27.61 | 26.32 | 23.04 to 29.03 | 24.96 to 27.81 | 1.049 | 0.951 to 1.198 | 0.993 to 1.106 |
| NSW and ACT | 0.425 | 9.08 | 4.49 | 3.96 to 4.96 | 4.16 to 4.61 | 2.020 | 1.830 to 2.294 | 1.968 to 2.180 |
| Victoria | 0.479 | 7.07 | 2.95 | 2.77 to 3.08 | 2.92 to 3.08 | 2.395 | 2.295 to 2.555 | 2.298 to 2.424 |
| Queensland | 0.527 | 5.67 | 4.74 | 4.42 to 4.92 | 4.43 to 4.90 | 1.196 | 1.152 to 1.281 | 1.156 to 1.280 |
| South Australia | 0.509 | 1.90 | 1.05 | 0.96 to 1.11 | 1.02 to 1.10 | 1.817 | 1.712 to 1.973 | 1.722 to 1.866 |
| Western Australia | 0.730 | 3.04 | 2.27 | 2.11 to 2.39 | 2.27 to 2.49 | 1.342 | 1.271 to 1.443 | 1.224 to 1.343 |
| Tasmania | 0.764 | 0.58 | 0.24 | 0.22 to 0.25 | 0.22 to 0.25 | 2.370 | 2.282 to 2.646 | 2.290 to 2.655 |
| Northern Territory | 0.509 | 0.26 | 0.03 | 0.03 to 0.03 | 0.01 to 0.01 | 8.640 | 7.597 to 10.234 | 29.6 to 40.8 |

**Regions (52 NRM regions and the Northern Territory, as in Table 6).** On either range the regional counts barely move: at 1 in 10, 21 regions are over capacity at the central figure, 21 at the 95th-percentile capacity and 22 at the 5th; the one region whose population lies inside its range is North Tasmania (people over capacity 1.000 at the central figure). At 1 in 20, 24 regions are over capacity at every point of the range and no region's population lies inside its range. In the average year the regions inside their range are Corangamite, Wet Tropics and Rangelands on the published range, and Corangamite and Rangelands on the herd-cycle range.

**Queensland** is the one state whose population lies inside its 1-in-10 range on both bases (people over capacity 0.92 to 1.02).

## 2. Herd-cycle windows (`results/ranges_2025-fixed_herdcycle.csv`)

**What was run.** The 1,000 Latin hypercube draws of the published all-zones run (`MC_RELEASE=2025-fixed MC_ZONES=all MC_LONG=1`, 13 choices, seed 20261027), with the meat-data window drawn from the four full-cycle windows the sensitivity README names (8 years 2017-18 to 2024-25, 10 years 2015-16 to 2024-25, 15 years 2010-11 to 2024-25, 20 years 2005-06 to 2024-25), equal chances (250 draws each). The uniform behind the window choice is the same hypercube column, and the other twelve choices take exactly their published values in every draw (checked: 0 differing cells of 12,000). `monte_carlo.mjs` was not edited: B112 copied it to `analysis/sensitivity_2025/monte_carlo_herdcycle.mjs` and added `MC_WIN_ONLY=1` (window from the four full-cycle windows alone) and `MC_SHORT_RES` (used only for check (b) of section 1). The copy was taken before B115 added its `MC_WIDE` and `sobol` options to `monte_carlo.mjs`; with neither B112 option set it behaves as `monte_carlo.mjs` without B115's options.

The window folder was rebuilt for this job by the X069 route (`rebuild_off.py` then `make_win.py` on the ABS herd, flock and meat files); it is byte for byte the earlier X069 folder and passes the `MC_WIN_DIR` check. The work folder for the group factors passes the X054 check and reproduces the published draws (check (d) above). The summary is `summarise_herdcycle.py`, the rules of `summarise_mc.py` with one change: the meat window is grouped by its values when it has up to five (summarise_mc.py does so only up to three). On the published draws it reproduces `results/ranges_2025-fixed.csv` byte for byte.

**Result, Australia** (millions; p5 to p95):

| Draws | Short term | Long term |
|---|---|---|
| Published, three meat windows | 36.3 to 45.8 (median 41.2) | 13.4 to 16.5 (median 14.8) |
| **Four full-cycle windows** | **39.4 to 43.8 (median 41.6)** | **13.9 to 16.2 (median 15.0)** |
| Variant: base window and the four full-cycle windows | 39.3 to 43.8 (median 41.5) | 13.9 to 16.2 (median 15.0) |

Base 41.5 and 15.6 throughout. The 2011 short-term figure (33.3) lies below every range; the 2011 long-term figure (15.35) lies inside every long-term range, so A009's reading holds on the herd-cycle basis too.

**Variance share of each choice alone, Australia** (first-order, four full-cycle windows; published run in brackets):

| Choice | Short term | Long term |
|---|---|---|
| red meat share of the diet | 84.7% (16.3%) | 0% (0%) |
| meat and egg share of the diet | 16.5% (2.1%) | 0.3% (0%) |
| window of herd and meat data | 1.2% (80.6%) | 2.2% (36.3%) |
| organic share of land | 1.1% (0%) | 0.9% (1.0%) |
| timber per person | 1.0% (0%) | 0.3% (0%) |
| field-crop group factor | 0.9% (1.2%) | 0.1% (0.5%) |
| biofuel share | 0.9% (0.2%) | 0% (0%) |
| long-term liquid fuel | 0.1% (0.6%) | 0.6% (1.2%) |
| resilience table | 0% (0%) | 81.3% (52.1%) |
| default organic yield factor | 0% (0%) | 13.8% (8.6%) |
| vegetable, fruit and nut factors; liquid fuel per person; feeding benchmark | 0% | 0% |

The shares of about 1% for timber, biofuel, the organic share and the field-crop factor are at the noise floor of the 20-bin estimate (the short-term shares add to 106%). The mean national short-term capacity by window is 41.8 (8 years), 41.7 (10), 41.6 (15) and 41.4 (20), against 41.4 for the base window, 37.7 for the early three years and 44.3 for the late three years: with the three-year windows out, the window choice hardly matters and the diet shares carry the short-term range.

**Limits of the herd-cycle range.** (1) With the base window excluded, the release base lies outside the zone's own range in eight zone and setting results: the Northern Territory short and long term (base 0.060, range 0.013 to 0.018 short term), four Western Australian wheatbelt regions short term (Avon, Northern Agricultural, South Coast, South West: the base is 0.6% to 4.3% below the range) and Corangamite and Lower Murray Darling at the edge. With the base window included as a fifth choice only Lower Murray Darling (long term, at the edge) remains. Every full-cycle window gives the Northern Territory about a quarter of its base capacity; that comes from the X069 construction (wool, milk and cattle meat follow the herds between windows, not the series) and from the territory's thin data, and the Northern Territory and the Western Australian regional herd-cycle ranges should not be quoted without a look at them. The national and state ranges (other than the Northern Territory) are unaffected. (2) The full-cycle windows are built by the X069 route, not directly, for want of wool, cattle-on-feed and state milk series before 2020-21 (README, X069).

## 3. The drought factor: construction and a crop-only bound (`analysis/resilience_2025/drought_bounds.csv`)

**Construction (one paragraph for the paper or its supplement).** The drought factor is the `resilience` sheet of the model, which in release 2025-fixed holds the table `analysis/resilience_2025/tables.csv`, rows "data: ABS to 2024-25" (identical to every cell; built by `analysis/resilience_2025/resilience.py`). For Australia and each state, each season's yield is the unweighted mean of the wheat, oats and barley yields in tonnes per hectare (all three grains required), from the ABS Historic Agricultural Commodities 1860 to 2022 workbook (Tables 4, 3 and 1) and the ABS 2022-23 to 2024-25 cubes (`data/abs-2022-25/cube_<season>.json`): 153 observations, the seasons ending 1861, 1866 and 1871, then every season from 1875-76 to 2024-25. Each season is divided by the mean of the ten observations from five before to four after it (the season itself included; held at the first or last ten observations at the ends). The 153 ratios are ranked from the worst; rank k is read as a one-in-(n+1)/k year; the table takes anchors at 1, 3, 5, 10, 20, 30, 50 and 150 years (rank round(154/T)) and interpolates in a straight line between them. For Australia the **1-in-10 factor 0.742 is the 15th-worst ratio (the season ending 1947)**, the **1-in-20 factor 0.634 the 8th-worst (1896)**, and the **1-in-100 factor 0.456 the midpoint of the 50-year anchor (3rd-worst, 1941, 0.552) and the 150-year anchor (the worst, 1915, 0.359)**. The model reads the factor in `Yield!C2`, which picks `resilience!B3` (Australia) to `B10` (Northern Territory, which carries South Australia's row) by zone number; `resilience!B3 = INDEX(C3:EV3, MATCH(Settings!B8, C2:EV2))` reads the row at the return period in `Settings!B8`; and every yield row is `Yield!B = C2 x E x D`, D being the zone yield of column F with the irrigation adjustment and E the organic adjustment, so the one factor scales crops, pasture-fed and grain-fed animal products, fish, honey and timber alike. Australia's cells: 1 in 10 `resilience!L3` = 0.742361, 1 in 20 `resilience!V3` = 0.634262, 1 in 100 `resilience!CX3` = 0.455821. (The 2011 releases use the thesis table, 0.599 at 20 years.) The recent droughts appear in the cereal record as the seasons ending 2007 (0.567, 4th-worst), 2003 (0.578) and 2020 (0.762, 16th-worst).

**Bounds** (`drought_bounds.mjs`; national, release 2025-fixed; the factor applied to the zone yields in column F, which is the same as applying it through `Yield!C2` to those rows alone):

| Setting | Return period | Factor | Average year | Both applied (the model) | Crop only | Plant rows only | Population | Capacity over population: both / crop only |
|---|---|---|---|---|---|---|---|---|
| short | 1 in 10 | 0.742 | 41.50 | **30.81** | **41.19** | 41.32 | 27.61 | 1.116 / 1.492 |
| short | 1 in 20 | 0.634 | 41.50 | **26.32** | **40.99** | 41.20 | 27.61 | 0.953 / 1.485 |
| short | 1 in 100 | 0.456 | 41.50 | **18.92** | **40.45** | 40.88 | 27.61 | 0.685 / 1.465 |
| long | 1 in 100 | 0.456 | 34.27 | **15.62** | **24.68** | 24.68 | 27.61 | 0.566 / 0.894 |

*Both applied*: every yield row times the factor (the model's rule); it equals the model run at that return period to the person in all four rows. *Crop only*: the plant rows (field crops, vegetables, fruit, nuts, fodder; rows 4 to 94 and 106 to 133) and the grain-fed animal rows (chicken, duck, turkey, eggs, pig meat; rows 99 to 103, whose yield per hectare is a grain yield over a feed conversion ratio) times the factor; pasture-fed output (sheep meat, wool, dairy milk, cattle meat, goat and sheep milk; rows 95 to 98, 135, 136) and the rest (fish, seafood, honey, timber; rows 104, 105, 134, 137, 138) at the mean. *Plant rows only*: the strict reading, grain-fed animals also at the mean. The long term is set at 100 years by definition, so it has the one row.

**Reading.** The two bounds bracket the truth for a drought that hits crops at the cereal factor: pasture-fed output does fall in a drought, but by an amount the records do not give (the one observed check, the single-year series, puts the drought years 2018-19 and 2019-20 near the median and the following year at 0.90). In the short term the crop-only bound barely moves from the average year (-0.8% at 1 in 10, -2.5% at 1 in 100), because short-term capacity is bound by pasture-fed meat and dairy; the whole of the short-term drought effect in Table 6 is the factor applied to pasture-fed output. In the long term, which is cropping-limited, the crop-only bound takes 28% off the average year at 1 in 100 (34.3 to 24.7) against 54% with the factor on everything.

**Not computed here:** fitted-tail intervals for the 10 and 20-year factors do exist in the records, contrary to R03a issue 6 (`analysis/resilience_2025/bootstrap.csv`, Australia: 0.66 to 0.81 at 10 years, 0.52 to 0.71 at 20); they are on the leave-one-out ratios and were not applied here. The livestock-output drought test and the 1990 sub-period table of R03a issue 6 were not part of this brief.

## Sentences the paper should carry

* Section 8 / Table 6: "Across the sensitivity range of the 2025 corrected release, the national capacity is 27.0 to 34.0 million in a 1-in-10 year and 23.0 to 29.0 million in a 1-in-20 year (5th to 95th percentile; base 30.8 and 26.3), against a population of 27.6 million: the base is above balance at 1 in 10 and below it at 1 in 20, but neither statement holds across the whole range."
* If the herd-cycle basis is adopted (a Tier A choice for Murray): "With the meat data window restricted to windows spanning a full herd cycle, the 2025 short-term range is 39.4 to 43.8 million, and the national capacity is 29.2 to 32.5 million in a 1-in-10 year (above the population throughout) and 25.0 to 27.8 million in a 1-in-20 year (at or below it). The red-meat share of the diet then explains 85% of the short-term variance and the window 1%."
* Abstract and highlight 3 (A196): name the basis, for example "a crop-yield weather allowance applied to all output", and state that the 1-in-10 and 1-in-20 statements are at the base settings with the range above.
* Drought basis: "The drought allowance is a factor from 153 seasons of wheat, oat and barley yields (1861 to 2024-25), each season over its ten-season local mean; the 1-in-10 factor for Australia (0.742) is the 15th-worst season. The model applies it to every yield, pasture-fed products included, which has not been tested. Applied to crops alone, with pasture-fed output at its mean, the national short-term capacity is 41.2 million at 1 in 10, 41.0 at 1 in 20 and 40.4 at 1 in 100, against 30.8, 26.3 and 18.9 with the factor on all output: the short-term drought results are a statement about pasture-fed output in a drought, which the cereal record does not measure."
* Regions: "The count of regions over capacity is robust to the range: 21 or 22 of 53 at 1 in 10 (North Tasmania is the one at balance) and 24 at 1 in 20."

## Files changed

All new, except one appended section:

* `analysis/paper_a/shocks_ranges.mjs` (new script) and `analysis/paper_a/shocks_ranges.csv` (new output)
* `analysis/paper_a/check_shocks_ranges.py` (new check)
* `analysis/paper_a/README.md` (a section appended at the end; nothing else changed)
* `analysis/sensitivity_2025/monte_carlo_herdcycle.mjs` (new; a copy of `monte_carlo.mjs` with two options added; `monte_carlo.mjs` not edited by B112)
* `analysis/sensitivity_2025/summarise_herdcycle.py` (new)
* `analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_herdcycle_all.csv`, `monte_carlo_2025-fixed_herdcycle_all.md` (new)
* `analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_herdcycle5_all.csv`, `monte_carlo_2025-fixed_herdcycle5_all.md` (new; variant with the base window)
* `results/ranges_2025-fixed_herdcycle.csv`, `results/ranges_2025-fixed_herdcycle5.csv` (new)
* `analysis/resilience_2025/drought_bounds.mjs` (new script) and `analysis/resilience_2025/drought_bounds.csv` (new output)
* `qa/reports/B112_shock_ranges.md` (this report)

Not edited: `qa/claims_register.csv`, any frozen release, `results/ranges_2025-fixed.csv`, `monte_carlo.mjs`, `summarise_mc.py`, the sensitivity and resilience READMEs (the resilience README is rewritten whole by its `write_readme.py`, and B115 is editing the sensitivity README; a pointer to the B112 files belongs in each in a README job).

**Reproduce** (repository root; WORK_DIR is a `build_variants.py` folder that passes the X054 check, WIN_DIR the X069 folder):
`python3 -I analysis/sensitivity_2025/rebuild_off.py OFF_DIR ABS_DIR`, `python3 -I analysis/sensitivity_2025/make_win.py OFF_DIR WIN_DIR`;
`MC_RELEASE=2025-fixed MC_ZONES=all MC_LONG=1 MC_WIN_DIR=WIN_DIR MC_WIN_ONLY=1 node analysis/sensitivity_2025/monte_carlo_herdcycle.mjs WORK_DIR analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_herdcycle_all.csv 1000` (and without `MC_WIN_ONLY` for the `_herdcycle5` variant);
`python3 -I analysis/sensitivity_2025/summarise_herdcycle.py <draws> results/2025-fixed.csv results/ranges_2025-fixed_herdcycle.csv analysis/sensitivity_2025/monte_carlo_2025-fixed_herdcycle_all.md` (it refuses to overwrite);
`node analysis/paper_a/shocks_ranges.mjs analysis/paper_a/shocks_ranges.csv`; `python3 -I analysis/paper_a/check_shocks_ranges.py`;
`node analysis/resilience_2025/drought_bounds.mjs analysis/resilience_2025/drought_bounds.csv`.
`shocks_ranges.mjs` and `drought_bounds.mjs` give byte-identical files on a second run.

## Claim rows that move (for a register job; the register was not edited)

Tier A:

| id | tier | before | after |
|---|---|---|---|
| A014 | A | 30.8 (1-in-10 national, no range) | 30.8, range 27.0 to 34.0 (published basis) or 29.2 to 32.5 (herd-cycle basis) |
| A183 | A | 1.12 (capacity over population, 1 in 10) | 1.12, range 0.98 to 1.23 (published) or 1.06 to 1.18 (herd-cycle) |
| A187 | A | 0.95 (1 in 20) | 0.95, range 0.83 to 1.05 (published) or 0.90 to 1.01 (herd-cycle) |
| A196 | A | "0.89; 0.95 ... feeds itself ... in a 1-in-10 year with about 12%, and not in a 1-in-20 year" | holds at the base only; on the published range both return periods straddle balance; on the herd-cycle range 1 in 10 is above balance throughout and 1 in 20 is at or below it except the top edge (1.01); the basis "crop-yield weather allowance applied to all output" to be named |
| A027 | A | 36.3 to 45.8 | 39.4 to 43.8, only if the herd-cycle basis is adopted (Murray's decision); otherwise unchanged |
| A028 | A | 13.4 to 16.5 | 13.9 to 16.2, only if the herd-cycle basis is adopted |
| A009 | A | "15.35 and 15.6 within 13.4 to 16.5" | "within 13.9 to 16.2" if the herd-cycle basis is adopted; the reading (inside the range) holds |
| A184 | A | 21 of 53 regions over capacity at 1 in 10 | 21, with 21 to 22 across the range (North Tasmania at balance) |
| A038 | A | three short-term flips not robust (Wet Tropics, Rangelands, Corangamite) | probably two (Rangelands, Corangamite) if the herd-cycle basis is adopted: Wet Tropics' population leaves its average-year range; to be confirmed by rerunning `regional_flips.py` on the herd-cycle file (not done here) |

Tier B and C:

| id | tier | before | after |
|---|---|---|---|
| A195 | B | 26.3; 18.9 | 26.3 (23.0 to 29.0 published; 25.0 to 27.8 herd-cycle); 18.9 unchanged (1-in-100 ranges not in this brief) |
| A188 | B | 24 of 53 at 1 in 20 | 24 at every point of either range |
| A343 | B | North Tasmania 1.000 at 1 in 10 | unchanged; it is the one region whose population lies inside its 1-in-10 range |
| A366 | B | meat window drawn from three windows with equal chances | four full-cycle windows with equal chances, if the herd-cycle basis is adopted |
| A223 | A (no value change) | -26% at 1 in 10 | unchanged; the crop-only bound (-0.8% at 1 in 10) supports its reading and can be cited beside it |

New claims the paper would gain (no register row): the shocked ranges above; the herd-cycle variance shares (red meat 85%, meat and egg 16%, window 1%); the drought-factor construction (0.742 = 15th-worst of 153 seasons, 1946-47); the crop-only bounds 41.2, 41.0, 40.4 (short term) and 24.7 (long term). Paper B rows B096, B097, B134, B137, B167 quote the central shocked values, which do not change.

Register rows touched: **none**.

## Wrong-value check

`check_shocks_ranges.py` recomputes all 1,620 percentiles of `shocks_ranges.csv` from the draws with the factors from `tables.csv` (1,620 agree to one person) and checks the 16 national figures quoted in this report (all pass, exit status 0).

*Example, a deliberate wrong value:* `python3 -I analysis/paper_a/check_shocks_ranges.py 2025-fixed_herdcycle_all 10 p5 29.9` replaces the quoted herd-cycle 1-in-10 lower end (29.2) with 29.9 and fails with exit status 1:
`FAIL quoted 2025-fixed_herdcycle_all 1-in-10 p5 = 29.9 but the file gives 29.214 million`.
