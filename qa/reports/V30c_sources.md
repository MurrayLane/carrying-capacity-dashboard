# V30c: data sources behind the cited claims, group 3 of 3

Blind checker report for brief `qa/briefs/V30c_sources.md`, rules `qa/briefs/_checker_rules_results_wave.md`. Twelve source rows checked: A04, A28, D17, D22, D25, D28, D42, D45, D48, D51, D55, D58. No register was edited; no repository file other than this report was written. Checking code lives in the session scratchpad (`code/`), outside the repository.

## Tolerance (set before comparing)

* Hashes, file names, row counts, item counts, region counts, codes and names: exact.
* A value copied from a source (a cell, a csv field, a FAOSTAT record): equal to the source as stored. Workbook floats within 1e-12 relative; ABS and FAOSTAT values printed to two decimals within 0.006; AUSNUT-derived means within half a unit of the last printed digit of the derived file.
* A value the pipeline computes from the source (a mean, a sum, a unit conversion): within 0.5%, or one unit of the last printed digit where that is tighter.
* Where the pipeline's method differs on purpose from a plain recomputation (allocation of SA2s to zones, excluded territories), the difference is explained, not waived.

## The check can fail: deliberate wrong values

Every comparison script was run a second time with one value altered on the pipeline side. Each run reported exactly the one planted mismatch and nothing else:

| Source | Planted wrong value | Reported |
|---|---|---|
| A28 | `unit_micronutrients.csv`, breads wm, iron 0.01687 raised by half to 0.025305 | 1 mismatch (mine 0.016867 against 0.025305) |
| D42 | `model.json` Base!E175 set to 0.9 (workbook 0.9155) | 1 mismatch of 12,141 cells |
| D42 | `regions.json` region 3 wheat yield set to 150.0 (workbook Yield!J4 160.1309) | 1 mismatch of 8,100 cells |
| D45 | `defaults-short-term.csv` Australia biofuel set to 0.005 (Totals.xls 0.0053) | 1 mismatch of 2,940 values |
| D48 | `cube_2020-21.json` Wheat (ha), Australia, set to 12,643,000 (ABS 12,643,215.65) | 1 mismatch of 316 values |
| D51 | `land_2011_method_zones.csv` Australia cropping set to 316,400.00 (ABS-derived 316,498.98) | MISMATCH line printed |
| D55 | one SA2 of the 650k map moved to region 999 | 54 regions against 53, region 23 reported not contiguous |

The FAOSTAT extracts (D22, D25, D28) were compared row for row, as tuples, with my own re-cut of the bulk files; any single changed character fails that comparison.

One false alarm of my own is worth recording: my first D45 run reported 18 mismatches, all in region 36. My code had mapped region 36 to the last column carrying the number 36, which in Totals.xls is a custom "Noosa Biosphere" column (column 64 of SHORTdefults), not "QLD: South East Qld" (column 38). With the Noosa column excluded, as the pipeline's extractor also does, there are no mismatches.

---

## A04: Henry and Godden 1995 (scan, comparator)

**Identity.** `/home/user/carrying-capacity-models/Comparators/Henry-and-Godden-1995-A-note-on-estimating-Australias-sustainable-population.pdf` exists; sha256 `557dd31291149a0889e98120b00cd1489372b94184dff8534086906c8540bb0e` equals the register. 7 pages, scanned, no text layer (PDF title field "63010103.tif"). Page 1 heading: "A Note on Estimating Australia's Sustainable Population, L.A. Henry and D.P. Godden", printed page number 97; running head on page 2: "Review of Marketing and Agricultural Economics, Vol. 63, No. 1, April 1995". Matches the title, volume, issue and first page in the row.

**Origin.** The row says unknown (no DOI or URL). No host is named, so no network check. The archive `Comparators/README.md` gives the same citation and no URL. Compared with the scan's own running heads only: consistent.

**Values** (read from the page images first, then compared with `analysis/method_tests_2025/henry_godden.py` and `henry_godden_summary.csv`):

| Value | Source (scan) | Pipeline | Result |
|---|---|---|---|
| Energy 1990-91 excl. wool/cotton, 404 x 10^15 J | Table 2, p. 99 | `henry_godden.py` check line `404 * NIX / 45.7 * FE` | equal |
| Protein 1990-91 excl. wool/cotton, 306 x 10^10 g | Table 2, p. 99 | same line, `306 * ...` | equal |
| Intensive land in use 1990-91, 45.7 Mha | Table 3, p. 99 (Contemporary, Total) | `45.7` in check and LAND list | equal |
| Sown pasture 1990-91, 28.3 Mha | Table 3, p. 99 | `28.3 + 31.65` (claim B027) | equal |
| Nix potential intensive land, 70 Mha | p. 98 item (d), p. 99, p. 101 | `NIX = 70.0` | equal |
| Consumption factors 0.1760 (energy), 0.2041 (protein) | Table 4, p. 99 | `FE, FP = 0.1760, 0.2041` (claim B014) | equal |
| Supportable population 109 (energy), 96 (protein) million | Table 5, p. 100, "contemporary excl. wool/cotton" | `published Table 5, 109, 96` (claim B008) | equal |

Recipe check (claim B015): 404 x 70/45.7 x 0.1760 = 108.9 and 306 x 70/45.7 x 0.2041 = 95.7, as in `henry_godden_summary.csv` row 2. The paper's own worked line on p. 99 gives 404 x 70/45.7 = 618.8, which my arithmetic also gives. Claim B025 ratios: 781.6/404 = 1.93 and 655.6/306 = 2.14 (summary TOTAL row), stated as 1.9 and 2.1: consistent.

**Verdict: verified.** Register change: status to verified (V30c); no path, hash or origin change. The note that the row also belongs in the literature register stands.

---

## A28: AUSNUT 2023 food nutrient profiles (FSANZ)

**Identity.** `/home/user/carrying-capacity-models/Foundation diets/AUSNUT2023/AUSNUT 2023 - Food nutrient profiles.xlsx` exists; sha256 `374650afc59951009d5ddf48fe35f712467458eb07eef513ea9f54c8f110f317` equals the register. Sheets "Contents" and "Food nutrient profiles". Contents title: "AUSNUT 2023 - Food nutrient profiles - Content summary". Data sheet A1: "AUSNUT 2023 - Food nutrient profiles (per 100 g)"; header row 3 begins "Survey ID, Public food key, Derivation, Food name, Energy with dietary fibre (kJ) ...", 62 columns. Food rows with a Survey ID: 3,741, all IDs distinct.

**Origin.** The row says unknown. No host is named, so no network check. The file's own Contents sheet links to `https://www.foodstandards.gov.au/sites/default/files/2025-08/AUSNUT%202023%20-%20About%20the%20foods%20and%20nutrients.pdf`, and the folder README in the archive says the files were fetched from `https://www.foodstandards.gov.au/science-data/food-nutrient-databases/ausnut/food-nutrients`. The file's metadata agrees with an FSANZ origin.

**Values.** The pipeline (`analysis/nutrition_lp_2025/match_ausnut.py` writing `unit_micronutrients.csv`) gives each model unit the mean, per gram, of three matched AUSNUT foods. Unit conversion: per 100 g in AUSNUT, divided by 100 for the micronutrient columns; macronutrient columns stay per 100 g. My own code looked up the three named foods in the workbook (by the first 48 characters of the food name, as printed in `matches`) and recomputed the means. 152 of the 178 units resolve to unique food names (the other 26 have truncated names shared by two or more foods and were skipped); 1,976 values compared (10 micronutrients and 3 macronutrients each), 0 mismatches.

Worked example, unit "breads wm" (matches Bread, mixed grain, homemade, row 392; Bread, wholemeal, homemade, row 437; Muffin, English style, wholemeal, commercial, toasted, row 478):

| Column | Workbook cells (rows 392, 437, 478) | Mean / 100 | `unit_micronutrients.csv` |
|---|---|---|---|
| Calcium (S) mg | 28, 20, 181 | 0.76333 | 0.76333 |
| Iron (U) mg | 1.57, 1.86, 1.63 | 0.01687 | 0.01687 |
| Zinc (AA) mg | 1.08, 1.2, 1.13 | 0.01137 | 0.01137 |
| Iodine (T) ug | 4.8, 6, 52.7 | 0.21167 | 0.21167 |
| Magnesium (V) mg | 55, 59, 45 | 0.53 | 0.53 |
| Energy (E) kJ, per 100 g | 1033, 983, 1027 | 1014.33 (no division) | 1014.33 |

Claim A134 (53.6 to 86.9; 85.5 with micronutrients) is an LP output, not a value read from AUSNUT; it was not re-run.

**Verdict: verified with notes.** Register changes: origin from "unknown" to the FSANZ page named in the archive README (`foodstandards.gov.au/science-data/food-nutrient-databases/ausnut/food-nutrients`, fetched 2026-10-30), marked as taken from the README and not re-fetched. Note for the builder (not a register field): the workbook holds 3,741 foods; the archive README and `analysis/nutrition_lp_2025/README.md` say 3,742.

---

## D17: FAOSTAT Food Balances (2010-), bulk normalized csv

**Identity.** No `local_path` (the raw file is not stored in either repository). A copy outside both repositories, `/tmp/claude-0/fao/x/FoodBalanceSheets_E_All_Data_(Normalized).csv`, has sha256 `2834e1012daaebf4e4f8195fa86ce9063d1c81fdd9d7c04cbf0aba758ccfa020`, equal to the register and to `qa/fao_bulk_hashes.csv`; 633,057,019 bytes. Its zip, `/tmp/claude-0/fao/fbs.zip`, has sha256 `26200855ed5d...` equal to the zip hash in `qa/fao_bulk_hashes.csv`; the member is dated 2025-10-14 12:03, matching "file dated 14 Oct 2025". Header: `Area Code,Area Code (M49),Area,Item Code,Item Code (FBS),Item,Element Code,Element,Year Code,Year,Unit,Value,Flag,Note`; first data row Afghanistan, Population, 2010.

**Origin.** One HEAD request to `https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_All_Data_(Normalized).zip` (plain client string, no retry): HTTP 200, `content-length: 54840802`, `last-modified: Tue, 28 Oct 2025`. The byte size equals that of the hash-matched local zip (54,840,802). The URL is the right one for this file.

**Values** (read from the bulk csv with my own code, then compared with `henry_godden_items.csv`; means of 2021, 2022, 2023; edible = production less feed, seed, non-food, losses and, where the script says so, processing; world kcal and protein per kg = world Food supply (kcal) or Protein supply quantity (t) over world Food):

| Item (Australia) | Bulk production 2021 / 2022 / 2023, 1000 t | Mean | Edible | World kcal/kg | World protein g/kg | `henry_godden_items.csv` |
|---|---|---|---|---|---|---|
| Wheat and products (2511) | 31,923 / 36,237 / 41,199 | 36,453 | 30,287 | 2,846 | 91.8 | 36453, 30287, 2846, 91.8 |
| Barley and products (2513) | 14,649 / 14,377 / 13,491 | 14,172 | 9,760 | 2,655 | 80.5 | 14172, 9760, 2655, 80.5 |
| Sorghum and products (2518) | 1,639 / 2,648 / 2,326 | 2,204 | 2,058 | 3,028 | 84.5 | 2204, 2058, 3028, 84.5 |
| Bovine Meat (2731) | 1,894 / 1,878 / 2,236 | 2,003 | 2,003 | 1,587 | 150.3 | 2003, 2003, 1587, 150.3 |
| Rape and Mustardseed (2558) | 4,756 / 6,820 / 8,918 | 6,831 | 5,413 | 2,293 | 109.8 | 6831, 5413, 2293, 109.8 |

Australia population, Total Population - Both sexes (1000 No): 25,956.42 / 26,200.98 / 26,451.12. D58 values traced to this file are listed under D58.

**Verdict: verified with notes** (the file is not stored; identity rests on the hash of a copy held outside the repositories, and the live host still serves a zip of the same size). Register changes: none to origin or hash. Status text could say "hash and content checked on a hash-matched copy (V30c); file not stored".

---

## D22: FAOSTAT food balance extract, Australia and World, 2021-23

**Identity.** `analysis/method_tests_2025/fbs_au_world_2021_23.csv` exists; sha256 `e1ae3196e3d51f7cf3c77e73b7cc5b105eb78e3cf2f24c4e07a1277d2fc6cb21` equals the register. Header `Area,Item,Element,Year,Unit,Value`; 6,603 data rows; 120 items. Matches the row's "6,603 data rows, 120 items".

**Origin.** Re-cut from D17 by my own code (Areas Australia and World, Years 2021 to 2023, the 13 elements listed in the row): 6,603 rows, identical to the extract in content and order (`only mine []`, `only extract []`). So the extract is exactly what the row says it is.

**Values.** Every row (6,603) matches the bulk file. Named examples, bulk record and extract row the same: Australia, Wheat and products, Production, 2021 = 31923 (1000 t); 2022 = 36237; 2023 = 41199; Australia, Population, Total Population - Both sexes, 2021 = 25956.42 (1000 No); World Bovine Meat Food supply (kcal) and Food over 2021-23 giving 1,587 kcal/kg as used by `henry_godden.py`. Pipeline conversion checked: `energy_PJ = edible kt x 1e6 x kcal/kg x 4184 / 1e15` (kcal to J at 4,184 J/kcal); wheat 30,287 x 1e6 x 2,846 x 4,184 / 1e15 = 360.7 PJ, as in the items file.

**Verdict: verified.** Register change: replace the note "No check of the extract against the bulk file was found" with "re-cut from a hash-matched copy of D17 by V30c: identical, 6,603 rows"; status to verified.

---

## D25: FAOSTAT land use extract for the HALF test

**Identity.** `analysis/method_tests_2025/half_landuse.csv` exists; sha256 `051423c6888dabc355f4ba5b00ceab6e9da01d649032fbca1552a09cc8fea636` equals the register. 174 data rows, 26 items, element Area, unit 1000 ha. Matches the row.

**Origin.** The bulk land use file (D19) copy `/tmp/claude-0/fao/l/Inputs_LandUse_E_All_Data_(Normalized).csv` has sha256 `cd8c9ab6fd02...` equal to the csv hash in `qa/fao_bulk_hashes.csv`; header `Area Code,Area Code (M49),Area,Item Code,Item,Element Code,Element,Year Code,Year,Unit,Value,Flag,Note`. My re-cut (World and Australia; 2011, 2021, 2022, 2023; Element Area) gives 174 rows identical to the extract. No network request was made for D19 (it is not one of my twelve rows).

**Values** (bulk record = extract row; `half_index.py` multiplies by 1000 to hectares):

| Record | Bulk | Extract |
|---|---|---|
| World, Land area (6601), 2011 | 13,017,353.8 | 13017353.800000 |
| World, Cropland (6620), 2011 | 1,535,138.5 | 1535138.500000 |
| World, Permanent meadows and pastures (6655), 2011 | 3,182,078.85 | 3182078.850000 |
| World, Agricultural land (6610), 2011 | 4,717,479.45 | identical (row-level comparison) |
| Australia, Cropland, 2022 | 31,650 | 31650.000000 |

**Verdict: verified.** Register change: status to verified; note that D19 was hash-matched and the extract re-cut identically.

---

## D28: FAOSTAT crops extract for the people-per-hectare test

**Identity.** `analysis/method_tests_2025/fao_qcl_countries.csv` exists; sha256 `97d6c073b4106eca66e2162e98843d8658ed0f271f583ace131b05ee09d5f665` equals the register. 7,444 data rows, 279 items. Matches the row.

**Origin.** The QCL bulk copy (D18) `/tmp/claude-0/fao/q/Production_Crops_Livestock_E_All_Data_(Normalized).csv` has sha256 `c4ff713e4b8e...` equal to `qa/fao_bulk_hashes.csv`. My re-cut (six areas; 2011, 2021, 2022, 2023; Area harvested and Production) gives 7,444 rows identical to the extract.

**Values** (bulk = extract; units ha and t as in the file, no conversion in the extract):

| Record | Bulk |
|---|---|
| World, Wheat (15), Area harvested, 2011 | 220,839,223 ha |
| World, Maize (corn) (56), Area harvested, 2011 | 172,620,259 ha |
| World, Rice (27), Area harvested, 2011 | 162,665,998 ha |
| World, Soya beans (236), Area harvested, 2011 | 103,792,075 ha |
| Australia, Wheat, Area harvested, 2022 | 12,925,286 ha |
| Australia, Wheat, Production, 2022 | 41,199,486 t |

The cropland total in `cassidy.csv` (1,061.4 Mha for World 2011) sums many items and was not re-derived.

**Verdict: verified.** Register change: status to verified; note the identical re-cut.

---

## D42: model workbook `model/model.xls`

**Identity.** `model/model.xls` exists; sha256 `f14140154e55754713a7d5c60643f1abab8b5a8c8c9891b9a0e0cf85286ff5bd` equals the register and the `inputs` entry in `releases/2011/release.json`. Sheets: Settings (163 x 61), Base (348 x 44), Yield (138 x 67), Recycle (9 x 12), Diet (23 x 97), resilience (10 x 152), log (11 x 3). OLE metadata: last saved 2012-10-17 23:47:31, created 2011-02-22, matching "the model saved 2012-10-17". The two archive relatives named in the notes hash as stated: `Models/Carrying capacity dashboard model 021012.xls` `dc4336477f53...`, `Models/Lane_Dashboard_model.xls` `b81caa6126bb...`.

**Origin.** "QUT repository snapshot, commit 04a612e" cannot be checked here (the brief forbids git). Compared against the file's own metadata only: consistent.

**Values.** Read with xlrd, my own code, then compared with what the pipeline takes into release 2011 (`web/public/data/2011/model.json`, no cell overrides, and `web/public/data/2011/regions.json`):
* every constant (non-formula) cell of the six model sheets: 12,141 cells, 0 mismatches;
* the regional yield block Yield!H:BO (one column per region, region number in row 2) against the `yield` vectors of all 60 regions in `regions.json`: 8,100 cells, 0 mismatches.

Named cells:

| Cell | Workbook | Pipeline |
|---|---|---|
| Base!D175 / E175 | "beef (dressed)" / 0.9155 | model.json Base 174:4 = 0.9155 |
| Base!K175 | 1.0 | model.json Base 174:10 = 1 |
| Base!V175:V178 (red meat split) | 0.69225, 0.17891, 0.01993, 0.10891 | `data/2025/red_meat_mix.json` shares_2011 (equal to 1e-9) |
| Yield!J4 (wheat, region 3) | 160.130889853738 | regions.json region 3 yield[0] = 160.130889853738 |
| Yield!G4 (wheat organic factor) | 0.6944081480707129 | `data/2025/organic_factors.json` Wheat factor_2011 |
| Settings!BQ4:BQ7 (claims A342, B252) | Settings has 61 columns (A to BI), so BQ does not exist | consistent with "the model has no Settings!BQ4:BQ7 cells" |

Formulas were not compared (xlrd does not expose them for .xls); the pipeline's formula translation is outside this source check.

**Verdict: verified with notes** (origin commit not checkable without git). Register change: status to verified (V30c); no other change.

---

## D45: `data/2011-thesis`

**Identity.** Folder holds `defaults-long-term.csv`, `defaults-short-term.csv`, `timber-yield-by-region.csv` (61 lines each). Listing hash (sha256 of the sha256sum listing, files bytewise-sorted) `126dd3d11edfc1b6749d2a2c8f8c8842aadf703c26b67ade3533745d19e7e076` equals the register.

**Origin.** Source workbooks read first: `/home/user/carrying-capacity-models/Results/Totals.xls` (sheets SHORTmaps, SHORTtotals, SHORTdefults, LONGmaps, LONGtotals, LONGdefults, ...; SHORTdefults A1 "BAU", LONGdefults A1 "Post-fossil fuels") and `Results/21b.xls` (sheets Defaults, Settings, Base, Yield, ...; Yield!A138 "timber (m3/ha)"). The extractor `analysis/model_archive/extract_thesis_release.mjs` names both. Consistent.

**Values.** My code compared all 24 input rows of SHORTdefults and LONGdefults (rows 3 to 26) for the 60 zones with the two defaults files, and 21b.xls Yield row 138 (columns H to BO by region number) with the timber file: 2,940 values, 0 mismatches. Named values:

| Value | Source cell | data/2011-thesis |
|---|---|---|
| Short-term timber, Australia | Totals.xls SHORTdefults C22 = 0.5 | short `timber` 0.5 |
| Short-term biofuel, Australia | SHORTdefults C18 = 0.0053 | short `biofuel` 0.0053 |
| Long-term fuel, Australia | LONGdefults C17 = 253 | long `fuel` 253 |
| Short-term reserve share, Australia | SHORTdefults C24 = 0.2355758786842247 | `nature2` same |
| Timber yield, region 1 | 21b.xls Yield!H138 = 0.0004685323101369817 | `timberYieldPerM2` same |
| Thesis national capacity, long term (claim B160) | Totals.xls LONGtotals C36 = 9,431,486.59 | `results/2011-thesis.csv` zone 1 long 9,431,487 (9.4 million) |

Notes: Totals.xls has an extra column "Noosa Biosphere" that reuses region number 36; the extractor skips it, correctly. The extractor reads the SHORTtotals and LONGtotals sheets; my comparison used the SHORTdefults and LONGdefults sheets of the same workbook, so the two sheets agree for these rows. The workbook labels row 138 "m3/ha" while the file calls the value per m2; the numbers are identical (no conversion), so only the label differs. The value (about 0.00047) reads as m3 per m2 (4.7 m3/ha), which suggests the workbook label, not the file name, is wrong; not tested further.

**Verdict: verified with notes.** Register change: status to verified; origin could name the sheets read (SHORTtotals/LONGtotals rows 3 to 31 of Totals.xls; Yield!H138:BO138 of 21b.xls) and the Noosa column exclusion.

---

## D48: `data/abs-2016-21` (ABS NRM cubes, mapped)

**Identity.** Folder holds `cube_2016-17.json` to `cube_2020-21.json` and `regions.json`; listing hash `44284458791cdef21eeee32c22779ecf292f88b12fab0927690489db06a41465` equals the register. `regions.json` has 64 regions (nation, states, NRM regions; code 0 Australia).

**Origin.** The 2020-21 raw cube (D13) is not stored. I fetched `https://www.abs.gov.au/statistics/industry/agriculture/agricultural-commodities-australia/2020-21/AGCDCNRM202021.xlsx` once (one HEAD, then one GET, plain client string): HTTP 200, last-modified 1 Aug 2022, 479,046 bytes, sha256 `04408ebe58ed3b513c71840a877764c2a83fdb449d38e59be9d559e8470b083d`, equal to the D13 row. Contents sheet: "AGCDCNRM202021 Agricultural Commodities, Australia-2020-21; Agricultural commodity estimates by Natural Resource Management (NRM) regions (2016 edition); Released ... 26 July 2022". Table 1 header: `Region code, Region label, Commodity code, Commodity description, Estimate, Number of agricultural businesses`. Origin confirmed for 2020-21.

For 2016-17 to 2019-20 the raw csv cubes are not stored and have no registered hash. Copies outside the repository (a fetch made by an earlier session, `scratchpad/abs/current/<year>_NRM.csv`) were used as a supplementary check; their title lines read "AGRICULTURAL COMMODITIES-Australia, States and Territories and NRM regions-2016-17" and so on. Their sha256: 2016-17 `49e127dcade2...`, 2017-18 `dc5e4ba85e40...`, 2018-19 `1bc6ee4ec976...`, 2019-20 `3e62902f3278...`. Their provenance rests on that session's fetch, not on a registered hash.

**Values.**

| Check | Compared | Mismatches |
|---|---|---|
| 2020-21 Wheat, Barley, Canola area (ha) and production (t), every region, against D13 | 316 | 0 |
| 2020-21 Broccoli (t) from ABS kg x 0.001 | 49 | 0 |
| 2020-21 Mushrooms (ha) from ABS m2 x 0.0001 | 34 | 0 |
| 2020-21 Apples (t) and Almonds (t), ABS code in t from 2019-20 (factor 1) | 69 | 0 |
| 2016-17 to 2019-20 Wheat and Barley area and production, every region, against the scratch csv copies | 814 | 0 |

Named values: Wheat (ha), Australia, 2020-21: ABS AGCEREAL_AHAWHT_F 12,643,215.65 = cube 12,643,215.65. Wheat (t), Australia: 2016-17 31,818,743.54; 2017-18 20,941,134.0; 2018-19 17,597,560.79; 2019-20 14,480,217.44 (source = cube each year). Broccoli, Australia 2020-21: 72,912,318.55 kg x 0.001 = 72,912.32 t = cube. Mushrooms, Australia: 1,231,034.61 m2 x 0.0001 = 123.10 ha = cube. Apples (t), Australia: AGFRUTAPPLATO_F 284,896.51 = cube.

**Verdict: verified with notes** (2020-21 against a live, hash-matched source; earlier years against unregistered copies). Register changes: add the four raw csv cubes (2016-17 to 2019-20) as source rows with their hashes, or store them, so the earlier years have a registered source; status to verified for 2020-21.

---

## D51: `data/nrm2011`

**Identity.** Folder holds `land_2011_method_zones.csv`, `land_use_by_nrm2011.csv`, `land_use_by_sa2_nrm2011_piece.csv`; listing hash `edd40dadb278363e2b912640ba114a76e7a45da9865a0d3fb11f8dc01a5c24a9` equals the register. Header of the zone file: `zone,name,cropping,pasture,nonAgricultural,infrastructure,reserve,total,population,old_cropping,...,old_population`.

**Origin.** The CLUM raster (D32) is not stored, so the km2-by-class figures cannot be traced to their raster. The ABS input (D14, `AGCDCASGS202021.xlsx`) is available as a copy outside the repository whose sha256 `0fdbd3e398b5...` equals the D14 row; Table 1 title "AGRICULTURAL COMMODITIES-Australia, states and territories and ASGS regions-2020-21". D31 is `data/sa2/population_erp.csv`, sha256 `71f24cf1584d...`, equal to the D31 row.

**Values.**

| Value | Source | data/nrm2011 | Result |
|---|---|---|---|
| Australia cropping | D14 AGPROD_AHACRP_F 31,649,898.02 ha / 100 = 316,498.98 km2 | 316498.98 | equal |
| Australia pasture | D14 AGLANDGRAZEHA_F / 100 = 3,318,688.84 km2 | 3318688.84 | equal |
| Australia infrastructure | population 27,608,199.78 x 730 m2 / 1e6 = 20,153.99 km2 | 20153.99 | equal |
| Australia non-agricultural | total - (cropping + pasture + infrastructure + reserve) = 2,063,387.27 | 2063387.27 | equal |
| Australia population | sum of D31 column 2025 over all SA2 = 27,613,654 | 27,608,199.78 | explained, see below |
| NSW-ACT cropping | (D14 NSW + ACT) / 100 = 95,079.62 | 95079.06 | within tolerance (0.0006%), see below |
| `old_*` columns, 7 columns x 60 zones | `data/2011/default-inputs-short-term.csv` | equal | 420 values, 0 mismatches |

Population: the 5,454 people not in the Australia total are the SA2s outside the 2011 zones: Lord Howe Island (108031161, 442), Christmas Island, Cocos (Keeling) Islands, Norfolk Island (901011001, 901021002, 901041004: 1,889 + 626 + 2,193) and Jervis Bay (901031003, 305), 5,455 in all; the rest is rounding of apportioned SA2 parts. This matches the exclusion stated in `pipeline/land/land_2011_method.py`. NSW-ACT: the zones are built from SA2 parts, and an SA2 that straddles a zone boundary shares its cropping by its cropping land; a plain state sum differs by 0.56 km2. Not an error.

**Verdict: verified with notes** (the CLUM raster part is not checkable from stored files). Register change: note that D32 is not stored, so the class areas in `land_use_by_nrm2011.csv` rest on the zonal script alone; status to verified for the ABS and ERP parts.

---

## D55: `data/regions` (model output)

**Identity.** Folder holds `ideal_2025-fixed_short_K53_cap650k.csv` and `ideal_2025-fixed_short_K53_cap1300k.csv` (header `sa2_code,region`, 2,450 rows each); listing hash `addefa2631b7c7a1f5c5fcea7fff242e821e6ad0ce946059ff98c546d7cf660b` equals the register.

**Origin.** Output of `analysis/regionalise_2025/regionalise.mjs`; no external source. Its inputs are `data/sa2/land_2011_method_by_sa2.csv`, `data/sa2/population_erp.csv` (2025) and `data/sa2/adjacency.csv`.

**Values** (my code, recomputed from the maps and those inputs, against `analysis/regionalise_2025/summary.csv` rows release 2025-fixed, short, K 53):

| Check | cap 650k | cap 1300k |
|---|---|---|
| SA2 rows / distinct / missing / extra against the land file (2,450) | 2,450 / 2,450 / 0 / 0 | 2,450 / 2,450 / 0 / 0 |
| Regions (summary 53) | 53 | 53 |
| Largest region, km2 (summary 649,002 / 1,299,059; cap 650,000 / 1,300,000) | 649,002 | 1,299,059 |
| Smallest region, km2 (summary 9) | 9 | 9 |
| Largest population (summary 7,501,035 / 6,650,306) | 7,501,035 | 6,650,306 |
| Smallest population (summary 5) | 5 | 5 |
| Regions not contiguous on the SA2 adjacency | none | none |

The capacity shares in claim A124 (0.757 short, 0.694 long) need the model evaluator and were not re-run. The long-term figure 0.694 comes from a long-term map (summary row long, K 53, 650,000) that is not stored in `data/regions`: only short-term maps are there.

**Verdict: verified** (structure and summary figures). Register change: none to path or hash; the notes could say that the long-term K=53 map behind claim A124's 69.4% is not in the folder.

---

## D58: `data/2025` consumption_proxies.json, red_meat_mix.json, organic_factors.json

**Identity.** The three files exist; listing hash `043bab33e32307ce26c8f321b4651c82f2acb220c4223f2edda026f8fa4adb2e` equals the register.

**Origin.** Read the sources first: D17 (hash-matched bulk FBS, above), `model/model.xls` (D42) and the archive workbook A21 `/home/user/carrying-capacity-models/Organic/Organic comparisons for paper.xls` (sha256 `b2467fc0311d...`, equal to the A21 row; sheet yield-final, A1 "Percentage difference between organic and conventional agricultural yield", row 2 "No." of studies). The register names FAOSTAT D20 (Oceania regional file) for the meat series; the values match the global bulk file D17 exactly. D35 (petroleum statistics), D21 (forestry) and the Organic Market Report figure (44.4 Mha) are not stored and were not checked.

**Values.**

| Value | Source | Pipeline | Result |
|---|---|---|---|
| Beef and veal kg/person, mean 2010-12 | D17 Australia, Bovine Meat, Food supply quantity (kg/capita/yr) | red_meat_mix 39.11 | equal |
| Beef and veal, mean 2021-23 | same | 25.8833 | equal |
| Mutton and goat, mean 2010-12 | D17 Mutton & Goat Meat | 9.7667 | equal |
| Pork, mean 2021-23 | D17 Pigmeat | 25.8233 | equal |
| Poultry, mean 2010-12 | D17 Poultry Meat | consumption_proxies base poultry_kg 46.9567 | equal |
| Meat, mean 2021-23 | D17 Meat | latest meat_kg 112.8 | equal |
| Red meat shares 2011, rows 175 to 178 | model.xls Base!V175:V178 | shares_2011 | equal (4 values) |
| Organic factor 2011, Wheat, Oats, Barley, Maize, Soybeans | model.xls Yield!G4, G5, G6, G8, G19 | factor_2011 | equal (5 values) |
| Same five factors | A21 yield-final, mean of the non-zero study ratios / 100 (19, 7, 8, 12, 8 studies) | 0.694408, 0.712354, 0.578086, 0.824451, 0.883719 | equal |
| Organic factor 2025 = mean of 2011 factor and Kniss 2016 ratio | arithmetic | 0.6772, 0.7562, 0.669, 0.7372, 0.7819 | equal |

Unit note: FAOSTAT gives kg per person per year; the JSON keeps that unit; A21 gives percent, the pipeline divides by 100. The FBS "Grand Total" item has no food quantity element in this series, so `total_food_kg` (884.08 and 894.9) was not checked.

**Verdict: verified with notes** (FAO meat series, red meat shares and organic factors checked; fuel, biofuel, timber and organic land not checkable from stored files). Register changes: origin to name D17 (the values match the global bulk file; whether D20 gives the same was not tested) and D42 (organic_factors.py reads Yield!G of model.xls; A21 reproduces those values); keep the note that the 44.4 Mha figure has no stored source, and add that D35 and D21 are not stored.

---

## Found outside the brief

* FAOSTAT food balance years for Australian crops are shifted against the crops file: FBS "Wheat and products" Production 2023 is 41,199 (1000 t) and QCL "Wheat" Production 2022 is 41,199,486 t. The FBS appears to book the Australian split-year harvest one year on. `henry_godden.py` averages 2021-23 FBS values; the method tests that set FBS against QCL years may compare different harvests. Not tested further.
* AUSNUT food count: 3,741 in the workbook, 3,742 in two READMEs (above).

## Summary

| Source | Verdict | Values checked | Mismatches |
|---|---|---|---|
| A04 | verified | 9 printed values + 2 recipe checks | 0 |
| A28 | verified with notes | 1,976 (152 units x 13) | 0 |
| D17 | verified with notes | 23 named + whole-file re-cut of D22 | 0 |
| D22 | verified | 6,603 rows (whole extract) | 0 |
| D25 | verified | 174 rows (whole extract) | 0 |
| D28 | verified | 7,444 rows (whole extract) | 0 |
| D42 | verified with notes | 12,141 constant cells + 8,100 yield cells + 6 named | 0 |
| D45 | verified with notes | 2,940 + 2 capacities | 0 |
| D48 | verified with notes | 1,282 (468 for 2020-21, 814 for 2016-17 to 2019-20) | 0 |
| D51 | verified with notes | 426 (6 direct + 420 old-value cells) | 0 (2 differences explained by method) |
| D55 | verified | 16 structural and summary figures | 0 |
| D58 | verified with notes | 25 | 0 |

No value mismatch was found in any of the twelve sources. Register rows touched: none. Ids checked: A04, A28, D17, D22, D25, D28, D42, D45, D48, D51, D55, D58.

## Network requests (one at a time, client string `curl/8`, no retries)

1. HEAD `https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_All_Data_(Normalized).zip`: 200.
2. HEAD `https://www.abs.gov.au/statistics/industry/agriculture/agricultural-commodities-australia/2020-21/AGCDCNRM202021.xlsx`: 200.
3. GET of the same ABS file: 479,046 bytes, hash equal to D13.

## Rerun

From `/home/user/carrying-capacity-dashboard`, with `S` the session scratchpad and the FAOSTAT copies under `/tmp/claude-0/fao/`:

```
python3 -I $S/code/recut.py "/tmp/claude-0/fao/x/FoodBalanceSheets_E_All_Data_(Normalized).csv" "/tmp/claude-0/fao/q/Production_Crops_Livestock_E_All_Data_(Normalized).csv" "/tmp/claude-0/fao/l/Inputs_LandUse_E_All_Data_(Normalized).csv" .
python3 -I $S/code/fao_values.py <same three files>
python3 -I $S/code/ausnut_check.py "<AUSNUT profiles xlsx>" analysis/nutrition_lp_2025/unit_micronutrients.csv [poison]
python3 -I $S/code/wb_check.py [poison];  python3 -I $S/code/wb_yield.py [poison]
python3 -I $S/code/thesis_check.py [poison]
python3 -I $S/code/abs_check.py $S/abs/AGCDCNRM202021.xlsx data/abs-2016-21 [poison]
python3 -I $S/code/abs_csv_check.py $S/abs/current data/abs-2016-21
python3 -I $S/code/nrm_check.py $S/abs/rd/AGCDCASGS202021.xlsx . [poison]
python3 -I $S/code/regions_check.py . [poison]
python3 -I $S/code/d58_check.py "/tmp/claude-0/fao/x/FoodBalanceSheets_E_All_Data_(Normalized).csv" .
```

Folder hashes: `find <dir> -type f | LC_ALL=C sort | xargs sha256sum | sha256sum`.
