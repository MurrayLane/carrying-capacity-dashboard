# B90: North East Victoria's 2011 population (decision 84)

Brief: `qa/briefs/B90_ne_vic_population.md`. Finding traced: V32a problem 1. The claims register and the sources register were not edited. No frozen release was changed. No subagents. Network: abs.gov.au only, one request at a time, plain client string; six requests, none refused (two of them re-sent the same address to follow a redirect). One read-only `git diff --stat` was run by mistake; nothing was committed or staged.

## 1. The outcome in plain words

* **North East Victoria had about 98,600 people at 30 June 2011, not 204,651.** The 204,651 is Goulburn Broken's figure copied into the next row, and the infrastructure area (149 km2) was computed from the copy.
* **The copy is the author's, not the rebuild's.** It is in the earliest workbook that holds the regional populations and in every model after it, and the thesis prints it (Table 25, p. 382).
* **With the true figure North East Vic is under capacity in 2011 in the short term on every release** (published 99%, corrected 93% of capacity), so it is not a short-term flip between 2011 and 2025. The corrected-method story moves from nine short-term flips (three clean) to eight (two clean: Mackay Whitsunday and North Tasmania). North East Vic now tips over capacity at 1 in 10 in 2011 as well as in 2025.
* The correction went in as error 6 did: a data module in the corrections tier. Because `2011-fixed` and `2011-improved` are frozen, the module is applied in two new releases, `2011-fixed-2` and `2011-improved-2` (status current). Every published release stays as published.

## 2. The true figure and its source

| Route | Source | Figure |
|---|---|---|
| 1 (adopted) | ABS estimated resident population at 30 June 2011 by SA2, 2021 boundaries (sources register **D31**, `data/sa2/population_erp.csv`, column `2011`), allocated to the 2011 NRM zone exactly as `pipeline/land/land_2011_method.py` allocates the 2025 population (an SA2 that straddles the boundary is shared by residential land, CLUM class 5.4). Script `analysis/population_2011/ne_vic_population.py`; output `analysis/population_2011/zone_population_2011.csv`, row zone 22, column `erp_2011_sa2_route` | **98,604** |
| 2 (check) | ABS 3218.0 *Regional Population Growth, Australia, 2011*, released 31 July 2012, data cube `32180ds0002_2001-11.xls` (https://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&32180ds0002_2001-11.xls&3218.0&Data%20Cubes&B0858D4274744BADCA257A4B00147687&0&2011&31.07.2012&Latest, sha256 4d15b8213f89d9e1672e86802524a31a012ff017edc6825d8455119d3a5b934a, 838,656 bytes), sheet `Table 2` (Victoria), column `2011pr` (column Q), rows 551 to 564 (SA2s 21065 to 21075, Hume SA4) with 21082 Bruthen - Omeo and 21412 Moira in part, the shares of route 1 | **98,642** |

The two agree within 38 people (0.04%). Route 1 is adopted because it is the sources register's population source and the basis of the 2025 figure for the same zone (114,355), so 2011 and 2025 are like for like. The SA2s: Wangaratta 17,980, West Wodonga 14,749, Wodonga 14,743, Wangaratta Surrounds 8,809 (95% of it), Bright - Mount Beauty 7,849, Baranduda - Leneva 6,533, Towong 5,890, Myrtleford 4,560, Yackandandah 4,433, Beechworth 4,289, Rutherglen 3,739, Chiltern - Indigo Valley 2,907, and parts of Bruthen - Omeo (1,415) and Moira (704). Giving each straddling SA2 wholly to the zone that holds most of it gives 96,930 instead, so the allocation is worth under 2%.

**No ABS 2011 NRM population cube exists in the register, and none was found at the ABS.** The 3218.0 releases for 2009-10 and 2011 offer cubes by SA2, LGA, SLA, SD, remoteness area and electoral division, none by NRM region (pages read: https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/3218.02009-10?OpenDocument and https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/3218.02011?OpenDocument). The National Regional Profile 2006-2010 page (https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1379.0.55.0012006-2010?OpenDocument) redirects to the ABS home page. The thesis says the regional populations were "sourced predominantly from journal articles" (section 8.5, p. 221, footnote 912: Robins and Dovers 2007, *Geographical Research* 45(3), pp. 280-281); that article's table (archive `references re production yields/Non-food/Robins - NRMs.pdf`) gives rounded figures, about 200,000 for North East and 189,500 for Goulburn Broken, and neither is 204,651.

## 3. Where the copy came from

| Place | Cells | Goulburn Broken | North East Vic |
|---|---|---|---|
| Archive `Yield data/NRM - Landuse.xls` (the author's land-use workbook, the earliest holder), sheet `xSummary` | Y20 / Y23 (population), F20 / F23 (built-on land) | 204,651; 149 | 204,651; 149 |
| Archive `superceded/Carrying capacity dashboard model 050412.xls` (an April 2012 model version) | Settings X25 / AA25 | 204,651 | 204,651 |
| Archive `Models/Carrying capacity dashboard model 021012.xls` (the October 2012 model) | Settings T133 / W133 | 204,651 | 204,651 |
| Archive `Models/Lane_Dashboard_model.xls` | Defaults U26 / X26 | 204,651 | 204,651 |
| Archive `Results/1a.xls` to `39b.xls` (thesis runs) | Defaults T25 / W25 | 204,651 | 204,651 |
| Thesis, Table 25, p. 382 (PDF page 382 of `Papers and manuscripts/Lane-2014-PhD-thesis-QUT-eprint-67485.pdf`) | rows 19 and 22 | 204,651; infrastructure 149 | 204,651; infrastructure 149 |
| Rebuild: `data/2011/default-inputs-*.csv` (copied from the QUT snapshot) and `baseline/baseline_2011.csv` (the original servlet's output) | zone 22 | 204,651 | 204,651 |

Every `.xls` workbook in the archive was scanned: every one that holds the regional populations has the copy, and none has a different value for North East Vic. **So the thesis itself carried the copy, and the rebuild inherited it.** Thesis Table 16 (p. 280) has no region rows and its capacities do not depend on population, so Table 16 is unaffected; Table 25 and what is built on it (population density, population against capacity) are. Every zone's infrastructure in the 2011 inputs equals population times 730 m2 (checked for all 60), which is why the infrastructure area was copied too.

**A second copy of the same kind:** Fitzroy (zone 33) and Wet Tropics (zone 39) share 230,982 and 169 km2 of infrastructure, in the same cells of the same workbooks. The ABS figures are 235,629 and 246,885; no status changes on any 2011 release with either. Logged as ERRATA error 9, not corrected (outside decision 84).

## 4. The correction

Following error 6: a data module in the corrections tier, generated by its script, with the published releases kept as published.

* `methods/north-east-vic-population/method.json` (new; written by `analysis/population_2011/ne_vic_population.py`): `zoneInputs` for zone 22: population 98,604, infrastructure 72 km2 (98,604 x 730 m2), non-agricultural land 3,034 km2 (the remainder; total area unchanged at 20,234 km2).
* `web/scripts/build-data.mjs`: reads `zoneInputs` from a release's modules and applies them before `statePopulationsFromRegions`, so Victoria's population (the sum of its regions in this tier) falls by the same 106,047. No change to `web/src/model/` (the evaluator is untouched).
* `releases/2011-fixed-2/release.json` and `releases/2011-improved-2/release.json` (new, status current): extend the frozen `2011-fixed` and `2011-improved` with the one module. They are not locked; freezing them is a decision for the gate.
* `releases/index.json`: the two ids added after `2011-improved`.
* `2011`, `2011-thesis`, `2011-corrected`, `2011-fixed`, `2011-improved`: untouched; `npm test` confirms their locks. `baseline/baseline_2011.csv` is untouched: it is the original servlet's output, a record of what was published.
* The national row is left at 22,326,388, as error 6 left it. It is the sum of the regions with the copy; with the ABS figure the 53 regions sum to 22,220,341. Whether to change it is a decision (section 9).

Effect on the new releases (checked zone by zone against the parents, `results/2011-fixed-2.csv`, `results/2011-improved-2.csv`):

| Release | Zone | Population | Capacity | Population over capacity |
|---|---|---|---|---|
| 2011-fixed to 2011-fixed-2 | North East Vic short | 204,651 to 98,604 | 105,525 (unchanged) | 194% to 93%: over to **under** |
| | North East Vic long | 204,651 to 98,604 | 9,476 (unchanged) | 2,160% to 1,041%: over |
| | Victoria short / long | 5,545,932 to 5,439,885 | unchanged | 104% to 102% / 689% to 676%: over |
| 2011-improved to 2011-improved-2 | North East Vic short | 204,651 to 98,604 | 110,288 to 109,339 (the infrastructure area under reserve-pro-rata) | 186% to 90%: over to **under** |
| | North East Vic long | 204,651 to 98,604 | 8,099 (unchanged) | over |
| | Victoria | 5,545,932 to 5,439,885 | unchanged | short under, long over (unchanged) |

No other zone, field or workbook cell differs; every capacity of `2011-fixed-2` equals `2011-fixed`'s (new test in `web/test/releases.test.js`).

## 5. What was run, with hashes

1. `python3 -I analysis/population_2011/ne_vic_population.py <the 3218.0 cube>` (repository root): wrote the module and `zone_population_2011.csv`.
2. `cd web && npm run build:data`: rebuilt `web/public/data/` for every release (the two new folders added; the build refuses any frozen release whose inputs changed, and none had).
3. `cd web && node scripts/make-results.mjs 2011-fixed-2 2011-improved-2`: the documented subset form of `npm run results`. It wrote the two new results files, rewrote `results/comparison_cells.csv` from the existing files (byte-identical afterwards) and `results/releases.json`. **The full `npm run results` was not run**: it would also regenerate `method_effects.csv`, `scenarios.csv` and `scale_curve.csv`, which do not read the new releases and which B91 is working on.
4. `python3 -I analysis/paper_a/regional_flips.py`; `node analysis/paper_a/shocks_by_region.mjs analysis/paper_a/shocks_by_region.csv`; `python3 -I analysis/paper_a/shocks_summary.py`.
5. `cd web && node --test test/*.test.js`: 33 of 33 pass (32 before plus the new one).

| File | sha256 before | sha256 after |
|---|---|---|
| `results/2011-fixed-2.csv` | (new) | c8dea311ed28e0226f914d9d1f004ae508ebe11aa4910b77315f30656a84cb10 |
| `results/2011-improved-2.csv` | (new) | 33e047310ddedd90f806f1f6b2321e119b5c66ab10147fa6ddf77929575ff497 |
| `results/releases.json` | 0ca091739974e5392a49a5d8edc2674c7974bbc970a02ae6c34e654f4d113de9 | b4ad2d5d837397945072dc2666b6cf91d463792158bbebf63e5f7af796f32a17 |
| `results/comparison_cells.csv` | unchanged | unchanged |
| `analysis/comparison_2025/movers.csv` | 56f159c208fa4b2a94e6fca7220a7eefa1eabd20eeb2ac3ecef75434ff56777a | dec71f5d8d955386a862f95febef1c8226376e915f870b64a257d681a793e5a6 |
| `analysis/paper_a/regional_flips.csv` | b1cd3b39e72b7e068761f9c4fc34bd4fc47f59cfd955af38b2acc6ca3a639566 | 052a3b2d4c1b443b65bdf761d8bd9bad6b2d99cf0e67f55ed41d0f07958a1503 |
| `analysis/paper_a/shocks_by_region.csv` | 94637fb615a6578052a10d7ac52ee55037a95f3acdd31f6532bcef25b0d53565 | 00e9eaf128020fa317c61e585058222cdafcef5ea936ba043fcdab2efd22f980 |
| `analysis/paper_a/shocks_summary.csv` | ab95b6cfb152eb6090ea6f1cabd35485cae5f90e58f189edebc63074d4dfde29 | 0446002fac2217a64a0b62025620858e1d7e03cacff9cf8d8e0114a8b3ed5535 |
| `analysis/paper_a/scenarios_by_region.csv` (also written by `shocks_summary.py`) | unchanged | unchanged (byte-identical) |

`results/releases.json` gains the two new releases; it also now records the store releases `2025-store-1` and `2025-store-2` as frozen with new regions hashes, which is B91's concurrent work read from disk at the time of the run, not a change of mine.

## 6. Every file changed

| File | Change |
|---|---|
| `analysis/population_2011/ne_vic_population.py` | new: the trace (two routes) and the module generator |
| `analysis/population_2011/zone_population_2011.csv` | new: every zone's 2011 default population against the ABS 2011 figure, and which zones share a population |
| `methods/north-east-vic-population/method.json` | new module (generated) |
| `methods/README.md` | one row added to the module table |
| `web/scripts/build-data.mjs` | `zoneInputs` applied before the state sums (5 lines) |
| `web/test/releases.test.js` | one test appended (the new releases differ from their parents only as intended; the 2011-fixed capacities do not move) |
| `releases/2011-fixed-2/release.json`, `releases/2011-improved-2/release.json` | new releases, status current |
| `releases/index.json` | two ids added |
| `results/2011-fixed-2.csv`, `results/2011-improved-2.csv` | new (generated) |
| `results/releases.json` | regenerated (two releases added) |
| `analysis/comparison_2025/movers.csv` | zone 22 rows: `pop2011` 204651 to 98604, `dpop` -90296 to 15751, `ratio2011` short 0.52 to 1.07 and long 0.05 to 0.1, `over2011` short 1 to 0 (long stays 1). Capacities unchanged |
| `analysis/comparison_2025/movers.md` | one note under the source line saying the zone 22 rows carry `2011-fixed-2`'s population and that the text below predates the correction |
| `analysis/paper_a/regional_flips.py` | docstring only (says where zone 22's population comes from) |
| `analysis/paper_a/regional_flips.csv` | zone 22 short: population 2011 204651 to 98604, over 2011 1 to 0, flip "over to under" to blank, clean and robust "yes" to blank; zone 22 long: population 2011 to 98604 (status unchanged) |
| `analysis/paper_a/shocks_by_region.mjs` | reads `2011-fixed-2` instead of `2011-fixed` (comment says why) |
| `analysis/paper_a/shocks_by_region.csv` | the 324 rows of 2011 now say `2011-fixed-2`; zone 22's six rows population 204651 to 98604; every capacity and every 2025 row unchanged |
| `analysis/paper_a/shocks_summary.py` | reads `2011-fixed-2` instead of `2011-fixed` (comment says why) |
| `analysis/paper_a/shocks_summary.csv` | 2011 rows renamed `2011-fixed-2`; return period 1: regions over capacity 23 to 22, share of population in over-capacity regions 82% to 81%; every other cell unchanged |
| `ERRATA.md` | errors 8 and 9 added to the table |
| `qa/reports/B90_ne_vic_population.md` | this report |

Changed on disk during the job but **not by me** (concurrent builder): `analysis/paper_a/README.md`, `results/README.md`.

## 7. The dependent analyses: before and after

| Measure (corrected method, 2011, 53 regions) | Before (`2011-fixed`) | After (`2011-fixed-2`) |
|---|---|---|
| Regions over capacity, short term | 23 | **22** |
| Regions over capacity, long term | 36 | 36 |
| Short-term flips 2011 to 2025 | 9 (8 over to under, 1 under to over) | **8 (7 over to under, 1 under to over)** |
| Clean and robust short-term flips | 3: Mackay Whitsunday, North Tasmania, North East Vic | **2: Mackay Whitsunday, North Tasmania** |
| Long-term flips; clean | 4; 1 (South West Qld) | 4; 1 (unchanged) |
| Net fall short term against clean flips | 7 against 3 | **6 against 2** |
| Share of population in over-capacity regions, average year | 82% | **81%** |
| Regions under capacity in an average year and over at 1 in 10 | 2011: 1 (Corangamite); 2025: 5 | **2011: 2 (Corangamite, North East Vic)**; 2025: 5 (unchanged) |
| The same at 1 in 20 | 2011: 4 (Burnett Mary, Corangamite, Lower Murray Darling, Murrumbidgee - ACT); 2025: 8 | **2011: 5 (the four and North East Vic)**; 2025: 8 (unchanged) |
| Regions over capacity at 1 in 5, 10, 20, 50, 100 (2011) | 23, 24, 27, 32, 33 | unchanged |
| Population shares at 1 in 5 to 1 in 100 (2011) | 82, 84, 87, 91, 92% | unchanged |
| National figures (capacity, population, ratios, regional sums) | | unchanged |

**Not rerun, so still carrying 204,651 for zone 22 (follow-ups):**
* `analysis/paper_a/long_term_and_measures.mjs` (`long_term_regions.csv`): not run because the same script writes `measures.csv`, which B91 owns. Checked by hand: the 2011 long-term count (36 over, 17 under) and the 94% share do not change.
* `analysis/paper_a/method_effects_by_region.py` (`method_effects_by_region.csv`, `method_status.csv`): reads `2011-fixed` and `2011-improved`. If switched to the new releases, the 2011 short-term over-capacity counts by tier (published, corrected, improved) go from 22, 23, 22 to 22, 22, 21 (claim A308), and the 2011 population column of zone 22 changes; the published tier stays at 22 because `2011-corrected` keeps the copy.
* `analysis/paper_a/regions_in_depth.py`: none of its seven regions is North East Vic, but its cross-checks compare `movers.csv` and `regional_flips.csv` with `results/2011-fixed.csv` and would now report the zone 22 rows as disagreements, and it looks up `shocks_by_region.csv` by the release id `2011-fixed`, which is now `2011-fixed-2`; it needs the same one-word switch before its next run. Its outputs were not touched.
* `analysis/paper_a/make_readme_tables.py`: its shocks table reads `shocks_summary.csv` by the id `2011-fixed`; same switch needed. `analysis/paper_a/README.md` prose (flips table, section 8) and the Paper A drafts were not edited (claim wording is B95's).
* `analysis/comparison_2025/decompose_corrected.mjs`, `make_cells.py`, `results/comparison_cells.csv`, `method_effects.csv`, `scale_curve.csv`: capacity-only or national, or on the published releases; left as they were. `scale_curve.csv`'s 2011-fixed and 2011-improved state rows use Victoria's population and would move by 106,047 if switched; capacities would not.
* ERRATA's "Corrected headline figures" table (regions over capacity 21 / 38 published, 22 / 35 corrected, on 52 regions) is one lower in the short term in both columns with the true figure; left as written, noted here.

## 8. Claim rows whose value or statement changes

Nothing in `qa/claims_register.csv` was changed.

**Tier A: not changed; for Murray**

| Id | Before | After |
|---|---|---|
| A029 | 23 of the 53 regions are over capacity in 2011, short term, corrected method (value 23) | 22 (release `2011-fixed-2`) |
| A033 | Regions over capacity fall from 23 to 16 in the short term and from 36 to 32 in the long term ("23 to 16; 36 to 32") | "22 to 16; 36 to 32" |
| A034 | Nine regions change status in the short term: eight over to under, one under to over ("9 (8 over to under, 1 under to over)") | "8 (7 over to under, 1 under to over)": North East Vic is under capacity at both dates |
| A036 | Three of the nine short-term flips are clean and robust: Mackay Whitsunday, North Tasmania and North East Victoria | Two of the eight: Mackay Whitsunday and North Tasmania |
| A164 | In an average year in 2011, 23 of 53 regions are over capacity (23) | 22 (`shocks_summary.csv`, release `2011-fixed-2`, return period 1) |
| A165 | In an average year in 2011, 82% of the population lives in over-capacity regions (82) | 81 |
| A199 | Five regions tip at 1 in 10 in 2025, "against one in 2011 (Corangamite)" ("5 (2025); 1 (2011)") | "5 (2025); 2 (2011)": Corangamite and North East Vic; North East Vic tips at 1 in 10 in both years |

Tier A rows whose value holds but whose locator or release names `2011-fixed` where the output now says `2011-fixed-2`: A031, A035, A039 (`regional_flips.csv`, values unchanged), A163, A167, A171, A196 (`shocks_summary.csv` rows renamed, values unchanged). A037 and A038 hold (three artefacts, three not robust).

**Tier B and C: listed, not changed (B95 applies after V33)**

| Id | Tier | Before | After |
|---|---|---|---|
| A043 | B | net fall "7 against 3; 4 against 1" | "6 against 2; 4 against 1" |
| A197 | B | "81-82; 85; 91" ("81% to 82%" in an average year) | "81; 85; 91" (81% in both years) |
| A308 | B | "22; 23; 22" (2011 short, published, corrected, improved) | "22; 22; 21" once `method_status.csv` is rerun on the new releases (not rerun here) |
| A047 | C | "The test of an artefact is on capacity, not on whether the population change is real" | value unchanged; V32a asked for a population-input check in the flip classification, which this job did not add |
| A168 to A178 | B | 2011 rows at 1 in 5 to 1 in 100 | values unchanged; locator release `2011-fixed` is now `2011-fixed-2` |
| A043, A042, A045, A046, A048, A056 | B, C | | values unchanged (A056 depends on A036 but its own figures hold) |

Paper text outside the register that moves (for B95 and the section scopes): section 3 and the headline (nine flips, three clean), section 8 ("five tip at 1 in 10 in 2025 against one in 2011"), section 10 and section 12 point 6 where they use North East Vic as a flip (V32a problem 1), `analysis/comparison_2025/movers.md` "Status flips" line, `qa/reports/digest_2026-11-09.md` item 5.

## 9. Registers and decisions

* **Register rows touched: none** (claims, sources, literature, defects).
* Rows to add, for whoever applies them: a sources-register row for the ABS 3218.0 2011 SA2 cube (route 2; URL and sha256 in section 2; the file is in the session scratchpad only and is not stored in either repository); D31's `used_by` gains `analysis/population_2011/ne_vic_population.py`; D44's notes gain "zone 22 population and infrastructure are a copy of zone 19's (ERRATA error 8); zones 33 and 39 share a population (error 9)"; a defects row for the copy (layer 1, data, found by V32a, fixed in `2011-fixed-2`).
* Decisions for Murray (numbered; recommendation first):

| # | Decision | Recommended | Confidence | Cost | Reason |
|---|---|---|---|---|---|
| 1 | Use `2011-fixed-2` in place of `2011-fixed` as Paper A's 2011 corrected release (and `2011-improved-2` for the improved tier), and freeze them | Yes | High | small builder job (switch the remaining scripts in section 7, lock, rerun) | The frozen releases keep the copy; the new ones differ only in this zone and Victoria's population |
| 2 | Set the national 2011 population to the sum of the regions (22,326,388 to 22,220,341) | No: keep the national row, as error 6 did | Medium | none | The national row is a published input; at one decimal it reads 22.2 instead of 22.3 million and moves Tier A rows A002 (22.3 to 22.2) and A005 (1.49 to 1.50) and Tier B row A328 (population growth +23.7% to +24.2%) |
| 3 | Correct Fitzroy and Wet Tropics (error 9) | Record only | Medium | none | Which zone carries the copy is not settled, and no status changes with either ABS figure |
| 4 | Accept the Tier A changes in section 8 | Yes | High | B95 applies | Two ABS routes agree within 38 people |

Reply "yes" to take all recommendations.

## 10. Wrong-value check

Wrong-value check: a check of the module's population against both ABS routes (pass when within 50 of route 1, within 100 of route 2, and not 204,651). Run on the module: 98,604 against 98,604 and 98,642, pass. Run on **89,604 (an example, deliberately wrong)**: FAIL. The new test in `web/test/releases.test.js` also fails if the module's population is anything but 98,604 or if any `2011-fixed-2` capacity differs from `2011-fixed`'s.
