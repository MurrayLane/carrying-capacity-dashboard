# V33 checker report: North East Victoria's 2011 population (decision 84, builder B90)

Brief: `qa/briefs/V33_ne_vic_check.md`, with `qa/briefs/_checker_rules_results_wave.md`. No git, no subagents, no network. My scripts sit outside the repository (session scratchpad, folder `v33`); this report is the only file written in the repository. Nothing else was edited.

## 1. Tolerance (set before comparing)

* Counts, names, flip lists and statuses: must match exactly.
* Populations: must match to the person.
* Capacities: within 0.5%.
* Shares and ratios: within one unit of the last printed digit.

## 2. Wrong values fed to my own code

1. **Population 89,604 for North East Vic** (`NE_POP=89604`). My comparison then reported 4 mismatching rows in `results/2011-fixed-2.csv` (zone 22 short and long, Victoria short and long, e.g. "98604 against mine 89604") and 4 in `results/2011-improved-2.csv`. Note: the regional count alone would not have caught this one (still 22 over in the short term), which is why every cell is compared, not only the counts.
2. **Capacity 90,000 for North East Vic short term** (`INJECT=22:short=90000`). My code then reported North East Vic "over" and 23 regions over in the short term, against 22 in the release.

Both runs were discarded and the correct run restored; the comparison on the restored run shows 0 mismatches.

## 3. My own figures (derived before opening B90's report or the changed files)

### 3.1 Population at 30 June 2011

Source: sources register **D31**, ABS estimated resident population by SA2 (2021 boundaries), `data/sa2/population_erp.csv`, column `2011`. No ABS 2011 population by NRM region is in the register, so the SA2 route is the one available. SA2s are allocated to the 2011 NRM zones with the SA2-by-zone pieces of `data/nrm2011/land_use_by_sa2_nrm2011_piece.csv`. An SA2 that straddles a zone boundary is shared by its residential land (CLUM classes 540 to 545), with area as the fallback where an SA2 has no residential land. I also ran two other allocations to see how much the choice matters.

| Zone | Residential land (adopted) | Shared by area | Whole SA2 to the zone holding most of it | 2011 default input |
|---|---|---|---|---|
| North East Vic (NRM 207, model zone 22) | **98,604** | 99,460 | 96,930 | 204,651 |
| Goulburn Broken (NRM 204, model zone 19) | **177,479** | 181,059 | 184,989 | 204,651 |

The allocation choice moves North East Vic by under 2%. 20 SA2s touch the North East zone. The national ERP total in the file is 22,340,024; the allocation places 22,336,904 of it in zones.

### 3.2 Capacities and statuses (evaluator `web/src/model/evaluator.js`)

My correction, applied by my own code to the frozen `2011-fixed` and `2011-improved` release data: zone 22 population 98,604; infrastructure 72 km2 (98,604 x 730 m2, rounded); non-agricultural land 3,034 km2 as the remainder so the total area stays 20,234 km2; Victoria's population reset to the sum of its regions (state-population-sum), 5,439,885. National row left as it is (22,326,388). I evaluated every zone in both presets, and also evaluated `2011-fixed-2` and `2011-improved-2` exactly as they stand.

| Release | Zone | Term | Population | Capacity | Capacity per person | Status |
|---|---|---|---|---|---|---|
| corrected 2011 | North East Vic | short | 98,604 | 105,525 | 1.070 | under |
| corrected 2011 | North East Vic | long | 98,604 | 9,476 | 0.096 | over |
| corrected 2011 | Goulburn Broken | short | 204,651 | 498,595 | 2.436 | under |
| corrected 2011 | Goulburn Broken | long | 204,651 | 42,830 | 0.209 | over |
| improved 2011 | North East Vic | short | 98,604 | 109,339 (was 110,288) | 1.109 | under |
| improved 2011 | North East Vic | long | 98,604 | 8,099 | 0.082 | over |
| improved 2011 | Goulburn Broken | short | 204,651 | 525,377 | 2.567 | under |
| improved 2011 | Goulburn Broken | long | 204,651 | 28,250 | 0.138 | over |

On the corrected method no capacity moves (North East Vic was 105,525 and 9,476 before as well). On the improved method North East Vic's short-term capacity falls by 949 because the smaller infrastructure area enters the reserve-pro-rata share. Goulburn Broken does not move. Victoria: corrected short 5,345,825 against 5,439,885 (over, 0.983), long 804,809 (over); improved short 6,747,547 (under, 1.240), long 631,471 (over). Australia unchanged (corrected short 1.492, long 0.688).

### 3.3 National counts and flips (53 regions: 52 NRM regions plus NT, population greater than capacity)

| | Before (2011-fixed) | Mine | 2025-fixed |
|---|---|---|---|
| Over capacity, short | 23 | **22** | 16 |
| Over capacity, long | 36 | **36** | 32 |
| Improved method, short (2011-improved; mine) | 22 | **21** | |
| Improved method, long | 38 | **38** | |

Short-term flips 2011 to 2025, corrected method, mine: **8** (7 over to under: Desert Channels, Mackay Whitsunday, Southern Gulf, Wet Tropics, SA Arid Lands, Rangelands, North Tasmania; 1 under to over: Corangamite). North East Vic is under capacity at both dates and is no longer a flip. Long-term flips: 4, unchanged (Desert Channels, South West Qld, Northern and Yorke, SA Arid Lands).

The three "clean" flips: the artefact and robustness tests sit on the 2025 side and on capacity, which this correction does not touch, so the verdicts of V08 stand for the remaining flips. Of the three short-term clean flips (Mackay Whitsunday, North Tasmania, North East Vic), **two remain: Mackay Whitsunday and North Tasmania**. Long-term clean flip: South West Qld, unchanged. Net fall against clean flips: short 6 against 2, long 4 against 1.

Improved method flips (2011-improved to 2025-improved), mine: short 7 to 6 (North East Vic drops out); long 8, unchanged.

Shock rows (from the capacities in `analysis/paper_a/shocks_by_region.csv`, which I first checked equal my own short-term capacities at return period 1 for all 53 zones, against my populations): 2011 average year 22 over, 81.3% of the population in over-capacity regions (80.9% if divided by the national row); 1 in 5: 23; 1 in 10: 24; 1 in 20: 27; 1 in 50: 32; 1 in 100: 33. Under in an average year and over at 1 in 10: 2011 two (Corangamite, North East Vic), 2025 five (North East Vic, Burnett Mary, Mackay Whitsunday, Wet Tropics, Rangelands). The same at 1 in 20: 2011 five, 2025 eight.

## 4. Comparison with B90 (report `qa/reports/B90_ne_vic_population.md` and the changed files, opened only now)

| # | Item | B90 | Mine | Verdict |
|---|---|---|---|---|
| 1 | North East Vic 2011 population | 98,604 (route 1, D31) | 98,604 | **pass** (exact) |
| 2 | Goulburn Broken ERP 2011 (`zone_population_2011.csv`) | 177,479 | 177,479 | **pass** |
| 3 | Majority allocation alternative | 96,930 | 96,930 | **pass** |
| 4 | Infrastructure and non-agricultural land in the module | 72; 3,034 | 72; 3,034 | **pass** |
| 5 | Every cell of `results/2011-fixed-2.csv` (120 rows) | | all population, capacity, capacity per person and over-capacity cells agree; 0 mismatches | **pass** |
| 6 | Every cell of `results/2011-improved-2.csv` (120 rows) | | 0 mismatches | **pass** |
| 7 | Cells that differ from the parent release | zone 22 and Victoria only; improved zone 22 short capacity 110,288 to 109,339 | the same four rows per release, the same cells, nothing else | **pass** |
| 8 | Status table in B90 section 4 (194% to 93%, 2,160% to 1,041%, 104% to 102%, 689% to 676%, 186% to 90%) | | recomputed, all agree | **pass** |
| 9 | Published release with the true figure, 99% | | 98,604 / 99,603 = 99.0% | **pass** |
| 10 | `analysis/comparison_2025/movers.csv` zone 22 | pop2011 98,604, dpop 15,751, ratio2011 1.07 and 0.1, over2011 0 and 1 | the same | **pass** |
| 11 | `analysis/paper_a/regional_flips.csv` (106 rows) | 8 short flips, 2 clean; 4 long, 1 clean | every row's population, capacity, both statuses and flip agree with mine; same lists | **pass** |
| 12 | `analysis/paper_a/shocks_summary.csv`, 2011 rows | 22, 81% at return period 1; 23, 24, 27, 32, 33 and 82, 84, 87, 91, 92% at 1 in 5 to 1 in 100 | the same (81.3%, 81.8%, 83.5%, 87.4%, 91.3%, 92.2%) | **pass** |
| 13 | Tipping counts (B90 section 7) | 1 in 10: 2011 two, 2025 five; 1 in 20: 2011 five, 2025 eight | the same, same names | **pass** |
| 14 | Counts before and after (23 to 22 short; 36 long; improved 22 to 21) | | the same | **pass** |
| 15 | Route 2 (ABS 3218.0 cube, 98,642) | | the cube is not stored in either repository and I had no network | **cannot determine** |

### Claim rows B90 says move (register not edited by B90 or by me)

Tier A, all **pass** on the values (I agree with each before and after):

| Id | Before | After | Move |
|---|---|---|---|
| A029 | 23 | 22 | down 1 |
| A033 | 23 to 16; 36 to 32 | 22 to 16; 36 to 32 | short 2011 side down 1 |
| A034 | 9 (8 over to under, 1 under to over) | 8 (7 over to under, 1 under to over) | down 1 (North East Vic drops) |
| A036 | 3: Mackay Whitsunday; North Tasmania; North East Vic | 2: Mackay Whitsunday; North Tasmania | down 1 |
| A164 | 23 | 22 | down 1 |
| A165 | 82 | 81 | down 1 point (81.9% to 81.3%) |
| A199 | 5 (2025); 1 (2011) | 5 (2025); 2 (2011), North East Vic added | 2011 side up 1 |

Tier A rows I confirm do not move in value: A002, A005, A031, A035, A037, A038, A039, A163, A167, A171, A196, A363 (national figures and long-term counts do not depend on zone 22's population while the national row is kept).

Tier B and C rows: A043 (6 against 2; 4 against 1), A197 (81; 85; 91) and A308 (22; 22; 21, my corrected and improved counts agree) **pass**. A310 (39; 36; 38): corrected 36 and improved 38 unchanged, as B90 implies. For A144 see finding 2.

## 5. Things found that the brief did not ask about

1. **Goulburn Broken's own 2011 figure is 15% above its ERP.** Its default 204,651 against 177,479. Not part of decision 84 and B90 did not change it. With 177,479 Goulburn Broken stays under in the short term (2.81) and over in the long term (0.24), so no status moves. Among the Victorian zones the default-to-ERP ratio otherwise runs 0.81 (Glenelg Hopkins) to 1.05, so 1.15 is at the high end but not of the copy's kind (North East Vic 2.08).
2. **A144 (Tier B, 94% of the population in long-term over-capacity regions, 2011) depends on the denominator.** With the national row kept at 22,326,388 the 53 regions now sum to 22,220,341. Over the regions' sum the share is 93.7% (94, holds, as B90 says); over the national row it is 93.3% (93, moves). The short-term share is 81 either way. Which denominator the paper uses should be fixed along with B90 decision 2 (whether to reset the national row).
3. **Wording of "tips at 1 in 10".** North East Vic is already over capacity at 1 in 5 in both years (2011: 90,488 against 98,604; 2025: 110,651 against 114,355). The A199 count ("under in an average year, over at 1 in 10") holds, but B90's phrase "tips over capacity at 1 in 10" should read "is over capacity by 1 in 10" if it reaches the paper.
4. Victoria's own infrastructure input (3,957 km2) is not the sum of its regions either before (4,048) or after (3,971) and was not changed; state capacity is evaluated on state land, so nothing moves. Recorded only.
5. My Fitzroy and Wet Tropics ERP figures (235,629 and 246,885) agree with `zone_population_2011.csv` and ERRATA error 9.

## 6. Register rows touched

None (claims, sources, literature, defects).

## 7. Commands to rerun (from any folder; the scripts read the repository by absolute path)

```
S=<session scratchpad>/v33
python3 -I $S/pop2011.py          # 2011 zone populations, three allocations
cd /home/user/carrying-capacity-dashboard
node $S/run.mjs                   # evaluate old, mine and new releases; counts; flips; writes $S/results.json
node $S/flips_imp.mjs             # improved-method flips against 2025-improved
python3 -I $S/compare.py          # every cell of results/2011-fixed-2.csv and 2011-improved-2.csv against mine
python3 -I $S/shocks.py           # shock counts and shares from shocks_by_region.csv capacities
NE_POP=89604 node $S/run.mjs      # wrong-value test 1 (then rerun node $S/run.mjs)
INJECT=22:short=90000 node $S/run.mjs   # wrong-value test 2
```

## 8. Files read

Before comparing: `qa/briefs/V33_ne_vic_check.md`, `qa/briefs/_checker_rules_results_wave.md`, `qa/DECISIONS.md` (row 84), `qa/sources_register.csv`, `data/sa2/population_erp.csv`, `data/sa2/clum_classes.csv`, `data/nrm2011/*.csv`, `data/2011/default-inputs-*.csv`, `web/src/model/evaluator.js`, `analysis/sensitivity_2025/evaluate.mjs`, `web/public/data/{2011-fixed,2011-fixed-2,2011-improved,2011-improved-2,2025-fixed,2025-improved}/`, `web/public/data/releases.json`, `qa/reports/V08_regional_flips.md` (definitions of the flip tests), `qa/claims_register.csv`. Seen before the comparison by a search: the first line of ERRATA error 8, which states 98,604; my figure comes from my own allocation script.
At the comparison: `qa/reports/B90_ne_vic_population.md`, `results/2011-fixed{,-2}.csv`, `results/2011-improved{,-2}.csv`, `results/2011-corrected.csv`, `analysis/comparison_2025/movers.csv`, `analysis/paper_a/regional_flips.csv`, `analysis/paper_a/shocks_summary.csv`, `analysis/paper_a/shocks_by_region.csv`, `analysis/population_2011/zone_population_2011.csv`, `methods/north-east-vic-population/method.json`, `releases/2011-fixed-2/release.json`, `ERRATA.md` errors 8 and 9, part of `analysis/paper_a/long_term_and_measures.mjs`.
