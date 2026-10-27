# E9 back-test: does pooling thin regions toward their state beat the plain mean?

Result: **no. Pooling as designed is not worth building.** (SCOPE.md E9: not adopted.)

Run: `python3 -I analysis/yield_pooling/backtest.py` from the repository root. Method and data are in the docstring of `backtest.py`; figures in `backtest.csv` and `backtest_window.csv`.

## The test

Hold out one year of the ABS crop data 2016-17 to 2020-21 (55 NRM regions, every reported crop); estimate each region's yield for that year, relative to the national yield of the same year, from the other years; compare with what the region actually yielded.
The current estimator is the plain mean of the region's own years. The pooled estimator moves the mean toward the mean of the other regions of the same state, by more the less area the region has (`w = n a / (n a + k)`). The scale `k` was chosen on the first three held-out years and judged on the last two.

## Result

| Estimator | Mean error (last two years) | Median error | Area-weighted error | Misses over 2-fold |
|---|---|---|---|---|
| Plain mean (current) | 0.338 | 0.224 | 0.190 | 12.1% |
| Pooled, best k on the training years (k = 30 ha-years) | 0.332 | 0.229 | 0.190 | 11.5% |

Error is |log(estimate / actual)|, so 0.34 is a typical miss of about 40%. Pooling improves the mean by 2%, makes the median slightly worse, and does not change the area-weighted error that the capacity calculation feels. A stronger pull toward the state mean makes every measure worse (k = 100,000: mean error 0.397). The other regions of a state are a poor guide to a region's own productivity.

## What does matter

Most of the error is the weather of the held-out year, which no estimator of the average can predict. A longer window helps only slowly (plain mean of the other years, all combinations):

| Years averaged | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Mean error | 0.358 | 0.338 | 0.330 | 0.324 |
| Area-weighted error | 0.213 | 0.190 | 0.181 | 0.176 |

The 2025 matrix uses three years. Going to a fourth or fifth would improve the area-weighted error by about 3% to 5%, which is as much as any pooling, and would also reduce the dependence on the record year 2022-23 (SCOPE.md E10).

## What this does not show

* Only a state-mean prior was tried. Other priors (the region's own 2011 yield, or its productivity in related crops) were not.
* The test uses the 2016-21 NRM regions, not the 60 zones with SA2 allocation; the 2022-25 data has only three years, too few to hold out one and keep a mean of two.
* The Northern Territory's large swings in the sensitivity run come from the herd and meat window and the choice of crop year, which is weather and the herd cycle, not estimation noise. That is what E10 (capacity in a bad year) addresses.
* The plausibility rules (3x and 0.1x the national yield) were kept in this test and not tested alone.

## Decision

Do not build E9. Keep the three-year mean with the plausibility rules. Consider a longer crop window when E10 shows how much the choice of years moves the result.
