# B69: small defects X068, X087, X090 to X103

Scope: prose, labels and notes in the README files and outlines the brief lists, one label in `second_build_values.csv`, and the `fixed_in` and `notes` cells of `qa/defects.csv`. No results file, evaluator, script or number was changed. No network, no subagents.

## Table

| Defect | What changed | File:line, or "left open: decision" with the one-line proposal |
|---|---|---|
| X068 | Note that the 2011-corrected State rows carry the state sum 20,686,860 against the national 22,326,388; capacities unaffected, only the over-capacity count. Release frozen. | `results/README.md:19`; `analysis/scale_curve_2025/README.md:29` |
| X087 | Left open: decision. Proposal: count every leaf item in `energy_exports.py` as `proportional_count.py` does, use 365 days as FAO does, and add a reader note that `likely_range_*` are quick ranges that differ from the Monte Carlo ranges. | none (code change) |
| X090 | `familygrams` gives the sedentary family only (short preset, not long); the table's land is the land of the diet as eaten, 0.675 against 0.19 ha per person fed for C (figure from the V21 recheck, no results file holds it); where the sha256 values are; 7.88 is the ratio of rounded figures, unrounded 7.87. The `diet_land.py` docstring (line 6) is a script file outside this brief and is left. | `analysis/nutrition_lp_2025/README.md:11`, `:116`, `:130`; `analysis/method_tests_2025/README.md:323` |
| X091 | "Short of three" reads "short of four" (four nutrients are listed). The 41 to 49 million is sourced to the one-year rows of `analysis/comparators_2025/rerun.csv` (41.5 on 2025-fixed, 49.4 on 2025-mirror). Every diet figure names its release; 5% meat and eggs is 103.3 on 2025-improved (`diet_land.csv`) and 76.8 on 2025-fixed (`diet_scale.csv`). | `analysis/nutrition_lp_2025/README.md:45`, `:34`, `:26` |
| X092 | 13.8% changed to 13.9%. The ten-choice wording is limited to the three-window run, with the all-zones runs stated as thirteen. The X069 note says the three-window run was rerun under X088 (42.5 to 52.9 and 11.4 to 13.3) and states the base column of the long-window files (48.0 and 12.3). `results/README.md` said ten input choices where the ranges files have thirteen influence columns; changed to thirteen. Left: `write_readme.py` types 13.8% (line 45) and ten choices (line 62), so a rerun would overwrite README lines 17 and 72; the `monte_carlo_longwindow_summary.csv` base column is a results file. `summarise_mc.py` already writes the count from its input list, which reads 13 in the all-zones summaries. | `analysis/sensitivity_2025/README.md:17`, `:72`, `:213`; `results/README.md:15` |
| X093 | Left open: decision. Proposal: say plainly in the footprint reading that 276 million divides local hectares by a world-average-hectare footprint with no local-productivity adjustment, and cite 76.0 (column e of `harmonised_comparison.csv`). | none |
| X094 | Eggs: 12.4 kg is the 1978-79 average carried forward; 129 eggs give about 7.3 kg (12.4 x 129 / 220 = 7.27); no verdict changes. Red-meat citation changed from Table 3 to Table 1. Build 3 poultry takes the Table A2.3 meat energy. | `analysis/method_tests_2025/README.md:38`, `:46` |
| X095 | Left open: decision. Proposal: at the results regeneration, label `land_km2` as millions of km2 (the division by 1e6 at `results-lib.mjs` line 20) or change the division, and give the unit in `results/README.md`; drop the column if Murray decides so. | none (code change) |
| X096 | Left open: decision. Proposal: where the populations are described, say the 2025 ERP of 27,608,200 is for the SA2s with land, not the national 27,613,654, and that the 2011 input 22,326,388 is 0.06% below the 2021-boundary ERP series. | none |
| X097 | Left open: decision. Proposal: keep the QCL extract that `gap_attribution.py` needs in the repository, or state in the data availability statement that the script needs the bulk file named in `qa/fao_bulk_hashes.csv` and that the table is reproducible from the committed csv. | none (code change) |
| X098 | Henry and Godden total row: residuals 8% and 22% of half a unit. The 186 kg milk base rests on an assumed 12.5% solids from ABS's 23.3 kg of solids. The Simpson (e) rows mix per-person and tonnes bases (55% and 27% on one basis, 56% and 30% as printed). Cassidy with 2000 alone: United States 27%, India 65%, China 56%, Brazil 99% (checked against `gap_attribution.csv` rows 128 to 159). | `analysis/method_tests_2025/README.md:408`, `:410`, `:412` |
| X099 | The outlines carry no EAT-Lancet, Tilman, Hunter or Tilman and Clark text, so the only addition is a caution in Paper B section 6: Willett et al. 2019 find diet change alone cuts global cropland by 0 to 2% (p. 472), so it supports diet for emissions, not cropland (register L081). `qa/reports/B17_reading.md:78` says the EAT-Lancet reference diet points the same way as the diet argument; that statement is outside this brief and is the one that register row L081 contradicts. | `papers/B_methods/OUTLINE.md:47` |
| X100 | Export-inclusive counts in group 4 are 60 (PMSEIC 2010, no source given), 61, 75 and 100, matching claim B230. Left: the notes of claim B004 (claims register, outside this brief). | `analysis/comparators_2025/README.md:98` |
| X101 | The label says the filed 307 is the pasture-only reading (331.87 Mha over 1.082 ha) and that together the figure is 277.7 (363.52 / (0.227 + 1.082) = 277.7). The label's opening words are kept because `cross_method.py` and `harmonised_comparison.py` find the row by them; a rename of those words would stop both scripts. README text says 307 is pasture alone and the range 268 to 343 is unaffected. Left: notes of claims B044 and B046. | `analysis/method_tests_2025/second_build_values.csv:3`; `analysis/method_tests_2025/README.md:107`, `:263` |
| X102 | Checked, no change needed. All six items were already in place from B60, and the docstring point is in `harmonised_comparison.py` lines 14 and 15. Figures checked against `harmonised_comparison.csv` (277.7, 9.29, 8.27). | `analysis/method_tests_2025/README.md:420`, `:422`, `:444`, `:446`, `:447`, `:449` (read, not changed) |
| X103 | Paper B section 2: Hardin and Meyer and Ausubel are described as arguing for and extending the concept; Seidl and Tisdell, Sayre, Price and Cohen as those who question it (register L044 to L049). Section 6: the Peters sentence gives what the paper finds, that diet moves capacity threefold, 2.04 to 6.08 million (L040), in place of "highly sensitive to cultivable cropland". Left: identifying the Fairlie file L041 needs the article and the register is outside this brief; Gilland's claim about Cohen is in no outline file (B62 report lines 206 and 306 record that Cohen 1995 does not say it). | `papers/B_methods/OUTLINE.md:28`, `:44` |

## Defects closed, partly closed, left open

* Closed with `fixed_in` = "B69": X068, X091, X094, X098, X099, X101.
* Closed in the permitted files, with the out-of-scope remainder named in `fixed_in`: X090, X092, X100, X103.
* Checked only, `fixed_in` unchanged: X102.
* Left open, one note line each, `fixed_in` not set to B69: X087, X093, X095, X096, X097. Their existing `fixed_in` text was written by other builders and was left as it was, not blanked.

## Register rows touched

None edited. Read to take wording from: literature L040, L044, L045, L046, L047, L048, L049, L081 (also L111, L113, L120, L142, L041 for X099 and X103); claims B004 and B230 (X100). No claim value or literature row changed.

## Files changed

* `qa/defects.csv` (cells `fixed_in` and `notes` of the 16 rows only)
* `analysis/nutrition_lp_2025/README.md`
* `analysis/method_tests_2025/README.md`
* `analysis/method_tests_2025/second_build_values.csv` (label of row 3)
* `analysis/sensitivity_2025/README.md`
* `analysis/scale_curve_2025/README.md`
* `analysis/comparators_2025/README.md`
* `results/README.md`
* `papers/B_methods/OUTLINE.md`
* `qa/reports/B69_small_defects.md` (this report)

Not changed: `papers/A_results/OUTLINE.md` and `papers/B_methods/SECTION7_DRAFT.md` (searched, nothing in them needed correcting), every `results/<release>.csv`, every script.

## Checks run

* Each stated number was checked against its file before it was written: 13.9% from `results.csv` (base 12,376,463; group-trend row 10,660,326); 7.3 kg from 12.4 x 129 / 220; 277.7 from 363.52 / 1.309; the 41.5 and 49.4 from `rerun.csv`; 76.8 from `diet_scale.csv`; Cassidy 2000-alone shares and the Henry and Godden 8% and 22% from `gap_attribution.csv`.
* After the label change the prefix lookups used by the three scripts that read `second_build_values.csv` each find exactly one row, with value 307.
* `qa/defects.csv` keeps 103 rows of 8 columns, CRLF line endings preserved; only the 16 target rows differ.
* Added text contains no em dashes and no time words.
* Not rerun (brief forbids touching scripts and results): no script was executed, so no generated table or csv was regenerated. The generated table blocks in `analysis/method_tests_2025/README.md` were not edited.

Wrong-value check: example of a wrong fix, marked as an example and not applied. Setting `analysis/sensitivity_2025/README.md` line 17 back to "13.8%", or writing "13.9" as "14.0%", would fail the check: (12,376,463 - 10,660,326) / 12,376,463 = 0.1387, which rounds to 13.9%, and the table row at line 32 of the same file reads -13.9%. A checker that recomputes the figure from `results.csv` would flag 13.8 and 14.0 and pass only 13.9.
