# V52: blind check of B138 (Paper A, the smaller computations)

Checker brief: `qa/briefs/V52_check_B138.md`; rules `qa/briefs/_checker_rules_results_wave.md`. Builder brief `qa/briefs/B138_paper_A_smaller_computations.md` was read first. I derived every figure below with my own code, written in the session scratch folder (`.../scratchpad/v52/`), before I opened `qa/reports/B138_paper_A_smaller_computations.md`, `analysis/paper_a/README_round2_B138.md` or any B138 output. No git, no subagents, no network. This file is the only repository file written.

## Tolerance (stated before comparing)

* Counts, names and years must match exactly.
* Capacities: within 0.5%, or within half a unit of the last digit the builder prints (39.1 million: plus or minus 0.05 million), whichever is larger.
* Shares and ratios: within one unit of the last printed digit.
* Random groupings (item 3): the builder's median must lie within the 95% order-statistic interval of my median (plus half a printed unit), because both are samples of 200; counts of draws compared the same way.

## Wrong-value checks (examples, not results)

Each check below was run with one deliberate wrong value, and each one reported a mismatch:

* Diet window: my 2014-23 capacity replaced by 39.88 million (2% high). Output: `CHECK 2014-23 builder 39100000 mine 39882000 FAIL`.
* 2011 subsets: the long-term capacity of subset 2005-06/2006-07/2007-08 replaced by 12.0 million. Output: `RANGE all_ratio short 32.71 to 34.02 long 12.00 to 15.49 FAIL vs builder 32.7-34.0 / 13.3-15.5`.
* Partition: my state-basis median replaced by 80.0%. Output: `CHECK median state: builder 85.0% mine 80.0% tolerance 3.0% FAIL`.
* Age-sex energy: a mean of 8.60 MJ compared with the builder's 8.30. Output: `CHECK wrong value 8.60 vs builder 8.30: FAIL`.

## My figures

### 1. Diet window (the item that matters most)

**Source.** The FAO food balance bulk file for Oceania (`FoodBalanceSheets_E_Oceania_NOFLAG.csv`, FAO file date 2025-10-14, 2010 to 2023), which is the file `analysis/consumption_2025/make_red_meat_mix.py` and `consumption_proxies.py` take as input. Its FAO date matches the All-Data bulk of `qa/fao_bulk_hashes.csv`. I unpacked it into my own folder. Element: food supply quantity (kg/capita/yr), Australia.

**Rebuild.** I recomputed the three diet inputs as the pipeline does: the meat-and-egg share (0.13 times the change of the FAO share, snapped to 0.005), the red-meat share (0.64 times the change, to 3 decimals), and the red-meat split Base!V175:V178 (each 1995 share times its FAO series change, then renormalised). The base stays at 2010-12. The latest window is each three-year window and also 2014-23. I ran `2025-fixed` through `web/src/model/evaluator.js` for Australia, short term.

**Reproduction.** On the 2021-23 window the inputs are 0.12, 0.578 and the released split (0.595284, 0.231357, 0.017140, 0.156219), and capacity is 41,503,537. That equals the release exactly.

| Latest window | Beef kg/person | Meat-egg share | Red-meat share | Capacity (release rounding) | vs 41.5 M base | Diet-input effect vs 2011 values | Capacity, unrounded inputs |
|---|---|---|---|---|---|---|---|
| 2010-12 (= 2011 values) | 39.11 | 0.130 | 0.640 | 35,535,584 | -5.97 M | 0 | 35,535,578 |
| 2011-13 | 38.17 | 0.130 | 0.637 | 35,820,517 | -5.68 M | +0.28 M | 35,836,443 |
| 2012-14 | 35.88 | 0.130 | 0.630 | 36,329,325 | -5.17 M | +0.79 M | 36,914,611 |
| 2013-15 | 34.60 | 0.125 | 0.627 | 37,208,840 | -4.29 M | +1.67 M | 37,201,554 |
| 2014-16 | 34.05 | 0.130 | 0.623 | 36,883,149 | -4.62 M | +1.35 M | 37,459,854 |
| 2015-17 | 31.75 | 0.125 | 0.610 | 38,372,998 | -3.13 M | +2.84 M | 38,382,569 |
| 2016-18 | 30.06 | 0.125 | 0.601 | 38,996,795 | -2.51 M | +3.46 M | 38,989,176 |
| 2017-19 | 27.30 | 0.125 | 0.593 | 39,960,555 | -1.54 M | +4.42 M | 40,580,221 |
| 2018-20 | 30.15 | 0.125 | 0.606 | 38,874,889 | -2.63 M | +3.34 M | 38,875,594 |
| 2019-21 | 29.09 | 0.125 | 0.599 | 39,396,215 | -2.11 M | +3.86 M | 40,003,800 |
| 2020-22 | 29.14 | 0.125 | 0.597 | 39,397,558 | -2.11 M | +3.86 M | 40,015,310 |
| **2021-23 (released)** | 25.88 | 0.120 | 0.578 | **41,503,537** | 0 | +5.97 M | 41,494,927 |
| **2014-23 (ten years)** | 29.84 | 0.125 | 0.601 | **39,082,575** | **-2.42 M** | **+3.55 M** | **39,691,826** |
| 2010-23 (whole series) | 32.25 | 0.125 | 0.612 | 38.20 M | -3.30 M | +2.67 M | |

* 2021-23 has the lowest beef supply of any window, and it gives the highest capacity.
* **Share of the 2011-to-2025 rise.** The rise is 41,503,537 minus 33,307,814, which is 8,195,723. The window choice 2014-23 against 2021-23 is worth 2.42 million, **29.5% of the rise**, on the release's rounding, or 1.81 million (22.1%) on unrounded inputs. On three-year windows that end in 2019 or later (2017-19 to 2021-23), the gap from 41.5 million runs from 0 to 2.63 million, which is 0 to 32% of the rise. 2025 stays above 2011 on every window except 2010-12 itself.
* The 0.005 snap of the meat-and-egg share moves results by up to 0.6 million within one window (2014-16, 2017-19, 2019-21, 2014-23). It also explains why the three-year series is not monotone (2014-16 is below 2013-15).
* Further checks:
  * Queensland's short-term diet effect is negative on every window after 2010-12 (2021-23: -1.03 million; 2014-23: -0.67 million).
  * Australia's long-term effect (red-meat split only) is +0.40 million on 2021-23 and +0.27 million on 2014-23.

### 2. 2011 window subsets

**Method.** I rebuilt the 2011 Yield sheet with `pipeline/yields` (the stage functions that `verify_end_to_end.py` uses) from the author archive (`/home/user/carrying-capacity-models/Yield data`, file 1 cubes, `archive_livestock_inputs.json`) on all five archive years and on each of the ten three-year subsets. I applied each subset as a ratio to the released yield. Where a subset had no value, I kept the released value. A direct replacement gives the same figures. For Australia, the five-year rebuild equals the released crop rows to within 4e-16 and reproduces 33,307,814 and 15,350,146. I evaluated `2011-fixed-3`, Australia.

| Subset (FY ending) | Crops and animal products: short | long | Crops only: short | long |
|---|---|---|---|---|
| 2006, 2007, 2008 | 32.719 | 14.371 | 33.269 | 14.366 |
| 2006, 2007, 2009 | 32.981 | 15.320 | 33.312 | 15.354 |
| 2006, 2007, 2010 | 32.714 | 14.603 | 33.291 | 14.612 |
| 2006, 2008, 2009 | 33.146 | 15.362 | 33.331 | 15.399 |
| 2006, 2008, 2010 | 32.880 | 14.543 | 33.299 | 14.556 |
| 2006, 2009, 2010 | 33.147 | 15.293 | 33.347 | 15.413 |
| 2007, 2008, 2009 | 33.843 | 14.971 | 33.264 | 14.960 |
| 2007, 2008, 2010 | 33.559 | 13.304 | 33.229 | 13.318 |
| 2007, 2009, 2010 | 33.857 | 15.302 | 33.291 | 15.305 |
| 2008, 2009, 2010 | 34.020 | 15.486 | 33.318 | 15.387 |
| **Range** | **32.71 to 34.02** | **13.30 to 15.49** | 33.23 to 33.35 | 13.32 to 15.41 |

The builder's short-term range of 32.7 to 34.0 is reproduced only when the animal-product rows (livestock yields) are subsetted as well. With crop yields alone, the short term barely moves (33.2 to 33.3). The long term is crop driven, and the two scopes agree.

### 3. Partition effect

**Method.** I took 200 random groupings of the 53 regions into 7 non-empty groups (Fisher-Yates shuffle, the first 7 seed the groups, the rest are assigned at random). I used my own LCG generator with seeds 987654321 and 20261118, release `2025-fixed`, short term. The basis rule I chose before reading the builder's script was the state basis, where a group takes the yields, climate zone, irrigation and reserve of the state holding most of its cropland (this mirrors `make-scale-curve.mjs` for coarse units). The second basis is the national yield vector.

| | Seed 987654321 | Seed 20261118 |
|---|---|---|
| State basis: median (5th to 95th percentile; min to max) | 83.3% (56.6 to 115.3; 45.4 to 129.5) | 83.1% (58.1 to 116.7; 42.8 to 129.8) |
| National vector: median (5th to 95th percentile) | 91.1% (71.4 to 100.0) | 91.1% (72.5 to 100.0) |
| Real states, state basis / national vector | 75.4% / 75.8% | same |
| Draws above the real states, national vector | 179 of 200 | 182 of 200 |
| Draws above the real states, state basis | 135 of 200 | 129 of 200 |
| 53 regions, state basis / national vector | 44.0% / 32.7% | same |

The state basis is fragile for groups that mix states. Groups exceed 100% (up to 130%) because one state's yields are applied to land in another state. If I give a mixed group the state holding most of its *land* instead of its cropland, the median falls to 58.0%. The national-vector figure does not depend on that rule.

### 4. Reference periods and the national row

**Window centres.** An ABS financial year has its midpoint at 1 January of its second calendar year.

| Window | Centre | Years before the population date |
|---|---|---|
| 2011 windows, 2005-06 to 2009-10 | 1 January 2008 | 3.5 before 30 June 2011 (1.0 from the window end) |
| 2011 pasture (four years) | | 3.25 |
| 2025 livestock, 2020-21 to 2024-25 | 1 January 2023 | 2.5 |
| 2025 crops, 2022-23 to 2024-25 | | 1.5 |
| 2025 land, 2020-21 | | 4.5 |
| Diet, 2021-23 | mid-2022 | 3.0 |

**Midpoint populations** (D31, `data/sa2/population_erp.csv`, interpolated between 30 June values), 2025 short term, capacity over population:

| Window | Population at the midpoint | Ratio |
|---|---|---|
| Livestock | 26.34 M | 1.576 |
| Crops | 26.93 M | 1.541 |
| Land | 25.67 M | 1.617 |
| Diet | 26.02 M | 1.595 |
| Vegetable, fruit and nut group factor (1 January 2019) | 25.15 M | 1.650 |

Range: **1.54 to 1.65**. There is no 2011 midpoint figure on the series used for the populations. The archive's June 2009 and June 2010 ERP (21,965,287 and 22,342,398) are a pre-2011-census vintage and should not be mixed with D31.

**National row.**

* The 53 regions of `2011-fixed-3` sum to **22,336,514**, and so do its seven states. The national row is 22,326,388 (10,126 fewer).
* Short-term status: 22,326,388 / 33,307,814 = 0.6703 and 22,336,514 / 33,307,814 = 0.6706, so **0.670 becomes 0.671**.
* Long-term status: 1.45447 and 1.45513, so **1.454 becomes 1.455**.
* A005: 1.4919 and 1.4912, so it **prints 1.49 either way**.
* A328: population +23.66% and +23.60%, so **23.7% becomes 23.6%**.

### 5. Projections and age-sex energy

**Projections.** I used straight lines between the printed points, as the builder's rule does:

* IGR 2023, from 37.3 M (2052-53) to 40.5 M (2062-63): 41.5 M is reached about 3.1 years after June 2063, which is **2066**.
* Population Statement 2025, from 31.5 M (2035-36) to 41.0 M (2065-66): 41.5 M is reached 1.6 years after June 2066, which is **2068**.
* 30.8 M is reached in **2034** on both: IGR between 30.4 M (2032-33) and 33.9 M (2042-43); Statement between 28.3 M and 31.5 M (2035-36).
* A cross-check with one straight line from 27.61 M at June 2025 gives 2066.5 and 2068.0 for 41.5 M. For 30.8 M it gives 2034.9 and 2035.3, so the Statement's 30.8 crossing is 2034 or 2035 depending on the line used.
* 40.5 / 15.623209 = **2.592**. 40.5 / 15.6 = 2.596, so "2.6 times" is right, but "40.5 over 15.6 = 2.59" is only true with the unrounded capacity.

**Age-sex energy.** I used the ABS 3101.0 (June 2010 issue) Tables 7 and 8 in the archive (`Yield data/ABS - Aust demographics 2010.xls`; single years 0 to 84, five-year groups 85 to 99, 100 and over; totals 21,965,287 and 22,342,398) and the NHMRC NRV in the archive (`Foundation diets/nutrient-refererence-dietary-intakes.pdf`):

* Table 1 for ages 0 to 2 (age 0 the mean of months 1 to 12; age 1 the mean of months 15 to 24; age 2 the 24-month value).
* Table 2 at PAL 1.4 for ages 3 to 18.
* Table 3 at PAL 1.4 for adults.

The result depends on which adult body size is used:

| Adult basis | Mean 2009 | Mean 2010 | Over 8.0 MJ |
|---|---|---|---|
| Reference weights (76 kg, 61 kg) interpolated in Table 3 | 8.308 | 8.306 | **1.038** |
| The text's printed sedentary values (10.8, 11.0, 9.5, 7.4; 8.1, 7.9, 7.6, 7.1) | 8.403 | 8.400 | 1.050 |
| Table 3 at 1.7 m | 8.045 | 8.042 | 1.006 |
| Table 3 at 1.8 m (men) and 1.6 m (women) | 8.077 | 8.074 | 1.009 |

## Comparison (builder against mine; opened only after the figures above)

| Item | Builder | Mine | Result |
|---|---|---|---|
| Diet: 2021-23 reproduces the release | 41,503,537 | 41,503,537 | pass |
| Diet: 2014-23 capacity, release rounding | 39.1 M (39,082,575) | 39,082,575 | pass (to the person) |
| Diet: 2014-23 capacity, unrounded inputs | 39.7 M | 39,691,826 | pass |
| Diet: 2014-23 effect, rounded / unrounded | 3.55 / 4.16 M | 3.547 / 4.156 M | pass |
| Diet: each three-year window (11 rows) and 2010-23 | 35.8 to 41.5; 38.2 | same to 0.01 M | pass |
| Diet: 2021-23 is the lowest-beef window | yes | yes (25.88 kg) | pass |
| Diet: 2025 over 2011 on 2014-23 | 17% to 19% | 17.3% / 19.2% | pass |
| Diet: Queensland effect negative on every later window | yes | yes | pass |
| Diet: long-term effect 2021-23 / 2014-23 | 0.4 / 0.27 M | 0.398 / 0.269 M | pass |
| Diet: share of the 2011-to-2025 rise | not stated (59% of the released diet effect) | 29.5% (22.1% unrounded) | (new figure) |
| 2011 subsets: short-term range | 32.7 to 34.0 | 32.71 to 34.02 | pass (crops and animal products) |
| 2011 subsets: long-term range | 13.3 to 15.5 | 13.30 to 15.49 | pass |
| 2011 subsets: all ten rows | as tabled | same to 0.01 M | pass |
| 2011 subsets: 2025 over 2011, short / long | 22% to 27% / 1% to 17% | 22.0% to 26.9% / 0.9% to 17.4% | pass |
| Partition: state-basis median | 85.4% | 83.3%, 83.1% (interval about ±3 points) | pass (sampling) |
| Partition: national-vector median | 90.5% (91%) | 91.1%, 91.1% | pass |
| Partition: national-vector 5th to 95th percentile | 73.2% to 99.8% | 71.4 to 100.0; 72.5 to 100.0 | pass |
| Partition: real states, state basis / national vector | 75.4% / 75.8% | 75.4% / 75.8% | pass |
| Partition: draws above the real states, national vector | 181 of 200 | 179, 182 | pass (sampling) |
| Partition: draws below the real states, state basis | 54 of 200 | 65, 71 | pass (sampling; SD of the share 0.21) |
| Partition: 53 regions, state basis / national vector | 44.0% / 32.7% | 44.0% / 32.7% | pass |
| Partition: group yield rule | state with most cropland | same rule, chosen blind | pass |
| Window centre, 2011 | 3.5 y | 3.5 y | pass |
| Window centre, 2025 livestock / land | 2.5 / 4.5 y | 2.5 / 4.5 y | pass |
| Midpoint ratios, 2025 | 1.54 to 1.65 (1.576 livestock) | 1.541 to 1.650 (1.576) | pass |
| 2011 regional sum | 22,336,514 | 22,336,514 | pass |
| A363 short | 0.670 to 0.671 | 0.6703 to 0.6706 | pass |
| A363 long | 1.454 to 1.455 | 1.4545 to 1.4551 | pass |
| A005 | 1.49 either way | 1.4919 / 1.4912 | pass |
| A328 | 23.7% to 23.6% | 23.66% to 23.60% | pass |
| Projections: 41.5 M reached | 2066 (IGR), 2068 (Statement) | 2066, 2068 | pass |
| Projections: 30.8 M passed | 2034 both | 2034 both (printed-point lines) | pass (2035 for the Statement on a line from June 2025) |
| Long term 2.6 times | 2.59 | 2.592 (2.596 on the rounded 15.6) | pass |
| Age-sex mean, 2009 / 2010 | 8.304 / 8.302 MJ | 8.308 / 8.306 MJ | pass (within 0.01) |
| Age-sex ratio to 8.0 MJ | 1.038 | 1.038 | pass |
| Age-sex one-year move | 0.02% | 0.02% | pass |

Not checked (not asked for in this brief): the arable-share and dairy relaxations (item 4 b, c), the higher and lower projection cases, and the regional and state rows of the CSVs other than Queensland's diet effect.

## Points that change a number or a sentence

1. **Diet window, share of the rise (new number).** The paper should say what the window is worth against the 2011-to-2025 change. The builder gives it only as a share of the diet effect. Proposed: "On the 2014-23 window, capacity is 39.1 million (39.7 on unrounded inputs) against 41.5, which is 2.4 million (1.8 unrounded), or 22% to 30% of the 8.2 million rise between 2011 and 2025; 2025 still exceeds 2011 by 17% to 19%."
2. **Diet window wording (overclaim).**
   * "The beef fall is steady across the series" is not right: the window means rise from 27.3 kg (2017-19) to 30.2 kg (2018-20). Say "falls over the series, unevenly; 2021-23 is the lowest window".
   * "Which spans the cattle price cycle" and "a period of herd rebuilding" are not shown by anything on disk. Write "chosen to span a cattle price cycle (R05a)", or cite a source.
   * The paper must give 39.1 and 39.7 together. The 0.6 million gap is the release's 0.005 snap of the meat-and-egg share, not the window.
3. **2011 subsets, wording (changes what the range means).**
   * The 32.7 to 34.0 short-term range comes from subsetting the animal-product yields. Crop yields alone give 33.2 to 33.3.
   * The 2025 livestock window is five years, not three, so a three-year livestock subset is *not* matched in length to 2025. Matched length applies to crops only.
   * The proposed sentence ("to match the three-year crop window of 2025, moves 2011 short-term capacity between 32.7 and 34.0") should say "yields of crops and animal products" and add that crops alone move the short term by under 0.1 million. The long-term range (13.3 to 15.5) holds on either scope.
4. **Partition.**
   * The state-basis median for mixed-state groups depends on the rule for which state's yields a group takes (85% on cropland majority; 58% on land majority in my run). The paper should put the national-vector figures in the main text, as the builder's sentence does, and should not quote the 85%.
   * The builder's note "the sum cannot exceed the nation's" on the national vector holds for 2025, but its own 2011 summary has a maximum of 101.6%.
5. **Age-sex energy.** 8.30 MJ (1.038) is reproduced on the reference-weight basis. On other adult body sizes the NRV gives 8.04 to 8.40 (1.006 to 1.050), so the sentence should name the basis ("at the NHMRC reference body weights"). As the builder says, it is a level on 2009 and 2010 counts and says nothing about the change from 2011 to 2025.
6. **Projections.**
   * "40.5 over 15.6 = 2.59" should read 2.6, or 2.59 on the unrounded 15.62.
   * "1.8 times below the 2025 population" is awkward. Write "the 2025 population is 1.8 times the long-term capacity".
   * The Statement's 30.8 crossing is 2034 on the printed-point rule and 2035 on a line from June 2025. Keep "2034" only with the rule stated.
7. **Midpoints.** "1.5 to 1.6 on the 2025 midpoint populations" understates the top of 1.65, which is the vegetable group-factor window. Write "1.54 to 1.65 (1.58 on the livestock window)", and keep the builder's statement that 2011 has no midpoint figure.

## Claim rows

| Row | Builder | Verdict |
|---|---|---|
| A363 (Tier A) | 0.670 to 0.671, 1.454 to 1.455, statement "22,336,514 people" (conditional on decision 140) | holds |
| A328 (Tier B) | population 23.7% to 23.6%; capacity +24.6% stays | holds |
| A369 (Tier B) | statement text changes; values stay as the record | holds (22,326,388 + 10,126 = 22,336,514) |
| A005 (Tier A) | 1.4919 to 1.4912, prints 1.49; no move | holds |

A376 and A380 (the diet layers, 5.6 million, 68%) are affected in meaning. The builder rightly says the window effect measured last on `2025-fixed` is not the decomposition's measure (README line 45). The paper should not put 3.5 million beside 5.6 million as if they were the same quantity.

## What I would do differently

* Report the diet window against the 2011-to-2025 rise (item 1 above), and print the rounded and unrounded results together.
* Run the 2011 subsets with crops only as the matched-length case, and with livestock subsetted only as a separate stress case.
* Report the partition on the national vector only, or give the state-basis rule's sensitivity beside it.
* Name the adult body-size basis of the age-sex mean.

## Register rows touched

None.

## Rerun

From the repository root (scripts in the session scratch folder `v52/`; `S` is that folder):

```
python3 -I $S/diet_inputs.py $S/fbs_oc/FoodBalanceSheets_E_Oceania_NOFLAG.csv $S/diet_inputs.json && node $S/diet_eval.mjs $S/diet_inputs.json [wrong]
python3 -I $S/diet_inputs2.py $S/fbs_oc/FoodBalanceSheets_E_Oceania_NOFLAG.csv $S/diet_inputs2.json && node $S/diet_extra.mjs $S/diet_inputs2.json
MODELS_DIR=/home/user/carrying-capacity-models python3 -I $S/subsets_2011.py $S/subsets_2011.json && node $S/subsets_eval.mjs $S/subsets_2011.json [wrong]
node $S/partition.mjs 987654321 crop [wrong]; node $S/partition.mjs 20261118 crop; node $S/partition.mjs 987654321 land
python3 -I $S/agesex.py [wrong]
```

The FAO zip is the Oceania bulk at `.../scratchpad/diet/dl/fbs.zip`, unpacked into `$S/fbs_oc/`. The NRV text was extracted with `pdftotext -layout`.

## Files read

* Briefs: `qa/briefs/V52_check_B138.md`, `_checker_rules_results_wave.md`, `B138_paper_A_smaller_computations.md`.
* Background: `qa/reports/R05a_response_plan_A.md` (issues 1, 9, 10, 14, 2).
* Diet: `analysis/comparison_2025/README.md`, `analysis/consumption_2025/README.md`, `consumption_proxies.py`, `make_red_meat_mix.py`, `data/2025/consumption_proxies.json`, `data/2025/red_meat_mix.json`.
* Scale curve: `analysis/scale_curve_2025/README.md`, `ideal_split_test.mjs`, `web/scripts/make-scale-curve.mjs`.
* Model and releases: `web/src/model/evaluator.js`, `analysis/sensitivity_2025/evaluate.mjs`, `releases/README.md`, `releases/2011-fixed*/release.json`, `releases/2025-fixed/release.json`.
* Yields and land: `pipeline/yields/README.md`, `yields.py`, `average.py`, `fill.py`, `verify_end_to_end.py`, `analysis/land_2011/README.md` (lines).
* Data and registers: `data/sa2/population_erp.csv`, `qa/sources_register.csv` (D31), `qa/claims_register.csv` (A005, A328, A363, A369).
* Archive: `Yield data/ABS - Aust demographics 2010.xls`, `Foundation diets/nutrient-refererence-dietary-intakes.pdf`.
* Last, the builder's work: `qa/reports/B138_paper_A_smaller_computations.md`, `analysis/paper_a/README_round2_B138.md` (grep), `analysis/scale_curve_2025/scale_partition.mjs` (grep), `scale_partition_summary.csv`, `analysis/diet_2025/diet_window.csv` (rows), `analysis/paper_a/window_subsets_2011_summary.csv` (rows).
