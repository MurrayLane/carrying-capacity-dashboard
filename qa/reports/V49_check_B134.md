# V49: blind check of B134 (the Paper B drought bound, pasture output and PAL one at a time)

Checker report. No git, no subagents, no network. The only repository file written is this report; my code is in the session scratch folder (`v49/check.mjs`, `v49/resid.mjs`, `v49/extra.mjs`, `v49/cmp.py`). I derived every figure below with my own evaluator calls before opening `qa/reports/B134_paper_B_drought_bound_and_pasture.md` or any B134 output.

## Tolerance

Capacities within 0.5%; counts and names exact; shares, ratios, factors and percentages within one unit of the last printed digit; Sobol indices to the printed digit.

## Wrong-value example

EXAMPLE (deliberate wrong value): I fed my comparison script a builder value of 40.85 million for the crop-only short-term capacity at 1 in 100 against my 40.45. `python3 -I cmp.py --wrong` printed `FAIL` for that row (1.0% off, beyond 0.5%) and exited 1; the six true rows passed.

## My route and figures (2025-fixed, Australia, region 1)

Row groups were set by the Yield sheet labels, not copied from B112: plant 118 rows, grain-fed animal 5 (chicken, duck, turkey, eggs, pig), pasture-fed 6 (sheep meat, wool, dairy milk, cattle meat, goat milk, sheep milk), other 6 (fish, seafood, honey, wild fish, timber). The factors are read from `resilience` row 3 (Australia). "Crop only" scales plant and grain-fed rows. The both-applied runs equal the model run at each return period in every case.

### 1. Drought bound

| Preset, return period | Factor | Both applied (model) | Crop only |
|---|---|---|---|
| short, 1 (average) | 1 | 41.504 | 41.504 |
| short, 1 in 5 | 0.892291 | 37.033 | 41.394 |
| short, 1 in 10 | 0.742361 | 30.811 | 41.192 |
| short, 1 in 20 | 0.634262 | 26.324 | 40.988 |
| short, 1 in 50 | 0.552352 | 22.925 | 40.782 |
| short, 1 in 100 | 0.455821 | 18.918 | 40.450 |
| long, average | 1 | 34.275 | 34.275 |
| long, 1 in 100 | 0.455821 | 15.623 | 24.682 |

B112's 41.2, 41.0, 40.4 against 30.8, 26.3, 18.9, and 24.7 against 15.6, are confirmed.

Drought factor (average year over 1 in 100): short 2.194 both applied, 1.026 crop only; long 2.194 and 1.389.

Share of the fall carried by the rows the crop-only rule holds at the mean ((crop only less both) over (average less both)): short 97.1% at 1 in 10, 95.3% at 1 in 100; long 93.1% and 48.6%. Those held rows are pasture-fed plus fish, seafood, honey and timber. Pasture-fed rows alone, by two readings: scaling every row but the pasture-fed ones, short 95.5% and 92.8% (long 93.1% and 48.6%); scaling the pasture-fed rows alone, short 97.4% and 98.4%. So the short-term pasture share is 93% to 98% depending on the reading, and the long term at 1 in 100 is about half (cropland binds there).

Failure probability at 27,608,200, interpolation as in `fearnside_failure_curve.py` (points at T = 1, 5, 10, 20, 50, 100; same result from points rounded to 0.01 million and unrounded):

| Preset, rule | Return period (linear to log) | Failure probability a year |
|---|---|---|
| short, both | 17.1 to 16.4 | 5.84 to 6.10% (5.8 to 6.1) |
| short, crop only | curve stays above the population at 1 in 100 (40.45) | below 1%; a bound at the last run point, no figure without extrapolation |
| long, both (not printed by Paper B) | 7.9 to 7.5 | 12.7 to 13.4% |
| long, crop only (not printed by Paper B) | 69.8 to 65.8 | 1.4 to 1.5% |

What the crop-only curve supports: on the short-term curve Paper B uses, only "below 1% a year" (failure rarer than 1 in 100); a point estimate needs a run past 1 in 100.

Release 2025-improved (extra): crop only 53.47, 53.15, 52.83, 52.51, 51.99 at 1 in 5 to 1 in 100, long 20.69; the row-scaling rule differs from the release's own run from 1 in 20 (34.156 against 34.277, 29.771 against 29.877, 24.593 against 24.681; long 18.481 against 18.496), as the builder flags.

### 2. Pasture output one at a time (short term, pasture-fed yield rows scaled)

| Pasture output | Model | Change | Cropland used | Closed form, base needs (`pairing_relaxed.py` frame) | Closed form, evaluator's needs at that output |
|---|---|---|---|---|---|
| minus 20% | 33.431 | -8.073 (-19.45%) | 37.0% | 33.462 | 33.431 |
| base | 41.504 | 0 | 44.5% | 41.504 | 41.504 |
| plus 20% | 49.467 | +7.963 (+19.19%) | 52.0% | 49.421 | 49.467 |

Pasture binds at both ends (the pool of pasture plus idle cropland is full; cropland is never full). The residual of the base-needs closed form (+0.031 million at minus 20%, -0.046 at plus 20%, about 0.1%) is the cropland need for oils and fats, Settings!C45, which contains butter (Base row 266, dairy milk yield, Yield!B97) and so moves with pasture output: 481.8 m2 a person at base, 585.8 at minus 20%, 412.5 at plus 20% (about 416 m2 of it scales as 1 over the factor). With the evaluator's whole cropland and pasture need (Settings!C53:D53) the closed form equals the model to 4 decimals. Long term (preset settings, so 1 in 100): 12.630 and 18.555 against 15.623; pasture binds.

### 3. PAL one at a time (food = PAL / 1.4, everything else at base)

| Release, preset | PAL 1.2 | PAL 1.4 | PAL 1.8 | PAL 2.2 |
|---|---|---|---|---|
| 2025-fixed, short | 47.998 (+15.6%) | 41.504 | 32.664 (-21.3%) | 26.929 (-35.1%) |
| 2025-fixed, long | 16.980 (+8.7%) | 15.623 | 13.470 (-13.8%) | 11.839 (-24.2%) |
| 2025-improved, short | 61.767 (+15.1%) | 53.644 | 42.473 (-20.8%) | 35.153 (-34.5%) |
| 2025-improved, long | 19.900 (+7.6%) | 18.496 | 16.210 (-12.4%) | 14.427 (-22.0%) |

Window 1.4 to 1.8: factor 1.271; NHMRC range 1.2 to 2.2: 1.782. The evaluator's diet energy (food groups, from Base) is 7.38 MJ a day short term at every food amount (the food amount acts downstream); the 8.0 MJ the builder uses comes from `analysis/nutrition_lp_2025/README.md`, which counts drinks (271 g a day) as well. The MJ labels (6.86, 8.00, 10.29, 12.57) are 8.0 x PAL / 1.4, not model outputs; consistent with the project's documented figure, not checkable from the evaluator.

## Comparison with the builder (opened after the above)

| Item | Builder | Mine | Verdict |
|---|---|---|---|
| Short both 1 in 5/10/20/50/100 | 37.03, 30.81, 26.32, 22.92, 18.92 | 37.033, 30.811, 26.324, 22.925, 18.918 | pass |
| Short crop only 1 in 5/10/20/50/100 | 41.39, 41.19, 40.99, 40.78, 40.45 | 41.394, 41.192, 40.988, 40.782, 40.450 | pass |
| Plant rows only (csv) | 41.32 at 1 in 10, 40.88 at 1 in 100 | not run as a separate column | not checked |
| Long 1 in 100 both, crop only | 15.62, 24.68 | 15.623, 24.682 | pass |
| Percent below average, short 1 in 100 / long | 54.4 / 2.5; 54.4 / 28.0 | 54.4 / 2.5; 54.4 / 28.0 | pass |
| Drought factor both, crop only, long crop only | 2.194, 1.026, 1.389 | 2.194, 1.026, 1.389 | pass |
| Share of fall from pasture-fed output | 97% (1 in 10), 95% (1 in 100) | 97.1%, 95.3% as (crop less both) over fall; pasture alone 93% to 98% | pass on the arithmetic; wording, see below |
| Failure, short both | 17 to 16 yr; 5.8 to 6.1% | 17.1 to 16.4; 5.84 to 6.10% | pass |
| Failure, short crop only | below 1% (bound at last run point) | below 1% | pass |
| Improved crop only 1 in 5 to 100 | 53.47, 53.15, 52.83, 52.51, 51.99 | same | pass |
| Improved rule against own run | -121,491, -105,983, -87,639, -14,943 | -0.121, -0.106, -0.088, -0.015 million | pass |
| Improved both failure | 71 to 67 yr, 1.4 to 1.5% | not computed (approximate rule) | not checked |
| Pasture minus 20%, model | 33,430,993 (-19.45%) | 33.431 (-19.45%) | pass |
| Pasture plus 20%, model | 49,466,640 (+19.19%) | 49.467 (+19.19%) | pass |
| Pasture closed form, base needs | 33.4624, 49.4209 | 33.462, 49.421 | pass |
| Pasture closed form, with oils | 33.4304, 49.4676 | 33.431, 49.467 (all needs from evaluator) | pass |
| Oils cropland m2 a person | 585.82, 481.83, 412.50 | 585.82, 481.83, 412.50 | pass |
| Cropland used share | 0.3698, 0.4454, 0.5200 | 0.3698, 0.4454, 0.5200 | pass |
| Pasture binds, both ends | yes | yes | pass |
| Pasture long term | 12.630, 18.555 | 12.630, 18.555 | pass |
| PAL, all 16 cells | as in my table | same to the person shown | pass |
| PAL factors | 1.27, 1.78 | 1.271, 1.782 | pass |
| Energy MJ labels | 6.86, 8.00, 10.29, 12.57 | evaluator food-group energy 7.38 MJ at base | pass with note (8.0 is the README figure with drinks) |
| Sobol meat window short, long | 0.24 (0.21 to 0.27), 0.14 (0.12 to 0.16) | 0.2413 (0.2137 to 0.2673), 0.1413 (0.1208 to 0.1619) | pass |
| Sobol meat calibration short, long | 0.03 (0.02 to 0.04), 0.01 (0.01 to 0.02) | 0.0337 (0.0241 to 0.0432), 0.0141 (0.0080 to 0.0205) | pass |
| Long-term energy index | 0 | 0.0 | pass |
| B193 factors to 62.9 | 2.55, 1.56 | 2.549, 1.555 | pass |

No number moves.

## Proposed paper sentences: overclaim check

1. **S5, first sentence: overclaims.** "Pasture output is national meat output ... so its uncertainty is the window ... and the calibration ..., and both are drawn." Pasture output in the model also includes dairy milk (12,424 of 84,191 pasture m2 a person, short term, about 15%) and wool (4,513, about 5%), which come from the wool and milk series, not meat output; the sensitivity README lists those series as "not varied" with "no second source to set a range", and the meat calibration scales sheep and cattle meat only. Suggested: "Pasture-fed meat output is national meat output shared among zones by dry sheep equivalent; the window of herd and meat data and the calibration of the ABS meat tables are drawn (indices ...); the wool and milk series are not." The Sobol values themselves are right, and they are shares of capacity variance, not a measure of pasture uncertainty.
2. **S5, second sentence: "this is a bound" overclaims.** Plus and minus 20% is a chosen width with no source; the result is an illustration of sensitivity (elasticity about 0.96 to 0.97), not a bound on the undrawn deviation. Suggested: "an illustration at 20% either way, not a bound and not a range with a probability."
3. **Section 6.6: "97% of it at 1 in 10, 95% at 1 in 100" from "applying a cereal factor to pasture-fed output".** Holds for the short term only, and the figure counts fish, seafood, honey and timber with the pasture-fed rows; pasture alone is 93% to 98% by reading. The sentence sits beside the long-term 24.7 against 15.6, where the share is 49%. Suggested: "in the short term, about 95% of it (93% to 98% by how the pasture rows are separated); in the long term at 1 in 100, about half".
4. **Section 5.8 and abstract:** the crop-only figures and "below 1% a year" are stated correctly as bounds. Add "short term" to the failure-probability sentence. The abstract's 1.58 and section 6.11's land base 1.09 were not in my route: not checked.
5. **Table 8 crop-only row (1.03) and the S5 PAL sentence (48.0, 26.9, 1.27, 1.78):** hold.

## Claim rows the builder says move (Tier A)

| Row | Builder proposal | Verdict |
|---|---|---|
| B001 | 18.9 model rule; 40.4 crop only | holds |
| B003 | 18.9 (40.4 crop only) and 55.3 as two separate changes | holds for 18.9 and 40.4; 55.3 not in my route |
| B096 | keeps 30.8; companion 41.2 | holds |
| B130 | keeps 5.8 to 6.1%; adds below 1% crop only | holds (add "short term") |
| B137 | adds crop-only low end 40.45 | holds |
| B167 | keeps 2.19; adds 1.03 (1.026) | holds |
| B188 | 1.03 below land base 1.09 and below 1.58 | 1.03 holds; 1.09 and 1.58 not checked |
| B193 | crop-only factors 2.55 and 1.56 to 62.9 | holds (62.9 taken as given) |

Tier B rows I reproduced: B095, B097, B098 companions (41.4, 41.0, 40.8); B099 to B103 improved companions (53.5, 53.2, 52.8, 52.5, 52.0, approximate); B134 (0.8% and 2.5%); B247 (pasture binds at both ends); B369, B371 (48.0, 26.9). B157 range 31.1 to 49.2 not checked.

## What I would do differently

* Report the pasture-fed share of the drought fall with its definition and preset, as a range (93% to 98% short term), not as 97% and 95%.
* Name the butter row (Base row 266, Yield!B97) as the reason the oils cropland moves, and close the closed form with the evaluator's whole cropland need (C53), which leaves no residual, instead of leaving 0.002% "not traced".
* State in the PAL output that the MJ column is the README's 8.0 MJ (with drinks) scaled, not an evaluator output.
* Builder note correct: `analysis/sensitivity_2025/rerun.mjs` does not exist.

## Register rows touched

None.

## Rerun

From the repository root: `node <scratch>/v49/check.mjs`, `node <scratch>/v49/resid.mjs`, `node <scratch>/v49/extra.mjs`, `python3 -I <scratch>/v49/cmp.py --wrong`.

## Files read

`qa/briefs/V49_check_B134.md`, `qa/briefs/_checker_rules_results_wave.md`, `qa/briefs/B134_paper_B_drought_bound_and_pasture.md`, `web/src/model/evaluator.js`, `web/public/data/2025-fixed/` and `2025-improved/` (model.json, regions.json), `analysis/sensitivity_2025/evaluate.mjs`, `analysis/resilience_2025/drought_bounds.mjs` and `.csv` (B112), `analysis/method_tests_2025/fearnside_failure_curve.py` and `.csv`, `analysis/comparators_2025/rerun.csv`, `analysis/pasture_2025/pairing_relaxed.py`, `pairing_relaxed_inputs.mjs`, `pairing_relaxed_inputs_2025-fixed.csv`, `analysis/sensitivity_2025/sobol_2025-fixed.csv`, `analysis/sensitivity_2025/README.md` (grep), `analysis/nutrition_lp_2025/README.md` (grep); then the builder's report and its CSVs (`drought_bounds_paper_B.csv`, `fearnside_failure_curve_crop_only.csv`, `pal_one_at_a_time_2025.csv`, `pasture_output_one_at_a_time_2025-fixed.csv`, `pasture_output_one_at_a_time_closed_form_2025-fixed.csv`) and one grep of `pal_one_at_a_time.mjs`. The builder's scripts were not run.
