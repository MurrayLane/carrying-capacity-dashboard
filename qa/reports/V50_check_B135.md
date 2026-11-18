# V50: blind check of B135 (the shares robustness table; the footprint's own accounting)

Brief: `qa/briefs/V50_check_B135.md`; rules `qa/briefs/_checker_rules_results_wave.md`. No git, no subagents, no network. My code sits outside the repository (scratch: `check.py`, `compare.py`, `compare_alt.py`); this file is the only repository file written.

Order kept: I read the B135 brief, `harmonised_comparison_lines.csv`, the README's footprint and harmonised sections (up to the line before the B135 section), the "share closed" definition in `V39_check_B113.md`, `simpson_food.csv` and `harmonised_comparison.csv` (the footprint build files), wrote and ran my own code, and only then opened `harmonised_robustness.csv`, `harmonised_robustness_footprint.csv`, the B135 report, the B135 README section and two lines of `harmonised_robustness.py`.

## Tolerance

Counts and labels exactly; shares, SDs, ratios and multiples within one unit of the last printed digit (share 0.001; SD 0.001; max to min 0.01; footprint ratios 0.01; readings 0.1 million).

## Wrong-value check (example)

EXAMPLE, deliberately wrong: I fed my comparison the line (a) base share to 41.5 as 0.045 in place of my computed 0.0411. It reported `FAIL base (all 19 readings, geometric-mean centres) a 41.5 share closed builder 0.041 mine 0.045`; with the true value the cell passes. A second deliberate value (stating 4.5% in the reproduction check) also printed FAIL.

## My route and figures

Definitions (README and V39): per method D = mean over its paired readings of |ln(reading / R)|; five methods weighted equally; S = (sum D as run - sum D harmonised) / sum D as run; a method's centre = geometric mean of its readings; median and geometric-mean references from each stage's own centres; SD of logs with divisor n. A median of an even number of values is the mean of the middle two.

Reproduced: 4.1% (4.109) and 38.5% (38.536) to 41.5; SD of log centres 0.646 to 0.702 (a) and 0.646 to 0.440 (b), narrowing 31.8%; highest over lowest 6.22 to 6.95 (a) and 6.22 to 3.70 (b); all 19 readings 0.718 to 0.604 and 22.69 to 12.40 (b).

Share closed by variant (references 31.1 / 41.5 / 49.2 / 53.6 / median / geometric mean), %:

| Variant | Line (a) | Line (b) | SD log centres (b), narrowing |
|---|---|---|---|
| base | 3.3 / 4.1 / 4.5 / 4.7 / -4.9 / -6.3 | 32.6 / 38.5 / 42.3 / 44.4 / 16.0 / 17.2 | 0.646 to 0.440, 31.8% |
| energy balance out | 2.4 / 3.1 / 3.4 / 3.5 / -14.4 / -9.5 | 39.1 / 45.9 / 49.9 / 52.2 / 35.5 / 32.0 | 0.720 to 0.378, 47.5% |
| footprint out | 5.5 / 6.8 / 7.4 / 7.8 / -5.2 / -2.7 | 26.2 / 31.1 / 34.0 / 35.7 / 9.6 / 10.7 | 0.674 to 0.492, 27.0% |
| HALF out | 4.5 / 5.6 / 6.2 / 6.5 / -1.1 / 0.3 | 23.2 / 27.7 / 30.4 / 31.9 / 9.4 / 5.9 | 0.637 to 0.490, 23.2% |
| people per hectare out | -1.2 / -1.1 / -1.2 / -1.2 / -6.2 / 1.4 | 35.4 / 41.5 / 45.1 / 47.1 / 24.7 / 26.9 | 0.721 to 0.464, 35.7% |
| commodity balance out | 5.3 / 6.2 / 6.9 / 7.4 / -32.1 / -27.4 | 37.5 / 44.3 / 49.6 / 52.8 / 12.5 / 14.5 | 0.236 to 0.263, -11.5% |
| fish dropped | 4.6 / 5.9 / 6.6 / 6.9 / -0.5 / -2.3 | 33.7 / 40.9 / 45.3 / 47.9 / 18.2 / 23.0 | 0.469 to 0.270, 42.4% |
| pasture-alone dropped | 2.9 / 3.7 / 4.1 / 4.3 / -3.2 / -5.4 | 29.6 / 35.1 / 38.6 / 40.7 / 16.1 / 15.4 | 0.623 to 0.442, 29.0% |
| median as method centre | 3.3 / 4.1 / 4.5 / 4.7 / -5.1 / -4.7 | 32.6 / 38.5 / 42.3 / 44.4 / 15.6 / 17.4 | 0.717 to 0.430, 39.9% |
| energy balance alone (41.5) | 8.2 | 8.2 | one centre, undefined |
| footprint and HALF out (41.5) | 10.5 | 10.5 | 0.611 to 0.565, 7.7% |

Ranges over these variants: line (a) to 41.5 -1.1% to 6.8%; at the four model references -1.2% to 7.8%; to the median -32.1% to -0.5%. Line (b) to 41.5 27.7% to 45.9%; at the four references 23.2% to 52.8%; to the median 9.4% to 35.5% (the 4.1% low end needs the scale-up variant, below).

Footprint accounting (population 26.20 million; build 1 output 22.3 and 46.4 Mha world-average and footprint 0.198 and 0.860 ha; build 3 output 25.3 and 81.6 Mha and footprint 0.216 and 1.047 ha on 2021-23 yields, from the `harmonised_comparison.csv` notes and `simpson_food.csv`): ratios build 1 cropland 4.30 (4.29 from the reading 112.5 / 26.20), pasture 2.06, pooled 2.48 (2.47 from 64.8 / 26.20); build 3 4.47, 2.97, 3.23. Pooled = consumption-weighted mean of the land-type ratios. Binding land type: min of cropland and pasture per build, 53.9 (build 1; 54.0 from the rounded 46.4 Mha) and 77.9, 1.30 and 1.88 times 41.5, 1.01 and 1.45 times 53.6. Pooled 64.8 to 117.0: 1.56 to 2.82 and 1.21 to 2.18.

## Comparison

`harmonised_robustness.csv`: 176 rows, 2,072 numeric cells reached (every row and column). All cells of the variants in my brief match within tolerance (0 fails). The three land scale-up rows (not in my brief) fail under my reading and all match under the builder's (see finding 1).

| Item | Builder | Mine | Verdict |
|---|---|---|---|
| Base 4.1%, 38.5%; 0.65 to 0.44; 6.2 to 3.7 | as printed | 4.109, 38.536; 0.646 to 0.440; 6.22 to 3.70 | pass |
| Robustness csv, variants in my brief (all references, all spread columns) | csv | identical within tolerance | pass |
| Robustness csv, three land scale-up variants | e.g. (b) 36.5% to 41.5, 4.1% to median (combined) | 35.8%, 5.4% (scale factor kept, consumption harmonised) | fail on definition (finding 1) |
| Line (a) to 41.5 | -1.1% to 6.8% | -1.1% to 6.8% | pass |
| Line (a) four references | -1.2% to 7.8% | -1.2% to 7.8% | pass |
| Line (a) to median | -32.1% to -0.5% | -32.1% to -0.5% | pass |
| Line (b) to 41.5 | 27.7% to 45.9% | 27.7% to 45.9% | pass |
| Line (b) four references | 23.2% to 52.8% | 23.2% to 52.8% | pass |
| Line (b) to median | 4.1% to 35.5% | 9.4% to 35.5% on my variants; 5.4% to 35.5% with my scale-up reading | fail at the low end (finding 1) |
| Without footprint and HALF | 10.5% | 10.5% | pass |
| Energy balance alone | 8.2% | 8.2% | pass |
| "About a third" depends on the commodity balance; without it widens 11.5% | 0.236 to 0.263 | 0.236 to 0.263, -11.5% | pass |
| Narrowing 22.3% to 47.5% with the commodity balance in | core set | 23.2% to 47.5% on my variants; 22.1% with my scale-up reading; 7.7% for footprint and HALF out | pass for the core set; see sentence 5 |
| Footprint ratios build 1 (4.29, 2.06, 2.47), build 3 (4.47, 2.97, 3.23) | csv | same | pass |
| Binding reading 53.9 to 77.9; 1.30 to 1.88 (41.5); 1.01 to 1.45 (53.6); pooled 1.56 to 2.82, 1.21 to 2.18 | csv, report | same | pass |
| Footprint csv, build 3 cropland-bound and together: footprint, consumption, output cells | 0.307 / 8.04 / 35.92; 1.354 / 35.47 / 114.55 | 0.216 / 5.66 / 25.3; 1.263 / 33.09 / 106.9 | fail (finding 2); ratios and readings unaffected |
| Footprint csv, all other cells | csv | same (1.058 against 1.059 is rounding) | pass |

## Findings

1. **The land scale-up variant is defined differently from R05b's scratch.** The builder's "classed as method" keeps the four scaled energy readings (and Cassidy's 190) at their as-run values, so it also undoes the consumption harmonisation on those readings. Keeping only the scale-up as method (harmonised production-as-it-is reading times the same land factor: 169.5, 173.7, 222.3, 227.9; Cassidy 145.5) gives 1.4% (a) and 35.8% (b) to 41.5, which is exactly R05b's scratch, the one row the builder reports as not reproduced. Under that reading the combined variant gives 5.4% (not 4.1%) to the median on line (b), so the line (b) median range is 5.4% to 35.5% (or 9.4% to 35.5% without it), not 4.1% to 35.5%. No other headline range moves.
2. **Footprint csv build 3 intermediates use the wrong footprint.** `harmonised_robustness.py` line 128 hard-codes build 3 cropland 0.307 and together 1.354 ha (the thesis's 1990 yields), but the 117.0 and 84.6 readings rest on the 2021-23-yield footprint 0.216 and 1.263 ha (`harmonised_comparison.csv` note: output 25.3 and 81.6 Mha). The csv's consumption and output columns for those two rows are therefore wrong; the ratios (computed from readings over population) are right. The report does not print these cells.

## The six paper sentences (do they say no more than the figures support?)

1. Holds (an ordering instruction).
2. Holds (4.29, 2.06, 2.47; pooled is output-inclusive of exports).
3. Holds as a classification statement. "Australian hectares divided by world-average hectares" is loose: it is Australia's physical hectares divided by a per-person footprint in world-average hectares.
4. Overstates. "-1% to 7% across references at 31.1 to 53.6 million" should be -1% to 8% (-1.2% to 7.8%). "4% to 36%" to the median rests on the contestable scale-up variant (5% to 36% under R05b's construction; 9% to 36% without it). "So the line (b) closure is the productivity conversion of those two land indices": the footprint and HALF give about 87% of the line (b) closure in log distance; "mostly" is supported, "is" is not.
5. Overstates "in every variant that keeps the commodity balance": footprint and HALF out keeps it and narrows only 7.7%. Supported if limited to the core set or to "each single method left out" (23% to 48%). "Widens by 12%" holds (11.5%).
6. Wrong word: the pasture is not in shortfall (ratios 2.06 and 2.97); it is a smaller surplus, as the builder's own README says. Numbers hold.
Abstract: "almost all of it the footprint and HALF" is a stretch at about 87%; "most of it" is supported. Highlight (82 characters, counted) holds on line (b) (footprint 61%, HALF 68% of own distance), but should say it is under the own-productivity classification.

## Claim rows the builder says move

- B276 (A): range values hold except the line (b) median low end: 4% depends on finding 1; I would print 5% to 36% (or 9% to 36% without the combined scale-up variant). Line (a) and line (b) to the model, as stated, agree.
- B277 (A): value unchanged, holds; the commodity-balance dependence (widens 11.5%) holds; "22% to 48% with it in" holds for the core set only (7.7% with the footprint and HALF out).
- B270 (B): holds (53.9 to 77.9; 1.30 to 1.88; 1.01 to 1.45; ratios as stated).
- B156, B046: no figure moves; agree.

## What I would do differently

Define the scale-up variant as "scale factor kept, consumption harmonised" (reproduces R05b), or print both; take build 3's footprint for the accounting csv from the same 2021-23 basis as its readings; qualify sentences 4 and 5 as above and fix "shortfall".

## Register rows touched

None.

## Rerun

From `/home/user/carrying-capacity-dashboard`: `python3 -I <scratch>/v50/check.py` (my figures and the reproduction checks) and `python3 -I <scratch>/v50/compare.py` (cell comparison; add any argument to inject the wrong value); `compare_alt.py` is the builder's scale-up reading, which gives 0 fails on all 2,072 cells.
