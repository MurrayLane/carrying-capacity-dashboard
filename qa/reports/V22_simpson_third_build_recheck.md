# V22 report: re-check of the third Simpson build on the thesis rates (decision 32)

Checker rules followed (`qa/briefs/_checker_rules_results_wave.md`). No repository file was edited and the script under test was not run (it writes into the repository); B45/B47 material was not opened. Files under test were opened only for part C.

**Tolerance, set before comparing:** counts and names exact; capacities within 0.5%; shares, ratios and ha figures within one unit of the last printed digit (for example 1.718 means 1.717 to 1.719); the "within 3%" test means |gap| <= 3.0%.
**Can-fail:** (1) red meat changed from 58.4 to 63.0 kg: my pasture goes to 1.853, +5.4% against 1.758, reported "OUTSIDE 3%", and "MISMATCH" against 1.718. (2) With the unrounded sheep-meat rate (5.5 x 5 x 1.24 = 34.1) my pasture is 1.7126 and the code reported MISMATCH against 1.718; with the printed 34 it reports match. So the comparison does fail on a wrong value.

## A. Rates in the scan (thesis page = PDF page minus 10)

| Rate | Holds? | Where, quoted |
|---|---|---|
| Sheep meat 34 kg/ha/yr (5.5 kg a sheep, 5 sheep an animal unit, 1.24 AU/ha) | holds | p. 285 (e41): "5.5 [kg/sheep/yr] * 5 [sheep/animal unit] * 1.24 [animal units/ha] = 34 [kg/ha/yr] of meat"; 5.5 kg and "5 sheep correspond to 1 animal unit ... 1.24 [ha]" on p. 284. (Exact product is 34.1.) |
| Wool 10.5 gross, 14.2 net, 26% of sheep pasture to meat | holds | p. 285: "1.7 ... * 5 ... * 1.24 ... = 10.5 [kg/ha/yr] of wool"; "34 /129 ... =) 26 % ... 26 % of a sheep's pasture requirement is used for meat production ... 10.5 [kg/ha/yr] /(1-0.26) [ha] = 14.2 [kg/ha/yr] net wool production". Wool is "wool, scoured" (Table A2.3 row 104, p. 297; 1,940,989 t used on p. 284). |
| Cattle pasture 0.00322 ha yr/kg meat | holds | p. 284 (e12, 3rd calculation): "(79.3% * 12,195,000 [cattle] / 1.24 [cattle/ha]) / 2,423,435,000 [kg meat consumed/yr] = 0.00322 [ha*yr/kg]" |
| Feed cropland 0.00457 | holds | p. 284: "92 [kg meat/cap/yr] / 0.42 [ha crop land for feed stock/cap] (see d12) = 0.00457 [ha*yr/kg]" (total 0.00779, "or 129 [kg/yr/ha] of meat") |
| Table A2.2 world yields (kg/ha) | holds | p. 295: cereals 2646 (row 15), wheat 2381 (16), rice 3350 (17), oats 1821 (22), potatoes 15315 (26), vegetables and melons 15000 (49), fruits without melons 7000 (also 7000 for each fruit row on p. 296), sugar cane 60229 (67, note "13 [kg] of sugar canes produce 1 [kg] of sugar"; beets 35573, "6 [kg] beets produce 1 [kg] sugar") |
| Garden at 15 t/ha | holds | p. 279 (c11): "the assumed average yield for vegetables (and fruits) is 15 [t] per hectare (Table A2.2)" |
| 6:1 feed ratio for pork, poultry, eggs | holds | p. 281 (d12, Calculations): "on average it requires 8 [j] feedstock to produce 1 [j] of animal products. In fact, for beef this ratio is 16; for pork, turkey, chicken and eggs it is 6; for milk it is 5 (Corson 1990:74, de Looy 1987:132-136)". It is an energy ratio (J feed per J product), not a mass ratio. |

Food energies used in part B: cereal 13,020 kJ/kg (p. 281); meat 13,000, milk 2,720, eggs 6,120 MJ/t (Table A2.3, p. 297); Table A2.4 (p. 298): meat 11,000, poultry 8,000, eggs 6,000 kJ/kg.

## B. My own build (ABS 4306.0 Table 1, 1991-92, kg a person)

Inputs read from the pdftotext layout of Table 1: beef and veal 37.4, lamb 13.4, mutton 7.6, pigmeat 19.3, poultry 25.9; flour 71.7, breakfast foods 11.9, table rice 5.6; potatoes 66.6, vegetables total 153.2; fruit total (fresh equivalent) 120.1; peanuts 2.2, tree nuts 4.3; oils and fats total 19.6 (butter 2.6); sugars total 45.6; eggs "n.c." in kg, 129 eggs (1978-79: 12.4 kg for 220 eggs).

| Component | My treatment | Mine | vs Simpson | vs build-3 claim |
|---|---|---|---|---|
| (1) Pasture | 58.4 kg red meat / 34 kg/ha, no dairy | 1.7176 | 1.758: -2.3% (within 3%) | 1.718: holds |
| (2) Plant crop | flour at wheat, all breakfast foods at oats, rice at rice, sugar as cane 13:1, potatoes at potato yield, peanuts 1124, tree nuts 1000; oils excluded (no oil yield in the thesis) | 0.0588 | 0.312: -81% | 0.074: does not hold on my treatment |
| (2) variant | as above plus non-butter fat (17.0 kg) at rapeseed seed yield 1239 | 0.0725 | -77% | 0.074: does not hold (outside one digit) |
| (3) Garden | fruit 120.1 + vegetables less potatoes 86.6, at 15 t/ha | 0.0138 | 0.032: -57% | 0.014: holds |
| (4) Feed crop, 6:1 by mass, eggs 129 x 50 g = 6.45 kg | (pork+poultry+eggs) x 6 / 2646 | 0.1171 | 0.095: +23% | 0.116: does not hold by mass (holds only at 46.5 g eggs, 0.1161) |
| (4) Feed crop, 6:1 by energy, eggs 12.4 kg, pork and poultry at meat 13,000 MJ/t, eggs 6,120 (A2.3) | | 0.1156 | +22% | 0.116: holds |
| (4) Feed crop, by energy at Table A2.4 (11,000 / 8,000 / 6,000), eggs 12.4 kg | | 0.0860 | -9.5% | 0.086: holds |
| Wool at 14.2 kg/ha | 0.854 x 14.2 | 12.13 kg | | 12.1: holds |
| Wool at 10.5 kg/ha | 0.854 x 10.5 | 8.97 kg (9.00 at 10.54) | | 9.0: holds |

The plant-crop difference is treatment only: with oatmeal (1.5 kg, ABS Table 3) at oats and other breakfast foods (10.4) at the cereals average, and oils (17.0 kg) at the 1,000 kg/ha placeholder, my code gives 0.0739, so the claim of 0.074 reproduces under the file's stated treatment. Every treatment I tried lies between 0.059 and 0.074, a quarter or less of 0.312. Feed crop: the 6:1 ratio is stated in energy terms, so the energy build is the faithful one; it matches the claim.

## C. Files under test

Figures in `simpson_food.csv` (build 3) against mine: pasture 1.718 = 1.7176; plant foods 0.074 (mine 0.0739 under their treatment, 0.0588 to 0.0725 under mine); garden 0.0138 = 0.0138; feed 0.1156 = 0.1156; feed at A2.4 energies 0.086 = 0.0860; cattle-rate pasture 0.188 = 58.4 x 0.00322 = 0.1880; wool 12.13 and 8.97 = mine; thesis wool rule 1.8 / 14.2 = 0.127 = mine. No difference in figures beyond my own treatment choices.

Statements:
1. **"Pasture reproduced within 3% at the thesis's sheep-meat rate": holds.** 1.718 against 1.758, -2.3%. At the unrounded 34.1 it is -2.6%, still within 3%.
2. **"Feed crop matched by two of three builds": holds.** Builds 1 and 2 are taken as filed (0.098, 3.6% high; 0.094, 1.1% low); I did not rebuild them. Build 3 is 0.116 (22% high) and is not matched, as I also find. The README adds that 0.086 at Table A2.4 energies is 9% low (mine -9.5%, which rounds to 9%); the cross-method fidelity text gives only the 22% figure.
3. **"Plant-food crop not reproduced by any of three builds": holds.** 0.074, 0.107, 0.142 against 0.312; my own range 0.059 to 0.074.
4. **"Wool not reproduced from the published sources": holds** on the readings I could check (12.13 and 8.97 kg needed; thesis rule gives 0.127 ha, not 0.854). The ABS 7503.0 reading (1,063.8 kt greasy, 35.9 kg clean a person, 2.529 and 3.42 ha) is outside my inputs: cannot determine those three numbers.
5. **Cross-method Simpson reading "103 to 343 (cropland-bound 103 to 160; crop and pasture together 268 to 343)": holds.** `cross_method.csv` prints exactly this, low 103, high 343; it takes min and max over (V04 140 and 307; build 1 159.8 and 343.4; build 3 103.1 and 268.4).
6. **2021-23 build-3 reading (crop 0.307 with garden, pasture 1.047; 103, 317 and 268 million): holds as arithmetic.** 31.65 / 0.307 = 103.1; 331.87 / 1.047 = 317.0; 363.52 / 1.354 = 268.5 (CSV 268.4 from unrounded inputs; within 0.5%). I did not rebuild the 2021-23 consumption (FAO food balance sheet, not a named input): cannot determine 0.307 and 1.047 themselves.
7. **Prose states sources and assumptions without judging the authors: holds.** "Sources used" lists the paper, ABS 4306.0, Wackernagel and Rees 1996, the thesis pages and ABS 7503.0, and says the authors were not consulted (Murray's decision). Assumptions are listed per component; verdicts are "reproduced / not reproduced on the sources used"; unresolved readings are "left open". No words of fault (error, mistake, wrong, flaw) about the authors.

## Found beyond the brief

* **Eggs 12.4 kg is the 1978-79 three-year average carried forward** (the README says so). ABS Table 1 gives 129 eggs a person in 1991-92 against 220 in 1978-79; at the 1978-79 weight per egg that is about 7.3 kg. With 7.3 kg: build 3 feed 0.110 (16% high, still not matched), A2.4 variant 0.081 (15% low); build 1 feed for eggs about 0.0069, build 1 feed about 0.094 (still matched). No verdict changes, but the carried-forward figure overstates eggs by about 70%.
* **Build 3 charges poultry at the Table A2.3 "meat" energy (13,000 MJ/t)**; Table A2.3 gives one meat figure and Table A2.4 gives poultry 8,000. The README's assumption line says "by food energy" without saying poultry takes the meat figure. Worth one clause.
* README says the 58.4 kg red meat is from "ABS 4306.0 Table 3"; the same figures are in Table 1 (the brief's source). Not a discrepancy in value.
* The thesis states 6:1 as an energy ratio; a mass reading of 6:1 gives 0.117 with 50 g eggs. The brief's phrase "6:1 feed" is ambiguous; the file uses energy, which follows the thesis.

## Rerun

```
cd /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v22
pdftotext -layout "/home/user/carrying-capacity-models/Comparators/ABS-4306.0-1991-92-Apparent-Consumption-of-Foodstuffs.pdf" abs.txt
python3 -I build.py
python3 -I feedcheck.py
```

## Files read

* /home/user/carrying-capacity-dashboard/qa/briefs/_checker_rules_results_wave.md
* /home/user/carrying-capacity-dashboard/qa/briefs/V22_simpson_third_build_recheck.md
* /home/user/carrying-capacity-models/Literature review/Wackernagel_1994_PhD_thesis_UBC_Ecological_footprint_and_appropriated_carrying_capacity.pdf (PDF pages 289 to 295 and 305 to 308; thesis pp. 279 to 285, 295 to 298)
* /home/user/carrying-capacity-dashboard/analysis/method_tests_2025/wackernagel_1994_food_factors.csv (head only)
* /home/user/carrying-capacity-models/Comparators/ABS-4306.0-1991-92-Apparent-Consumption-of-Foodstuffs.pdf (via pdftotext: Table 1, Table 3 breakfast and nut rows, technical notes on eggs)
* Part C: /home/user/carrying-capacity-dashboard/analysis/method_tests_2025/simpson_food.py, simpson_food.csv, cross_method.csv, cross_method.py (Simpson lines), README.md (Simpson section, lines 36 to 114, and the cross-method table row)
* My code: /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v22/build.py, /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v22/feedcheck.py
