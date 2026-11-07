# V16 report: the ladder of definitions and the comparator figures

Checker: independent, blind until part D. Everything below was derived with my own code in the scratch folder (`partA.mjs`, `partB.mjs`, `partC.py`, `partD_energy.py`). No repository file was changed.

## Tolerance and the fail test (written before comparing)

- Capacities: within 0.5% of the stated value, or within 0.05 million (one unit of the last printed digit) for figures printed to one decimal.
- Factors and ratios: within one unit of the last printed digit (1.66 means 1.65 to 1.67).
- Names and counts must match exactly.
- Fail test, part A: I fed my comparison a wrong claim of 19.5 for the worst-of-100 figure. It reported `MISMATCH` (mine 18.918). Fail test, part C: I fed a claim of 300.0 for the export energy count. It reported `MISMATCH`.

## A. Definition-only figures (Australia, evaluator, `regions[1]`)

The waste setting is the input `losses` (0.12 in the short preset). "Worst of N years" is the input `resilience` = N.

| Target | Release, preset, change | Mine (million) | Stated | Verdict |
|---|---|---|---|---|
| Worst of 100 years, corrected | 2025-fixed short, resilience 100 | 18.918 | 18.9 | holds |
| No avoidable waste, corrected | 2025-fixed short, losses 0 | 55.285 | 55.3 | holds |
| No avoidable waste, improved | 2025-improved short, losses 0 | 62.919 | 62.9 | holds |
| Worst of 10, corrected | 2025-fixed short, resilience 10 | 30.811 | 30.8 | holds |
| Thesis long term as built, 2011 data | 2011-thesis long | 9.431 | 9.4 | holds |
| Corrected long term | 2025-fixed long | 15.623 | 15.6 | holds |
| Improved short | 2025-improved short | 53.644 | 53.6 | holds |

Also: 2025-fixed short base 41.504 (the ladder's 41.5); all agree with `results/<release>.csv`.

## B. The ladder

- Steps 9.4, 15.6, 18.9, 30.8, 41.5, 53.6, 55.3, 62.9: **hold** (part A). 100.0 is the published CSIRO and UQ count, not a model run. I confirmed 258.1 in part C, but only under one choice of energy densities.
- 9.4 to 15.6 = 1.66: **holds**. Unrounded values give 1.656; the rounded steps give 1.660.
- 15.6 to 62.9 = 4.03: **holds**. Unrounded 4.027, rounded 4.032.
- 62.9 to 100 = 1.59: **holds** (1.589).
- Product 10.6: **holds**. It is 10.603 unrounded, or 10.64 from the rounded factors. By construction it equals 100 / 9.431.
- "The published span 9 to 100 is a factor of 10.6": **holds only as 100 / 9.4**. Taken literally, 100 / 9 = 11.1.
- **Does the order change the factors?**
  - The product of the three end-to-end factors cannot change, because they chain the same endpoints.
  - Individual step factors do depend on the order wherever settings interact:
    - The release step (corrected to improved) is x1.293 at 12% waste but x1.138 with no waste.
    - The waste step is x1.332 on corrected but x1.173 on improved.
    - The weather allowance and waste happen to commute (x1.332 and x0.456 in either order, both together 25.20).
  - The long-to-short settings interact strongly. For example, fuel alone moves the long term by x0.237, while biofuel moves the short term by x0.234. So any split of the 4.03 into named definitions depends on the order chosen.
  - The listed ladder is a sorted list of separate runs, not one path. It mixes the corrected and improved tiers.

## C. The energy count of exports

Basis: the long-format extract `fbs_au_world_2021_23.csv`, Australia, mean 2021-23. I used leaf items only (aggregates removed, duplicate group=item rows for Eggs and Milk counted once). Population is 26.20 million, at 2,100 kcal a day.

**People fed by exports alone depend almost entirely on the kcal/kg used.**

| kcal/kg basis | Exports alone | Exports + population | Exports + domestic food energy / 2,100 |
|---|---|---|---|
| FBS-derived: Australian food kcal over food quantity, world fallback | 194.3 M | 220.5 M | 238.3 M |
| FBS-derived, world first | 212.5 M | 238.7 M | 256.5 M |
| Raw-commodity densities (my assumed table: wheat 3340, barley 3540, canola 4940, sugar 3730, others similar), FBS for the rest | 262.0 M | 288.2 M | |

Against 258.1: **cannot determine as a single number**.
- The figure is reproducible only with commodity-as-traded energy densities (my raw basis gives 262.0, 1.5% away, outside tolerance because the densities are a choice).
- The FBS's own food energy per kg gives 194 to 213 M.
- So "258 million" is one end of a range of roughly 195 to 262 M, set by the density table.
- It is an exports-alone count (it does not add the domestic population).

**Dominant items:**
- Wheat is 44 to 50% of export energy (86 to 124 M).
- Barley is 16 to 17% (33 to 44 M).
- Canola seed is 7 to 12%.
- Raw sugar is 5 to 8%.
- Pulses about 5%, sorghum about 4%.
- Meat, dairy, oils, fruit and vegetables together are under 10%.

**What "61 to 100" can rest on: a proportional count, production over domestic use times population.** I computed it in energy from the balance (domestic supply = production + imports - exports - stock variation, which closes the wheat balance exactly).
- Production / domestic supply = 2.53. Times 26.2 M = 66.2 M; times 27.6 M (2025) = 69.7 M. The world-first basis gives 66.8 M.
- Excluding feed from domestic use: ratio 3.72, giving 97.4 M (world basis 98.9 M). This is close to the CSIRO and UQ "around 100".
- Mass basis instead of energy: ratio 1.67, giving 43.7 M.

So the span 61 to 100 is reproducible as a proportional count. Its low end is near the energy ratio with feed included (66, against Bellotti's 61 for 2017). Its high end is near the ratio with feed excluded (97 to 99). B004 itself is a typed span with no output file (the register says so). Its "60" is not a single published figure.

## D. Files under test: differences

**`rerun.mjs` / `rerun.csv`**
- I reran it into the scratch folder: byte-identical to `rerun.csv`.
- Every 2025-fixed and 2025-improved value I derived matches. For example, R1: 41.50 / 37.03 / 30.81 / 26.32 / 22.92 / 18.92; R3: 55.29 and 62.92; improved R1 at 10: 39.93; at 100: 24.68.
- No differences.

**`ladder.csv` (written by `analysis/method_tests_2025/design_choices.py`)**
- All ten values match my derivations or the stated sources.
- 9.4 and 100.0 are typed literals in the script, not read from `results/2011-thesis.csv` (9.431) or from a file. The values are correct but not traced.
- The script's docstring does not list `results/2011-thesis.csv`.

**`energy_exports.py` / `energy_exports.csv`**
- I reimplemented its density table on the repository's long-format extract. It reproduces all four rows exactly: 127.6, 182.7, 240.6, 258.1.
- Differences and issues:
  1. **The script cannot run on any file in the repository.** It expects a FAOSTAT wide-format bulk file (columns `Y2021`..`Y2023`, latin-1). Run on `analysis/method_tests_2025/fbs_au_world_2021_23.csv` it fails with `KeyError: 'Y2021'`. The input it was run on is not in the repository, so 258.1 is not reproducible from repository inputs by its own script.
  2. **The densities are typed "standard values" for the commodity as traded** (wheat 3400, barley 3300, canola 4900, sugar 3900 and so on), not FAO's own. With the FBS's own food kcal/kg the same exports give 194 to 213 M, not 258. The README presents 258 as "the" energy count without saying how much rests on the density choice.
  3. **"All foods" is not all exports.** The table omits these exported items:
     - cottonseed (534 kt)
     - other sweeteners (408 kt)
     - tree nuts (219 kt)
     - wine (634 kt)
     - edible offals (202 kt)
     - fish (82 kt)
     - some fruit and vegetable leaves outside the group rows

     Together they add roughly 8 M at its densities.
  4. The year length is 365.25 days (I used 365). The effect is under 0.1%.
  5. It counts the canola seed and the vegetable-oil group side by side. These are separate exports in the FBS, so this is not a double count. Noted only.

**`analysis/method_tests_2025/README.md`, "What moves the number" and the ladder (lines 262-309)**
- Holds:
  - The ladder table matches the csv (100 and 258 printed rounded).
  - Design-choice rows used here (18.9 / 41.5 / 2.2; 41.5 / 55.3 / 1.33; improved 53.6 to 62.9, 1.17; 41.5 / 45.1 / 1.09; 41.5 / 53.6 / 1.29; 15.6 / 41.5 / 2.7; 100 / 41.5 = 2.4; 258 / 41.5 = 6.2) agree with my runs.
  - Factors 1.7, 4.0, 1.6, product 10.6: hold.
  - "Factor of 4 from 15.6 to 62.9" (4.03) and "3.3 from 18.9" (62.9 / 18.9 = 3.33): hold.
  - Line 259 (15.6 or 18.9 to 55.3; 62.9 improved): holds.
- Differences:
  - "9 to 100 million, a factor of 10.6" is 100 / 9.4; 100 / 9 is 11.1.
  - "exports 2.4 to 6.2": the 6.2 inherits the density dependence of 258. On FBS energy densities it would be 4.7 to 5.1.
  - The README's own caveat (order is a choice, tiers mixed) is correct, and part B confirms it with the release-by-waste interaction.

**`analysis/comparators_2025/README.md`, model table and exports passage (lines 36-47, 91)**
- Holds:
  - Every number in the model table: 49.4; 41.5; 53.6; 30.8; 39.9; 37.0; 26.3; 22.9; 18.9; 47.9; 34.3; 29.9; 24.7; 45.1; 58.3; 55.3; 62.9; long term 14.1 (2025-mirror 14.147), 15.6 and 18.5 (18.496).
  - 27 x 70/30 = 63; 90; 24.4 x 1.5 = 36.6.
  - "128 million from wheat and rice" (127.6) and "258 million for all foods" match the csv.
- Difference: "An energy count of exports ... gives ... 258 million for all foods" should carry the caveat that this is on typed as-traded densities and a partial item list. The FBS's own energy gives about 195 to 213, so "128 to 258" (line 91) is one density basis among several.

## Found outside the brief
- `qa/claims_register.csv` B165 is marked `self-checked`, but its script cannot be run on any repository input (`KeyError: 'Y2021'`). That status overstates its reproducibility.
- B004 "61 to 100" has no output file. The proportional count from the balance (66 to 70 with feed, 97 to 99 without) would give it one.

## Commands to rerun (repository root)
```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v16
node $S/partA.mjs; node $S/partA.mjs wrong
node $S/partB.mjs
python3 -I $S/partC.py; python3 -I $S/partC.py wrong
python3 -I $S/partD_energy.py
node analysis/comparators_2025/rerun.mjs $S/rerun_rerun.csv && diff $S/rerun_rerun.csv analysis/comparators_2025/rerun.csv
python3 -I analysis/comparators_2025/energy_exports.py analysis/method_tests_2025/fbs_au_world_2021_23.csv $S/ee_try.csv   # fails: KeyError 'Y2021'
```

## Files read
- qa/briefs/_checker_rules_results_wave.md, qa/briefs/V16_ladder_and_comparators.md
- web/src/model/evaluator.js (head), analysis/sensitivity_2025/evaluate.mjs
- web/public/data/{2025-fixed,2025-improved,2011-thesis}/{model,regions}.json (via code)
- results/2025-fixed.csv, 2025-improved.csv, 2011-thesis.csv, 2025-mirror.csv (Australia rows)
- analysis/method_tests_2025/fbs_au_world_2021_23.csv, fao_au_production_1997_2023.csv
- Part D: analysis/comparators_2025/rerun.mjs, rerun.csv, energy_exports.py, energy_exports.csv, README.md (lines 10-47, 75-97); analysis/method_tests_2025/ladder.csv, design_choices.py, make_readme_tables.py (ladder table), README.md (lines 12-27, 245-309); qa/claims_register.csv (rows B004, B165, B186, B195, by grep)
