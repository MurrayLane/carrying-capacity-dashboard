# V24: independent re-check of the Monte Carlo ranges of 2025-improved and 2025-mirror (B114; B110, B111, B115)

Summary: **A holds** (all 8 ends, for both releases and both presets, agree with the claims and with the files within tolerance). **B holds** (120 of 120 rows in each file: the base equals the release capacity to the person and lies inside p5 to p95). **C**: the report, commands and files read are below.

## Tolerances set before comparing, and the deliberate wrong values
- A: my p5 or p95 agrees when |mine - stated| <= 2 x SE x sqrt(1 + 300/1000). SE is the bootstrap standard error of my own percentile (1,000 resamples). The square-root term allows for the file's own error from its 1,000 draws, as in V14. Percentiles use linear interpolation. Against the claims, which are printed to 0.1 million, I add half a unit (0.05 million). Against the files' unrounded values I add nothing.
- Deliberate change for A: the red-meat share range was doubled (0.478 to 0.702 about the 0.578 mode), with the same seed.
- B: keys must match exactly; the base must be within 0.5% of the release capacity; and p5 <= base <= p95. Deliberate wrong values: Australia short base x1.01, and Australia long base set to 25 million.

## A. Independent 300-draw rerun: holds
Sampler: `v24/mysampler24.mjs`. This is V14's sampler with only these changes:
- the release can be switched (`V24_REL`);
- zones are Australia only;
- the release's regional yield factors are applied to the matrices before differencing, as the header says the matrices hold unscaled yields. This is one factor, on row 98 (cattle meat); it is 1 for Australia, so it is inert here;
- `lbench` is drawn (triangular 0.30, base, 0.525, on Settings!BQ4:BQ7) wherever the release has those cells.

The rest is the same as V14:
- plain independent draws, my own splitmix-style PRNG, **new seed 7177**, 300 draws;
- the 13 choices with the header's distributions;
- the b22/work matrices, used as differences from `data/2025/yield_matrix_livestock.csv`.

Locked rows, found by my own comparison of the release yield vector with the matrix:
- **2025-improved, Australia: row 97 (dairy milk) is locked**, as the header says. It is kept at the release value and takes no group-factor or meat-window difference.
- 2025-mirror: no rows are locked.

Organic factor:
- In 2025-improved, 3 of the 119 organic cells are at 0.9 (the organic-ruminant module) and are held there. The other 116, which are at the default 0.80834, are drawn.
- In 2025-mirror, all 119 cells are drawn.

lbench:
- It is active in 2025-improved (base 0.4).
- It is absent from 2025-mirror (no BQ4:BQ7), so mirror varies 12 choices.

My centring check of b22/work gives a largest relative offset of 5.2e-8.

My base reproduces the releases:
- improved: 53,643,731 short and 18,496,334 long;
- mirror: 49,389,414 short and 14,146,847 long.

These equal `results/<release>.csv`.

| release | preset | end | mine (SE), million | claim | file | diff vs file | tol vs file | agree |
|---|---|---|---|---|---|---|---|---|
| improved | short | p5 | 46.166 (0.358) | 46.2 | 46.176 | -0.010 | 0.817 | yes |
| improved | short | p95 | 60.353 (0.526) | 60.1 | 60.117 | +0.236 | 1.200 | yes |
| improved | long | p5 | 15.837 (0.021) | 15.9 | 15.873 | -0.036 | 0.047 | yes |
| improved | long | p95 | 19.375 (0.098) | 19.4 | 19.418 | -0.042 | 0.223 | yes |
| mirror | short | p5 | 43.610 (0.293) | 43.4 | 43.430 | +0.180 | 0.668 | yes |
| mirror | short | p95 | 54.234 (0.217) | 54.3 | 54.251 | -0.017 | 0.495 | yes |
| mirror | long | p5 | 11.783 (0.117) | 11.8 | 11.779 | +0.003 | 0.267 | yes |
| mirror | long | p95 | 15.851 (0.148) | 16.0 | 15.992 | -0.141 | 0.337 | yes |

All 8 ends also agree with the rounded claims (with the 0.05 rounding allowance), and the claims are the files' values rounded correctly.

**Deliberate change (red meat doubled, seed 7177):**
- improved short p5 goes to 44.216 against 46.176 (diff -1.960, tol 0.989): **outside**.
- mirror short p95 goes to 55.828 against 54.251 (diff +1.528, tol 1.072 against the claim): **outside**.
- The long-term ends do not move, as they should not, because red meat is a short-term input.

The check can fail.

## B. Base assertion: holds
- 2025-improved: 120 rows in the ranges file and 120 in `results/2025-improved.csv`, with no missing or extra keys. All 120 bases equal the release capacity to the person, and all lie inside p5 to p95. Leaving out zero rows, the closest a base comes to an end is 1.33%.
- 2025-mirror: the same result (120 of 120), with the closest at 1.23%.
- In both files, zone 42 has capacity 0 in both presets, with p5 = p95 = 0. The base of 0 lies inside that degenerate range.
- With the deliberate wrong values, the check reported 3 problems in each file: Australia short base mismatch, Australia long base mismatch, and Australia long base outside p5 to p95. The check can fail.

## Found outside the brief
1. **The improved long p5 sits at a lumpy point of the distribution.** Its bootstrap SE (0.021 million) is unusually small, and my value passes with little room (diff 0.036 against tol 0.047). The file's influence column puts 0.545 of the long variance on `restable`, a 50/50 two-valued switch. So the long-term distribution is likely two-humped, and the bootstrap may understate the SE at p5. The pass is sound, but it is the tightest of the 8 tests.
2. In mirror long, `sf` and `sh` matter more than in improved long. My one-at-a-time runs give -6.4%/+5.4% for field crops and -4.5%/+3.3% for veg, fruit and nuts, against -0.7%/+0.3% and -1.3%/+0.3% in improved. That is consistent with the files' influence columns (mirror long sf 0.136, improved long 0.014). The likely cause is that improved locks the dairy row and adds its own modules; I did not trace this further.
3. In the file, mirror's `influence_lbench` is 0.0 everywhere, consistent with lbench being inert there. Improved's is 0.004 for Australia in both presets.
4. The header does not say that `lbench` is set on all four cells BQ4:BQ7 at one value; I took that from the script's draw line (line 101, seen by grep).

## Commands to rerun (from /home/user/carrying-capacity-dashboard)
```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad
V24_REL=2025-improved node $S/v24/mysampler24.mjs $S/v24/oat_imp.csv 0 1 oat          # base and one-at-a-time check
V24_REL=2025-mirror   node $S/v24/mysampler24.mjs $S/v24/oat_mir.csv 0 1 oat
V24_REL=2025-improved node $S/v24/mysampler24.mjs $S/v24/draws300_imp.csv 300 7177     # A (about 45 s each)
V24_REL=2025-mirror   node $S/v24/mysampler24.mjs $S/v24/draws300_mir.csv 300 7177
V24_REL=2025-improved node $S/v24/mysampler24.mjs $S/v24/draws300_improved_red2x.csv 300 7177 draws '{"redmeatLo":0.478,"redmeatHi":0.702}'   # A, deliberate change
V24_REL=2025-mirror   node $S/v24/mysampler24.mjs $S/v24/draws300_mirror_red2x.csv 300 7177 draws '{"redmeatLo":0.478,"redmeatHi":0.702}'
python3 -I $S/v24/claims.py $S/v24/draws300_imp.csv 46.2 60.1 15.9 19.4               # vs claims (0.05 rounding allowance)
python3 -I $S/v24/claims.py $S/v24/draws300_mir.csv 43.4 54.3 11.8 16.0
python3 -I $S/v24/claims.py $S/v24/draws300_imp.csv 46.175771 60.117042 15.873433 19.417732 0   # vs file values
python3 -I $S/v24/claims.py $S/v24/draws300_mir.csv 43.429543 54.251016 11.779402 15.991928 0
python3 -I $S/v24/partb.py 2025-improved ; python3 -I $S/v24/partb.py 2025-improved wrong   # B, and B's deliberate wrong values
python3 -I $S/v24/partb.py 2025-mirror   ; python3 -I $S/v24/partb.py 2025-mirror wrong
node $S/v24/rel.mjs ; node $S/v24/inspect.mjs                                          # release methods, yield factors, presets, organic and BQ cells
```

## Files read
- qa/briefs/_checker_rules_results_wave.md
- qa/briefs/V24_improved_range_recheck.md
- qa/reports/V14_ranges_recheck.md
- v14/mysampler.mjs and v14/analyse.py, which I reused
- analysis/sensitivity_2025/monte_carlo.mjs:
  - lines 1 to 60, which are the header plus the set-up code (matrix loading, yield factors, locked rows, the centring guard). That is past the header proper;
  - lines 84 to 92, the long-term header;
  - a grep for MC_LONG, lbench, lfuel, restable and BQ.
- web/src/model/evaluator.js (grep for sheet ids)
- web/scripts/releases.mjs (imported only, for each release's methods and yield factors)
- web/public/data/{2025-improved,2025-mirror,2025-fixed}/{model,regions}.json, and 2025-resilience-loo/model.json
- data/2025/yield_matrix_livestock.csv, and b22/work/*/yield_matrix_livestock.csv and variants.json
- results/2025-improved.csv and results/2025-mirror.csv (Australia rows, and all rows for B)
- results/ranges_2025-improved.csv and results/ranges_2025-mirror.csv, read only after all four of my draw files existed

Not read: the README section, qa/defects.csv and other reports.
