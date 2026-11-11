# B77: stale claim rows and gap-attribution claims (decisions 63, 65)

Files written: `qa/claims_register.csv` and this report. No git, no network, no subagents. Register went from 623 data rows to 685 (7 Paper A rows added, 55 Paper B rows added, 7 rows corrected). Line endings stay CRLF throughout; no em dashes.

## Part 1: rows corrected

| Row | What was wrong | What it says now | File and cell checked |
|---|---|---|---|
| A119 | NRM zones' unused land given as 4.80 million km2. | 1.96 nationally, 3.67 for the SA4s, 4.50 for the NRM zones. 4.50 is right: the script prints 4,497,124 km2 for the NRM zones as built (4,490,416 when rebuilt from whole SA2s). Nothing in the script gives 4.80. | `analysis/scale_curve_2025/nrm_vs_sa_diagnosis.mjs` run on 2025-fixed short term (national 1.96, SA4 3,674,201, NRM 4,497,124); `analysis/scale_curve_2025/README.md` line 38 |
| A124 | Said the achievable contiguous split is not known. | Best contiguous split found at 53 regions, 650,000 km2 cap: 75.7% of national capacity short term, 69.4% long term (heuristic, so a lower bound). Script, output file and sources filled in. Tier left at C. | `analysis/regionalise_2025/summary.csv`, K=53, area_max_km2=650000, column sum_capacity_share_of_national (0.757 short, 0.694 long) |
| A140 | Garden shares 27, 68, 136%. | 30, 74, 148%. 73, 183 and 365 m2 over the 246 m2 the script prints give 29.7, 74.4, 148.4. The old figures match nothing in the README or the script output. | `analysis/scale_curve_2025/food_land_by_category.py` run (246 m2); README line 61 |
| A225 | "any other single setting". | "A grain store is worth more than any other named scenario in the long term." Checked: grain-store-1 +48.27%, grain-store-2 +64.21%, every other named scenario under 20% in magnitude. The note keeps the finding that the drought allowance (+120%) is larger. | `analysis/paper_a/scenarios_by_region.csv`, term=long, column "change on reference" |
| A314 | Said the interaction is small. | The interaction is not small nationally: 2025 short term +4.25 million together against 7.13 alone, interaction -2.88 million; 2025 long term +4.35 against 1.15 alone, interaction +3.20 million. Value now "-2.88; +3.20". | `results/method_effects.csv`, zone=1, vintage 2025, columns effect_total, interaction, and the sum of the effect_alone columns (7,133,291 and 1,153,459); also `results/README.md` and `analysis/paper_a/README.md` limits |
| A333 | "2 of 8" figures exist. | "3 of 8": Figures 4, 7 and 8 have scripts and images (`plot_scale_curve.py`, `plot_method_effects.py`, `migration_map.py`); Figures 1, 2, 3, 5, 6 have none; Figure 2 needs region polygons, which the repository does not hold. | `analysis/` file listing; `analysis/paper_a/migration_map.py` line 5 |
| B243 | Every checklist item "moved the answer by more than 1.2 times". | Of items 2 to 8 (the seven design choices), those over 1.2 are exports 2.41, diet 2.14, weather 2.19, unit 2.67, time frame 2.66. Waste is 1.33 (corrected) and 1.17 (improved); the land base is 1.09. Items 1 and 9 to 12 are not design choices and carry no ratio. Now has script, output file and locator. | `analysis/method_tests_2025/design_choices.csv`, column "high over low" |

## Tier A rows left for Murray

None. Every row corrected is Tier B or C (A119 B, A124 C, A140 B, A225 B, A314 C, A333 C, B243 B), and no Tier A value in the register changed (checked by comparing old and new file: the only changed ids are those seven).

Findings outside the two files I may write, for Murray to decide:
1. `analysis/scale_curve_2025/README.md` line 47 still says the SA2 boundaries are not in the repository and the contiguous value is not known; `data/sa2/adjacency.csv` and `analysis/regionalise_2025/summary.csv` show otherwise. Decision row: correct that README line (small).
2. The regionalise README gives the NRM zones 33% (national-yield vector, A123) while `results/scale_curve.csv` and `design_choices.csv` give 44% (state-yield basis). Both are right on their own basis; A353 records the basis in its note. Decision row: whether the paper quotes one basis only (small).

## New rows

Paper A, Tier B, unverified, script `analysis/regionalise_2025/regionalise.mjs`, output `analysis/regionalise_2025/summary.csv`:
A347 (cap 513,391, 57.9%), A348 (cap 1,300,000, 91.9%), A349 (no cap, 99.9%), A350 (89 regions, 63.3% short and 63.6% long), A351 (336 regions, 49.5%), A352 (11 to 13 regions under the land floor), A353 (76% against NRM 33%, depends on A123 and A124). Not registered: the README's "gains of 9 and 14 points over SA4 and SA3", because 49.5 less 35 is 14.5 and the SA3 figure is a rounded typed value.

Paper B, Tier B, unverified, script `analysis/method_tests_2025/gap_attribution.py`, output `analysis/method_tests_2025/gap_attribution.csv`: B278 to B332 (55 rows).
* B278 to B317: the 40 rows of the README "Gap attribution" table, in table order (HALF 17, Simpson 6, Henry and Godden 4, Foran and Poldy 5, Cassidy 8). Each row holds the figure with the cause, this test's figure, the published figure and the share of the residual explained, from the csv cells named in its locator.
* B318 to B332 (15 rows): figures the section's prose quotes that are in the csv but not the table. B318 and B319: HALF inputs (cropland, harvested area, pasture, the derived adjustment 1.165) and feed pool and feed cropland. B320: HALF causes each under 8% of residual. B321 and B322: Henry and Godden half-unit shares and totals, and the rounding-edge figures. B323 to B325: Simpson 34.00 and 33.22, the retail-weight range, and the milk reading. B326 to B328: Foran and Poldy residuals, three-year means, and cereals plus pulses with the listed meats. B329 to B332: Cassidy 2000-alone shares, the grain-fed share maximum, the calorie basis, and the 22 to 42% range.
Not registered, with reason: the HALF figures "six times", "a quarter to a third", and the V25 re-based shares 55% and 27%, because they are derived or come from a report, not a csv cell.

## Checks

* Parse: the register parses with Python's csv module; every row has 18 fields; ids are unique.
* Count: 623 before, 685 after = 623 + 7 (A347 to A353) + 55 (B278 to B332).
* No em dashes or en dashes in the file; no bare line feeds (686 CRLF line ends, header plus 685 rows); an untouched-row round trip reproduced every original line byte for byte before writing.
* Tier A: no Tier A row changed.
* Time words: none of the banned words in new or changed text.

Wrong-value check (example of a correction that would itself be wrong, not made): changing A119 from 4.80 to 4.49 because the "NRM rebuilt from whole SA2s" line prints 4,490,416. That line is a different partition (an approximate rebuild with the first SA2's state zone); the README and the register mean the NRM zones as built, 4,497,124, which is 4.50.
