# V46: blind check of B130 (the widened Monte Carlo on the improved release)

Checker report. Brief: `qa/briefs/V46_check_B130.md`. Builder brief: `qa/briefs/B130_widened_draws_improved.md`. Rules: `qa/briefs/_checker_rules_results_wave.md`. My code and runs are in my scratch folder (`/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v46/`: `stats.py`, `sobol.py`, `compare.py`, and the run outputs). No repository file other than this report was written. No git, no subagents, no network.

Order kept: I read the builder's brief, B115's report and V41, then ran `monte_carlo.mjs` (which I had to open to run; its header carries B130's one added comment on the loss-factor choice) and derived every figure below. Only then did I open `results/ranges_2025-improved_wide.csv`, `sobol_2025-improved.csv`, the builder's draws file (for the Sobol recompute, after my own block A run), the three method-test csvs, the README sections and the builder's report.

## Tolerance (set before comparing)

* Counts, choice names and the design layout: exact.
* Capacities: within 0.5%; for the ranges-file cells I used within 0.5 of a person, since both sides come from the same integers.
* Ratios, shares and indices: within one unit of the last printed digit (0.0011 for the three-decimal ratio and influence cells, 0.0005 for the four-decimal Sobol cells, 0.00011 for the binned column). Bootstrap intervals: my point estimate must lie inside the builder's interval, and the builder's half width must be within a factor 1.5 of mine (different resample counts and seeds).

## Wrong-value example (marked as an example)

`compare.py short:land:first_order=0.40 range:wide:short:p5=46175771` puts the 13-choice 5th percentile into the widened short-term row and 0.40 into the short-term land first-order index before comparing. Output:

```
MISMATCH ranges wide short p5 builder 46175771 mine 37903299
ranges cells compared 128 mismatches 1
MISMATCH sobol short land first_order builder 0.4 mine 0.3284
sobol cells compared 180 mismatches 1
```

The plain run reports 0 mismatches in both. So the check can fail.

## My figures

**Run.** `MC_RELEASE=2025-improved MC_LONG=1 MC_WIDE=1 MC_ZONES=national`, 2,000 draws, seed 20261027 (the script's fixed seed, as in B115), work folder the X054 folder used in V41 (`scratchpad/b41/work`). The script reports that the release applies `loss-factors-australia` and draws 18 choices; I confirmed independently that `resolveRelease('2025-improved').methods` includes `loss-factors-australia` and `2025-fixed`'s does not. All 18 choices vary on this release, `lbench` included (the release has Settings!BQ4:BQ7, from `recycling-stage`).

**Base values.** `fixed '{}'` gives 53,643,731 short term and 18,496,334 long term, equal to the person to Australia in `results/2025-improved.csv`.

**Ranges (Australia, 2,000 draws, linear-interpolation percentiles):**

| | Short term | Long term |
|---|---|---|
| p5 | 37,903,299 | 15,665,896 |
| p25 | 43,488,870 | 17,032,173 |
| p50 | 48,100,544 | 18,473,998 |
| p75 | 52,879,522 | 20,111,704 |
| p95 | 59,970,715 | 22,054,828 |
| min | 32,006,845 | 15,057,221 |
| max | 69,472,537 | 22,976,313 |
| p95 / p5 | 1.582 | 1.408 |
| max / min | 2.171 | 1.526 |
| base | 53,643,731 | 18,496,334 |

So: short term 37.9 to 60.0 (1.58), 32.0 to 69.5 (2.17), median 48.1; long term 15.7 to 22.1 (1.41), 15.1 to 23.0 (1.53), median 18.5. The short-term base (53.6) lies above the 75th percentile.

**13-choice improved run** (`monte_carlo_draws_2025-improved_all.csv`, zone 1, 1,000 draws): 46.2 to 60.1 (1.30), min to max 43.6 to 63.1 (1.45), median 53.3; long term 15.9 to 19.4 (1.22), 14.7 to 19.6 (1.33).

**One choice at a time** (short, long): land raster 62,933,179 and 21,699,331; meatcal 0 49,159,096 and 17,675,949; energy 1.2857 42,472,646 (long unchanged); waste 0.14 52,082,313 (long unchanged); trendwin 1 53,631,543 and 18,473,274; lbench 0.30 and 0.525 move the long term to 18,492,527 and 18,501,094 (short unchanged).

**Sobol indices** from the stored design (`monte_carlo_draws_2025-improved_wide.csv`). Design check: 20 blocks of 2,000 rows (A, B, AB_j for 18 choices), every AB_j row equals A with column j from B (0 mismatches); block A equals my own 2,000-draw run byte for byte (after the file's CRLF line ends are removed). I also ran the `sobol 2000 7 200` part myself (200 runs, draws i = 7, 207, ..., 1807): all 200 rows occur verbatim in the stored design. First order: centred Saltelli, mean((f(B) - m)(f(AB_j) - f(A))) / V; total order: Jansen, mean((f(A) - f(AB_j))^2) / 2V; 300 bootstrap resamples.

| Setting | Choice | First order | Total order |
|---|---|---|---|
| Short | land | 0.3284 (±0.035) | 0.3500 |
| Short | meat | 0.2994 (±0.033) | 0.3018 |
| Short | energy | 0.2177 (±0.029) | 0.2546 |
| Short | redmeat | 0.0573 | 0.0628 |
| Short | meatcal | 0.0213 | 0.0355 |
| Long | land | 0.6289 (±0.040) | 0.6642 |
| Long | restable | 0.1952 (±0.026) | 0.1954 |
| Long | meat | 0.1425 (±0.025) | 0.1545 |
| Long | meatcal | 0.0147 | 0.0150 |
| Long | lfuel | 0.0092 | 0.0125 |

Sums: S1 0.945 short and 0.997 long; ST 1.022 and 1.054. Short-term interactions (1 minus the S1 sum) are about 5.5%, against 2.6% on the corrected release; the largest gap between total and first order is energy (3.7 points) short term and land (3.5 points) long term.

**Corrected-release files untouched.** No git, so: (1) my fresh 2,000-draw run of `2025-fixed` with the same options equals block A of `monte_carlo_draws_2025-fixed_wide.csv` in all 42,000 cells, and `cmp` reports them identical once the committed file's CR characters are stripped; (2) every wide-row cell of `results/ranges_2025-fixed_wide.csv` equals my fresh run (31,115,433 to 49,169,829; 13,307,157 to 18,765,604; influences equal), the same figures as V41; (3) V41's `compare.py` reruns on the committed `sobol_2025-fixed.csv` and `ranges_2025-fixed_wide.csv` with 0 mismatches of 76 and 0 range mismatches; (4) all three files carry a modification time of 11:47 to 11:48, before the B130 script edits (18:51 onward). md5: draws 592a3d6f..., sobol 6e140eed..., ranges 8a3dcda5....

## Comparison with the builder

| Item | Builder | Mine | Result |
|---|---|---|---|
| lossaus has no meaning on 2025-improved; 18 choices | yes | the release applies loss-factors-australia; 18 drawn | pass |
| All 18 vary (lbench has an effect here) | yes | all 18 vary; lbench moves the long term by up to 70,679 people, indices under 0.0001 | pass |
| Base-value run | 53,643,731; 18,496,334 | the same | pass |
| Widened short p5 to p95 (factor) | 37.9 to 60.0 (1.58) | 37.90 to 59.97 (1.582) | pass |
| Widened long p5 to p95 | 15.7 to 22.1 (1.41) | 15.67 to 22.05 (1.408) | pass |
| Widened min to max | 32.0 to 69.5 (2.17); 15.1 to 23.0 (1.53) | 32.01 to 69.47 (2.171); 15.06 to 22.98 (1.526) | pass |
| Median (base) | 48.1 (53.6); 18.5 (18.5) | 48.10 (53.64); 18.47 (18.50) | pass |
| 13-choice improved | 46.2 to 60.1 (1.30), 43.6 to 63.1 (1.45); 15.9 to 19.4 (1.22), 14.7 to 19.6 (1.33) | the same | pass |
| `results/ranges_2025-improved_wide.csv`, 128 cells (4 rows: counts, percentiles, min, max, base, both ratios, 19 influence columns, influence_lossaus empty) | as filed | 0 mismatches | pass |
| Same columns as `ranges_2025-fixed_wide.csv` | yes, plus a leading `#` line | header identical | pass |
| `sobol_2025-improved.csv`: 72 point cells, 72 interval checks, 36 binned cells | as filed | 0 mismatches | pass |
| Top five tables and sums (94/100, 102/105) | as stated | the same | pass |
| One at a time: land 62.9 and 21.7; meatcal 49.2 and 17.7; energy 42.5; waste 52.1; trendwin 53.6 and 18.5 | as stated | the same | pass |
| `model_entry.csv`, improved row: 37.9 to 60.0; 15.7 to 22.1 | as filed | the same | pass |
| `cross_method.csv`, "The model, improved": 53.6 (37.9 to 60.0); 37.9; 60.0 | as filed | the same | pass |
| `cross_method.csv`, corrected row | 41.5 (31.1 to 49.2) | unchanged, matches | pass |
| `design_choices.csv`, new improved Monte Carlo row: 37.9; 60.0; 1.58 | as filed | the same | pass |
| README blocks (model_entry, cross_method) and hand text line 298 | 37.9 to 60.0; 15.7 to 22.1; contains 41.5 and 40 to 41, not 30.8; 18.9 inside the long range | the same | pass |
| Corrected-release files untouched | `cmp` identical | identical by content (see above) | pass |
| "The first 13 columns are the corrected run's" | 13 | 13 named choices plus waste: the underlying uniform columns of the first 14 are the same (lbench's value differs only because it is fixed at 0.4 on the corrected release) | wording, no number |
| Report: "each added choice can only pull the figures down"; README: the bottom falls "because the improved base sits near the top of the meat-window and meat-calibration choices" | as stated | **fail (wording).** The land raster, an added choice, raises the figure (62.9 short, 21.7 long) and lifts the maximum from 63.1 to 69.5. The meat window is not an added choice. The fall at the bottom comes mainly from the energy requirement (42.5 at its top end), then meat calibration and waste, each with the base at its favourable end. No number moves. |
| `sobol_2025-improved.csv`, lbench source text "no effect in this release" | as filed | **fail (text).** Copied from the corrected file; on this release lbench is drawn and has a small effect (indices round to 0.0000). The builder's own README says it has an effect. No number moves. |
| README design_choices block | not listed as changed | the block still shows only the corrected Uncertainty row (the generator picks the first match), so the new improved row is in the csv but not in the README table | note, no number |
| "No other register row carries 46.2 to 60.1 or 15.9 to 19.4" | none | searched value, statement, file, locator and notes: only B114, B115, B157, B159 | pass |

## Claim rows the builder says move: my verdict

* **B159** (A), "41.5 (31.1 to 49.2); 53.6 (46.2 to 60.1)" to "41.5 (31.1 to 49.2); 53.6 (37.9 to 60.0)": holds. This one is not conditional: its locator is the `cross_method.csv` row, which now prints the new range, so the row no longer matches its output until it moves (it is gate-5 approved, so the change needs the gate).
* **B114** (A), 46.2 to 60.1 to 37.9 to 60.0, conditional on adoption: holds. Its output file is the unchanged 13-choice `results/ranges_2025-improved.csv`, so as written it still matches that file.
* **B115** (B), 15.9 to 19.4 to 15.7 to 22.1, same condition: holds.
* **B157** (B): holds. On the widened improved range the short term contains Fearnside's 41.5 (not 30.8), and the long-term 18.9 lies inside 15.7 to 22.1; "contains none of his points" no longer holds on that range.
* Tier A separated in the builder's report: yes.

## What I would do differently, and whether it changes a number

1. Rewrite the "only pull the figures down" sentence (report and README): name the land raster as the one added choice that raises the figure, and the energy requirement as the main reason the bottom falls. No number changes.
2. Change the lbench source text in `sobol_2025-improved.csv` to "small effect in this release (indices under 0.0001)". No number changes.
3. Say "the first 14 columns (the 13 choices and waste)". No number changes.
4. Note that the short-term base (53.6) lies above the 75th percentile (52.9), not just above the median; any paper text calling 53.6 central needs this. No number changes.
5. Short-term interactions are about 5.5% on this release (S1 sum 94%), twice the corrected release's; a paper sentence reusing "interactions carry about 3%" for both releases would be wrong for the improved one.

None of these changes a figure in the ranges file, the Sobol file or the three method-test csvs.

## Register rows touched

None.

## Commands to rerun (repository root; S is my scratch folder, W = S/b41/work)

    MC_RELEASE=2025-improved MC_LONG=1 MC_WIDE=1 MC_ZONES=national node analysis/sensitivity_2025/monte_carlo.mjs $W $S/v46/base_imp.csv fixed '{}'
    MC_RELEASE=2025-improved MC_LONG=1 MC_WIDE=1 MC_ZONES=national node analysis/sensitivity_2025/monte_carlo.mjs $W $S/v46/imp2000.csv 2000
    MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 MC_ZONES=national node analysis/sensitivity_2025/monte_carlo.mjs $W $S/v46/fix2000.csv 2000
    MC_RELEASE=2025-improved MC_LONG=1 MC_WIDE=1 MC_ZONES=national node analysis/sensitivity_2025/monte_carlo.mjs $W $S/v46/sob_part.csv sobol 2000 7 200
    python3 $S/v46/stats.py $S/v46/imp2000.csv
    tr -d '\r' < analysis/sensitivity_2025/monte_carlo_draws_2025-improved_wide.csv > $S/v46/impdesign.csv; python3 $S/v46/sobol.py $S/v46/impdesign.csv
    python3 $S/v46/compare.py ; python3 $S/v46/compare.py short:land:first_order=0.40 range:wide:short:p5=46175771
    python3 $S/v41/compare.py

## Files read

`qa/briefs/V46_check_B130.md`, `qa/briefs/_checker_rules_results_wave.md`, `qa/briefs/B130_widened_draws_improved.md`, `qa/reports/B115_monte_carlo_widened.md`, `qa/reports/V41_check_B115.md`, `qa/reports/B125_apply_B123_and_loose_ends.md` (sections 6 and decision 4), `qa/reports/B127_register_and_regen_after_patches.md` (parts), `analysis/sensitivity_2025/monte_carlo.mjs`, `summarise_mc.py`, `monte_carlo_draws_2025-fixed_wide.csv`, `monte_carlo_draws_2025-improved_all.csv`, `monte_carlo_draws_2025-improved_wide.csv`, `sobol_2025-fixed.csv`, `sobol_2025-improved.csv`, `monte_carlo_2025-improved_wide.md`, `README.md` (B130 section), `check_wide.py` (run only), `results/2025-improved.csv`, `results/2025-fixed.csv`, `results/ranges_2025-fixed_wide.csv`, `results/ranges_2025-improved_wide.csv`, `analysis/method_tests_2025/cross_method.csv`, `model_entry.csv`, `design_choices.csv`, `README.md` (lines 267 to 350, 610 to 614), `make_readme_tables.py` (line 343), `qa/claims_register.csv` (search only), `web/scripts/releases.mjs` (via node), `qa/reports/B130_widened_draws_improved.md` (last).
