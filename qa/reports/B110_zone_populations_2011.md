# B110: every 2011 zone population on the ABS footing (decision 100)

Brief: `qa/briefs/B110_zone_populations_2011.md`. Finding answered: R03a issue 1 (both referees of Paper A). No git, no subagents, no network. `qa/claims_register.csv` and every frozen release were not edited. No file of `analysis/comparison_2025`, `sensitivity_2025`, `resilience_2025`, `method_tests_2025` or `pasture_2025` was written (`analysis/comparison_2025/movers.csv` is read only). Every `-2` output is unchanged (hashes in section 7).

## 1. The outcome in plain words

* **The thesis's 2011 regional populations are not the ABS estimate, and nothing records how they were made.** Against the ABS estimated resident population at 30 June 2011, allocated to the same zones the way the 2025 population is, 23 of the 52 zones other than North East Vic differ by more than 10% and 12 lie outside 0.8 to 1.25 times the ABS figure. Inland and arid zones are much too high (Western NSW 3.0 times, SA Arid Lands 3.0, Alinytjara Wilurara 2.6); a few are too low (Eyre Peninsula 0.72). In total they differ by little: the 53 regions sum to 22,220,341 in `2011-fixed-2` against 22,336,514 on the ABS route.
* **Every 2011 regional population is the ABS figure** in two new releases, `2011-fixed-3` and `2011-improved-3` (status current), through one new data module, `zone-population-2011`. Fitzroy and Wet Tropics (ERRATA error 9) are included, so error 9 is closed. The national row stays at 22,326,388; each state is the sum of its regions.
* **On the corrected method nothing moves in the short term.** 22 regions are over capacity in 2011 either way, the same eight flips, the same two clean flips (Mackay Whitsunday, North Tasmania). **In the long term 36 becomes 35:** Northern and Yorke (86,691 people against a capacity of 89,933) is under capacity in 2011, so it is no longer a flip; long-term flips go from 4 to 3, and the one clean long-term flip (South West Qld) holds.
* **The drought figures move by one region here and there.** Share of people in over-capacity regions in an average year: 81.3% to 81.5% (it prints 81% before and 82% after: a rounding edge). Regions that tip over capacity at 1 in 10 in 2011: 2 to 3 (Burnett Mary joins Corangamite and North East Vic). At 1 in 20: 5 to 4 (Lower Murray Darling leaves). Over-capacity counts at 1 in 10, 20, 50, 100: 24, 27, 32, 33 become 25, 26, 30, 32.
* **Capacities do not move on the corrected method** (all 120 cells equal). On the improved method they move slightly (75 of 120 cells, at most 0.9%), because there the infrastructure area enters capacity through `reserve-pro-rata`; so the brief's test 4 holds for `2011-fixed-3` and, as expected, not exactly for `2011-improved-3`.
* No national figure, no state status and nothing in 2025 changes.

## 2. The comparison (step 1)

Table: `analysis/population_2011/zone_population_2011_comparison.csv` (zone; name; state; `2011-fixed-2` figure; ABS figure; difference; percent of the ABS figure; note). Script: `analysis/population_2011/zone_populations_2011.py`.

**How the original figures were made, as far as the records go.** The 2011 regional populations are the author's (sources register D44, `data/2011/default-inputs-*.csv`, copied from the QUT snapshot); they are thesis Table 25 (p. 382) and they first appear in the author's land-use workbook (`Yield data/NRM - Landuse.xls`, sheet `xSummary`). The thesis says they were "sourced predominantly from journal articles" (section 8.5, p. 221, footnote 912: Robins and Dovers 2007, *Geographical Research* 45(3), pp. 280-281). That article's table gives rounded figures (about 200,000 for North East and 189,500 for Goulburn Broken, B90), so the exact figures were not copied from it. No reference date, ABS release or allocation is recorded anywhere in the project (R03a issue 1). The 52 regions sum exactly to the national 22,326,388 before error 8 was corrected (ERRATA error 6). Infrastructure is population x 730 m2 in all 60 zones (checked again here). Two pairs of zones share one figure to the person (errors 8 and 9). Why inland zones run high cannot be told from the records; three of the five older-boundary zones are among the 12 outliers (Desert Channels, Alinytjara Wilurara, Northern and Yorke; claim A066, `analysis/land_2011/README.md`), the other nine are not.

**The ABS figure** is the column `erp_2011_sa2_route` of `zone_population_2011.csv` (B90): ERP at 30 June 2011 by SA2 (D31, 2021 SA2s), shared among zones by residential land (CLUM 5.4) where an SA2 straddles a boundary, exactly as the 2025 population is allocated.

| | 2011-fixed-2 | ABS route | Difference |
|---|---|---|---|
| 53 regions (52 NRM regions and the Northern Territory) | 22,220,341 | 22,336,514 | -116,173 (-0.5%) |
| National row (kept) | 22,326,388 | 22,326,388 | the regions sum to 10,126 more on the ABS route |

The 12 outside 0.8 to 1.25 (release over ABS): Western NSW 3.009 (37,528 against 12,470), SA Arid Lands 2.955 (31,361 against 10,613), Alinytjara Wilurara 2.564, Border Rivers Maranoa-Balonne 1.513, Desert Channels 1.509, Northern and Yorke 1.447 (125,445 against 86,691), Border Rivers - Gwydir 1.444, South West Qld 1.368, Cape York 1.319, Southern Gulf 1.31, Hunter - Central Rivers 1.264; Eyre Peninsula 0.719. Largest absolute: Hawkesbury - Nepean - Sydney -321,475 (-7.3%), Hunter - Central Rivers +265,889 (+26.4%), Port Phillip and Westernport -119,829 (-2.8%). North East Vic is 0 (corrected in `-2`); Fitzroy -2.0%, Wet Tropics -6.4%.

**A correction to R03a:** its list of the 12 names Glenelg Hopkins (0.805) and South West WA (0.807); both are inside 0.8 to 1.25. The twelfth and eleventh are Hunter - Central Rivers (1.264) and Southern Gulf (1.31). The counts (23 and 12) are right.

## 3. The correction (step 2)

* `methods/zone-population-2011/method.json` (new, generated by `zone_populations_2011.py`): `zoneInputs` for all 53 regions: population = ABS figure; `infrastr1` = round(population x 730 m2), the rate the 2011 land method and `north-east-vic-population` use; `nonAg` = old `nonAg` + old `infrastr1` - new `infrastr1` (total area unchanged; none negative). Zone 22 gets the same 98,604, 72 and 3,034 as `north-east-vic-population`. Fitzroy 235,629 (infrastructure 172 km2), Wet Tropics 246,885 (180 km2).
* `web/scripts/build-data.mjs` needed **no change**: B90's `zoneInputs` step already applies any number of zones before `statePopulationsFromRegions`, so each state becomes the sum of its regions and the Northern Territory (zone 60, no children) takes its value directly. The national row is not in the module.
* `releases/2011-fixed-3/release.json` and `releases/2011-improved-3/release.json` (new, status current, not locked): extend `2011-fixed-2` and `2011-improved-2` with the one module. `releases/index.json`: the two ids added after `2011-improved-2`.
* `results/2011-fixed-3.csv`, `results/2011-improved-3.csv` (new) and `results/releases.json` (two releases added), by `node scripts/make-results.mjs 2011-fixed-3 2011-improved-3` after `node scripts/build-data.mjs`. `results/comparison_cells.csv` was rewritten byte-identical. The full `npm run results` was **not** run.
* `ERRATA.md`: error 10 added in the table's format; error 9's status closed ("corrected by error 10").
* `methods/README.md`: one row for the module.

State populations (`-2` to `-3`): NSW-ACT 7,591,160 to 7,586,092; Victoria 5,439,885 to 5,537,815; Queensland 4,513,849 to 4,476,810; South Australia 1,644,582 to 1,639,287; Western Australia 2,293,510 to 2,353,409; Tasmania 507,644 to 511,483; Northern Territory 229,711 to 231,618. No state or national status changes on either method.

## 4. What changes (step 3)

Outputs, all new, `-2` files untouched: `analysis/paper_a/movers-3.csv` (movers table with the 2011 columns from `2011-fixed-3` and a `release_2011` column; script `movers_release.py`, which reproduces `movers.csv` exactly when run on `2011-fixed-2`), `analysis/paper_a/regional_flips-3.csv`, `analysis/paper_a/shocks_by_region-3.csv` (2011 rows named `2011-fixed-3`), `analysis/paper_a/shocks_summary-3.csv` (2011 rows named `2011-fixed-3`), and `analysis/population_2011/changes_2_to_3.csv` (every zone, preset and tier whose population, capacity or status differs; script `compare_2_and_3.py`).

**National counts, corrected method, 53 regions**

| Measure | `-2` | `-3` |
|---|---|---|
| Regions over capacity 2011, short term | 22 | 22 |
| Regions over capacity 2011, long term | 36 | **35** |
| Short-term flips 2011 to 2025 | 8 (7 over to under, 1 under to over) | 8 (the same) |
| Clean and robust short-term flips | 2 (Mackay Whitsunday, North Tasmania) | 2 (the same) |
| Long-term flips | 4 | **3** (Northern and Yorke drops out) |
| Clean and robust long-term flips | 1 (South West Qld) | 1 (the same) |
| Long-term flips with an artefact flag; not robust | 3; 2 | **2; 1** (Desert Channels and SA Arid Lands; SA Arid Lands) |
| Net fall short / long against clean flips | 6 against 2; 4 against 1 | 6 against 2; **3 against 1** |
| Share of people in over-capacity regions, average year (2011) | 81% (81.3) | **82% (81.5)** |
| Share at 1 in 10, 20, 50, 100 (2011) | 84, 87, 91, 92% | **85, 88, 90, 91%** |
| Regions over capacity at 1 in 5, 10, 20, 50, 100 (2011) | 23, 24, 27, 32, 33 | 23, **25, 26, 30, 32** |
| Regions under in an average year and over at 1 in 10 (2011) | 2: Corangamite, North East Vic | **3: + Burnett Mary** |
| The same at 1 in 20 (2011) | 5: Burnett Mary, Corangamite, Lower Murray Darling, Murrumbidgee - ACT, North East Vic | **4: Lower Murray Darling leaves** |
| Long-term share of people in over-capacity regions (2011, from results; `long_term_and_measures.mjs` not rerun) | 94% (93.7) | **93% (93.4)** |
| National capacity, population, ratios; sums of regional capacities; every 2025 figure | | unchanged |

**Every status change, corrected method (`2011-fixed-2` to `2011-fixed-3`):** Northern and Yorke, long term, over to under (125,445 to 86,691 against 89,933). Drought runs (short-term settings): 1 in 10 Burnett Mary under to over (296,812 to 309,314 against 298,088); 1 in 20 Lower Murray Darling over to under (31,567 to 28,081 against 30,456); 1 in 50 Burdekin over to under (242,531 to 230,763 against 231,658) and Northern and Yorke over to under; 1 in 100 Condamine and Northern and Yorke over to under, SA Murray Darling Basin under to over (101,610 to 118,534 against 111,565).

**Improved method (`2011-improved-2` to `2011-improved-3`):** short term 21 to 20 over capacity (Desert Channels over to under: 18,479 to 12,247 against 14,748); long term 38 to 36 (Western NSW: 37,528 to 12,470 against 35,040; Northern and Yorke: 86,691 against 111,711). Capacities move in 75 of 120 cells by at most 0.9% (Port Phillip and Westernport long term 10,310 to 10,407). Regions differing in status between the corrected and improved method, 2011: short term Mackay Whitsunday becomes Desert Channels and Mackay Whitsunday; long term Western NSW and South East SA becomes South East SA.

## 5. Tests (step 4)

`python3 -I analysis/population_2011/compare_2_and_3.py`: 13 checks, 0 failed.
* `2011-fixed-3` capacities equal `2011-fixed-2`'s in all 120 cells: **pass**. `2011-improved-3`: 75 cells differ (reported above; infrastructure enters capacity through `reserve-pro-rata`), so this test is stated for the corrected method only.
* Every state equals the sum of its regions, both releases, both presets: **pass**. National row 22,326,388: **pass**.
* **The 52 NRM regions plus the Northern Territory sum to 22,336,514** on both releases: **pass**.
* Every region of `2011-fixed-3` carries the ABS figure: **pass**. `shocks_by_region-3.csv` capacities equal the `-2` file in all 648 rows and its 2025 rows are identical: **pass**.

`web/test/releases.test.js`: one test appended (module covers exactly the 53 regions with the ABS figure and 730 m2; the `-3` releases add only this module; only populations, infrastructure and non-agricultural land of the regions and the state populations differ; area unchanged; states are their regions' sums; the regions sum to 22,336,514; the national row is kept; `2011-fixed-3` capacities equal `2011-fixed-2`'s). `cd web && node --test test/*.test.js`: **34 of 34 pass** (33 before).

## 6. What was run

1. `python3 -I analysis/population_2011/zone_populations_2011.py` (twice; byte-identical outputs).
2. `cd web && node scripts/build-data.mjs && node scripts/make-results.mjs 2011-fixed-3 2011-improved-3` (rebuilds `web/public/data/` for every release; the built data of the existing releases come from unchanged inputs).
3. Reproduction of the `-2` outputs into the scratchpad with the edited scripts: `regional_flips`, `shocks_by_region` and `shocks_summary` byte-identical to the files on disk; `movers_release.py 2011-fixed-2` identical in every value to `movers.csv`.
4. `python3 -I analysis/paper_a/movers_release.py 2011-fixed-3 analysis/paper_a/movers-3.csv`; `python3 -I analysis/paper_a/regional_flips.py analysis/paper_a/movers-3.csv analysis/paper_a/regional_flips-3.csv`; `node analysis/paper_a/shocks_by_region.mjs analysis/paper_a/shocks_by_region-3.csv 2011-fixed-3`; `python3 -I analysis/paper_a/shocks_summary.py --release-2011 2011-fixed-3 analysis/paper_a/shocks_by_region-3.csv analysis/paper_a/shocks_summary-3.csv` (run twice; identical).
5. `python3 -I analysis/population_2011/compare_2_and_3.py`; `cd web && node --test test/*.test.js`.

## 7. Every file changed

| File | Change | sha256 after |
|---|---|---|
| `analysis/population_2011/zone_populations_2011.py` | new: comparison table and module generator | 0fd2ab853345a54570a86bfa0a39d4fcf875d1a5d77b9bf0b7b0f020ede0ee70 |
| `analysis/population_2011/zone_population_2011_comparison.csv` | new (generated) | 29523b77c1c97310b454c729ffe9781bd26d047a3dd0f3c90b9dfa3c55fc22b2 |
| `analysis/population_2011/compare_2_and_3.py` | new: `-2` against `-3`, and the step 4 checks | 39788c62b9d672f9168c780a9d8bb1072e06650fbbd046e69f1ec44a855b693f |
| `analysis/population_2011/changes_2_to_3.csv` | new (generated) | f9c0a726435a456b663c98df8e815c38af09d7261f78a5c13b8ac48bcdc49265 |
| `methods/zone-population-2011/method.json` | new module (generated) | 0be3ade3cf694f648eff5cd514124bb761504dd70895b8f86b7ec6a99f8fb99e |
| `methods/README.md` | one row added | 423299104ec86a2f77ab6ebf25dede1da4577156331b5ceacad98a9936baac9d |
| `releases/2011-fixed-3/release.json`, `releases/2011-improved-3/release.json` | new releases, status current | db87b104...e7b2b2; 988252d3...5d82 |
| `releases/index.json` | two ids added | 585b6990f4f08b113d4bd91a4d35de6b48c709eca616cf287f2c159c0e92be7a |
| `results/2011-fixed-3.csv`, `results/2011-improved-3.csv` | new (generated) | 39e8533fb271436d789992f3a7e2fed18fa346066a2c810ba208cf9904c0b481; c11dcbc88605006472e0e714c4cbcda6131f8cf4968712a8f1a8c832dc1421e1 |
| `results/releases.json` | regenerated: two releases added | b4ad2d5d...2a17 before; 8b295ccbe4538e988afbb7f6fccf4495ff9aaae7bbd113522e8c910570150fb8 after |
| `results/comparison_cells.csv` | rewritten by `make-results.mjs`, byte-identical | 94b3778c...daadb (unchanged) |
| `web/test/releases.test.js` | one test appended | 729c6bfe3f9a382d095afb49b4a8c6065b32aafcc08afa5e442a80d41a7e1e90 |
| `analysis/paper_a/movers_release.py` | new: movers table on a named 2011 release (reads `movers.csv`, never writes it) | e56797664bd1ce4b680c9f29582ff33424c67f120718254ce42bef900b27b323 |
| `analysis/paper_a/movers-3.csv` | new (generated) | 3bd8901478acce6be9f9f985a2eb12e16bf9a9b630a160da961c68803b8cf42b |
| `analysis/paper_a/regional_flips.py` | optional `MOVERS.csv OUT.csv` arguments; default run unchanged | 03faf20639a05f4800397d371d21d31a0a232585b3da39fc377b355316099109 |
| `analysis/paper_a/regional_flips-3.csv` | new (generated) | 9aa28f1000cb324e8848f05695dc0e118b7f897ebcd595cf82982ce337152d3a |
| `analysis/paper_a/shocks_by_region.mjs` | optional second argument, the 2011 release (default `2011-fixed-2`) | 875e7abb4819454d4c8a384433f628d9d6625a736ba00d524d2c4c89e697d58d |
| `analysis/paper_a/shocks_by_region-3.csv` | new (generated) | 3b5f4a2f32486772ffd7d046f3a4645bb31ac1a4cba1215f6a65115d71628cdb |
| `analysis/paper_a/shocks_summary.py` | optional `--release-2011 ID IN OUT` (shocks only; does not write `scenarios_by_region.csv`); default run unchanged | e6853ff96804a8e483af2827d37a8b719c084246c5b099acc81a3187172f6f7f |
| `analysis/paper_a/shocks_summary-3.csv` | new (generated) | 3e284bfced843ff106ca5f7a2aac7d7d3b6787cbc3945f05cf582dcaaf05284a |
| `ERRATA.md` | error 10 added; error 9 status closed | 63d3846995df3d942dad18eebcda0f1b9715a782a385964400dca897312306a6 |
| `qa/reports/B110_zone_populations_2011.md` | this report | |

Unchanged (checked): `analysis/paper_a/regional_flips.csv` 052a3b2d...0a1503, `shocks_by_region.csv` 00e9eaf1...f980, `shocks_summary.csv` 0446002f...35e5, `results/2011-fixed-2.csv` c8dea311...cb10, `results/2011-improved-2.csv` 33e04731...f497, `analysis/comparison_2025/movers.csv` dec71f5d...e5a6 (all equal B90's recorded hashes). `web/public/data/` (generated, not tracked as a result) was rebuilt for every release.

## 8. Follow-ups not done (outside the brief's step 3 list)

* `analysis/paper_a/long_term_and_measures.mjs` (`long_term_regions.csv`; its 2011 long-term count would read 35 over, 18 under, and the share 93%), `method_effects_by_region.py` (`method_status.csv`: A308 to A311), `regions_in_depth.py` and `make_readme_tables.py` read `-2` or earlier ids. Their values on `-3`, from the results files, are in section 9.
* `analysis/comparison_2025/movers.md` and `movers.csv` (B111's folder) carry `-2`'s populations; `movers-3.csv` sits in `analysis/paper_a`.
* ERRATA's "Corrected headline figures" table (on 52 regions, `2011-fixed`) was left as written, as B90 left it.
* Freezing `2011-fixed-3` and `2011-improved-3`, and making them Paper A's 2011 releases, is Murray's call (decision 100 implies it; the drafts and `analysis/paper_a/README.md` were not edited).
* Sources register rows to add for whoever applies them: D31 `used_by` gains `analysis/population_2011/zone_populations_2011.py` and `methods/zone-population-2011`; D44 notes gain "the 53 regional populations replaced by the ABS route in `2011-fixed-3` and `2011-improved-3` (ERRATA error 10)"; a defects row for error 10 (found by R02a and R02b, fixed in `-3`).
* The brief cites "decision 73 reasoning in R03a" for keeping the national row. Row 73 of `qa/DECISIONS.md` is the provenance audit scope; the reasoning applied is B90 decision 2 (keep the national row, a published input, as error 6 did), which R03a issue 1 carries. The module cites that.

## 9. Claim rows that move (register not edited)

"Before" is the register's value as it stands; where B90 proposed a change that the register does not carry, it is noted. "After" is on `2011-fixed-3` (and `2011-improved-3` for the tier rows).

**Tier A (for Murray)**

| Id | Tier | Before | After |
|---|---|---|---|
| A031 | A | 36 (`2011-fixed-2`) | **35** (`2011-fixed-3`): Northern and Yorke under capacity in 2011, long term |
| A033 | A | "23 to 16; 36 to 32" (B90 pending: "22 to 16; 36 to 32") | **"22 to 16; 35 to 32"** |
| A035 | A | 4 | **3** (Desert Channels, South West Qld, SA Arid Lands) |
| A039 | A | "1: South West Qld" ("One of the four long-term flips") | value holds; statement **"One of the three long-term flips"** |
| A165 | A | 82 (B90 pending: 81) | **82** (81.5%: the register value holds on `-3` and B90's pending change to 81 is withdrawn; a rounding edge) |
| A199 | A | "5 (2025); 1 (2011)" (B90 pending: "5 (2025); 2 (2011)") | **"5 (2025); 3 (2011)"**: Corangamite, North East Vic, Burnett Mary |

Tier A rows whose value holds on `-3`, locator release only: A002, A005, A163, A167, A171, A196 (national rows); A029 and A164 (22, as B90 proposed against the register's 23), A034 and A036 (as B90 proposed), A037, A038.

**Tier B and C**

| Id | Tier | Before | After |
|---|---|---|---|
| A040 | B | "3: Desert Channels; SA Arid Lands; Northern and Yorke" | "2: Desert Channels; SA Arid Lands" |
| A041 | B | "2: SA Arid Lands; Northern and Yorke" | "1: SA Arid Lands" |
| A042 | B | "short 3 and 3; long 3 and 2" | "short 3 and 3; long 2 and 1" |
| A043 | B | "6 against 2; 4 against 1" | "6 against 2; 3 against 1" |
| A057 | B | SA Arid Lands population "31 to 8 thousand" | "11 to 8 thousand" (10,613 to 8,049); capacity 2 to 28 and the flip hold |
| A067 | B | "31,361; 8,049" | value holds as a statement of the thesis model; the 2011 release `-3` uses 10,613 (wording) |
| A143 | B | 17 | 18 |
| A144 | B | 94 | 93 (93.4%; computed from `results/2011-fixed-3.csv`, script not rerun) |
| A151 | B | "13 published; 17; 21" | "13 published; 18; 21" |
| A168 | B | 24 | 25 |
| A169 | B | 84 | 85 |
| A172 | B | 27 | 26 |
| A173 | B | 87 | 88 |
| A176 | B | 33 | 32 |
| A177 | B | 92 | 91 |
| A197 | B | "81; 85; 91" | "81-82; 85; 91" (2011: 82, 85, 91; 2025: 81, 85, 91) |
| A308 | B | "22; 22; 21" | "22; 22; 20" (when `method_status.csv` is rerun on `-3`) |
| A309 | B | "Mackay Whitsunday" | "Desert Channels; Mackay Whitsunday" |
| A310 | B | "39; 36; 38" | "39; 35; 36" |
| A311 | B | "Western NSW; South East SA" | "South East SA" |

Hold: A056 (North Tasmania 143,631 reads 144 thousand), A145, A166, A170, A174, A178 (capacities), A328 (national), A048 (53 regions), A045 to A047 (C, descriptions; A047's "the test of an artefact is on capacity" holds, and the population input is like for like with 2025, which answers V32a's and the referees' concern without a fourth column). Paper text outside the register that moves: Table 1 long-term row (4 flips to 3), section 7.3 count (36 to 35), section 8 tipping sentence and shares.

**Register rows touched: none** (claims, sources, literature, defects).

## 10. Wrong-value check

Wrong-value check: the check "every region of `2011-fixed-3` carries the ABS figure of `zone_population_2011_comparison.csv`, both presets" (the same condition as in `compare_2_and_3.py`). Run on `results/2011-fixed-3.csv`: PASS. Run on a scratchpad copy in which Northern and Yorke's long-term population is **86,961 (an example, deliberately wrong; the true figure is 86,691)**: **FAIL** (`('45', 'long', '86961', 86691)`). The new test in `web/test/releases.test.js` also fails if any region's population differs from the ABS column, if any `2011-fixed-3` capacity differs from `2011-fixed-2`'s, or if the regions do not sum to 22,336,514.
