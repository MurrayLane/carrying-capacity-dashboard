# B116: the bases table; fidelity restated; the intake variant (decisions 109, 110)

Brief: `qa/briefs/B116_bases_and_fidelity.md`. Read: R03b issues 9 and 10, the method-tests README (fidelity checks), `gap_attribution.py` and csv, `second_build_values.csv`, `published_values.csv`. No git, no subagents, no network. The claims register and every existing csv are unchanged; no frozen release is touched.

## What was done

One new script, `analysis/method_tests_2025/bases_fidelity.py` (deterministic; `--check [DIR]` recomputes and compares every cell), writes four new files beside the existing ones: `bases.csv`, `fidelity.csv`, `intake_variant.csv`, `gap_attribution_readable.csv`. `simpson_food.py` and `half_index.py` are run in memory up to their csv-writing line (as `harmonised_comparison.py` does), so their csvs are not rewritten. `make_readme_tables.py` gained three tables (bases, fidelity, intake_variant), the new Table S1 rule for the gap-attribution table, and a `--only` flag so a builder replaces only its own blocks (B113 was editing the same README; I re-read it from disk and replaced only my blocks). Determinism: two consecutive runs give identical csvs (same md5 over every csv in the folder).

## 1. The bases table (`bases.csv`; README "Bases of each method")

Sixteen rows: each method as run and harmonised. In short:
* **Population.** No method reading uses the model's 27.6 million. Harmonised per-person bases are FAO's head count, 26.20 million (2021-23; Foran and Poldy's script 26.08, the 2021-22 mean). Henry and Godden and Cassidy as run use no head count at all (output over a per-person requirement). The model's population enters only the model rows and Fearnside's failure probability at the population. Paper B 5.1's "one population" sentence is wrong (for B118).
* **Energy.** Henry and Godden 15.6 MJ implied by the factor 82/466 (Gifford through Table 4); Cassidy 2,700 kcal (11.3 MJ, p. 5); harmonised FAO supply 3,525 kcal (14.8 MJ) and 120.7 g protein; the model 8.0 MJ as eaten (nutrition README). Henry and Godden's protein factor implies 134 g a day.
* **Land.** Methods: FAOSTAT 2021-23, cropland 31.65 and pasture 331.87 Mha (Henry and Godden as run scales to Nix's 70 Mha over 45.7 or 59.95 Mha, with 1990-91 sown pasture carried forward); model: ABS holdings 2020-21, equal to FAOSTAT's 363.52 Mha to 0.01 Mha.
* **Data years.** Methods FAOSTAT 2021-23 (Simpson build 3 as run: the thesis's FAO 1990 yields); Foran and Poldy's requirement is their 2050 Table 2.5; the model's 2025 layer (meat window 2020-21 to 2024-25) taken as the same vintage.
* **Waste.** FAO food supply includes retail and household waste (its losses stop before retail), so on the harmonised basis waste sits inside each method's per-person need; the model charges its own (12% avoidable on US factors corrected; Australian FIAL and bin-audit factors improved). Henry and Godden as run charge none explicitly (their factor is nearly twice a plain requirement).

## 2. Fidelity restated (`fidelity.csv`; README "Fidelity restated")

Verdict on the rebuild on the authors' printed inputs where one exists, else on the rebuild as run: reproduced (within published rounding or 2%), partly (within 10%), not reproduced (beyond 10%).

| Method | Component | Authors' figure | Rebuild as run (gap) | Rebuild on the authors' printed inputs (gap) | Verdict |
|---|---|---|---|---|---|
| Energy and protein balance (Gifford; Henry and Godden) | energy, 1990-91 | 109 | | 108.9 (-0.1%) | **reproduced** |
| Energy and protein balance (Gifford; Henry and Godden) | protein, 1990-91 | 96 | | 95.7 (-0.4%) | **reproduced** |
| Energy and protein balance (Gifford; Henry and Godden) | energy, total row incl. wool and cotton | 206 | | 206.0 (0%) | **reproduced** |
| Energy and protein balance (Gifford; Henry and Godden) | protein, total row incl. wool and cotton | 188 | | 187.9 (-0.1%) | **reproduced** |
| Ecological footprint, food row (Simpson) | pasture (food row), 1991-92 | 1.758 | 1.737 (-1.2%) | 1.718 (-2.3%) | **partly** |
| Ecological footprint, food row (Simpson) | crop land for animal products (feed), 1991-92 | 0.095 | 0.098 (+3.6%) | 0.116 (+21.6%) | **not reproduced** |
| Ecological footprint, food row (Simpson) | crop land for plant foods, 1991-92 | 0.312 | 0.107 (-65.8%) | 0.074 (-76.3%) | **not reproduced** |
| Ecological footprint, food row (Simpson) | crop plus pasture, 1991-92 | 2.165 | 1.942 (-10.3%) | 1.907 (-11.9%) | **not reproduced** |
| Ecological footprint, food row (Simpson) | garden, 1991-92 | 0.032 | | 0.014 (-56.9%) | **not reproduced** |
| Ecological footprint, food row (Simpson) | wool pasture (clothing row), 1991-92 | 0.854 | | 0.127 (-85.1%) | **not reproduced** |
| HALF index (Alexander) | World, 2011 | 35.13 | 34.37 (-2.2%) | 36.10 (+2.8%) | **partly** |
| HALF index (Alexander) | Australia, 2011 | 112.20 | 113.12 (+0.8%) | 121.59 (+8.4%) | **partly** |
| HALF index (Alexander) | United States, 2011 | 97.73 | 94.55 (-3.3%) | 101.04 (+3.4%) | **partly** |
| HALF index (Alexander) | Argentina, 2011 | 114.88 | 109.63 (-4.6%) | 118.36 (+3.0%) | **partly** |
| HALF index (Alexander) | India, 2011 | 15.76 | 14.63 (-7.2%) | 15.11 (-4.1%) | **partly** |
| HALF index (Alexander) | New Zealand, 2011 | 135.76 | 94.80 (-30.2%) | | **not reproduced** |
| People per hectare (Cassidy) | world, people a hectare produced | 10.1 | 12.3 (+22.0%) | 10.7 (+6.2%) | **partly** |
| People per hectare (Cassidy) | world, people a hectare delivered | 6.0 | 7.5 (+24.9%) | 6.4 (+6.5%) | **partly** |
| People per hectare (Cassidy) | United States, people a hectare produced | 16.1 | 21.0 (+30.2%) | 19.3 (+19.7%) | **not reproduced** |
| People per hectare (Cassidy) | India, people a hectare produced | 6.5 | 8.8 (+35.6%) | 7.3 (+13.0%) | **not reproduced** |
| People per hectare (Cassidy) | China, people a hectare produced | 13.5 | 18.4 (+36.5%) | 16.0 (+18.2%) | **not reproduced** |
| People per hectare (Cassidy) | Brazil, people a hectare produced | 10.6 | 14.1 (+33.5%) | 11.2 (+5.9%) | **partly** |
| People per hectare (Cassidy) | United States, feed share of calories | 67 | 41.0 (-38.8%) | | **not reproduced** |
| People per hectare (Cassidy) | United States, delivered share | 34 | 33.0 (-2.9%) | | **partly** |
| People per hectare (Cassidy) | world, delivered share | 59 | 61.0 (+3.4%) | | **partly** |
| Commodity balance (Foran and Poldy) | grain production 1997-98 | 31.578 | 31.950 (+1.2%) | | **reproduced** |
| Commodity balance (Foran and Poldy) | meat production 1997-98 | 3.514 | 3.471 (-1.2%) | | **reproduced** |
| Failure probability (Fearnside) | Trans-Amazon study area (0.24 persons a hectare) | 0.24 | | | **not checked** |
| The model (thesis method as built) | Australia, short term (thesis results, Table 16) | 40,439,187 | 40,439,187 (0%) | | **reproduced** |
| The model (thesis method as built) | Australia, long term (thesis results, Table 16) | 9,431,487 | 9,431,487 (0%) | | **reproduced** |

**HALF Australia, 6 to 8% and its cause.** On the current FAOSTAT revision the rebuild is +0.8% (113.12 against 112.2). With the world pasture the supplement prints (3,364 Mha against 3,182 Mha in the current revision; +5.7% pasture per tonne of ruminant product; animal products are 95% of Australia's 2011 HALF) it is 118.88, **+6.0%**; the feed pool and feed cropland as printed add most of the rest, and all printed inputs together give 121.59, **+8.4%**. The same inputs move the world, United States, Argentina and India toward their published figures and Australia away from its own, so the 0.8% agreement holds on the current revision only. What offsets it in the authors' figure is not identified (untested: the 2015 food balance's Australian diet; the bovine share of pasture, 59% in the paper against 67% here).

**Gap-attribution table regenerated** (README Table S1 block; source `gap_attribution_readable.csv`). A residual column (value and share of the published figure) is added. Residuals within published rounding read "within rounding" (Henry and Godden). The one ill-conditioned case under the brief's rule (residual under 1% of the figure) is HALF Australia (0.92 points, 0.8%): its rows now print the change in index points and the people it is worth, on Australia's 2011 cropland and pasture (396.1 Mha) over the diet's 2.093 ha a person (189.3 million at this test, 190.8 at the published figure). Example: world pasture as printed, previously "-622%", now "+5.76 points, -9.2 million people". Rows for all printed inputs together (a+b1-b5) were added for Australia and the world. Shares are kept where the residual exceeds 1% of the figure, as the brief's rule says; note that Simpson's (2.3%) and Foran and Poldy's (1.2%) still carry shares of hundreds of per cent (-1057%, +365%), which R03b also cites as ill-conditioned. Whether to widen the threshold is the coordinator's call.

## 3. Intake variant (`intake_variant.csv`; README "Intake variant")

Each food's per-person supply times its eaten share, item by item, on two bases: FAO's waste factor (Gustavsson et al. 2011, Annex 4, North America and Oceania, distribution-and-retail times consumption) and the model's own retail and consumer loss factors (corrected tier, category means from `analysis/loss_factors_2025/compare.csv`). Foods with no factor keep full supply (20% of food energy on FAO's, 37% on the model's), so intake readings are if anything understated. The model's rows do not change (its diet is intake; it charges waste itself).

| Method | Reading | Supply basis (times the corrected model) | Intake, FAO waste factor (times) | Intake, model loss factors (times) | Gap to the corrected model |
|---|---|---|---|---|---|
| Energy and protein balance (Gifford; Henry and Godden) | energy, production as it is | 145 (3.5) | 170 (4.09) | 177 (4.26) | widens |
| Energy and protein balance (Gifford; Henry and Godden) | protein, production as it is | 149 (3.59) | 182 (4.39) | 206 (4.96) | widens |
| Ecological footprint, food row (Simpson) | build 1, cropland-bound | 160 (3.85) | 189 (4.55) | 208 (5.0) | widens |
| Ecological footprint, food row (Simpson) | build 1, pasture | 386 (9.29) | 454 (10.95) | 537 (12.95) | widens |
| Ecological footprint, food row (Simpson) | build 1, crop and pasture together | 343 (8.27) | 405 (9.75) | 472 (11.38) | widens |
| Ecological footprint, food row (Simpson) | build 3 (thesis rates), cropland-bound | 146 (3.52) | 173 (4.16) | 193 (4.65) | widens |
| Ecological footprint, food row (Simpson) | build 3 (thesis rates), pasture | 317 (7.64) | 371 (8.94) | 430 (10.37) | widens |
| Ecological footprint, food row (Simpson) | build 3 (thesis rates), crop and pasture together | 288 (6.93) | 337 (8.12) | 389 (9.36) | widens |
| HALF index (Alexander) | agricultural land over the diet's land a person | 276 (6.64) | 324 (7.82) | 376 (9.05) | widens |
| People per hectare (Cassidy) | this build, delivered calories | 113 (2.72) | 132 (3.18) | 138 (3.32) | widens |
| People per hectare (Cassidy) | second build (V05), delivered calories | 111 (2.67) | 130 (3.12) | 135 (3.26) | widens |
| Commodity balance (Foran and Poldy) | meat | 41.1 (0.99) | 48.1 (1.16) | 58.1 (1.4) | widens |
| Commodity balance (Foran and Poldy) | fish | 12.0 (0.29) | 19.7 (0.47) | 17.9 (0.43) | narrows |
| Commodity balance (Foran and Poldy) | grain with embodied feed grain | 127 (3.05) | 137 (3.31) | 138 (3.33) | widens |
| The model, thesis method corrected | short term, average year | 41.5 (1.0) | 41.5 (1.0) | 41.5 (1.0) | reference |
| The model, improved | short term, average year | 53.6 (1.29) | 53.6 (1.29) | 53.6 (1.29) | reference |

**Result: the gap widens, as R03b said.** Every reading above the model rises (eaten share 0.82 to 0.86 on FAO's factor, so +17% to +22%; +22% to +39% on the model's factors; grain only +8% as Foran and Poldy's embodied feed grain is kept). The calorie and land readings go from 2.7 to 9.3 times the corrected model (supply) to 3.1 to 11.0 (FAO factor) and 3.3 to 13.0 (model factors). The meat count crosses from 0.99 to 1.16 or 1.40 times (widens, now above); fish narrows (0.29 to 0.47 or 0.43). Against the model with no avoidable waste (55.3, the like-for-like intake comparison) the readings are 2.3 to 8.2 times on FAO's factor, meat 0.87. The input share of the harmonised comparison was not recomputed. Footprint build 2 (V04) cannot be re-run, so it has no intake reading. HALF supply reading here is 275.7 (unrounded diet); `harmonised_comparison.csv` holds 275.8 (diet rounded to 1.318 ha).

## Every file changed

New:
* `analysis/method_tests_2025/bases_fidelity.py`
* `analysis/method_tests_2025/bases.csv`
* `analysis/method_tests_2025/fidelity.csv`
* `analysis/method_tests_2025/intake_variant.csv`
* `analysis/method_tests_2025/gap_attribution_readable.csv`
* `qa/reports/B116_bases_and_fidelity.md` (this report)

Edited:
* `analysis/method_tests_2025/make_readme_tables.py`: Table S1 rule and residual column in `t_gap_attribution` (plus the a+b1-b5 rows for HALF Australia and world); new `t_bases`, `t_fidelity`, `t_intake`; `--only` flag.
* `analysis/method_tests_2025/README.md`: three new sections before "Gap attribution" (Bases of each method; Fidelity restated, with replacement wording for 9.1; Intake variant); the gap-attribution block regenerated and one "Table S1 rule" passage added to its Convention paragraph; one clause added to the HALF fidelity paragraph ("on the inputs the paper and its supplement print they are 2.8% and 8.4% high"). B113's harmonised subsection untouched. Only my four generated blocks were replaced (`--write --only gap_attribution,bases,fidelity,intake_variant`).

Unchanged: `gap_attribution.csv` and every other existing csv; `qa/claims_register.csv`; all releases.

## Claim rows that move (id; tier; before; after)

Tier A:
* B058; A; "reproduces the paper for Australia (within 0.8%) and the world (within 2.1%)"; on the current FAOSTAT revision +0.8% (Australia) and -2.2% (world, -2.16% unrounded; 2.1% came from the rounded 34.4); on the authors' printed inputs +8.4% and +2.8%; verdict "partly" for both under decision 109 (fidelity.csv rows "Australia, 2011", "World, 2011").

Tier B:
* B249; B; "reproduced well ... world (within 2.1%) and Australia (within 0.8%)"; as B058: current revision 2.2% and 0.8%, printed inputs 2.8% and 8.4%, verdict partly.
* B260; B; "pasture ... reproduced within 3% (1.718 ha)"; value unchanged (1.718, -2.3%), verdict "partly" under the 2% rule (fidelity.csv row "pasture (food row), 1991-92").
* B278; B; 112.74; +42%; after: 112.74; -0.38 points, +0.6 million people.
* B279; B; 118.88; -622%; after: 118.88; +5.76 points, -9.2 million people.
* B280; B; 113.15; -3%; after: 113.15; +0.03 points, -0.1 million people.
* B281; B; 113.11; +2%; after: 113.11; -0.01 points, 0 million people.
* B282; B; 113.20; -8%; after: 113.20; +0.08 points, -0.1 million people.
* B283; B; 115.88; -298%; after: 115.88; +2.76 points, -4.5 million people.
* B284; B; 113.15; -3%; after: 113.15; +0.03 points, -0.1 million people.

Unchanged but affected in wording (no value moves): B015 and B301 to B304 (Henry and Godden, reproduced, within rounding); B141 and B326 (Foran and Poldy, reproduced); B035, B057, B261 (not reproduced, as before); B094 and B263 (values unchanged; the bases table states 27.6 is an input to no method reading). New claims for a later register job: the fidelity verdicts (fidelity.csv column "verdict"), the bases (bases.csv), the intake readings and the "widens" finding (intake_variant.csv), the people equivalents of HALF Australia's attribution (gap_attribution_readable.csv column "change in people (million)").

## Register rows touched

None.

## Checks

* `python3 -I analysis/method_tests_2025/bases_fidelity.py --check`: "check: 0 mismatches", exit 0.
* Supply-basis readings recomputed here against `harmonised_comparison.csv` column (b): all 14 agree within rounding (printed by the script on each run).
* numbers_lint was not run (it writes a dated report file shared with other builders).

Wrong-value check: (example) a copy of `fidelity.csv` with the HALF Australia printed-input rebuild changed from 121.59 to 119.0 fails the script's own check: `MISMATCH fidelity.csv row 12 column "rebuild on the authors' printed inputs": file '119.0', recomputed '121.59'`, "check: 1 mismatches", exit 1.
