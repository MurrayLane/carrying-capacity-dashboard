# V38: blind check of B112 (shocked ranges, herd-cycle Monte Carlo, drought bounds)

Checker brief: `qa/briefs/V38_check_B112.md`, under `qa/briefs/_checker_rules_results_wave.md`. Release `2025-fixed`, short-term settings unless stated. I derived my own figures first, using my own code in the scratch folder `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/V38/`. Only after that did I open `qa/reports/B112_shock_ranges.md` and the files it names. No git, no subagents, no network. This file is the only repository file written.

## Verdict in brief

Every number in B112 that I could reach matches my own figures: the shocked national, state and regional ranges (1,080 cells of the published draw set and 720 cells of the two herd-cycle sets), the herd-cycle range and its variance shares, the drought-factor construction, and all four rows of the drought bounds. **No number changes.** Five items fail on wording or labelling:

1. The per-window means in section 2 come from the five-window variant, not the four-window run the report names.
2. "R03a's reading confirmed to within 0.1 million": the largest gap is 0.15 million.
3. "1 in 20 holds for all but the top few per cent of draws" and the proposed paper sentence "(at or below it)": in fact 7.5% of the herd-cycle draws are above 27.6 million.
4. "The whole of the short-term drought effect is the factor applied to pasture-fed output": the true share is about 97%.
5. A223 is Tier A but sits in the Tier B and C table.

## Tolerance (set before comparing)

* Counts and names: exact.
* Capacities: within 0.5%. In practice I also checked file cells to one person.
* Ratios and shares: within one unit of the last printed digit.
* Factors: within 1e-6.

## Wrong-value example

My comparator `compare2.py`, run with the argument `wrong`, inflates my national 1-in-10 p5 by 3% (27,781,272 instead of 26,972,109). It then reports `MISMATCH 1 10 p5 26972109.0 27781272.27` and a count of 1 mismatch, where the clean run reports 0 of 1,080. So the check can fail.

## My figures

**Shocked ranges** (`shocks.mjs`). The published 1,000 draws (`analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_all.csv`, column `<zone>_short`) are multiplied by the zone's factor from the release's `resilience` sheet. The zone is mapped to its state row by the `Yield!C2` formula, and the Northern Territory uses SA values. Percentiles use straight-line interpolation (the `summarise_mc.py` rule). The central figure is the evaluator at `resilience` = T. Population is 27,608,200.

| Return period | Factor | Central | p5 | p95 | People over capacity: central / at p5 / at p95 |
|---|---|---|---|---|---|
| average year | 1 | 41,503,537 | 36,332,875 | 45,763,902 | 0.665 / 0.760 / 0.603 |
| 1 in 10 | 0.742361 | 30,810,607 | 26,972,109 | 33,973,336 | 0.896 / 1.024 / 0.813 |
| 1 in 20 | 0.634262 | 26,324,116 | 23,044,562 | 29,026,304 | 1.049 / 1.198 / 0.951 |

At both return periods, 27.6 million lies inside the range.

**Regions** (53: the 52 NRM regions and the NT):

| Return period | Regions over capacity at central / p95 / p5 | Region whose population lies inside its range |
|---|---|---|
| 1 in 10 | 21 / 21 / 22 | North Tasmania |
| 1 in 20 | 24 / 24 / 24 | none |
| average year | 16 / 15 / 18 | Corangamite, Wet Tropics, Rangelands |

**Multiplication confirmed.**

* Evaluator at T against average year times factor, unrounded: all 60 zones agree to within 0.001% except Northern and Yorke (0.239% at 1 in 10, 0.393% at 1 in 20).
* Two published draws rerun through the full model, using a copy of `monte_carlo.mjs` with the short-term resilience set by an environment variable and the X054 work folder `scratchpad/b41/work`. Draw 0 at T=1 gives 39,665,043 against 39,664,807 published (the stored choices are rounded to five decimals). Draw 2 gives 42,876,684 against 42,876,869.
  * At 10 and 20 years: draw 0 gives 29,445,781 and 25,158,029, ratios 0.7423610 and 0.6342620. Draw 2, with its `restable` set to the release table, gives 31,829,978 and 27,195,051, ratios 0.742361 and 0.634262.

**Drought factors** (`factors.py`, written from the resilience README). The inputs are the ABS Historic Agricultural Commodities workbook (Tables 4, 3 and 1) and `data/abs-2022-25/cube_*.json`, with the yield taken as the mean of the three grains. Each season's ratio is to the mean of the 10 observations from 5 before to 4 after, held at the ends. The ratios are ranked, and the factor at return period T is the ratio at rank round(154/T). The 100-year factor is the midpoint of the 50 and 150-year values.

* n = 153 for Australia. The observations are the seasons ending 1861, 1866 and 1871, then annual from 1876.
* Australia: 1 in 10 = 0.742361 (15th-worst, season ending 1947); 1 in 20 = 0.634262 (8th-worst, 1896); 1 in 50 = 0.552352 (3rd, 1941); 1 in 150 = 0.359290 (worst, 1915); 1 in 100 = 0.455821.
* All six states also reproduce the release's 10, 20, 50, 100 and 150-year cells to six decimals.
* Recent seasons: 2007 is 0.567 (4th-worst), 2003 is 0.578 (5th), 2020 is 0.762 (16th).
* The 2011-fixed table gives 0.599 at 20 years.

**Crop-only bound** (`bounds.mjs`, national). The factor is applied to the region's yield vector (column F) at resilience 1.

| Setting, T | Both (model at T) | All rows scaled | Plant rows only (4-94, 106-133) | Plant + grain-fed animals (99-103) |
|---|---|---|---|---|
| short, 10 | 30,810,607 | 30,810,607 | 41,321,416 | 41,191,546 |
| short, 20 | 26,324,116 | 26,324,116 | 41,201,815 | 40,987,723 |
| short, 100 | 18,918,184 | 18,918,184 | 40,883,687 | 40,449,636 |
| long, 100 | 15,623,209 | 15,623,209 | 24,681,948 | 24,681,948 |

The average year is 41,503,537 short term and 34,274,878 long term (long preset at resilience 1).

Attribution test (`attr.mjs`):

* The factor on the pasture-fed rows only (95-98, 135, 136) gives 31,083,890 at 1 in 10.
* The factor on every row except those gives 41,017,763.
* So the pasture-fed rows carry about 97% of the 1-in-10 drop.

**Herd-cycle draws** (recomputed from B112's draw files, `compare2.py`). Short-term p5, p50 and p95 are 39,352,295, 41,564,362 and 43,841,245. Long-term p5, p50 and p95 are 13,948,722, 15,035,386 and 16,206,614. With the base window as a fifth choice: 39,346,781 to 43,769,992 short term and 13,919,524 to 16,179,271 long term.

Shocked herd-cycle ranges:

* 1 in 10: 29,213,609 to 32,546,031. The minimum draw is 28,454,834, so every draw is above 27.6 million.
* 1 in 20: 24,959,665 to 27,806,836. 75 of 1,000 draws are above 27.6 million.

Other checks on the herd-cycle draws:

* The other 12 choices are identical to the published draws (0 cells differ of 12,000).
* Each window has 250 draws.
* First-order shares, by my own implementation: short term red meat 0.847, meat and egg 0.165, window 0.012; long term resilience table 0.813, organic factor 0.138, window 0.022.
* Mean short-term capacity by window, four-window run: 41.69, 41.70, 41.67 and 41.30 for 8, 10, 15 and 20 years. Five-window run: 41.36 (base), 41.76, 41.71, 41.60, 41.35.

## Comparison with B112

| Item | Builder | Mine | Result |
|---|---|---|---|
| 1-in-10 national range (published draws) | 27.0 to 34.0, central 30.8 | 26.97 to 33.97, 30.81 | pass |
| 1-in-20 national range | 23.0 to 29.0, central 26.3 | 23.04 to 29.03, 26.32 | pass |
| 27.6 m inside both ranges | yes | yes | pass |
| Capacity over population, 1 in 10 / 1 in 20 | 0.98 to 1.23 / 0.83 to 1.05 | 0.977 to 1.231 / 0.835 to 1.051 | pass |
| People over capacity | 0.81 to 1.02 / 0.95 to 1.20 | 0.813 to 1.024 / 0.951 to 1.198 | pass |
| `shocks_ranges.csv`, published set: central, p5, p95 and the three people-over-capacity ratios (60 zones x 3 T) | file | mine | pass (1,080 of 1,080; capacities to 0 people) |
| `shocks_ranges.csv`, herd-cycle and herdcycle5 sets: p5 and p95 | file | recomputed | pass (720 of 720, to one person) |
| State tables, 1 in 10 and 1 in 20 (all cells; published columns mine, herd-cycle columns recomputed) | table | same | pass |
| Regions over capacity, 1 in 10: central / p95 / p5 | 21 / 21 / 22, North Tasmania inside | same | pass |
| Regions, 1 in 20 | 24 at every point, none inside | same, on both bases | pass |
| Average year, regions inside range | Corangamite, Wet Tropics, Rangelands; herd-cycle: Corangamite, Rangelands | same | pass |
| Check (a): release at T = average x factor in 59 zones; Northern and Yorke 0.24% / 0.39% | stated | 0.239% / 0.393%; others within 0.001% | pass |
| Check (b)/(d): draws reproduce; multiplication | stated | draws 0 and 2 reproduce within 236 people; ratios exact | pass |
| Herd-cycle national range, short | 39.4 to 43.8 (median 41.6) | 39.35 to 43.84 (41.56) | pass |
| Herd-cycle national range, long | 13.9 to 16.2 (15.0) | 13.95 to 16.21 (15.04) | pass |
| Herdcycle5 variant | 39.3 to 43.8 (41.5); 13.9 to 16.2 (15.0) | 39.35 to 43.77 (41.54); 13.92 to 16.18 (15.00) | pass |
| Herd-cycle variance shares, every cell, including the bracketed published shares | table | same to 0.001 | pass |
| Shocked herd-cycle, 1 in 10 | 29.2 to 32.5, below whole range | 29.21 to 32.55; every draw above 27.6 | pass |
| Shocked herd-cycle, 1 in 20 | 25.0 to 27.8; 0.90 to 1.01 | 24.96 to 27.81; 0.904 to 1.007 | pass |
| "1 in 20 holds for all but the top few per cent of draws" | few per cent | 7.5% of draws above 27.6 m | **fail (wording)**: say "about 92% of draws" |
| "R03a's reading confirmed to within 0.1 million" | 0.1 | gaps 0.09, 0.15, 0.14, 0.11 | **fail (wording)**: within 0.15 million |
| Mean short-term capacity by window, 41.8 / 41.7 / 41.6 / 41.4, attributed to the four-window run | 41.8, 41.7, 41.6, 41.4 | four-window run: 41.7, 41.7, 41.7, 41.3; these figures are the five-window file's | **fail (label)**; the conclusion ("the window hardly matters") stands |
| Mean for base / early / late window | 41.4 / 37.7 / 44.3 | 41.37 / 37.71 / 44.33 | pass |
| Short-term shares add to 106% | 106% | 106.4% | pass |
| Drought factor construction: 153 seasons, ranks, years, cells L3 / V3 / CX3, 2011 at 0.599 | stated | identical | pass |
| Recent seasons 2007 (0.567, 4th), 2003 (0.578), 2020 (0.762, 16th) | stated | identical | pass |
| `drought_bounds.csv`, all four rows: both, crop only, plant rows only, ratios | file | identical to the person | pass |
| Crop-only, -0.8% at 1 in 10 and -2.5% at 1 in 100; long -28% against -54% | stated | -0.75%, -2.54%; -28.0%, -54.4% | pass |
| "The whole of the short-term drought effect in Table 6 is the factor applied to pasture-fed output" | whole | pasture-fed rows alone: about 97% of the drop | **fail (overstated)**: "almost all" holds; the report's own brief section says "almost wholly", which passes |
| Claim table split by tier | Tier A separated | A223 (Tier A in the register) sits in the "Tier B and C" table, though marked A | **fail (minor, layout)** |

## Proposed paper sentences

1. **Section 8 / Table 6 range sentence: supported.** The figures support "the base is above balance at 1 in 10 and below it at 1 in 20, but neither statement holds across the whole range".
2. **Herd-cycle sentence.** "29.2 to 32.5 ... (above the population throughout)" is supported: every draw is above, not only the 5 to 95 range. "25.0 to 27.8 million in a 1-in-20 year (at or below it)" says more than the figures: the upper end, 27.8, is above 27.6, and 7.5% of draws are above. Suggested: "(below it in about 92% of draws; the 95th percentile, 27.8, is just above)". "Red-meat share 85%, window 1%" is supported.
3. **Abstract / A196 basis naming: supported** as a wording instruction; no figure involved.
4. **Drought basis sentence: supported.** I checked 153 seasons, 0.742 as the 15th-worst, and 41.2, 41.0 and 40.4 against 30.8, 26.3 and 18.9. "41.2" uses the definition that includes grain-fed animals; the strict plant-only reading gives 41.3, 41.2 and 40.9. The sentence says "crops alone, with pasture-fed output at its mean", which matches the builder's definition, but the paper should name the grain-fed animals as following crops.
5. **Regions sentence: supported** (21 or 22 at 1 in 10, North Tasmania at balance, 24 at 1 in 20).

## Claim rows the builder says move: my verdict

| id | Tier | Builder's "after" | Verdict |
|---|---|---|---|
| A014 | A | 30.8; 27.0 to 34.0 published, 29.2 to 32.5 herd-cycle | agree |
| A183 | A | 1.12; 0.98 to 1.23, or 1.06 to 1.18 | agree (0.977 to 1.231; 1.058 to 1.179) |
| A187 | A | 0.95; 0.83 to 1.05, or 0.90 to 1.01 | agree |
| A196 | A | holds at base only; basis to be named | agree; adopt the 1-in-20 herd-cycle wording above |
| A027 | A | 39.4 to 43.8 if herd-cycle adopted | agree (the figure is right; the adoption is Murray's choice) |
| A028 | A | 13.9 to 16.2 if adopted | agree |
| A009 | A | inside 13.9 to 16.2 if adopted | agree; 15.35 and 15.6 are inside |
| A184 | A | 21, 21 to 22 across the range | agree |
| A038 | A | probably two (Rangelands, Corangamite) | agree on the evidence: Wet Tropics leaves its average-year range on both herd-cycle sets. Still to be confirmed by `regional_flips.py`, as the builder says |
| A223 | A | unchanged; crop-only -0.8% supports it | agree (-25.8% at 1 in 10); it belongs in the Tier A table |
| A195 | B | 26.3 with ranges; 18.9 unchanged | agree |
| A188 | B | 24 at every point of either range | agree |
| A343 | B | unchanged; North Tasmania the one region inside its range | agree |
| A366 | B | four full-cycle windows if adopted | agree |

## Method points

1. **The resilience-table choice is not carried into the shock.** Half the published draws (500) have `restable` = 1, the leave-one-out table. That choice only acted on the long term because the short-term resilience is 1. B112 applies the release table's factor to every draw. If a draw's own table were applied to its shocked short-term figure (Australia 0.713504 at 10 years, 0.602007 at 20), the national ranges would be 26.27 to 33.64 million at 1 in 10 and 22.21 to 28.74 million at 1 in 20. 27.6 million would still lie inside both ranges. This is a defensible alternative, not an error: it changes no B112 number under B112's stated method, but the paper could say the table is held at the release's. My full-model rerun of draw 2 first showed 0.7135 for this reason: the copy of the script swaps in the leave-one-out table when `restable` = 1.
2. **Definition of "crop".** B112's crop-only bound counts grain-fed chicken, duck, turkey, eggs and pig meat as crop-driven, and reports the plant-only reading beside it. I agree with showing both. The difference is at most 0.43 million (1 in 100, short term).
3. **The percentile of a product.** Multiplying each draw by one national factor scales the percentiles exactly, so the national shocked range is just the published range times the factor. The regional and state ranges are the same per zone. There is no interaction to miss, apart from Northern and Yorke at 0.4%.

None of these changes a B112 number.

## Anything else found

* While running my shock script I wrote `mine_shocks.csv` into the repository root by mistake (a relative path). I moved it to the scratch folder at once; nothing in the repository is left changed by me except this report.
* The ABS historic workbook I used is the copy at `scratchpad/histdl/Historic Ag Commodities_1860 to 2022.xlsx`. Its origin in the shared scratch folder is not recorded. It reproduces every factor of the release exactly, which is good evidence that it is the right file.
* The paper_a README already carries B112's appended section. I saw its first lines while reading the Section 8 method, before deriving my figures; it gave no numbers beyond the 0.4% Northern and Yorke note.

## Register rows touched

None.

## Rerun (repository root)

```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/V38
node $S/shocks.mjs; node $S/exact.mjs; node $S/bounds.mjs; node $S/attr.mjs
python3 -I $S/factors.py
python3 -I $S/compare.py; python3 -I $S/compare2.py; python3 -I $S/compare2.py wrong; python3 -I $S/compare3.py
# full-model draws: RES=10 MC_RELEASE=2025-fixed MC_LONG=1 MC_ZONES=national node $S/mc_res.mjs $S/../b41/work OUT.csv fixed '<draw JSON>'
```

## Files read

`qa/briefs/V38_check_B112.md`, `qa/briefs/_checker_rules_results_wave.md`, `qa/briefs/B112_shock_ranges.md`, `analysis/resilience_2025/README.md` and `resilience.py` (method description and data layout only), `analysis/paper_a/README.md` (Section 8), `analysis/sensitivity_2025/evaluate.mjs`, `monte_carlo.mjs`, `summarise_mc.py` (percentile rule), and parts of `README.md`. Also `web/src/model/evaluator.js` (head), `web/public/data/2025-fixed/{model,regions}.json`, `web/public/data/2025-resilience-loo/model.json`, `web/public/data/2011-fixed/model.json`, `analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_all.csv`, `results/ranges_2025-fixed.csv` and `data/abs-2022-25/cube_*.json`. Then, last: `qa/reports/B112_shock_ranges.md`, `analysis/paper_a/shocks_ranges.csv`, `analysis/resilience_2025/drought_bounds.csv`, `results/ranges_2025-fixed_herdcycle.csv`, the two herd-cycle draw files, the herd-cycle summary `.md` (grep), `summarise_herdcycle.py` (grep), `qa/reports/R03a_response_plan_A.md` (grep) and `qa/claims_register.csv` (read only).
