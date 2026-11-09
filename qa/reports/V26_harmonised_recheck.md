# V26 checker report: re-check of the harmonised comparison (decision 35)

**Verdict.** Every figure in A and B reproduces from my own code, with one exception. My first reading of HALF's local-productivity land gave 78.9 million, not 76.0. The script's reading (world cropland per tonne produced) gives 76.0, and so does my code when it uses that basis, so this one is reading-dependent. I re-ran the script with its output sent to my scratch folder, and the result matches the filed `harmonised_comparison.csv` exactly. Two README sentences need qualifying:
* "17 to 343" and "2.7 to 8.3 times" hold only with the pasture-alone rows left out. The CSV has 385.7 million (9.29 times) for build 1 pasture.
* The README says only build 3's oil placeholder was replaced. The script also replaces the tree-nut placeholder and the 15 t/ha garden rate.

No repository file was changed.

## Tolerance and can-fail test (written before comparing)
* **Tolerance:** figures within 0.5%, or equal at the printed precision. Whole-million claims must round to the same whole million. Counts and names must match exactly.
* **Deliberate wrong values:**
  * `partA.py --wrong` raises my Henry and Godden energy reading by 1% to 146.64. It then reports `MISMATCH` against 145.2.
  * In `fp3.py`, keeping the thesis's 1,000 kg/ha oil placeholder gives build 3 cropland-bound 144.3 against 146.2, which is 1.3% out.
  * `summary2.py --wrong` raises Cassidy's harmonised readings by 30%. The summary then becomes 0.09 and 1.41 (6%) instead of 0.14 and 1.35.
* **Real mismatch:** my first HALF reading in part B came out at 78.9 against the claimed 76.0 (see B3). The comparison therefore reports real differences.

## A. Harmonised readings (derived blind)
The food balance from my own code gives 3,525.4 kcal and 120.69 g of protein a person a day. FAO population is 26.203 million (mean of 2021 to 2023). Agricultural land is 31.650 + 331.869 = 363.519 Mha.

1. **Henry and Godden, production as it is, divided by the food-balance supply per person: holds.** Production is 781.65 PJ and 655.55 × 10^10 g (my own rebuild of the recipe). Energy gives 145.18 million (claim 145.2) and protein 148.82 (claim 148.8). Both use 365 days.
2. **Cassidy at 3,525 kcal, no scaling to all cropland: holds.** This build gives 147.4 × 2,700 / 3,525.4 = 112.89 (claim 112.9). V05 gives 5.77 × 25.1 = 144.83, then 110.92 (claim 110.9).
3. **Foran and Poldy on food-balance use per person: holds.**
   * With the three-year population: meat 41.27, fish 12.06, grain with embodied feed grain 126.75. The claims are 41, 12 and 127.
   * With the method script's two-year population (see C4): 41.07, 12.00 and 126.59. These round to the same whole millions.
4. **Footprint build 3 at 2021-23 world yields, thesis pasture rate kept: holds, but only on one reading.**
   * Every Table A2.2 row is mapped to FAOSTAT 2021-23 world yields: the grains, cereals, potatoes, pulses, sugar cane, groundnuts, tree nuts, vegetables for the garden, and oil at build 1's oil-equivalent yield. Cropland-bound is then 146.25 (claim 146.2) and together 287.67 (claim 287.7).
   * Pasture stays at 1.047 ha a person, since the 34 kg/ha rate is not a yield.
   * The figures depend on which placeholders are replaced:

| Placeholders replaced | Cropland-bound | Together |
|---|---|---|
| Oil only (garden 15 t/ha and tree nuts 1,000 kg/ha kept), as the README describes | 141.3 | 286.0 |
| None (oil kept at 1,000 kg/ha) | 144.3 | 287.0 |
| Oil, tree nuts and garden (what the script does) | 146.2 | 287.7 |

5. **HALF unchanged: holds.** 363.519 / 1.318 = 275.81 (claim 275.8).

## B. Local-productivity sensitivity, and the summary
1. **Build 1: holds.**
   * Australia's 2021-23 output is 22.28 Mha of world-average cropland (claim 22.3) and 46.36 Mha of pasture (claim 46.4). Cropland is the QCL group outputs at build 1's world yields; pasture is ruminant protein × 0.0598 ha/kg.
   * Together: 68.64 / 1.059 = 64.82 (claim 64.8). Cropland-bound is 112.55 and pasture 53.91; the README gives 113 and 53.9.
2. **Build 3 together: holds.** Crop output at 2021-23 world yields is 25.31 Mha, with sugar as cane. Red meat at 34 kg/ha gives 81.63 Mha of pasture. Together: 106.94 / 1.2637 = 84.62 (claim 84.6). Counting sugar as raw sugar × 13 instead gives 84.9, which is still within tolerance.
3. **HALF at 76.0: holds on the script's definition only; reading-dependent.**
   * My first reading valued Australia's FBS production at world cropland per tonne of world uses (30.35 Mha). For pasture it used HALF's land per tonne × pasture's share of ruminant land (73.70 Mha). That gives 104.04 Mha and **78.9 million, which does not match 76.0 (3.9% high)**.
   * The gap is almost all in cropland: wheat, barley and oats on the FBS-uses basis against the QCL-production basis.
   * Valuing QCL production at world cropland per tonne of world QCL production, with pasture by feed need, gives 27.7 + 72.4 = 100.1 Mha and 76.0. This is the script's definition.
   * Defensible readings I tried span 73.7 to 79.3. The QCL-production basis is the cleaner one, because area and tonnes come from the same source.
4. **Summary, about 10% (0.14 against 1.35): holds, with a wording note.**
   * Built from my own harmonised values, on the script's rows (every row with both an (a) and a (b), the five methods weighted equally): inputs 0.143 and method 1.352, so 9.6% of the two together.
   * Over the distance itself, the mean absolute ln(a/41.5) is 1.411, and inputs are 10.1% of it.
   * Before opening the files I tried 24 other definitions, which gave 10% to 18%. "About 10%" depends on the row set:
     * Dropping the rows where (a) equals (b) (the three Simpson build 1 rows and the build 3 pasture row) gives 11.6%.
     * Taking Henry and Godden's 45.7 Mha scale-up as its only as-run reading gives about 14% to 17%.

## C. The files under test
I re-ran `harmonised_comparison.py` in memory, writing to my scratch folder. The CSV is identical to the filed one. Every figure in A and B matches the CSV and the README table.

Differences and wording issues:
1. **The spread sentence holds as a direction, but its endpoints leave out rows in the CSV.**
   * "Does not narrow" holds: 343/17 = 20 as run against 343/12 = 29 harmonised. With the pasture rows included it is 22.7 against 32.1.
   * But column (a) and (b) both contain build 1 pasture at 385.7, so 343 is the top only with the pasture-alone readings left out.
   * The "17" depends on choosing their 2050 requirement as the as-run fish reading. `cross_method.csv` already lists fish as "12 to 17" as run.
   * Suggested wording: "crop-bound or crop and pasture together".
2. **"2.7 to 8.3 times the corrected model" leaves out the pasture-alone readings.** Build 1 pasture is 9.29 times and build 3 pasture 7.64. The README table's (d) cell for Simpson (3.36 to 8.27) also leaves out 9.29, though the CSV and the summary statistic include those rows.
3. **Build 3's replacements go further than the README says.** It says only the oil placeholder is replaced and that "the thesis rates that are not dated yields are kept". The script also replaces:
   * the tree-nut placeholder (1,000 kg/ha), by the FAO tree-nut yield;
   * the 15 t/ha garden rate (c11, p. 279), by the FAO vegetable yield of 19,778 kg/ha.

   The docstring's "garden charged at the vegetable yield" says so only obliquely. Keeping both as the README describes gives 141.3, not 146.2 (3.3%).
4. **The Foran and Poldy readings do not use 26.20 million.** The Limits sentence says the per-person bases rest on FAO's 2021-23 head count, 26.20 million. But the Foran and Poldy readings are taken from `foran_poldy_balance.csv`, whose script divides by the mean of 2021 and 2022 only (26.08 million). The effect is under 0.5%, and the whole millions do not change.
5. **"Inputs make 10% of the distance and the methods 90%" is loose.** The statistic is inputs over inputs plus method (9.6%). Because signs offset (for example, Henry and Godden as it is, Foran and Poldy fish, build 3 cropland), 0.14 + 1.35 = 1.49 exceeds the mean distance of 1.41, so the two do not split the distance. "About 10%" holds either way (9.6% or 10.1%).
6. **The docstring's population line is misleading.** It lists "population 27,608,200 (the model's)" under "Equalised". It also says no harmonised method reading uses it, and the README makes the same clarification, so this is wording only.
7. **The rest of the README reading checks out:**
   * the input factors, 0.594 to 1.419;
   * Henry and Godden falling from 211 to 145;
   * Cassidy falling from 190 to 113, with 0.766 on every row;
   * protein rising from 134 to 149, because Gifford's factor implies 134 g a day against 120.7;
   * fish falling from 17 to 12;
   * build 3 rising from 103 to 146;
   * the pasture factor of about 7 (331.87 / 46.4 = 7.2);
   * local readings of 64.8 to 84.6, 53.9 to 77.9 and 76.0;
   * build 2 at 277.7 (331.87 / 1.082 = 306.7 filed, against 363.52 / 1.309 = 277.7).
8. **The boundary holds.** No method is given the model's diet, yields or land classes:
   * The model's land layer appears only in an assertion that the ABS holdings equal FAOSTAT's 363.519 Mha, and they do: 31.650 + 331.869.
   * Build 3's yields are FAOSTAT world yields, not the model's.
   * Cassidy and Henry and Godden use food-balance supply, not the model's diet.
   * The model readings, 41.5 and 53.6, match `results/2025-fixed.csv` (zone 1, short: 41,503,537; population 27,608,200).
9. **The Limits sentence on non-food crops holds.** HALF's output still counts the seed share (15%) of seed cotton, as HALF's own area rule does.

## Found outside the brief
* `foran_poldy_balance.py` divides food use by `pop_now`, the mean of 2021 and 2022. Every other script uses all three years. It is the same issue as C4, but it sits in the method script itself.
* The script computes per-day supply as pooled three-year totals over the summed population. This differs from the mean of yearly ratios by under 0.1%.
* The Henry and Godden harmonised reading uses the TOTAL row as rounded in `henry_godden_summary.csv` (781.6 and 655.6). The effect is under 0.01%.

## Commands to rerun (from /home/user/carrying-capacity-dashboard)
```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v26
python3 -I $S/partA.py            # A; add --wrong for the can-fail test
python3 -I $S/fp3.py              # footprint build 3 variants
python3 -I $S/partB.py            # B: local productivity (build 1, build 3, HALF readings)
python3 -I $S/summary.py          # pre-opening exploration of summary definitions
python3 -I $S/summary2.py --wrong # summary on the script's row set, from my values
python3 -I $S/half_items.py       # HALF cropland per item, two bases
python3 -I $S/rerun_under_test.py # the script under test, CSV written to $S/harmonised_rerun.csv
```

## Files read
* `qa/briefs/_checker_rules_results_wave.md` and `qa/briefs/V26_harmonised_recheck.md`.
* In `analysis/method_tests_2025/`:
  * all of `README.md`. I read the "Harmonised comparison" section only in part C, though an early grep showed two of its lines.
  * the scripts `henry_godden.py`, `simpson_food.py`, `half_index.py`, `cassidy_people_per_hectare.py`, `foran_poldy_balance.py`, and the `extract_*.py` scripts;
  * the CSVs `henry_godden_summary.csv`, `simpson_food.csv`, `half_index.csv`, `cassidy.csv`, `foran_poldy_balance.csv`, `cross_method.csv` and `second_build_values.csv`;
  * the FAOSTAT extracts `fbs_au_world_2021_23.csv`, `fao_world_land_production.csv`, `fao_qcl_countries.csv`, `fao_au_production_1997_2023.csv` and the `half_*.csv` files, plus `wackernagel_1994_food_factors.csv`.
* `results/2025-fixed.csv` (zone 1).
* In part C only: `harmonised_comparison.py`, `harmonised_comparison.csv` and the README section "Harmonised comparison".
* Not read: `qa/reports/B58_*` and `qa/briefs/B58_*`.
