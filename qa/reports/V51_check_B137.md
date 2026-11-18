# V51: blind check of B137 (eight-layer table, meat identity, drought factor variants, residue bound, X118)

Checker brief: `qa/briefs/V51_check_B137.md`; rules `qa/briefs/_checker_rules_results_wave.md`. No git, no subagents, no network. Only this file was written in the repository; all scripts and outputs are in the scratch folder `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v51/`. My own figures were derived before I opened the builder's report or any B137 output.

**Overall: every number I could reach reproduces. No figure changes.** Three of the proposed sentences overclaim (S4, S6, S10) and two caveats belong beside the drought-factor and identity readings (below).

## Tolerance

* Counts, region names, layer names, year cells: exact.
* Capacities and changes in capacity (people): within 0.5% of the builder's value.
* Ratios, factors and shares: within one unit of the last digit the builder prints.

## Wrong-value check (example, deliberately wrong)

`cmp.py` holds every builder value against mine under the rules above. With the true figures it reports `failures 0`. Run with an extra line in which my residue is set to -204,427 against the builder's -194,427 (5.1% off), it prints `INJECTED WRONG: residue short  builder -194427 mine -204427 FAIL` and `failures 1`. The same probe on the evaluator: a factor of 0.60 gives 24,902,122, not the 31.6 million of the 0.762 factor, so a wrong factor would show.

## My figures

### 1. Eight layers (capacity_by_cause_corrected_orders.csv, game `eight_layers_land_livestock_one`, zone 1)

| Layer | Short average | Short forward | Short reverse | Long average | Long forward | Long reverse |
|---|---|---|---|---|---|---|
| Land and livestock | +2,456,649 | +2,043,444 | +2,886,869 | -598,893 | -627,341 | -569,036 |
| Crop yields | +161,723 | +153,478 | +161,965 | +235,890 | +238,533 | +231,217 |
| Consumption | +4,149,655 | +4,183,947 | +4,090,572 | 0 | 0 | 0 |
| Organic | 0 | 0 | 0 | +176,975 | +172,682 | +180,979 |
| Resilience | 0 | 0 | 0 | -7 | -7 | -7 |
| Fuel | 0 | 0 | 0 | +103,056 | +90,858 | +114,983 |
| Red meat mix | +1,427,697 | +1,814,854 | +1,056,317 | +356,042 | +398,338 | +314,927 |
| Infrastructure | 0 | 0 | 0 | 0 | 0 | 0 |
| Total | +8,195,723 | | | +273,063 | | |

Averages sum to the total within 1 person. The average lies between the two walks in every national row.

Regions (52 NRM regions plus the Northern Territory, zone 60), largest layer by **absolute** average: land and livestock 42 short term (crop yields 7, consumption 4) and 31 long term (crop yields 20, fuel 1, resilience 1). Forward walk names a different largest layer in 4 (short) and 6 (long) regions; reverse in 2 and 2. Note: "largest" must mean largest absolute value; by signed value the counts are 31 and 24. The 7/3 and 2/1 walk counts in V37 are the nine-layer game, not the eight.

### 2. Meat identity (FAOSTAT bulk files `/tmp/claude-0/fao/x/FoodBalanceSheets_E_All_Data_(Normalized).csv` and `/tmp/claude-0/fao/q/Production_Crops_Livestock_E_All_Data_(Normalized).csv`, Australia, three-year means)

| Window | Production (FBS / QCL), kt | Food, kt | Ratio FBS / QCL | Food per person, kg | People fed at FAO intake (FBS / QCL), million | Model capacity over population |
|---|---|---|---|---|---|---|
| 2021-23 | 4,645.0 / 4,656.2 | 2,956.3 | 1.5712 / 1.5750 | 112.82 | 41.17 / 41.27 | 41,503,537 / 27,608,200 = 1.5033 |
| 2010-12 | 4,148.3 / 4,114.1 | 2,731.7 | 1.5186 / 1.5061 | 121.45 | 34.16 / 33.87 | 33,307,814 / 22,326,388 = 1.4919 |

Model ratio is 4.3% below the FBS balance in 2025 and 1.8% below in 2011. Red meat (bovine plus mutton and goat) 2.97 and 2.46; milk excluding butter 1.479 and 2.039.

**At the model's own per-person meat intake** (the brief's wording): the evaluator's Base sheet, national short term, gives a primary (dressed) requirement of beef, lamb, veal, pork and poultry of 2,663.7 g a week (139.0 kg a year) in 2025-fixed and 2,827.5 g (147.5 kg) in 2011-fixed-3, against FAO food supply of 112.8 and 121.5 kg. On that intake FAOSTAT production feeds **33.4 million (2021-23) and 28.1 million (2010-12)**, 19% and 16% below the model's 41.5 and 33.3. On ruminant meat alone at the model's beef, lamb and veal requirement: 37.0 and 29.5 million. The builder's "people fed" column uses FAO's food supply per person, not the model's intake.

### 3. Drought factors (resilience.py functions imported, not edited; ABS `Historic Ag Commodities_1860 to 2022.xlsx` plus `data/abs-2022-25` cubes; capacity = 2025-fixed, Australia, short term, factor written into resilience!B3)

Base reproduced (41,503,537); the release table at 10 years via the input (30,810,607) equals the forced factor 0.742361. Thesis method (10-observation reference):

| Series, start | Seasons | 1 in 10 factor; capacity | 1 in 20 factor; capacity | 1 in 100 |
|---|---|---|---|---|
| Unweighted, whole record | 153 | 0.7424; 30.81 M | 0.6343; 26.32 M | 0.4558 |
| Unweighted, 1950-51 | 75 | 0.7621; 31,629,202 | 0.6532; 27,111,924 | 0.5729 |
| Unweighted, 1970-71 | 55 | 0.7621; 31,629,202 | 0.5940; 24,652,515 | 0.5675 |
| Unweighted, 1990-91 | 35 | 0.7621; 31,629,202 | (0.5783; 24,002,961) | n/a |
| Area-weighted, whole record | 153 | 0.7047 | 0.6378 | 0.3566 |
| Area-weighted, 1950-51 | 75 | 0.7106; 29,492,719 | 0.6378; 26,469,770 | 0.5598 |
| Area-weighted, 1970-71 | 55 | 0.7083; 29,395,451 | 0.5850; 24,280,415 | 0.5421 |
| Area-weighted, 1990-91 | 35 | 0.7083; 29,395,451 | (0.5774; 23,966,142) | n/a |

**Capacity at 1 in 10 is above 27,608,200 in every thesis-method variant** (lowest 29.25 million). At 1 in 20 it is below in every variant. Capacity is linear in the factor here: the break-even factor is 27,608,200 / 41,503,537 = 0.665.

Caveat (not in the builder's brief): with resilience.py's own leave-one-out reference ('loo'), the 1-in-10 factors are 0.661 to 0.702, and the area-weighted 1990-91 variant gives 0.6611, capacity **27,438,890, below the population** by 0.6%. Every other loo variant stays above (27.85 to 29.11 million). So "above the population at 1 in 10 in every variant" holds on the model's own method, not on every reference rule resilience.py offers.

### 4. Residue bound (2025-fixed, Australia; 2011 pasture 3,639,794 km2 against 3,318,689, k = 1.09676; pasture yields divided by k so output is unchanged; diet unchanged)

| Setting | Short term | Long term |
|---|---|---|
| Rows 95 to 98 (sheep meat, wool, milk, cattle meat) | -187,781 | -47,653 |
| Rows 95 to 98, 135, 136 (adds goat and sheep milk) | **-194,427** | **-48,724** |
| Same, extra pasture taken out of non-agricultural land | -194,427 | -48,724 |
| Yields divided by the archive denominator ratio 1.104 instead of k | -450,001 | |
| 2011 area with yields unchanged (output not fixed) | +3,666,108 | |

My first setting (the four ABS livestock rows) gave -187,781; adding the two minor milk rows, which are also pasture yields, gives the builder's figure to the person. Both are within 0.5% of base capacity; as a change they differ by 3.4%. Either way the residue is about 0.19 million, 8% of the +2.46 million combined layer, not R05a's rough 0.4 million.

### 5. X118

`build_years_fixed.py` run by me (work dirs in scratch, not `rebuild_years.sh`, which writes into the repository), then `analysis/sensitivity_2025/evaluate.mjs`:
* All placeholders: **128 of 128 year cells equal the committed `analysis/reliability_2025/years.csv` exactly** (largest difference 0). National short term 43,482,098 to 55,369,977; long term 10,360,668 to 13,819,017.
* Base row stale: committed 48,004,473 against 48,265,660 on rerun and in `results/2025-organic.csv` (long 12,305,891 against 12,376,463). 14 of the 16 base cells differ (all but the Northern Territory).
* Series where held: short 43,295,508 (2020-21) to 55,801,003 (2024-25); long 10,360,668 to 13,899,250.

## Comparison (builder against mine)

| Item | Builder | Mine | Result |
|---|---|---|---|
| L&L short average; forward; reverse | 2,456,649; 2,043,444; 2,886,869 | same | pass |
| L&L long average; forward; reverse | -598,893; -627,341; -569,036 | same | pass |
| Other eight-layer rows, both presets, three columns | table | same in every cell | pass |
| Shares 30%; 68% | 30; 68 | 29.97; 68.05 | pass |
| People over capacity 0.670, 0.665, 1.454, 1.767 | as printed | 0.6703, 0.6652, 1.4545, 1.7671 | pass |
| Regions L&L largest, short; long | 42; 31 | 42; 31 | pass |
| Other average counts (7, 4; 20, 1, 1) | as printed | same | pass |
| Forward / reverse differ from average | 4, 2; 6, 2 | 4, 2; 6, 2 | pass |
| Forward counts (39, 7, 7; 26, 25, 2) | as printed | same | pass |
| Meat ratio QCL; FBS 2021-23 | 1.575; 1.571 | 1.5750; 1.5712 | pass |
| Meat ratio QCL; FBS 2010-12 | 1.506; 1.519 | 1.5061; 1.5186 | pass |
| Production, food Mt 2021-23 | 4.656 / 4.645; 2.956 | 4.6562 / 4.6450; 2.9563 | pass |
| People fed 2021-23; 2010-12 (FAO intake) | 41.27, 41.17; 33.87, 34.16 | same | pass |
| Model capacity over population | 1.5033; 1.4919 | same | pass |
| Red meat ratio | 2.972; 2.462 | 2.97; 2.46 | pass |
| Milk ratio | 1.479; 2.039 | 1.479; 2.039 | pass |
| Drought factors, all 24 rows of drought_factor_variants.csv where I computed them (1 in 10, 20, 100) | as printed | same to 4 digits | pass |
| Capacity at each factor, all output | as printed | same to the person | pass |
| 1 in 10 above 27,608,200 in every variant | yes (29.2 to 31.6) | yes on the thesis method; no for loo, area-weighted, 1990-91 | pass (with caveat) |
| Capacity crop-only column | as printed | not computed | not checked |
| Residue short; long | -194,427 (0.47%); -48,724 (0.31%) | -194,427; -48,724 | pass |
| Residue share of combined layer | 7.9% | 7.9% | pass |
| Years: 128 cells reproduced | 128 of 128 | 128 of 128, exact | pass |
| Placeholder range | 43.5 to 55.4 | 43,482,098 to 55,369,977 | pass |
| Series-where-held range | 43.3 to 55.8; 10.4 to 13.9 | 43,295,508 to 55,801,003; 10,360,668 to 13,899,250 | pass |
| Base staleness | 48,004,473 against 48,265,660 | same | pass |
| Feedlot lines 44 to 47, 59, 63 of pipeline/yields/livestock.py | as cited | the lines hold what is cited | pass |
| "Variants give -24% to -30%" at 1 in 10 | -24 to -30 | -23.8 to -29.5 | pass |
| "Rise 20 to 22% on the balance, 25% in the model" | as printed | 20.5 to 21.8; 24.6 | pass |

## Proposed sentences (`abs_frame_feedlot_and_driver_sentences.csv`): overclaim review

* **S1, S2, S3:** hold. S3's "the average lies between the forward and reverse walks in every row" is true of the national table only; say "every row of Table 2".
* **S4: overclaims.** It calls the balance "a commodity balance of pasture-fed food", but the ratio that matches (1.57, 1.51 to 1.52) is **all meat**, including pork and poultry (about 1.8 of the 4.65 Mt), which cropland, not pasture, limits. Pasture-fed red meat alone is 2.5 to 3.0 and milk 1.5 to 2.0; neither matches. Suggested: "Meat production over meat eaten as food (all meats, FAOSTAT) is ...". Also the "people fed" figures (34 and 41 million) are at FAO's per-person food supply; at the model's own meat requirement, which adds losses and waste, the same production feeds 28 and 33 million. The agreement is therefore of ratios, and it should not be presented as an independent count of people. "Validation" is too strong; "consistency check" fits S5's own limits.
* **S5:** fair and well hedged. Its claim that FAOSTAT draws on the ABS tonnes is flagged by the builder as unconfirmed; keep that flag. "Cereals about 19 times" not checked by me.
* **S6: overclaims if used as written.** It states the 2015-16 Business Register frame and the $40,000 threshold as fact, and adds "most of all in peri-urban and coastal zones"; none of this is held in the records (the builder says so in the next column). The location clause has no source at all. Keep out of the paper until the ABS notes are read.
* **S7, S8:** hold; S8 correctly says the figure is not held.
* **S9:** numbers hold (8.8% fall, 0.19 of 2.46 million, 8%). "At most" rests on the stated assumptions (all of the fall definitional; whole rows scaled); "about 0.19 million, an upper bound under these assumptions" is safer. "The rest of the combined layer is output" also includes interaction terms; "mostly output" is safer.
* **S10: overclaims in one clause.** "So feedlot growth does not inflate the pasture yield" does not follow from the denominator rule: the cattle meat yield is all meat over pasture share plus grain and feedlot hectares, and grain-fed meat yields more per hectare than grazing, so a rising feedlot share raises the blended yield that the model then credits per square metre of pasture. Suggested: "so grain-fed output is not credited to pasture alone". The national-invariance clause is argued, not computed, as the row says.

## Claim rows named by the brief

| Row | Verdict |
|---|---|
| A382 (+2,456,649; -598,893) | Holds, exactly; forward and reverse in the notes also hold. No change. |
| A317 (43.5 to 55.4, as built) | Holds as built: the second route (placeholder build) reproduces all 128 year cells exactly, so the "second route blocked" status can move to independently verified for the as-built value. On the series where it is held the range is 43.3 to 55.8; the upper end differs by 0.8%, outside the 0.5% tolerance, so restating the value would move it (a decision, not a checker change). The committed base row (48.0 million) is stale; it is not part of A317's range. |
| A223 (-26% at 1 in 10) | Holds: 30,810,607 / 41,503,537 - 1 = -25.8%. Thesis-method variants give -23.8% to -29.5%. |
| A014 (30.8 million at 1 in 10 against 27.6) | Holds as stated (release table). Every thesis-method variant stays above the population (29.25 to 31.63 million); one loo variant (area-weighted, from 1990-91) falls 0.6% below. |

## What I would do differently

* Report the identity at the model's own meat intake beside the FAO-intake reading (28.1 and 33.4 million), so the paper does not suggest the balance counts the same people the model does.
* Name the loo reference result next to the drought-factor variants; the margin in the 35-season area-weighted case is thin.
* State in the residue file why rows 135 and 136 are in the pasture set (they move the result by 3.4% of itself).

## Register rows touched

None.

## Commands to rerun (repository root)

```
V=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v51
(cd analysis/comparison_2025 && python3 $V/s1.py)                       # eight layers and region counts
python3 $V/s2.py                                                          # meat identity (FAO values extracted by awk from the bulk files)
node $V/meat.mjs 2025-fixed short; node $V/meat.mjs 2011-fixed-3 short    # model meat requirement
python3 $V/s3.py && node $V/s3.mjs $V/factors.json                        # drought factors and capacities
node $V/s4.mjs 2011-fixed; node $V/s4b.mjs                                # residue bound
B137_ALL_PLACEHOLDERS=1 python3 -I analysis/years_2025/build_years_fixed.py $V/yrs_off $V/../abs/ls && node analysis/sensitivity_2025/evaluate.mjs $V/yrs_off/years.json $V/years_off.csv && python3 $V/s5.py $V/years_off.csv
python3 -I analysis/years_2025/build_years_fixed.py $V/yrs_mix $V/../abs/ls && node analysis/sensitivity_2025/evaluate.mjs $V/yrs_mix/years.json $V/years_mix.csv
python3 $V/cmp.py; python3 $V/cmp.py wrong                                # comparison and wrong-value probe
```

## Files read

`qa/briefs/V51_check_B137.md`, `_checker_rules_results_wave.md`, `B137_paper_A_layers_identity_factor_variants.md`; `analysis/comparison_2025/capacity_by_cause_corrected_orders.csv`; `results/2025-fixed.csv`, `2011-fixed.csv`, `2011-fixed-3.csv`, `2025-organic.csv`; `web/public/data/{2025-fixed,2011-fixed,2011-fixed-3}/{model,regions}.json`; `web/src/model/evaluator.js`; `analysis/sensitivity_2025/evaluate.mjs`; `analysis/resilience_2025/resilience.py`; FAOSTAT bulk files under `/tmp/claude-0/fao/`; the ABS historic workbook in the scratch folder; `analysis/pasture_2025/README.md`, `analysis/method_tests_2025/README.md` (parts), `qa/reports/R04b_rereview_A_land_systems.md` (point 3), `R05a_response_plan_A.md` (issue 3), `V37_check_B111.md` (parts); `qa/defects.csv` X118; `pipeline/yields/livestock.py` lines 40 to 66; `analysis/years_2025/build_years_fixed.py`, `rebuild_years.sh`; `analysis/reliability_2025/years.csv`; `qa/claims_register.csv` rows A014, A223, A317, A382 (read only). Then, last: the builder's report and `decomposition_eight_layer_table.csv`, `decomposition_eight_layer_regional_counts.csv`, `meat_balance_identity.csv` (and the header of its script), `drought_factor_variants.csv`, `definitional_residue.csv` and `.mjs`, `abs_frame_feedlot_and_driver_sentences.csv`.
