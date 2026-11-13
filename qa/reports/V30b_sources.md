# V30b: data sources behind the cited claims, group 2 of 3 (decision 74)

Checker: independent, blind. Brief: `qa/briefs/V30b_sources.md`; rules: `qa/briefs/_checker_rules_results_wave.md`. This report is the only repository file written. No register was edited; no git; no subagents. My scripts and downloads are in the scratch folder `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/V30b/` (`chk.py`, `d19.py`, `d19b.py`, `qcl.py`, `qcl2.py`, `d44.mjs`, `d16.mjs`, `d53.py`, `d53b.py`; downloads under `dl/`).

Network: one request at a time, curl with its default client string, no retry; no host refused. Requests: eprints.qut.edu.au (the D16 PDF, 1); bulks-faostat.fao.org (Land Use zip and Crops and livestock zip, 2); www.abs.gov.au (SA2 zip: a 301 redirect, followed once to its target; 7121.0 details pages for 2010-11 and 2015-16; the two cubes, the 2015-16 one through a 302 to ausstats.abs.gov.au). No other host was contacted. Copies of the FAO, SA2 and 7121.0 files left in the session scratch by other checks were used only to compare hashes against my own downloads; every value below is read from my own download or from the archive file named in the register.

## 1. Tolerance, stated before comparing

* Hashes, row counts, names, codes and pair lists: exact.
* A value the pipeline copies from the source (an extract row, a default-input cell): exact, after the unit conversion the pipeline states.
* A value the pipeline prints rounded: equal within one unit of the last printed digit.
* A value the pipeline computes from the source (a mean, a ratio, an average of two published intakes): within one unit of the last printed digit, or 0.5% where the printed value is a rounded model result.
* Coordinates: equal at the 4 decimal places the pipeline writes.

## 2. A deliberate wrong value, to show the check can fail

* `chk.py`: fed OWID Australia 158 against a wrong 168: reported `MISMATCH`; against 158: `MATCH`.
* `d19.py`: Australia cropland 2011 from the FAO Land Use bulk (32,078 thousand ha) against 99999: `MISMATCH`.
* `qcl.py`: Australia "Cereals, primary" 2022 (59,607,882.55 t) against 59,607,883.55: `MISMATCH`.
* My first adjacency rebuild of D53 (unsimplified polygons, plain 200 m buffer) gave 6,783 pairs against the pipeline's 6,729 (57 only mine, 3 only the pipeline's), and plain centroids differed from `centroids.csv` by up to 1.6 degrees: the geometry comparison does report differences when the method is not the same.
* My first FAO crops comparison keyed rows without the unit and reported 8 egg rows as mismatches (FAO gives eggs in both tonnes and thousand eggs); keyed with the unit, 0. The checks fail when something is wrong, including when the checker is wrong.

## 3. One block per source

### A03: Our World in Data HALF index table (comparator)

* Identity: `/home/user/carrying-capacity-models/Comparators/OWID-HALF-index-habitable-land-Alexander2016.csv` exists; sha256 `3fab565edc9cf357f4bf645d6ac72a204587a4767c912f9537c8e6edfe3b25cc` equals the register. Header: `Entity,Code,Year,HALF Index (habitable land area) (Alexander et al. (2016))`. 170 data rows, all year 2011: 169 countries and World (`OWID_WRL`). One row has no code (Cabo Verde).
* Origin: unknown in the register; no host is named, so nothing was fetched. Compared instead with the primary, the supplement `Literature review/Alexander2016_SI.pdf`, Table S5 ("Human Appropriation of Land for Food (HALF) index by country in 2011").
* Values (file row; pipeline place: `analysis/comparators_2025/README.md` line 22 and claim B059):

| Value | Source file | Pipeline | Result |
|---|---|---|---|
| Australia | 158 | 158 (README, B059) | match |
| United States | 137.64789 | 138 (README); 137.65 (register); 137.6 (B059 notes) | match |
| India | 22.2 | 22 (README) | match |
| World | 49.5 | 49.5 (README) | match |
| Ratio OWID over SI, Australia | 158 / 112.20 (SI Table S5) = 1.408 | 1.41 (B059) | match |
| Ratio, five more countries | World 49.5/35.13 = 1.409; US 1.408; India 22.2/15.76 = 1.409; Argentina 161.8/114.88 = 1.408; NZ 191.2/135.76 = 1.408 | 1.408 for all six (register notes) | match |

* Verdict: **verified with notes**. Register changes: the title says "170 countries and World", the file holds 169 countries and World (170 rows; `what_taken` has it right). Origin remains unknown (an OWID grapher export); say so plainly in `status`.

### A27: NHMRC Nutrient Reference Values (archive PDF)

* Identity: `/home/user/carrying-capacity-models/Foundation diets/nutrient-refererence-dietary-intakes.pdf` exists; sha256 `481140bb45d13bc84cd5c31e1dc5e386968e7e001387d529939beda1d61ec2ff` equals the register. 320 pages. Cover: "NUTRIENT REFERENCE VALUES FOR AUSTRALIA AND NEW ZEALAND INCLUDING RECOMMENDED DIETARY INTAKES 2006 VERSION 1.2 UPDATED SEPTEMBER 2017"; publisher NHMRC; ISBN Online 1864962437; PDF title metadata the same.
* Origin: unknown in the register; the NHMRC host is not named, so nothing was fetched. The cover and metadata confirm the title the register took from BLOCKED_SOURCES.md.
* Values: the ten intakes and the protein floor in `analysis/nutrition_lp_2025/optimise.py` lines 32 to 36 and 49 to 50 (`RDI = dict(...)`, `PROTFLOOR` 55), each the average of men and women aged 19 to 50 (adult RDI tables; PDF page numbers are the file's pages):

| Intake | Source (men; women, 19-30 and 31-50) | PDF page | Average | Pipeline | Result |
|---|---|---|---|---|---|
| Protein | 64; 46 g | 38 | 55 | 55 | match |
| Calcium | 1,000; 1,000 mg | 154 | 1,000 | 1000 | match |
| Iron | 8; 18 mg | 183 | 13 | 13 | match |
| Zinc | 14; 8 mg | 229 | 11 | 11 | match |
| Iodine | 150; 150 ug | 177 | 150 | 150 | match |
| Vitamin B12 | 2.4; 2.4 ug | 93 | 2.4 | 2.4 | match |
| Vitamin A | 900; 700 ug RE | 62 | 800 | 800 | match |
| Folate | 400; 400 ug DFE | 99 | 400 | 400 | match |
| Vitamin C | 45; 45 mg | 121 | 45 | 45 | match |
| Magnesium | 400 and 420; 310 and 320 mg | 188 | 362.5 | 365 | **mismatch** (+0.7%) |
| Potassium (AI) | 3,800; 2,800 mg | 209 | 3,300 | 3300 | match |

* Verdict: **verified with notes**. Every value is the source's, except magnesium: the stated rule (average of men and women 19 to 50) gives 362.5 mg, the pipeline uses 365 (perhaps rounded up to the nearest 5; the code does not say). The constraint is 0.7% tighter than the stated rule. Register changes: drop "Title taken from BLOCKED_SOURCES.md, not from the PDF cover" (the cover confirms it); add version 1.2 (September 2017) and the ISBN; origin "NHMRC (publisher)"; note the magnesium rounding.

### D16: Lane, Dawes and Grace 2015, accepted manuscript

* Identity: no `local_path` (not stored). I fetched the origin `https://eprints.qut.edu.au/75171/3/75171.pdf` once: 200, 432,249 bytes (the register's size). Cover page: "Lane, Murray, Dawes, Les, & Grace, Peter (2015) Scalar considerations in carrying capacity assessment: an Australian example. Population and Environment, 36(3), pp. 356-371"; DOI 10.1007/s11111-014-0216-1. sha256 of my download: `7b3f9e95c9c073f087e2bf816acae76fc8fef4d740f04a8b93ae721c0af22ded`, not the register's `e4104793...`. A copy with the register's hash exists in the session scratch (`article/article.pdf`). The two differ in 75 bytes, all in the QUT cover stamp: `/ModDate` and `/CreationDate` (mine D:20261107143744, the register's copy D:20260927011407) and the trailer `/ID`. Everything else is byte-identical. QUT restamps the cover per download, so the register's hash cannot be reproduced from the origin.
* Origin: correct (the file came from it).
* Values (paper text, section 4 and conclusion, lines of `pdftotext -layout`; pipeline: `analysis/model_archive/paper_claims.mjs` run from `web/`, release `2011-thesis`, the release ERRATA.md says produced the 2015 tables; my own `d16.mjs` for unrounded figures):

| Value | Paper | Pipeline (2011-thesis) | Result |
|---|---|---|---|
| National capacity | "over 40 million", "just over forty million" | 40,439,187 | match |
| Current population | 22.3 million | 22,326,388 | match |
| Aggregation of states | 28 million | 28.2 million | match |
| Aggregation of regions | 23 million | 22.9 million | match |
| Excess land, national | 1.8 million km2 | 1.78 million (1,782,633) | match |
| Excess land, regions summed | 4.5 million km2 | 4.55 million (4,551,388); the script prints 4.6 | match (one unit of the last digit) |
| NSW population over capacity | 74% | 7,454,854 / 10,033,151 = 74.3% | match |

* Verdict: **verified with notes**. Register changes: say that the sha256 is of one particular download (its cover stamp is dated 2026-09-27, while `dated_or_accessed` says retrieved 2026-10-26) and that a fresh download differs only in the QUT cover stamp and `/ID`; add the size as the reproducible identity check. `local_path` stays empty (not stored).

### D19: FAOSTAT Land Use bulk file

* Identity and origin: no `local_path`. I fetched `https://bulks-faostat.fao.org/production/Inputs_LandUse_E_All_Data_(Normalized).zip` once: 200, 2,970,716 bytes, Last-Modified Fri, 02 Oct 2026. Zip sha256 `39b739fb...a6ca3f` and unpacked csv sha256 `cd8c9ab6fd02529fe519c770d546135b8b39e74013190480f95c7d4a372d25ac` equal `qa/fao_bulk_hashes.csv` and the register. Header: `Area Code,Area Code (M49),Area,Item Code,Item,Element Code,Element,Year Code,Year,Unit,Value,Flag,Note`; csv 49,969,452 bytes. Zip member dates: **2026-10-01**.
* Values: all 36 `RL` rows of `analysis/method_tests_2025/fao_world_land_production.csv` and all 174 rows of `half_landuse.csv` equal the bulk exactly (0 mismatches). Values used by claims (bulk unit 1000 ha; pipeline converts to Mha by dividing by 1,000; 2021-23 is the mean of three years):

| Value | Bulk | Pipeline | Result |
|---|---|---|---|
| Australia cropland 2021-23 | 31,650 each year, mean 31.650 Mha | 31.65 (B045; `simpson_food.csv`) | match |
| Australia pasture 2021-23 | 331,869 each year, 331.869 Mha | 331.87 (B045) | match |
| Australia agricultural land 2021-23 | 363,519, 363.519 Mha | 363.5 (B262) | match |
| Australia cropland "1991-92" | 1991: 17,382 (17.382 Mha); 1992: 16,404 | 17.38 (B045) | match, but it is calendar 1991 alone (`simpson_food.py` line 61), not a 1991-92 mean (16.89) |
| Australia pasture "1991-92" | 1991: 445,400; 1992: 449,600 | 445.4 (B045) | match, same note (1991-92 mean 447.5) |
| World pasture 2011 | 3,182,078.85 (3,182 Mha) | 3,182 (B060) | match |

* Verdict: **verified with notes**. Register changes: `dated_or_accessed` "file dated Oct 2025" and `qa/fao_bulk_hashes.csv` `fao_file_date` 2025-10-01 should read 2026-10-01 (zip member dates; server Last-Modified 2026-10-02); the same year slip is in the `extract_fao_world.py` header. The notes say both "sha256 is unknown" and give the sha256: drop the first. Origin URL: replace "expected" with the confirmed zip URL. The "1991-92" label of the Australian land rows is calendar 1991 (worth a line in B045's notes).

### D24: FAOSTAT crops extract for the HALF test

* Identity: `analysis/method_tests_2025/half_qcl_world.csv` exists; sha256 `239f0c34...a403e3` equals the register. Header `Area,Item,Element,Year,Unit,Value`; 1,800 data rows, 279 items, World only, years 2011, 2021, 2022, 2023, elements Area harvested and Production (as `what_taken` says).
* Origin: the parent D18 bulk. I fetched `https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_All_Data_(Normalized).zip` once: 200, 33,921,825 bytes, Last-Modified 31 Dec 2025; zip sha256 `c5835418...0c6d6853`, csv `c4ff713e...b01`, both equal `qa/fao_bulk_hashes.csv`; zip member date 2025-12-23.
* Values: every one of the 1,800 rows equals the bulk row with the same item, element, year and unit (0 mismatches), and the bulk has no World row for that filter that the extract lacks (complete). Named values (bulk line numbers in the unpacked csv):

| Value | Bulk (line) | Extract | Result |
|---|---|---|---|
| Wheat area harvested 2011 | 220,839,223 ha (3,186,474) | 220839223 | match |
| Rice area harvested 2011 | 162,665,998 ha (3,179,952) | 162665998 | match |
| Maize area harvested 2011 | 172,620,259 ha (3,163,720) | 172620259 | match |
| Soya beans area harvested 2011 | 103,792,075 ha (3,182,250) | 103792075 | match |
| Oilcrops, Cake Equivalent production 2011 | 324,416,628.18 t (3,189,472) | 324416628.18 | match |
| Wheat production 2011 | 698,000,561.61 t (3,186,602) | 698000561.61 | match |

  `half_index.py` reads the extract keyed by item and element without the unit (line 25); the two egg items carry Production in both tonnes and thousand eggs, so the second row (thousand eggs) wins the key, but the script does not read egg production from this file (it reads Area harvested and the cake series), so no result is affected.
* Verdict: **verified with notes**. Register changes: the notes say the raw bulk sha256 is unknown; it is recorded (`qa/fao_bulk_hashes.csv`, D18) and reproduces from the origin.

### D27: FAOSTAT Australian production extract

* Identity: `analysis/method_tests_2025/fao_au_production_1997_2023.csv` exists; sha256 `d476a608...16be` equals the register. 15 rows: Australia, Production (t), Cereals primary, Meat Total, Pulses Total, years 1997, 1998, 2021 to 2023.
* Origin: all 15 rows are in the D18 crops and livestock bulk I downloaded (lines 135,030 to 137,038), equal exactly, and the bulk has no further row for that filter. So the origin is D18.
* Values (bulk in t; the pipeline converts to Mt by dividing by 1,000,000, `foran_poldy_balance.py` line 19):

| Value | From the bulk | Pipeline | Result |
|---|---|---|---|
| Grain 1997-98 mean | (31,279,701.3 + 32,621,200) / 2 = 31.950 Mt | 31.95 (B141) | match |
| Meat 1997-98 mean | 3.471 Mt | 3.47 (B141), 3.471 (B326) | match |
| Grain 2021-23 mean | 52.562 Mt | 52.56 (B145) | match |
| Meat 2021-23 mean | 4.656 Mt | 4.66 (B145) | match |
| Grain calendar 1997 | 31.280 Mt | 31.28 (B305) | match |
| Meat calendar 1998 | 3.601 Mt | 3.60 (B308) | match |
| Cereals plus pulses 1997-98 | 31.950 + 2.421 = 34.37 Mt | 34.37 (B328) | match |

* Verdict: **verified with notes**. Register changes: origin "cut from D18 by extract_fao_au_production.py"; the notes say both "NO extract script exists" and that one was written on 2026-11-07: keep only the second; "sha256 is unknown" for the bulk is out of date (c4ff713e..., reproduced here).

### D33: ABS ASGS Edition 3 SA2 boundaries

* Identity and origin: no `local_path`; sha256 unknown in the register. The register's URL answered 301 to `https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs/edition-3-july-2021-june-2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip`, which gave 200, 50,678,443 bytes, Last-Modified 24 Jun 2021, sha256 **`c4dc5bac209f01177eaa0715d27f32cdb09ab5784fb82979741556d2f8e6d148`** (the same as an older copy in the session scratch). Contents: `SA2_2021_AUST_GDA2020.shp/.dbf/.shx/.prj/.xml`. Metadata: fileIdentifier `ABS-ASGS-ED3-SA2-2021-7844`, title "Statistical Area Level 2 2021"; projection GDA2020 (EPSG 7844). Fields `SA2_CODE21, SA2_NAME21, ..., STE_NAME21, AREASQKM21`; 2,473 features, 19 without geometry.
* Values (what the pipeline takes: the polygons, via `sa2_adjacency.py`): 2,450 SA2s kept (2,454 with geometry; the 4 not kept are 108031161 Lord Howe Island and 901011001, 901021002, 901041004, the Other Territories, absent from the land file); representative points of all 2,450 equal `data/sa2/centroids.csv` at 4 decimals; adjacency rebuilt with the script's rule gives exactly the 6,729 pairs of `data/sa2/adjacency.csv` (the figure in claim A124's notes). Five named points under D53.
* Verdict: **verified with notes**. Register changes: sha256 `c4dc5bac...d148` (zip, 50,678,443 bytes, server date 24 Jun 2021); origin URL: the redirect target above (the old path still redirects); `dated_or_accessed`: confirmed 2026-11-13 by this check.

### D44: data/2011 default inputs

* Identity: `data/2011/default-inputs-short-term.csv` and `default-inputs-long-term.csv`; listing sha256 `8dfdcc04...9640` equals the register. 60 zones each; 26 columns: `regionId`, 24 input fields, `regionName` (so "24 fields" counts the inputs only).
* Origin: identical to the archive `Default inputs/default-inputs.csv` (A24) and `default-inputs-longterm.csv` (A25) once the archive's CR characters are removed (`tr -d '\r' | cmp`: identical; archive 61 CR and 61 LF each, repository 0 CR).
* Values: all 2,760 numeric cells of both files (60 zones, 23 fields and population, two presets) equal the built release `web/public/data/2011/regions.json` (`land`, `population`, `presets.short/long`): 0 mismatches. Examples: Australia population 22,326,388; Australia cropping 305,997 km2; NSW-ACT pasture 468,924; QLD population 3,908,395 (ERRATA row 6: 3.91 million); NT nature reserve 651,251; long term Australia fuel 253, infrastructure 500 m2, textiles 12.5.
* Verdict: **verified**. Register change: "60 zones x 24 fields" could add "plus id and name columns".

### D47: data/2025-population (derived)

* Identity: listing sha256 `f239f472...c4eb` equals the register. Same 26 columns; written with CRLF line ends (Python csv default), where data/2011 has LF.
* Values: I followed `pipeline/land/make_defaults_2025.py` and checked its rules against its inputs (`data/nrm2011/land_2011_method_zones.csv`, `data/sa2/population_erp.csv`):

| Check | Source side | D47 | Result |
|---|---|---|---|
| Australia population | zones file 27,608,199.78, rounded 27,608,200 | 27608200 | match |
| Infrastructure = population x 730 m2, zones 1, 2, 15, 26, 60 | 20,154; 6,626; 5,164; 4,139; 193 km2 | same | match (5 of 5) |
| Non-agricultural = total - cropping - pasture - infrastructure - reserve, same zones | 2,063,387; 218,751; 44,646; 263,294; 196,459 | same | match (5 of 5) |
| Zone population vs zones file, same zones | 27,608,200; 9,076,673; 7,073,857; 5,669,806; 264,883 | same | match (5 of 5) |
| Australia population vs ABS ERP 2025 (D31), the 2,450 kept SA2s | 27,608,504 | 27,608,200 | **mismatch** (304 people, 0.001%) |

  The national total of D31 over all 2,454 SA2s is 27,613,654; 5,150 of the gap is Lord Howe Island and the Other Territories (not in the model's land), and 304 people are lost in the SA2-to-zone allocation of `land_2011_method.py` (cause not traced). Against the release: all 2,760 cells equal `web/public/data/2025-population/regions.json` except long-term `fibre` in all 60 zones (12.5 in the file, 11.5 in the release); that is the release's documented patch in `releases.json` ("The workbook's own long-term default is =23/2 = 11.5 kg"), not a fault of the file.
* Verdict: **verified with notes**. Register changes: note the 304-person allocation loss and the exclusion of Lord Howe Island and the Other Territories (5,150 people); note that the release patches long-term fibre; note the CRLF line ends.

### D50: data/abs-history grain series

* Identity: `data/abs-history/grain_state.csv`; listing sha256 `2544d115...9bad` equals the register. Header `year,state,crop,area_ha,tonnes`; 134 rows, 2010-11 to 2015-16 (24, 24, 21, 21, 21, 23 rows).
* Origin: ABS 7121.0 details pages fetched for 2010-11 (title "7121.0 - Agricultural Commodities, Australia, 2010-11") and 2015-16, and one cube from each: `71210do004_201011.xls` (sha256 `1ab4505f...8f07`; sheet "Broadacre data", "Table 2 Broadacre commodities, National and State-2010-11") and `7121do001_201516.xls` (sha256 `faa084ae...7660`; one sheet per state, "Table 1: AGRICULTURAL COMMODITIES-Australia-2015-16"). Both equal the copies the script downloaded, so these are the cubes it read.
* Values: all 24 rows of 2010-11 and all 23 of 2015-16 (94 values) equal the cubes exactly; for 2015-16 the cube has no row the csv lacks (NT oats is absent in both). Examples: 2010-11 Australia wheat 13,501,780 ha and 27,410,076 t (sheet row 10, 11); NSW barley 878,015 ha, 2,193,564 t; WA oats 254,860 ha, 283,297 t; 2015-16 Australia wheat 11,282,202.1 ha, 22,274,513.74 t ("Aust." sheet rows 10 and 11); WA wheat 4,615,760.97 ha, 8,510,576.52 t; Victoria barley 844,470.21 ha, 1,107,379.79 t. No unit conversion (ha and t throughout). The years 2011-12 to 2014-15 (87 rows) were not re-fetched.
* Verdict: **verified with notes** (two of six years checked against the origin). Register changes: add the two cube names and hashes; note that the Australia rows include the ACT while the state rows do not list it.

### D53: data/sa2 adjacency and centroids (derived from D33)

* Identity: listing sha256 `ac971204...7410` equals the register. `centroids.csv` (`sa2_code,lon,lat`, 2,450 rows) and `adjacency.csv` (`sa2_a,sa2_b`, 6,729 pairs).
* Origin: rebuilt from my own D33 download with the method in `analysis/regionalise_2025/sa2_adjacency.py` (Albers EPSG 3577, outlines simplified at 200 m, 200 m buffer; points are `representative_point()` in Albers, returned to EPSG 4326, rounded to 4 decimals).
* Values: all 2,450 points equal at 4 decimals (largest difference 0); pair set identical (6,729 against 6,729, none only on one side). Named: Braidwood 101021007 149.7535, -35.5104; Karabar 101021008 149.2337, -35.3755; Acton 801051049 149.1158, -35.2799; Ross 702011051 133.831, -23.78; Townsville City - North Ward 318021490 146.809, -19.2539 (all match). Pairs (101021007, 101021611) and (101021007, 101031015) present in both.
* Verdict: **verified with notes**. Register change: `what_taken` says "centroid lon/lat"; the file holds representative (interior) points, which differ from geometric centroids by up to 1.6 degrees. Say "representative point".

### D57: data/2025 pasture and dairy files (derived)

* Identity: the four files exist; listing sha256 `411ceb0b...7ebc` equals the register. Headers: `pasture_quality_by_zone.csv` (59 zones, `zone,name,state,pasture_km2,improved_km2,improved_share,milk_tonnes_2025,milk_g_per_m2_improved`); `dairy_good_land_by_zone.csv` (60); `dairy_farm_yield_by_zone.csv` (60); `abs_improved_pasture_2007_08_by_zone.csv` (60).
* Origin and values, by upstream source:
  * A15 (`Yield data/NRM07-08/land use07-08.xls`, sha256 `32ccde9e...4198`, Sheet1, rows 2 to 4, columns 1 to 60; row 1 is "2007-8" and the zone names): all 180 values of `holding_000ha`, `improved_pct_of_holding`, `other_grazing_pct_of_holding` equal the sheet (0 mismatches; the one blank, Hawkesbury-Nepean-Sydney improved pasture, is blank in both). Zone names match by column (zone 3 Border Rivers-Gwydir, zone 60 NT). `abs_improved_share_of_grazing` = improved / (improved + other grazing): NSW 26.0/78.3 = 0.3321, Border Rivers-Gwydir 0.4941, NT 0.0342: match. The AUS column holds 160.0 and 403.8, which cannot be percentages of holding area; its share 0.2838 is computed from them as if they were. Hawkesbury-Nepean-Sydney's blank is written as share 0.0.
  * D37 (`dairy_farm_yield_by_state.csv`): each of the 60 zones of `dairy_farm_yield_by_zone.csv` carries its state's `milk_g_per_m2` (Australia and NT the AUS value 1,012.6): 0 mismatches. Unit conversion litres a ha x 1.03 kg/L / 10 = g/m2: NSW 9,337 gives 961.7 (961.7), Victoria 10,408 gives 1,072.0 (1,072.1), Tasmania 13,586 gives 1,399.4 (1,399.3), AUS 9,831 gives 1,012.6 (1,012.6): match within one unit.
  * D32 (CLUM) and D34 (GAEZ), behind `improved_km2`, the arable shares and the GAEZ shares, and D36 behind `milk_tonnes_2025`: not stored, not checked against a source. Internal relations hold only to the rounding of the printed areas (for example zone 27, 13,084 t over 83.5 km2 gives 156.7 against the printed 156.79, because the area is printed to 0.1 km2); state rows of `pasture_quality_by_zone.csv` hold 0 areas by design.
* Verdict: **verified with notes** (the A15 and D37 parts; the CLUM, GAEZ and D36 parts cannot be checked here). Register changes: note that the AUS column of A15 is not a percentage and that a blank improved share is read as zero; name D36 as the source of `milk_tonnes_2025`.

## 4. Summary

| Source | Verdict | Values checked | Mismatches |
|---|---|---|---|
| A03 | verified with notes | 9 (4 table values, 5 ratios against the SI) plus the row count | 0 |
| A27 | verified with notes | 11 (protein floor and ten micronutrients) | 1 (magnesium 365 against 362.5) |
| D16 | verified with notes | 7 | 0 (hash not reproducible from the origin; cover stamp only) |
| D19 | verified with notes | 210 extract rows, 6 claim values | 0 values; 1 metadata (file date 2025 against 2026) |
| D24 | verified with notes | 1,800 extract rows, 6 named | 0 |
| D27 | verified with notes | 15 extract rows, 7 derived | 0 |
| D33 | verified with notes | 2,450 points, 6,729 pairs, identity fields | 0 (sha256 supplied) |
| D44 | verified | 2,760 cells, 2 files byte-compared | 0 |
| D47 | verified with notes | 16 rule checks, 2,760 cells against the release | 1 (national population 304 below D31 for the kept SA2s); release fibre patch documented |
| D50 | verified with notes | 47 rows (94 values), 2 of 6 years | 0 |
| D53 | verified with notes | 2,450 points, 6,729 pairs, 5 named | 0 ("centroid" is a representative point) |
| D57 | verified with notes | 180 A15 values, 60 zone yields, 4 unit conversions, 3 shares | 0 (CLUM, GAEZ, D36 parts not checkable) |

Mismatches found:

1. A27: magnesium intake 365 mg in `optimise.py` against 362.5 mg by the stated rule (average of 400, 420, 310, 320 from NHMRC page 188).
2. D47: Australia 2025 population 27,608,200 against 27,608,504 in D31 for the same 2,450 SA2s (304 people lost in allocation).
3. D19: the bulk file date is recorded as Oct 2025 (register, `qa/fao_bulk_hashes.csv`, `extract_fao_world.py`); the file is dated 2026-10-01.
4. D16: the register's sha256 cannot be reproduced from the origin (QUT restamps the cover per download; content otherwise identical).
5. A03 title: 169 countries and World, not 170 countries and World.

Other things found that the brief did not ask about: B045 calls calendar 1991 FAO land "1991-92"; `half_index.py` keys the crops extract without the unit (harmless for the rows it reads); D53 calls representative points centroids; the AUS column of A15 is not a percentage; data/2025-population has CRLF line ends where data/2011 has LF.

## 5. Register rows touched and ids checked

Register rows touched: none. Ids checked: A03, A27, D16, D19, D24, D27, D33, D44, D47, D50, D53, D57.

## 6. Commands to rerun (from the repository root unless stated; S is the scratch folder above)

* Hashes: `sha256sum <file>`; folder rows: `find <dir> -type f | LC_ALL=C sort | xargs sha256sum | sha256sum` (lists in the order of `local_path`).
* A27: `pdftotext -layout "<pdf>" S/nrv.txt` and read the adult tables at the lines of "Adults EAR ... <nutrient>".
* D16: `cd web && node S/d16.mjs` and `node ../analysis/model_archive/paper_claims.mjs`.
* D19: `python3 -I S/d19.py "S/dl/lu/Inputs_LandUse_E_All_Data_(Normalized).csv" fao_world_land_production.csv half_landuse.csv` (from `analysis/method_tests_2025`); `python3 -I S/d19b.py "<same csv>" S`.
* D24, D27: `python3 -I S/qcl.py "S/dl/qcl/Production_Crops_Livestock_E_All_Data_(Normalized).csv"` and `python3 -I S/qcl2.py "<same>"`.
* D33, D53: `python3 -I S/d53b.py S/dl/sa2/SA2_2021_AUST_GDA2020.shp` (from any folder outside the downloads).
* D44, D47: `cd web && node S/d44.mjs 2011 data/2011` and `node S/d44.mjs 2025-population data/2025-population`.
* D50 and D57: the inline python in this session (xlrd over `S/dl/abs_71210do004_201011.xls`, `S/dl/abs_7121do001_201516.xls` and the A15 xls); the comparisons are restated in the blocks above.

Files read: `qa/briefs/V30b_sources.md`, `qa/briefs/_checker_rules_results_wave.md`, `qa/sources_register.csv`, `qa/claims_register.csv`, `qa/fao_bulk_hashes.csv`, the source files above, `analysis/comparators_2025/README.md`, `analysis/method_tests_2025/README.md`, `extract_fao_world.py`, `half_index.py`, `simpson_food.py`, `foran_poldy_balance.py`, `analysis/nutrition_lp_2025/optimise.py` and `README.md`, `analysis/model_archive/paper_claims.mjs`, `ERRATA.md` (rows 1 to 6 and the 2015 lines), `analysis/regionalise_2025/sa2_adjacency.py`, `analysis/resilience_2025/fetch_abs_grain.py`, `pipeline/land/make_defaults_2025.py`, `pipeline/land/land_2011_method.py` (allocation lines), `analysis/pasture_2025/pasture_quality.py` (header), `web/public/data/releases.json`, the data files under `data/2011`, `data/2025-population`, `data/abs-history`, `data/sa2`, `data/2025`, `data/nrm2011/land_2011_method_zones.csv`.
