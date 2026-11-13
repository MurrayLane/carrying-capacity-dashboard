# V31d: second route for 54 one-route claims (decision 83)

Checker: blind checker under `qa/briefs/V31d_claims.md` and `qa/briefs/_checker_rules_results_wave.md`. Scripts and outputs are in `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/V31d/`. No register was edited. No git, no network, no subagents. Every repository script I re-ran was either read-only (stdout only) or a copy in the scratch folder with its output path pointed there. Nothing in `results/`, `releases/`, `data/` or `analysis/` was written.

## Tolerance

* Counts, labels and ratings: exact.
* Model outputs (capacities, land in km2): within 0.5%.
* Rounded figures (shares, millions, ratios as printed): within one unit of the last printed digit. Where a value is inside that tolerance but rounds to a different printed figure, I still report the correctly rounded value.

## The deliberate wrong value

`cmp.py` applies the rounded-figure rule. For A072 my value is 8,195,723. Against the stated 8.2 it passes. Against a deliberately wrong 8.4 it reports FAIL. So the check can fail. The same script showed that the rule is loose for two-decimal ratios: SA's 0.353 passes against 0.36, although the correct rounding is 0.35 (see A321).

## Routes used (shared)

* **Evaluator route.** My own node scripts call `web/src/model/evaluator.js` on `web/public/data/<release>/` (`nat.mjs`, `sums.mjs`, `scen.mjs`, `a113.mjs`, `a124.mjs`, `a324.mjs`). They do not read `results/*.csv`.
* **Script re-runs into the scratch folder.** `make-scale-curve.mjs`, `make-method-effects.mjs`, `diet_scale_test.mjs`, `regionalise.mjs` (long preset) and `resilience.py` were re-run as scratch copies with their output paths changed. The stdout-only scale scripts were re-run directly. The re-run `scale_curve.csv` is byte-identical to `results/scale_curve.csv` after sorting.
* **Own recomputation from committed inputs.** Meat-window variance share from the Monte Carlo draws (`meat_share.py`). Re-evaluation of the stored optimised diets through `server.mjs` (`nutr.py`). Cropland allocation to the 2011 Perth polygon from `data/sa2` and `data/nrm2011`.
* **Documents** for the text claims, quoted by line.

No claim in this set is tier A. Where the brief asks for two agreeing routes, my route is the second.

## Claims

### A114 (B)
Route: re-ran `nrm_vs_sa_diagnosis.mjs` (2025-fixed short).
Mine: NRM zones as built 44%; NRM rebuilt from whole SA2s (53) 44%. Register: 44. **Pass.** Status: independently verified (V31d).

### A119 (B)
Route: same re-run. My `a324.mjs` excess vector agrees: 1,957,628 km2 nationally, all of it non-agricultural land.
Mine: 1.96; SA4 3,674,201 (3.67); NRM zones as built 4,497,124 (4.50). Register: 1.96; 3.67; 4.50. **Pass.** Status: independently verified (V31d).

### A121 (B)
Route: re-ran `ideal_split_test.mjs`.
Mine: 100.0% at 0.5, 0.1 and 0.01. Register: 100.0%. **Pass.** Status: independently verified (V31d).

### A122 (B)
Route: same re-run (seeded, deterministic).
Mine: K=7 gives 100, 100, 95, 100, 100; K=53 gives 68 to 81; K=89 gives 56 to 69; K=336 gives 34 to 44. Register: 100; 68-81; 56-69; 34-44. **Pass with a note:** one of the five K=7 draws is 95%, so "about 100%" is fair but not "100%". Status: independently verified (V31d, note: one K=7 draw 95%).

### A123 (B)
Route: same re-run. `regionalise.mjs` also prints "NRM zones 33%, SA4 54% on this basis".
Mine: NRM 33, SA4 54, SA3 35, SA2 28. Register: 33; 54; 35; 28. **Pass.** Status: independently verified (V31d).

### A125 (B)
Route: re-ran a copy of `diet_scale_test.mjs` writing `diet_scale_rerun.csv` in the scratch folder.
Mine: Australia, 2.5% meat and eggs, 284%; today's 12% gives 100%. Register: 284. **Pass.** Status: independently verified (V31d).

### A133 (B)
Route: same re-run.
Mine: nation 2.5% 284 against 0% 271; states 179 against 177; SA4 0% 158 against 2.5% 136; SA3 132 against 108; SA2 best 126 against 0% 121. Register: 2.5% nation and states; 0% SA4 down; 126 against 121. **Pass.** Status: independently verified (V31d).

### A135 (B)
Route: re-ran `urban_gardens_test.mjs`.
Mine: 33 SA4s; 14.7 M; infrastructure land 10,734 of 20,154 km2; cropping 563 km2. Register: 33; 14.7; 10,700; 20,150; 563. **Pass** (rounded). Status: independently verified (V31d).

### A140 (B)
Route: re-ran `food_land_by_category.py`, which prints fruit and non-starchy vegetables at 246 m2 a person. The urban land per person is 10,734 km2 / 14.7 M = 730 m2 (the 730 m2 infrastructure rule). 10%, 25% and 50% of that are 73, 183 and 365 m2. Divided by 246 they give 29.7, 74.4 and 148.4.
Register: 30; 74; 148. **Pass.** Status: independently verified (V31d).

### A141 (B)
Route: same re-run.
Mine: fruit and non-starchy vegetables are 7.4% of the crop land a person needs. Register: 7. **Pass.** Status: independently verified (V31d).

### A324 (B)
Route: own `a324.mjs` on 2025-fixed. It reports land used against land held by type, then the same with cropland raised 25% at the pasture's expense.
Mine: short term, pasture used 3,494,216 against 3,318,689 held, so pasture excess is 0. Long term, pasture used 3,420,466 against 3,318,689, also no pasture excess. The national excess (1,957,628 km2 short; 1,400,853 long) is non-agricultural land, plus 9,944 km2 of infrastructure land in the long term. Cropland +25% leaves capacity unchanged (41.50 and 15.62 M).
Register: "unused pasture (1.8 million km2 excess nationally)".
**Fail.** There is no unused pasture in either term, and no figure of 1.8 million km2 exists in any output I produced. The second half of the claim holds: moving 25% more land into cropland changes nothing. `DISCUSSION_MEASURES.md` line 22 no longer says 1.8 either; it says the 1.96 million km2 unused is non-agricultural land.
Right text: "Pasture is fully used (need 3.49 million km2 against 3.32 held, short term); the unused land is 1.96 million km2 of non-agricultural land; raising cropland 25% at the pasture's expense leaves capacity unchanged."
Status: mismatch (V31d): no unused pasture; the excess is 1.96 million km2 of non-agricultural land.

### A325 (B)
Route: same as A141.
Mine: 7.4%. Register: 7. **Pass with a note:** the 7% is a share of the crop land a person's diet needs (fruit and non-starchy vegetables), not a share of the cropland held. Status: independently verified (V31d, note: share of crop land needed by the diet).

### A345 (B)
Route: re-ran `diet_binding_test.mjs` and own `a324.mjs`.
Mine: pasture need 3,494,216 against 3,318,689 held. Cropland used for food 140,972 of 316,499, which leaves 175,527 spare; that equals the pasture gap. Register: 3.49; 3.32 (175,000 and 141,000). **Pass.** Status: independently verified (V31d).

### A336 (C)
Route: read `papers/A_results/OUTLINE.md` line 45, which says "the Monte Carlo method is described and tested in Paper B, section 6, and only used here". `papers/B_methods/OUTLINE.md` line 48 describes the method and line 90 places it in section 6.
**Pass.** Status: independently verified (V31d).

### A340 (B)
Route: read `monte_carlo.mjs` lines 11, 127 and 145 (`tri(u('meategg'), 0.115, 0.12, 0.13)`) and the release presets. 2025-fixed short meategg is 0.12; 2011-fixed short is 0.13. The draws file has a minimum of 0.11518 and a maximum of 0.12999.
Mine: 0.115, 0.12, 0.13. Register: 0.115. **Pass.** Status: independently verified (V31d).

### A341 (B)
Route: same lines (`tri(u('redmeat'), 0.528, 0.578, 0.64)`). 2025-fixed redmeat is 0.578; 2011-fixed is 0.64. The proxy less 0.05 is 0.528.
Register: 0.528. **Pass with a note:** the unit column says "share of diet". It is the red-meat share of meat. Status: independently verified (V31d, note: unit is share of meat).

### A342 (B)
Route: `monte_carlo.mjs` line 148 draws lbench as `tri(u('lbench'), 0.30, LBENCH, 0.525)` only when `hasBench`. I read Settings!BQ4:BQ7 in each model.json. They are absent in 2025-fixed and 2025-mirror, and all four are 0.4 in 2025-improved. lbench is constant at 0.4 in the 2025-fixed and 2025-mirror draws, and spans 0.302 to 0.521 in the 2025-improved draws.
Register: 0.30, with no effect in 2025. **Pass with a note:** this holds for 2025-fixed and 2025-mirror. 2025-improved has the cells and draws the benchmark; its national effect is negligible (squared correlation with national long-term capacity 0.000). Status: independently verified (V31d, note: 2025-improved has BQ4:BQ7 and draws it).

### B116 (C)
Route: counted the columns and rows of `monte_carlo_draws_2025-fixed_all.csv` myself: 1,000 rows and 13 choice columns. The OAT files `oat_*.csv` and `rss_check.py` exist.
Register: 13; 1,000. **Pass.** Status: independently verified (V31d).

### B117 (B)
Route: own `meat_share.py` computes the correlation ratio of national short-term capacity on the three meat-window groups from the draws file, less the binning noise 2/999.
Mine: 0.806 (raw 0.808). Register: 81. **Pass.** Status: independently verified (V31d).

### B120 (B)
Route: same, long term.
Mine: 0.363 (raw 0.365). Register: 36. **Pass.** Status: independently verified (V31d).

### B250 (B)
Same as A340. **Pass.** Status: independently verified (V31d).

### B253 (B)
Route: as A342. On the draws: 12 of 13 choices vary in 2025-fixed and 2025-mirror, and 13 of 13 vary in 2025-improved.
Register: 12 of 13 (release 2025-fixed). **Pass with a note:** right for the release named. "In the 2025 releases" overstates it, because 2025-improved varies the benchmark too (with negligible national effect). Suggested wording: "12 vary in 2025-fixed and 2025-mirror; in 2025-improved the benchmark is drawn but has almost no effect". Status: independently verified (V31d, note: wording excludes 2025-improved).

### A134 (B)
Route: own `nutr.py` re-evaluates the stored optimised diets (`diets_2025-improved/1_short_*_fixcap3.json`, `g_vec`) through `server.mjs` 2025-improved. This is not a re-optimisation.
Mine: default 53.64 M; variant A 86.90 M (macronutrients) and 85.46 M (ten micronutrients). Register: 53.6 to 86.9; 85.5. **Pass with a note:** the rise is +62% (+59% with micronutrients), more than "about half". Status: independently verified (V31d, note: rise is about three fifths).

### B201 (B)
Route: same script, variants B (famcap3) and C (free).
Mine: B 202.06 (micro) and 300.55 (macro); C 422.27 (micro) and 532.86 (macro). Register: 202.1; 422.3; 301; 533. **Pass.** Status: independently verified (V31d).

### A321 (B)
Route: re-ran `resilience.py` in a scratch root, using the archive workbook `carrying-capacity-models/prelim models/resilience 150 years.xls` and the ABS historic workbook. I also read the 100-year column of the `resilience` sheet in `web/public/data/2025-resilience/model.json` directly. Both routes agree.
Mine, 2025-resilience (method "data: ABS to 2024-25", per `make_release.py`): Australia 0.456, NSW 0.300, Victoria 0.218, Queensland 0.347, SA 0.353, WA 0.471, Tasmania 0.665.
Register: 0.46; 0.30; 0.22; 0.35; 0.36; 0.49; 0.67.
**Fail.** WA is 0.47, not 0.49 (outside tolerance). SA rounds to 0.35, not 0.36 (inside the one-digit tolerance but wrongly rounded). The register's 0.359 and 0.491 are the "thesis (archive data)" table, which 2025-organic also carries, not the 2025-resilience table. The comparison still reads the same way: national 0.46 is milder than SA 0.35 and not milder than WA 0.47.
Right values: SA 0.35, WA 0.47 (Tasmania 0.665 still rounds to 0.67).
Status: mismatch (V31d): SA 0.35 and WA 0.47 on 2025-resilience; 0.36 and 0.49 are the thesis archive table.

### A317 (B)
Route attempted: re-run `analysis/reliability_2025/build_years.py` into the scratch folder with the ABS livestock files. It stops at 2016-17. `pipeline/yields/recent/livestock_zone.py` line 80 raises `KeyError: '2016-17'`, because `data/2025/livestock_national_series.csv` has no 2016-17 to 2019-20 columns.
**Cannot determine** by a second route. `years.csv` (route 1) cannot be rebuilt from the committed pipeline as it stands. That is a reproducibility finding in its own right. Status: unverified: second route blocked (V31d, build_years.py fails at 2016-17 on the current livestock series).

### A124 (C)
Route: own `a124.mjs` evaluates the committed short split `data/regions/ideal_2025-fixed_short_K53_cap650k.csv` (national yield vector). I re-ran `regionalise.mjs` 2025-fixed long 53 650000 as a scratch copy and evaluated its split the same way.
Mine: short 0.7569 (largest region 649,002 km2); long 0.6936 (largest 646,522 km2). Register: 75.7; 69.4. **Pass with a note:** the short and long figures come from two different splits, each optimised for its own term. The short split scores 0.661 in the long term. Status: independently verified (V31d, note: separate splits per term).

### A065 (B)
Route: 2011-fixed `regions.json` zone 55 Swan has land 13,536 km2 in all and cropping 5,035. For the 2011 Perth polygon (NRM 503) I summed the CLUM classes in `data/nrm2011/land_use_by_nrm2011.csv`: 3,737.6 km2. I allocated SA2 cropping (`data/sa2/land_2011_method_by_sa2.csv`) to the polygon by its share of each SA2's CLUM cropland: 29.4 km2.
Register: 13,536; 5,035; 3,738; 29. **Pass.** Status: independently verified (V31d).

### B238 (B)
Route: `papers/B_methods/SECTION7_DRAFT.md` line 13: `| **1. Food security and drought risk** | ○ | ○ | ○ | ○ | ◐ | ● | ● |`. **Pass.** Status: independently verified (V31d).

### B239 (B)
Route: same file, line 14: `| **2. Explaining why national estimates range from 9 to 100 million** | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ● |`.
Register: HALF o, PPH o. File: HALF ◐, PPH ◐. **Fail.** Right ratings: EP partly, FP partly, HALF partly, PPH partly, CB partly, FAIL partly, LDB well suited. Status: mismatch (V31d): HALF and PPH are "partly" in the matrix.

### B240 (B)
Route: same file, line 15: `| **3. Regional and local land-use planning** | ○ | ◐ | ○ | ○ | ○ | ◐ | ● |`.
Register: FP o. File: FP ◐. **Fail.** Right ratings: EP o, FP partly, HALF o, PPH o, CB o, FAIL partly, LDB well suited. Status: mismatch (V31d): FP is "partly" in the matrix.

### B241 (B)
Route: same file, line 16: `| **4. Diet change and land use** | ○ | ◐ | ● | ◐ | ○ | ○ | ● |`. **Pass.** Status: independently verified (V31d).

### A012 (B)
Route: `nat.mjs` reads the populations from `regions.json`: 22,326,388 and 27,608,200, a ratio of 1.2366 (+23.7%).
Register: 24 (22.3 to 27.6). **Pass** (rounded). Status: independently verified (V31d).

### A072 (B)
Route: `nat.mjs`, short term: 2025-fixed 41,503,537 less 2011-fixed 33,307,814 is 8,195,723.
Register: 8.2. **Pass.** Status: independently verified (V31d).

### A073 (B)
Route: `nat.mjs`, long term: 15,623,209 less 15,350,146 is 273,063.
Register: 0.27. **Pass.** Status: independently verified (V31d).

### A094 (B)
Route: own `sums.mjs` (the seven states on the release land) gives 31.28 / 41.50 = 75.4%. The scratch re-run of `make-scale-curve.mjs` gives 0.754.
Register: 75. **Pass.** Status: independently verified (V31d).

### A098 (B)
Route: scratch re-run of `make-scale-curve.mjs`, SA2 local basis: 22,365,734 / 41,503,535 = 0.539.
Register: 54. **Pass.** Status: independently verified (V31d).

### A106 (B)
Route: `sums.mjs` on 2011-corrected short: national 40.45, states 28.28, the 53 regions 23.01. The published paper is not on disk. Register L013 `what_taken` records 40.4, 28.2 and 22.9 from it.
Register: 40; 28; 23. **Pass with a note:** these are the published-method figures. On the corrected method (2011-fixed) they are 33.3, 25.7 and 21.0. The shape survives the corrections; the numbers do not. Status: independently verified (V31d, note: corrected method 33.3, 25.7, 21.0).

### A108 (B)
Route: scale-curve re-run, SA2 short: local 0.539, state 0.374.
Mine: 16.5 points. Register: 17 (54 against 37). **Pass with a note:** 16.5 unrounded; 17 only from the rounded shares. Status: independently verified (V31d, note: 16.5 points unrounded).

### A111 (C)
Route: scale-curve re-run. On the local basis, 2025-fixed short gives NRM region (53 units) 0.627 against SA4 (89 units) 0.799, so more units do not always mean a smaller sum. **Pass.** Status: independently verified (V31d).

### A113 (B)
Route: own `a113.mjs`. The 2011-fixed national short is 33.3, which confirms the 33. The rejected method is not in the repository. Two reconstructions give 46.6 (mean over all 53 regions, weighted by cropland) and 73.0 (mean over the regions that grow each crop, weighted by cropland). Neither gives 77.
**Cannot determine** the 77. The direction (inflation) is reproduced. Status: unverified: rejected method not committed (V31d; 33 confirmed, 77 not reproduced, nearest reconstruction 73.0).

### A207 (B)
Route: own `scen.mjs` from `scenarios/scenarios.json` and the evaluator (national, 2025-improved reference 53.64 M short).
Mine: waste-target-6 short +8.67%. Register: 8.67%. **Pass.** Status: independently verified (V31d).

### A217 (B)
Route: same script.
Mine: fuel-csiro-340 short 0.00% (long -18.75%). Register: 0%. **Pass.** Status: independently verified (V31d).

### A225 (B)
Route: same script, long term.
Mine: grain-store-1 +48.27%, grain-store-2 +64.21%. The largest other magnitude is fuel-csiro-340 at -18.75%. **Pass with a note:** this holds among the named scenarios only (the register note already says so). Status: independently verified (V31d, note: named scenarios only).

### A227 (B)
Route: same script.
Mine: recycling-none short -0.11%, long -0.23%; recycling-half short -0.06%, long -0.12%. Register: -0.1; -0.1 to -0.2. **Pass** (rounded). Status: independently verified (V31d).

### A314 (C)
Route: `nat.mjs`: 2025-improved less 2025-mirror is 4,254,317 short and 4,349,487 long. A scratch re-run of `make-method-effects.mjs` gives, summed by me: effect_alone 7,133,291 (short) and 1,153,459 (long), so the interactions are -2,878,974 and +3,196,028. For 2011 the interactions are -2,238,001 and -1,383,468.
Register: -2.88; +3.20 (4.25, 7.13, 4.35, 1.15). **Pass.** Status: independently verified (V31d).

### A328 (B)
Route: `nat.mjs`. 41,503,537 / 33,307,814 = 1.2461; population ratio 1.2366.
Register: 24.6; 23.7. **Pass.** Status: independently verified (V31d).

### B094 (B)
Route: 2025-fixed `regions.json` zone 1 population is 27,608,200. Register: 27.6. **Pass.** Status: independently verified (V31d).

### B129 (B)
Route: 2011-fixed `regions.json` zone 1 population is 22,326,388. Register: 22.3. **Pass.** Status: independently verified (V31d).

### B135 (B)
Route: `nat.mjs`: 2011-fixed 1.4919, 2025-fixed 1.5033. Register: 1.5. **Pass.** Status: independently verified (V31d).

### B171 (B)
Route: `sums.mjs` 75.4%; scale-curve re-run on the state basis gives 0.754. Register: 75. **Pass.** Status: independently verified (V31d).

### B174 (B)
Route: scale-curve re-run, SA3 state basis: 18,202,613 / 41,503,535 = 0.439. Register: 44. **Pass.** Status: independently verified (V31d).

### B229 (B)
Route: `nat.mjs` and `sums.mjs` on 2011-thesis: short 40.44, long 9.43, the 53 regions short 22.95. Register: 40; 9 to 40; 23. **Pass.** Status: independently verified (V31d).

### B234 (C)
Route: `papers/B_methods/OUTLINE.md` lines 43 to 46 put the six module ids under three design choices: yield basis (regional-beef-output, dairy-good-land, organic-ruminant-factor), waste (loss-factors-australia, recycling-stage) and land base (reserve-pro-rata). `methods/README.md` lines 39 to 43 class them as improvements, and all six folders exist under `methods/`.
**Pass with a note:** the claim has three choices and six modules. The organic factor is long term only (OUTLINE line 44). Status: independently verified (V31d, note: six modules under three choices).

## Summary

| id | tier | verdict |
|---|---|---|
| A114 | B | pass |
| A119 | B | pass |
| A121 | B | pass |
| A122 | B | pass with a note |
| A123 | B | pass |
| A125 | B | pass |
| A133 | B | pass |
| A135 | B | pass |
| A140 | B | pass |
| A141 | B | pass |
| A324 | B | fail |
| A325 | B | pass with a note |
| A345 | B | pass |
| A336 | C | pass |
| A340 | B | pass |
| A341 | B | pass with a note |
| A342 | B | pass with a note |
| B116 | C | pass |
| B117 | B | pass |
| B120 | B | pass |
| B250 | B | pass |
| B253 | B | pass with a note |
| A134 | B | pass with a note |
| B201 | B | pass |
| A321 | B | fail |
| A317 | B | cannot determine |
| A124 | C | pass with a note |
| A065 | B | pass |
| B238 | B | pass |
| B239 | B | fail |
| B240 | B | fail |
| B241 | B | pass |
| A012 | B | pass |
| A072 | B | pass |
| A073 | B | pass |
| A094 | B | pass |
| A098 | B | pass |
| A106 | B | pass with a note |
| A108 | B | pass with a note |
| A111 | C | pass |
| A113 | B | cannot determine |
| A207 | B | pass |
| A217 | B | pass |
| A225 | B | pass with a note |
| A227 | B | pass |
| A314 | C | pass |
| A328 | B | pass |
| B094 | B | pass |
| B129 | B | pass |
| B135 | B | pass |
| B171 | B | pass |
| B174 | B | pass |
| B229 | B | pass |
| B234 | C | pass with a note |

Totals: 36 pass, 12 pass with a note, 4 fail (A324, A321, B239, B240), 2 cannot determine (A317, A113).

## FAOSTAT year finding

Did not arise. None of the 54 claims rests on a FAOSTAT food balance year beside a FAOSTAT crops year.

## Other findings

* `build_years.py` (reliability_2025) does not run on the committed data: `data/2025/livestock_national_series.csv` lacks 2016-17 to 2019-20, so `livestock_zone.py` fails with KeyError at 2016-17. `years.csv` is not reproducible as committed.
* A321: the resilience README table and the register row quote the thesis-archive 100-year factors for SA and WA, not those of 2025-resilience.
* `food_land_by_category.py` and the urban gardens test were read-only. `diet_scale_test.mjs`, `make-scale-curve.mjs`, `make-method-effects.mjs`, `regionalise.mjs` and `resilience.py` write into the repository by default; they were run only as scratch copies.

## Register rows touched

None.

## Ids checked

A114, A119, A121, A122, A123, A125, A133, A135, A140, A141, A324, A325, A345, A336, A340, A341, A342, B116, B117, B120, B250, B253, A134, B201, A321, A317, A124, A065, B238, B239, B240, B241, A012, A072, A073, A094, A098, A106, A108, A111, A113, A207, A217, A225, A227, A314, A328, B094, B129, B135, B171, B174, B229, B234.

## Rerun commands (repository root unless stated)

```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/V31d
node $S/nat.mjs 2011-fixed 2025-fixed 2011-thesis 2011-corrected 2025-improved 2025-mirror 2011-improved
node $S/sums.mjs 2011-thesis 2011-corrected 2011-fixed 2025-fixed
node $S/scen.mjs ; node $S/a324.mjs ; node $S/a113.mjs 2011-fixed 2025-fixed
node $S/a124.mjs $PWD/data/regions/ideal_2025-fixed_short_K53_cap650k.csv ; node $S/a124.mjs $S/ideal_long.csv
python3 -I $S/meat_share.py analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_all.csv
python3 -I $S/nutr.py ; python3 -I $S/cmp.py
(cd web && for f in nrm_vs_sa_diagnosis ideal_split_test urban_gardens_test diet_binding_test; do node ../analysis/scale_curve_2025/$f.mjs; done)
(cd web && node $S/diet_scale_copy.mjs && node $S/scale_copy.mjs && node $S/me_copy.mjs && node $S/regionalise_copy.mjs 2025-fixed long 53 650000)
python3 -I analysis/scale_curve_2025/food_land_by_category.py
(cd $S/resil_root && python3 -I /home/user/carrying-capacity-dashboard/analysis/resilience_2025/resilience.py "/home/user/carrying-capacity-models/prelim models/resilience 150 years.xls" "$S/../histdl/Historic Ag Commodities_1860 to 2022.xlsx")
```
