# Paper B, round two, brief B139: a third harmonisation line, the bridge from HALF to the model, Table 8 in three panels, the production window, the production comparison (decisions 144 and 145)

All files are new; no existing file, csv or release was changed (the README of this folder is not touched; these notes are in this file). Every script is deterministic (two runs give identical md5 on every csv) and has a `--wrong-value-demo` flag that plants one wrong value and shows its own check failing. Run from the repository root; the model's side is read through the evaluator (`web/src/model/evaluator.js`, unchanged) by `b139_model_runs.mjs`, which needs node.

| Item | Script | Output |
|---|---|---|
| 1 third line | `harmonised_line_c.py` | `harmonised_line_c.csv`, `harmonised_line_c_robustness.csv`, `harmonised_line_c_model_runs.csv` |
| 2 bridge | `bridge_half_to_model.py` | `bridge_half_to_model.csv`, `bridge_groups.csv` |
| 3 panels | `design_choices_panels.py` | `design_choices_panels.csv` |
| 4 production window | `production_window_10y.py`, `extract_fao_au_production_10y.py` (for the fetch) | `production_window_10y.csv` |
| 5 production comparison | `analysis/comparison_2025/production_comparison.py` | `analysis/comparison_2025/production_comparison_2025.csv` |
| shared | `b139_model_runs.mjs` | none (prints JSON) |

## 1. Line (c): one per-person requirement and one waste treatment, for every method and the model

**Expected direction, written in the script's docstring as the brief asks: wider.** The methods divide by the FAO food supply (3,525 kcal, 14.75 MJ a day, waste inside it); the model runs on 8.0 MJ as eaten with waste charged on its own loss factors. Putting the methods on the model's requirement raises every method reading by one factor and most readings are above the model, so the share closed falls. Result: it falls, from 38.5% (line (b)) to 14.7%, and stays positive.

The two requirements and two waste treatments (four cells; shares are of the log distance to 41.5, methods weighted equally):

| Cell | Requirement | Waste | Methods | Model (million) | Share closed to the model | to the median of centres | to the geometric mean | SD of log centres, as run to harmonised (narrowing) |
|---|---|---|---|---|---|---|---|---|
| (b) | as it stands | unequalised | line (b) | 41.5 | 38.5% | 16.0% | 17.2% | 0.65 to 0.44 (31.8%) |
| c1 | 8.0 MJ eaten | the model's loss factors, for all | x 1.512 (grain with embodied feed x 1.10) | 41.5 as run | **14.7%** | 20.0% | 20.7% | 0.65 to 0.48 (26.2%) |
| c2 | FAO supply, waste inside | inside the supply, for all | unchanged | 27.9 (evaluator; 27.45 by the closed form) | 14.3% | 16.0% | 17.2% | 0.65 to 0.44 (31.8%) |
| c3 | 8.0 MJ eaten | none charged to anyone | x 1.844 | 55.3 | 21.0% | 20.9% | 21.7% | 0.65 to 0.50 (23.3%) |
| c4 | FAO supply | none charged to anyone | unchanged | 31.0 | 20.7% | 16.0% | 17.2% | 0.65 to 0.44 (31.8%) |

How the factors are built (all read from the records, none typed): M1 = S s_e / E_m = 14.75 MJ x 0.8202 / 8.0 MJ = 1.512, where 0.8202 is the energy-weighted eaten share of the food balance on the model's own retail and consumer loss factors (`intake_variant.csv`); M0 = 14.75 / 8.0 = 1.844. A method's diet is the food balance mix; scaled to the new energy, the item shares cancel, so one number multiplies every method reading (the protein reading too, as the diet scales as a whole). Only the commodity balance's grain reading differs: their embodied feed grain (303 kg a person) is kept, as in the intake variant, so it rises 10%, not 51%. On the model side, c2 and c4 raise the model's food amount (Settings!B9) to M1 and M0 and run the evaluator; the evaluator gives 27.9 where 41.5 / 1.512 is 27.4, because capacity is not exactly inverse to the food amount (oils and animal fat move with it).

**Per method, share of its own distance to 41.5 closed, line (b) to c1:** footprint 61% to 38%, HALF 68% to 46%, people per hectare 26% to -5%, energy and protein balance 8% to -22%, commodity balance -15% to -19%. The footprint and HALF still close more than a third of their distance on the model's own requirement; the other three move away from the model.

**Which requirement the paper should lead with: 8.0 MJ eaten (c1, waste on the model's loss factors).** Four reasons. (i) 8.0 MJ is a requirement; 3,525 kcal is availability, which carries over-consumption, alcohol and unrecorded waste, so putting the model on it replaces a requirement by a supply figure. (ii) c1 leaves the model at its published 41.5 (the abstract, Table 3, the register's Tier A rows for the model), and moves only the methods, whose figures are in Tables 3, 5 and 6 as harmonised. (iii) c1 and c2 give the same share to the model to within half a point (14.7% and 14.3%), so the choice does not change the finding; c2 belongs in the supplement as the check that the result is not an artefact of who moves. (iv) c2 needs a model reading (27.9 million) that appears nowhere else. The waste choice matters more than the requirement choice: charging the model's waste to the methods (c1, c2) leaves 14 to 15% closed, charging none to anyone (c3, c4) leaves 21%.

**Robustness (`harmonised_line_c_robustness.csv`; B135's core variants: the base case, each of the five methods left out, the fish reading dropped, the pasture-alone footprint readings dropped, the method centre as the median of its readings; nine variants).** Share closed to the corrected model: line (b) 27.7% to 45.9%; c1 3.2% to 23.6%; c2 2.2% to 22.7%. Across the four model reference points (31.1, 41.5, 49.2, 53.6, each scaled with the line's model on c2): c1 2.3% to 30.3%; line (b) 23.2% to 52.8%. To the median of the method centres: c1 12.5% to 39.7%; line (b) 9.4% to 35.5%. Narrowing of the spread of centres: c1 -11.5% to 41.6%; line (b) -11.5% to 47.5% (the commodity balance carries the spread, as in B135: without it the spread widens 11.5% on every line). The B135 land scale-up variants are not repeated (they re-class as-run scaled readings and are not affected by the factor). The model's requirement, if the evaluator's diet energy (7.376 MJ, the diet the model's land is computed from) is used in place of 8.0 MJ, raises M1 and M0 to 1.640 and 2.000 (c2 reads 25.8, c4 28.7: `harmonised_line_c_model_runs.csv`); the records give both figures (the 0.62 MJ difference is drinks and other items outside the land accounting, per the nutrition README) and the direction and ordering do not change.

**Sentences Paper B needs** (5.11, Table 6, the abstract of section 5, S5):
1. "A third line puts every method and the model on one per-person requirement and one waste treatment. With the model's 8.0 MJ a day as eaten and its own retail and consumer loss factors, every method reading is multiplied by 1.51 (the food balance's 14.75 MJ times the eaten share of 0.82, over 8.0). Harmonising then closes 15% of the log distance to the corrected model (14.7%; 38.5% on line (b)), 20% of the distance to the median of the method centres, and narrows the spread of method centres by 26% (standard deviation of logs 0.65 to 0.48). The gap to the model widens, as an intake basis would lead one to expect (section 5.13); the footprint and HALF at Australian productivity still close 38% and 46% of their own distances."
2. "Putting the model on the supply requirement instead (3,525 kcal, waste inside, the model at 27.9 million) gives 14.3%; charging no avoidable waste to anyone gives 21% (the model at 55.3 or 31.0)."
3. Table 6 gains a block for line (c); S5's classification table gains the requirement and waste rows, classed as inputs.

## 2. The bridge from HALF at Australian productivity (76.0 million) to the corrected model (41.5 million)

**One machine for both ends.** People are land over land a person, built group by group in the model's eleven food groups. The model world is the evaluator's diet (cropland and pasture m2 a person, energy, protein, at the model's avoidable waste 0.12 and at 0). The HALF world is the food balance mix of the 46 items HALF counts (13.60 MJ a day), with HALF's own land a tonne split into cropland and pasture (ruminants take all pasture and the feed cropland that remains) and converted to Australian m2 with Australia's own productivity (kappa 0.876 for cropland, 0.218 for pasture: Australia's output in world-average hectares over its hectares, the figures of column (e)). Checked: all switches model-like gives 41.5035 (the evaluator and `results/2025-fixed.csv`, to 1e-6); all switches HALF-like gives 75.97 (HALF's local-productivity reading, column (e) 76.0, equal to (27.73 + 72.42) over 1.3184 ha). B114's variant 1 is reproduced by the pooled-land switch alone at its exchange rate (91.3; 81.70).

**Seven switches** (HALF-like or model-like each; `bridge_groups.csv` lists the two worlds group by group): the land pool; the per-person requirement (13.60 against 7.376 MJ a day); waste (none on top of the supply against the model's loss factors); the diet composition; the yield layer for cropland; the yield layer for pasture-fed output; non-food land. Forward, reverse and the exact average over all 5,040 orderings are in `bridge_half_to_model.csv` (million people, from HALF toward the model; shares are of the total change of -34.46 and can exceed 100%).

| Switch | Forward | Reverse | All-orderings average | Share |
|---|---|---|---|---|
| Land pool: one pool in world-average hectares (k = 4.01) against the model's rule | -6.99 | -5.41 | -6.34 | 18% |
| Per-person requirement (13.60 against 7.376 MJ) | +64.06 | +18.43 | +36.21 | -105% |
| Waste (none on top of the supply against the model's loss factors) | -20.69 | -13.78 | -17.90 | 52% |
| Diet composition (food balance mix against the guideline diet) | -27.24 | -19.96 | -22.65 | 66% |
| Yield layer, cropland | -12.66 | -0.67 | -6.41 | 19% |
| Yield layer, pasture-fed output | -16.91 | -10.53 | -12.96 | 38% |
| Non-food land (wool, fibre, biofuel) | -5.88 | -2.32 | -4.42 | 13% |
| Total change, 75.97 to 41.50 | | | -34.46 | 100% |

Requirement and waste have opposite signs (the model's lower requirement raises capacity, charging waste lowers it), so the pair is the robust number (game G2, requirement and waste as one switch): +16.44 (-48%), then diet composition -21.89 (64%), pasture-fed yield layer -12.53 (36%), cropland yield layer -6.39 (19%), land pool -6.17 (18%), non-food land -3.92 (11%).

**Reading.** The biggest single reason the model reads below HALF is the diet: the model's guideline diet carries about twice the share of food energy from pasture-fed red meat that the Australian food balance does (9.2% against 4.9% of eaten and supplied energy), and pasture-fed food is the binding land. The pasture-fed yield layer is next (HALF charges 60 m2 a kJ a day of pasture to pasture-fed red meat at Australian productivity, the model 74 without waste and 99 with its waste). The pooled-land rule accounts for about a fifth of the net distance when the pool is held in HALF's own currency, the world-average hectare (an Australian cropland m2 worth 4.01 pasture m2); it is a part, not the whole. This is the sufficient-cause wording: pairing is sufficient to account for the residual (B114), and is one of several features that together account for it.

**The pooled-land switch, three ways** (the pool is one formula with an exchange rate k between a cropland m2 and a pasture m2): G1 HALF's own, k = 4.01 (end points exactly HALF's 76.0 and the model's 41.5). G3 B114's variant 1, energy held by substitution at the crop-equivalent energy rate, k = 91.3: the HALF world with that pooling reads 113.6 (not 76.0; the difference is printed, not attributed), the pooled-land switch alone is -43.2 on average (-40.2 reverse, which is B114's +40.2 on the model) and the share 60%. G4, **the protein-held variant**: a linear program at the model's own pool rule, pasture-fed groups down only, every other group between 1 and 3 times its present amount, energy and protein at least the diet's (93.1 g a day): the corrected model reads **85.4 million** (84.9 with a cap of 2, 86.2 with 5), cereals x 1.61, legumes x 3, pasture-fed red meat x 0.33. Holding protein does not lower the pairing's reach: B114's variant 1 (81.7) replaces the pasture-fed energy by the diet's cropland foods in their present proportions, which include crop-fed meat and eggs that need much land, and lets protein fall to 80.9 g; a replacement chosen from cereals and legumes holds both and reads higher. Its exchange rate is k = 145.6; the HALF world with that pooling reads 116.9. Mod Q6 asked for a run that holds protein with legumes for pasture-fed protein: this is it, with the cap of three on legumes stated as a bound.

**What the records cannot separate, and why** (also in the csv notes).
* The requirement from waste. FAO's food supply holds retail and household waste and no record splits it; the two are separated here only through the model's own loss factors. Charging the model's waste to a HALF-like requirement is a double count that no one holds, which is why the pair is the robust number.
* Inside the pasture-fed yield layer. HALF's land a tonne for ruminants is a joint allocation (all world pasture, shared by feed need); the model's is national output over dry-sheep-equivalent land. The difference mixes the allocation rule, the data (FAOSTAT world totals against ABS and AWI national series) and the conversion from world-average to Australian productivity.
* Inside the diet composition. The two diets differ in pattern (meat, oils, sugar) and in what is counted as food (HALF 46 items, the model eleven groups, drinks and sweeteners in one group). The food balance mix is supply energy and the model's mix is eaten energy; no record gives the food-by-food waste of the food balance.
* The protein floor. HALF has no protein constraint and the model's diet is a fixed guideline pattern, so a floor never binds when food is not substituted; it enters only through G4 against G3.
* Land base and population are not switches (FAOSTAT's 363.52 Mha and the ABS holdings agree to 0.01 Mha; no population enters either capacity). Exports enter through kappa, because HALF's numerator is Australia's whole output, and cannot be separated from pasture productivity.
* The model's 8.0 MJ against the 7.376 MJ of the diet its land is computed from: the requirement switch uses 7.376 (the land-bearing diet) against 13.60 (the food balance items HALF counts, 92% of the 3,525 kcal); their ratio, 1.843, equals 14.75 over 8.0 (1.844), so the headline factor of 1.85 in Mod M2 is the same number.

**Sentences Paper B needs** (5.14, section 6/7.6 and H4): "Between HALF at Australian productivity (76.0 million) and the corrected model (41.5) lie 34.5 million. Averaged over every ordering of seven features, the model's lower per-person requirement and its charging of waste together raise the reading by 16.4 million (the requirement alone by 36.2 and waste alone lowering it by 17.9), the model's diet composition lowers it by 21.9, the model's pasture-fed yield layer by 12.5, its cropland yield layer by 6.4, its pooling rule by 6.2 and its non-food land by 3.9. Pairing is a sufficient cause, not shown to be the only one: it accounts for about a fifth of the net distance when land is pooled at world-average hectares and for about three fifths of a larger distance (from 113.6 million) when food is substituted at the crop-equivalent energy rate (81.7 million for the model alone; 85.4 with the protein of the diet held)."

## 3. Table 8 in three panels (`design_choices_panels.csv`)

Panel A (in-model changes, one at a time): 18 rows. Panel B (ratios between methods, not model runs, each labelled): 13 rows. Panel C (the other methods' own factors from their papers, from the literature register): 11 rows, each number checked against the register's `what_taken` text by the script, with the register id and status copied from the file. The ladder (`ladder.csv`, Figure 3's ladder) is dropped from Table 8; `design_choices.csv` and `ladder.csv` are untouched.

**Where the existing Table 8 rows went.**
| Existing row | Placed in |
|---|---|
| Land available (1.09) | Panel A |
| Avoidable waste, improved (1.17) and corrected (1.33) | Panel A, both |
| Australian settings (1.29) | Panel A, marked a bundle, outside the single-choice order |
| Diet, guideline diets (2.14) | Panel A |
| Drought allowance (2.19) | Panel A, "factor on every yield (the model's rule)"; a new row beside it gives the factor on crops only (40.4 against 41.5, 1.03) |
| Time frame (2.66) | Panel A, marked a bundle |
| Unit of self-sufficiency (2.67) | Panel A |
| Diet (optimised) C (7.88) | Panel A as an upper bound, not a realistic diet, outside the ranked rows; new ranked rows for diet A (53.6 to 85.5, 1.60) and diet B (202.1, 3.77) |
| Uncertainty (Monte Carlo), corrected and improved (1.58) | Panel A, last, labelled a spread of joint draws |
| Exports counted, CSIRO and UQ (2.41) | Panel B |
| Exports counted by energy (4.43, 6.36) | Panel B |
New rows: crops-only drought bound; the energy requirement (PAL 1.2 to 2.2: 26.9 to 48.0, 1.78; improved 35.2 to 61.8, 1.76; the drawn window 1.4 to 1.8: 1.27); pasture output minus and plus 20% (33.4 to 49.5, 1.48); in Panel B the food-balance rebuild of the proportional count (68.0 to 70.1 with feed a domestic use, 101.2 to 103.6 without; by mass 45.9 and 53.9, as multiples of 41.5: 1.64 to 1.69, 2.44 to 2.50, 1.11, 1.30) and the footprint's own-productivity ratios of output to consumption (build 1 pooled 2.47, build 3 3.23; cropland 4.29 and 4.47, pasture 2.06 and 2.97), which count exports as the proportional count does (2.41); in Panel C eleven factors (Gifford et al. 1975: exports 2.00, nutrient 1.37; the House of Representatives committee's margin for bad seasons 1.43 to 1.67; Peters et al. 2016, ten diets, 2.01; Peters, Wilkins and Fick 2007, 42 diets, 2.98; Cassidy et al. 2013, 1.68 and 1.7; Alexander et al. 2016, 3.19; Simpson et al. 2000, 3.31; Wackernagel et al. 1999, 1.56) with a "same choice in this study" column.
One Panel C row is flagged unverified in the register: Gifford et al.'s land step from 40.5 to 70 Mha (1.73), the figure Paper B 6.4 cites from Henry and Godden p. 99; the register's L035 holds the 70 Mha and not the 40.5. It needs a register entry for the row to be printed.

**Order of the single in-model choices (panel A, corrected and improved rows mixed, as the paper's Table 8 mixed them), low to high:** drought on crops only 1.03; land 1.09; waste improved 1.17; PAL drawn window 1.27; waste corrected 1.33; pasture output 1.48; diet A 1.60; PAL range 1.76 to 1.78; guideline diets 2.14; drought on every yield 2.19; unit 2.67; diet B 3.77. Bundles and the upper bound are outside it: Australian settings 1.29, time frame 2.66, diet C 7.88. The Monte Carlo 1.58 sits between pasture output and diet A. Land is the smallest factor among the definitions (1.09), no longer the smallest of all rows (1.03 for the crop-only drought bound). The top of the in-model order is the unit (2.67) and diet B (3.77), not the optimised diet C and not the exports.

**Sentences Paper B needs** (6.1, 6.10, 6.11, Table 8, S4): the opening of 6.1 "with the author's model on the same 2025 data" applies to panel A only; panels B and C are labelled comparisons; 6.10 and Figure 3 lose the ladder and its 223.9 rung; 6.11's sentence "From lowest to highest draw the factor is 2.22" is dropped (Mod minor 8) and the ordering is read from panel A; the 18.9 to 55.3 span sentence follows decision 146 (one at a time, 40.4 with the allowance on crops only); Table S4's column "factor measured in section 6" changes for exports (a ratio between methods) and for diet (A and B, with C an upper bound).

## 4. The ten-year production window (`production_window_10y.csv`)

**What is held.** FAOSTAT Australian production and area harvested are on disk for 2011 and 2020 to 2023 (and 1997, 1998 for three items). The window 2014 to 2023 is not held: four of its ten years (2020 to 2023) are. The script uses what is held (window "five held years", 2011 and 2020 to 2023; "held years of the decade", 2020 to 2023; "held years outside 2021-23", 2011 and 2020) and computes the ten-year rows when `fao_au_production_2014_2023.csv` exists; if the file is absent those rows are present and empty.

**The fetch for Murray.** URL: `https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_All_Data_(Normalized).zip` (FAOSTAT, CC BY 4.0; the file is pinned in `qa/fao_bulk_hashes.csv`: zip sha256 `c5835418c18f9322e7decbd6800f93a216eaae3cdfa31acb08f0518c0c6d6853`, FAO file dated 2025-12-23). Then `extract_fao_au_production_10y.py` (docstring has the four commands, including the hash check) writes `fao_au_production_2014_2023.csv`, and `production_window_10y.py` fills the ten-year rows. The extractor was tested on a synthetic bulk-layout file (340 rows; a missing year stops it) and the ten-year path of the window script was run on that synthetic file; neither synthetic file is filed.

**Result on the years held.** 2021 to 2023 is above the mean of the five held years for crops and slightly above for livestock:

| Median over groups | 2021-23 over the five held years | over 2020 to 2023 | over 2011 and 2020 |
|---|---|---|---|
| Crops, production (8 groups) | +9.3% | +5.3% | +27.2% |
| Crops, yield (production over area harvested) | +4.2% | +1.4% | +14.1% |
| Livestock, production (6 groups) | +3.3% | +0.5% | +8.7% |

Cereals: production +5.2%, yield +8.9% against the five held years; beef -2.4%, sheep and goat meat +9.1%, milk -2.0%, total meat +2.9%. The window is partly circular (it contains 2021 to 2023), so the ten-year fetch is needed for the paper to state a ten-year figure.

**The model with its yield layers on the window** (every plant row and feed-based animal row by the crop yield ratio, the pasture-fed rows by their own item; 2021-23 stands for the model's own windows). Corrected, short term, 41.50 million: five held years 41.35 (crops only 41.44, livestock only 41.41; -0.37%); 2020 to 2023 41.63 (+0.31%); 2011 and 2020 only 40.73 (-1.87%). Pasture binds, so capacity follows the pasture rows almost one for one and the crop rows hardly at all (pasture output minus 20% gives 33.43 million, B134, reproduced). The ten-year row will lie in this span unless the ten years differ more than the five held.

**Sentences Paper B needs** (S3 or 8, R05b issue 12): "FAOSTAT's Australian production is held for 2011 and 2020 to 2023 in the extracts used here. Against the mean of these years 2021 to 2023 is higher by 9% for crop production (4% for yield) and by 3% for livestock production; rescaling the model's yield layers to that window lowers the short-term capacity by 0.4% (41.5 to 41.35 million). The ten-year window 2014 to 2023 was not held and is listed for fetching."

## 5. The production comparison (`analysis/comparison_2025/production_comparison_2025.csv`)

The model's production inputs against FAOSTAT's for the same items and years, with the year rule typed first: winter field crops are harvested in the calendar year the ABS crop year starts (ABS 2022-23 is FAOSTAT 2022), summer crops and horticulture in the year it ends (ABS 2022-23 is FAOSTAT 2023).

* **Land:** cropland 31.65 Mha and pasture 331.87 Mha of the ABS holdings against FAOSTAT's land use, 363.52 Mha together, difference 0.00 Mha.
* **Field crops** (wheat, oats, barley, sorghum, maize, rice, sugar cane, canola, chickpeas, lentils; 26 comparisons, 2020-21, 2022-23, 2023-24): the model's ABS production equals FAOSTAT's to 0.0002% (the rounding of FAOSTAT's figures; FAOSTAT carries the ABS series), 94% of the tonnes of the compared crops in 2020-21.
* **Fruit and vegetables** (18 items, 19 comparisons): FAOSTAT's series is not the ABS series; median absolute difference 13.1%, range 0.0 to 59.2% (almonds, probably in shell against kernel, not checked), 6% of the compared tonnes.
* **Milk:** the model's input (the 2010 national milk times Dairy Australia's change) is within 0.1% to 3.5% of FAOSTAT's, depending on which calendar year the financial year is set against (both are shown); **wool:** 2.8% above FAOSTAT's shorn greasy wool where FAOSTAT equals the AWI figure (the model's base is the ABS 2009-10 total, 352,737 t, against AWI's 343 Mkg), -13% to +7% in the other comparisons.
* **Beef and sheep meat:** the model's inputs are ABS tonnes times a calibration to the thesis's 2010 figure (cattle 1.086, sheep and lamb 1.155); the ABS tables are not on disk, so the 2022-23 to 2024-25 inputs cannot be recomputed. The archive's 2010 bases are 7.6% (cattle) and 21.8% (sheep) above FAOSTAT's 2011 (a one-year offset, and FAOSTAT's sheep figure includes goat); the repository's reported 2020-21 cattle meat of 2.10 Mt is 1.2% below FAOSTAT's 2020 (reported, not recomputed).
* **Poultry meat, pig meat and eggs:** no production input (the model sets their yield from grain yield over a feed conversion ratio); FAOSTAT's figures are listed for reference.

**The sentence that makes the data claim true** (for the abstract's "Australian data for 2021 to 2023 (FAOSTAT 2025; the model on its own 2025 layer)" and 5.1): "The methods and the model share a common land base (FAOSTAT's 363.52 Mha of cropland and pasture, which the ABS holdings under the model match to 0.01 Mha) and the methods share the FAO food balance for 2021 to 2023; the model keeps its own diet and its own production layer, which is ABS-based, equals FAOSTAT's for the field crops, lies within 4% of FAOSTAT's for milk, differs for fruit and vegetables, and carries a calibration to the thesis's meat figures that FAOSTAT does not (Table S6)."

## Files changed

New: `b139_model_runs.mjs`, `harmonised_line_c.py`, `harmonised_line_c.csv`, `harmonised_line_c_robustness.csv`, `harmonised_line_c_model_runs.csv`, `bridge_half_to_model.py`, `bridge_half_to_model.csv`, `bridge_groups.csv`, `design_choices_panels.py`, `design_choices_panels.csv`, `production_window_10y.py`, `production_window_10y.csv`, `extract_fao_au_production_10y.py`, this file; and in `analysis/comparison_2025/`: `production_comparison.py`, `production_comparison_2025.csv`. Nothing in `analysis/pasture_2025/`; no existing file edited.
