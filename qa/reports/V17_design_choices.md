# V17 report: the design-choice table and the diet figures (methods paper, section 6)

## Tolerance and the test that the check can fail

Set before comparing: counts and names must match exactly; capacities within 0.5%; factors and shares within one unit of the last printed digit (0.01 for a factor printed to two decimals).

Deliberate wrong value: with `INJECT_WRONG=1`, `partA.mjs` replaces the drought factor with 2.50. It then printed `drought allowance,41.50,18.92,2.50,2.19,MISMATCH`, so the comparison reports a mismatch when one exists. The diet row also came out MISMATCH on the honest run (see A6).

## A. Each design choice as a factor

All runs are Australia (region 1) through `Evaluator.evaluate` with the release's own short or long preset and only the named input changed.

| # | Choice | My values (million) | My factor | Stated | Verdict |
|---|---|---|---|---|---|
| A1 | Drought allowance, resilience 1 against 100 (fixed) | 41.50 / 18.92 | 2.19 | 41.5, 18.9, 2.19 | holds |
| A2 | Avoidable waste, losses 0.12 against 0 (fixed) | 41.50 / 55.29 | 1.33 | 41.5 to 55.3, 1.33 | holds |
| A3 | The same on improved | 53.64 / 62.92 | 1.17 | 53.6 to 62.9, 1.17 | holds |
| A4 | Land: cropland doubled, taken from non-agricultural land (fixed) | 41.50 / 45.12 | 1.09 | 1.09 | holds |
| A5 | Unit: nation against the SA2 sum (scale_curve, 2025-fixed, short, state basis) | 41.50 / 15.53, share 0.374 | 2.67 | 15.5 against 41.5, 2.67, 37% | holds |
| A6 | Diet: guideline 15% against 5% meat and eggs (improved) | 48.33 / 103.28 | 2.14 | 48.2 to 100.3, 2.08 | **does not hold** with meategg set directly; holds (48.18 / 100.26, 2.08) only on the nutrition server's grams route (see B) |
| A7 | Default diet against diet C (improved) | 53.64 (direct) or 53.50 (grams route) / 342.50 (C as the nutrition model now produces it) | 6.39 (6.40 on 53.5) | 53.6 to 248.7, 4.65 | **does not hold**: 248.7 cannot be reproduced (see B and C). The stated pair is also inconsistent with itself: 248.7/53.6 = 4.64; 4.65 needs 53.5, which is the value in the CSV |
| A8 | Australian settings: fixed against improved, short | 41.50 / 53.64 | 1.29 | 1.29 | holds |
| A9 | Time frame: long against short (fixed) | 15.62 / 41.50 | 2.66 | 15.6 to 41.5, 2.66 | holds |
| A10 | Exports counted, proportional 100 | 41.50 / 100 | 2.41 | 2.41 | holds |
| A11 | Exports by energy, 258.1 (energy_exports.csv) | 41.50 / 258.1 | 6.22 | 6.22 | holds |
| A12 | Uncertainty p5 to p95 (ranges_2025-fixed.csv, zone 1, short) | 36.33 / 45.76 | 1.26 | 36.3 to 45.8, 1.26 | holds |

The drought sweep for the ladder (fixed, short) gives 41.50, 37.03, 30.81, 26.32, 22.92 and 18.92 at 1, 5, 10, 20, 50 and 100 years. All match `rerun.csv` and the ladder's 30.8.

## B. The three diet figures (improved release, short term)

* **Guideline 15% and 5% meat and eggs.** These are the Diet sheet's sedentary guideline diets.
  * **Direct evaluation**, changing only `meategg` (0.15 or 0.05; `redmeat` 0.578 and `activity` 1 are already the preset's values): 48.33 and 103.28. Against 48.2 that is 0.27%, within tolerance. Against 100.3 it is 3.0%, **outside tolerance**.
  * **Nutrition server's grams route** (`server.mjs` `familygrams`, then `eval`): this is what reproduces the stated figures, 48.18 and 100.26. The route works in three steps:
    1. It sets `meategg` to the diet's share, with `redmeat` 0.578 and `activity` 1.
    2. It reads the grams of each of the 178 units.
    3. It writes those grams back as serves a week per food group (Base column R) and unit shares (column V), with Settings left at the preset (`meategg` 0.12).
  * Adding `meategg` to the `eval` call gave the same results.
  * The route is not neutral. The default diet goes from 53.64 to 53.50 (0.26%), and the gap grows as meat falls: at 0% meat it is 103.6 directly against 88.0 by grams; at 2.5% it is 100.4 against 96.7.
  * So the 2.08 factor and the "5% feeds more than none (100 against 88)" reading in `comparators_2025/README.md` depend on the route. Directly, 0% (103.6) is slightly above 5% (103.3).
* **Diet C (nutrition-optimised, ten micronutrients, protein floor 55 g, free choice).** C is defined by nutrient constraints, not by shares, so I ran the nutrition model myself: `optimise.py`, chained as `run_variants.sh` does (fixcap3, then famcap3, then free, with `micro`).
  * It produced A 85.10, B 188.95 and **C 342.50 million**. This is exactly `nutrition_lp_2025/variants.csv`.
  * Re-evaluating the C grams through the server gives 342.50 again.
  * Other settings: C without the start chain gives 342.50; C with no micronutrients gives 410.21; C with the 95 g protein floor gives 317.04.
  * **None gives 248.7**, so the stated 248.7 does not hold against the current nutrition model.
  * What C changes: the serves of the 17 food groups and the shares of the units within them. No Settings input changes (`meategg` stays 0.12; legumes and sweeteners stay at the default because their shares do not sum to one). The optimised C is mainly brown rice 344 g, skim milk 249 g and tofu, with B12 exactly at the intake.

## C. The files under test

* **`design_choices.csv`**: every capacity and factor matches my own values except the two diet rows.
  * The Diet row (48.2, 100.3, 2.08) matches only the grams route (A6).
  * The Diet (optimised) row is 53.5 to 248.7, 4.65. My value is 342.5 for C, a factor of 6.40 on 53.5.
  * The brief's "53.6" for the default is not what the CSV holds (53.5).
* **Root cause of 248.7.** `diet_land.py` does not take the optimised diets from the repository. It reads `1_short_micro_{fixcap3,famcap3,free}.json` from `VARDIR`, which defaults to a scratch folder outside the repository: `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/var55`. That folder is dated 2026-10-31 07:10. I listed it only and did not read its contents, because the rules keep reading inside the repository.
  * The date is before the 2026-11-03 dairy-module rerun that produced `variants.csv`.
  * So the A, B and C rows of `diet_land.csv` (84.1, 133.1, 248.7) are diets optimised on the withdrawn basis, evaluated on the current release. They are not the current nutrition model's 85.1, 189.0 and 342.5.
  * The script's docstring says the diets come from the "`variants.csv` run", which they do not.
  * `comparators_2025/README.md` line 71 says the table "has been rerun on the current improved release (2026-11-06)". That is true of the evaluation but not of the optimisation.
  * The run cannot be reproduced from the repository: without that folder the optimised rows simply drop out of the CSV.
* **`design_choices.py`** takes the factors from `rerun.csv`, `results/`, `scale_curve.csv`, `diet_land.csv`, `energy_exports.csv` and `monte_carlo_2025-fixed_all_summary.csv`. Its p5 and p95 equal those of `ranges_2025-fixed.csv`, and every rerun.csv value matches my evaluator runs.
* **README "What moves the number" section** (`analysis/method_tests_2025/README.md` lines 262 to 312):
  * **Table**: every number matches the CSV, rounded. The factors shown to one decimal are within one unit of the last printed digit of mine: 2.2, 2.7, 2.7, 2.1, 2.4, 6.2. Exceptions:
    * Diet, optimised: 53.5, 248.7 and 4.7 do not hold. On the current nutrition model it would be 342.5 and 6.4.
    * Diet 2.1 holds either way (2.08 or 2.14).
  * **"The model's own uncertainty is small beside the definitions: 1.26 against 2.2 (weather), 2.7 (time frame), 2.7 (unit) ... and exports 2.4 to 6.2"**: holds (2.19, 2.66, 2.67, 2.41, 6.22). The same sentence's "diet 2.1 to 4.7" does not hold at the upper end (6.4 on the current C).
  * **"Waste and land matter least (1.2 to 1.3 and 1.09)"**: the numbers hold (1.17, 1.33, 1.09). The ranking claim does not quite hold: the Australian-settings row (1.29) is smaller than corrected waste (1.33). Waste is not strictly among the least; land (1.09) is the least of the design choices.
  * **Ladder and drivers**: hold. Ladder values: 15.6, 18.9, 30.8, 41.5, 53.6, 55.3, 62.9, 100, 258. Spread: 9.4 to 15.6 is 1.66, 15.6 to 62.9 is 4.03, 62.9 to 100 is 1.59, and 100/9.4 is 10.64. Drivers: short-term meat 0.806 and red meat 0.163; long-term resilience table 0.521 and meat 0.363. I did not check the 9.4 thesis figure (outside the brief).
  * **"Limits" paragraph**: it says the diet rows use "the nutrition model's ten-micronutrient diets". As above, they are the stale pre-dairy-module diets.

## Found outside the brief

* The README file's heading says "Paper B, section 5", while the script's docstring and this brief say section 6.
* The CSV's "Exports counted (energy)" row says "(wheat and rice; all foods)" but uses only the all-foods count (258.1).
* The grams round trip of the nutrition server undervalues low-meat guideline diets by up to 15% against direct evaluation (0% meat: 88.0 against 103.6). This affects the Peters comparison table and its non-monotone-in-meat reading in `comparators_2025/README.md` section 2b.

## Commands to rerun (repository root)

```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v17
node $S/partA.mjs                         # part A and direct guideline diets; INJECT_WRONG=1 for the wrong-value test
node $S/res10.mjs                         # drought sweep
python3 -I $S/family_rt.py                # guideline diets by the server grams route
O=analysis/nutrition_lp_2025/optimise.py; mkdir -p $S/lp
python3 -I $O 2025-improved 1 short $S/lp/1_short_micro_fixcap3.json 1 micro fixgroups cap3
python3 -I $O 2025-improved 1 short $S/lp/1_short_micro_famcap3.json 1 micro cap3 start=$S/lp/1_short_micro_fixcap3.json
python3 -I $O 2025-improved 1 short $S/lp/1_short_micro_free.json 1 micro start=$S/lp/1_short_micro_famcap3.json
python3 -I $S/opt_rt.py $S                # re-evaluate the optimised diets through the server
```

## Files read

* **Inputs**: `qa/briefs/_checker_rules_results_wave.md`, `qa/briefs/V17_design_choices.md`, `web/src/model/evaluator.js`, `analysis/sensitivity_2025/evaluate.mjs`, `web/public/data/2025-{fixed,improved}/` (`model.json`, `regions.json`), `results/2025-fixed.csv` (head), `results/scale_curve.csv`, `results/ranges_2025-fixed.csv`, `analysis/comparators_2025/energy_exports.csv`, `analysis/comparators_2025/README.md` (grep for the diet definitions; its section 2b table repeats the figures under test, which I saw before part C), `analysis/comparators_2025/COMPARATORS.md` (grep), `analysis/comparators_2025/rerun.csv` (R1 to R3 rows), `analysis/nutrition_lp_2025/` (`README.md`, `server.mjs`, `run_variants.sh`, `optimise.py` lines 1 to 60, `variants.csv`, a grep of `variants_family95.csv` and `staples*.csv`), `analysis/sensitivity_2025/monte_carlo_2025-fixed_all_summary.csv` (zone 1).
* **Under test (part C)**: `analysis/method_tests_2025/design_choices.py`, `design_choices.csv`, `analysis/comparators_2025/diet_land.py`, `diet_land.csv`, and `analysis/method_tests_2025/README.md` lines 262 to 312.
