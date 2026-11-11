# B79: small fixes after V28 and B77 (decisions 70, 71)

Brief: `qa/briefs/B79_small_fixes_after_V28.md`. Only the five files the brief names were written.

## What changed

1. `papers/B_methods/SECTION7_DRAFT.md`
   * Line 24 (purpose 1, EP, FP, HALF, PPH): before "they read 134 to 343 million"; after "they read 103 to 343 million" (claims B046, B156, B247 in `qa/claims_register.csv` give 103 to 343; 134 is the low end of the energy and protein balance alone).
   * Matrix, purpose 2 row: HALF and PPH changed from not suited to partly. Purpose 3 row: FP changed from not suited to partly (decision 69).
   * Purpose 2 reasons (HALF, PPH bullet): now marked partly; the draft's original reason (not capacity methods; HALF not predictive; PPH cropland only) is kept as "stated limit", and the V28 one-line reason is added (read as a capacity, 276 and 76.0 million for HALF, 145 to 190 million for PPH, they show why land-per-diet and calorie counts read high).
   * Purpose 3 reasons (line 34): FP split out as partly; the original reason (world-average productivity, national as run) kept as "stated limit", with the V28 reason (local-productivity adjustment, Wackernagel and Rees 1996 p. 78, 64.8 to 84.6 million; regional use beside a capacity figure).
2. `analysis/scale_curve_2025/README.md` line 47: before "needs the SA2 boundaries ... which are not in the repository ... the achievable contiguous value is not known yet"; after: adjacency is in `data/sa2/adjacency.csv`; the search was run (`analysis/regionalise_2025/summary.csv`): at 53 regions, cap 650,000 km2, 76% (75.7) short term and 69% (69.4) long term, lower bounds from a heuristic (A124; A347 to A353); the unconstrained 100% and random 68 to 81% remain the references.
3. `analysis/comparison_2025/decompose.mjs` line 9, comment only: before "checked: 2025-land and 2025-population give identical capacities"; after: identical in every zone except Northern and Yorke (zone 45), where infrastructure land that follows population moves capacity (B76). `node --check` passes; no code changed.
4. `qa/defects.csv`: appended X105 (scale-curve README line; found_by S02/B77, fixed_in B79) and X106 (decompose.mjs comment; found_by B76, fixed_in B79), layer 5. File still parses (106 lines including header, 8 fields each), CRLF line endings kept.

## Register rows touched

None.

## Wrong-value check

Example of a wrong fix (deliberately wrong, not applied): changing 134 to 143 in the purpose 1 line. It would still disagree with B046 and B156 (103 to 343), so a check against the register would flag it.
