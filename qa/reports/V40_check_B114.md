# V40: blind check of B114 (the pasture-crop pairing relaxed)

Checker report. Release `2025-fixed`, Australia (region 1), presets short and long. Brief: `qa/briefs/V40_check_B114.md`; rules `qa/briefs/_checker_rules_results_wave.md`; builder brief `qa/briefs/B114_pairing_relaxed.md`.

## 1. Tolerance (set before comparing)

* Counts, names, which land binds, and the 0.5% diets chosen: must match exactly.
* Capacities, land areas and per-person energy and protein: within 0.5%.
* Shares, ratios and percentages: within one unit of the last printed digit.
* A sentence for the paper passes only if every figure in it is within tolerance and it claims no more than the figures show.

## 2. Wrong-value example (marked as an example)

EXAMPLE: my variant 1 script run with `wrong` multiplies its solved population by 1.01. It then gives 82.537 million short (against the builder's 81.70: +1.0%, outside 0.5%, FAIL), and its own land check fails: cropland used 319,664 km2 against 316,499 existing, pasture 3,351,876 against 3,318,689. So both the comparison and the constraint check can fail.

## 3. My route and figures (derived before opening any builder file)

Read: R03b issue 8, `web/src/model/evaluator.js`, the Settings formulas of `web/public/data/2025-fixed/model.json` (rows 33 to 75), Base rows 170 to 200. Scripts (scratch, outside the repository): `check.mjs` (base, variant 2, side checks) and `v1b.mjs` (variant 1), run with node from the repository root.

**How the model pairs the lands.** Capacity is Settings!C62 = C61/C53. Cropland and pasture (C56 = 316,499 km2, D56 = 3,318,689 km2) are one pool shared in proportion to the per-person need (C59, D59); cropland is capped at what exists (C60 = min(C59, C57)); pasture takes the rest. When cropland is not the cap, capacity = (C + P)/(c + d). Forestry, infrastructure and reserve shares do not enter capacity (B62 = C62) and leave C56 and D56 unchanged while H56 > 0 (it is positive in every run below).

**Base.** Reproduced from the evaluator: 41,503,537 short and 15,623,209 long. Pasture binds in both; idle cropland ceded to pasture 175,527 km2 short, 101,777 long.

**Variant 1** (pasture full of pasture-fed meat and dairy, Base rows 90 to 143 and 175 to 177; the shortfall replaced energy for energy by the diet's cropland food groups in their present proportions; groups with no cropland, the recycled feed of the long term, held fixed). Solved in closed form so that both lands are exactly full.

| | Short | Long |
|---|---|---|
| Capacity | 81.720 M (+96.9%) | 21.872 M (+40.0%) |
| Share of pasture-fed energy kept on pasture | 45.3% | 45.6% |
| Cropland growing the replacement | 38,926 km2 | 15,895 km2 |
| Cropland food, kJ a year per m2; pasture-fed food, kJ per m2; ratio k | 650; 7.11; 91.5 | 487; 5.27; 92.5 |
| Cropland used / existing | 316,499 / 316,499 | 316,499 / 316,499 |
| Pasture used / existing | 3,318,689 / 3,318,689 | 3,318,689 / 3,318,689 |
| Energy a day (unchanged by construction) | 7,388 kJ | 11,329 kJ |
| Protein a day, base to variant | 93.2 to 80.9 g | 129.7 to 114.9 g |
| Plant foods only as the replacement (1p) | 86.976 M (k 190.0, protein 77.4 g) | 21.872 M (no crop-fed animal food has land) |

Protein stays above the NHMRC average of 55 g used in `analysis/nutrition_lp_2025` and at about 18% of energy. Forestry and infrastructure, under the model's own proportional allocation at the variant 1 footprint, would carry 121.6 M short and 28.6 M long, above the solution, so they do not bind.

**Variant 2** (Settings!B10, the meat-and-egg share, run through the evaluator at every 0.5% step from 0 to the preset's own; the population split between the two neighbouring diets where the binding land changes, solving the two land equations).

| | Short | Long |
|---|---|---|
| Neighbouring diets | 3.5% (cropland binds, 109.831 M alone) and 4.0% (pasture binds, 100.558 M alone) | 3.5% (cropland, 21.749 M) and 4.0% (pasture, 21.883 M) |
| Share of people on the 3.5% diet | 42.7% | 1.3% |
| Capacity | 107.688 M (+159.5%) | 21.899 M (+40.2%) |
| Effective meat-and-egg share | 3.79% (preset 12.0%) | 3.99% (preset 7.5%) |
| Cropland and pasture used | both exactly full | both exactly full |
| Energy a day (base) | 7,433 kJ (7,388), +0.6% | 11,489 kJ (11,329), +1.4% |
| Protein a day (base) | 89.3 g (93.2), -4.2% | 132.4 g (129.7), +2.1% |
| Best single diet on the grid | 2.5% at 118.037 M, cropland binds | 4.0% at 21.883 M |

Forestry and infrastructure at the two diets carry 148 to 173 M short and 28.6 to 30.1 M long: not binding.

Not derived by me: variant 3 (free allocation by linear program) and 3u; my brief did not ask for them.

## 4. Comparison with the builder (opened after section 3)

Builder files: `qa/reports/B114_pairing_relaxed.md`, `analysis/pasture_2025/pairing_relaxed.csv`, `pairing_relaxed_inputs_2025-fixed.csv`, `pairing_relaxed_meatscan_2025-fixed.csv`, `pairing_relaxed_inputs.mjs` (read in part), the README section appended to `analysis/pasture_2025/README.md`.

| Item | Builder | Mine | Verdict |
|---|---|---|---|
| Base short / long | 41.503537 / 15.623209 M | 41,503,537 / 15,623,209 | pass |
| Base binding land; idle cropland ceded | pasture; 175,527 / 101,777 km2 | same | pass |
| Base energy, protein short | 7,376 kJ, 93.1 g | 7,388 kJ, 93.2 g | pass (0.16%; basis, see section 6) |
| Base energy, protein long | 11,305 kJ, 129.5 g | 11,329 kJ, 129.7 g | pass (0.21%) |
| V1 short capacity; change | 81.70; +96.9% | 81.720; +96.9% | pass |
| V1 long capacity; change | 21.87; +40.0% | 21.872; +40.0% | pass |
| V1 share kept on pasture short / long | 45% / 46% | 45.3% / 45.6% | pass |
| V1 cropland for replacement short / long | 38,987 / 15,931 km2 | 38,926 / 15,895 | pass (0.16%, 0.23%) |
| V1 kJ per m2 cropland short / long | 649 / 486 | 650 / 487 | pass (one unit) |
| V1 kJ per m2 pasture short / long | 7.11 / 5.27 | 7.11 / 5.27 | pass |
| V1 k short / long | 91.3 / 92.2 | 91.5 / 92.5 | fail on the one-unit rule (0.2%, 0.3%); energy basis only, no capacity moves |
| V1 protein short / long | 80.9 / 114.8 g | 80.9 / 114.9 g | pass |
| V1p short; k; protein | 86.96; 189.6; 77.3 g | 86.976; 190.0; 77.4 g | pass; k fails one-unit rule as above |
| V1p cropland for replacement; share kept | 21,115 km2; 42% | 21,073; 42.2% | pass |
| V1p long equal to V1 long | 21.87 | 21.872 | pass |
| V2 short capacity; change | 107.69; +159.5% | 107.688; +159.5% | pass |
| V2 long capacity; change | 21.90; +40.2% | 21.899; +40.2% | pass |
| V2 diets, binding land of each | 3.5% cropland, 4.0% pasture (both presets) | same | pass |
| V2 split short / long | 42.7:57.3 / 1.3:98.7 | 42.7 / 1.3 | pass |
| V2 diet capacities alone short | 109.83, 100.56 | 109.831, 100.558 | pass |
| V2 diet capacities alone long | 21.75, 21.88 | 21.749, 21.883 | pass |
| V2 effective share | 3.79% / 3.99% | 3.79% / 3.99% | pass |
| V2 energy, protein short | 7,412 kJ, 89.2 g | 7,433 kJ, 89.3 g | pass (0.3%, 0.1%) |
| V2 energy, protein long | 11,456 kJ, 132.2 g | 11,489 kJ, 132.4 g | pass |
| Best single diet short / long | 2.5% at 118.04 / 4.0% at 21.88 | 118.037 / 21.883 | pass |
| Meat scan, every grid row short (25) and long (16) | csv | my grid | pass (capacities and binding land agree on the rows checked: 0, 0.5, 1.0, 1.5% and the bracket) |
| Gap closed, V1: build 1 64.8 / HALF 76.0 / build 3 84.6 | 173% / 117% / 93% (2.9 M short) | 173% / 117% / 93% (2.9 M) | pass |
| Gap closed, V1p | 195 / 132 / 105% | 195 / 132 / 106% | pass (one unit) |
| Gap closed, V2 | 284 / 192 / 154% | 284 / 192 / 154% | pass |
| V3, V3u capacities and gap shares | 172.31, 249.60; 28.36 | not derived | cannot determine |
| Builder's wrong-value example | planted 41.6 fails | not rerun | noted |
| Report location | says it is in `analysis/pasture_2025/B114_pairing_relaxed_report.md` | that file does not exist; the report is at `qa/reports/B114_pairing_relaxed.md`; the README section points to the missing file | fail (pointer only, no number) |

## 5. The proposed sentences and claim rows

**Section 5.11 replacement.** Figures pass (81.7, 87.0, 107.7, 3.8% against 12%; 172.3 not checked; "93% of the gap to 84.6"). Wording does not hold in two places:
* "What remains above the model is the pairing of pasture-fed food with crops" states the cause as fact; the paragraph's own last sentence says other causes are not excluded. Keep "consistent with" or "accounted for by".
* "Relaxed in the model, the residual closes" is true of variants 1p, 2 and 3 but not of variant 1 against footprint build 3 (93%). Only variant 1 (and 1p) relaxes the pairing alone; variants 2 and 3 change the diet, so they test the fixed diet as much as the pairing. Suggested: "With only the pairing relaxed (variant 1), the model reads 81.7 million, above HALF's 76.0 and the footprint's 64.8 and 93% of the way to the footprint's 84.6, at the diet's energy and with protein falling from 93 to 81 g a day."
Verdict: figures pass; wording says more than the figures support.

**Section 7.6 replacement.** "Two features account for the distance, each tested on its own" fails. The distance in 7.6 is three to eight times the model (B247, 134 to 343 million). The builder's own section 4 says the pairing test does not reach the unadjusted readings, and R03b issue 3 shows the productivity basis does not apply to the energy balance or people per hectare (134 to 211 million as run). No run combines the two features, so the pair is not shown to account for the whole distance. Also "82 to 108 million on the same diet energy": variant 2's energy is 0.5% (builder basis) to 0.6% (Settings basis) above the base, which is close enough to "about the same", not "the same". Verdict: does not hold as written.

**Section 8.4 addition.** 107.7 against 41.5 passes. "The meat-and-egg share that the existing pasture can carry, 3.8%" is a population mix of the 3.5% and 4.0% diets, not a diet of the family; say so. Verdict: holds with that qualifier.

**Table 5, column (f).** 81.7 and 107.7 pass; 172.3 cannot determine.

**Response letter.** Figures and the comparison (81.7 between 64.8 and 84.6, above 76.0; the other two pass all three) pass.

**Claim rows the builder says move.**
* B247 (Tier B): the value "3 to 8" unchanged, agreed. The reworded cause clause: not agreed as proposed (see 7.6 above). The proposed note figures "81.7 to 107.7 million" pass.
* New rows proposed (81.70, 107.69, 172.31; closure shares 117% and 93%): 81.70, 107.69, 117%, 93% pass; 172.31 cannot determine.
* Tier A: builder lists none moving; B090 (41.5) reproduced, B270 and B272 values are as the builder quotes them from the register. Agreed.

## 6. Method points I would do differently, and whether a number moves

* **Energy basis.** The builder takes energy and protein from the evaluator's diet rows (Base `dietRows`); I took Settings!T and O (the workbook's own group totals, Base rows 6 to 89 for cereals). They differ by 11.7 kJ a day in cereals (0.16% of the diet). This moves k by 0.2 to 0.3 and the V1 cropland area by 0.2%; capacities move by 0.02% at most. No headline number changes.
* **Replacement basket.** My first route counted the long term's zero-land groups (recycled-feed white meat and pork) in the basket, which gave 21.93 M long; that lets free food scale with no land, which is wrong. The builder's choice (hold them fixed) is the right one and I adopted it; it gives 21.872 M, matching.
* **Variant 2 is not the best the family can do.** Capacity along the meat grid is not monotonic: the 2.5% diet alone gives 118.0 M short, above the 107.7 M split. The builder reports this; the paper sentence for 8.4 should not imply the split is the family's ceiling.
* **Long-term variant 2 energy rises 1.4%** (11,489 against 11,329 kJ on my basis). The builder prints only the short-term "within 0.5%"; correct as limited to the short term.
* None of these changes a printed capacity.

## 7. Register rows touched

None. I edited no file other than this report.

## 8. Rerun

From the repository root: `node <scratch>/v40/check.mjs` and `node <scratch>/v40/v1b.mjs` (add `wrong` to either for the planted example). The scripts live in the session scratch folder, not in the repository.
