# V41: blind check of B115 (the widened Monte Carlo and the Sobol indices)

Checker report. Brief: `qa/briefs/V41_check_B115.md`. Builder brief: `qa/briefs/B115_monte_carlo_widened.md`. My code is in my scratch folder (`/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v41/`: `stats.py`, `sobol.py`, `sobol2.py`, `dist.py`, `more.py`, `compare.py`). No repository file other than this report was written. No git, no subagents, no network.

Order kept: I derived the percentiles, extremes, ratios and both Sobol indices from the draws file first. I then opened `monte_carlo.mjs` (to run it) and the README section (for the sources it names); that section also gives the builder's results table, so from that point I had seen them. The builder's report, `sobol_2025-fixed.csv`, `results/ranges_2025-fixed_wide.csv` and `check_wide.py` were opened last.

## Tolerance (set before comparing)

* Counts and names: exact.
* Capacities: within 0.5%. For the cells of the ranges file I applied a tighter test, within 0.5 of a person, because both sides come from the same integers.
* Shares, indices and ratios: within one unit of the last printed digit. For the four-decimal Sobol cells I used 0.0005.

## Wrong-value example (marked as an example)

`compare.py short:land:first_order=0.40` replaces the builder's short-term first-order index for the land source (0.3186) with 0.40 before comparing. Output: `MISMATCH short land first_order builder 0.4 mine 0.3186`, `sobol cells compared 76 mismatches 1`. The plain run reports 0 mismatches. So the check can fail.

## My figures

**Design of the draws file.** It has 42,000 rows: blocks A, B and AB_j for 19 choices, with 2,000 rows each. I checked every AB_j row against its A and B rows: it equals A with column j taken from B (the Saltelli design). `lbench` is constant at 0.4 in every row; on this release it is not drawn (the script falls back to 0.4 when Settings!BQ4:BQ7 is absent). `land` and `restable` take only the values 0 and 1; `meat` takes 0, 1 and 2.

**Ranges (Australia, block A, 2,000 draws, linear-interpolation percentiles).**

| | Short term | Long term |
|---|---|---|
| p5 | 31,115,433 | 13,307,157 |
| p95 | 49,169,829 | 18,765,604 |
| p95 / p5 | 1.580 | 1.410 |
| min | 26,160,467 | 12,421,961 |
| max | 58,142,557 | 19,898,446 |
| max / min | 2.223 | 1.602 |
| median | 38,994,576 | 15,763,939 |

The choice of block and of percentile method moves nothing at one decimal. A and B together (4,000 draws): 31.2 to 49.1 (1.58) short term and 13.3 to 18.7 (1.41) long term. All 42,000 rows: 1.58 and 1.41 for 5th to 95th; their min to max is 2.28 and 1.61, but those extremes come from the AB mixes and are not draws of the joint distribution, so block A is the right basis.

**Existing 13-choice range** (`monte_carlo_draws_2025-fixed_all.csv`, zone 1, 1,000 draws): short term 36.33 to 45.76 (1.26), min to max 34.60 to 47.65 (1.38); long term 13.39 to 16.52 (1.23), min to max 12.94 to 16.90 (1.31). Recomputed with the percentile rule of `summarise_mc.py`, the five percentiles equal the zone 1 rows of `results/ranges_2025-fixed.csv` exactly.

**Conditional on the land source** (block A): holdings only (1,000 draws), short term 29.8 to 43.1 (1.45) and long term 13.0 to 16.2 (1.24); raster only (1,000 draws), 35.6 to 51.2 (1.44) and 15.3 to 19.1 (1.25).

**Sobol indices**, from the stored design matrices (not a regression substitute). First order: mean((f(B) - m)(f(AB_j) - f(A))) / V, with m and V the mean and variance over A and B together. Total order: Jansen, mean((f(A) - f(AB_j))^2) / 2V. 95% half-widths are from 300 bootstrap resamples.

| Choice | Short S1 | Short ST | Long S1 | Long ST |
|---|---|---|---|---|
| land | 0.319 (±0.032) | 0.327 | 0.576 (±0.038) | 0.563 |
| energy | 0.268 (±0.034) | 0.254 | 0.000 | 0.000 |
| meat | 0.241 (±0.028) | 0.234 | 0.141 (±0.024) | 0.139 |
| lossaus | 0.055 | 0.061 | 0.000 | 0.000 |
| redmeat | 0.044 | 0.046 | 0.000 | 0.000 |
| restable | 0.000 | 0.000 | 0.197 (±0.026) | 0.204 |
| orgfac | 0.000 | 0.000 | 0.043 | 0.039 |
| meatcal | 0.034 | 0.026 | 0.014 | 0.012 |

Sums: S1 is 0.974 short term and 0.973 long term; ST is 0.964 and 0.961. Every other choice is under 0.01 in both indices.

**Uncentred form.** I first used the uncentred Saltelli 2010 first-order form, mean(f(B)(f(AB_j) - f(A))) / V. It gives the same point estimates within noise (land 0.295, energy 0.254, meat 0.258), but its bootstrap half-widths are ±0.22 to ±0.27, because the output mean (about 39 million) is large next to its spread. The builder's centred form is the right choice.

**Base values, the script under test.** With `MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 MC_ZONES=national` and the fixed mode at the base values (`{}`), the run gives 41,503,537 short term and 15,623,209 long term. Those are the zone 1 capacities in `results/2025-fixed.csv` to the person. The work folder was the X054 folder at `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/b41/work`.

**One choice at a time** (short, long):

| Run | Short term | Long term |
|---|---|---|
| lossaus 1 | 46,153,962 | unchanged |
| land 1 | 48,690,676 | 18,328,669 |
| meatcal 0 | 38,417,338 | 15,010,078 |
| energy 1.2857 | 32,664,283 | unchanged |
| waste 0.14 | 39,272,117 | unchanged |
| trendwin 1 | 41,496,001 | 15,608,147 |

The trend window moves Australia by under 0.1%, so its index of 0.000 is a real result, not a fault.

**No-option run against the committed draws.** I reran with `MC_RELEASE=2025-fixed MC_LONG=1` and 1,000 draws, with none of the new options except `MC_ZONES=national`. The 13 choice columns and the 1_short and 1_long columns equal `monte_carlo_draws_2025-fixed_all.csv` in all 15,000 cells. That file's zone 1 percentiles equal `results/ranges_2025-fixed.csv` (above). A full all-zone byte comparison was not completed: at the measured speed of 6.4 minutes per 1,000 national draws, 60 zones would take hours. I stopped it, so that part is **cannot determine**.

## Sources of the six added ranges (files opened)

| Choice | Source opened | Verdict |
|---|---|---|
| waste 12% to 14% | `analysis/waste_2025/README.md` line 27: "roughly 12 to 14%" | holds. Note: the release value is 0.12 (`results/2025-fixed.csv`, losses), the low end of the range. |
| lossaus | `methods/loss-factors-australia/method.json` (474 Base cells, FIAL 2021 Table 5, Burnside 2022 in its errata) | the endpoints hold. The uniform weight between two point estimates is not a measured range, and the README does not mark it as judgement (it does for other weights). |
| land | `build_variants.py` variant `land_raster` (present in the work folder's `variants.json`) | holds; equal chances are stated as judgement. |
| meatcal | `pipeline/yields/recent/livestock_zone.py` lines 14 to 15 and 72 to 74 (cattle 1.086, sheep 1.155; LS_CAL=off) | the endpoints hold. I did not recompute the yearly gaps of 4.6% to 8.6% and 12.4% to 16.9% (the ABS files were not located): cannot determine. The uniform weight is unmarked judgement. |
| energy 1.000 to 1.286 | NHMRC NRV PDF (`carrying-capacity-models/Foundation diets/`), Table 3, Table 4 and page 19 text: 1.8 / 1.4 = 1.2857; "from ... sedentary activity to ... moderate activity" | the end values hold. The NHMRC range itself is PAL 1.2 to 2.2 (Table 3 note b), so 1.4 to 1.8 is a chosen part of it. The builder's report says so; the README table does not. I did not verify that the release diet corresponds to PAL 1.4. |
| trendwin 1.289 to 1.356 | `data/abs-2022-25/group_trend.json` (1.28891, 1.35557) | holds. |

## Comparison with the builder

| Item | Builder | Mine | Result |
|---|---|---|---|
| Draw count, choices | 2,000 in block A, 19 choices, 42,000 runs | the same | pass |
| Widened short p5 to p95 (factor) | 31.1 to 49.2 (1.58) | 31.12 to 49.17 (1.580) | pass |
| Widened long p5 to p95 | 13.3 to 18.8 (1.41) | 13.31 to 18.77 (1.410) | pass |
| Widened short min to max | 26.2 to 58.1 (2.22) | 26.16 to 58.14 (2.223) | pass |
| Widened long min to max | 12.4 to 19.9 (1.60) | 12.42 to 19.90 (1.602) | pass |
| Median (base) | 39.0 (41.5); 15.8 (15.6) | 38.99 (41.50); 15.76 (15.62) | pass |
| Existing p5 to p95, min to max | 36.3 to 45.8 (1.26), 34.6 to 47.7 (1.38); 13.4 to 16.5 (1.23), 12.9 to 16.9 (1.31) | the same | pass |
| `ranges_2025-fixed_wide.csv`, wide rows: p5, p25, p50, p75, p95, min, max, both ratios | as filed | all equal to the person, ratios within 0.001 | pass |
| `ranges_2025-fixed_wide.csv`, existing rows | as filed | equal to `ranges_2025-fixed.csv` and the draws | pass |
| `sobol_2025-fixed.csv`, 76 cells (19 choices x 2 settings x first and total order) | as filed | 0 mismatches at 0.0005 | pass |
| Short shares (first, total): land 32/33, energy 27/25, meat 24/23, lossaus 6/6, redmeat 4/5, meatcal 3/3, waste 1/1 | as stated | 32/33, 27/25, 24/23, 6/6, 4/5, 3/3, 1/1 | pass |
| Long shares: land 58/56, restable 20/20, meat 14/14, orgfac 4/4, meatcal 1/1 | as stated | 58/56, 20/20, 14/14, 4/4, 1/1 | pass |
| "First-order shares add to 97% (short) and 96% (long)" | 97, 96 | 97.4, 97.3 (the builder's own CSV column also sums to 0.973) | **fail** (long is 97%; 96% is the total-order sum) |
| "Interactions carry about 3% to 4%" (report) and "about 4%" (paper sentence) | 3 to 4; 4 | 1 - sum S1 = 2.6% short, 2.7% long, and every ST is within 1.4 points of its S1 | report wording within tolerance; **paper "about 4%": fail** (about 3%) |
| "Three choices carry four-fifths of the short-term variance" | four-fifths | 83% first order, 81% total | pass |
| Each total within two points of its first order | yes | the largest gap is 1.4 points (energy) | pass |
| Holdings-only and raster-only ranges | 29.8 to 43.1 (1.45), 13.0 to 16.2 (1.24); 35.6 to 51.2 (1.44), 15.3 to 19.1 (1.25) | the same; 1,000 draws each | pass |
| Base-value run equals the release | 41,503,537 and 15,623,209 | the same | pass |
| Australian loss factors at weight 1 | 46,153,962 | 46,153,962 | pass |
| No-option output identical to before | byte-identical on four runs | zone 1 identical in all 15,000 cells of the committed 1,000-draw file; the all-zone byte compare was not run | pass for zone 1; all zones cannot determine |
| 2011 inside the widened range | 33.3 inside 31.1 to 49.2; 15.35 inside 13.3 to 18.8 | 33.31 and 15.35 (`results/2011-fixed.csv`): both inside | pass |
| "Four new choices have the release at one end" | four (lossaus, meatcal, energy, trendwin) | five: waste too (the release value 0.12 is the low end of 12% to 14%) | **fail** (count) |
| Paper: "19 choices ... each drawn over the range its source gives" | 19 | 18 vary; lbench is fixed at 0.4 on this release (the builder's B253 row says so) | **fail** (wording) |
| Paper: "four with ends or weights that are the author's judgement" | four | The README table marks five as judgement (meat, meategg, redmeat, restable, land), and the builder's report adds energy, making six. The uniform weights of lossaus and meatcal, and the point inside trendwin, are judgements too but unmarked. | **fail** (count) |
| Against the definitions: 1.58 above waste (1.33) and land available (1.09); below diets 2.14, drought 2.19, exports 2.41 to 6.36, time frame 2.66, unit 2.67 | as stated | matches `design_choices.csv` | pass |
| Paper (highlight 5): "every definition moves it further" | every | Land available (1.09) is a definition by the README's own reasoning (dairy-good-land is classed a definition "as the land-available row of Table 6 does"). "Australian settings" (1.29) is listed as a definition ("the improved line as a whole"). Both are below 1.58. | **fail** |
| Paper (abstract s7): "by definition alone the model spans 18.9 to 55.3 million" | 18.9 to 55.3 | Not derived in B115. In `design_choices.csv` the corrected rows run lower, to 15.5 (unit) and 15.6 (time frame), and 55.3 is the waste-to-zero row, which the new rule treats as a setting, not a definition. | **fail** (unsupported as written) |
| Paper (section 6.9, against 2011): "the short-term change since 2011 is within the uncertainty of the settings" | as stated | The range is for the 2025 level, and 2011 was not sampled. Settings shared by both years (land source, energy requirement, loss factors, waste) would move the 2011 figure too, so the range of the change is not this range. Only "33.3 lies inside the 2025 range" is supported. | **fail** (says more than the figures) |
| Paper: "31.1 to 49.2 ... factor 1.58; 26.2 to 58.1 ... 2.22"; "Three choices ... 32%, 27%, 24%" | as stated | the same | pass |

## Claim rows the builder says move: my verdict

* **B112** (A), 36.3 to 45.8 to 31.1 to 49.2: figures hold; conditional on adoption, as the builder says.
* **B159** (A), 41.5 (31.1 to 49.2): holds; same condition.
* **B187** (A), 1.58 over 19 choices, 2.22 min to max: the figures hold. "19 choices" should read "19 choices, 18 of which vary on this release".
* **B188** (A), "1.58 (2.22) against 2.14 (diet), 2.2 ... 6.4": holds against `design_choices.csv`.
* **A027 and A028** (A), 31.1 to 49.2 and 13.3 to 18.8: hold; same condition.
* **B113** (B), 13.3 to 18.8: holds.
* **B116** (C), 19 choices, 2,000 draws, 42,000 runs: holds (with the lbench note).
* **B117** (B), meat window 24% first order and 23% total; land 32% and 33%: holds.
* **B120** (B), meat window 14% and 14% long term: holds.
* **B157** (B), Fearnside's 30.8 just below 31.1: holds (31.12).
* **B253** (B), 18 of 19 vary: holds.
* B110, B111, B114 and B115 do not move: agreed; the mirror and improved releases were not rerun.

## What I would do differently, and whether it changes a number

1. **Interaction share.** Quote 1 - sum of S1 (about 3%), not 4%. This changes one printed number in a proposed paper sentence (4% to 3%) and the report's "96%" to 97%.
2. **Release at one end.** Waste belongs in the list (five of the six new choices have the release at one end). No figure moves; one count does.
3. **Judgement count.** State the judgement choices by name rather than "four", and mark the uniform weights of lossaus and meatcal as judgement in the README table, as is done for the other weights. No number moves.
4. **The highlight sentence.** Write "every definition except the land available and the Australian settings" or "the larger definitions", and drop or re-source "18.9 to 55.3". No range moves.
5. **The 2011 sentence.** Keep only "the corrected 2011 figure (33.3 million, not sampled) lies inside the widened 2025 range". A statement about the change needs paired draws on both releases.
6. **Energy range.** Describe 1.4 to 1.8 as a part of the NHMRC range of 1.2 to 2.2, in the README table as well as the report. A wider PAL window would widen the short-term range, since energy is the second driver. This is a decision, not an error.
7. **The 2,000-draw design.** Bootstrap intervals are about ±0.03 on the large indices, which is adequate for the shares quoted to whole percent. No change.

## Register rows touched

None.

## Commands to rerun (repository root; S is my scratch folder)

    python3 $S/v41/stats.py analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv
    python3 $S/v41/sobol.py analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv
    python3 $S/v41/sobol2.py analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv
    python3 $S/v41/more.py
    python3 $S/v41/compare.py ; python3 $S/v41/compare.py short:land:first_order=0.40
    MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 MC_ZONES=national node analysis/sensitivity_2025/monte_carlo.mjs $S/b41/work out.csv fixed '{}'
    MC_RELEASE=2025-fixed MC_LONG=1 MC_ZONES=national node analysis/sensitivity_2025/monte_carlo.mjs $S/b22/work nat.csv 1000

## Files read

`qa/briefs/V41_check_B115.md`, `qa/briefs/_checker_rules_results_wave.md`, `qa/briefs/B115_monte_carlo_widened.md`, `analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv`, `monte_carlo_draws_2025-fixed_all.csv`, `monte_carlo.mjs`, `README.md` (B115 section), `summarise_mc.py` (head), `build_variants.py` (head), `check_wide.py`, `sobol_2025-fixed.csv`, `results/ranges_2025-fixed.csv`, `results/ranges_2025-fixed_wide.csv`, `results/2025-fixed.csv`, `results/2011-fixed.csv`, `analysis/method_tests_2025/design_choices.csv`, `analysis/waste_2025/README.md`, `methods/loss-factors-australia/method.json`, `pipeline/yields/recent/livestock_zone.py` (parts), `data/abs-2022-25/group_trend.json`, the NHMRC NRV PDF (dietary energy pages), `qa/sources_register.csv` (row A27), `qa/reports/B115_monte_carlo_widened.md`.
