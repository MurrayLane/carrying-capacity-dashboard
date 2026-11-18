# V39: blind check of B113 (the harmonised comparison under both classifications)

Brief: `qa/briefs/V39_check_B113.md`; rules `qa/briefs/_checker_rules_results_wave.md`. No git, no subagents, no network. This report is the only file written in the repository; my own code is in the session scratch folder (`v39/check.py`, `v39/extra.py`, `v39/compare.py`), not filed.

Order of work: read B113's brief and R03b issues 1 to 3; derived my figures from `harmonised_comparison.csv`, `cross_method.csv` and the README up to the end of the existing "Harmonised comparison" section (lines 1 to 571); only then opened `qa/reports/B113_harmonised_both_lines.md`, `harmonised_lines.py`, `harmonised_comparison_lines.csv`, `cross_method_local.csv` and the new README subsection (from line 572).

## Tolerance

Counts and row sets must match exactly. Distances, standard deviations, shares and ratios must agree within one unit of the last digit the builder prints. Million-people readings must match the source csv cells exactly.

## Wrong-value example

`compare.py wrong` adds one deliberate wrong value: the line (b) share of the distance to 41.5 claimed as 41.3% (the factor-split figure) against my 38.5%. Output: `DELIBERATE WRONG: closed (b) % claimed as 41.3 builder 41.3 mine 38.5 FAIL; mismatches 1`. Without it: `mismatches 0`. Example only.

## My figures (derived before opening the builder's files)

Definitions I chose: per method, D = mean over its readings of |ln(reading / R)|; the five methods (energy and protein balance, footprint, HALF, people per hectare, commodity balance) weighted equally; share closed = 1 - D_harmonised / D_as_run; a method centre = geometric mean of its readings; standard deviation in population form. Line (b): the footprint (builds 1 and 3) and HALF take column (e), the others keep column (b). Because the row set was not fixed by the brief I ran both footprint build 2 kept (21 readings) and dropped (19); the method-centre references both from each stage's own centres and fixed at one stage.

Main set (19 readings, build 2 out; references from each stage's own centres):

| Measure | (a) as run | (a) harmonised | (a) closed | (b) as run | (b) harmonised | (b) closed |
|---|---|---|---|---|---|---|
| Distance to 41.5 | 1.411 | 1.353 | 4.1% | 1.411 | 0.867 | 38.5% |
| Distance to median of centres (164.7; 147.0 / 82.0) | 0.530 | 0.556 | -4.9% | 0.530 | 0.445 | 16.0% |
| Distance to geometric mean of centres (150.3; 135.8 / 83.6) | 0.535 | 0.569 | -6.3% | 0.535 | 0.443 | 17.2% |
| SD of log centres | 0.646 | 0.702 | -8.6% | 0.646 | 0.440 | 31.8% |
| Max over min centre | 6.22 | 6.95 | | 6.22 | 3.70 | |
| SD of log readings | 0.718 | 0.768 | | 0.718 | 0.604 | |
| Max over min reading | 22.69 | 32.14 | | 22.69 | 12.40 | |

Factor split (paper's B276 form) to 41.5: (a) 9.6%, (b) 41.3%. Per method, share of the distance to 41.5 closed: energy 8.2%; footprint -4.0% (a), 61.1% (b); HALF 0% (a), 68.1% (b); people per hectare 26.1%; commodity balance -15.4%.

Variants: with build 2 kept (21 readings; on line (b) its two readings stay at world-average): distance to 41.5 closed 4.6% (a) and 35.1% (b); SD of log centres 0.641 to 0.690 (a) and 0.641 to 0.447 (b); SD of log readings 0.699 to 0.745 (a). These reproduce R03b's scratch 0.64, 0.69, 0.70, 0.75, 0.45 and 6.2 to 3.7. With the centre reference fixed at the harmonised stage instead of each stage's own: line (b) closes 51% (median) and 51% (geometric mean); fixed at the as-run stage: -28% and -10%.

'Times the model' (corrected 41.5; improved 53.6): footprint local, together 64.8 to 84.6: 1.56 to 2.04 and 1.21 to 1.58; all local footprint rows except pasture alone, 64.8 to 117.0: 1.56 to 2.82 and 1.21 to 2.18 (pasture alone 53.9 is 1.30); HALF 76.0: 1.83 and 1.42. Energy and protein balance 133.8 to 210.7: 3.22 to 5.08 and 2.50 to 3.93. People per hectare 145 to 190: 3.49 to 4.58 and 2.71 to 3.54. Aggregate with local readings primary: 64.8 to 210.7, 1.56 to 5.08 (about 1.6 to 5), 1.21 to 3.93.

## Comparison

| Item | Builder | Mine | Verdict |
|---|---|---|---|
| Paired set: 19 readings, five methods (6, 6, 1, 3, 3); build 2, Fearnside and model rows out | 19 | 19 (on that row set) | pass (row-set choice: see below) |
| Distance to 41.5, (a) as run / harmonised / closed | 1.411 / 1.353 / 4.1% | same | pass |
| Distance to 41.5, (b) harmonised / closed | 0.867 / 38.5% | same | pass |
| Median of centres: references 164.7; 147.0; 82.0 | same | same | pass |
| Median, closed (a) / (b) | -4.9% / 16.0% | same | pass |
| Geometric mean: references 150.3; 135.8; 83.6 | same | same | pass |
| Geometric mean, closed (a) / (b) | -6.3% / 17.2% | same | pass |
| SD of log centres (a) 0.646 to 0.702; (b) to 0.440 | same | same | pass |
| Max over min centre 6.22 to 6.95; to 3.70 | same | same | pass |
| SD of log readings 0.718 to 0.768; to 0.604 | same | same | pass |
| Max over min reading 22.69 to 32.14; to 12.40 | same | same | pass |
| Log-scale shares of the dispersion rows (-8.6, -6.0, -7.0, -11.2; 31.8, 28.4, 15.9, 19.4%) | as listed | recomputed from the figures above | pass |
| Factor split to 41.5: 9.6% (a), 41.3% (b) | same | same | pass |
| Factor split to the median / geometric mean: 19.6, 20.4 (a); 47.3, 50.9 (b) | as listed | reproduced with R = the as-run centre (the builder's stated choice); 20.5, 20.1 (a) and 57.8, 57.9 (b) with R = the harmonised centre | pass on the builder's definition; definition-sensitive on (b), see below |
| Per-method shares to 41.5 (footprint -4%/61%, HALF 0%/68%, people per hectare 26%, energy 8%, commodity -15%) | same | same | pass |
| `harmonised_comparison_lines.csv` row count | 98 | 2 x (19 readings + 5 centres + 3 x 7 reference rows + 4 dispersion) = 98 | pass |
| `cross_method_local.csv` row count | 13 | 13 | pass |
| Footprint primary 64.8 to 117.0; 1.56 to 2.82; 1.21 to 2.18 | same | same | pass |
| Footprint together 64.8 to 84.6; 1.56 to 2.04; 1.21 to 1.58 | same | same | pass |
| HALF primary 76.0; 1.83; 1.42 | same | same | pass |
| HALF secondary 276; 6.65; 5.15 | same | same | pass |
| Energy balance 133.8 to 210.7; 3.22 to 5.08; 2.50 to 3.93 | same | same | pass |
| People per hectare 145 to 190; 3.49 to 4.58; 2.71 to 3.54 | same | same | pass |
| Aggregate primary 64.8 to 210.7; 1.56 to 5.08 (about 1.6 to 5); 1.21 to 3.93 | same | same | pass |
| Footprint secondary 103 to 343; 2.48 to 8.27; 1.92 to 6.40 | as listed | arithmetic right; 343.4 / 53.6 = 6.41 (the existing csv prints 6.41), 6.40 comes from the rounded 343 | arithmetic pass (one unit, within tolerance); basis fail, see below |
| Aggregate secondary 103 to 343; 2.48 to 8.27 ("about 2.5 to 8.3") | as listed | on current (2021-23) yields: 133.8 to 343.4, 3.22 to 8.27 ("about three to eight", as the paper has it) | fail (low end) |
| README subsection figures (rounded copies of the table above) | as listed | same | pass |
| README prose: no em dashes, no time words | none found | none found | pass |
| Determinism (two runs, same md5) | claimed | not rerun by me (the script writes repository files and I write only this report) | not checked |

## Proposed sentences: do they say no more than the figures support?

* "On line (a), harmonisation closes almost none of the distance and the spread does not narrow" (4%; SD 0.65 to 0.70; 6.2 to 7.0): supported.
* "On line (b), harmonisation closes about two fifths of the distance to the model" (38.5%): supported. "and the spread narrows by about a third": supported for the five method centres (SD 32%, max over min 28% on the log scale), not for all 19 readings (16% and 19%, about a sixth). The bullet gives both sets of figures, so it is accurate as written, but the headline phrase should say "the spread among method centres" to say no more than the figures.
* "Which line holds is a classification, not a finding. The productivity basis is the largest single input once it is counted as one": supported (ln 343.4/64.8 = 1.67 and ln 275.8/76.0 = 1.29 against at most 0.53 for any other input factor).
* "The aggregate methods ... 64.8 to 210.7 million, about 1.6 to 5 times": supported. "against 103 to 343 million, about 2.5 to 8.3 times, with the footprint and HALF at world-average productivity": the 103 is build 3 at 1990 world yields, while every primary reading is on 2021-23 yields. The like-for-like counterfactual is 133.8 to 343.4, 3.2 to 8.3 times (the paper's own "three to eight"). The README's last sentence does say what the 103 is, so it is not false, but the "2.5" ratio mixes data years and should not go into B156.

## Claim rows the builder says move

| Id | Tier | Builder's after | Verdict |
|---|---|---|---|
| B276 | A | line (a) 4% closed to 41.5 (factor split 9.6%, 20% to the method centre); line (b) 39% (factor split 41%); input factors 0.59 to 1.42 | agree on the figures. The "20% to the method centre" is the factor split with R = as-run centre; with the harmonised centre it is 20.1 to 20.5% on (a), so it holds; do not carry a line (b) factor split to a centre (47 to 58% by definition) |
| B277 | A | (a) SD of log centres 0.65 to 0.70, 6.2 to 7.0; (b) 0.65 to 0.44, 6.2 to 3.7, "narrows by about a third" | agree; "about a third" is of method centres (readings: about a sixth) |
| B156 | A | about 65 to 211 million, about 1.6 to 5 times; world-average 103 to 343, 2.5 to 8.3 times, secondary | primary agree; secondary should be 134 to 343 (146 to 343 for the footprint on current yields), about 3.2 to 8.3 times, keeping "(103 at 1990 world yields)" as a qualifier as the claim does now |
| B046 | A | primary 64.8 to 117.0 (together 64.8 to 84.6); 103 to 343 secondary | agree on the primary; keep the existing "146 to 343 on current yields (103 at 1990 world yields)" wording for the secondary |
| B068 | A | HALF primary 76.0; 276 secondary | agree |
| B272 | A | primary 1.83 and 1.42 (76.0); 6.65 and 5.15 secondary | agree |
| B247 | B | about 1.6 to 5 times; footprint 64.8 to 117.0 (1.56 to 2.82); HALF 76.0 (1.83) | agree |
| B270 | B | values unchanged; role sensitivity to primary | agree |
| B019, B083, B266 to B269 | | unchanged in value (B267 to B269 become secondary) | agree |

## What I would do differently, and whether it changes a number

1. Secondary (world-average) footprint and aggregate rows: take them on 2021-23 yields, matching the primary rows. Changes numbers: footprint secondary low 103 to 146.2 (builds 1 and 3) or 139.4 (with build 2), 2.48 to 3.52 or 3.36 times; aggregate secondary low 103 to 133.8, 2.48 to 3.22 times (1.92 to 2.50 over the improved). Primary figures unchanged.
2. Row set: the builder drops footprint build 2 on both lines. On line (b) that is the right choice (it has no local reading); on line (a) keeping it moves little (4.1% to 4.6%; SD of centres 0.646 to 0.702 becomes 0.641 to 0.690). On line (b) keeping build 2 at world-average gives 35.1% in place of 38.5%. No headline wording changes ("about two fifths" holds at 35 to 39%), but the paper should name the 19-reading set.
3. Centre references: the builder computes each stage's distance to that stage's own centre, which makes the "share closed" a dispersion measure. That is defensible and stated, but the result depends heavily on it: a reference fixed at the harmonised centres gives about 51% on line (b); fixed at the as-run centres, -28% (median) and -10% (geometric mean). I would print this sensitivity beside the 16 to 17% or rely on the reference-free dispersion figures for the "spread" claim. No headline number changes if the paper uses the builder's definition as stated.
4. The 343 / 53.6 = 6.40 cell: use the unrounded 343.4 (6.41) to match `harmonised_comparison.csv`. One unit in the last digit.

## Register rows touched

None.

## Files read

`qa/briefs/V39_check_B113.md`, `qa/briefs/_checker_rules_results_wave.md`, `qa/briefs/B113_harmonised_both_lines.md`, `qa/reports/R03b_response_plan_B.md` (issues 1 to 3), `analysis/method_tests_2025/harmonised_comparison.csv`, `cross_method.csv`, `README.md`; then `qa/reports/B113_harmonised_both_lines.md`, `analysis/method_tests_2025/harmonised_lines.py`, `harmonised_comparison_lines.csv`, `cross_method_local.csv`, and the claim rows listed above in `qa/claims_register.csv` (read only).

## Rerun

From the repository root: `python3 -I <scratch>/v39/check.py`, `python3 -I <scratch>/v39/extra.py` (run from the scratch folder), `python3 -I <scratch>/v39/compare.py` and `python3 -I <scratch>/v39/compare.py wrong`.
