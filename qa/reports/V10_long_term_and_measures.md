# V10 report: the long term by region, its settings, and the measures (results paper sections 7 and 11)

## Tolerance and the deliberate wrong values

**Tolerance.** Counts and names must match exactly. Capacities must be within 0.5%. Shares and ratios must be within one unit of the last printed digit.

**Wrong values fed to my own code, to show it can report a mismatch:**
- **Part A:** I set `INJECT=1`, which raises the 2025 national long-term capacity by 1%. The code then prints 15.78 against the stated 15.6 (out of tolerance) and a regional share of 38.0% against 38.4%.
- **Part C:** I set the meat and egg share to 0.06 instead of 0.05. The code then gives +49.6% short and +14.0% long against the stated +85% and +26%, so it would report a mismatch.

**The 53 regions** are the 52 rows of kind `region` plus NT, which is a `state` row with no regions under it. With only the 52 `region` rows, the counts come out one short (35 and 31), because NT is over capacity in the long term.

**The evaluator reproduces the frozen results exactly.** For 2025-fixed, 2011-fixed and 2025-improved, my national capacities match `results/<release>.csv` to the person for both presets.

## A. Long term by region (results/2011-fixed.csv, results/2025-fixed.csv, long preset)

| Target | Mine | Verdict |
|---|---|---|
| Nation 2011: 15.4 / 22.3 = 0.69 | 15.35 / 22.33 = 0.688 | holds |
| Nation 2025: 15.6 / 27.6 = 0.57 | 15.62 / 27.61 = 0.566 | holds |
| Over capacity 36 then 32; under 17 then 21 | 36 and 17 (2011); 32 and 21 (2025) | holds |
| Population in over-capacity regions 94% both years | 93.8% and 93.8% | holds |
| Sum of regions over national, 2011: 5.1 / 15.4 = 33% | 5.12 / 15.35 = 33.3% | holds |
| Sum of regions over national, 2025: 6.0 / 15.6 = 38% | 6.00 / 15.62 = 38.4% | holds |
| 2025 long-term capacity over population: South Coast WA 8.1, Avon 7.3, Border Rivers - Maranoa - Balonne 7.1, Western NSW 6.1, Border Rivers - Gwydir 4.6, Northern Agricultural 3.9 | 8.07, 7.27, 7.11, 6.10, 4.60, 3.86, the same top six in the same order | holds (one name differs, see below) |

**Name difference.** The release's name for the third region is "Border Rvs Maranoa-Balonne". The paper writes "Border Rivers - Maranoa - Balonne". It is the same zone, so the value holds, but the text does not match exactly.

## B. What each long-term setting is worth (Australia, 2025-fixed; long term 15.62)

**Settings that differ between the presets.** In `regions.json` zone 1 they are:
- resilience: 1 to 100
- meategg: 0.12 to 0.075
- redmeat: 0.578 to 0.5
- activity: 1 to 3
- recycling: 0 to 1
- losses: 0.12 to 0
- organic: 0.07 to 1
- fuel: 2360 to 210
- biofuel: 0.0023 to 1
- fibre: 23 to 11.5
- fibreNat: 0.5 to 1
- fibreWool: 0.12 to 0.9
- timber: 0.8 to 5
- infrastr2: 730 to 500
- nature2: 0.26 to 0.3

`food` and `irrigation` are the same in both presets. Between zones, only irrigation and nature2 differ.

**The stated description of the long term is incomplete.** It leaves out the activity level (3), the three fibre settings, timber and the infrastructure area. Several of those are large levers.

**"Without" values (each setting put back to its short-term value), in millions:**

| Setting put back | Capacity | Change |
|---|---|---|
| resilience | 34.27 | +119% |
| fibreWool | 22.83 | +46% |
| fibreNat | 19.68 | +26% |
| organic | 19.04 | +22% |
| activity | 16.20 | +3.7% |
| biofuel | 16.11 | +3.1% |
| fuel and biofuel together | 16.09 | |
| timber, infrastr2, nature2 | 15.62 | 0 |
| recycling | 15.43 | -1.2% |
| redmeat | 14.72 | -5.8% |
| losses | 12.98 | -17% |
| meategg | 11.65 | -25% |
| meategg and redmeat together | 10.74 | |
| fibre | 11.06 | -29% |
| fuel | 3.71 | -76% |

**Verdicts:**
- **The weather allowance is the largest single lever: holds.** It is the largest change in absolute terms: +18.65 million, against -11.92 million for fuel. It is also the largest rise.
- **Without the low-fuel setting the long term is 3.7 million: holds.** I get 3.71.

## C. Measures, one at a time (Australia, 2025-fixed; against 41.50 and 15.62)

The first four columns give the measure, which evaluator input I changed and my results.

| Measure | How I changed it | Short | Long | Target | Verdict |
|---|---|---|---|---|---|
| Meat and eggs 5% | `meategg` = 0.05 | 76.77 (+85.0%) | 19.64 (+25.7%) | +85%, +26%, about 76 and about 19.7 | holds (19.64 is 0.3% from 19.7) |
| Red meat 30% of meat | `redmeat` = 0.3 | 64.57 (+55.6%) | 18.53 (+18.6%) | +56%, +19% | holds |
| Avoidable waste 6% | `losses` = 0.06 | 48.31 (+16.4%) | 14.35 (-8.2%) | +16%, -8.2% (14.3) | holds (14.35 is 0.35% from 14.3) |
| No avoidable waste | `losses` = 0 | 55.29 (+33.2%) | 15.62 (0.0%) | +33%, 0% | holds |
| Livestock output +10% | Not an evaluator input. I scaled the release's yield vector (`regions.json` `yield`, which the evaluator writes into Yield column F) by 1.1 for the animal-product rows 95 to 103 (sheep meat, wool, dairy milk, cattle, chicken, duck, turkey, eggs, pig) plus 135 and 136 (goat and sheep milk). Yield is the only place the model holds output per hectare. | 45.54 (+9.7%) | 17.10 (+9.4%) | +9.6%, +9.4%, 45.5, 17.1 | holds (short is +9.71% against +9.6%, at the edge of the one-digit tolerance; see E) |
| Field-crop yields +10% | Not an input. I scaled yield rows 4 to 20 (cereals, sugar cane, canola, pulses, oilseeds) by 1.1. I also tried adding cotton (row 94) and adding buckwheat, quinoa, rye, spelt, linseed and sesame. | 41.53 (+0.1%) | 15.65 to 15.67 (+0.2% to +0.3%) | +0.1%, +0.2% to +0.3% | holds |
| Cropland doubled from non-agricultural land | `cropping` x2; `nonAg` reduced by the original cropping area | 45.12 (+8.7%) | 16.98 (+8.7%) | +8.7% both | holds |
| Liquid fuel 156 litres | `fuel` = 156 | 41.53 (+0.1%) | 15.75 (+0.8%) | +0.1%, +0.8% | holds |
| Drought-proofing | Not an input. The 100-year factor for zone 1 is `model.json` resilience!C3:EV3 at the column headed 100 (cell 2:101), and it is **0.4558**, not 0.46. I changed the factor itself: f becomes 1-(1-f)/2, so 0.4558 becomes 0.7279. I also tried setting it to exactly 0.73. The factor is the `C$2` multiplier on every yield row, so changing it is the direct way to model a smaller worst-year loss. | unchanged | 24.95 (+59.7%); with 0.73, 25.02 (+60.2%) | +57% (24.6) | **does not hold**: 24.95 against 24.6 (1.4% apart) and +59.7% against +57%. The cause is in E. |

## D. Grain store equivalence (improved release, long term)

| Target | Mine | Verdict |
|---|---|---|
| 2025-improved long term 18.5 | 18.50 | holds |
| One-year store 27.4 (+48%) | 27.43 (+48.3%), same in the CSV and the evaluator | holds |
| Two-year store 30.4 (+64%) | 30.37 (+64.2%) | holds |
| Same capacity from the weather allowance alone, one-year store: about 16 years | resilience 16 gives 27.44, the nearest return period (bracket 16 to 17) | holds |
| Same, two-year store: about 10 years | resilience 10 gives 30.05 and 9 gives 31.26, so the exact equivalent is about 9.7 years | holds ("about 10") |

## E. Comparison with the files under test

**The script reproduces its committed outputs exactly.** I ran `analysis/paper_a/long_term_and_measures.mjs` into my scratch folder. All five CSVs are byte-identical to the committed ones.

**The CSVs agree with my independent results:**
- **`long_term_regions.csv`:** all 108 rows agree with `results/*.csv` long capacities, within 1 person.
- **`long_term_levers.csv`:** the 2025 Australia "without" values are identical to mine.
- **`store_equivalence.csv`:** its values match my curve (10: 30.05, 15: 27.87, 20: 25.71).
- **`transfers.csv`:** it matches my pool figures (see below).

**Differences found:**

1. **Drought-proofing is not computed as described.** README and DISCUSSION_MEASURES say "the 100-year factor 0.46 to 0.73", 24.6 (+57%). This is the one target that does not hold. The script does not change the factor. It multiplies the yields of rows 4 to 99 by 0.73/0.46 = 1.587:
   ```js
   cap('long', {}, sc([FIELD, HORT, LIVE], 0.73 / 0.46 > 1 ? 0.73 / 0.46 : 1))
   ```
   That has three errors:
   - (a) The release factor is 0.4558. The correct ratio is 0.7279/0.4558 = 1.597, or 0.73/0.4558 = 1.602.
   - (b) Rows 100 to 138 are left unscaled: duck, turkey, eggs, pig, fish, seafood, the derived crop rows, honey, goat and sheep milk, and timber. The real factor multiplies all of them.
   - (c) The `> 1 ?` guard is dead code.

   Changing the factor directly gives 24.95 million (+59.7%), or 25.02 (+60.2%) at exactly 0.73. The paper's figure is understated by about 0.35 million, or 2.3 to 2.8 points.

2. **Livestock output +10% covers fewer rows than described.** The script's `LIVE` is rows 95 to 99 only: sheep meat, wool, dairy milk, cattle and chicken meat. It leaves out pig, duck, turkey, eggs and goat or sheep milk. The description says "meat, wool and milk per hectare", and the same tables advertise "more poultry and pork" for red meat. With all animal products I get +9.7% short (45.54) against the stated +9.6% (45.5); the long term is unchanged at +9.4% (17.10). The figure is within tolerance, but the definition is inconsistent.

   The same narrow row sets (rows 4 to 99) make "All yields +10%, every food yield" leave out rows 100 to 137. That row was not under test.

3. **The pool multiplier "1.6 to 1.8" is short term only.** It is stated without a preset in both README ("The regions as a pool") and DISCUSSION_MEASURES section C. I find national over summed regions of:
   - 1.60 short term in an average year
   - 1.82 short term at a 1-in-10 year
   - 2.60 long term (2025) and 3.00 (2011)

   The same sentence then quotes the long-term trade figure (9.6 million), and the long-term multiplier there is 2.6. The text should either limit the range to the short term or give the long-term multiplier.

4. **Pool figures, recomputed from the 53 regions (2025-fixed, short preset, resilience 1 and 10), all hold:**

   | Figure | Mine | Stated |
   |---|---|---|
   | Average year shortfall / spare | 20.70 / 19.10 (16 regions over) | 20.7 / 19.1 |
   | National surplus, average year | 13.89 | 13.9 |
   | 1-in-10 shortfall / spare | 21.48 / 10.77 | 21.5 / 10.8 |
   | National surplus, 1 in 10 | 3.20 | 3.2 |
   | Trade recovers, short | 41.50 - 26.01 = 15.49 | 15.5 |
   | Trade recovers, long | 15.62 - 6.00 = 9.62 | 9.6 |

5. **Section 7's definition of the long-term settings is incomplete.** Its list (100-year allowance, low-meat diet, no avoidable waste, full recycling, organic, almost no fossil fuel, 30% reserve) leaves out activity level 3, the three fibre settings, timber and infrastructure area.
   - The levers table itself does list them, and the fibre settings are large: without the wool share +46%, without natural fibre +26%, without the fibre cut -29%.
   - "30% reserve" is the national value. The reserve setting (nature2) differs by zone.

6. **"The 2011 table has the same order" holds only for the top two levers.** The weather allowance (+119%) and fuel (-83%) do lead in 2011. Below them the order changes: in 2011 the wool share is worth +2%, against +46% in 2025.

7. **The region name differs, as in A.** The paper writes "Border Rivers - Maranoa - Balonne"; the data says "Border Rvs Maranoa-Balonne".

**Every other number in the two README sections matches my values within tolerance:**
- the national table
- "17 of 2011 become 21"
- the population growth of 24% (27.61 / 22.33 = 1.237)
- the next-ranked regions: Northern Gulf 3.41, South West Qld 3.31, Lachlan 3.15
- every levers-table entry
- every measures row
- the store sentence

**DISCUSSION_MEASURES section A** matches its CSV on every row except drought-proofing (item 1). **Section C** matches, apart from the scope of "1.6 to 1.8" (item 3).

I did not verify:
- the irrigation, horticulture, cropland +25% and recycling rows, beyond checking them against the CSV; the brief did not ask for my own recomputation of these
- the interpretive statements, such as "the model's best diet is near this share" and "pasture and cropland complement each other"

## Found outside the brief
- The `results/*.csv` `over_capacity` flag agrees with capacity < population for all 53 regions.
- In 2025-fixed, the 100-year factor for zone 1 (0.4558) is the same as in 2011-fixed, 2025-improved and 2025-mirror.
- Capacity is linear in the factor: 0.6 gives +31.6% = 0.6/0.4558 - 1.

## Commands to rerun (from /home/user/carrying-capacity-dashboard)
```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v10
node $S/partA.mjs; INJECT=1 node $S/partA.mjs     # A, and the A wrong-value test
node $S/check_base.mjs                              # evaluator against results CSVs
node $S/partB.mjs                                   # B
node $S/partC.mjs 2025-fixed; node $S/partC2.mjs; node $S/partC3.mjs   # C (includes the meategg=0.06 wrong-value test)
node $S/partD.mjs                                   # D
node $S/pool.mjs 2025-fixed                         # pool figures
mkdir -p $S/rerun && node analysis/paper_a/long_term_and_measures.mjs $S/rerun   # script under test, then diff against analysis/paper_a/*.csv
```
`$S/lib.mjs` is the shared loader. `$S/yield_dump.txt` lists the yield rows and the resilience sheet.

## Files read
- qa/briefs/_checker_rules_results_wave.md and qa/briefs/V10_long_term_and_measures.md
- analysis/sensitivity_2025/evaluate.mjs and web/src/model/evaluator.js
- web/public/data/{2011-fixed,2025-fixed,2025-improved,2025-mirror,2025-store-1,2025-store-2}/{model.json,regions.json} and web/public/data/releases.json
- results/2011-fixed.csv, 2025-fixed.csv, 2025-improved.csv, 2025-store-1.csv, 2025-store-2.csv; results/scenarios.csv (grep only); releases/README.md (grep only)
- After the blind parts:
  - analysis/paper_a/long_term_and_measures.mjs
  - long_term_regions.csv, long_term_levers.csv, measures.csv, store_equivalence.csv, transfers.csv
  - analysis/paper_a/README.md, sections "Section 7" and "Ameliorative measures"
  - papers/A_results/DISCUSSION_MEASURES.md, sections up to C
