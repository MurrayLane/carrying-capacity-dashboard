# V36: blind check of B110 (every 2011 zone population on the ABS footing)

Brief: `qa/briefs/V36_check_B110.md`; rules `qa/briefs/_checker_rules_results_wave.md`. Builder's brief `qa/briefs/B110_zone_populations_2011.md`; builder's report `qa/reports/B110_zone_populations_2011.md`. No git, no subagents, no network. This file is the only repository file written; my scripts and outputs are in my scratch folder.

**Verdict: every number checked holds.** 2,110 cell checks against the builder's files, 0 mismatches; every headline count, share, flip and tipping list in the report agrees with my own derivation. Three remarks, none of which changes a number: the release status on disk differs from what the report and ERRATA error 10 say; one ERRATA phrase needs its base stated; the 1-in-100 share sits on a rounding edge if the denominator were the national row.

## 1. Tolerance (fixed before comparing)

* Populations, counts, names, status flags and flip labels: exact.
* Capacities: within 0.5% (in practice I required 1 person on the corrected method, where nothing should move).
* Shares and percentages: within one unit of the last printed digit.
* Rounding to whole people: half up (as the module does). A first pass of mine rounded a 2-decimal copy with Python's half-even rule and flagged Corangamite (371,118 against 371,119). The exact value is 371,118.5007, so 371,119 is right; the flag came from my rounding, not the builder's.

## 2. Wrong-value check

Example, deliberately wrong: I set Burnett Mary's 2011 population in my own figures to 296,812 (its `-2` figure; the true ABS-route value is 309,314) and reran the comparison. Result: 9 mismatches (the ABS column of `zone_population_2011.csv`, the comparison table's ABS, difference and percent cells, the module's population, infrastructure (217 against 226) and non-agricultural land, and the population cell of both `-3` results files). Fed through the evaluator, the same wrong value gives 24 regions over capacity at 1 in 10 instead of 25. The check can fail. With the correct value: 0 mismatches.

## 3. My route and my figures

1. **Populations.** Own script (`alloc.py`): ABS ERP at 30 June 2011 by SA2 (`data/sa2/population_erp.csv`, register D31), each SA2 shared among the 2011 zones through `data/nrm2011/land_use_by_sa2_nrm2011_piece.csv` by residential land (CLUM 5.4), by area where an SA2 has none, NRM codes merged into zones by `pipeline/land/zone_to_nrm2011.json`. The same script with year 2025 reproduces the stored 2025 zone populations (`data/nrm2011/land_2011_method_zones.csv`) with a largest difference of 0.0 people, so it is the 2025 build's allocation. Four SA2s outside the zones (3,120 people in 2011) drop out, as in 2025.
2. **Release.** Own script (`evalmine.mjs`): `2011-fixed-2` and `2011-improved-2` as built, each region's population set to my figure, infrastructure = round(population x 730 m2) in km2, non-agricultural land = old non-agricultural + old infrastructure - new infrastructure, each state = sum of its regions, national row kept. Evaluated with `web/src/model/evaluator.js` for all 60 zones, both presets, and the short-term preset at return periods 1, 5, 10, 20, 50, 100 (the `resilience` input; with no change this reproduces all 324 rows of `-2`'s `shocks_by_region.csv` and all 120 cells of `results/2011-fixed-2.csv` exactly).
3. **Counts.** Own script (`counts.py`): the 53 regions are the 52 of kind `region` plus zone 60 (NT). Over capacity = population > capacity. Share = population of over-capacity regions / population of the 53 regions (this reproduces `-2`'s 81% and 84, 87, 91, 92%). Flips against `results/2025-fixed.csv`. The artefact and range flags are per zone and rest on capacity and the 2025 range only, so I took them from the unchanged `-2` `regional_flips.csv`.

**Zone populations (ABS route).** The 53 regions sum to **22,336,514** (`2011-fixed-2`: 22,220,341; national row 22,326,388, so the regions sum to 10,126 more). States: NSW-ACT 7,586,092; Victoria 5,537,815; Queensland 4,476,810; South Australia 1,639,287; Western Australia 2,353,409; Tasmania 511,483; NT 231,618. Selected regions: North East Vic 98,604; Fitzroy 235,629; Wet Tropics 246,885; Northern and Yorke 86,691; Burnett Mary 309,314; Western NSW 12,470; SA Arid Lands 10,613; North Tasmania 143,631. Against the release, 23 of the 52 regions other than North East Vic differ by more than 10% of the ABS figure (22 if measured against the release figure) and 12 lie outside 0.8 to 1.25 times it (the same 12 names as the builder, ratios equal to three decimals); Glenelg Hopkins 0.805 and South West WA 0.807 are inside.

**Corrected method, `-2` (reproduced) and `-3` (mine).**

| Measure | -2 | -3 (mine) |
|---|---|---|
| Over capacity 2011, short / long | 22 / 36 | 22 / 35 |
| Status changes, short / long | | none / Northern and Yorke over to under (86,691 against 89,933) |
| Short-term flips; clean | 8; 2 | 8 (7 over to under, Corangamite under to over); 2 (Mackay Whitsunday, North Tasmania) |
| Long-term flips; clean | 4; 1 | 3 (Desert Channels, South West Qld, SA Arid Lands); 1 (South West Qld) |
| Long-term flips with artefact flag; not robust | 3; 2 | 2; 1 |
| Share in over-capacity regions, average year | 81.33% | 81.55% |
| Share, long term | 93.73% | 93.41% |
| Over capacity at 1 in 5, 10, 20, 50, 100 | 23, 24, 27, 32, 33 | 23, 25, 26, 30, 32 |
| Share at 1 in 5, 10, 20, 50, 100 | 81.8, 83.5, 87.4, 91.3, 92.2% | 82.0, 85.0, 87.7, 89.9, 91.5% (91.48) |
| Under in an average year, over at 1 in 10 | 2: Corangamite, North East Vic | 3: + Burnett Mary (309,314 against 298,088) |
| The same at 1 in 20 | 5: Lower Murray Darling, Murrumbidgee - ACT, Corangamite, North East Vic, Burnett Mary | 4: Lower Murray Darling leaves (28,081 against 30,456) |
| Capacity cells differing from -2 | | 0 of 120 (0 of 420 with the drought runs) |

Other drought status changes on `-3`: 1 in 50 Burdekin over to under (230,763 against 231,658) and Northern and Yorke over to under; 1 in 100 Condamine and Northern and Yorke over to under, SA Murray Darling Basin under to over (118,534 against 111,565).

**Improved method.** Short term 21 to 20 over (Desert Channels under: 12,247 against 14,748); long term 38 to 36 (Western NSW 12,470 against 35,040; Northern and Yorke 86,691 against 111,711). Capacities move in 75 of 120 cells, at most 0.94% (Port Phillip and Westernport long term, 10,310 to 10,407), through `reserve-pro-rata`. Regions differing between the corrected and improved method, 2011: short term Desert Channels and Mackay Whitsunday; long term South East SA.

## 4. Comparison with the builder

| Item | Builder | Mine | Result |
|---|---|---|---|
| ABS column, `zone_population_2011.csv` (53 rows) | file | my allocation | pass (all exact) |
| `zone_population_2011_comparison.csv`: release, ABS, difference, percent (53 rows) | file | mine | pass (all exact; percent within 0.1) |
| Module `zone-population-2011`: population, infrastr1, nonAg (53 zones) | file | mine | pass (all exact) |
| `results/2011-fixed-3.csv`: population, capacity, over flag (120 cells) | file | evaluator | pass |
| `results/2011-improved-3.csv` (120 cells) | file | evaluator | pass |
| `shocks_by_region-3.csv`, 2011 rows (324) | file | evaluator | pass; 2025 rows identical to `-2` |
| `regional_flips-3.csv` (106 rows): population, over 2011, flip | file | mine | pass; only Northern and Yorke long differs from `-2` |
| `shocks_summary-3.csv`, 2011 rows: counts, shares, sums | 22, 23, 25, 26, 30, 32; 82, 82, 85, 88, 90, 91% | same | pass |
| 53-region total | 22,336,514 | 22,336,514 | pass |
| Regions minus national row | 10,126 | 10,126 | pass |
| Seven state populations | as in section 3 of report | same | pass |
| Over 2011 short / long | 22 / 35 | 22 / 35 | pass |
| Flips short; clean | 8; 2 | 8; 2 | pass |
| Flips long; clean | 3; 1 | 3; 1 | pass |
| Long artefacts; not robust | 2; 1 | 2; 1 | pass |
| Net fall against clean flips | 6 against 2; 3 against 1 | same | pass |
| Share, average year | 81.5% (prints 82) | 81.55% | pass |
| Share, long term | 93.4% | 93.41% | pass |
| Tipping at 1 in 10 | 3 (Corangamite, North East Vic, Burnett Mary) | same | pass |
| Tipping at 1 in 20 | 4 (Lower Murray Darling leaves) | same | pass |
| Every drought status change listed | Burnett Mary, Lower Murray Darling, Burdekin, Condamine, Northern and Yorke, SA Murray Darling Basin with figures | same, figures equal | pass |
| Fixed capacities equal `-2` | 120 of 120 | 120 of 120 | pass |
| Improved: cells moving; largest | 75 of 120; 0.9% (PPW long 10,310 to 10,407) | 75; 0.94%, same cell | pass |
| Improved over counts | 21 to 20; 38 to 36 | same | pass |
| Corrected against improved differences | short Desert Channels, Mackay Whitsunday; long South East SA | same | pass |
| 23 differ by over 10%; 12 outside 0.8 to 1.25; names and ratios | as stated | same (on the ABS-figure base) | pass |
| Largest absolute: HNS -321,475 (-7.3%), Hunter +265,889 (+26.4%), PPW -119,829 (-2.8%); Fitzroy -2.0%, Wet Tropics -6.4% | as stated | same | pass |
| R03a correction (Glenelg Hopkins 0.805, South West WA 0.807 are inside the band) | as stated | same | pass |
| Release status "current, not locked" | report and ERRATA error 10 | on disk both `-3` release.json files read `"status": "frozen"` with an `inputs` hash block, dated after the report; their sha256 differs from the report's table (f563d8d0... and 768d693f...) | note, no number moves |

## 5. Claim rows the builder says move

| Id | Builder's after | Mine | Verdict |
|---|---|---|---|
| A031 | 35 | 35 | holds |
| A033 | "22 to 16; 35 to 32" | 22 to 16; 35 to 32 | holds |
| A035 | 3 | 3 | holds |
| A039 | one of the three long-term flips: South West Qld | same | holds |
| A165 | 82 (81.5%) | 81.55% | holds; a rounding edge, as the builder says |
| A199 | "5 (2025); 3 (2011)": Corangamite, North East Vic, Burnett Mary | 3, same names | holds; the sentence must change from "against one in 2011 (Corangamite)" |
| A040 | 2: Desert Channels; SA Arid Lands | same | holds |
| A041 | 1: SA Arid Lands | same | holds |
| A042 | short 3 and 3; long 2 and 1 | same | holds |
| A043 | 6 against 2; 3 against 1 | same | holds |
| A057 | population 11 to 8 thousand (10,613 to 8,049) | 10,613 | holds |
| A067 | wording only | 10,613 on `-3` | holds |
| A143 | 18 | 53 - 35 = 18 | holds |
| A144 | 93 | 93.41% | holds |
| A151 | 13 published; 18; 21 | 18; 2025 long under 21 | holds |
| A168 / A169 | 25 / 85 | 25 / 85.0% | holds |
| A172 / A173 | 26 / 88 | 26 / 87.7% | holds |
| A176 / A177 | 32 / 91 | 32 / 91.48% | holds |
| A197 | "81-82; 85; 91" | 2011: 82, 85, 91; 2025: 81, 85, 91 | holds; the phrase "(81%) in both vintages" needs the builder's rewording |
| A308 | 22; 22; 20 | corrected 22, improved 20 | holds (the published value not rechecked here) |
| A309 | Desert Channels; Mackay Whitsunday | same | holds |
| A310 | 39; 35; 36 | corrected 35, improved 36 | holds (published value not rechecked) |
| A311 | South East SA | same | holds |
| Rows held (A029, A164 at 22; A034 at 8 flips; A036 at 2 clean; A037, A038 at 3; A056 North Tasmania 143,631; national rows) | hold | same on `-3` | holds |

The proposed sentences say no more than the figures support. Two cautions for the paper text: A165 and the 1-in-100 share are rounding-edge figures (81.55% prints 82; 91.48% prints 91), so "about 82%" and "about 91%" are safer than a precise-looking integer.

## 6. Method: what I would do differently, and whether it changes a number

* **Share denominator.** Builder and `-2` divide by the 53 regions' population. Divided by the national row (22,326,388) the shares are 81.6, 85.1, 87.8, 90.0 and 91.5% (1 in 100: 91.52, which prints 92, not 91). The builder's choice matches the `-2` outputs, so it is the right like-for-like; no number changes under the stated method. Worth one line in the paper that the share is of the regions' population.
* **ERRATA error 10 wording.** "23 of the 52 zones ... differ by more than 10%" holds when the difference is taken as a share of the ABS figure; as a share of the release figure it is 22. Suggest "by more than 10% of the ABS figure". No number changes.
* **Infrastructure rounding.** Rounding infrastructure to whole km2 (as `north-east-vic-population` does) matters only on the improved method, by at most a few people of capacity. Same choice as mine; no change.
* **Flags reused.** Artefact and range flags rest on capacity and the 2025 range, which population does not move; the builder's `regional_flips-3.csv` has the same flags as `-2` in every row. No change.
* **Release status.** The report and ERRATA error 10 say `2011-fixed-3` and `2011-improved-3` are status current and not locked; on disk both are frozen with an inputs block, written after the report. Either the ERRATA and report wording or the release files should be brought into line by whoever froze them. No number changes.

## 7. Register rows touched

None. `qa/claims_register.csv`, `qa/sources_register.csv` and every other register were read only.

## 8. Rerun

From the repository root, with `S` the scratch folder:

```
python3 -I $S/alloc.py 2011            # writes $S/zone_pop_2011.csv (run from $S)
node $S/evalmine.mjs 2011-fixed-2 $S/base_fixed2.csv none
node $S/evalmine.mjs 2011-fixed-2 $S/mine_fixed3.csv $S/zone_pop_2011.csv
node $S/evalmine.mjs 2011-improved-2 $S/base_improved2.csv none
node $S/evalmine.mjs 2011-improved-2 $S/mine_improved3.csv $S/zone_pop_2011.csv
python3 -I $S/counts.py $S/mine_fixed3.csv
python3 -I $S/compare.py               # (run from $S) 2,110 checks, 0 fail
python3 -I $S/compare.py WRONG         # the deliberate wrong value: 9 fail
```

Files read: the two briefs and the rules file; `data/sa2/population_erp.csv`, `data/sa2/clum_classes.csv`, `data/nrm2011/*.csv`, `pipeline/land/land_2011_method.py`, `pipeline/land/zone_to_nrm2011.json`; `web/scripts/build-data.mjs` (zone inputs step), `methods/north-east-vic-population/method.json`, `web/public/data/2011-fixed-2|2011-improved-2/*.json`, `web/src/model/evaluator.js`, `analysis/sensitivity_2025/evaluate.mjs`; `results/2025-fixed.csv`, `results/2011-fixed-2.csv`; `analysis/paper_a/regional_flips.csv`, `shocks_by_region.csv`, `shocks_summary.csv`, README section 3; register rows D31, D47, D51 and the claim rows above. Last: the builder's report, `zone_population_2011*.csv`, the module, the `-3` results, release files and paper_a outputs, ERRATA errors 8 to 10.
