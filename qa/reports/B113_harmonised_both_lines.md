# B113: the harmonised comparison under both classifications; local-productivity readings primary

Brief: `qa/briefs/B113_harmonised_both_lines.md` (decisions 105 and 106). Leads read: `qa/reports/R03b_response_plan_B.md` issues 1 to 3. Inputs: `harmonised_comparison.csv`, `cross_method.csv`, `model_entry.csv` in `analysis/method_tests_2025/`, read as their scripts wrote them. No existing csv or script was changed (md5 of every csv in the folder checked before and after the run).

## 1. The formula (README subsection and the docstring of `harmonised_lines.py`)

For a method with paired readings i (as run a_i, harmonised h_i) and a reference R: distance as run D_a = mean |ln(a_i / R_a)|; harmonised D_h = mean |ln(h_i / R_h)|; share closed S = (D_a - D_h) / D_a; for the five methods together (sum D_a - sum D_h) / sum D_a, methods weighted equally. References: the corrected model 41.5; the median of the five method centres; the geometric mean of the five method centres (a centre is the geometric mean of a method's paired readings, taken as run for D_a and harmonised for D_h). Dispersion with no reference: standard deviation of natural logs (divisor n) and highest over lowest, over the five method centres and over all 19 readings.

Paired set, both lines: 19 readings of five methods (energy and protein balance 6, footprint 6, HALF 1, people per hectare 3, commodity balance 3). Footprint build 2, Fearnside and the model rows are outside it. Line (a): harmonised = column (b). Line (b): footprint builds 1 and 3 and HALF take column (e); the others keep column (b).

## 2. Results (`harmonised_comparison_lines.csv`)

| Reference or measure | (a) as run | (a) harmonised | (a) share closed | (b) as run | (b) harmonised | (b) share closed |
|---|---|---|---|---|---|---|
| Distance to the corrected model (41.5) | 1.411 | 1.353 | 4.1% | 1.411 | 0.867 | 38.5% |
| Distance to the median of method centres | 0.530 | 0.556 | -4.9% | 0.530 | 0.445 | 16.0% |
| Distance to the geometric mean of method centres | 0.535 | 0.569 | -6.3% | 0.535 | 0.443 | 17.2% |
| SD of log method centres | 0.646 | 0.702 | -8.6% | 0.646 | 0.440 | 31.8% |
| Highest over lowest method centre | 6.22 | 6.95 | -6.0% | 6.22 | 3.70 | 28.4% |
| SD of log readings (19) | 0.718 | 0.768 | -7.0% | 0.718 | 0.604 | 15.9% |
| Highest over lowest reading (19) | 22.69 | 32.14 | -11.2% | 22.69 | 12.40 | 19.4% |

Factor split as in the paper (continuity with B276): line (a) 9.6% (corrected model), 19.6% (median), 20.4% (geometric mean); line (b) 41.3%, 47.3%, 50.9%. The script stops if line (a) to 41.5 does not reproduce the 10% in the existing summary row.

Per method, share of the distance to 41.5 closed: footprint -4% (a), 61% (b); HALF 0% (a), 68% (b); people per hectare 26% both; energy and protein balance 8% both; commodity balance -15% both (fish 17 to 12).

In plain words: with the productivity basis counted as part of the method, harmonisation closes 4% of the distance to the model and the methods spread slightly further apart. Counted as an input, it closes about two fifths of the distance to the model (39%; 41% on the paper's factor split) and the spread among methods narrows by about a third (SD of log method centres 0.65 to 0.44; highest over lowest 6.2 to 3.7).

## 3. Times the model, local productivity primary (`cross_method_local.csv`)

| Row | Reading (million) | Times corrected (41.5) | Times improved (53.6) |
|---|---|---|---|
| Footprint, primary (Australian productivity) | 64.8 to 117.0 | 1.56 to 2.82 | 1.21 to 2.18 |
| Footprint, primary, crop and pasture together | 64.8 to 84.6 | 1.56 to 2.04 | 1.21 to 1.58 |
| Footprint, secondary (world-average) | 103 to 343 | 2.48 to 8.27 | 1.92 to 6.40 |
| HALF, primary | 76.0 | 1.83 | 1.42 |
| HALF, secondary (world-average) | 276 | 6.65 | 5.15 |
| Energy and protein balance (unchanged) | 133.8 to 210.7 | 3.22 to 5.08 | 2.50 to 3.93 |
| People per hectare (unchanged) | 145 to 190 | 3.49 to 4.58 | 2.71 to 3.54 |
| Aggregate methods, primary | 64.8 to 210.7 | 1.56 to 5.08 (about 1.6 to 5) | 1.21 to 3.93 |
| Aggregate methods, secondary | 103 to 343 | 2.48 to 8.27 | 1.92 to 6.40 |

## 4. Files changed

- Added `analysis/method_tests_2025/harmonised_lines.py` (rerunnable, deterministic: two runs give identical md5).
- Added `analysis/method_tests_2025/harmonised_comparison_lines.csv` (98 data rows).
- Added `analysis/method_tests_2025/cross_method_local.csv` (13 data rows).
- `analysis/method_tests_2025/README.md`: one new subsection appended at the end of the harmonised comparison section ("Both classifications of the productivity basis"); no other text touched (read from disk immediately before the write).
- Added this report.

## 5. Claim rows that move (for a later register job; the register is not edited)

Tier A:
- B276; A; "Inputs are 10% of the ratio-scale distance ... 0.14 and 1.35"; after: the share is stated per classification and reference: line (a) 4% of the distance closed to the corrected model (factor split 9.6%, 20% to the method centre), line (b) 39% (factor split 41%); input factors 0.59 to 1.42 unchanged.
- B277; A; "The spread among methods does not narrow ... 17 to 343 as run, 12 to 343 harmonised"; after: dispersion figures, line (a) SD of log method centres 0.65 to 0.70, highest over lowest 6.2 to 7.0 (does not narrow); line (b) 0.65 to 0.44 and 6.2 to 3.7 (narrows by about a third).
- B156; A; "146 to 343 million ... about three to eight times the model"; after: about 65 to 211 million, about 1.6 to 5 times (footprint and HALF at Australian productivity); world-average 103 to 343, 2.5 to 8.3 times, as a secondary reading.
- B046; A; footprint "146 to 343 million (103 at 1990 world yields)"; after: primary 64.8 to 117.0 (together 64.8 to 84.6) at Australian productivity; 103 to 343 secondary.
- B068; A; HALF "about 276 million"; after: primary 76.0, 276 secondary (world-average).
- B272; A; "6.65 times the corrected and 5.15 times the improved"; after: primary 1.83 and 1.42 (76.0); 6.65 and 5.15 secondary.

Tier B:
- B247; B; "about three to eight times ... 146 to 343 million (103 at 1990)"; after: about 1.6 to 5 times; footprint 64.8 to 117.0 (1.56 to 2.82 times) and HALF 76.0 (1.83 times).
- B270; B; values unchanged (64.8; 84.6 etc.); role moves from sensitivity to primary reading.

Unchanged in value, listed by R03b near these: B019 (134 to 211), B083 (145 to 147), B266, B267, B268, B269 (the latter three become secondary world-average readings).

Register rows touched: none.

Wrong-value check: an independent script (scratch, not filed) recomputes the line (b) share to 41.5 from the reading rows of `harmonised_comparison_lines.csv`: recomputed 0.3854 against the csv's 0.385, PASS. Example of a deliberate wrong value: claiming 0.41 (the factor-split figure) as the distance closed gives "recomputed 0.3854, claimed 0.4100", AssertionError: MISMATCH.
