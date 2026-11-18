# B138: Paper A, the smaller computations (decision 138)

Brief: `qa/briefs/B138_paper_A_smaller_computations.md`. Issues answered: R05a 1, 8, 9, 10, 14 and 21 (the 2011 window subsets). No git, no subagents, no network. New files only, in the folders the brief allows; notes are in `analysis/paper_a/README_round2_B138.md`. No claim register, paper, frozen release or `results/` file was edited.

## Summary, one line per item

1. **Reference periods** (`analysis/population_2011/reference_periods.csv`): the 2011 data windows are centred 3.5 years before 30 June 2011 (1.0 year before at the window end); the 2025 livestock window is centred 2.5 years before 30 June 2025 and ends on it, the land layer (2020-21) 4.5 years before. On the population at the 2025 window midpoints capacity is 1.54 to 1.65 times the population (1.58 on the livestock window) against 1.50 at 30 June 2025. The 2011 midpoint column is empty: ERP before 30 June 2011 is not on disk (fetch 1 below).
2. **Projections** (`analysis/paper_a/projections_against_capacity.csv`): no baseline series reaches 41.5 million within its printed years (40.5 million in 2062-63, 41.0 million in 2065-66); their last slopes reach it in 2066 and 2068; the higher cases in 2058 and 2062. Every baseline passes the 1-in-10 capacity (30.8 million) in 2034. The 2062-63 projection is 2.6 times the long-term capacity. ABS 3222.0 is not held (fetch 4).
3. **Age-sex energy** (`analysis/population_2011/age_sex_energy.csv`): stopped for 2011 and 2025, because ERP by age and sex at those dates is not on disk (fetch 2). On the only age-sex counts held (30 June 2009 and 2010) the national mean requirement at PAL 1.4 is 8.30 MJ, 1.038 times the model's 8.0 MJ, and moves 0.02% in a year.
4. **Partition effect** (`analysis/scale_curve_2025/scale_partition.csv`, `scale_partition_summary.csv`): on the state basis the seven states keep 75% and the 53 regions 44% of national short-term capacity. In 200 random groupings of the 53 regions into 7 groups the median is 85% on the state basis and 91% on the national yield vector; the states keep less than 90% of the random groupings on the national vector. Letting the GAEZ arable share of pasture carry crops lifts the SA2 sum from 37% to 47% (61% on the broad crop set); the national figure does not move.
5. **Diet window** (`analysis/diet_2025/diet_window.csv`): with the FAO window 2014-23 the diet inputs add 3.5 million people to 2025-fixed (4.2 million unrounded) instead of 6.0 million, and national short-term capacity is 39.1 million (39.7 unrounded) instead of 41.5. The 2021-23 window is the lowest-beef window of the series. ABS 4316.0 and an industry series are not held (fetch 3).
6. **2011 window subsets** (`analysis/paper_a/window_subsets_2011.csv`): on the ten three-year subsets, 2011 short-term capacity runs from 32.7 to 34.0 million (33.3 on the five-year mean) and 2025 exceeds it by 22% to 27% on every subset; long term 13.3 to 15.5 million, 2025 exceeds it by 1% to 17%.

Wrong-value check: see the last section.

---

## Item 1. Reference-period table (issue 1)

Files: `reference_periods.py`, `reference_periods.csv`, `reference_periods_national_row.csv` (folder `analysis/population_2011/`).

**The table.** One row per input layer (12 rows). Year conventions: an ABS financial year runs 1 July to 30 June, its midpoint is 1 January of its second calendar year; a window's midpoint is the mean of its years. Population date is 30 June of the data year (ERP). Gaps in years, population date minus window midpoint (and minus window end):

| Layer | 2011 data years | 2025 data years | Gap to midpoint 2011 | Gap to midpoint 2025 | Gap to end 2011 | Gap to end 2025 |
|---|---|---|---|---|---|---|
| Population (ERP) | 30 June 2011 | 30 June 2025 | 0 | 0 | 0 | 0 |
| Cropland area | 2005-06 to 2009-10 (5-year mean) | 2020-21 | 3.50 | 4.50 | 1.00 | 4.00 |
| Pasture area (total grazing) | 2005-06, 2007-08 to 2009-10 (4 years; 2006-07 missing) | 2020-21 | 3.25 | 4.50 | 1.00 | 4.00 |
| Reserve and total area | ABARES CLUM raster, update December 2023 | the same raster | not defined | not defined | | |
| Field-crop yields (12 crops) | 2005-06 to 2009-10 (5-year mean) | 2022-23 to 2024-25 | 3.50 | 1.50 | 1.00 | 0.00 |
| Vegetable, fruit and nut yields | 2005-06 to 2009-10 | 2005-06 to 2009-10 pattern times a 2016-17 to 2020-21 group factor | 3.50 | 6.50 | 1.00 | 4.00 |
| Meat, wool and milk output per hectare | 2005-06 to 2009-10 (5-year mean) | 2020-21 to 2024-25 (5-year mean) | 3.50 | 2.50 | 1.00 | 0.00 |
| Diet shares and red-meat split | thesis defaults (FAO 2010-12 sits close to them) | defaults times the FAO change, 2010-12 to 2021-23 | 0 | 3.00 | -1.50 | 1.50 |
| Liquid fuel per person | thesis default; proxy base year to June 2011 | year to June 2025 | 0.50 | 0.50 | 0 | 0 |
| Weather allowance | thesis table (138 observations) | 153 seasons to 2024-25 | long record | long record | | |
| Organic share | draft paper of February 2016 (about 12 Mha) | 2026 market report (44.4 Mha) | not dated | not dated | | |
| Scale-curve SA land | not used | 2020-21 SA2 land of the 2011 method | | 4.50 | | 4.00 |

**ERP vintage (sources register D31).** One ABS flow serves both years: Data API flow `ABS_ANNUAL_ERP_ASGS2021`, estimated resident population at 30 June, 2021 SA2 boundaries, `data/sa2/population_erp.csv`, file dated 2026-10-27. The 2025 values agree with the ABS Regional population 2024-25 release of 31 March 2026 (V30a checked 8 SA2 values and the 2024-25 growth). The release label of the file and its retrieval date are not recorded in the project, and the API was unreachable at V30a, so the 2011 to 2024 values are unchecked against the ABS. R05a reads the 2011 values as the post-2021-census series; that reading is not checked here.

**Midpoint-population check** (national short-term capacity over the population at the midpoint of the window; population from D31 on the model's 2,450 SA2, scaled so that the end year equals the release population):

| 2025 layer | Population at the midpoint | Capacity over population, short term | Long term |
|---|---|---|---|
| At 30 June 2025 | 27,608,200 | 1.503 | 0.566 |
| Livestock window (midpoint 1 January 2023) | 26,333,942 | 1.576 | 0.593 |
| Field-crop yields (2024.0) | 26,921,680 | 1.542 | 0.580 |
| Land, pasture and cropland (2021.0) | 25,662,102 | 1.617 | 0.609 |
| Vegetable, fruit, nut group factor (2019.0) | 25,143,963 | 1.651 | 0.621 |
| Diet window (2022.5) | 26,013,372 | 1.596 | 0.601 |

The 2011 column is **empty for every window with a midpoint before 30 June 2011** (nothing before that date is in D31, and nothing is estimated). Only the diet row has a 2011 midpoint on the held series (2011.5, ratio 1.491).

**National 2011 row (decision 140).** The national row 22,326,388 becomes the regional sum 22,336,514. Capacity does not move. The seven state rows of `2011-fixed-3` sum to 22,336,514, so **no state figure moves** on that release (the older releases `2011-fixed`, `-2` keep their own state sums, 20,686,860 on `2011-fixed`; they are frozen and unchanged). The national figures that depend on the row (`reference_periods_national_row.csv`):

| Figure | Claim rows | Tier | Before | After | Moves at the printed precision |
|---|---|---|---|---|---|
| People over capacity 2011, short term | A363 | A | 0.670 | 0.671 | yes |
| People over capacity 2011, long term | A363 | A | 1.454 | 1.455 | yes |
| Population growth 2011 to 2025 | A328 | B | 23.7% | 23.6% | yes |
| Capacity over population 2011, average year | A005, A163 | A | 1.4919 | 1.4912 | no (1.49) |
| Same, 1 in 10 and 1 in 20 year | A167, A171, A196 | A | 1.11; 0.89 | 1.11; 0.89 | no |
| Same, 1 in 100 year | A175 | B | 0.68 | 0.68 | no |
| Long-term capacity over the 2011 population | A010 | A | 0.687 | 0.687 | no (69%) |
| Population growth, whole percent | A012 | B | 24% | 24% | no |

The statement text of A363 ("22,326,388 people") and of A369 ("the national row stays at 22,326,388, so the regions sum to 10,126 more") changes; their values 22,336,514; 22,220,341; 22,326,388 are history of the releases and stay as record. Whether the release `2011-fixed-3` itself is rebuilt with the new row is the coordinator's decision (it is frozen); the figures above are what a rebuild gives.

**Sentences for the paper.**

* Section 2 (after the data paragraph): "A data year pairs the production data of its window with the population to be fed at 30 June of that year. The 2011 windows end in June 2010 and are centred on 1 January 2008, 3.5 years before the population date. The 2025 livestock window ends on the population date and is centred on 1 January 2023, 2.5 years before it; the land layer is the single year 2020-21. Set against the population at the midpoint of the 2025 livestock window, 26.3 million, short-term capacity is 1.58 times the population, against 1.50 at 30 June 2025; the same check for 2011 needs the population of 2008, which the series used here does not hold."
* Section 2 or Table S11: "Both populations are the ABS estimated resident population at 30 June by 2021 SA2 (Data API flow ABS_ANNUAL_ERP_ASGS2021, as in the Regional population 2024-25 release of 31 March 2026), shared among the 2011 NRM zones by residential land. The 2011 regions sum to 22,336,514, the national figure used for 2011."
* Table S11 row "Crop yields": the 2011 window is 2005-06 to 2009-10 (five years). The present text says 2006-07 to 2009-10; that is the span the ABS archive holds (`analysis/yield_conversion/README.md`), while the pipeline and the thesis average five years (the 2005-06 cube is in the author's archive; `pipeline/yields/README.md`).
* "About 1.5 in both years" (A005, A328, abstract sentence 4) reads "1.5 at the population date and 1.5 to 1.6 on the 2025 midpoint populations".

## Item 2. Projections against capacity (issue 8)

Files: `projections_against_capacity.py`, `projections_against_capacity.csv` (`analysis/paper_a/`).

**What is held.** Only printed figures: IGR 2023 Table A1.1 (26.5, 30.4, 33.9, 37.3, 40.5 million, 2022-23 to 2062-63) and its population sensitivity (higher case 3.1 million higher by 2062-63; the lower case "broadly symmetric"); Population Statement 2025 Table 1 (27.6 at 30 June 2025, 28.0, 28.3, 31.5 in 2035-36, 41.0 in 2065-66) and Box 7 (about 43 million in 2065-66 on a higher-fertility or higher-migration case); IGR 2021 Table A1.1 (38.8 million in 2060-61). PDFs in the models archive, hashes equal to literature register rows L226 to L228. The ABS Population Projections (3222.0) are not held, so the only variants are the two reports' own. The sensitivity paths between printed points are built as a straight-line excess from 2031-32 and marked "assumed path" in the file; the lower IGR case reads "broadly symmetric" as 3.1 million lower (a reading).

**Years in which each series reaches a capacity** (30 June of the year; capacity held at 2025 data; straight lines between printed points):

| Series | 41.5 M (short, average year) | 39.4 M (herd-cycle low end) | 30.8 M (1 in 10) | 36.5 M (1 in 10, 95th percentile) | 31.1 M (widened 5th percentile) | 49.2 M (widened 95th percentile) |
|---|---|---|---|---|---|---|
| IGR 2023 baseline | not reached; 40.5 in 2063 (0.976); slope reaches it 2066 | 2059 | 2034 | 2051 | 2035 | not reached; slope 2090 |
| IGR 2023 higher (assumed path) | 2058 | 2053 | 2034 | 2046 | 2034 | not reached; slope 2076 |
| IGR 2023 lower (assumed) | not reached; 37.4 (0.901); slope 2082 | not reached | 2035 | 2059 | 2036 | not reached |
| Statement 2025 baseline | not reached; 41.0 in 2066 (0.988); slope 2068 | 2061 | 2034 | 2052 | 2035 | not reached; slope 2092 |
| Statement 2025 higher (assumed path) | 2062 | 2056 | 2034 | 2049 | 2034.5 | not reached; slope 2082 |
| IGR 2021 baseline (superseded) | not reached; 38.8 in 2061 (0.935) | not reached | 2037 | 2054 | 2038 | not reached |

The 5th percentile of the 1-in-10 range (23.1 million) and the 1-in-20 central value (26.3 million) are below the 2025 population (27.6 million), so every series is above them at the start. **Long term:** the 2025 population is 1.77 times the long-term capacity (15.6 million); the 2062-63 projection of 40.5 million is **2.59 times** it (R05a's "2.6 times"), the Statement's 41.0 million 2.62 times; on the widened range ends (13.3 and 18.8 million) 3.04 and 2.16 times.

**Sentences for the paper (section 8.1, replacing the sentence on the 40.5 and 41 million).**

* "Held at 2025 data, the short-term capacity of 41.5 million in an average year is not reached by either baseline within the years it prints: the 2023 Intergenerational Report gives 40.5 million in 2062-63 and the 2025 Population Statement 41.0 million in 2065-66, and the last printed growth of each reaches 41.5 million in 2066 and 2068. In a 1-in-10 year (30.8 million) both baselines pass capacity in 2034. The report's higher-growth case and the Statement's higher-fertility or higher-migration case reach 41.5 million in 2058 and 2062 on a straight-line path between their printed points. The long-term capacity of 15.6 million is 1.8 times below the 2025 population, and the 2062-63 projection is 2.6 times it."
* "Regional projections are out of scope: no official series is published for these 53 regions, and state series on other geographies could be allocated by the method used for the estimated resident population, which we note as a use of the regional results."

## Item 3. Age-sex energy requirement (issue 9): stopped for 2011 and 2025

Files: `age_sex_energy.py`, `age_sex_energy.csv` (`analysis/population_2011/`).

**Stopped.** ERP by age and sex at 30 June 2011 and at 30 June 2025 is not on disk (D31 holds totals). The 2011 and 2025 averages, the change between them, and its sign and size are therefore **not computed**; the file carries empty rows for them. Fetch 2 below.

**What was done with what is held.** The NHMRC Nutrient Reference Values (register A27, file hash equal to the register) give the requirement by age and sex at PAL 1.4 (the sedentary level of the model's diet): Table 1 for ages 0 to 2, Table 2 for 3 to 18, Table 3 for adults at the reference body weights (men 76 kg, women 61 kg). The interpolation reproduces the text's sedentary values for 19 to 30 years, 10.8 MJ (men) and 8.1 MJ (women), to 0.06 MJ, and the script stops if it does not. The table was on disk, so the model's Diet sheet was not needed. The only age-sex counts on disk are the ABS Australian Demographic Statistics June 2010 workbook (Tables 7 and 8: 30 June 2009 and 30 June 2010; `Yield data/ABS - Aust demographics 2010.xls`, not in the sources register):

| Date | Mean requirement, PAL 1.4 | Over the model's 8.0 MJ |
|---|---|---|
| 30 June 2009 | 8.304 MJ | 1.038 |
| 30 June 2010 | 8.302 MJ | 1.038 |

So the model's fixed 8.0 MJ (food groups 7.38 MJ in the evaluator, 8.0 with drinks; V49) is 3.6% below the age-sex weighted mean requirement of the 2010 population, and the mean moved by 0.02% in the one year held. Capacity is proportional to the inverse of the food amount (V49: PAL 1.4 to 1.8 gives a factor 1.271 on the energy and -21.3% on capacity), so the 3.8% gap is a level effect that applies to both years and sits inside the energy choice's range of 1.000 to 1.286. The change between years is the unknown; its sign is expected to be negative per person as the population ages, its size is not in the records.

**Sentence (conditional on the fetch).** "Weighted by the estimated resident population by age and sex at 30 June 2010, the national mean energy requirement at PAL 1.4 is 8.30 MJ a day, 1.04 times the 8.0 MJ of the model's diet; the change in this mean between 2011 and 2025, from the age structure alone, is [to be computed from fetch 2]." Until the fetch the paper can say only the first part.

## Item 4. Scale as a partition effect (issue 10)

Files: `scale_partition.mjs`, `scale_partition.csv` (3,266 rows), `scale_partition_summary.csv` (`analysis/scale_curve_2025/`). Basis: the state yield basis of the paper throughout (a unit takes the yields, climate zone, irrigation and reserve settings of one state's zone). Deterministic (seed 138).

**(a) Real partitions and 200 random groupings of the 53 regions into 7 groups** (2025-fixed, short term, share of national capacity; the real figures equal `results/scale_curve.csv`: 75.4% and 44.0%):

| Basis | Real 7 states | Real 53 regions | Random groupings: median | 5th to 95th percentile | Lowest to highest | Draws below the real states |
|---|---|---|---|---|---|---|
| State basis (main) | 75.4% | 44.0% | 85.4% | 51.9% to 122.5% | 41.4% to 149.2% | 54 of 200 |
| National yield vector (reference) | 75.8% | 32.7% | 90.5% | 73.2% to 99.8% | 57.5% to 100.0% | 19 of 200 |
| State basis, group sizes of the real states | 75.4% | 44.0% | 83.4% | 53.0% to 131.2% | 39.0% to 159.4% | 65 of 200 |
| National vector, group sizes of the real states | 75.8% | 32.7% | 90.1% | 72.7% to 100.0% | 54.5% to 100.0% | 14 of 200 |

On the state basis a group that mixes states takes one state's yields, which can lift the sum above the nation's capacity (shares above 100%); that is the yield-assignment effect named in `scale_curve_2025/README.md`, not a land effect. The national-vector rows remove it: the sum cannot exceed the nation's. There a typical random split into seven groups keeps about 90% of national capacity and the real states 76%: the states are worse than 181 of 200 random groupings. Long term the same reading holds (state basis: real states 49.1%, random median 50.0%, 88 of 200 below; national vector: real states 67.2%, median 78.6%, 39 of 200 below). The 2011 figures (`2011-fixed-3`) are in the file: short term, real states 77.1%, random median 82.3% on the state basis and 90.7% on the national vector (28 of 200 below the states).

**(b) Arable-share relaxation** (2025-fixed, SA2 land of the 2011 method, state basis, short term; share of the unrelaxed national capacity; the national figure does not move because the model hands idle cropland to pasture in any case):

| Level | Unrelaxed | Temperate arable share, full | Half of it | Broad (any field crop) share, full |
|---|---|---|---|---|
| Australia | 100.0% | 100.0% | 100.0% | 100.0% |
| States | 75.4% | 85.6% | 85.6% | 90.3% |
| SA4 | 58.1% | 67.9% | 65.4% | 90.1% |
| SA3 | 43.9% | 52.3% | 52.3% | 70.4% |
| SA2 | 37.4% | 47.4% | 46.7% | 61.0% |

Long term, SA2: 19.8% unrelaxed, 26.9% temperate, 40.1% broad. The rule moved is "pasture never grows crops": the GAEZ share of each SA2 (`data/sa2/arable_share_gaez_by_sa2.csv`, D54) of its pasture is moved to cropping at the unit's own crop yields. It is an upper bound (a suitability model applied to every hectare of pasture, not a measure of what farmers do), and the broad set includes tropical crops. SA2 retains 37% under the model's rule, 47% with arable grazing land growing crops (temperate set), and at most 61%; the loss from pooling the nation into SA2s stays above one third on every treatment.

**(c) Dairy relaxation, held and not rerun** (`analysis/pasture_2025/two_pool.csv`, rows copied into `scale_partition.csv` with the source named): dairy on cropland at observed dairy-farm yields takes the SA2 share from 37.4% to 40.3% (39.0% with the yield halved) of the unchanged national figure; relative to its own national figure (116.4%) SA2 keeps 34.6%.

**Sentences for the paper (section 5 and S2).**

* "The loss follows from the partition and the rule that pasture never grows crops, not from size. Capacity is exactly proportional to land, so a split in which every unit has the national land mix loses nothing. In 200 random groupings of the 53 regions into seven groups, on the national yield vector, the median sum is 91% of national capacity (5th to 95th percentile 73% to 100%); the seven states keep 76% and the 53 regions 33% on the same basis. On the state basis of the figure the states keep 75% and the regions 44%."
* "Letting the arable share of each SA2's pasture carry crops at the unit's own crop yields raises the SA2 sum from 37% to 47% of national short-term capacity (61% on the broad crop set), an upper bound; dairy on cropland at observed dairy-farm yields raises it from 37% to 40%. Both leave the loss from pooling the nation into 2,450 SA2s above one third."

## Item 5. Diet window (issue 14)

Files: `diet_window.py`, `diet_window_eval.mjs`, `diet_window.csv` (`analysis/diet_2025/`). Source: the FAOSTAT food balance bulk file for Australia, 2010 to 2023, food supply quantity (kg per person a year); sha256 of the file equal to `qa/fao_bulk_hashes.csv` (checked in the script). The diet layer's three inputs are recomputed with every available latest window and the base kept at 2010-12 (so the 2011 anchor is the same); the window 2021-23 reproduces the released 12%, 57.8% and the 2025-diet mix and the capacity 41,503,537. The layer's effect is the national short-term capacity of 2025-fixed with the window's three inputs minus the capacity with the 2011 values (13%, 64%, the 1995 mix), everything else at 2025-fixed. FAO beef and veal supply is availability, not intake.

| Latest window | Beef kg a person | Meat and eggs share | Red-meat share | Capacity, million (release rounding) | Diet-input effect, million | Share of the released effect | Capacity, million (unrounded) |
|---|---|---|---|---|---|---|---|
| 2011-13 | 38.2 | 13.0% | 63.7% | 35.8 | 0.28 | 5% | 35.8 |
| 2012-14 | 35.9 | 13.0% | 63.0% | 36.3 | 0.79 | 13% | 36.9 |
| 2013-15 | 34.6 | 12.5% | 62.7% | 37.2 | 1.67 | 28% | 37.2 |
| 2014-16 | 34.1 | 13.0% | 62.3% | 36.9 | 1.35 | 23% | 37.5 |
| 2015-17 | 31.8 | 12.5% | 61.0% | 38.4 | 2.84 | 48% | 38.4 |
| 2016-18 | 30.1 | 12.5% | 60.1% | 39.0 | 3.46 | 58% | 39.0 |
| 2017-19 | 27.3 | 12.5% | 59.3% | 40.0 | 4.42 | 74% | 40.6 |
| 2018-20 | 30.2 | 12.5% | 60.6% | 38.9 | 3.34 | 56% | 38.9 |
| 2019-21 | 29.1 | 12.5% | 59.9% | 39.4 | 3.86 | 65% | 40.0 |
| 2020-22 | 29.1 | 12.5% | 59.7% | 39.4 | 3.86 | 65% | 40.0 |
| **2021-23 (released)** | 25.9 | 12.0% | 57.8% | **41.5** | **5.97** | 100% | 41.5 |
| 2014-23 (10 years, cattle price cycle) | 29.8 | 12.5% | 60.1% | **39.1** | **3.55** | 59% | 39.7 (effect 4.16, 70%) |
| 2010-23 (whole series) | 32.3 | 12.5% | 61.2% | 38.2 | 2.67 | 45% | 38.2 |

Reading. The beef fall is steady across the series (39.1 kg in 2010-12, 25.9 in 2021-23) and 2021-23 is its lowest window; the 2021-23 window sits in the high-price herd-rebuild period. With the cycle-spanning window 2014-23 the diet inputs add 3.5 million people (4.2 million unrounded) instead of 6.0 and national short-term capacity is 39.1 million (39.7 unrounded) instead of 41.5, a fall of 4% to 6% of the released figure; 2025 exceeds 2011 (33.3 million) by 17% to 19% instead of 25%. The release's rounding of the meat-and-egg share to the nearest 0.5 point moves the result by up to 0.6 million within a window (for example 2017-19: 40.0 rounded, 40.6 unrounded). Queensland's capacity falls with the diet change on every window after 2010-12 (its effect is negative), so the regional effect is not uniform; the state rows are in the file. The long-term effect (the red-meat split only) is 0.4 million on the released window and 0.27 million on 2014-23.

**Not widened from disk.** The FAO series is the only consumption series held, so the corroboration (a second source for direction and size) needs the fetches under item 3 of the next section.

**Sentences for the paper (section 3 or 4, and S7).**

* Replace "consumption" wording for the FAO change: "food supply (availability) of beef and veal fell from 39.1 to 25.9 kg a person between 2010-12 and 2021-23".
* "The diet inputs rest on the FAO food-balance change between 2010-12 and 2021-23, the lowest-beef window of the series and a period of herd rebuilding. On the 10-year window 2014 to 2023, which spans the cattle price cycle, they add 3.5 million people to the 2025 capacity instead of 6.0 million (4.2 million unrounded), and national short-term capacity is 39.1 million (39.7 unrounded) instead of 41.5."
* "Fuel, biofuel and timber change the consumption layer by 0.2% or less, so the layer is the diet shares."

## Item 6. 2011 window subsets (issue 21; also issue 2)

Files: `window_subsets_2011.py`, `window_subsets_2011_eval.mjs`, `window_subsets_2011.csv` (1,320 rows), `window_subsets_2011_summary.csv`, `window_subsets_2011_cells.csv` (`analysis/paper_a/`). The yield sheet of 2011 is rebuilt by the pipeline (`pipeline/yields`, from the raw cubes of the author archive) on each three-year subset of 2005-06 to 2009-10 (all ten subsets; three consecutive), each released yield is scaled by subset over five-year pipeline yield, and release `2011-fixed-3` is evaluated for Australia, the seven states and the 53 regions, both presets. The five-year row reproduces the released 33,307,814 and 15,350,146. Only yields change; the land windows (five years of cropping, four of grazing) are not subsetted.

| Subset (financial years) | Consecutive | Short term, million | vs five-year | Regions over capacity (of 53) | 2025 over 2011 | Long term, million | vs five-year | 2025 over 2011 |
|---|---|---|---|---|---|---|---|---|
| Five-year mean (released) | | 33.31 | 1.000 | 22 | 1.246 | 15.35 | 1.000 | 1.018 |
| 2005-06, 2006-07, 2007-08 | yes | 32.72 | 0.982 | 21 | 1.269 | 14.37 | 0.936 | 1.087 |
| 2005-06, 2006-07, 2008-09 | no | 32.98 | 0.990 | 21 | 1.258 | 15.32 | 0.998 | 1.020 |
| 2005-06, 2006-07, 2009-10 | no | 32.71 | 0.982 | 22 | 1.269 | 14.60 | 0.951 | 1.070 |
| 2005-06, 2007-08, 2008-09 | no | 33.15 | 0.995 | 20 | 1.252 | 15.36 | 1.001 | 1.017 |
| 2005-06, 2007-08, 2009-10 | no | 32.88 | 0.987 | 22 | 1.262 | 14.56 | 0.949 | 1.073 |
| 2005-06, 2008-09, 2009-10 | no | 33.15 | 0.995 | 20 | 1.252 | 15.29 | 0.996 | 1.022 |
| 2006-07, 2007-08, 2008-09 | yes | 33.84 | 1.016 | 22 | 1.226 | 14.97 | 0.975 | 1.044 |
| 2006-07, 2007-08, 2009-10 | no | 33.56 | 1.008 | 23 | 1.237 | 13.31 | 0.867 | 1.174 |
| 2006-07, 2008-09, 2009-10 | no | 33.86 | 1.017 | 22 | 1.226 | 15.30 | 0.997 | 1.021 |
| 2007-08, 2008-09, 2009-10 | yes | 34.02 | 1.021 | 21 | 1.220 | 15.49 | 1.009 | 1.009 |

Short term the range is 32.7 to 34.0 million (-1.8% to +2.1%) and 2025 exceeds 2011 by 22% to 27% on every subset, against 24.6% on the five-year mean. Long term the range is wider, 13.3 to 15.5 million (-13.3% to +0.9%), because the long term is crop limited and a three-year subset can drop a poor or good crop year; the 2025 long-term figure exceeds 2011 by 0.9% to 17% (1.8% on the five-year mean), so the long-term comparison, a gain of about 2% on the five-year mean, runs from 1% to 17% across the subsets. The number of regions over capacity in the short term stays between 20 and 23. A cell with a five-year value and no value in a subset is set to zero: 43 to 307 of about 8,100 cells (`window_subsets_2011_cells.csv`); the long-term subset 2006-07, 2007-08, 2009-10 is the one to read with that in mind.

**Sentence for the paper (section 3 and S4).** "Rebuilding the 2011 yields on each three-year subset of the five years 2005-06 to 2009-10, to match the three-year crop window of 2025, moves 2011 short-term capacity between 32.7 and 34.0 million (33.3 million on the five-year mean) and the 2025 figure exceeds it by 22% to 27% on every subset. The long term varies more, 13.3 to 15.5 million, because it is limited by cropland and the subsets drop individual seasons."

---

## Fetches Murray must make (inputs not on disk), with addresses

I had no network, so none of these addresses was opened from this session; each is the ABS or agency page named, taken from the site's own structure, and should be checked when fetched.

1. **ERP for Australia at 30 June 2007 and 30 June 2008** (the 2011 midpoint column of item 1; any ERP before 30 June 2011 is absent from D31). ABS, Historical population: https://www.abs.gov.au/statistics/people/population/historical-population/latest-release (annual ERP, Australia). Archived series: https://www.abs.gov.au/AUSSTATS/abs@.nsf/mf/3101.0 (Australian Demographic Statistics). State the series basis when fetched: pre-2011 figures on the 2011-census rebase differ slightly from the 2021-census series of D31.
2. **ERP by single year of age and sex, Australia, at 30 June 2011 and 30 June 2025** (item 3). ABS, National, state and territory population, Table 59 (Estimated resident population by single year of age, Australia), Data downloads: https://www.abs.gov.au/statistics/people/population/national-state-and-territory-population/latest-release . For a regional adjustment (the 53 regions, if a regional adjustment is wanted): ABS, Regional population by age and sex, SA2 by five-year age groups and sex: https://www.abs.gov.au/statistics/people/population/regional-population-age-and-sex/latest-release (the 30 June 2025 edition may not be published; the latest edition is acceptable if the paper says so).
3. **ABS 4316.0 and an industry consumption series** (item 5, corroboration of direction and size of the beef fall). ABS, Apparent consumption of selected foodstuffs, Australia: https://www.abs.gov.au/statistics/health/health-conditions-and-risks/apparent-consumption-selected-foodstuffs-australia/latest-release ; archived catalogue: https://www.abs.gov.au/AUSSTATS/abs@.nsf/mf/4316.0 . Industry series: ABARES Agricultural commodities (per-person beef and veal consumption, in the commodity statistics tables): https://www.agriculture.gov.au/abares/research-topics/agricultural-outlook/data ; Meat and Livestock Australia market information (domestic beef consumption per capita): https://www.mla.com.au/prices-markets/ . One or two of these is enough for the one-line corroboration.
4. **ABS Population Projections, Australia (3222.0)** (item 2: the ABS series A, B and C and the regional tables, which are not held). https://www.abs.gov.au/statistics/people/population/population-projections-australia/latest-release . Without it the paragraph rests on the two Treasury and Centre for Population reports only, as written.
5. **ERP vintage label and retrieval date for `data/sa2/population_erp.csv`** (item 1): no fetch, a statement from Murray. The file is dated 2026-10-27 and the register has no release label.

## Claim rows that move

**Tier A** (all conditional on decision 140, the national 2011 row at 22,336,514; capacity does not move):

| Id | Tier | Before | After |
|---|---|---|---|
| A363 | A | people over capacity 2011: 0.670 (short), 1.454 (long), "22,326,388 people" | 0.671, 1.455, "22,336,514 people" |

Tier A rows checked and not moving at the printed precision: A005 (1.4919 to 1.4912, prints 1.49), A163 (1.49), A167 (1.11), A171 (0.89), A196 (0.89), A010 (69%), A002 (22.3 million).

**Other tiers:**

| Id | Tier | Before | After |
|---|---|---|---|
| A328 | B | population +23.7% | +23.6% (capacity +24.6% stays) |
| A369 | B | statement text: the national row stays at 22,326,388, regions sum to 10,126 more | text changes: the national row is the regional sum; the values stay as the record of the releases |

Not moving at the printed precision: A175 (0.68), A012 (24%).

**Rows affected in meaning, no register value changed:** A088 (SA2 share 37% stands as a model result under the rule of the model; the relaxation shows 47% to 61%), A376 and A380 (diet layers, 5.6 million, 68%: 3.5 to 4.2 million on the 2014-23 window by the measure of item 5, a different order of the decomposition), A001 to A003 (the direction holds on every 2011 subset).

**New claim rows the paper patch will need (proposed, not written):** item 1 midpoint ratios (1.576, 1.617, 1.542; national row figures above); item 2 reach years (2066, 2068, 2058, 2062, 2034; 2.59 and 2.62 times); item 3 8.30 MJ and 1.038; item 4 the random-grouping medians and the arable-share shares (47%, 61%; 91%, 76%, 33%); item 5 3.5, 4.2, 39.1, 39.7 million; item 6 the 32.7 to 34.0 and 13.3 to 15.5 million ranges and 22% to 27%. A register row for the ABS June 2010 demographics workbook (item 3) is also needed.

**Register rows touched: none** (claims, sources, literature, defects).

## Files changed (all new)

* `analysis/paper_a/README_round2_B138.md`
* `analysis/paper_a/projections_against_capacity.py`, `projections_against_capacity.csv`
* `analysis/paper_a/window_subsets_2011.py`, `window_subsets_2011_eval.mjs`, `window_subsets_2011.csv`, `window_subsets_2011_summary.csv`, `window_subsets_2011_cells.csv`
* `analysis/paper_a/check_B138.py`
* `analysis/population_2011/reference_periods.py`, `reference_periods.csv`, `reference_periods_national_row.csv`
* `analysis/population_2011/age_sex_energy.py`, `age_sex_energy.csv`
* `analysis/scale_curve_2025/scale_partition.mjs`, `scale_partition.csv`, `scale_partition_summary.csv`
* `analysis/diet_2025/diet_window.py`, `diet_window_eval.mjs`, `diet_window.csv`
* `qa/reports/B138_paper_A_smaller_computations.md`

## Notes for the coordinator

* The brief names `analysis/population_2011/README.md`; that file does not exist (the folder holds scripts and csv files only), so the 2011 population route was read from `qa/reports/B110_zone_populations_2011.md`, ERRATA error 10 and the register.
* Table S11 gives the 2011 crop-yield window as four years; the pipeline uses five (item 1).
* The FAO bulk file used in item 5 is at `/tmp/claude-0/fao/x/` (outside the repository); its hash equals the register. The 2011 subsets (item 6) need the private archive, as `pipeline/yields/verify_end_to_end.py` does.
* Item 4 takes about ten minutes to run; items 1, 2, 3 and 5 take under a minute, item 6 under a minute plus the evaluation.

## Wrong-value check

`python3 -I analysis/paper_a/check_B138.py --wrong` runs 37 real comparisons (all `ok`: the five-year row against the released capacities, the ratios, the midpoint population by a second route, the regional-sum ratio, the reach year worked by hand, the 2.6 times, the age-sex shares, the real partitions against `results/scale_curve.csv`, the diet window 2021-23 against the released capacity), followed by three deliberate wrong values, each of which must fail. **Example, not to be used:** the five-year Australia short-term capacity entered as 33,300,000, the IGR 2023 reach year of the widened 5th percentile entered as 2040, and the 2011 capacity over the regional sum entered as 1.52. Output:

```
FAIL TEST | five-year Australia short capacity entered as 33,300,000 | got 33307814 | expected 33300000 | tolerance 0.0
FAIL TEST | IGR 2023 base reaches the widened 5th percentile entered as 2040 | got 2035.0 | expected 2040 | tolerance 0.051
FAIL TEST | national 2011 ratio entered as 1.52 | got 1.491182 | expected 1.52 | tolerance 5e-07
```
