# The resilience (climate variability) table, reproduced and updated (SCOPE.md E14)

The long-term settings ask the land to feed the population through a given number of years of weather: the setting is 100 years, and the harvest is scaled to the worst year expected once in that time. Without the setting the long-term figure for Australia would be 27.0 million instead of 12.3 (`analysis/long_term_2025/`), so the table behind it is the largest single lever of the long term.
It is the `resilience` sheet of the workbook: for Australia and each state, a factor for return periods of 1 to 150 years. This folder reproduces it from the thesis workings, updates its data to 2024-25, tests alternatives, and quantifies its uncertainty.
Reproduce: `python3 -I analysis/resilience_2025/resilience.py ARCHIVE_XLS HISTORIC_XLSX` (the archive workbook `prelim models/resilience 150 years.xls`, and the ABS `Historic Ag Commodities_1860 to 2022.xlsx` from the Agricultural Commodities, Australia 2021-22 release), `node analysis/resilience_2025/evaluate_tables.mjs analysis/resilience_2025/capacity_by_table.csv`, `python3 analysis/resilience_2025/write_readme.py`.

## 1. The thesis method is reproduced exactly

From the archive workbook: for each location and year, the unweighted mean of the wheat, oats and barley yields (t/ha); a reference that is the mean of the 10 observations from 5 before to 4 after the year (the window is held at the first or last 10 observations at the ends); the ratio of yield to reference; the ratios ranked from worst, rank k read as a one-in-(n+1)/k year event; anchors at 1, 3, 5, 10, 20, 30, 50 and 150 years, and straight-line interpolation between them (so the 100-year factor is the midpoint of the 50 and 150 year anchors).
`resilience.py` reproduces every anchor of the archive's table for Australia and the six states to machine precision (`replication.txt`), and the workbook's 150-year table exactly (a model evaluation with the reproduced table gives 12,305,891 for Australia, the same as the workbook).

## 2. The data update changes little

The ABS historical series (to 2021-22) and the three recent cubes extend the record from 138 to 153 observations. The same method on this data (release `2025-resilience`; the other tables are shown for comparison):

| Location | 5 yr | 10 yr | 20 yr | 50 yr | 100 yr | 150 yr |
|---|---|---|---|---|---|---|
| Australia | 0.866 | 0.741 | 0.599 | 0.552 | 0.456 | 0.359 |
| New South Wales | 0.827 | 0.561 | 0.407 | 0.344 | 0.300 | 0.257 |
| Victoria | 0.857 | 0.692 | 0.474 | 0.282 | 0.218 | 0.153 |
| Queensland | 0.790 | 0.675 | 0.492 | 0.405 | 0.347 | 0.289 |
| South Australia | 0.843 | 0.701 | 0.500 | 0.440 | 0.359 | 0.278 |
| Western Australia | 0.889 | 0.792 | 0.730 | 0.689 | 0.491 | 0.294 |
| Tasmania | 0.910 | 0.834 | 0.762 | 0.688 | 0.669 | 0.651 |

Thesis table above; data to 2024-25 below.

| Location | 5 yr | 10 yr | 20 yr | 50 yr | 100 yr | 150 yr |
|---|---|---|---|---|---|---|
| Australia | 0.892 | 0.742 | 0.634 | 0.552 | 0.456 | 0.359 |
| New South Wales | 0.806 | 0.550 | 0.425 | 0.344 | 0.300 | 0.257 |
| Victoria | 0.857 | 0.682 | 0.479 | 0.282 | 0.218 | 0.153 |
| Queensland | 0.766 | 0.663 | 0.527 | 0.405 | 0.347 | 0.289 |
| South Australia | 0.843 | 0.701 | 0.509 | 0.429 | 0.353 | 0.278 |
| Western Australia | 0.889 | 0.792 | 0.730 | 0.648 | 0.471 | 0.294 |
| Tasmania | 0.906 | 0.834 | 0.764 | 0.688 | 0.665 | 0.643 |

* **Australia's 100-year and 150-year factors do not change** (0.456 and 0.359): the worst year in the record is still 1915, and the second worst is old. The 5 and 20 year factors rise (0.866 to 0.892 and 0.599 to 0.634): the record now holds recent good years.
* Western Australia's 50 and 100-year factors fall (0.689 to 0.648, 0.491 to 0.471); South Australia's and Queensland's move by a few hundredths.
* Long-term capacity at 100 years (millions): Australia unchanged, Western Australia 1.86 to 1.78, South Australia 0.89 to 0.88; the short term is unchanged (resilience of one year is a factor of 1).
* The recent years are consistent with the table: the worst of eight recent single years gives a long-term capacity about 85% of their mean (`analysis/reliability_2025/`), between the table's 0.87 at five years and 0.74 at ten.

## 3. How uncertain the 100-year factor is

A one-in-100-year event estimated from about 150 years is an extrapolation, and the table hides how uncertain it is. Fitting a generalised Pareto distribution to the worst 20% of years (on the leave-one-out ratios below) and resampling the years 500 times gives:

| Location | Thesis table, 100 yr | 90% interval for a fitted tail, 100 yr |
|---|---|---|
| Australia | 0.46 | 0.32 to 0.54 |
| New South Wales | 0.30 | 0.02 to 0.27 |
| Victoria | 0.22 | 0.13 to 0.39 |
| Queensland | 0.35 | 0.22 to 0.46 |
| South Australia | 0.36 | 0.19 to 0.42 |
| Western Australia | 0.49 | 0.41 to 0.65 |
| Tasmania | 0.67 | 0.58 to 0.70 |

For Australia the 100-year factor could plausibly lie anywhere from 0.32 to 0.54, which scales the long-term capacity at 100 years from about 8.7 to 14.5 million (the figure is 12.3). The state intervals are wider still (New South Wales 0.02 to 0.27). **The fitted tail should be used to state the uncertainty, not to replace the table**: its point estimates are unstable by state (New South Wales falls from 0.30 to 0.19, Western Australia rises from 0.49 to 0.54).

## 4. Alternatives tested

* **Leave-one-out reference.** The thesis reference includes the year itself, so a very bad year pulls its own reference down by a tenth of its shortfall and the ratio is closer to 1 than the year deserves. A reference from the 20 other nearest observations removes that. It lowers Australia's 100-year factor from 0.456 to 0.415 (long-term capacity 11.21 million, -9%) and the state capacities by 7% to 10%. The effect is real and the thesis choice is a mild bias, so it is published as the alternate release `2025-resilience-loo` (an alternate of `2025-resilience`, not a later layer); the default stays the thesis method on updated data.
* **A fitted tail as the table**: see section 3; unstable.
* **Weighting the three grains by area**, **dropping the artefacts** (an unplanted grain counted as a yield of 0 in the early years, Queensland barley before 1871), and **a smoother trend** than a moving average were not tested.

## 5. Storage and the length of a drought

The table asks the population to meet its needs in the single worst year. A population holding a store of grain is bound instead by the worst run of consecutive years, whose average yield is higher. With the leave-one-out reference, the 100-year factor for the worst run of d consecutive years (a store of d-1 years of consumption):

| Location | Single worst year (no store) | worst 2 years (1 year of store) | worst 3 years | worst 5 years |
|---|---|---|---|---|
| Australia | 0.4154 | 0.6224 | 0.7047 | 0.8098 |
| New South Wales | 0.2744 | 0.4595 | 0.5507 | 0.7189 |
| Victoria | 0.1966 | 0.4951 | 0.5654 | 0.7439 |
| Queensland | 0.3238 | 0.5141 | 0.6131 | 0.67 |
| South Australia | 0.3299 | 0.5216 | 0.6036 | 0.7195 |
| Western Australia | 0.4397 | 0.6658 | 0.7274 | 0.8018 |
| Tasmania | 0.6285 | 0.7077 | 0.7556 | 0.8084 |

For Australia a store of one year of consumption lifts the 100-year factor from 0.42 to 0.62, and two years to 0.70; as capacity is proportional to the factor that is 11.2, 16.8 and 19.0 million. The model has no store input, so the 100-year setting is implicitly a population with no reserves of food. Offering a storage input is a design choice (SCOPE.md E15), not an update of data.

## Limits

* The series is three grains, yield only. Pasture, livestock, horticulture and the correlation of failures between crops are not in it; the factor scales all of the harvest.
* State series are for the states; regional zones use their state's row, so a small region's own variability is understated.
* Early observations (1861, 1866, 1871, then annual from 1876) are sparse, and early yields reflect the farming of the time.
* NSW in the 2022-23 to 2024-25 cubes includes the ACT; the historical series is NSW alone. The Northern Territory takes South Australia's row, as in the thesis.

## 6. Grain store as a scenario (2026-10-28)

`store.py` builds the full 150-year table for a population holding a store of s years of consumption (the worst run of s + 1 consecutive years instead of the worst year), with the model's own method on the series to 2024-25 (`store_tables.csv`; the s = 0 table is checked to equal the model's, and `resilience.py` reproduces the committed `tables.csv` exactly). The 100-year factor for Australia:

| Store | none | 1 year | 2 years | 3 years | 4 years |
|---|---|---|---|---|---|
| Factor at 100 years | 0.456 | 0.677 | 0.750 | 0.815 | 0.882 |

Two scenario releases on `2025-improved`, `2025-store-1` and `2025-store-2`, use the 1 and 2 year tables. Australia, long term: **12.0 million with no store, 17.8 million with one year of grain, 19.7 million with two** (+48% and +64%; capacity is proportional to the factor). The short term does not change.
Read these as the upper end of what a store can do, not as a result: **the store is free in the model** (no land for the grain held, no storage losses, no refilling after a drawdown), and a store of a year of consumption is a large physical stock (the long-term diet produces about 147 kg of cereals a person a year, so a year of cereals alone is about 4 million tonnes for 27.6 million people, and a year of all food as produced is 1.2 tonnes a person, much of it perishable). The earlier figures with the leave-one-out reference were 0.62 and 0.70 (`storage.csv`).
A costed store, and the store as a dashboard switch among the tables shipped in a release instead of a release of its own, belong to the rebuild (IDEAS.md).
