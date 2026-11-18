# V48: blind check of B133 (paired draws, 2011 on the 2025 weather table, failure-probability range)

Checker report. Brief: `qa/briefs/V48_check_B133.md`; rules `qa/briefs/_checker_rules_results_wave.md`. My own figures were derived first, with my own code in my scratch folder (`.../scratchpad/v48/`: `paired.mjs`, `shock.mjs`, `fail.py`, `summ.py`, `more.py`, `cmp.py`), before I opened the B133 report, `monte_carlo_paired.mjs`, its draws, `results/paired_change_2011-2025.csv`, `shocks_2011_on_2025_table*.csv` or `failure_probability_range.csv`. No git, no subagents, no network; no repository file edited except this report.

## 1. Tolerance

* Counts, region names and statuses: exact.
* Deterministic figures (2011 on either table; failure range from the B115 draws): capacities within 0.5%; shares, ratios and percentages within one unit of the last printed digit.
* Monte Carlo figures (my 500 independent draws against the builder's 2,000): the gap must be within twice the combined sampling error. My error is from 2,000 bootstrap resamples of my draws; the builder's is taken as half of mine (four times the draws; its Latin hypercube makes this conservative). A share of draws with a fall is checked the same way with the binomial error; a zero count against a zero count passes.

## 2. Wrong-value example

`cmp.py` applies those tolerances. The true values pass (exit 0): short-term all-draws p95, builder 16.48 against mine 15.88, allowed 0.64; failure linear p5, 2.33 against 2.33. **Example of a deliberate wrong value:** quoting 13.0 for that p95 and 3.9 (the 13-choice figure) for the failure p5:

```
short all p95 (WRONG: 13.0): builder 13.0, mine 15.88, tol 0.66: FAIL
fail linear p5 (WRONG: 3.9): builder 3.9, mine 2.33, tol 0.1: FAIL
exit 1
```

## 3. My figures

### 3.1 Paired draws (500 draws, my own seed, plain random numbers, national)

My sampler evaluates both releases itself. The 2025 side uses the work folder of an earlier job (`scratchpad/b132/work`, read only) for the 2025-only yield choices; checked against seven rows of block A of `monte_carlo_draws_2025-fixed_wide.csv`, it reproduces the 2025 capacities to within 0.001% (the file rounds the choices to five decimals). At the release settings it gives 41,503,537 and 15,623,209 (2025) and 33,307,814 and 15,350,146 (2011).

Shared choices, drawn once per draw and applied to both years: energy (food amount x 1 to 1.8/1.4, short term), avoidable waste (12% to 14%, both years' base is 12%), loss-factor weight (the 474 Base cells hold the same US values in both releases, checked), default organic factor (the 119 cells hold 0.8083 in both, checked), meat-and-egg share and red-meat share (2025 drawn on its triangle; 2011 = 0.13 x d/0.12 and 0.64 x d/0.578), resilience table (long term; coin 1 puts the `2025-resilience-loo` cells into both years; nationally the thesis and 2025 tables are equal at 100 years, 0.4558, and the leave-one-out value is 0.4154). The 12 2025-only choices are drawn for 2025 only.

Millions of people, 2025 minus 2011 (p5, p50, p95; bootstrap 95% intervals in brackets):

| Preset | Basis | n | Draws with a fall | Difference |
|---|---|---|---|---|
| short | shared choices only | 500 | 0 (0.0%; 95% upper bound 0.8%) | 6.59 [6.49, 6.65], 7.44 [7.39, 7.51], 8.44 [8.36, 8.55] |
| short | all draws | 500 | 0 (0.0%; upper bound 0.8%) | 2.60 [2.30, 2.84], 8.31 [7.93, 8.83], 15.88 [15.32, 16.44] |
| short | holdings land only | 259 | 0 | 2.19, 6.13, 9.95 |
| long | shared choices only | 500 | 0 (0.0%) | 0.23 [0.23, 0.24], 0.26, 0.29 |
| long | all draws | 500 | 135 (27.0%, s.e. 2.0) | -0.79 [-0.90, -0.73], 0.87 [0.72, 1.37], 3.33 [3.26, 3.39] |
| long | holdings land only | 259 | 52.1% | -0.94, -0.03, 0.81 |

Unpaired share (2025 draws below 2011 at its base): short 11.0% all draws, 19.7% holdings, 6.0% shared only; long 44.0%, 81.1%, 62.4%. 2011 on the shared choices: short 26.6, 30.2, 35.0; long 13.6, 14.5, 15.8.

### 3.2 2011 on the 2025 weather table (`2011-fixed-3`, short-term settings, resilience sheet of `2025-fixed` swapped in)

| Basis | 1 in 10: people over capacity (capacity over population) | 1 in 20 | Regions over capacity of 53, 1 in 10 / 1 in 20 | Tipping from the average year, 1 in 10 / 1 in 20 |
|---|---|---|---|---|
| 2011, thesis table | 0.9045 (1.1056) | 1.1188 (0.8938) | 25 / 26 | 3 / 4 |
| 2011, 2025 table | 0.9029 (1.1075) | 1.0568 (0.9462) | 25 / 26 | 3 / 4 |
| 2025 | 0.8961 (1.1160) | 1.0488 (0.9535) | 21 / 24 | 5 / 8 |

No region changes status between the two 2011 tables at 1 in 10 or 1 in 20. Tipping regions: 2011 (either table) Burnett Mary, Corangamite, North East Vic at 1 in 10, plus Murrumbidgee - ACT at 1 in 20; 2025 Burnett Mary, Mackay Whitsunday, North East Vic, Rangelands, Wet Tropics at 1 in 10, and at 1 in 20 those five plus Murrumbidgee - ACT, North Tasmania and Southern Gulf (eight).

### 3.3 Failure range (block A, 2,000 draws, short term, Australia row of the 2025-fixed table, population 27,608,200)

| Interpolation | p5 | p50 | p95 |
|---|---|---|---|
| linear in return period (the table's own rule; same on every column or on its anchors 1, 3, 5, 10, 20, 30, 50, 150) | 2.33% | 7.59% | 19.35% |
| log-linear between the table's anchors 1, 3, 5, 10, 20, 30, 50, 150 | 2.39% | 8.02% | 19.54% |
| log-linear between Paper B's run points 1, 5, 10, 20, 50, 100 (`fearnside_failure_curve.py`) | 2.22% | 8.02% | 19.54% |
| linear between Paper B's run points | 2.14% | 7.59% | 19.35% |

Draws failing in an average year: 9. None beyond the last point. Base: 17.14 years, 5.835% linear; 16.40 years, 6.098% log. The same code with a wrong population (28,608,200) gives 3.4%, 9.3%, 23.2%, so it can fail.

## 4. Comparison

| Item | Builder | Mine | Verdict |
|---|---|---|---|
| Short, all draws: share with a fall | 0.0% | 0.0% (upper 0.8%) | pass |
| Short, all draws: p5, p50, p95 | 2.32, 8.43, 16.48 | 2.60, 8.31, 15.88 | pass (p95 gap 0.60 against 0.64 allowed: the closest call) |
| Short, all draws: ratio | 1.076, 1.277, 1.532 | 1.085, 1.272, 1.512 | pass |
| Short, shared only | 6.55, 7.43, 8.45; ratio 1.236 to 1.253 | 6.59, 7.44, 8.44; 1.236 to 1.253 | pass |
| Short, holdings only | 1.87, 6.02, 9.64; no fall | 2.19, 6.13, 9.95 (n 259); no fall | pass (within sampling error of n 259) |
| Short, unpaired share (2025 below 2011 base) | 13.2% all, 25.2% holdings, 7.5% shared | 11.0%, 19.7%, 6.0% | pass (1.5, 1.8 and 1.2 combined s.e.) |
| Short, 2011 distribution | 26.3, 30.3, 34.8 | 26.6, 30.2, 35.0 | pass |
| Long, all draws: fall | 26.1% | 27.0% (s.e. 2.0) | pass |
| Long, all draws: p5, p50, p95 | -0.87, 1.08, 3.40 | -0.79, 0.87, 3.33 | pass (p50 inside my interval 0.72 to 1.37) |
| Long, holdings: fall; difference | 52.2%; -0.98, -0.05, 0.80 | 52.1%; -0.94, -0.03, 0.81 | pass |
| Long, shared only | 0.24, 0.26, 0.29; no fall | 0.23, 0.26, 0.29; no fall | pass |
| Long, unpaired | 41.9%, 77.7%, 63.2% | 44.0%, 81.1%, 62.4% | pass |
| Per-row cells of `monte_carlo_draws_paired_2011-2025.csv` (rows 0, 1, 17, 333, 1000, 1999 rerun with my evaluator) | cap2011 and cap2025_shared_only, both presets | identical to the person, except 2011 long-term rows with restable 1, 6 to 7 people apart (the builder scales the thesis table by the leave-one-out ratio; I swap in the leave-one-out table) | pass |
| 2011 thesis table, 1 in 20 / 1 in 10 (people over capacity) | 1.119 / 0.904 | 1.1188 / 0.9045 | pass |
| 2011 on 2025 table | 1.057 / 0.903 | 1.0568 / 0.9029 | pass |
| 2025 | 1.049 / 0.896 | 1.0488 / 0.8961 | pass |
| Capacity over population (thesis, 2025 table, 2025) at 1 in 20 | 0.894, 0.946, 0.953 | 0.8938, 0.9462, 0.9535 | pass |
| Regional cells of `shocks_2011_on_2025_table.csv`, return periods 1, 10, 20, three bases (486 cells) | | 0 mismatches, largest difference 0 | pass |
| Regions over capacity, tipping counts and tipping names | 25/26, 3/4 (both 2011 tables); 21/24, 5/8 | same, names identical | pass |
| No region changes status between 2011 tables | none | none | pass |
| Failure, linear p5, p50, p95 | 2.33%, 7.59%, 19.35% (report: 2.3, 7.6, 19.4) | 2.33%, 7.59%, 19.35% | pass |
| Failure, log-linear | 2.39%, 8.02%, 19.54% | 2.39%, 8.02%, 19.54% on the table's anchors | pass on the builder's definition; see 6(a) |
| Draws failing in an average year | 9 | 9 | pass |
| Base 5.84% / 6.10% | 17.1 y, 5.84%; 16.4 y, 6.10% | 5.835%, 6.098% | pass |
| A223: 2011 on the 2025 table at 1 in 10 | -25.8% | -25.76% | pass |

Nothing I computed changes a number of the builder's outputs.

## 5. The proposed sentences (report section 3) and the claim rows

**Sentences.**
* **Section 9.1 (amends decision 115's wording): overclaims as drafted.** "On the seven choices both years share, drawn with common random numbers, 2025 short-term capacity is above 2011's in every one of 2,000 draws (difference 2.3 to 16.5 million ...)" attaches the all-draws range to the seven shared choices. On the shared choices alone the difference is 6.5 to 8.4 million; 2.3 to 16.5 is with the 12 2025-only choices drawn for 2025 and 2011 held at its single values on them. Suggested: "On the seven choices both years share, drawn with common random numbers, 2025 short-term capacity is above 2011's in all 2,000 draws: by 6.5 to 8.4 million (5th to 95th percentile) on those choices alone, and by 2.3 to 16.5 million when the 2025-only data choices are drawn for 2025 as well (1.9 to 9.6 on holdings land only). 2011 is not sampled on the 2025-only choices." Also: "The 13% ... overstates the doubt" should name what it is ("the share of 2025 draws below 2011's base value, an unpaired comparison"). The long-term part ("26% of the draws fall, 52% on holdings land only") holds. Amending decision 115's sentence is Murray's decision row, as the builder says.
* **Abstract:** holds, with one care: "above 2011's in all 2,000 paired draws ... when the 2025-only data choices are drawn as well" should add "for 2025" so it is not read as 2011 being drawn on them. "None of 2,000" supports "in every draw", not "certainly": the 95% upper bound on the share with a fall is about 0.15%.
* **Section 8.1, margin at 1 in 20: mild overclaim.** "On one weather table the two years are the same" (1.057 against 1.049) and "The improvement from 1.12 to 1.05 is the table, not the data": of the 0.070 fall in people over capacity, 0.062 is the table and 0.008 the data. Suggested "nearly the same (1.06 against 1.05)" and "is almost all the table". The 1-in-10 sentence and the regional sentence ("on either table") hold.
* **Failure probability:** holds; mixed precision ("2.3% to 19%" next to "2.4% to 19.5%") should be one precision, and see 6(a) on which log-linear reading is "Paper B's".
* **Conclusions:** "not of data" has the same mild overclaim as 8.1.

**Claim rows** (verdict on the builder's proposed movement):
* **A196** (A): agree. On the 2025 table 2011 is 0.946 against 0.953 in 2025; the thesis-table 0.894 stays as the as-published basis. "The margin is gone at 1 in 20 in both vintages" still holds on one table (0.946 < 1).
* **A009** (A): agree, wording only. The level statement stays; add the paired result (short term no fall in 2,000 draws; long term 26% fall, 52% on holdings land).
* **A418** (A, currently unverified): the base values 5.84% and 6.10% are reproduced here (5.835%, 6.098%), so this check can stand as A418's checker. Agree the conclusion's single 5.8% becomes the range 2.3% to 19.4% linear (median 7.6%).
* **A013** (B): agree, and stronger: "not because capacity fell" is not established by the paired draws (capacity falls in 26% of them, 52% on holdings land); "capacity changed little (paired difference -0.9 to +3.4 million) while the population rose 24%" is supported.
* **B363** (B): agree; true as levels, the paired change is the stronger statement and its notes' "a paired draw is needed" is now met.
* **A072** (B): agree 8.2 stands. Note: on the shared choices alone the paired difference is 6.5 to 8.4 (median 7.4); the base 8.2 sits near the top because the ratio is nearly constant (1.236 to 1.253) and most shared choices lower both levels.

## 6. What I would do differently / found beyond the brief

* (a) **"Log-linear as Paper B does."** The builder interpolates in log return period between the table's anchors (1, 3, 5, 10, 20, 30, 50, 150). Paper B's `fearnside_failure_curve.py` interpolates between its run points (1, 5, 10, 20, 50, 100). They agree at the median and p95 but not at p5: 2.39% against 2.22% (the draws near 1 in 40 sit between 20 and 50, where the table has an anchor at 30). The base value is the same either way (6.10%). The CSV and sentence should name the points used; if "as Paper B does" is meant literally, p5 is 2.2%.
* (b) The builder's 2,000 paired draws reuse the B115 Latin hypercube, so they are not a fresh sample; my independent 500 draws agree within sampling error, which covers this.
* (c) Resilience-table pairing: the builder scales the 2011 thesis table by the leave-one-out/2025 ratio cell by cell; I put the leave-one-out table into both years. Nationally they differ by under 10 people (the two tables are equal at 100 years). Both are judgements, as the builder's limits say.
* (d) The short-term pairing rests on the diet shares moving in proportion; an absolute move was not tested by either of us.

## 7. Register rows touched

None.

Rerun (repository root): `node SCRATCH/v48/paired.mjs SCRATCH/b132/work SCRATCH/v48/paired_500.csv 500 4848`; `python3 SCRATCH/v48/summ.py`; `python3 SCRATCH/v48/more.py`; `node SCRATCH/v48/shock.mjs SCRATCH/v48/shock.csv`; `python3 SCRATCH/v48/fail.py` (SCRATCH = the session scratchpad).
