# Paper A, second round: the smaller computations (brief B138, decision 138)

New files only. Nothing in `analysis/sensitivity_2025/`, nothing existing in `analysis/paper_a/`, no frozen release, no file of `results/`, no paper file and no register file was edited. Report: `qa/reports/B138_paper_A_smaller_computations.md` (figures, the sentences for the paper patch, claim rows that move, the fetches Murray must make).

| Item | Issue (R05a) | Script | Output | Folder |
|---|---|---|---|---|
| 1 Reference-period table, midpoint check, national row | 1 | `reference_periods.py` | `reference_periods.csv`, `reference_periods_national_row.csv` | `analysis/population_2011/` |
| 2 Projections against capacity | 8 | `projections_against_capacity.py` | `projections_against_capacity.csv` | `analysis/paper_a/` |
| 3 Age-sex energy requirement | 9 | `age_sex_energy.py` | `age_sex_energy.csv` (2009 and 2010 only; 2011 and 2025 need a fetch) | `analysis/population_2011/` |
| 4 Scale as a partition effect | 10 | `scale_partition.mjs` | `scale_partition.csv`, `scale_partition_summary.csv` | `analysis/scale_curve_2025/` |
| 5 Diet window over the cattle price cycle | 14 | `diet_window.py`, `diet_window_eval.mjs` | `diet_window.csv` | `analysis/diet_2025/` |
| 6 2011 window subsets | 21 (also 2) | `window_subsets_2011.py`, `window_subsets_2011_eval.mjs` | `window_subsets_2011.csv`, `window_subsets_2011_summary.csv`, `window_subsets_2011_cells.csv` | `analysis/paper_a/` |
| Check of all six | | `check_B138.py` (`--wrong` adds three deliberate wrong values that must fail) | printed | `analysis/paper_a/` |

## How to rerun (repository root unless stated)

* Item 1: `python3 -I analysis/population_2011/reference_periods.py`
* Item 2: `python3 -I analysis/paper_a/projections_against_capacity.py`
* Item 3: `python3 -I analysis/population_2011/age_sex_energy.py` (needs `xlrd`; reads the ABS June 2010 demographics workbook in the models archive)
* Item 4: `cd web && node ../analysis/scale_curve_2025/scale_partition.mjs` (about ten minutes of computation; needs the built data, `npm run build:data`)
* Item 5: `python3 -I analysis/diet_2025/diet_window.py [FBS_CSV]` (the FAOSTAT food balance bulk file; its sha256 is checked against `qa/fao_bulk_hashes.csv`)
* Item 6: `MODELS_DIR=/path/to/Models python3 -I analysis/paper_a/window_subsets_2011.py` (needs the private archive, as `pipeline/yields/verify_end_to_end.py` does)
* Check: `python3 -I analysis/paper_a/check_B138.py` and `... --wrong`

All are deterministic (the random groupings use a seeded generator, seed 138).

## What each output is, in plain words

**Item 1.** `reference_periods.csv` has one row per input layer. Columns give the data years in 2011 and 2025, the window midpoint and end as decimal years, the population date (30 June), the gap in years from the midpoint and from the window end, the ERP vintage, the population at the midpoint of each 2025 window (from the ERP of source D31, scaled so the end year equals the release population), and the short-term capacity over that population. The 2011 midpoints (about 1 January 2008) lie before 30 June 2011, the first ERP date held, so those cells are empty; nothing is estimated. `reference_periods_national_row.csv` gives the national figures that depend on the Australia population row, on 22,326,388 and on 22,336,514 (decision 140), with the claim rows. Capacity does not move.

**Item 2.** The series are the printed points of IGR 2023 (Table A1.1), the 2025 Population Statement (Table 1) and IGR 2021 (Table A1.1), with the two sensitivity cases built as a straight-line excess (marked "assumed path"). ABS 3222.0 is not held. For each series and each capacity threshold the file gives the year reached, or says the printed points stop below it and shows the last printed value over the threshold and the year the last printed slope would reach it (an extrapolation, marked). Regional projections are out of scope: no official series is published for the 53 regions.

**Item 3.** Stopped for the 2011 and 2025 averages: ERP by age and sex at 30 June 2011 and 2025 is not on disk. The file holds the requirement by age and sex (NHMRC Nutrient Reference Values, PAL 1.4, checked against the text's 10.8 and 8.1 MJ) and the 2009 and 2010 averages from the ABS June 2010 workbook, which are the only age-sex counts held. The ABS workbook is not in the sources register.

**Item 4.** `scale_partition.csv` rows: `real_partition` (7 states and 53 regions, state basis, and on the national yield vector as a reference), `random_grouping` (200 groupings of the 53 regions into 7 groups, two ways, on the state basis and on the national yield vector), `arable_relaxation` (SA2 land, 2025-fixed, GAEZ arable share of pasture moved to cropping, at the unit's own crop yields), and `dairy_relaxation_held` (copied from `analysis/pasture_2025/two_pool.csv`, not rerun). `scale_partition_summary.csv` holds the distribution of the random groupings.

**Item 5.** For each FAO three-year window (2010-12 to 2021-23), the 10-year window 2014-23 and the whole series 2010-23: the three diet inputs (meat-and-egg share, red-meat share, the red-meat split), and the national and state capacity of 2025-fixed with them, short and long term, with the release's rounding and unrounded. The layer's effect is the capacity less the capacity with the 2011 values of the three inputs. The 2021-23 row reproduces the released 41,503,537.

**Item 6.** Capacity of 2011-fixed-3 with the yields rebuilt from each three-year subset of the five archive years (all ten subsets; three are consecutive), for Australia, the seven states and the 53 regions, short and long term, with the 2025-fixed to 2011 ratio. Only yields change. The five-year row reproduces the released 33,307,814 and 15,350,146.

## Limits that matter

* Item 6 varies yields only; the 2011 land windows (five years of cropping, four of grazing) are not subsetted. A cell that has a value in the five-year mean and none in a subset is set to zero (the pipeline's fill rule supplies a value only where the author marked the pair suitable); `window_subsets_2011_cells.csv` counts them. The long-term result is the more sensitive one.
* Item 4's arable relaxation is an upper bound on what letting arable grazing land carry crops can do: the GAEZ share is a model result on suitability, applied to every hectare of the SA2's pasture. The national capacity does not move (the model hands idle cropland to pasture in any case), so the effect is on fine scales.
* Item 5's capacity effect is the diet inputs measured last on 2025-fixed. It is not the decomposition's consumption layer (A376) or red-meat-mix layer (A380), which sit in a chain that also moves fuel, biofuel, timber and the organic share, and are averaged over orderings. A window-based variant of those two rows needs the same measurement made in the decomposition; this folder gives the national effect on 2025-fixed only.
* Item 1: Supplementary Table S11 gives the 2011 crop-yield window as 2006-07 to 2009-10 (four years). The pipeline and the thesis use five years, 2005-06 to 2009-10. The table here uses five; S11 needs the same.
