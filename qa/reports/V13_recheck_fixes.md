# V13 re-check: drought-proofing and scale-curve fixes (decisions 28 and 29)

Checker: independent, blind until part C. Everything in parts A and B was derived by my own scripts in the scratch folder, calling `web/src/model/evaluator.js` directly on `web/public/data/<release>/`.

## Tolerance (fixed before comparing)
- Counts and names: exact.
- Capacities: within 0.5%.
- Shares and ratios: within one unit of the last printed digit (so "49%" holds for 48.0 to 50.0; "+9.7%" holds for 9.6 to 9.8).

## The check can fail (deliberate wrong values)
- Part A: `partA.mjs 2025-fixed wrong` uses 1 - (1 - f)/3 in place of /2. It gives 28.06 million (+79.6%) against the stated 24.9 million (+60%): reported as a mismatch.
- Part B: `partB.mjs wrong` halves the land of every Victorian SA2. 2025 long SA4 then comes out at 32.7% against the stated 35%, SA3 22.4% against 24%, SA2 17.7% against 20%: reported as mismatches. The state and NRM levels, which do not use SA2 land, stay unchanged, as they should.

## Results by target

### A. Drought-proofing and livestock (2025-fixed, Australia)
| Target | Stated | Mine | Verdict |
|---|---|---|---|
| Reference, long term | 15.6 million | 15,623,209 | holds |
| Drought-proofing, long term | 24.9 million (+60%) | 24,949,043 (+59.69%) | **holds** |
| Australia 100-year factor | 0.4558 to 0.7279 | 0.455821 to 0.727911 | holds |
| Livestock output +10%, short term | +9.7% | 45,540,041 (+9.73%) | **holds** |
| Livestock output +10%, long term | +9.4% | 17,096,842 (+9.43%) | **holds** |

My method: on all 8 climate-zone rows of the `resilience` sheet (rows 2 to 9), I changed column 101 (the column whose header is 100) to 1 - (1 - f)/2. I then evaluated Australia with its own land, population and long preset. For livestock I multiplied 11 yield rows by 1.1 in the Australia record: Yield rows 95 to 103 (sheep meat, sheep wool, dairy milk, cattle meat, chicken meat, duck meat, turkey meat, chicken eggs, pig meat) and rows 135 and 136 (goat milk, sheep milk).

### B. Scale curve, state yield basis, share of the national long-term capacity
My method:
- Every unit takes its own land and population.
- Yields, all presets and the climate zone come from its state's zone record. NSW-ACT gets ASGS first digits 1, 8 and 9 (Jervis Bay).
- SA4, SA3 and SA2 units are built by summing SA2s on the first 3, 5 and 9 digits. Land comes from `land_2011_method_by_sa2.csv`. Population is the ERP column of the release year (2025 or 2011).
- The NRM level is the 52 `region` records plus NT, with their own land and population from the release.
- 2025 denominators are the national zone on the release's land. The 2011 SA levels use the national zone evaluated on the summed SA2 land (with the summed 2011 ERP).

| Cell | Level | Stated | Mine | Verdict |
|---|---|---|---|---|
| 2025 long | states | 49% | 49.14% (sum 7,677,637) | **holds**; the sum equals the stated 7,677,637 exactly |
| 2025 long | NRM (53 units) | 23% | 23.33% | **holds** |
| 2025 long | SA4 (89) | 35% | 34.94% | **holds** |
| 2025 long | SA3 (336) | 24% | 24.48% | **holds** |
| 2025 long | SA2 (2,450) | 20% | 19.75% | **holds** |
| 2011 long | states | 44% | 43.55% | **holds** |
| 2011 long | NRM | 20% | 19.72% | **holds** |
| 2011 long | SA4 | 32% | 32.07% (national on SA2 land 14,141,819) | **holds** |
| 2011 long | SA3 | 23% | 22.89% | **holds** |
| 2011 long | SA2 | 18% | 17.97% | **holds** |
| 2025 short (control) | states, NRM, SA4, SA3, SA2 | 75, 44, 58, 44, 37% | 75.37, 44.00, 58.12, 43.86, 37.42% | **holds** (all five) |

The capacity is floored at zero: no unit returned a negative value, so the raw sum and the sum of positive values are identical.

### C. Files under test
**`analysis/paper_a/measures.csv` and `long_term_and_measures.mjs`.** No difference.
- The script's route is the same as mine for both measures: `resilience` cells `r:101` for r = 2..9, and LIVE = rows 95 to 103 plus 135 to 136.
- The csv rows agree with my values:
  - Drought-proofing: long term 24.9, +59.7%; short term 41.5, 0.0%.
  - Livestock +10%: 45.5 (+9.7%) and 17.1 (+9.4%).
  - Livestock +20%: 49.6 (+19.4%) and 18.6 (+18.8%). I re-derived these as 49.56 (+19.40%) and 18.56 (+18.77%).

**`results/scale_curve.csv` and `web/scripts/make-scale-curve.mjs`.** No difference.
- On the state basis, all 2025-fixed and 2011-fixed sums match mine to the person, short and long term.
- The script evaluates each unit with the national presets, overriding only irrigation and nature2 with the state's values. I used the state's full presets. The two are equivalent because the release presets differ from the national ones only in irrigation and nature2, which I checked over all zones of both releases.
- In all six cells, the State row equals the sum of the release's own state capacities in `results/<cell>.csv`, to within 1 person of rounding.

**`analysis/scale_curve_2025/README.md`**
- Top note (units take the climate zone of the zone whose yields they use; the state level equals the release's state sum in every cell): holds.
- Table: every cell holds against the csv, and the eight state-basis columns hold against my own values.
  - Local basis, 2025 short: 75, 63, 80, 64, 54.
  - Local basis, 2025 long: 49, 38, 52, 40, 32.

*Reading it*
- "2025 states 75%, SA4 58, SA3 44, SA2 37 ... long term 49, 35, 24, 20 ... 7.7 against 15.6 million": holds.
- "2011 (77%, 60%, 46%, 40% short term)": holds (mine 77.09, 59.69, 46.32, 39.75).
- "2015 finding (national 40, states 28, regions 23 million)": the figures hold against the csv rows for 2011-corrected on the local basis (40.45, 28.28, 23.01). "Survives the corrections" is a reading, not a figure.
- "NRM ... 44% against 44% ... SA4s (58%)": holds.
- "the model's capacity does not depend on population at all": holds. Australia's short-term capacity is identical at populations of 1, 1,000, 27.6 million and 1e9.
- "rose from 75% to 80%" (local basis SA4): holds (0.799).
- "parent state's yields at every level 75, 58, 44, 37%": holds.
- "national yield vector 76, 54, 35, 28%": holds when every unit also takes the national settings (mine 75.8, 53.6, 34.8, 27.8). With the states' irrigation and nature2 it would be 75.9, 54.5, 35.8, 28.8.
- "dominant-zone yields, even the states exceed the nation (109%)": cannot determine. I did not rebuild the cropland-dominant zone of each state.
- "about 17 points at SA2 level (37% to 54%)": holds (37.4 to 53.9, 16.5 points).
- The two monotonicity statements are consistent: the state basis is monotone in both vintages and both terms; the local basis is not.

*Method and limits*
- "land_2011_method_by_sa2.csv, which sums to the national zone's land": holds within tolerance for the 2025 zone. Cropping, pasture and infrastructure agree to within 1 km2; non-agricultural is +346 km2 and reserve +203 km2. "Australia (SA land)" comes out at 15,623,208 against 15,623,209.
- "30.7 against 33.3 million short term" (2011): holds (30,685,903 against 33,307,814).
- "2,136 to 2,311 of 2,450 SA2s are over capacity across the six cells": holds against the csv's min and max. My own count for 2025-fixed on the state basis matches the csv: 2,182 short, 2,299 long.
- "The other settings (diet, waste, resilience) are the national defaults in every unit": holds; only irrigation and nature2 vary by zone.
- "national yield vector ... 10.8 against 21.0 million on the 2011 zones": holds when every unit takes the national record and national settings (10,798,143). 21.0 holds (21,009,675, 2011-fixed local NRM). With the zones' own irrigation and nature2 the first figure would be 11.2.
- "the national unit reached 77 million, not 33": 33 holds (2011-fixed national, 33,307,814); 77 cannot determine, because I did not rebuild the rejected averaged vector.

*Why the NRM regions do so badly*
- "Rebuilding the NRM regions from whole SA2s gives the same 44%": cannot determine. I did not build the SA2-to-NRM allocation.
- By state, NRM against SA4 (and the state itself):
  - NSW 17.6 / 25.3 (25.5), SA 1.2 / 4.8 (5.0), WA 2.0 / 5.1 (7.5): all hold.
  - "VIC, QLD, TAS, NT about equal" holds (VIC 12.5 / 11.9, QLD 9.8 / 10.2, TAS 0.8 / 0.8, NT 0.1 / 0.1).
- SA Arid Lands (326,000 km2 of pasture, 221 km2 of cropping, capacity 41 thousand): holds (326,126; 221; 41,460).
- SA4 406 (17,587 km2 of cropping, 1.7 million): holds (1,695,213).
- Eyre Peninsula (17,221 km2 of cropping, 132 thousand): holds (131,592).
- WA Rangelands (646,000 km2, 937 km2, 241 thousand): holds (646,203; 937; 241,368).
- SA4 511 (356,000 km2, 26,400 km2, 1.5 million): holds (355,565; 26,426; 1,499,707).
- Stranded pasture: NRM 8 units with 71%, SA3 18 units with 72%, SA4 3 units with 51%, "about 20 points": all hold (71.2, 71.5, 51.1).
- Excess land: national 1.96, SA4 3.67, NRM 4.50 million km2: holds (total-excess row).
- Limits: "12 points: NRM 23%, SA4 35%, long term ... against 14 points short term" holds (11.6 and 14.1). "only 7.5% meat and eggs" holds (long preset meategg 0.075).

**`analysis/paper_a/README.md`, "Ameliorative measures" (sentences with drought-proofing or livestock figures)**
- Table row "Livestock output +10% / +20%: 45.5 (+9.7%) / 49.6 (+19.4%) | 17.1 (+9.4%) / 18.6 (+18.8%)": holds.
- Table row "Drought-proofing ... 100-year factor 0.4558 to 0.7279 | n/a | 24.9 (+60%)": holds (+59.7%).
- Reading: "(livestock output +10% gives +9.7% ...)" holds. "drought-proofing and storage matter most (+60%; +48% to +64%)": the +60% holds; I did not check the store figures.
- "Nothing but diet, waste and livestock productivity moves the short term by more than 10% (livestock output +20% gives +19%)": the +19% holds (19.40%). "All yields +10%" gives exactly +10.000%, so it does not exceed 10%, and the sentence holds.

**`papers/A_results/DISCUSSION_MEASURES.md` table A**
- "Drought-proofing farming | n/a | +60%": holds.
- "Livestock output +10% / +20% | +9.7% / +19.4% | +9.4% / +18.8%": holds.
- The reading "the weather allowance is the largest long-term lever" holds only if it covers stores as well. Drought-proofing alone (+60%) is below the two-year grain store (+64%) in the same table.

## Found beyond the brief
1. **DISCUSSION_MEASURES.md table A, row "Cropland +25% taken from pasture", does not hold as worded.** It says "the model holds pasture in excess at the national level (1.96 million km2 unused)". In the evaluator's excess block (Settings rows 84 to 89), the 1.96 million km2 is excess **non-agricultural** land, which is the whole of the total excess. Excess pasture nationally is 0 in the short term. This agrees with the scale README's own diet-binding section: the pasture need of 3.49 million km2 exceeds the pasture held, 3.32 million. The 0% result needs a different explanation.
2. In `results/scale_curve.csv`, the 2011-corrected State rows carry a population of 20,686,860 against the national 22,326,388. The 2011-corrected release's own state populations sum to that figure. Capacities are unaffected; the `units_over_capacity` count uses it. This is noted only: the release is frozen, and the row is the published method.
3. The SA land and the 2025 national zone land differ slightly: +346 km2 non-agricultural and +203 km2 reserve. The effect on capacity is 2 people.

## Commands to rerun (from the repository root)
```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v13
node $S/partA.mjs                    # part A; add "2025-fixed wrong" for the deliberate wrong value
node $S/partB.mjs > $S/partB_out.json   # part B; "node $S/partB.mjs wrong" for the deliberate wrong value
node $S/partC_extra.mjs              # README sentence checks (by-state shares, named units, stranded pasture, excess, population test, 10.8/21.0)
node $S/partC_live20.mjs             # livestock +20% and all yields +10%
node $S/partC_natvec.mjs             # national-yield-vector curve 76, 54, 35, 28
```

## Files read
- qa/briefs/_checker_rules_results_wave.md, qa/briefs/V13_recheck_fixes.md
- web/src/model/evaluator.js, analysis/sensitivity_2025/evaluate.mjs
- web/public/data/{2025-fixed,2011-fixed,2011-corrected}/model.json and regions.json (resilience, Yield and Settings sheets; regions, presets, yields)
- data/sa2/land_2011_method_by_sa2.csv, data/sa2/population_erp.csv
- results/2025-fixed.csv (reference figures), results/<six cells>.csv (state sums only, in part C)
- Part C: analysis/paper_a/long_term_and_measures.mjs, analysis/paper_a/measures.csv, web/scripts/make-scale-curve.mjs, results/scale_curve.csv, analysis/scale_curve_2025/README.md, analysis/paper_a/README.md ("Ameliorative measures" section), papers/A_results/DISCUSSION_MEASURES.md (sections A and the frame)
- Not read, as instructed: qa/reports/V10_*, V12_*, builder briefs B25 and B26.
