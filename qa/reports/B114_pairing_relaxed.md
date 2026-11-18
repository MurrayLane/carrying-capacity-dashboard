# B114: the pasture-crop pairing tested (decision 107)

Builder report. Release `2025-fixed` (the corrected model), Australia, presets short and long. Answers R03b issue 8 (EE 3.7, Q3; Mod M3, Q3).

**Where this report sits.** The brief names `qa/reports/B114_pairing_relaxed.md`. The job was restricted to `analysis/pasture_2025` and the scratch folder, so the report is in `analysis/pasture_2025/B114_pairing_relaxed_report.md`; it can be moved to `qa/reports/` unchanged.

## 1. How the model pairs the two lands

`web/src/model/evaluator.js` evaluates the workbook and returns `capacity` = Settings!B75 = B62 = C62 = C61 / C53: the cropland the model allocates over the cropland a person needs. The allocation is in Settings!C57:D62 (0-based keys 56 to 61 in `model.json`):

* cropland and pasture are one pool (316,499 + 3,318,689 km2);
* the pool is shared in proportion to what a person needs of each, and the cropland share is capped at the existing cropland (C60 = min(C59, C57));
* whatever the crops do not need goes to pasture (D60 = 1 less the rest), square metre for square metre, at pasture's own output; pasture never grows crops.

So the binding land is decided in C60: in both presets the crops need less than the existing cropland, the idle cropland (175,527 km2 short, 101,777 long) is ceded to pasture, and pasture binds. Capacity is (C + P) / (c + p) = 3,635,188 km2 over 87,587 m2 a person = 41.50 million.

## 2. The three relaxations

The evaluator is not changed. `pairing_relaxed_inputs.mjs` sets inputs and reads cells; `pairing_relaxed.py` solves the closed form of the rule above, which reproduces the evaluator to 1e-6 (41.503537 and 15.623209 million, also equal to `results/2025-fixed.csv`), and relaxes one thing at a time.

1. **Substitution at the crop-equivalent energy rate.** The pasture-fed meat and dairy (beef, lamb, veal, dairy) that the existing pasture cannot carry is replaced, kilojoule for kilojoule, by more of the diet's own cropland foods in their present proportions. A square metre of cropland gives 649 kJ of food a year in those foods and a square metre of pasture 7.1 kJ in pasture-fed meat and dairy, so one square metre of idle cropland stands in for k = 91.3 of pasture. This is arithmetically the same as pooling the two lands at a common energy rate, the structure of R03b's first form with energy in place of world-average hectares. Variant 1p uses the plant foods alone (k = 189.6).
2. **The meat share falls to what the pasture carries.** The model's own diet family (Settings!B10, the meat-and-egg share, on its 0.5% grid) run through the evaluator at every share from 0 to the preset's own. Between 3.5% (cropland binds) and 4.0% (pasture binds) the population is split between those two diets so that both lands are full. Energy is held by the family's own construction; protein falls a little.
3. **Free allocation of land.** A linear program over the amounts of the eleven food groups (red meat split into pasture-fed and crop-fed), with energy and protein at least the diet's, the model's land rule and the non-food needs unchanged, maximising people. Each group is held between 0 and 3 times its present amount (the guard of `analysis/nutrition_lp_2025`, applied here to groups); 3u lifts the cap and is a bound, not a diet. Groups with no land (recycled feed, long term) stay at their present amount.

## 3. Results

`analysis/pasture_2025/pairing_relaxed.csv`, million people:

| Variant | Short | Change | Long | Change | Land that binds | Energy, protein a day (short) |
|---|---|---|---|---|---|---|
| Base | 41.50 | | 15.62 | | pasture, with idle cropland ceded to it | 7,376 kJ, 93.1 g |
| 1. Energy substitution into cropland | **81.70** | +96.9% | 21.87 | +40.0% | cropland and pasture both full (pasture carries 45% of the pasture-fed food; 55% of its energy grown as crops on 38,987 km2 of cropland) | 7,376 kJ, 80.9 g |
| 1p. Plant foods as the replacement | 86.96 | +109.5% | 21.87 | +40.0% | both full | 7,376 kJ, 77.3 g |
| 2. Meat share to the pasture (3.79% against 12.0%; long 3.99% against 7.5%) | **107.69** | +159.5% | 21.90 | +40.2% | both full | 7,412 kJ, 89.2 g |
| 3. Free allocation, groups 0 to 3 times | **172.31** | +315.2% | 28.36 | +81.5% | both full | 12,299 kJ, 93.1 g |
| 3u. Free allocation, no cap | 249.60 | +501.4% | 28.36 | +81.5% | both full | 7,376 kJ, 93.1 g |

## 4. Does the gap close?

The readings are column (e) of Table 5: the footprint at local productivity 64.8 (build 1) and 84.6 (build 3) million (B270) and HALF 76.0 million (B272; other defensible readings 73.7 to 79.3). They are average-year readings on the present diet, so only the short term is compared. Share of the gap from 41.50 closed:

| Variant | Footprint build 1, 64.8 | HALF, 76.0 | Footprint build 3, 84.6 |
|---|---|---|---|
| 1 (81.70) | closes, 173% | closes, 117% | does not close, 93% (2.9 million short) |
| 1p (86.96) | closes, 195% | closes, 132% | closes, 105% |
| 2 (107.69) | closes, 284% | closes, 192% | closes, 154% |
| 3 (172.31) | closes, 561% | closes, 379% | closes, 304% |
| 3u (249.60) | closes, 893% | closes, 603% | closes, 483% |

The mildest relaxation, which keeps the diet's energy and changes only where the pasture-fed share of it comes from, lands inside the footprint span (64.8 to 84.6) and above every HALF reading (73.7 to 79.3). The other two overshoot. So the pairing is sufficient to account for the residual; the test cannot show it is the only cause, and the overshoot says the adjusted readings sit between "pairing kept" and "pairing removed with the diet free".

What the test does not reach: the unadjusted readings (134 to 343 million, B156, B247). Relaxing the pairing on the present diet's energy gives 82 to 108 million; only the free allocation (172 to 250) enters that span, and it does so by changing the diet. The rest of the three-to-eight-fold distance is the productivity basis (Issues 1 and 3), which is a separate test.

## 5. Sentences the paper should carry

Section 5.11, replacing "What remains above the model is consistent with the pairing of pasture-fed food with crops, which neither method carries; the pairing was not removed from the model to test it.":

> What remains above the model is the pairing of pasture-fed food with crops, which neither method carries. Relaxed in the model, the residual closes: with the pasture-fed meat and dairy that the pasture cannot carry replaced, kilojoule for kilojoule, by the diet's cropland foods, the corrected model reads 81.7 million (87.0 with plant foods as the replacement); with the diet's meat-and-egg share lowered within the model's own diet family to what the pasture carries (3.8% against 12%), 107.7 million; and with land allocated freely among food groups at the diet's energy and protein, each group at most three times its present amount, 172.3 million (Table 5, column (f)). Each is above HALF's 76.0 million and the footprint's 64.8 million, and the first reaches 93% of the gap to the footprint's 84.6 million. The pairing is therefore enough to account for the residual, though the test cannot exclude other causes.

Section 7.6, replacing "This is consistent with none of them carrying the pairing of pasture-fed food with crops that binds the model in Australia, an interpretation not tested (section 5.11).":

> Two features account for the distance, each tested on its own: the productivity basis (at Australian productivity the footprint and HALF read 64.8 to 84.6 million) and the absence of the pairing of pasture-fed food with crops that binds the model (relaxed, the model reads 82 to 108 million on the same diet energy; section 5.11).

Section 8.4, added:

> The fixed diet is the decisive assumption. Within the model's own diet family, the meat-and-egg share that the existing pasture can carry, 3.8% against 12%, feeds 107.7 million against 41.5.

Table 5, column (f), the model with the pairing relaxed (corrected, short term): 81.7 (energy substitution), 107.7 (meat share to the pasture), 172.3 (free allocation, cap 3 times).

Response letter: "We have run the model with the pairing relaxed in three ways; the results are in Table 5, column (f). The mildest, which holds the diet's energy, gives 81.7 million, between the footprint's 64.8 and 84.6 and above HALF's 76.0; the other two pass all three."

## 6. Limits

* Variant 1 replaces food, it does not grow beef at cereal yields: protein falls from 93.1 to 80.9 g a day (77.3 in 1p). Variant 2 holds energy within 0.5% and protein falls 4.2%. Variant 3 holds both but is a land-efficiency bound (no pasture-fed red meat; sweeteners, cereals and legumes tripled), not a diet.
* Variant 2's mix is two neighbouring diets of the family, as the family exists only on a 0.5% grid; the best single diet of the family is 2.5% at 118.0 million, with pasture idle.
* Corrected release, Australia only; no states, no improved release, no micronutrients.
* R03b also proposed land pooled at world-average hectares, diet variant A on the corrected release (`analysis/nutrition_lp_2025/optimise.py`) and crop-fed protein within the meat group. The first is variant 1's structure with a different exchange rate; the second needs the nutrition server on `2025-fixed`, outside this job's folder; the third lies between variants 1 and 3. None was run.

## 7. Files changed

All in `analysis/pasture_2025/`:

* `pairing_relaxed_inputs.mjs` (new): reads the evaluator; writes the two input files below.
* `pairing_relaxed_inputs_2025-fixed.csv` (new): per preset and food group, cropland and pasture per person, energy, protein; non-food needs; land; the model's capacity.
* `pairing_relaxed_meatscan_2025-fixed.csv` (new): variant 2, the diet family through the evaluator on the 0.5% grid.
* `pairing_relaxed.py` (new): the closed form, the three variants, the checks; writes the csv below.
* `pairing_relaxed.csv` (new): variant; preset; capacity; change from base; which land binds; energy; protein; gap closed; how.
* `README.md` (one section appended).
* `B114_pairing_relaxed_report.md` (this report).

Not touched: `web/src/model/evaluator.js`, `qa/claims_register.csv`, every release and every existing output. Rerun: `node analysis/pasture_2025/pairing_relaxed_inputs.mjs && python3 analysis/pasture_2025/pairing_relaxed.py` from the repository root; two runs give byte-identical outputs.

## 8. Claim rows that move

Tier A: none. B270, B272 (the readings compared), B090 (41.5), B156 and B276 keep their values and statements.

Tier B:

* B247; B; before: "... give about three to eight times the land-and-diet balance because none carries the pairing of pasture-fed food with crops that binds Australia ...", note "the pairing explanation is the project's interpretation, not tested by removing the pairing from the model"; after: value 3 to 8 unchanged, the cause clause reworded as in section 5 (two features, each tested), note "pairing tested in B114: relaxed, the corrected model reads 81.7 to 107.7 million (172.3 with free allocation), `analysis/pasture_2025/pairing_relaxed.csv`".

New rows the register job should add (section 5.11 and Table 5 column (f), Tier A if printed in the table): 81.70 (variant 1, short), 107.69 (variant 2, short), 172.31 (variant 3, short), each with `pairing_relaxed.csv`, row variant and preset, column `capacity_million`; and the closure shares 117% (HALF) and 93% (footprint build 3) for variant 1, column `gap_to_adjusted_footprint_and_half`.

Register rows touched: none.

## 9. Wrong-value check

The script checks that its closed form gives the evaluator's capacity and the published `results/2025-fixed.csv` value to one part in a million, and recomputes every land and nutrient constraint of each variant from the solution. Example, a deliberate wrong value (`python3 analysis/pasture_2025/pairing_relaxed.py --wrong-value-demo`):

```
EXAMPLE (deliberate wrong value): the base capacity given as 41.6 instead of the closed form
EXAMPLE wrong value check, short: closed form 41.600000 M, evaluator 41.503537 M, results/2025-fixed.csv 41.503537 M: FAIL
```

Wrong-value check: the planted 41.6 fails; the real run prints PASS for both presets (41.503537 and 15.623209).
