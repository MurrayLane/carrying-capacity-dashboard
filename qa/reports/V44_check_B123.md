# V44: blind check of B123 (shocked ranges on the widened draws; the -3 reruns; three loose ends)

Brief: `qa/briefs/V44_check_B123.md`; rules `qa/briefs/_checker_rules_results_wave.md`. No git, no subagents, no network. My scripts and the two repository copies I ran the generators in are in the session scratch folder (`.../scratchpad/v44/`); the only repository file written is this report. No register row, release, `results/` file or analysis file was changed.

Order of work: items 1, 2, 4 and 5 were derived by my own code before I opened `qa/reports/B123_shocks_on_widened_draws.md`, `shocks_ranges_wide*.csv`, `method_status-3.csv`, `long_term_regions-3.csv` or `cross_method_local.csv`. One exception, stated plainly: for item 4 I read the "Both classifications of the productivity basis" section of `analysis/method_tests_2025/README.md` to learn which readings make the secondary rows, and that section already carries B123's numbers. The targets were also printed in my brief, so this changes nothing, but item 4 is not fully blind.

## Tolerance (set before comparing)

* Counts and region names: exact.
* National percentiles from the same 2,000 draws: within 0.5% (in practice I expected, and got, exact to the person).
* Shares of draws: within one unit of the last printed digit (0.0001 as a fraction).
* Ratios: within one unit of the last printed digit.
* State ranges (my 200 draws against the builder's 2,000): within two bootstrap standard errors of my 200-draw percentile (2,000 resamples), the sampling error of my run; the builder's 2,000-draw error is about a third of that and is ignored.
* Byte checks: `cmp` identical.

## Wrong-value example

`cmp_nat.py` recomputes the national shocked percentiles from block A and compares them with `shocks_ranges_wide.csv` at the tolerance above. Fed a deliberately wrong 1-in-10 factor (0.75 in place of 0.742361) it fails:

    FAIL rp10 p5: mine 23,336,575 builder 23098884 (1.03%)
    FAIL rp10 p50: mine 29,245,932 builder 28948052 (1.03%)
    FAIL rp10 p95: mine 36,877,371 builder 36501763 (1.03%)
    FAIL rp10 share: mine 0.3420 builder 0.3700
    MISMATCH

With the right factor it prints `ALL PASS`.

## My figures

### Item 1. Shocked ranges on the widened draws

Rule checked first: `Evaluator` on 2025-fixed, short term, at return periods 1, 10 and 20 gives capacity at 10 and 20 equal to the average year times the release's factor to six decimals in Australia (0.742361, 0.634262), NSW-ACT (0.549596, 0.425278) and Queensland (0.662675, 0.526601).

National, block A of `monte_carlo_draws_2025-fixed_wide.csv` (2,000 draws), short term, release table, linear percentiles; population 27,608,200:

| Return period | p5 | p50 | p95 | Capacity over population p5, p50, p95 | Population over capacity p5, p50, p95 | Draws below 27,608,200 |
|---|---|---|---|---|---|---|
| Average year | 31,115,433 | 38,994,576 | 49,169,829 | 1.127, 1.412, 1.781 | 0.887, 0.708, 0.561 | 9 of 2,000 (0.45%) |
| 1 in 10 | 23,098,884 | 28,948,052 | 36,501,763 | 0.837, 1.049, 1.322 | 1.195, 0.954, 0.756 | 740 (37.00%) |
| 1 in 20 | 19,735,337 | 24,732,778 | 31,186,554 | 0.715, 0.896, 1.130 | 1.399, 1.116, 0.885 | 1,553 (77.65%) |

Bootstrap standard errors of the national percentiles (2,000 draws): about 0.10, 0.11 and 0.28 million at 1 in 10 (p5, p50, p95); 0.09, 0.10, 0.25 at 1 in 20. 27.6 million lies inside both ranges. The other usual percentile definitions move the ends by at most 0.05 million.

Own-table variant (draws with `restable` 1 take the leave-one-out factors 0.713504 and 0.602007; 1,000 of 2,000 draws have `restable` 1): 1 in 10, 22,497,730 to 35,936,047 (median 28,382,696), 42.00% below; 1 in 20, 19,070,192 to 30,458,271 (median 24,115,753), 82.30% below.

My own run: `MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 node analysis/sensitivity_2025/monte_carlo.mjs WORK states200.csv 200`, with WORK the X054-passing work folder of B41 (the script's offset check passed). Shocked by the release factors, millions, value plus or minus bootstrap standard error:

| Zone | Return period | p5 | p50 | p95 | Share under own population |
|---|---|---|---|---|---|
| NSW-ACT | 1 in 10 | 4.335 ± 0.082 | 5.790 ± 0.069 | 7.339 ± 0.107 | 100% |
| NSW-ACT | 1 in 20 | 3.354 ± 0.063 | 4.480 ± 0.053 | 5.679 ± 0.080 | 100% |
| Queensland | 1 in 10 | 4.631 ± 0.100 | 5.711 ± 0.071 | 6.763 ± 0.093 | 48.5% ± 3.5 |
| Queensland | 1 in 20 | 3.680 ± 0.076 | 4.539 ± 0.055 | 5.374 ± 0.075 | 99.0% ± 0.7 |
| Australia (same 200) | 1 in 10 | 22.951 ± 0.458 | 29.134 ± 0.369 | 35.920 ± 0.428 | 36.0% ± 3.4 |

**The own-table variant and the time frame.** `restable` is a long-term choice (B115's table, preset "long"; Sobol short-term index 0%). The long-term preset runs at resilience 100, so each long-term draw already carries its own table; the short-term preset runs at resilience 1, where both tables give a factor of 1, so a short-term draw is the same whichever `restable` it holds. The variant is therefore defined by the draws only for the long term. The shocked short-term ranges, however, **can and do differ** under an "own table" rule, because the rule then applies the leave-one-out factor to the half of the draws that carry `restable` 1: 22.5 to 35.9 against 23.1 to 36.5 at 1 in 10, and 42.0% against 37.0% below. That difference is not a property of the short-term draws; it amounts to adding a fifty-fifty choice of table to the short-term shock, which B115 did not define. The release-table rule (B112's) is the one that matches the draws.

### Item 2. Regions under and over capacity, 2011 (the 52 NRM regions and the Northern Territory)

Over capacity means population above capacity; no region is exactly level. The `over_capacity` column of each results file agrees with this in every row.

| Release (method) | Population | Short: under, over | Long: under, over | Long: share of the regions' people in over-capacity regions |
|---|---|---|---|---|
| 2011-corrected (published) | own (thesis) | 31, 22 | 14, 39 | 94.3% |
| 2011-corrected (published) | the -3 population | 32, 21 | 16, 37 | 93.8% |
| 2011-fixed (corrected, old) | own | 30, 23 | 17, 36 | 93.8% |
| 2011-fixed-2 | own | 31, 22 | 17, 36 | 93.7% |
| 2011-fixed-3 (corrected) | own = -3 | 31, 22 | 18, 35 | 93.4% |
| 2011-improved (old) | own | 31, 22 | 15, 38 | 94.3% |
| 2011-improved-2 | own | 32, 21 | 15, 38 | 94.3% |
| 2011-improved-3 (improved) | own = -3 | 33, 20 | 17, 36 | 93.7% |

On the -3 population: status changes published to corrected, short 1 (Mackay Whitsunday), long 2 (Northern Gulf, South East SA); corrected to improved, short 2 (Desert Channels, Mackay Whitsunday), long 1 (South East SA). The -2 and -3 corrected releases have identical capacities (they differ in population only); the improved -2 and -3 differ in capacity in 75 of 120 cells.

### Item 3. `decompose_corrected.mjs --average`

Run in two fresh copies of the repository (copy A, copy B), then a second consecutive run in copy A. After each run `README.md`, `capacity_by_cause_corrected_orders.csv`, `capacity_by_cause_corrected.csv`, `capacity_by_cause.csv`, `movers.csv` (every file of the folder) are `cmp`-identical to the committed files. The second consecutive run is identical too, which shows the blank-line fix directly (B123 had not run it twice). The committed README carries the V37 wording: "the consumption and red-meat-mix layers" (once), "-7 people" (twice), "(the sum of the two rows)" (once), "as one layer" (nine times).

### Item 4. Secondary rows of `cross_method_local.csv` (2021-23 yields)

From `harmonised_comparison.csv`: footprint at world-average productivity on 2021-23 yields, builds 1 and 3, cropland-bound and crop and pasture together (pasture alone left out, as on the primary rows): 159.8, 343.4 (build 1), 146.2, 287.7 (build 3, column (b)) gives **146.2 to 343.4**. The aggregate set adds the energy and protein balance (133.8 to 210.7, as run), HALF 275.8 and people per hectare (144.8 to 190.0): **133.8 to 343.4**.

Ratios on 41.5 and 53.6: footprint 3.52 to 8.27 and 2.73 to 6.41; aggregate 3.22 to 8.27 and 2.50 to 6.41. The 1990-yield qualifier is 103.1 (2.48 and 1.92 times). On the unrounded 41,503,537 and 53,643,731 the aggregate low over improved is 2.494, which prints 2.49. That is within one unit of the last digit, so the check passes, but the cell depends on rounding the denominator first.

A rerun of `harmonised_lines.py` in a copy gives `cross_method_local.csv`, `harmonised_comparison_lines.csv` and `harmonised_comparison.csv` byte-identical to the committed files.

### Item 5. `foran_poldy_balance.py`

My count from `fbs_au_world_2021_23.csv`: the 2021-23 mean head count is 26.20284 million (25,956.42, 26,200.98 and 26,451.12 thousand), against 26.07870 million for 2021-22 (ratio 1.00476). My unrounded figures on three years (two years in brackets): food use per person grain 111.896 (112.429), meat 112.825 (113.362), fish 24.463 (24.579) kg; readings meat 41.269 (41.073), grain with feed grain 126.753 (126.590), fish 12.059 (12.002) million.

A rerun of the script in a copy is byte-identical to the committed csv. In a second copy I set the head count back to 2021-22: the output then differs in exactly one cell, "actual food use per person 2021-23 (kg)", fish 25 (old) against 24 (new).

## Comparison

| Item | Builder | Mine | Verdict |
|---|---|---|---|
| 1: national 1 in 10, p5 to p95 (median) | 23.1 to 36.5 (28.9); csv 23,098,884, 28,948,052, 36,501,763 | identical to the person | pass |
| 1: national 1 in 20 | 19.7 to 31.2 (24.7); csv 19,735,337, 24,732,778, 31,186,554 | identical | pass |
| 1: average year | 31.1 to 49.2, 0.45% | identical, 9 of 2,000 | pass |
| 1: shares below 27.6 million | 37.0%, 77.65% | 37.00%, 77.65% | pass |
| 1: capacity over population | 0.837 to 1.322; 0.715 to 1.130; average 1.127 to 1.781 | same | pass |
| 1: population over capacity | 1.195, 0.896 (central), 0.756; 1.399, 1.049, 0.885 | same (central 27.6082/30.8106 = 0.896) | pass |
| 1: 27.6 million inside both ranges | yes | yes | pass |
| 1: own-table variant | 22.5 to 35.9, 42.0%; 19.1 to 30.5, 82.3% | identical | pass (figures); see "differently" on its label |
| 1: NSW-ACT 1 in 10 | 4.373, 5.713, 7.459 | 4.335 ± 0.082, 5.790 ± 0.069, 7.339 ± 0.107 (0.5, 1.1, 1.1 SE) | pass |
| 1: NSW-ACT 1 in 20 | 3.384, 4.421, 5.772 | 3.354, 4.480, 5.679 (0.5, 1.1, 1.2 SE) | pass |
| 1: Queensland 1 in 10 | 4.686, 5.721, 6.896; 46.7% under | 4.631, 5.711, 6.763 (0.6, 0.1, 1.4 SE); 48.5% ± 3.5 | pass |
| 1: Queensland 1 in 20 | 3.724, 4.547, 5.480; 98.05% | 3.680, 4.539, 5.374 (0.6, 0.2, 1.4 SE); 99.0% ± 0.7 | pass |
| 1: builder's state draws file | Australia equals block A; 19 choices equal | max difference 0; 0 choice mismatches; NSW and QLD percentiles recomputed from it equal the csv to the person | pass |
| 1: own table defined only for the long term | "acts on the long term only" | true for the draws; the short-term shocked ranges do differ under the own-table rule | pass, with the label point below |
| 2: method_status-3, 2011 short (published, corrected, improved), one -3 population | 21, 22, 20 | 21, 22, 20 | pass |
| 2: 2011 long | 37, 35, 36 | 37, 35, 36 | pass |
| 2: published on its own population | 22, 39 | 22, 39 | pass |
| 2: old counts | 22, 23, 22; 39, 36, 38 | 22, 23, 22; 39, 36, 38 (2011-corrected, 2011-fixed, 2011-improved on own populations) | pass |
| 2: names, corrected to improved | short: Desert Channels; Mackay Whitsunday. long: South East SA | same | pass |
| 2: status changes published to corrected | 1, 2 | 1 (Mackay Whitsunday), 2 (Northern Gulf, South East SA) | pass |
| 2: long_term_regions-3, 2011 | 18 under, 35 over, 93.4% (old 17, 36, 93.8%) | same; all 108 rows match the results files in capacity and population, and ratios within 0.0005 | pass (note 1) |
| 3: --average twice; README and every csv | byte-identical (one run) | byte-identical in two fresh copies and on a second consecutive run | pass |
| 4: footprint secondary | 146.2 to 343.4; 3.52 to 8.27; 2.73 to 6.41 | same | pass |
| 4: aggregate secondary | 133.8 to 343.4; 3.22 to 8.27; 2.5 to 6.41 | same (2.50 on 53.6; 2.49 on the unrounded improved) | pass |
| 4: README table matches the csv | yes | yes | pass |
| 5: head count | 26.203 (was 26.079) | 26.20284 (was 26.07870) | pass |
| 5: the one cell changed | fish 25 to 24 | fish 25 to 24, the only difference | pass |
| 5: unrounded readings | meat 41.07 to 41.27; grain 126.59 to 126.75; fish 12.00 to 12.06 | same | pass |

Note 1: `long_term_regions-3.csv` (and the old file) prints South Tasmania 2025 as 0.041, where the results file gives 12,441 / 299,777 = 0.04150 (0.042 to three places). The script probably divides the unrounded capacity. This is within one unit of the last digit, comes before B123, and no claim uses it.

## Claim rows the builder says move

| Row | Builder's after | My verdict |
|---|---|---|
| A014 | 30.8, widened range 23.1 to 36.5; 27.6 inside | agree |
| A183 | 1.12, widened 0.84 to 1.32 (0.837 to 1.322) | agree |
| A187 | 0.95, widened 0.72 to 1.13 (0.715 to 1.130) | agree |
| A195 | 26.3, widened 19.7 to 31.2 | agree |
| A196 | the base holds; on the widened range 37.0% under at 1 in 10 and 77.65% at 1 in 20, so neither "feeds itself at 1 in 10" nor "not at 1 in 20" holds across the range | agree |
| A308 | 21; 22; 20 on one population, or 22; 22; 20 with the published release's own population; a choice for Murray | agree with both counts. My preference: one population for all three, so the comparison isolates the method; the choice is Murray's |
| A310 | 37; 35; 36 on one population, or 39; 35; 36 | agree; same preference |
| B046 | value 146.2 to 343.4, 103 as a qualifier | agree |
| B156 | value: secondary 133.8 to 343.4 (aggregate), footprint 146.2 to 343.4 | agree on the value. **The statement also moves:** it says the calorie and land methods (energy and protein balance, the two land-per-diet methods, people per hectare) "read 146 to 343 million on current yields". On 2021-23 yields that group's low is 133.8 (energy and protein balance, protein as run), so the statement should read 134 to 343. The builder did not list the statement |
| B144 | fish 25 to 24 kg (value list "...; 25" to "...; 24") | agree |
| B247 | value "103 to 343" is the 1990-yield reading; 146.2 to 343.4 on current yields | agree: footprint and HALF together read 146.2 to 343.4 (HALF 275.8 inside), so the statement's "146 to 343" is right |
| B350 | now equals the csv | agree: every figure in the statement equals a cell of `cross_method_local.csv`; its locator note ("print 103 to 343 and 2.48 to 8.27") is stale |

The builder's A390, A391, A392 (unchanged, with new companion ranges), A143, A144, A151, A309, A311 (hold) and A038, A184, A188, A402 (no regional widened draws) agree with my figures where I have them (A143 18, A144 93.4%).

## What I would do differently, and whether it changes a number

1. **Label of the own-table file.** It applies a long-term-only choice to short-term shocks. It is better described as "a fifty-fifty choice of resilience table added at the shock", not "each draw's own table". No headline number changes: 27.6 is inside both ranges either way. Only the variant's wording changes.
2. **B156 statement.** "146 to 343" should be 134 to 343 (133.8 to 343.4). This changes a printed number in a Tier A row that the builder listed for its value only.
3. **Build 2 in the secondary footprint row.** Build 2 (V04) is also on 2021-23 world yields (139.4 cropland-bound, 277.7 together). It is left out because it has no primary (local) reading. If it were included, the footprint secondary would read 139.4 to 343.4 (3.36 and 2.60 times). The aggregate low (133.8) would not change. I would keep the builder's choice but say it in the row text. No change as built.
4. **Rounded denominators.** The aggregate low over improved is 2.50 on 53.6 and 2.49 on 53.64. No change unless the convention changes.
5. **Outside the brief.** The model reference row of `cross_method_local.csv` still prints the 13-choice range 41.5 (36.3 to 45.8), although decision 115 makes the widened range (31.1 to 49.2) the headline. A later job should decide. `bases_fidelity.py` still uses the 2021-22 head count (the builder reported this).
6. **Item 3, the default mode.** Following the brief, I reran only `--average`. I did not rerun the default mode (the B76 section, which the builder says still drops the V29 paragraph, X129).

## Register rows touched

None.

## Rerun (repository root unless stated; S is the scratch folder)

    python3 S/v44/nat.py                       # national percentiles, shares, ratios, own table
    python3 S/v44/cmp_nat.py ; python3 S/v44/cmp_nat.py 0.75    # comparison and the wrong-value example
    MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 node analysis/sensitivity_2025/monte_carlo.mjs S/b41/work S/v44/states200.csv 200
    cd S/v44 && python3 states.py              # state ranges with bootstrap errors
    python3 S/v44/regions.py                   # item 2 counts
    node S/v44/rule.mjs                        # drought factor rule
    (in a copy) cd analysis/comparison_2025 && node decompose_corrected.mjs --average --jobs 4 ; cmp against the committed folder
    (in a copy) python3 -I analysis/method_tests_2025/harmonised_lines.py ; python3 -I analysis/method_tests_2025/foran_poldy_balance.py

Files read: the two briefs and the rules; `monte_carlo_draws_2025-fixed_wide.csv`, `monte_carlo_draws_2025-fixed_wide_states.csv`, `monte_carlo.mjs`, `evaluate.mjs`, sensitivity README (B115 section); `web/public/data/2025-fixed` and `2025-resilience-loo` model and regions; `results/2011-*.csv`, `results/2025-improved.csv`, `results/2025-fixed.csv`; `harmonised_comparison.csv`, `fbs_au_world_2021_23.csv`, `foran_poldy_balance.py` and csv, the method_tests README section on the productivity basis; `qa/defects.csv` (X102, X137); the named claim rows; and last, the B123 report, `shocks_ranges_wide*.csv`, `method_status-3.csv`, `long_term_regions-3.csv`, `cross_method_local.csv` and the paper_a README B112 and B123 sections.
