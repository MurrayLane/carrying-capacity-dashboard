# V14: independent re-check of the Monte Carlo ranges, 2025-fixed

Summary: **A holds. B holds** (23 of 24 ends agree within error at 300 draws; the one miss, Rangelands short p95, agrees on a 1,000-draw rerun with another seed). **C holds**, with one point on "about equal in size" (see below). **D holds with flags:** five choices have ends that are judgements, not cited sources.

## Tolerances set before comparing, and the deliberate wrong values
- A: the base must equal `results/2025-fixed.csv` capacity within 0.5%, with zone and setting keys matching exactly; p5 <= capacity <= p95. Deliberate wrong values fed to the code: Rangelands short x1.01, Australia long set to 16.6 million, Western NSW long set to 99,999,999. All three came back as base mismatches, and the last two also came back as outside p5 to p95. The check can fail.
- B: my p5 or p95 agrees with the file's when |mine - file| <= 2 x SE x sqrt(1 + n/1000). SE is the bootstrap standard error of my own percentile (1,000 resamples of my draws). The second term allows for the file's own sampling error from its 1,000 draws. Percentiles use linear interpolation. Deliberate change: red-meat share range doubled (0.478 to 0.702 about the 0.578 mode, same seed). See below.
- C: opposite signs required. The part that moves the same way at both ends ((lo+hi)/2) should be under 1%. Deliberate wrong input: I ran the same code on the old folder `sens2`.

## A. Base assertion: holds
All 120 zone-and-setting rows of `results/ranges_2025-fixed.csv` have a matching row in `results/2025-fixed.csv`, with no extra or missing keys. In all 120 the base equals the release capacity to the person. All 120 bases lie inside p5 to p95, and none lies within 2% of either end.

## B. Independent rerun: holds
My sampler (`mysampler.mjs`) uses plain independent draws, not Latin hypercube. Its PRNG is my own splitmix-style generator, seed 4242, 300 draws. It draws the same 13 choices as the header. The distributions are those the header states; the uniform or triangular shape of the three long-term choices was taken from the script's draw code, because the header gives only their ranges. It uses the evaluator and the b22/work matrices as differences from `data/2025/yield_matrix_livestock.csv`. My own centring check of b22/work gives a largest relative lo/hi offset of 5.2e-8. No yield rows are locked in 2025-fixed for these zones, and all 119 organic cells are at the default 0.80834. My base reproduces the release: Australia 41,503,537 and 15,623,209.

| Zone | setting | my p5 (SE) | file p5 | agree | my p95 (SE) | file p95 | agree |
|---|---|---|---|---|---|---|---|
| Australia (1) | short | 36,238,048 (198,159) | 36,332,875 | yes | 45,776,034 (178,179) | 45,763,902 | yes |
| Australia (1) | long | 13,372,275 (95,538) | 13,386,284 | yes | 16,488,963 (65,111) | 16,521,832 | yes |
| Rangelands WA (52) | short | 153,667 (641) | 153,454 | yes | 174,618 (435) | 176,195 | **no** (diff -1,577, tol 992) |
| Rangelands WA (52) | long | 44,386 (180) | 44,530 | yes | 51,318 (346) | 51,546 | yes |
| Western NSW (14) | short | 352,415 (1,942) | 353,485 | yes | 423,358 (591) | 424,579 | yes |
| Western NSW (14) | long | 52,150 (545) | 52,023 | yes | 66,300 (536) | 66,075 | yes |
| Corangamite (16) | short | 461,645 (1,608) | 461,213 | yes | 511,662 (629) | 511,976 | yes |
| Corangamite (16) | long | 44,214 (676) | 44,223 | yes | 61,099 (627) | 60,633 | yes |
| Wet Tropics (39) | short | 272,550 (1,513) | 273,074 | yes | 348,304 (1,323) | 348,457 | yes |
| Wet Tropics (39) | long | 82,262 (1,036) | 81,682 | yes | 106,333 (1,086) | 105,949 | yes |
| North Tasmania (57) | short | 174,731 (777) | 174,487 | yes | 195,318 (578) | 196,161 | yes |
| North Tasmania (57) | long | 47,643 (672) | 47,898 | yes | 68,135 (752) | 68,385 | yes |

Expected sampling error at 300 draws is about 0.5% of the value for Australia's ends and 0.2% to 2% for the zones (the SE column).

The single miss is 0.9%. With 24 tests at about 2 SE, one miss is what chance gives. To settle it, I ran 1,000 independent draws of Rangelands with seed 9001:
- short: p5 154,128 against 153,454, p95 176,028 against 176,195, both within tolerance;
- long: 44,415 against 44,530 and 51,393 against 51,546, also within tolerance.

So the miss was my sampling error, not a fault in the file. The bootstrap probably understates the SE at the upper tail, because the meat window is a three-valued choice and the distribution is lumpy there.

**Deliberate change (red-meat share range doubled, same seed 4242):**
- 10 of the 12 short-term ends move outside tolerance. Australia goes to 34.84 to 47.08 million against 36.33 to 45.76 (p5 diff -1.49 million, tol 0.98 million); Western NSW, Corangamite, Wet Tropics and North Tasmania move at both ends.
- Rangelands short stays inside, because red meat matters little there.
- The long term is unchanged, as it should be: red meat is a short-term input.

The check can fail.

## C. Symmetry and guard: holds
Effect on capacity of each factor alone, b22/work, compared with the base:

| factor | result | -1 | +1 | same-way part | size ratio, -1 against +1 |
|---|---|---|---|---|---|
| field crops (±14%) | Australia short | -0.06% | +0.05% | -0.01% | 1.23 |
| field crops (±14%) | Australia long | -0.30% | +0.23% | -0.04% | 1.32 |
| field crops (±14%) | Rangelands short | -0.22% | +0.17% | -0.03% | 1.32 |
| field crops (±14%) | Rangelands long | -0.85% | +0.65% | -0.10% | 1.31 |
| veg, fruit, nuts (±20%) | Australia short | -0.12% | +0.08% | -0.02% | 1.50 |
| veg, fruit, nuts (±20%) | Australia long | -0.36% | +0.24% | -0.06% | 1.49 |
| veg, fruit, nuts (±20%) | Rangelands short | -1.79% | +1.23% | -0.28% | 1.46 |
| veg, fruit, nuts (±20%) | Rangelands long | -3.25% | +2.29% | -0.48% | 1.42 |

The signs are opposite in all eight, and the same-way part is under 0.5%.

The sizes are not equal: the -1 effect is 1.2 to 1.5 times the +1 effect. That is the expected reciprocal response, not an offset. Land needed scales as 1/yield: 1/0.86 - 1 = +16.3% against 1 - 1/1.14 = 12.3%, a ratio of 1.33; for ±20%, 25% against 16.7%, a ratio of 1.50. These match the measured ratios. So "about equal" holds only in this reciprocal sense. They agree with README X054: Rangelands short -0.2%/+0.2% and -1.8%/+1.2%; Australia long -0.3%/+0.2%.

On the old folder `sens2`, the same code moves the same way at both ends: Rangelands short field crops -8.35%/-8.02%, Australia long +4.35%/+4.93%. This reproduces the X054 "before" figures and shows the check can fail.

Guard. On the old folder, `MC_RELEASE=2025-fixed MC_ZONES=all MC_LONG=1 node analysis/sensitivity_2025/monte_carlo.mjs .../sens2 .../v14/guard_old.csv 2` exited with code 1 and wrote no file. Its message was:
> work folder /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/sens2 was not built on the current base matrix (314 offsets, for example field crops: zone 1 row 96 offset 16.01%; field crops: zone 1 row 97 offset -7.98%; field crops: zone 1 row 98 offset 0.14%); rebuild it with build_variants.py

On b22/work, the same command printed "wrote 2 draws" and exited with code 0.

## D. Sources of the ranges: holds, with flags
| # | choice | range | stated source (header, README) | flag |
|---|---|---|---|---|
| 1 | sf field-crop factor | ±14%, uniform | "measured error of the rule" (header; README rows 36 and 40) | sourced, as an in-house measurement; the measurement itself is not cited in this README |
| 2 | sh veg/fruit/nut factors | ±20%, uniform | measured error "20 to 22%" (README row 41) | sourced; the range uses the low end of 20 to 22% |
| 3 | meat window | base / 2020-21 to 2022-23 / 2022-23 to 2024-25, equal chances | README l.106: "a three-way choice with equal chances that I made" | **no external source: a judgement.** README l.110 says full-cycle windows are the better basis |
| 4 | meategg | tri 0.115, 0.12, 0.13 | 0.12 proxy, 0.13 the 2011 value | **low end 0.115 is "one step below the proxy" (README row 49): no source.** The source of the 0.12 proxy is not stated in the README |
| 5 | redmeat | tri 0.528, 0.578, 0.64 | 0.578 proxy from FAO food balance sheets (README l.15); 0.64 the 2011 value | **low end 0.528 is "5 points below the proxy": no source** |
| 6 | fuel | U 2360 to 2520 L | proxy value and 2011 value (README row 61) | 2011 end sourced; the source of the 2360 proxy is not stated in the README |
| 7 | biofuel | U 0.0023 to 0.005 | proxy and 2011 value | as for fuel |
| 8 | timber | U 0.8 to 1.0 m3 | proxy and 2011 value | as for fuel |
| 9 | orgfac | U 0.771 to 0.845 | Ponisio et al. 2015 range | sourced |
| 10 | orgshare | tri 0.02, 0.07, 0.12 | 0.02 the 2011 value; 0.12 "the share of agricultural land the 2026 report gives" (README row 53) | ends sourced; the 0.07 mode is the release default, with no source given here |
| 11 | restable | the release table or the 2025-resilience-loo table, 50/50 | header and README l.139: leave-one-out table | an alternative internal table; **the 50/50 weighting has no stated source** |
| 12 | lfuel | tri 156, 210, 253 L | 156 with light vehicles electrified, 210 re-derived, 253 the thesis (header, README l.139) | sourced to in-house derivations and the thesis |
| 13 | lbench | tri 0.30, base, 0.525 | South Korea 42.5%, Japan 35.9%, Japan without households 52.5% (header) | **0.30 ("lower for Australia") has no source.** Inert in 2025-fixed, see below |

## Found outside the brief
1. In 2025-fixed, `lbench` is inert. The cells Settings!BQ4:BQ7 do not exist in the release model, so the script's `hasBench` is false and lbench is held at a constant 0.4. The file's `influence_lbench` is 0.0 everywhere. Only 12 of the 13 choices vary.
2. The header line under `MC_LONG` has a different short-term preset handling from the long term. The draws set organic, meategg, redmeat, fuel, biofuel and timber in the short preset only. The long preset keeps its own defaults and takes only the drawn long fuel; organic share enters the long term through Yield!E2. This is consistent with the header, but the header does not say it.
3. The 2026-11-04 README section still shows an older Australia corrected range (35.9 to 45.1, 14.3 to 17.8 in l.178). The file now gives 36.33 to 45.76 and 13.39 to 16.52, matching the README's X054 trial (36.4 to 45.9, 13.3 to 16.4). The table at l.178 is stale against the file; this is a README text issue only.
4. README l.193 says the same-way part after the rebuild is "under 1% in all 120 zone-and-setting results". My four-row sample agrees (largest 0.48%).

## Commands to rerun (from /home/user/carrying-capacity-dashboard)
```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad
node $S/v14/mysampler.mjs $S/v14/oat.csv 0 1 oat                                      # C, b22/work
V14_WORK=$S/sens2 V14_ZONES=1,52 node $S/v14/mysampler.mjs $S/v14/oat_sens2.csv 0 1 oat  # C, old folder (should fail)
node $S/v14/mysampler.mjs $S/v14/draws300.csv 300 4242                                # B (about 3 minutes)
node $S/v14/mysampler.mjs $S/v14/draws300_red2x.csv 300 4242 draws '{"redmeatLo":0.478,"redmeatHi":0.702}'   # B, deliberate change
V14_ZONES=52 node $S/v14/mysampler.mjs $S/v14/draws1000_z52.csv 1000 9001             # B, Rangelands follow-up
python3 -I $S/v14/analyse.py $S/v14/draws300.csv results/ranges_2025-fixed.csv        # comparison (also for the red2x and z52 files)
MC_RELEASE=2025-fixed MC_ZONES=all MC_LONG=1 node analysis/sensitivity_2025/monte_carlo.mjs $S/sens2 $S/v14/guard_old.csv 2   # guard: refuses
MC_RELEASE=2025-fixed MC_ZONES=all MC_LONG=1 node analysis/sensitivity_2025/monte_carlo.mjs $S/b22/work $S/v14/guard_new.csv 2 # guard: accepts
```
The part A check is an inline python script. It joins the two results files on (zone, setting/preset) and tests base equality and p5 <= capacity <= p95.

## Files read
- qa/briefs/_checker_rules_results_wave.md
- qa/briefs/V14_ranges_recheck.md
- analysis/sensitivity_2025/monte_carlo.mjs: the whole file, all 135 lines. My first read printed past the header, which the brief limits me to, so I saw the script's draw code. My sampler is my own code, but it necessarily follows the same arithmetic. I used the draw code only to learn the shapes of the three long-term choices.
- analysis/sensitivity_2025/evaluate.mjs
- analysis/sensitivity_2025/README.md (by section and grep)
- web/src/model/evaluator.js (lines 1 to 80)
- web/scripts/releases.mjs (imported only, to list the release's yield factors: none)
- web/public/data/2025-fixed/{model,regions}.json
- web/public/data/2025-resilience-loo/model.json
- web/public/data/2011-fixed/regions.json (2011 presets)
- data/2025/yield_matrix_livestock.csv
- b22/work/*/yield_matrix_livestock.csv and variants.json; sens2 matrices
- results/2025-fixed.csv
- results/ranges_2025-fixed.csv (read after my draws were complete)

Not read: qa/reports/V08_*, qa/reports/B22*, qa/defects.csv.
