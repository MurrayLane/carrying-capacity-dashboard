# B58: the harmonised comparison of the methods (decision 35)

Files written: `analysis/method_tests_2025/harmonised_comparison.py`, `analysis/method_tests_2025/harmonised_comparison.csv` (one row per method and reading, plus one summary row), a new table function `t_harmonised` and table id `harmonised_comparison` in `analysis/method_tests_2025/make_readme_tables.py`, a new README section "Harmonised comparison (decision 35; ...)" at the end of `analysis/method_tests_2025/README.md`, and this report. No existing output changed: `simpson_food.py` and `half_index.py` are run in memory up to the line that writes their csv, so their csvs are not rewritten. `--write` also refreshed the commit line of the 14 existing generated blocks (4bfa592 to 8906682, content identical); those 14 lines were set back to 4bfa592, so the only README change is the new section.

## The boundary as applied

* **Land base.** FAOSTAT agricultural land 2021-23 (cropland 31.650 + pasture 331.869 = 363.519 Mha) and the model's ABS holdings (zone 1 of `web/public/data/2025-fixed/regions.json`: cropping 316,499 km2, pasture 3,318,689 km2 = 363.519 Mha) are the same to 0.01 Mha, so one run serves both (the script asserts it). A method that counts production counts the production of that land: Henry and Godden's scale-up to Nix's 70 Mha and Cassidy's rate on all cropland are removed.
* **Consumption basis.** FAO food balance 2021-23, per person as FAO gives it: 3,525 kcal and 120.7 g of protein a day; food use in kilograms (Foran and Poldy).
* **Population.** No harmonised method reading takes a head count as an input; the per-person bases use FAO's own head count (26.20 million, 2021-23). The 27,608,200 enters only the model rows. Dividing 2021-23 food totals by the 2025 head count instead would raise the per-person-consumption readings in proportion (factor 27.61 / 26.20); not done, stated in Limits.
* **Data year.** Footprint build 3 was the one reading off the 2021-23 vintage (1990 thesis yields); its dated yield rows are replaced by FAOSTAT 2021-23 world yields of the same rows. Its sheep-meat pasture rate (a stocking-rate figure, not a dated yield), feed ratio, food energies, cane ratio and garden-at-vegetable-yield rule are kept.
* **Kept everywhere:** world-average productivity (Simpson, HALF), no diet balance (Henry and Godden), cropland only (Cassidy), item by item (Foran and Poldy), weather record (Fearnside), the model's pairing. No method is given the model's diet, yields or land classes.
* **Fearnside:** cannot take an equalised input (its readings are the model's runs); (b) to (d) left blank.
* **Sanctioned sensitivity (e):** local-productivity adjustment (Wackernagel and Rees 1996, p. 78): Australia's land expressed in world-average hectares as the hectares that would grow Australia's 2021-23 output at the method's own world-average productivity, divided by the same footprint. Done for footprint builds 1 and 3 and HALF; build 2 (V04) cannot be re-run.

## The table (generated, README)

| Method | (a) As the authors would run it | (b) Harmonised | (c) Input effect, b over a | (d) b over the model, corrected and improved | (e) Local-productivity adjustment (p. 78) |
|---|---|---|---|---|---|
| Energy and protein balance (Gifford; Henry and Godden) | 134 to 211 | 145 (energy), 149 (protein) | 0.69 to 1.11 | 3.50 to 3.59 and 2.71 to 2.78 | |
| Ecological footprint, food row (Simpson) | 103 to 343 (cropland-bound 103 to 160; together 268 to 343) | 139 to 343 (cropland-bound 139 to 160; together 278 to 343) | 1.00 to 1.42 | 3.36 to 8.27 and 2.60 to 6.41 | 64.8 to 117 (cropland-bound 113 to 117; together 64.8 to 84.6; pasture alone 53.9 to 77.9); builds 1 and 3 |
| HALF index (Alexander) | 276 | 276 | 1.00 | 6.65 and 5.15 | 76.0 |
| People per hectare (Cassidy) | 145 to 190 | 111 to 113 | 0.59 to 0.77 | 2.67 to 2.72 and 2.07 to 2.11 | |
| Commodity balance (Foran and Poldy) | meat 40, fish 17, grain 128 | meat 41, fish 12, grain 127 | 0.71 to 1.03 | 0.29 to 3.06 and 0.22 to 2.37 | |
| Failure probability (Fearnside) | 41.5 (average year), 30.8 (1 in 10), 18.9 (1 in 100) | blank: the readings are the model's own runs | | | |
| **The model, thesis method corrected** | **41.5** | **41.5** | 1.00 | 1.00 and 0.77 | |
| **The model, improved** | **53.6** | **53.6** | 1.00 | 1.29 and 1.00 | |

## Reading

* Inputs move readings by factors of 0.59 to 1.42; methods stay on their side of the model (calorie and land methods 2.7 to 8.3 times the corrected 41.5; the commodity balance's meat 41, at the model). On a ratio scale (input factor a/b times method factor b/41.5, exact), with the five methods weighted equally, inputs are 10% of the distance and methods 90% (mean absolute log factors 0.14 and 1.35).
* Largest input effects: land bases beyond the land in use (Henry and Godden over 45.7 Mha, 211 to 145; Cassidy on all cropland, 190 to 113) and consumption bases (Cassidy's 2,700 kcal against 3,525: factor 0.77; protein balance 134 to 149; Foran and Poldy's fish 17 to 12). Footprint build 3 rises 103 to 146 (cropland-bound) on current yields.
* The spread does not narrow: 17 to 343 as run, 12 to 343 harmonised.
* With the p. 78 adjustment the footprint methods fall to 64.8 to 84.6 (together) and HALF to 76.0: Australian output is 22.3 Mha of world-average cropland and 46.4 Mha of world-average pasture in build 1 (25.3 and 81.6 in build 3 at the thesis rates; 27.7 and 72.4 on HALF's rules), against 31.65 and 331.87 Mha. Build 1's pasture-alone reading (53.9) sits at the improved model.

## Limits

Only inputs a method takes are equalised and every defining choice is kept, so the method effect is left whole; the ladder (`ladder.csv`), not this table, is where the model is run under other definitions. Fearnside blank by construction. Build 2 used as filed. Per-person bases on FAO's head count (population choice above). Local productivity counts food output, exports included; non-food crops (cotton lint, fodder) are not converted, a slight understatement of world-average cropland. Foran and Poldy's embodied feed grain per person kept (the food balance's feed covers livestock for export too); their readings are whole millions.

## Findings outside the brief's scope

* **Mislabelled second-build value (new defect).** `second_build_values.csv` row "people, crop plus pasture together, second build, 2021-23 (million)" = 307 is V04's pasture-only reading (331.87 Mha / 1.082 ha = 306.7; V04 itself says "307 on pasture"). On V04's own footprint, crop and pasture together is 363.52 / (0.227 + 1.082) = 277.7. It enters `simpson_food.py` and `cross_method.py` (s_both), and the README footprint section says "Build 2 gives 140 million on cropland and 307 million together (V04)". The cross-method range 103 to 343 and B044's "together 268 to 343" do not change (both 307 and 277.7 lie inside).
* **Rounding.** `cross_method.csv` holds HALF as 276 (from 275.8) and the filed build 2 cropland as 140 (31.65 / 0.227 = 139.4); the csv leaves the (c) cell blank for build 2 cropland and uses the unrounded HALF value in (a).

## numbers_lint

`python3 -I qa/tools/numbers_lint.py`, last line: `report: qa/reports/numbers_lint_2026-11-07.csv (3860 rows)`. Methods README: not found 312 before, 318 after. The six new not-found are all in the new section and are labels or round numbers the tolerance rule cannot anchor: "70" (Nix's 70 Mha, a quoted input), the commit hash 8906682 of the new block, "40" (Foran and Poldy meat, a whole-million value present as 40.0 in the csv, unanchored because a trailing zero widens the tolerance), "10" and "100" (the "1 in 10" and "1 in 100" labels), and "10%" (the input share, present in the summary note as 10%).

## Register rows whose value or status this changes

* **X093** (footprint reading without the p. 78 adjustment): the adjustment is computed in B58 (`harmonised_comparison.csv` column (e): footprint 64.8 to 84.6 together, HALF 76.0). Proposed status: open to "computed in B58; the cross-method README and B068 wording to say that 276 is the unadjusted reading and cite the adjusted 76.0".
* **B068** (HALF footprint reading, 276): value unchanged; notes should add the local-productivity reading 76.0 (X093).
* **B044, B046** (footprint readings): values unchanged; notes should record that the build 2 "together" input of 307 is the pasture-only reading (new defect below), the correct together value 277.7, range unaffected.
* **B156, B247** ("about two to eight times"): unchanged; the harmonised readings (2.7 to 8.3 times) support them with inputs equalised.
* **New defect (proposed):** `second_build_values.csv` labels V04's pasture-only 307 as crop plus pasture together (correct together 277.7); also in the README footprint section ("307 million together") and the cross-method Simpson range inputs; found by B58.
* No existing claim value changes: no existing output was changed.

## New claims for the coordinator to register (value; output locator in `analysis/method_tests_2025/harmonised_comparison.csv`)

1. One land base serves both: FAOSTAT 2021-23 agricultural land 363.5 Mha equals the model's ABS holdings to 0.01 Mha; 363.5; row "The model, thesis method corrected", column "inputs equalised" (and the assertion in the script).
2. Food balance per person 2021-23: 3,525 kcal and 120.7 g protein a day; 3525; 120.7; rows "Energy and protein balance", column "inputs equalised".
3. Energy and protein balance harmonised: 145.2 (energy) and 148.8 (protein) million; rows "energy, production as it is" and "protein, production as it is", column (b).
4. Energy and protein balance input factors 0.69 to 1.11 (b over a); column "(c) input effect, b over a", rows "energy, scaled to Nix's 70 Mha over 45.7 Mha in use" (0.689) and "protein, production as it is" (1.112).
5. Energy and protein balance harmonised is 3.50 to 3.59 times the corrected model and 2.71 to 2.78 times the improved; columns "(d) b over corrected" and "(d) b over improved".
6. Footprint build 1 needs no harmonisation: 159.8 (cropland-bound) and 343.4 (together), input effect 0.0; rows "build 1, ...", columns (a) to (c).
7. Footprint build 3 on 2021-23 world yields: cropland-bound 146.2 (from 103.1, factor 1.419), together 287.7 (from 268.4), pasture 316.9 unchanged; footprint 0.216 ha crop and 1.047 pasture a person; rows "build 3 (thesis rates), ...", column (b) and note.
8. Footprint build 2 together on its own footprint: 277.7 (the filed 307 is its pasture-only reading); row "build 2 (V04), crop and pasture together", column (b) and note.
9. Footprint at local productivity (p. 78): build 1 cropland-bound 112.5, pasture 53.9, together 64.8; build 3 117.0, 77.9, 84.6; column (e), rows "build 1, ..." and "build 3 (thesis rates), ...".
10. Australian output in world-average hectares: build 1 cropland 22.3 Mha, pasture 46.4 Mha; build 3 25.3 and 81.6; HALF 27.7 and 72.4; column "note" of the build 1, build 3 and HALF rows.
11. HALF harmonised 275.8 (input factor 1.0), 6.65 times the corrected and 5.15 times the improved model; local productivity 76.0; row "HALF index (Alexander)", columns (b), (d), (e).
12. Cassidy harmonised: 112.9 (this build) and 110.9 (second build) million, factor 0.766 from the consumption basis; the all-cropland reading 190 falls to 112.9 (factor 0.594); rows "People per hectare (Cassidy)", columns (b) and (c).
13. Foran and Poldy harmonised: meat 41, fish 12, grain with embodied feed grain 127; meat at 0.99 times the corrected model; rows "Commodity balance (Foran and Poldy)", columns (b) and "(d) b over corrected".
14. Fearnside cannot take an equalised input; (b) to (d) blank; rows "Failure probability (Fearnside)".
15. Inputs are 10% of the ratio-scale distance from the corrected model and methods 90% (mean absolute log factors 0.14 and 1.35, five methods weighted equally); input factors 0.59 to 1.42; row "Summary (5 methods with a harmonised reading)", column "note".
16. The spread among methods does not narrow: 17 to 343 as run, 12 to 343 harmonised; column (a) row "Commodity balance, fish" (17.0) and column (b) rows "Commodity balance, fish" (12.0) and "build 1, crop and pasture together" (343.4).
