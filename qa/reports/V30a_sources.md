# V30a: data sources behind the cited claims, group 1 of 3

Blind check of 12 rows of `qa/sources_register.csv` (decision 74), by brief `qa/briefs/V30a_sources.md` under `qa/briefs/_checker_rules_results_wave.md`. Checked 2026-11-13. Work files and code are in the session scratch folder (`v30a_chk/`); nothing in the repository was edited except this report. No register row was touched.

## Tolerance (set before comparing)

* File identity: sha256 must match the register exactly (64 hex digits). Multi-file rows: sha256 of the `sha256sum` listing as the register's notes define it (repo-relative paths in local_path order; folders: all files, bytewise sorted).
* Raw data values (FAOSTAT records, ABS cube cells, ERP counts, workbook cells, thesis table entries, scan values typed into scripts): equal to the printed precision (relative 1e-9 for machine values; one unit of the last printed digit where the source prints fewer digits than the file holds).
* Counts and names: exact.
* Capacities and derived yields recomputed through a conversion: within 0.5%.
* Ratios and shares: within one unit of the last printed digit.

## Deliberate wrong values (the check can fail)

`check_values.py --wrong` adds three wrong source values; all three are reported `FAIL`, the 101 real comparisons are `ok`:

```
FAIL TEST | deliberate wrong: beef 37.5 against 37.4 | ... | exact
FAIL TEST | deliberate wrong: Table 16 Australia short 41,000,000 | pipeline 4.04392e+07 | cap
FAIL TEST | deliberate wrong: Victoria 150-yr 0.1543 | pipeline 0.15334 | digit0.0000005
total 104 mismatches 3
```

The bulk-file comparator was tested the same way: a copy of `fao_world_land_production.csv` with World wheat area 1991 changed by 1 ha (222,929,759 to 222,929,760) gives `match 2693 ... differ 1`, naming that row. A first run of the comparator also showed it reports real differences: keyed without the unit it flagged the egg rows (FAOSTAT carries egg Production twice, in t and in 1000 No); keyed with the unit, all rows match.

## Network

One request per host and file, client string curl's default, no retry.

| Host | Request | Result |
|---|---|---|
| eprints.qut.edu.au | the thesis PDF (D15 origin) | 200, 6,142,552 bytes, sha256 equal to the register |
| bulks-faostat.fao.org | Production_Crops_Livestock_E_All_Data_(Normalized).zip (D18) | 200; zip and csv sha256 equal to `qa/fao_bulk_hashes.csv` and to D18 |
| bulks-faostat.fao.org | FoodBalanceSheets_E_All_Data_(Normalized).zip (D17, behind D23) | 200; zip and csv sha256 equal to `qa/fao_bulk_hashes.csv` |
| bulks-faostat.fao.org | Inputs_LandUse_E_All_Data_(Normalized).zip (D19, behind D26) | 200; zip sha256 equal to `qa/fao_bulk_hashes.csv` |
| api.data.abs.gov.au | ABS_ANNUAL_ERP_ASGS2021, 2011 to 2025 (D31) | refused: proxy reports the host unreachable (CONNECT 502). Not retried. |
| www.abs.gov.au | Regional population 2024-25 release page (D31) | 200 |
| www.abs.gov.au | Australian Agriculture: Broadacre Crops 2024-25 release page (D49) | 200 |
| www.abs.gov.au | 4306.0 past-issues catalogue page (A01) | 200 |

---

## A01: ABS 4306.0 Apparent Consumption of Foodstuffs and Nutrients, Australia, 1991-92 (scan)

* **Identity.** `/home/user/carrying-capacity-models/Comparators/ABS-4306.0-1991-92-Apparent-Consumption-of-Foodstuffs.pdf` exists, 15,077,939 bytes, sha256 `4bc9ecfc...cbb1c` equal to the register. 31 pages, Canon scan (Acrobat Paper Capture). Title page OCR: "ABS Catalogue No. 4306.0 / EMBARGOED UNTIL 11.30 A.M. 21 JUNE 1994 / APPARENT CONSUMPTION OF FOODSTUFFS AND NUTRIENTS, AUSTRALIA 1991-92 / IAN CASTLES Australian Statistician". Page 5 header: "TABLE 1. APPARENT PER CAPITA CONSUMPTION OF SELECTED FOODSTUFFS, AUSTRALIA, 1938-39 to 1991-92 (kg per year, except where otherwise stated)". The OCR digits of Table 1 page 5 were confirmed against the page image (rendered at 110 dpi).
* **Origin.** The register has no URL. The ABS catalogue page for 4306.0 (www.abs.gov.au) lists "Apparent Consumption of Foodstuffs and Nutrients, Australia 1991-92" with release date 21/06/1994, the date on the scan. Identity of the issue confirmed; the scan itself cannot be compared byte for byte with an ABS file.
* **Values** (source: 1991-92 column; pipeline: literals in `analysis/method_tests_2025/simpson_food.py`, `C91`, `ABS3`, `POP`, `ASSUMPTIONS`):

| Value | Source (page, row) | Pipeline | Conversion | Result |
|---|---|---|---|---|
| Beef and veal 37.4 kg | Table 1 p.5 | C91 beef 37.4 | none | ok |
| Lamb 13.4 + mutton 7.6 kg | Table 1 p.5 | C91 sheep 13.4 + 7.6 | sum 21.0 | ok |
| Pigmeat 19.3 kg | Table 1 p.5 | C91 pork 19.3 | none | ok |
| Poultry 25.9 kg | Table 1 p.5 | C91 poultry 25.9 | none | ok |
| Dairy, milk solids 23.3 kg | Table 1 p.5 | C91 milk 23.3 / 0.125 | to whole milk at 12.5% solids: 186.4 kg | ok (arithmetic) |
| Grain products total 89.2 kg | Table 1 p.6 | C91 cereals 89.2 | none | ok |
| Vegetables total 153.2, potatoes 66.6 kg | Table 1 p.5 | C91 veg 153.2 - 66.6, potatoes 66.6 | 86.6 kg | ok |
| Fruit total 120.1 kg | Table 1 p.5 | C91 fruit 120.1 | none | ok |
| Sugar total 45.6 kg | Table 1 p.6 | C91 sugar 45.6 | none | ok |
| Oils and fats total 19.6, butter 2.6 kg | Table 1 p.6 | C91 oil 19.6 - 2.6 | 17.0 kg | ok |
| Peanuts 2.2, tree nuts 4.3 kg | Table 1 p.6 | C91 nuts 2.2 + 4.3, ABS3 | 6.5 kg | ok |
| Eggs 12.4 kg (1978-79 column; 1988-89 and 1991-92 print "n.c.") | Table 1 p.6 | ASSUMPTIONS eggs 12.4 | carried forward | ok, as the register says |
| Oatmeal and rolled oats 1.5 kg; other breakfast foods 10.4 kg | Table 3 p.11 | ABS3 1.5, 10.4 | none | ok (10.4 reads "lOA" in OCR; 1.5 + 10.4 = 11.9 = Table 1 breakfast foods) |
| Mean population 1991-92 17,390,836; 1990-91 17,176,910 | Technical notes para. 2 | POP | none | ok |

* **Verdict: verified with notes.** Notes: origin has no URL (catalogue entry confirmed); copyright ABS, scan not for the public repository. Recommended status text: "verified (V30a): sha256, title, Table 1 and Table 3 values used by simpson_food.py; origin: ABS catalogue 4306.0, issue 1991-92, released 21/06/1994".

## A19: prelim models/resilience 150 years.xls

* **Identity.** `/home/user/carrying-capacity-models/prelim models/resilience 150 years.xls` exists, 608,768 bytes, sha256 `85e9f42a...e8e31` equal to the register. Sheets: years, commodities, Aust replic only, wheat, oats, barley, Sheet1, Beef, Dairy, Sheep, Pigs, Wheat1, Oat1, Barley1. Sheet `years` A1:B1 "% of average 1" / "prob years of ..."; row 2 return periods 150, 50, 30, 20, 10, 5, 3, 1; rows 3 to 9 Australia and six states. Sheet `commodities` A1 "71240DO001_200..." (ABS 7124.0 historical series), row 3 years 1861 onward.
* **Origin.** Author workbook; no network check possible. Content agrees with the title (thesis resilience table method, anchors 1 to 150 years).
* **Values** (source: `years` sheet; pipeline: `analysis/resilience_2025/tables.csv`, method "thesis (archive data)"; 56 anchor cells compared, 0 differ; 16 listed in the script output):

| Value | Source cell | Pipeline | Result |
|---|---|---|---|
| Australia 150 yr 0.359290 | years!B3 | tables.csv col 150 0.35929 | ok |
| Australia 50 yr 0.552352 | years!C3 | col 50 0.552352 | ok |
| Australia 10 yr 0.741102 | years!F3 | col 10 0.741102 | ok |
| Victoria 150 yr 0.153340 | years!B5 | 0.15334 | ok |
| South Australia 50 yr 0.439559 | years!C7 | 0.439559 | ok |
| Western Australia 50 yr 0.688860 | years!C8 | 0.68886 | ok |
| 100 yr = midpoint of 50 and 150: Australia 0.455821, NSW 0.300307, Vic 0.217587, Qld 0.346997, SA 0.358753, WA 0.491409, Tas 0.669346 | years!B,C | col 100, identical | ok |

`analysis/resilience_2025/replication.txt` reports the archive ratios reproduced to 4.4e-16; consistent with the above.

* **Finding on a claim (not on the source).** Claim A321 cites release `2025-resilience` but its values (SA 0.36, WA 0.49, Tas 0.67) are the thesis archive table. The 2025-resilience table (tables.csv "data: ABS to 2024-25", which `make_release.py` writes into that release) gives SA 0.353, WA 0.471, Tas 0.665 at 100 years, so SA and WA round differently (0.35 and 0.47). Australia, NSW, Vic and Qld are the same in both tables. The claim's release label or its SA and WA values need correcting; the comparison it states (Australia milder than NSW, Vic, Qld, SA; not milder than WA, Tas) holds on both tables.
* **Verdict: verified.** Recommended status text: "verified (V30a): sha256; sheet years reproduced in tables.csv (56 cells)". The register note "contents not re-checked here" can be dropped.

## D15: Lane, PhD thesis, QUT eprint 67485

* **Identity.** `/home/user/carrying-capacity-models/Papers and manuscripts/Lane-2014-PhD-thesis-QUT-eprint-67485.pdf` exists, 6,142,552 bytes, sha256 `f19e1380...a1ef` equal to the register. PDF metadata title "The development of an interactive resource-based carrying capacity assessment model for societal planning"; page 1 "The development of a carrying capacity assessment model for the Australian socio-environmental context ... Queensland University of Technology ... February 2014".
* **Origin.** Fetched once from https://eprints.qut.edu.au/67485/1/Murray_Lane_Thesis.pdf: 200, same size, same sha256. Origin confirmed.
* **Values** (source: Table 16 p.280 and Table 7 p.216; pipeline: `results/2011-thesis.csv` and `data/2011/default-inputs-*.csv`):

| Value | Source | Pipeline | Result |
|---|---|---|---|
| Australia short 40,439,187 | Table 16 | results/2011-thesis.csv zone 1 short, and my re-evaluation of the build | ok, exact |
| Australia long 9,431,487 | Table 16 | zone 1 long | ok, exact |
| NSW-ACT short 10,033,151; VIC long 539,589; WA short 3,696,938; WA long 2,105,909; NT short 33,274 | Table 16 | zones 2, 15, 49, 60 | ok, exact (all 16 large-scale state figures equal) |
| Aggregated small-scale 22,945,793 short, 3,793,418 long | Table 16 | sum of region rows plus NT: 22,945,795 and 3,793,419 | ok (2 and 1 people: rounding of region figures) |
| Australia cropping 305,997, pasture 3,639,794, reserve 1,811,007, total 7,687,574 km2, population 22,326,388 | Table 7 | data/2011 short and long row 1 | ok, exact |

Known, recorded difference (not new): long-term textiles 11.5 kg in Table 7 against 12.5 in `data/2011/default-inputs-long-term.csv` (ERRATA.md error 4, corrected in release 2011-corrected); long-term meat-eggs 7 in Table 7, 7.5 in the file and the thesis text (rounding, ERRATA.md).

* **Verdict: verified.** Recommended status text: "verified (V30a): sha256 equal to the file at the eprint URL (fetched 2026-11-13); Table 16 and Table 7 values match results/2011-thesis.csv and data/2011".

## D18: FAOSTAT Crops and livestock products, all data, normalized

* **Identity.** No local_path (raw file not in either repository). Downloaded once from the expected origin; zip sha256 `c5835418...6d6853`, csv `Production_Crops_Livestock_E_All_Data_(Normalized).csv` 545,005,770 bytes, sha256 `c4ff713e...cbac01`, equal to the register and to `qa/fao_bulk_hashes.csv`. Zip entries dated 2025-12-23, as the register says. Header: `Area Code,Area Code (M49),Area,Item Code,Item Code (CPC),Item,Element Code,Element,Year Code,Year,Unit,Value,Flag,Note`. The file is Latin-1 encoded ("Maté leaves").
* **Origin.** https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_All_Data_(Normalized).zip served this exact file. The register's "expected" URL is the right one.
* **Values.** Every QCL row of three extracts compared with the bulk file, keyed by area, item, element, year and unit: `fao_world_land_production.csv` 2,694 of 2,694 rows equal; `fao_qcl_countries.csv` 7,444 of 7,444; `half_qcl_world.csv` 1,800 of 1,800. Five named:

| Value | Bulk record | Extract | Result |
|---|---|---|---|
| World wheat area harvested 1991 222,929,759 ha | World/Wheat/5312/1991 | same | ok |
| World cereals, primary production 2022 3,054,490,734.77 t | World/1717/5510/2022 | same | ok |
| World potatoes production 1991 256,993,287.92 t | World/116/5510/1991 | same | ok |
| World fruit primary area 2022 67,401,625 ha | World/1738/5312/2022 | same | ok |
| World roots and tubers production 2022 914,419,485.91 t | World/1720/5510/2022 | same | ok |

* **Verdict: verified.** Recommended register changes: status "verified (V30a): fetched from the origin 2026-11-13, zip and csv sha256 equal; all QCL rows of D26, fao_qcl_countries.csv and half_qcl_world.csv reproduce"; origin: replace "expected" with the URL as confirmed. local_path stays empty (file not stored).

## D23: half_fbs_countries.csv (FAOSTAT food balance extract)

* **Identity.** `analysis/method_tests_2025/half_fbs_countries.csv` exists, sha256 `99420962...e66b` equal to the register. Header `Area,Item,Element,Year,Unit,Value`; 28,290 data rows, 117 items, areas World plus Argentina, Australia, Brazil, China, India, New Zealand, United States of America; years 2011, 2021, 2022, 2023; the 12 elements the register lists. All as the register says.
* **Origin.** The register says "D17 assumed". Checked: every row is in the FAOSTAT Food Balances bulk file (D17), fetched once from https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_All_Data_(Normalized).zip (zip and csv sha256 equal to `qa/fao_bulk_hashes.csv`, csv dated 2025-10-14). Compared as a multiset per (area, item, element, year, unit): 27,554 keys, 0 differ. The assumption holds.
* **Values:**

| Value | Bulk (D17) | Extract | Result |
|---|---|---|---|
| Australia population 2022 26,200.98 thousand | item 2501 | same | ok |
| Australia wheat and products production 2011 27,410 kt | item 2511 | same | ok |
| Australia bovine meat food 2021 643 kt | item 2731 | same | ok |
| World wheat and products feed 2023 199,133 kt | item 2511 | same | ok |
| India rice and products production 2022 203,624 kt | item 2807 | same | ok |
| China pigmeat food 2011 50,354 kt | item 2733 | same | ok |

Unit conversion in the pipeline (`simpson_food.py fbs()`): kg a person = food (1000 t) / population (1000) x 1000; for Australia bovine meat, 643 kt over the 2021 population gives about 25 kg a person, consistent.

* **Note (extract design).** The extract drops the item code, so three labels appear twice: "Eggs" and "Milk - Excluding Butter" (group and item rows, equal values) and "Miscellaneous" (codes 2928 and 2899, which differ in 107 of 155 keys, for example Argentina import 2011: 32 and 31 kt). The scripts load into a dict keyed by area, item, element, so the last row read wins. No script read for this check names "Miscellaneous"; a total over all items would count the duplicates. Recorded as a note, not a mismatch.
* **Verdict: verified with notes.** Recommended register changes: origin "cut from D17 (FoodBalanceSheets bulk, csv sha256 2834e101..., file date 2025-10-14) by extract_fao_half.py; confirmed by V30a, all 28,290 rows"; drop "D17 assumed"; add the duplicate-label note.

## D26: fao_world_land_production.csv

* **Identity.** `analysis/method_tests_2025/fao_world_land_production.csv` exists, sha256 `96ce1924...64ea` equal to the register. Header `Source,Area,Item,Element,Year,Unit,Value`; 2,730 data rows (QCL 2,694, RL 36); 283 items in all (280 QCL plus 3 RL). Years 1990 to 1992 and 2021 to 2023. RL rows: World and Australia, Cropland, Permanent meadows and pastures, Agricultural land, as the register says.
* **Origin.** QCL rows: all 2,694 equal to D18 (above). RL rows: all 36 equal to the FAOSTAT Land Use bulk file (D19), fetched once (zip sha256 equal to `qa/fao_bulk_hashes.csv`). Origin confirmed.
* **Values:**

| Value | Bulk | Extract | Result |
|---|---|---|---|
| World cropland 1991 1,487,944.8 thousand ha | D19 | same | ok |
| World permanent meadows and pastures 2022 3,107,714.11 thousand ha | D19 | same | ok |
| Australia cropland 2022 31,650 thousand ha | D19 | same | ok |
| Australia permanent meadows and pastures 1991 445,400 thousand ha | D19 | same | ok |
| World cereal yield 1991, t x 1000 / ha = 2,683.4 kg/ha | D18 | `simpson_food.py yield_kg_per_ha` on the extract, same | ok |
| plus the five D18 values above | D18 | same | ok |

Conversion: `simpson_food.py` divides the RL areas (1000 ha) by 1000 to give million ha; checked on Australia 2022 cropland, 31.65 Mha.

* **Note for D19 (not in this group).** `qa/fao_bulk_hashes.csv` gives the Land Use file date as 2025-10-01; the zip entries are dated 2026-10-01. The zip hash is the one recorded, so the date in that file looks mistyped.
* **Verdict: verified.** Recommended status text: "verified (V30a): every QCL row equal to D18 and every RL row equal to D19".

## D31: ABS ERP by SA2, ABS_ANNUAL_ERP_ASGS2021

* **Identity.** `data/sa2/population_erp.csv` exists, sha256 `71f24cf1...dbea` equal to the register. Header `sa2_code,2011,...,2025`; 2,454 data rows (not 2,473 as the register's what_taken says); 9-digit ASGS 2021 SA2 codes. National sums: 2011 22,340,024; 2021 25,685,412; 2025 27,613,654.
* **Origin.** The ABS Data API host (api.data.abs.gov.au) was refused as unreachable by the proxy; not retried, so the file could not be compared with the API. The ABS "Regional population, 2024-25" release page (www.abs.gov.au, released 31/03/2026) links its Data Explorer dataset as `ABS_ANNUAL_ERP_ASGS2021`, the flow the register names, and its SA2 tables were used for the values.
* **Values** (source: ABS release page tables "Areas with the largest growth" and "highest growth rates"; pipeline: the file, SA2 code found by name in `data/sa2/land_types_by_sa2.csv`):

| SA2 | ABS page, ERP 30 June 2025 | File 2025 | Result |
|---|---|---|---|
| Rockbank - Mount Cottrell (213041359) | 35,856, growth 4,602 | 35,856, 2025 minus 2024 = 4,602 | ok |
| Mickleham - Yuroke (210051445) | 39,389, growth 4,145 | 39,389, 4,145 | ok |
| Fraser Rise - Plumpton (213041574) | 24,739, growth 4,064 | 24,739, 4,064 | ok |
| Box Hill - Nelson (115041623) | 26,348, growth 3,911 | 26,348, 3,911 | ok |
| Clyde North - South (212031556) | 28,328, growth 3,771 | 28,328, 3,771 | ok |
| Port Melbourne Industrial (206051511) | 3,148, 22.6% | 3,148, 581 / 2,567 = 22.6% | ok |
| Berrimah (701021012) | 2,871, 22.5% | 2,871, 22.5% | ok |
| Tarneit - North (213051584) | 15,880, 18.5% | 15,880, 18.5% | ok |

Pipeline use: the `population` column of `data/sa2/land_2011_method_by_sa2.csv` equals the 2025 column for all 2,450 SA2s it holds.

* **Verdict: verified with notes.** Notes: the API host was unreachable, so only 2025 (and 2024 through the growth figures) was checked against an ABS publication; earlier years are unchecked. Recommended register changes: what_taken "2,454-row table" (not 2,473); status "verified with notes (V30a): 8 SA2 values for 2025 and growth 2024-25 equal to the ABS Regional population 2024-25 release; API unreachable at the check".

## D43: release chain

* **Identity.** All files exist: `results/releases.json`, `releases/index.json`, 23 `releases/*/release.json`. **sha256 differs from the register**: listing hash `680a4ff004a6f8cefbd9cf93170d91a5676b631aa1dff8c3f225082f342ae980` against the register's `c9dff86c...3843` (bash glob order and bytewise order give the same listing). `results/releases.json` alone hashes to `0ca091739974e5392a49a5d8edc2674c7974bbc970a02ae6c34e654f4d113de9` against the register note's `0fbf7dc3...a9aa`; the file is dated 2026-11-07 04:41.
* **Origin.** Generated in the repository (`releases/README.md`, `web/scripts/releases.mjs`, `lock-release.mjs`). No network check applies.
* **Consistency checks.**
  * The 23 ids are the same in `results/releases.json`, `releases/index.json` and the folders; status, extends and label agree between results/releases.json and every release.json.
  * All 46 `model_sha256` and `regions_sha256` values equal the sha256 of `web/public/data/<id>/model.json` and `regions.json`.
  * All 98 input hashes in the release.json files match the files on disk (release.json inputs hashed without their `inputs` field, as `releases.mjs` defines; a plain file hash would wrongly report 46 differences).
  * 8 releases are frozen (2011, 2011-corrected, 2011-fixed, 2011-improved, 2011-thesis, 2025-fixed, 2025-improved, 2025-mirror), not 3 as the register note says; 15 are current.
* **Values** (re-evaluated with `web/src/model/evaluator.js` on the hash-checked builds, compared with `results/<id>.csv`):

| Value | Re-evaluation | results/ | Result |
|---|---|---|---|
| 2025-fixed Australia short (B090 41.5) | 41,503,537 | 41,503,537 | ok |
| 2025-fixed Australia long (B091 15.6) | 15,623,209 | 15,623,209 | ok |
| 2025-mirror Australia short (B088 49.4) | 49,389,414 | 49,389,414 | ok |
| 2025-improved Australia short (B092 53.6) | 53,643,731 | 53,643,731 | ok |
| 2011-fixed Australia short (A001 33.3) | 33,307,814 | 33,307,814 | ok |
| 2025-fixed WA long | 1,642,907 | 1,642,907 | ok |
| 2011-thesis Australia short and long, WA short and long | 40,439,187; 9,431,487; 3,696,938; 2,105,909 | same, and equal to thesis Table 16 | ok |

* **Verdict: verified with notes.** The chain is internally consistent and reproduces; the register row is stale. Recommended register changes: sha256 to `680a4ff0...e980` (or recompute when the row is next edited); results/releases.json alone `0ca09173...3de9`; notes "98 input hashes match (not 29); 8 of 23 releases frozen (not 3)"; status "verified with notes (V30a)".

## D46: data/2025-land

* **Identity.** `data/2025-land` holds `default-inputs-short-term.csv` and `default-inputs-long-term.csv`; listing sha256 `a38a1cdf...34e4` equal to the register. Header as data/2011 (`regionId,cropping,pasture,nonAg,...,regionName`), 60 zones each.
* **Origin.** Derived by `pipeline/land/make_defaults_2025.py` from `data/nrm2011/land_2011_method_zones.csv` and `data/2011`. Recomputed independently from those two inputs by the rule in the script docstring: all 960 checked cells equal (cropping, pasture, reserve, total area rounded from the zones; infrastructure and population from 2011; non-agricultural the remainder, floored at 0, one zone with a negative remainder in the short-term file; nature2 the reserve share, long term at least 0.30). All other 2011 columns unchanged.
* **Values:**

| Value | Input (zones file, zone 1) | data/2025-land row 1 | Result |
|---|---|---|---|
| cropping 316,498.98 km2 | zones | 316,499 | ok (rounded) |
| pasture 3,318,688.84 km2 | zones | 3,318,689 | ok |
| reserve 1,968,327.76 km2 | zones | 1,968,328 | ok |
| total 7,687,056.84 km2 | zones | 7,687,057 | ok |
| non-agricultural = 7,687,057 - 316,499 - 3,318,689 - 16,298 - 1,968,328 | zones and 2011 infrastructure | 2,067,243 | ok |
| B027: 2025 cropping 31.65 Mha | km2 / 10,000 | 31.65 | ok |

* **Verdict: verified.** Recommended register change to what_taken: "cropping, pasture, reserve, total area replaced; non-agricultural recomputed as the remainder; reserve share (nature2) recomputed; infrastructure and population kept at 2011" (the register's "then population replaced" belongs to data/2025-population).

## D49: data/abs-2022-25

* **Identity.** Six files (`cube_2022-23.json`, `cube_2023-24.json`, `cube_2024-25.json`, `group_trend.json`, `national_state_yields.csv`, `regions.json`); listing sha256 `7d05b8cc...a3213` equal to the register. `regions.json` "source": "ABS Data API AG_BROADACRE and AG_HORTICULTURE 1.0.1, SA2 ASGS Edition 3"; cubes carry rows "Wheat (ha)", "Wheat (t)" ... "Macadamias (t)" by column (Australia, states, SA2s).
* **Origin.** The ABS Data API host was unreachable (D31 above), so no request was made to it. The ABS release "Australian Agriculture: Broadacre Crops, 2024-25" (www.abs.gov.au, released 2/03/2026) prints production sold for the three years, and every national figure compared equals the cube rounded to thousand tonnes: production in the cubes is production sold (levied), as the register says.
* **Values:**

| Value | ABS release page | Cube | Result |
|---|---|---|---|
| Wheat 2024-25 Australia 34,779 kt | table "production sold by year" | 34,779,179 t | ok |
| Wheat 2022-23 Australia 41,199 kt | same table | 41,199,485 t | ok |
| Barley 2024-25 13,733 kt; canola 6,813 kt; oats 1,152 kt | same table | 13,733,406; 6,813,289; 1,151,512 t | ok |
| Wheat 2024-25 NSW 13,077 kt; WA 12,431 kt | "Wheat production sold by state" | 13,076,622; 12,430,868 t | ok |
| Sorghum 2024-25 545,000 ha | text | 545,225 ha | ok |
| Wheat Australia 2022-25 yield 2.7961 t/ha | cubes: mean of t/ha of the three years less seed 0.0665 | national_state_yields.csv 2.7961 | ok |
| Barley 2.9838, canola 1.9714 t/ha (seed 0.0446, 0.003) | cubes | national_state_yields.csv | ok |

* **Finding (data use, not a transcription error).** `national_state_yields.csv` gives Queensland oats 2022-25 as **-0.0211 t/ha**: levied oat tonnes in Queensland are tiny against the sown area (1,415 t on 104,636 ha in 2022-23; 2,201 on 59,939; 1,401 on 99,565), so the mean of 0.0214 t/ha less seed of 0.0425 is negative. South Australia oats is 0.2633 t/ha the same way. The negative Queensland value is not used in the 2025 yield matrix (that cell is "2011 x the crop's own national change", 54.0 g/m2), but South Australia oats is used as "observed 2022-25" (26.26 g/m2, 0.26 t/ha). Levied production understates oats where most of the crop is grazed or cut for hay. Not a mismatch against the source; worth a decision row.
* **Verdict: verified with notes.** Recommended status text: "verified with notes (V30a): national and state production sold equals the ABS Broadacre Crops 2024-25 release; API unreachable at the check; Queensland oats yield negative from levied production".

## D52: data/sa2 land use and land types

* **Identity.** Four files exist; listing sha256 `c522842e...5d94` equal to the register. Headers: `land_use_by_sa2.csv` `sa2_code,sa2_name,sa3_code,sa4_code,state,class_code,km2` (54,031 rows); `clum_classes.csv` `Value,Count,TERTV8,SECV8,PRIMV8,SIMP,AGIND` (189 classes, ALUM version 8 labels such as "1.1.1 Strict nature reserves"); `land_types_by_sa2.csv` and `land_2011_method_by_sa2.csv` 2,450 SA2s each (2,473 less the 23 the register notes).
* **Origin.** D32 (CLUM raster) and D33 (SA2 boundaries) are not stored, so the zonal statistics cannot be rerun. Checked instead against the files' own metadata and each other.
* **Values:**

| Value | Source side | Pipeline side | Result |
|---|---|---|---|
| Class 111 strict nature reserves | clum_classes Count x 0.0025 km2 (50 m cells) = 154,268.0 km2 | sum over SA2s 154,268.0 | ok |
| Class 210 grazing native vegetation | 3,613,776.6 km2 | same | ok |
| Class 310 plantation forests | 5,733.6 km2 | same | ok |
| Class 330 cropping | 341,826.1 km2 | same | ok |
| Class 540 residential and farm infrastructure | 1,349.6 km2 | same | ok |
| All classes | 7,687,605 km2 | land_use total 7,687,605; land_types total 7,687,605 | ok |
| Australia cropping and pasture (SA2 sums) | 316,498.98; 3,318,688.83 | zones file 316,498.98; 3,318,688.84 | ok |
| Braidwood population | ERP 2025 4,494 (D31) | land_2011_method_by_sa2 4,494 | ok |

Per SA2, the classes sum to the land_types total and both land tables' parts sum to their totals (largest difference 0.002 km2). The zones file's national reserve and total are 203 and 549 km2 below the SA2 sums (pieces outside the 2011 NRM zones); population 27,608,200 against 27,608,504; not a D52 matter.

* **Verdict: verified with notes** (internally consistent; underlying raster and boundaries not stored, so not checked against them). Recommended status text accordingly.

## D56: data/2025 yield layer

* **Identity.** Four files exist; listing sha256 `756659be...496a` equal to the register. `yield_matrix.csv` header `regionId,4,5,...,138` (135 Yield sheet rows), 60 zones; `yield_provenance.csv` `regionId,sheetRow,label,how`, 8,100 rows = 60 x 135; `crop_yields_by_year.json` note "Stage 1 yields (t/ha, before the zero-irrigation conversion) per crop, year and zone".
* **Origin.** Built by `pipeline/yields/recent/zone_yields.py` and `livestock_zone.py`. Observed cells recomputed from D49.
* **Values** (g/m2 = t/ha x 100 / (1 + 0.55 x irrigation default of the zone)):

| Value | From D49 | yield_matrix.csv | Result |
|---|---|---|---|
| Wheat zone 1 | 2.7961 t/ha, irrigation 0.007: 278.538 | 278.5399 | ok (0.001%, the 4-decimal rounding of the csv) |
| Barley zone 1 | 297.236 | 297.2363 | ok |
| Sorghum zone 1 | 372.356 | 372.3601 | ok |
| Canola zone 1 | 196.384 | 196.3865 | ok |
| Wheat zone 49 (WA) | 265.750 | 265.7472 | ok |
| Wheat 2022-23 zone 1, crop_yields_by_year.json | 41,199,485 / 12,925,286 - 0.0665 = 3.1210 | 3.12101 | ok |

* **Provenance counts.** observed 2022-25 455, 2011 x group factor 6,240, carried from 2011 960, none 221 (as the register says), plus 138 "2011 x the crop's own national change" and 86 "filled", which the register omits (total 8,100).
* **Livestock matrix (register's open question).** `yield_matrix_livestock.csv` hashes to `e514c2d3...2cb5`, the hash locked in the frozen releases 2025-fixed, 2025-mirror and 2025-improved, so it is the file those releases use. It differs from `yield_matrix.csv` only in rows 95 to 103 (sheep meat to pig meat); the 2025-livestock release text says rows 95 to 105.
* **Verdict: verified with notes.** Recommended register changes: add the 138 and 86 provenance counts; replace "Whether yield_matrix_livestock.csv is current ... was not checked" with "matches the hash locked in 2025-fixed, 2025-mirror, 2025-improved (V30a)".

---

## Summary

| Source | Verdict | Values checked | Mismatches |
|---|---|---|---|
| A01 | verified with notes | 14 | 0 |
| A19 | verified | 16 (56 anchor cells in all) | 0 (claim A321 release label, see block) |
| D15 | verified | 12 (+ 16 Table 16 state figures) | 0 |
| D18 | verified | 5 (+ 11,938 extract rows) | 0 |
| D23 | verified with notes | 6 (+ 28,290 rows) | 0 |
| D26 | verified | 5 (+ 2,730 rows) | 0 |
| D31 | verified with notes | 7 (8 SA2s) | 0 (row count 2,454, register says 2,473) |
| D43 | verified with notes | 6 (+ 46 build hashes, 98 input hashes) | register sha256 stale (listing and results/releases.json) |
| D46 | verified | 6 (+ 960 cells) | 0 |
| D49 | verified with notes | 11 | 0 (Queensland oats negative yield, data-use finding) |
| D52 | verified with notes | 8 | 0 |
| D56 | verified with notes | 5 (+ 1 year value) | 0 |

**Mismatches found.**
1. D43: register sha256 `c9dff86c...` does not match the files (`680a4ff0...`); results/releases.json alone `0ca09173...`, register note says `0fbf7dc3...`. Notes stale: 98 input hashes (not 29), 8 frozen releases (not 3).
2. D31: what_taken says a 2,473-row table; the file has 2,454 rows.
3. Claim A321 (not a source row): cites release 2025-resilience but quotes the thesis archive table; on 2025-resilience, SA is 0.35 and WA 0.47 at 100 years, not 0.36 and 0.49.

**Other findings.** D49 Queensland oats yield -0.0211 t/ha (levied production less seed), South Australia oats 0.26 t/ha used as observed in the 2025 matrix; D23 extract drops item codes, so "Miscellaneous" carries two different series under one label; D56 provenance omits 138 and 86 cells in the register; `qa/fao_bulk_hashes.csv` Land Use file date 2025-10-01 against zip entries dated 2026-10-01.

**Register rows touched:** none. **Ids checked:** A01, A19, D15, D18, D23, D26, D31, D43, D46, D49, D52, D56.

## Rerun

From the scratch folder `v30a_chk/` (bulk files are in `dl_d17/x`, `dl_d18/x`, `dl_d19/x`, downloaded as above):

```
python3 -I code/check_values.py /home/user/carrying-capacity-dashboard --wrong
cd /home/user/carrying-capacity-dashboard/analysis/method_tests_2025
python3 -I <scratch>/code/cmp_qcl.py "<scratch>/dl_d18/x/Production_Crops_Livestock_E_All_Data_(Normalized).csv" fao_world_land_production.csv fao_qcl_countries.csv half_qcl_world.csv
python3 -I <scratch>/code/cmp_multi.py "<scratch>/dl_d17/x/FoodBalanceSheets_E_All_Data_(Normalized).csv" half_fbs_countries.csv
cd /home/user/carrying-capacity-dashboard/web && node <scratch>/code/eval_releases.mjs /home/user/carrying-capacity-dashboard
node <scratch>/code/relcheck.mjs /home/user/carrying-capacity-dashboard
```

## Files read

Sources: the A01 scan (pages 1, 4, 5, 6, 11, 24 and the page 5 image), the A19 workbook (all sheets' heads; `years` in full), the D15 PDF (Tables 7 and 16), the three FAOSTAT bulk files, the two ABS release pages and the ABS catalogue page. Repository: `qa/sources_register.csv`, `qa/claims_register.csv`, `qa/fao_bulk_hashes.csv`, the data files named in each block, `analysis/method_tests_2025/simpson_food.py` (consumption block), `analysis/resilience_2025/resilience.py`, `make_release.py`, `README.md`, `tables.csv`, `replication.txt`, `pipeline/land/make_defaults_2025.py`, `pipeline/yields/recent/recent_yields.py`, `pipeline/yields/yields.py` (crop_year), `pipeline/yields/average.py`, `pipeline/yields/method.json`, `web/scripts/releases.mjs`, `web/scripts/lock-release.mjs`, `analysis/sensitivity_2025/evaluate.mjs`, `ERRATA.md` (rows on Table 7), `releases/README.md`.
