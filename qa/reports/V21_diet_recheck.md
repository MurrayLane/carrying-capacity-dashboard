# V21 report: diet route fix and re-optimised diets (decisions 30 and 31)

**Verdict: every numbered target holds.** I found no case where the files under test disagree with my own figures beyond the tolerance. There are four small findings at the end. None of them changes a figure.

## Tolerance and the test that it can fail
- Counts and names must match exactly. Capacities must agree within 0.5%. For part B the server route must agree with the direct route within 0.001 million, as the brief states. Shares and ratios must agree within one unit of the last printed digit.
- Deliberate wrong value: I gave my server-against-direct comparison a direct value of 100.392 for the 2.5% share; the true value is 100.3909. It reported `0.025 100.3909 100.392 MISMATCH 0.001051`, so the check can fail. With the true values the largest difference was 0.000049 million, which is my own 4-decimal rounding of the direct route.

## A. Direct route: holds
`2025-improved`, zone 1 (Australia), short preset, only `meategg` changed:

| meategg | mine (million) | claim |
|---|---|---|
| 0 | 103.6030 | 103.6 |
| 0.025 | 100.3909 | 100.4 |
| 0.05 | 103.2838 | 103.3 |
| 0.075 | 66.9401 | 66.9 |
| 0.10 | 58.8378 | 58.8 |
| 0.12 | 53.6437 | 53.6 |
| 0.15 | 48.3290 | 48.3 |

On the 0.5% grid from 0 to 15%:
- 0% is the highest point (103.603). The nearest is 103.42 at 4.5%.
- Capacity falls to a low of 100.39 at 2.5% and climbs back to 103.4 at 4 to 4.5%, so the dip at 2.5% holds.
- The cliff after 5.5% holds: 103.28 at 5%, 101.14 at 5.5%, then 89.68 at 6%, 80.56 at 6.5%, 73.12 at 7%, 66.94 at 7.5%. From there capacity falls smoothly to 48.33 at 15%.

On `2025-fixed`, zone 1, short preset: 118.0370 at 2.5% against 112.4492 at 0%. The claim of 118.0 against 112.4 holds.

## B. Server route: holds
- **Server against direct.** `familygrams` returns 31 diets, meat share 0 to 0.15 in steps of 0.005. I sent each through `eval` in one server session. All 31 agree with the direct route within 0.00005 million, including the seven shares named in the brief. The claim of agreement to 0.001 million holds.
- **sha256.** The hashes of `1_short_micro_fixcap3.json`, `1_short_micro_famcap3.json` and `1_short_micro_free.json` match those recorded. The folder `diets_2025-improved/` has no README of its own; the hashes are in `analysis/nutrition_lp_2025/README.md` (finding 1).
- **Optimised diets through `eval`.** Each file's `g_vec` is in grams a day, so I multiplied it by 7 to give the grams a week that `eval` takes. A gives 85.46, B 202.06 and C 422.27 million. The claims of 85.5, 202.1 and 422.3 hold.
- **Re-running the optimiser for C.** I ran `optimise.py` three times in a row into my scratch folder, using the arguments `run_variants.sh` passes: fixcap3 (`1 micro fixgroups cap3`), then famcap3 (`1 micro cap3 start=<fixcap3>`), then free (`1 micro start=<famcap3>`). The rerun reproduces C exactly: 422,267,921.46, 0% off. All three output files are byte-identical to the repository files (same sha256). I saw no non-determinism in this run, and each stage took about 10 seconds.
- **C's micronutrients.** C meets all ten micronutrient constraints. I recomputed the totals from `g_vec` and `unit_micronutrients.csv`, and they equal the file's `optimised_totals` exactly:

  | Nutrient | C's total | Floor |
  |---|---|---|
  | calcium | 1427.0 mg | 1000 |
  | iron | 13.0 mg | 13 (binding) |
  | zinc | 11.003 mg | 11 |
  | iodine | 150.5 ug | 150 |
  | B12 | 2.4 ug | 2.4 (binding) |
  | vitamin A | 800.0 ug | 800 (binding) |
  | folate | 536.6 ug | 400 |
  | vitamin C | 108.4 mg | 45 |
  | magnesium | 681.7 mg | 365 |
  | potassium | 3737 mg | 3300 |

- **C's protein.** Protein is 74.82 g against the 55 g floor, so the floor is met. I recomputed it from the server's per-gram coefficients, filled from the AUSNUT columns for units the workbook gives no nutrients, as `optimise.py` does with micronutrients. The energy floor is also met: 8009.5 kJ against 7993.9.
- A and B also meet all ten micronutrient constraints and the protein floor: A has 94.4 g protein, B 83.8 g.

## C. Files under test: all hold
I read `server.mjs`, `diet_land.py`, `diet_land.csv`, the two Diet rows of `design_choices.csv`, `analysis/comparators_2025/README.md` section 2b and `papers/B_methods/SECTION7_DRAFT.md`.

- **Meat-share sentence: holds.** The wording is in README 2b (third bullet) and SECTION7 (LDB bullet, line 38). Every figure in it matches my values: 103.6, the dip at 2.5% (100.4), the cliff after 5.5%, and 118.0 against 112.4 on the corrected release. README 2b's extra figures also match: 103.4 at 4 to 4.5%, 101.1 at 5.5%, 89.7 at 6%, 66.9 at 7.5%. The 2025-fixed values in `analysis/scale_curve_2025/diet_scale.csv` (112.4 and 118.0) equal my direct-route values.
- **Design-choice row "Diet", 48.3 to 103.3 (2.14): holds.** My values are 48.329 to 103.284, a ratio of 2.137.
- **Design-choice row "Diet (optimised)", 53.6 to 422.3 (7.88): holds within tolerance.** The unrounded ratio is 422.268 / 53.644 = 7.872, which prints as 7.87. The 7.88 comes from dividing the rounded figures. `variants.csv` itself records the gain as 7.872 (finding 2).
- **Land columns of the diet table: hold.** I computed them myself as land per gram times grams a day eaten, times 365 / 10,000, split cropland and pasture by unit type:

  | Diet | Total ha a person (mine / table) | Cropland (mine / table) | Pasture (mine / table) |
  |---|---|---|---|
  | A | 3.743 / 3.74 | 0.282 / 0.28 | 3.461 / 3.46 |
  | B | 1.198 / 1.2 | 0.139 / 0.14 | 1.060 / 1.06 |
  | C | 0.186 / 0.19 | 0.057 / 0.06 | 0.129 / 0.13 |

  The guideline-diet and default rows of `diet_land.csv` also match mine.
- **Other differences between the files and my results:** none in figures. People fed in `diet_land.csv` equals my direct route and my server route at every row. README 2b's derived claims also check out:
  - 6.23 / 0.27 = 23 times;
  - B is about twice the meat-free diet (202 against 104), with 0.14 against 0.27 cropland;
  - the macronutrient-only bounds B 301 and C 533 match `variants.csv` (300.55 and 532.86);
  - "1.6 to 7.9 times" matches 1.593 and 7.872.

## Findings the brief did not ask about
1. **Hashes not where the files say.** `diet_land.py` (docstring) says the sha256 is in "that folder's README". `diet_land.py` reads its diets from `diets_2025-improved/`, which has no README; the hashes are one folder up, in `analysis/nutrition_lp_2025/README.md` (lines 120 to 124). The wording should point there.
2. **7.88 against 7.87.** The design-choice ratio 7.88 is the ratio of the rounded capacities. The unrounded ratio is 7.87. This is within one unit of the last digit, but the other ratios in that file may be computed from unrounded values.
3. **`familygrams` always gives the sedentary diets.** It always uses `redmeat` 0.578 and `activity` 1, which is what its comment says ("sedentary diets"). For zone 1 short these equal the preset, so nothing here is affected. The long preset is `redmeat` 0.5, `activity` 3, `meategg` 0.075, so the family under a long-preset server is not the long-preset diet.
4. **The table's land is the diet's land, not land per person fed.** The "land per person" columns count the food as eaten. They are not the model's land used divided by people fed: on that measure C uses 0.675 ha of cropland and pasture per person fed (0.069 cropland), against the table's 0.19. README 2b says the figures are "the land of the diet", so this is stated, but a reader comparing with capacity should know.

The server held no state between commands that showed: 31 evals, then the three diets in one session, all matched.

## Commands to rerun (from /home/user/carrying-capacity-dashboard)
```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v21
node $S/direct.mjs 2025-improved 1 short 0 0.025 0.05 0.075 0.10 0.12 0.15
node $S/direct.mjs 2025-improved 1 short $(seq -f '%.3f' 0 0.005 0.15) > $S/grid.txt
node $S/direct.mjs 2025-fixed 1 short 0 0.025
echo '{"cmd":"familygrams"}' | node analysis/nutrition_lp_2025/server.mjs 2025-improved 1 short > $S/fam.json
python3 -I $S/serverroute.py $S              # server against direct; add 100.392 as a 2nd argument for the deliberate-mismatch test
P=$PWD/analysis/nutrition_lp_2025/diets_2025-improved
sha256sum $P/1_short_micro_{fixcap3,famcap3,free}.json
python3 -I $S/evaldiets.py x $P/1_short_micro_{fixcap3,famcap3,free}.json
python3 -I $S/micro.py $P/1_short_micro_free.json
python3 -I $S/prot.py $P/1_short_micro_{fixcap3,famcap3,free}.json
bash $S/rerun.sh                             # optimiser chain for C into $S/rerun
python3 -I $S/evaldiets.py x $S/rerun/1_short_micro_{fixcap3,famcap3,free}.json; sha256sum $S/rerun/*.json
python3 -I $S/land.py
```

## Files read
- `qa/briefs/_checker_rules_results_wave.md`
- `qa/briefs/V21_diet_recheck.md`
- `web/src/model/evaluator.js` (top)
- `analysis/sensitivity_2025/evaluate.mjs`
- `web/public/data/2025-improved/` and `2025-fixed/` (`model.json`, `regions.json`, loaded)
- `analysis/nutrition_lp_2025/server.mjs`:
  - header lines 1 to 18 only, before part C;
  - command names grepped, before part C;
  - the whole file, in part C.
- `analysis/nutrition_lp_2025/run_variants.sh`
- `analysis/nutrition_lp_2025/optimise.py` (argument, input and output lines, and the coefficient setup, lines 18 to 51, 91 to 93, 130 to 132)
- `analysis/nutrition_lp_2025/README.md` (sha256 table)
- `analysis/nutrition_lp_2025/unit_micronutrients.csv`
- `analysis/nutrition_lp_2025/variants.csv`
- the three diet files
- `analysis/scale_curve_2025/diet_scale.csv`
- Part C: `analysis/comparators_2025/diet_land.py`, `diet_land.csv`, `analysis/comparators_2025/README.md` section 2b, `analysis/method_tests_2025/design_choices.csv` (header and Diet rows), `papers/B_methods/SECTION7_DRAFT.md` (grep for the meat-share lines)
- Not opened: `qa/reports/V17_*`, `V19_*`, `qa/briefs/B39_*`.
