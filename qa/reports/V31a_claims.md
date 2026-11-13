# V31a: second route for cited one-route claims (decision 83)

Checker: blind checker under `qa/briefs/V31a_claims.md` and `qa/briefs/_checker_rules_results_wave.md`. Scratch: `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/V31a/` (own scripts `fp_own.py`, `simpson_own.py`, `hg_own.py`, `compare.py`; script reruns under `repo/`; paper text extracts under `txt/`; Henry and Godden page images under `hg/`).

Blindness note: the brief itself prints each claim's stated value, so the stated values were seen before any derivation. The full register rows (notes, status, locators) were opened only after the derivations below were run.

## Tolerance (set before comparing)

* Counts and labels: exact.
* Model outputs (unrounded figures from a script): within 0.5%.
* Rounded figures: within one unit of the last printed digit (for example 4.65 must lie within 0.01 of my value; 41 within 1).
* Paper quotations: the printed figure must appear on the cited page.

## Deliberate wrong value

`compare.py` was fed two wrong values with my derived values: B147 stated as 45 against my 41.27 (rounded rule, one unit) and the B079 crop count stated as 21 against my 22 (exact rule). Both printed FAIL, so the comparison can fail. The same code then printed PASS for 61 of the remaining comparisons and FAIL for two (B061 and B079, below).

## Routes used

* Route A (rerun): each named script (foran_poldy_balance, henry_godden, simpson_food, half_index, cassidy_people_per_hectare, fearnside_failure_curve, design_choices) was copied with its inputs into `scratch/V31a/repo/` and rerun there; every regenerated CSV is byte-identical to the committed file. This is used only where stdout holds figures the CSV does not.
* Route B (own code, the second route used wherever practicable): `fp_own.py` (Foran and Poldy balance from `fao_au_production_1997_2023.csv` and `fbs_au_world_2021_23.csv`, plus the FAOSTAT year test), `simpson_own.py` (pasture per kg of ruminant protein, 1991-92 plant-food crop land, meat use per person), `hg_own.py` (Henry and Godden edible energy and the 8.8 MJ reading), short inline code for Fearnside (interpolation from `analysis/comparators_2025/rerun.csv`), design choices (ratios from `rerun.csv`, `results/*.csv`, `results/scale_curve.csv`, `diet_land.csv`), HALF (unrounded values and gaps to the paper) and Cassidy (crop count, area, year alignment).
* Route C (text): Foran and Poldy 2002 full report; Henry and Godden 1995 (scanned; read from rendered page images); Simpson et al. 2000; Alexander et al. 2016 and its SI; Cassidy et al. 2013; Fearnside 1985; ABS 4306.0 1991-92; CSIRO and UQ 2025 state of the food system report; `papers/B_methods/SECTION7_DRAFT.md`; `qa/reports/V04_simpson_food.md` and `V05_cassidy.md`.

No tier A rows were in the list (43 tier B, 10 tier C), so no row needed two agreeing routes beyond this second one.

## Claims

### A315 (tier B)
Route: own code: QCL "Meat, Total" mean 2021-23 over FBS "Meat" Food mean 2021-23 (Australia); the model's ratio from `results/2025-fixed.csv` (capacity over population).
My value: produced 4.656 Mt (QCL; the FBS production series gives 4.645), eaten 2.956 Mt, ratio 1.575 (57%); model 41.50/27.61 = 1.50.
Register: 4.65; 2.96; 57%.
Verdict: pass with a note. 4.65 is within one unit of 4.656, but 4.656 rounds to 4.66, which is what B145 and the CSV print. Meat is booked in the same year in both FAO files, so no year mix.
Recommended status: "second route V31a: holds (4.656 rounds to 4.66; write 4.66 to match B145)". Correction: 4.65 to 4.66.

### A318 (tier B)
Route: own code: FBS cereal food 2021-23 per person; Foran and Poldy embodied grain 7.6 Mt / 25.1 million (report p. 64); times the 2025 population 27,608,200 (`results/2025-fixed.csv`); over QCL cereals mean 2021-23.
My value: direct 3.09 Mt (112 kg), feed 8.36 Mt (302.8 kg), total 11.45 Mt, 21.8% of 52.56 Mt.
Register: 11.5; 3.1; 8.4; 112; 303; 52.6.
Verdict: pass with a note. 11.45 is within one unit of 11.5 (rounded parts 3.1 + 8.4 = 11.5; the unrounded sum rounds to 11.4 or 11.5 depending on the food-use population window). "About a fifth" holds. The 52.6 is QCL calendar harvests 2021-23, set beside FBS food use 2021-23: see the year finding (immaterial here).
Recommended status: "second route V31a: holds". No correction needed.

### A319 (tier B)
Route: own code: FBS "Fish, Seafood" Import quantity and Food, Australia 2021-23 (all three years carry the same values); fish capacity as production over food use per person and over Foran and Poldy's 17.5 kg.
My value: imports 593 kt, food 641 kt; 12.1 (actual use) to 16.9 (their requirement) million.
Register: 593; 641; 12 to 17.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B014 (tier B)
Route: text: Henry and Godden 1995, Table 4, p. 99 ("inferred consumption rate factor ... 0.1760 / 0.2041"); arithmetic 82/466 = 0.1760 and 60/294 = 0.2041 from the same table.
My value: 0.1760; 0.2041.
Register: 0.1760; 0.2041.
Verdict: pass.
Recommended status: "second route V31a: holds (Table 4, p. 99, read from the scanned page)".

### B024 (tier B)
Route: own code `hg_own.py`: edible output of FBS 2021-23 production by item, FAO world food-supply energy per kg, divided by 8.8 MJ x 365.25 days.
My value: 781.6 PJ; 243.2 million (243.4 on 365 days).
Register: 243.2.
Verdict: pass. Note: the FBS 2021-23 production behind it carries Australian winter-crop harvests of 2020 to 2022 (year finding); all inputs are from the one file, so the claim does not mix years.
Recommended status: "second route V31a: holds".

### B027 (tier B)
Route: text: Henry and Godden 1995, Table 3, p. 99: contemporary sown pasture 28.3 m ha (crop 17.4, total 45.7); FAOSTAT cropland 2021-23 31,650 kha (`fao_world_land_production.csv`), which the method README says equals the model's ABS holdings to 0.01 Mha.
My value: 28.3; 28.3 + 31.65 = 59.95.
Register: 28.3; 59.95.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B028 (tier C)
Route: text: `henry_godden.py` item list and density function; FBS item names.
My value: FBS 2021-23 mean, world food-supply densities, oilseeds net of processing (meal excluded), no animal fats, no alcohol, no wool or cotton fibre items.
Register: description.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B029 (tier C)
Route: text: Henry and Godden p. 99 (scale by 70/45.7, divide by the inferred factors; "Both previous and contemporary analyses ignored food imports"); p. 100 (wool and cotton scenarios).
My value: description matches.
Register: description.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B032 (tier B)
Route: text: Simpson, Petroeschevsky and Lowe 2000, Table 1, p. 13: food row crop 0.407 (vegetarian 0.312, animal products 0.095), pasture 1.758.
My value: 0.312 + 0.095 + 1.758 = 2.165.
Register: 2.165.
Verdict: pass.
Recommended status: "second route V31a: holds (Table 1, p. 13)".

### B035 (tier B)
Route: own code `simpson_own.py`: ABS 4306.0 Table 1 1991-92 kg a person over FAOSTAT world group yields 1990-92 (cereals, roots, vegetables, fruit, sugar, oil, nuts; pulses 0).
My value: 0.1068 ha (cereals 0.0325, roots 0.0054, vegetables 0.0060, fruit 0.0132, sugar 0.0105, oil 0.0326, nuts 0.0066); 0.312/0.1068 = 2.92.
Register: 0.107.
Verdict: pass.
Recommended status: "second route V31a: holds (rebuild 0.107; not reproduced against the paper's 0.312, as stated)".

### B042 (tier B)
Route: text plus own code: ABS 4306.0 Table 1, 1991-92 column (beef and veal 37.4; lamb 13.4 + mutton 7.6 = 21.0); FBS 2021-23 Food over population (bovine 25.89, mutton and goat 9.72 kg).
My value: 37 to 26; 21 to 10.
Register: 37 to 26; 21 to 10.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B043 (tier B)
Route: own code: world permanent meadows and pastures over world beef, sheep and goat and milk production times FAO world protein per kg (FBS 2021-23), for 1990-92 and 2021-23.
My value: 0.1048; 0.0598 ha per kg.
Register: 0.105; 0.060.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B045 (tier B)
Route: own read of the RL rows in `fao_world_land_production.csv` (Australia).
My value: 2021-23 cropland 31.650, pasture 331.869 Mha (all three years equal); 1991: 17.382 and 445.4; mean 1991-92: 16.89 and 447.5.
Register: 31.65; 331.87.
Verdict: pass with a note: the "1991-92" figures in the statement are the FAOSTAT 1991 single year (the script reads 1991 only), not a 1991-92 mean.
Recommended status: "second route V31a: holds (1991-92 land figures are FAOSTAT 1991)".

### B048 (tier C)
Route: text: `simpson_food.py` (group yields such as "Cereals, primary", "Roots and Tubers, Total"; pulses 0.0); ABS 4306.0 Table 1 (no pulses row; eggs 12.4 kg in the 1978-79 column, "n.c." for 1988-89 and 1991-92); Simpson Table 1, p. 13 (energy 0.43, garden 0.032, forest 0.084).
My value: all elements hold (garden 0.032 and forest 0.084 printed to two places as 0.03 and 0.08).
Register: description.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B049 (tier C)
Route: text: Simpson 2000 p. 13 ("based on world average productivities"); `simpson_food.py` docstring (capacity as Australia's land over land a person).
My value: description matches; the capacity reading is the project's, not the paper's.
Register: description.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B052 (tier B)
Route: rerun of `half_index.py` with unrounded output read in memory; paper value from Alexander 2016 SI Table S5 (SI p. 6): World 35.13.
My value: 34.365 (34.4), gap -2.18%.
Register: 34.4.
Verdict: pass. Note: the register notes carry a stale "rebuild 34.07 (+1.0%)"; the current rebuild for 2011 is 34.37 (-2.2%); 34.1 is the 2021-23 world figure (B066).
Recommended status: "second route V31a: holds (34.37; note 34.07 in the notes is stale)".

### B053 (tier B)
Route: as B052; Table S5: United States of America 97.73.
My value: 94.548, gap -3.26%.
Register: 94.5.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B055 (tier B)
Route: as B052; Table S5: Argentina 114.88.
My value: 109.627, gap -4.57%.
Register: 109.6.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B057 (tier B)
Route: as B052; Table S5: New Zealand 135.76.
My value: 94.760, gap -30.20%.
Register: 94.8.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B060 (tier B)
Route: own read of `half_landuse.csv` (world cropland 1,535.1 Mha, pasture 3,182.08 Mha, 2011) plus the rerun (harvested area 1,317.5 Mha, feed cropland); paper p. 89 ("increased by a factor of 1.129", 1556 and 1378 Mha) and p. 91 (497 and 3203 Mha; 0.65 ha).
My value: 0.6358 ha; 1.1652; 437.6 Mha; 3,182.1 Mha.
Register: 0.636; 1.165; 438; 3,182.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B061 (tier C)
Route: text: Alexander SI Table S3 (90 commodities, SI p. 3) mapped item by item to the commodities `half_index.py` charges land to (56 food balance items with world food use, with "Vegetables" covering tomatoes, onions and vegetables other, "Fruits - Excluding Wine" covering 11 fruit rows, "Treenuts" covering nuts).
My value: 66 of 90 (67 if oil palm fruit is counted through palm oil). Left out: beverages alcoholic, beverages fermented, wine; cocoa, coffee, tea; pimento, spices other; fish; animal fats; nine oilseed cakes; cotton lint, seed cotton, molasses, ricebran oil, oil palm fruit. Beer is included (so "beverages" are not all left out), and offals are not among the paper's 90. The second clause (new FAOSTAT food balance against the authors' FAOSTAT 2015 downloads, paper pp. 89 to 91) holds.
Register: 70 of 90.
Verdict: fail on the count and on the list of what is left out.
Recommended status: "second route V31a: does not hold: 66 of the 90 Table S3 commodities (56 food balance items); left out are beverages other than beer, stimulants, spices, fish, animal fats, the oilseed cakes, cotton lint, molasses and ricebran oil; offals are not in Table S3". Correction: "70 of 90" to "66 of 90", and the left-out list as above.

### B064 (tier B)
Route: rerun, unrounded.
My value: 91.870%; 1.4957 ha; animal 1.3814.
Register: 91.9 (with 1.50 and 1.38).
Verdict: pass.
Recommended status: "second route V31a: holds".

### B066 (tier B)
Route: rerun, unrounded.
My value: 34.107%; 0.5553 ha; animal 0.4496.
Register: 34.1 (with 0.56 and 0.45).
Verdict: pass.
Recommended status: "second route V31a: holds".

### B067 (tier B)
Route: own arithmetic on the unrounded rerun: Australia HALF 113.125 (2011) and 80.976 (2021-23); ha 1.3184 against world 0.5553; animal 1.2149 of 1.3184.
My value: fall 28.4%; 2.37 times; 92.2% animal.
Register: 28; 2.4; 92.
Verdict: pass with a note: the register notes still carry the pre-fix builder checks (84.2/120.9, 84.2/34.1, 1.268/1.371); the values in the statement hold on the current build. The fall is in % of world land; per person the fall is 37% (2.093 to 1.318 ha) because world population grew.
Recommended status: "second route V31a: holds (notes' builder checks are pre-X036 and stale)".

### B071 (tier C)
Route: text: Alexander 2016 p. 89 (pro rata "by the mass used for each category"; processed products on an "approximate economic value basis (Table S4)"), section 2.2 (feed and pasture), p. 91 ("how much land would be used if the global population adopted the average diet"), p. 88 ("HALF is accordingly not predictive").
My value: description matches.
Register: description.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B072 (tier B)
Route: rerun plus own arithmetic: 12.89e15 kcal over 1,061.4 Mha over 985,500 kcal = 12.32; delivered 61% gives 7.5.
My value: 12.3 produced; 7.5 delivered; shares 56/34/11; delivered 61%.
Register: 7.5.
Verdict: pass. Year note: production is from the FBS and area from QCL for the same nominal year (year finding); at world scale the effect is under 1%.
Recommended status: "second route V31a: holds".

### B076 (tier B)
Route: rerun plus own arithmetic: 0.82e15 kcal over 58.7 Mha = 14.2 (14.1 unrounded in the run); delivered 48%.
My value: 14.1; 6.8; 41/46/13; 48%.
Register: 6.8.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B079 (tier B)
Route: own code: summed world 2011 "Area harvested" in `fao_qcl_countries.csv` over the 39 FAOSTAT crop items the script maps; counted the food balance crop items with world production.
My value: 1,061.4 Mha; 22 food balance items (9 cereals, 5 roots, 3 pulses, 4 oilseeds, sugar), drawn from 39 FAOSTAT crop items. Paper: "41 crops on 947 million hectares" (Cassidy p. 4).
Register: 21; 1,061.
Verdict: fail on the crop count (the area and the paper values hold). The script docstring's own list (cereals, roots, pulses, groundnuts, soybeans, rapeseed, sunflower, sugar) also comes to 22. For Australia 2021-23, 19 of the 22 have production.
Recommended status: "second route V31a: does not hold: 22 food balance crop items (39 FAOSTAT crops) on 1,061 Mha". Correction: "21 crops" to "22 crop items" here and in the method README (line 199 also says "Australia's 21 crops"; Australia has 19 with production).

### B082 (tier B)
Route: rerun plus own arithmetic on columns (calories over area over 985,500).
My value: World 7.9 (13.7), United States 8.0 (24.1), India 9.0 (10.8).
Register: 7.9; 8.0; 9.0.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B085 (tier B)
Route: rerun (stdout sensitivity table).
My value: grain-fed share 0 gives 6.1, 1.0 gives 5.8 (Australia 2021-23 delivered).
Register: 6.1 to 5.8.
Verdict: pass with a note: the Australian per-hectare figure is sensitive to the FBS/QCL year pairing (year finding): on 2022-23, pairing FBS production with QCL area of the same nominal years gives 6.39, and with the matching harvest years (QCL 2021-22) 6.00, a 6% shift, larger than the 0 to 100% beef range tested here.
Recommended status: "second route V31a: holds (year pairing moves Australia by about 6%)".

### B086 (tier C)
Route: text: script (KCAL and BEEF_GRAIN_SHARE typed; oilseed 50:50 oil and cake; LIVE has no sheep or goat); Cassidy p. 3 (grazing accounted for by including only feedlot beef).
My value: description matches.
Register: description.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B087 (tier C)
Route: text: Cassidy Table 1, p. 3 (calorie efficiencies 40, 22, 12, 10, 3); p. 2 (exports at "global average allocations for importing nations"); p. 4 (2700 calories a day; cropland).
My value: description matches.
Register: description.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B131 (tier B)
Route: own interpolation on `analysis/comparators_2025/rerun.csv` R1, 2011-fixed (T = 10: 24.68; T = 20: 19.96) at 22.326388 million, linear in T and in log T.
My value: return period 14.99 to 14.13 years; 6.67% to 7.08%.
Register: 6.7 to 7.1.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B134 (tier B)
Route: own arithmetic on rerun.csv R1 2025-fixed (41.50, 30.81, 18.92); average year cross-checked against `results/2025-fixed.csv` zone 1 short (41,503,537).
My value: 25.8% and 54.4% lower.
Register: 26; 54.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B139 (tier C)
Route: text: Fearnside 1985 Fig. 10, p. 353 ("four consumption criteria ... (A) calories; (B) total protein; (C) animal protein; (D) cash per capita"); script docstring (one criterion, wheat, oats and barley record, six run points).
My value: description matches.
Register: description.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B140 (tier B)
Route: text: Foran and Poldy 2002 full report, Table 1.1, p. 31 (20.6, 25.1, 32.5 in 2050), Table 2.5, p. 64 (grain 2.136, 2.713, 3.568; meat 2.278, 2.893, 3.804; fish 0.346, 0.439, 0.577; 1997-98 ABS 31.578, 3.514, 0.223), p. 64 ("an extra six, 7.6 and 10 million tonnes of grain").
My value: all figures as printed.
Register: see statement.
Verdict: pass.
Recommended status: "second route V31a: holds (read in the full report)".

### B142 (tier B)
Route: own arithmetic on Table 2.5: 31.578/2.713; 3.514/2.893; 0.223/0.439; conclusion quoted p. 64 ("a positive food balance in all main food commodity items, apart from fish").
My value: 11.64; 1.215; 0.508.
Register: 11.64; 1.21; 0.51.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B143 (tier B)
Route: own arithmetic: Table 2.5 1997-98 production over base-case requirement per person (115.3 kg meat; 108.1 + 302.8 kg grain; 17.5 kg fish).
My value: meat 30.5; grain with feed grain 76.9; fish 12.8. On FAOSTAT 1997-98 production instead (31.95 Mt cereals, 3.47 Mt meat): 30.1 and 77.8.
Register: 30; 77; 13.
Verdict: pass with a note: the figures use the authors' ABS 1997-98 production, not FAOSTAT as the row's release_or_data field says; on FAOSTAT the grain reading is 78. The register range 30 to 32 and 76 to 80 is in `analysis/comparators_2025/README.md` line 15.
Recommended status: "second route V31a: holds (on the ABS figures of Table 2.5; release_or_data should read 1997-98 published)".

### B144 (tier B)
Route: own code: Table 2.5 base case over 25.1 million; FBS 2021-23 food (cereals, meat, fish) over the 2021-23 mean population (26.203 million).
My value: grain 108.1 (112 actual: 111.9); meat 115.3 (113: 112.8); fish 17.5 (24.5).
Register: 108; 112; 115; 113; 17; 25.
Verdict: pass with a note. Fish 24.46 is within one unit of 25 but rounds to 24. The script divides 2021-23 food by the mean population of 2021 and 2022 only (26.079 million), which gives 24.58 and so 25; on a matching 2021-23 window it is 24.
Recommended status: "second route V31a: holds within one unit (fish 24.5 on a 2021-23 population; script population window is 2021-22)". Correction suggested: fish 25 to 24, or align the script's population window.

### B145 (tier B)
Route: own code: QCL cereals primary and meat total mean 2021-23; FBS fish production mean 2021-23.
My value: 52.5625; 4.6562; 0.295.
Register: 52.56; 4.66; 0.29.
Verdict: pass with a note: fish 0.295 rounds half-up to 0.30; 0.29 is within one unit.
Recommended status: "second route V31a: holds".

### B147 (tier B)
Route: own code: 4.6562 Mt over 112.8 kg (2021-23 population) or 113.4 kg (script window).
My value: 41.3 (41.1).
Register: 41.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B149 (tier B)
Route: own code: 52.5625 Mt over (111.9 + 302.8) kg.
My value: 126.7 (126.6 on the script window).
Register: 127.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B151 (tier B)
Route: own code: 0.295 Mt over 24.46 kg.
My value: 12.06 (12.00 on the script window).
Register: 12.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B154 (tier B)
Route: own code: meat 40.4 (their requirement) and 41.3 (actual use); grain direct 52.5625/108.1 kg = 486.3, with feed grain 126.7; model 41.50 and 53.64 from `results/2025-fixed.csv` and `2025-improved.csv`; balance on 2021-23: grain 52.6 against 2.7 Mt, meat 4.66 against 2.89, fish 0.295 against 0.439.
My value: 40 to 41 against 41.5; grain 3.1 to 11.7 times 41.5.
Register: 40 to 41 vs 41.5.
Verdict: pass with a note: "agrees" holds for the corrected 41.5 only; the improved 53.6 is 31% above the meat count, which the sentence's parenthesis does not say.
Recommended status: "second route V31a: holds for the corrected figure; improved 53.6 does not agree".

### B155 (tier C)
Route: text: Foran and Poldy p. 64 (balance per commodity); comparators README line 15 ("Derived here, not stated by the authors"); script docstring.
My value: description matches.
Register: description.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B243 (tier B)
Route: own ratios from inputs: rerun.csv R1 (41.50/18.92 = 2.19), R2 (45.12/41.50 = 1.087), R3 (55.29/41.50 = 1.332; 62.92/53.64 = 1.173); `results/2025-fixed.csv` (41.50/15.62 = 2.66); `scale_curve.csv` SA2 (41.50/15.53 = 2.67); `diet_land.csv` (103.3/48.3 = 2.14); CSIRO and UQ 100 (100/41.50 = 2.41); checklist numbering from `SECTION7_DRAFT.md` lines 47 to 59 (2 exports, 3 diet, 4 waste, 5 weather, 6 land, 7 unit, 8 time).
My value: above 1.2: items 2, 3, 5, 7, 8, and waste on the corrected method (1.33); waste 1.17 on the improved; land 1.09.
Register: >1.2: items 2, 3, 5, 7, 8; waste 1.33 and 1.17; land 1.09.
Verdict: pass with a note: the value field lists items above 1.2 without item 4, although waste moves the corrected method 1.33 times; the statement handles this in its second clause, so the sentence holds.
Recommended status: "second route V31a: holds".

### B246 (tier B)
Route: own read of `results/2025-fixed.csv` long (15,623,209), rerun.csv R3 2025-improved average year (62.92), `results/2011-thesis.csv` long (9,431,487); CSIRO and UQ report ("100 million people, including 27 million Australians").
My value: 15.6 to 62.9 (factor 4.03); 100 with exports; 9.4 thesis long-term.
Register: 15.6 to 62.9.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B248 (tier B)
Route: own code as B151, B147 and A319 (fish 12.1 to 16.9; meat 40.4 to 41.3).
My value: 12 to 17; 40 to 41.
Register: 12 to 17; 40 to 41.
Verdict: pass.
Recommended status: "second route V31a: holds".

### B249 (tier B)
Route: unrounded rerun against SI Table S5.
My value: world -2.18%; Australia +0.82%; United States -3.26%; Argentina -4.57%; India -7.19%; New Zealand -30.20%.
Register: within 2.1%; within 0.8%.
Verdict: pass with a note: "within 2.1%" holds only on the rounded 34.4 (-2.08%); on the unrounded rebuild the world gap is 2.2%, inside the one-unit tolerance.
Recommended status: "second route V31a: holds (world gap 2.2% unrounded; suggest 'within 2.2%' or 'about 2%')".

### B256 (tier B)
Route: own code (pasture: beef 37.4, sheep 21.0, milk 186.4 kg x world protein per kg x 0.1048 ha per kg protein = 1.736); text: `qa/reports/V04_simpson_food.md` line 3 ("pasture 2.385; paper ... 1.758. Project ... 1.737"); Simpson Table 1, p. 13 (1.758).
My value: project 1.736 to 1.737 (1.2% low); checker 2.385 (+35.7%).
Register: 2.385 against 1.758 (+36%).
Verdict: pass.
Recommended status: "second route V31a: holds".

### B257 (tier B)
Route: text: Cassidy 2013 Table 2, p. 3 (World food 55, feed 36, other 9 by calories); p. 4 ("only 5.57 x 10^15 (59% of the total produced)"); rebuild 56/34/11, 61 from the rerun.
My value: 55; 36; 9; 59 against 56/34/11 and 61.
Register: 55; 36; 9; 59.
Verdict: pass. The "table location not re-checked" note in `published_values.csv` can be closed: Table 2, p. 3.
Recommended status: "second route V31a: holds (Table 2, p. 3; 59% p. 4)".

### B258 (tier B)
Route: text: `qa/reports/V05_cassidy.md` line 3 (checker 5.77 and 7.3); own arithmetic on the unrounded project (147.4 million / 24.5 Mha = 6.02; 9,146.8 / 1,161.8 = 7.87).
My value: Australia 4.1% apart (4.3% of the checker figure); world 7.3% (7.8%).
Register: within 5% (Australia); within 8% (world).
Verdict: pass. Year note: the Australian per-hectare figure carries the FBS/QCL year pairing (B085 note).
Recommended status: "second route V31a: holds".

### B259 (tier B)
Route: own arithmetic 5.77 x 25.1 (V05 line 3) and the project's delivered calories over 985,500 kcal.
My value: 144.8 (about 145); 147.4.
Register: about 145; 147.
Verdict: pass. The 147 does not depend on area, so the year pairing does not touch it.
Recommended status: "second route V31a: holds".

## Summary table

| id | tier | verdict |
|---|---|---|
| A315 | B | pass with a note (4.656 rounds to 4.66) |
| A318 | B | pass with a note |
| A319 | B | pass |
| B014 | B | pass |
| B024 | B | pass |
| B027 | B | pass |
| B028 | C | pass |
| B029 | C | pass |
| B032 | B | pass |
| B035 | B | pass |
| B042 | B | pass |
| B043 | B | pass |
| B045 | B | pass with a note (1991 single year) |
| B048 | C | pass |
| B049 | C | pass |
| B052 | B | pass (notes stale) |
| B053 | B | pass |
| B055 | B | pass |
| B057 | B | pass |
| B060 | B | pass |
| B061 | C | **fail** (66 of 90, not 70; left-out list wrong) |
| B064 | B | pass |
| B066 | B | pass |
| B067 | B | pass with a note (notes stale) |
| B071 | C | pass |
| B072 | B | pass |
| B076 | B | pass |
| B079 | B | **fail** (22 crop items, not 21; area holds) |
| B082 | B | pass |
| B085 | B | pass with a note (year pairing) |
| B086 | C | pass |
| B087 | C | pass |
| B131 | B | pass |
| B134 | B | pass |
| B139 | C | pass |
| B140 | B | pass |
| B142 | B | pass |
| B143 | B | pass with a note (ABS, not FAOSTAT) |
| B144 | B | pass with a note (fish 24.5; script population window) |
| B145 | B | pass with a note |
| B147 | B | pass |
| B149 | B | pass |
| B151 | B | pass |
| B154 | B | pass with a note (improved 53.6 does not agree) |
| B155 | C | pass |
| B243 | B | pass with a note |
| B246 | B | pass |
| B248 | B | pass |
| B249 | B | pass with a note (world gap 2.2% unrounded) |
| B256 | B | pass |
| B257 | B | pass |
| B258 | B | pass |
| B259 | B | pass |

Totals: 53 checked; 40 pass, 11 pass with a note, 2 fail.

## FAOSTAT year finding

Tested on the committed extracts (`fbs_au_world_2021_23.csv`, `half_fbs_countries.csv` against `fao_qcl_countries.csv`, Australia):

* Winter cereals are booked one year behind in the food balance: FBS wheat 2022 = 36,237 kt = QCL wheat 2021 (36,237,477 t); FBS 2023 = 41,199 kt = QCL 2022 (41,199,486 t). Barley (FBS 2022 14,377 = QCL 2021; FBS 2023 13,491 = QCL 2022) and oats (FBS 2022 1,735 = QCL 2021; FBS 2023 960 = QCL 2022) follow the same rule. FBS 2011 wheat (27,410 kt) against QCL 2011 (29,905 kt) is the 2.5 Mt gap V05 noted.
* Sorghum, a summer crop, is booked in the same year in both (FBS 2021 1,639 and 2022 2,648 = QCL 2021 and 2022), and so is meat (FBS bovine 2021 1,894 kt = QCL cattle 2021 1,893,742 t; mutton and goat 684 = 663 + 21.5).
* So FBS "2021-23" carries Australian winter-crop harvests of 2020 to 2022; QCL "2021-23" carries 2021 to 2023.

Which claims mix: the Foran and Poldy rows (A315, A318, B145 to B154, B248) set QCL production beside FBS food use. For meat there is no lag; for grain the FBS side is a consumption figure (2.80 to 3.05 Mt a year), so the mix does not move any printed figure. The Cassidy rows pair FBS production (and uses) with QCL harvested area of the same nominal years: this is a real mix for Australia. On 2022-23 the delivered figure is 6.39 people a hectare with same-year pairing and 6.00 with harvest-matched pairing (QCL area 2021-22), a 6% shift; the 2021-23 window cannot be aligned on disk because QCL 2020 is not extracted. World figures move under 1% (7.92 against 7.97). B085, B258 and the Australian per-hectare readings carry this; B259's people count does not (it uses no area). Henry and Godden (B024) uses the FBS alone, so it does not mix, but its "2021-23 production" is the 2020 to 2022 winter harvests. Simpson 2021-23 and HALF country diets use FBS food only against QCL world yields; consumption is not tied to a harvest year, so no material mix.

## Other findings

* The `foran_poldy_balance.py` population for 2021-23 per-person use is the mean of 2021 and 2022 only (`pop_now = mean(..., ('2021', '2022'))`); this is why fish reads 25 kg rather than 24 (B144). Other printed figures are unchanged by the fix.
* Register notes carry stale builder checks: B052 ("rebuild 34.07 (+1.0%)", the current 2011 rebuild is 34.37) and B067 (84.2/120.9 and 1.268/1.371 are pre-X036 figures).
* B143's release_or_data says "FAOSTAT 1997-98"; the figures use the authors' ABS production in Table 2.5.
* `analysis/method_tests_2025/README.md` line 199 repeats "Australia's 21 crops" (B079).
* All seven scripts rerun in scratch reproduce their committed CSVs byte for byte.

## Rerun commands

From `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/V31a/`: `python3 -I fp_own.py`; `python3 -I simpson_own.py`; `python3 -I hg_own.py`; `python3 -I compare.py`. Script reruns: `cd repo && python3 -I analysis/method_tests_2025/<script>.py`.

## Register rows touched

None. No register, script, result or release file was edited. The only file written in the repository is this report.

## Ids checked

A315, A318, A319, B014, B024, B027, B028, B029, B032, B035, B042, B043, B045, B048, B049, B052, B053, B055, B057, B060, B061, B064, B066, B067, B071, B072, B076, B079, B082, B085, B086, B087, B131, B134, B139, B140, B142, B143, B144, B145, B147, B149, B151, B154, B155, B243, B246, B248, B249, B256, B257, B258, B259 (53).
