# B134: the drought bound and the pasture one-at-a-time for Paper B (decision 141)

Builder report. No git, no network, no subagent. Nothing in `papers/`, `qa/claims_register.csv`, any frozen release or any existing output was edited; every output is a new file. Scripts rerun to identical outputs.

## Headline

* Crop-only companions of the weather figures (corrected method, 2025-fixed, short term): 41.2, 41.0 and 40.4 million at 1 in 10, 1 in 20 and 1 in 100 against 30.8, 26.3 and 18.9 (B112 confirmed; the new file equals `drought_bounds.csv`). Also 41.4 at 1 in 5 (37.0) and 40.8 at 1 in 50 (22.9). Long term at 1 in 100: 24.7 against 15.6.
* Drought factor 2.19 (Table 8): crop-only 1.03 (41.5 over 40.4); long term 1.39 against 2.19.
* Failure probability at the 2025 population: 5.8 to 6.1% a year with the factor on every yield (reproduced from the new file by both interpolations, linear in T and in log T); below 1% a year on the crop-only bound (the curve is 40.4 at 1 in 100, above the population of 27.6; a bound set by the last run point, not extrapolated).
* Pasture output one at a time (short term): minus 20% gives 33.43 million (-8.07, -19.4%), plus 20% gives 49.47 (+7.96, +19.2%), full model; closed form 33.46 and 49.42 (the R05b scratch) or 33.43 and 49.47 with the oils cropland read from the evaluator. Pasture binds at both ends (crops use 37%, 45% and 52% of the cropland).
* PAL one at a time (short term, corrected): 1.2 gives 48.00 (+15.6%), 2.2 gives 26.93 (-35.1%) against 41.50 at 1.4 (8.0 MJ); improved: 61.77 and 35.15 against 53.64. Long term (not drawn): 16.98 and 11.84 against 15.62. The drawn window 1.4 to 1.8 spans 41.5 to 32.7 (factor 1.27); the NHMRC range spans 48.0 to 26.9 (factor 1.78).

Files (all new, nothing existing changed): `analysis/resilience_2025/drought_bounds_paper_B.mjs` and `.csv`; `analysis/method_tests_2025/fearnside_failure_curve_crop_only.py` and `.csv`; `analysis/pasture_2025/pasture_output_one_at_a_time.mjs` and `.py` with `pasture_output_one_at_a_time_2025-fixed.csv` (full model) and `pasture_output_one_at_a_time_closed_form_2025-fixed.csv`; `analysis/method_tests_2025/pal_one_at_a_time.mjs` and `pal_one_at_a_time_2025.csv`. Run from the repository root; each script has a `--wrong-value-demo` flag that plants one wrong value and shows its own check failing. Outputs are the same on a second run.

### 1. The crop-only drought bound beside every weather figure Paper B prints

The rule is B112's (`drought_bounds.mjs`, csv unchanged): the drought factor multiplies every yield (the model's rule), or the plant rows and grain-fed animal rows only (crop only), with pasture-fed output, fish, honey and timber at the mean year. National, release 2025-fixed (the corrected method), short term unless stated. B112's 41.2, 41.0, 40.4 and 30.8, 26.3, 18.9 are confirmed to the unit, and the new file's 2025-fixed rows equal `drought_bounds.csv` (the script checks this).

| Return period | Factor | Every yield (the model) | Crops only (bound) | Crop only below the average year (41.5) |
|---|---|---|---|---|
| 1 in 5 | 0.892 | 37.0 | 41.4 | 0.3% |
| 1 in 10 | 0.742 | 30.8 | 41.2 | 0.8% |
| 1 in 20 | 0.634 | 26.3 | 41.0 | 1.2% |
| 1 in 50 | 0.552 | 22.9 | 40.8 | 1.7% |
| 1 in 100 | 0.456 | 18.9 | 40.4 | 2.5% |
| 1 in 100, long term (average year 34.3) | 0.456 | 15.6 | 24.7 | 28.0% (the model's rule: 54.4%) |

* The drought factor of 2.19 (41.5 over 18.9, Table 8, section 6.10 and 6.11): the crop-only companion is 41.5 over 40.4, 1.03 (1.026). Long term at 1 in 100: 2.19 against 1.39.
* The weather span: 18.9 to 55.3 million becomes 40.4 to 55.3 on the crop-only bound.
* Share of the fall that comes from applying the factor to pasture-fed output: 97% at 1 in 10 and 95% at 1 in 100 (B112's "about 97%" is the 1-in-10 figure).
* Failure probability at the 2025 population (27.6 million), both interpolations of `fearnside_failure_curve.py` (linear in T and linear in log T): with the factor on every yield 5.8 to 6.1% a year (about 1 in 16 to 17), reproduced from the new file; with the factor on crops alone the curve never falls to the population (it is 40.4 at 1 in 100), so the failure probability is below 1% a year (below 1 in 100). That is a bound set by the last run point, not an estimate; the curve is not extrapolated past 1 in 100.
* Release 2025-improved is in the same csv as an approximate bound only: the row-scaling rule differs from that release's own drought run by 0.1 to 0.4% at 1 in 20 and beyond (cause not traced), flagged in the `both_check` column and outside the script's pass test. Crop only on that release: 53.2 at 1 in 10, 52.8 at 1 in 20, 52.5 at 1 in 50, 52.0 at 1 in 100 (the model's rule: 39.9, 34.2, 29.8, 24.6; its own runs 39.9, 34.3, 29.9, 24.7). Failure probability on the improved crop-only bound: below 1% a year (1.4 to 1.5% with the factor on every yield).
* Not computed: crop-only companions for the 2011 releases (Table 3 rows B124 to B128) and the mirror release (B104, B105); the script takes a release name in its list and the 2011 and mirror data are built, so this is a decision row if wanted.
* Scope: the bound tests nothing on livestock. No livestock output series for 1982-83 or 2002-03 is held; the observed check in B112 puts 2018-19 and 2019-20 near the median of the single-year series. The failure view therefore does not cover the binding constraint.

### 2. Pasture output one at a time (national, short term, everything else at base)

Pasture output is the yield per hectare of the pasture-fed rows (sheep meat, wool, dairy milk, cattle meat, goat and sheep milk). Full model rerun (the evaluator, `pasture_output_one_at_a_time.mjs`) and the closed form of `pairing_relaxed.py` (crops 3,397 m2 and pasture 84,190 m2 a person at 41.5 million, each pasture-fed food and the wool taking 1/f of the area) agree:

| Pasture output | Full model (million) | Change | Closed form, pasture groups only (R05b scratch) | Closed form, with oils cropland from the evaluator |
|---|---|---|---|---|
| minus 20% | 33.43 | -8.07, -19.4% | 33.46 | 33.43 |
| base | 41.50 | 0 | 41.50 | 41.50 |
| plus 20% | 49.47 | +7.96, +19.2% | 49.42 | 49.47 |

* Pasture binds at both ends. The crops use 37% of the cropland at minus 20%, 45% at base and 52% at plus 20%, and the unused cropland is ceded to pasture square metre for square metre; the cropland never binds in the short term. So a 20% error in pasture output carries to capacity almost one for one (elasticity 0.97 to 0.96), which is what a pasture-bound system implies.
* Why two closed-form columns: the cropland a person for oils and fats (Settings!C45) is not fixed when pasture output moves (it falls 14% at plus 20%, rising 22% at minus 20%, because animal fat is part of the oil supply). The R05b scratch (49.4 and 33.5) left it at base; setting it to the evaluator's value closes the gap to 0.002% (check tolerance 1e-4; the residual is not traced, one candidate being a cereals cell, Settings!H33, that moves by 0.01%).
* Long term, for completeness: 12.63 (-19.2%) and 18.56 (+18.8%) against 15.62.

### 3. Energy requirement (PAL) one at a time

The requirement is the food amount (Settings!B9, 1 at base) times the sedentary NHMRC diet, 8.0 MJ a day as eaten at PAL 1.4, so PAL p is food = p over 1.4. Everything else at base. PAL 1.4 reproduces `results/<release>.csv` (checked).

| Release and preset | PAL 1.2 (6.9 MJ) | PAL 1.4 (8.0 MJ) | PAL 1.8 (10.3 MJ) | PAL 2.2 (12.6 MJ) |
|---|---|---|---|---|
| 2025-fixed, short | 48.00 (+15.6%) | 41.50 | 32.66 (-21.3%) | 26.93 (-35.1%) |
| 2025-fixed, long | 16.98 (+8.7%) | 15.62 | 13.47 (-13.8%) | 11.84 (-24.2%) |
| 2025-improved, short | 61.77 (+15.1%) | 53.64 | 42.47 (-20.8%) | 35.15 (-34.5%) |
| 2025-improved, long | 19.90 (+7.6%) | 18.50 | 16.21 (-12.4%) | 14.43 (-22.0%) |

* Against the drawn window (PAL 1.4 to 1.8, food 1 to 1.286, short term only in the Monte Carlo): the window moves the corrected short term from 41.5 to 32.7 (0 to -21.3%), a factor of 1.27; the NHMRC range 1.2 to 2.2 moves it from 48.0 to 26.9, a factor of 1.78. The drawn window is the upper part of the range only: it has no draw below the base. The R05b scratch (about 48 and 26) was close; the 2.2 end is 26.9, not 26, because capacity does not vary exactly as the inverse of the food amount (capacity times PAL over base runs from 0.99 to 1.03 in the short term).
* The long-term energy requirement is not drawn at all (its first-order index is 0 in `sobol_2025-fixed.csv`); the long-term row above shows what it would do.

### 4. The S5 correction

Replace the claim that pasture productivity is not drawn (the list of 23 undrawn choices in S5, and any sentence saying so) by these two sentences, and in the list replace "pasture productivity" by "the deviation of national pasture output from the observed meat series (bounded one at a time, below)" so the count of 23 holds:

"In this model pasture output is national meat output shared among zones by dry sheep equivalent, so its uncertainty is the window of herd and meat data and the calibration of the ABS meat tables, and both are drawn: the window has a first-order index of 0.24 in the short term (95% interval 0.21 to 0.27) and 0.14 in the long term (0.12 to 0.16), and the calibration 0.03 (0.02 to 0.04) and 0.01 (0.01 to 0.02) (`sobol_2025-fixed.csv`)."

"What is not drawn is a deviation of national pasture output from the observed meat series, for example a carrying-capacity range in dry sheep equivalents by land class; one at a time, with everything else at base, pasture output 20% below and 20% above moves the short-term capacity from 41.5 to 33.4 million (-19.4%) and to 49.5 million (+19.2%), pasture binds at both ends, and this is a bound, not a range with a probability."

### 5. Sentences for Paper B (for the paper patch; no paper file was edited)

* **Section 5.8 (Fearnside test), replacing the Test paragraph's weather sentences:** "On the corrected model with 2025 data, capacity is 41.5 million in an average year. With the weather factor on every yield, which is the model's rule, it is 30.8 million at a maximum acceptable failure of 1 in 10 (26% lower) and 18.9 million at 1 in 100 (54% lower); with the factor on crop output alone and pasture-fed output at its mean it is 41.2 and 40.4 million (0.8% and 2.5% lower). At the 2025 population the failure probability is 5.8 to 6.1% a year with the factor on every yield (about 1 in 16 to 17) and below 1% a year with it on crops alone, because the crop-only capacity at 1 in 100 (40.4 million) is above the population (27.6 million). The first figure rests on a factor taken from the wheat, oats and barley record and applied to pasture-fed output, which no livestock series has tested, so the failure view does not cover the binding constraint."
* **Section 6.6 (weather), replacing the drought paragraph:** "In the model the drought allowance is a quantity. With the factor on every yield, an allowance for the worst year in 50 gave the corrected and improved releases 23 to 30 million and the worst year in 100 gave 19 to 25 million; the corrected method moved from 41.5 to 18.9 million, a factor of 2.19. With the factor on crop output alone, the corrected method reads 41.2, 41.0 and 40.4 million at 1 in 10, 1 in 20 and 1 in 100 (a factor of 1.03 at 1 in 100) and 24.7 million in the long term at 1 in 100 against 15.6. The fall comes almost wholly from applying a cereal factor to pasture-fed output (97% of it at 1 in 10, 95% at 1 in 100), a choice no livestock series has tested; none is held for 1982-83 or 2002-03. The Jones committee's margin ... [unchanged]." Where the paper says the model "reproduces" 30 to 35 million at 1 in 10 (section 7, B245): add "with the factor on every yield; on crops alone the 1-in-10 reading is 41.2 million".
* **Table 8:** keep the row "Drought allowance | average year; worst year of 5, 10, 20, 50, 100 | 18.9 | 41.5 | 2.19 | corrected" and add "Drought allowance, factor on crops only | worst year of 100 | 40.4 | 41.5 | 1.03 | corrected". Section 6.11's order: the crop-only drought factor (1.03) falls below the land base (1.09); the sentence listing the drought allowance (2.19) above the 1.58 carries "(1.03 with the factor on crops only)". Table 9, purpose 1: "for crops; not tested on pasture-fed output".
* **S5:** the two sentences of section 4 above. Add to the PAL sentence ("a wider window would widen the short-term range"): "One at a time, PAL 1.2 and 2.2 give 48.0 and 26.9 million against 41.5 (+15.6% and -35.1%); the drawn window 1.4 to 1.8 spans 41.5 to 32.7, a factor of 1.27 against 1.78 for the NHMRC range."
* **Abstract (decision 146), replacing "Weather and waste take the model from 18.9 to 55.3 million":** "One at a time, a weather allowance for the worst year in 100 lowers the model from 41.5 to 18.9 million (40.4 with the allowance on crops only) and removing avoidable waste raises it to 55.3 million; across the settings varied together it moves by a factor of 1.58 (5th to 95th percentile)." The same change is wanted in the highlights line and in the closing summary of section 8 ("Across the weather allowance and avoidable waste ... spans 18.9 to 55.3 million"). The abstract is held to 250 words or fewer: check the count in the patch.

## Claim rows that move (register not edited; proposals for the coordinator)

Tier A:
* B001; A; "lowest definition-only figure ... worst of 100 years" 18.9; becomes 18.9 with the model's rule and 40.4 with the factor on crops only (two changes one at a time, decision 146).
* B003; A; 18.9 to 55.3; becomes 18.9 (40.4 crop only) and 55.3 as two separate changes from 41.5, not a joint range; the crop-only span is 40.4 to 55.3.
* B096; A; 30.8 at 1 in 10; keeps 30.8 as the model's rule; gains the companion 41.2 (crop only).
* B130; A; 5.8 to 6.1% a year; keeps the figure for the factor on every yield; gains "below 1% a year with the factor on crops alone" and the caveat that pasture-fed output is untested.
* B137; A; 18.92 to 41.5; gains the crop-only low end 40.45.
* B167; A; factor 2.19; keeps 2.19 for the model's rule; gains 1.03 (1.026) crop-only companion.
* B188; A; "drought allowance (2.19)" in the ordering against 1.58; the crop-only 1.03 sits below the land base (1.09) and below 1.58.
* B193; A; "factor of 4 from 15.6 (long term) or 18.9 (worst of 100 years) to 62.9"; the crop-only low ends are 24.7 and 40.4, factors 2.55 and 1.56 to 62.9.

Tier B and C (listed for the coordinator; tiers as in the register):
* B095, B097, B098 (37.0, 26.3, 22.9; B); crop-only companions 41.4, 41.0, 40.8.
* B099 to B103 (improved, 47.9, 39.9, 34.3, 29.9, 24.7; B); approximate crop-only companions 53.5, 53.2, 52.8, 52.5, 52.0 (rule flagged as 0.1 to 0.4% off that release's own run).
* B134; B; "26% and 54% lower"; gains "0.8% and 2.5% lower on crops only".
* B138, B245, B226; B; Jones committee's 30 to 35 million as the 1-in-10 point (30.8): holds only with the factor on every yield; crop-only 1-in-10 reading is 41.2.
* B157; B; Fearnside's 1-in-10 and 1-in-100 points against the widened ranges: gains the crop-only points 41.2 and 40.4 (inside the corrected widened range 31.1 to 49.2 for 41.2; 40.4 also inside).
* B198, B199, B218, B224; B; drought figures 31 to 40, 23 to 30, 19 to 25, 1.3 to 2.2: crop-only companions 41.2 to 53.2 at 1 in 10, about 40.8 to 52.5 at 1 in 50, 40.4 to 52.0 at 1 in 100, and 1.01 to 1.03 for the factor.
* B230; C; group "the same with a drought allowance (30 to 35)": gains the crop-only reading.
* B238; B; Table 9 purpose 1 "well suited" for the failure view: gains "for crops; not tested on pasture-fed output".
* B243, B333, B364; B; the ordering of design choices by factor: the drought allowance has two values, 2.19 and 1.03 (crop only).
* B247; B; the pairing binds Australia: supported unchanged (pasture binds at plus and minus 20% pasture output); no value moves.
* B369, B371; B; PAL window: values unchanged; gain the one-at-a-time ends (48.0 and 26.9) as context.
* B124 to B128, B104, B105 (2011 and mirror drought figures; B): crop-only companions not computed (decision row).
* S5 rows in `supplementary_claims.csv`: "23 undrawn choices" (S5 sentence 5) keeps 23 if "pasture productivity" is replaced by the deviation of national pasture output (section 4 above); the sentence listing pasture productivity as undrawn is replaced; new rows for the Sobol indices, the plus and minus 20% results and the PAL ends.

New figures with no register row yet (Tier B proposals): 41.2, 41.0, 40.4 (and 41.4, 40.8) crop-only; 24.7 long term crop-only; 1.03; below 1% a year; 33.4 and 49.5; 48.0 and 26.9; 1.27 and 1.78.

Register rows touched: none.

## Notes and limits

* The improved release's crop-only rows are approximate: the row-scaling rule (apply the factor to a row group) differs from that release's own drought run by 0.1 to 0.4% from 1 in 20, cause not traced. The corrected release (the one Paper B headlines) reproduces exactly.
* The closed form for pasture needs the oils cropland (Settings!C45), which moves with pasture output; without it the closed form is 0.1% off the full model (the R05b scratch figures). A 0.002% residual is not traced.
* The PAL scaling assumes the model's energy requirement is the food amount, as the Monte Carlo draws it; the Monte Carlo draws it for the short term only.
* The brief names `analysis/sensitivity_2025/rerun.mjs`, which does not exist; `analysis/comparators_2025/rerun.mjs` (the weather runs) was read and the PAL and pasture evaluator calls were written fresh, in the allowed directories.
* Livestock drought test: out of scope (no livestock output series held for 1982-83 or 2002-03).

## Files changed (all new except one README append)

* `analysis/resilience_2025/drought_bounds_paper_B.mjs`, `analysis/resilience_2025/drought_bounds_paper_B.csv`
* `analysis/method_tests_2025/fearnside_failure_curve_crop_only.py`, `analysis/method_tests_2025/fearnside_failure_curve_crop_only.csv`
* `analysis/method_tests_2025/pal_one_at_a_time.mjs`, `analysis/method_tests_2025/pal_one_at_a_time_2025.csv`
* `analysis/pasture_2025/pasture_output_one_at_a_time.mjs`, `analysis/pasture_2025/pasture_output_one_at_a_time.py`, `analysis/pasture_2025/pasture_output_one_at_a_time_2025-fixed.csv`, `analysis/pasture_2025/pasture_output_one_at_a_time_closed_form_2025-fixed.csv`
* `analysis/method_tests_2025/README.md` (one section appended at the end; generated tables untouched)
* `qa/reports/B134_paper_B_drought_bound_and_pasture.md` (this report)

## Wrong-value check

EXAMPLE (deliberate wrong value, shown failing): the both-applied failure probability given as 6.5 to 6.9 instead of 5.8 to 6.1.

    python3 -I analysis/method_tests_2025/fearnside_failure_curve_crop_only.py --wrong-value-demo
    check, both-applied curve at the 2025 population: 6.5 to 6.9 (fearnside_failure_curve.csv: 5.8 to 6.1): FAIL

Also shown failing by the other three scripts (each `--wrong-value-demo`): drought bounds, both-applied planted 1,000,000 high ("DIFFERS by 1000000"); pasture, full-model plus 20% planted 1 million high (closed form 49.467562 against 50.466640: FAIL); PAL, base capacity planted 1 million high (42503536.97 against 41503537: FAIL).
