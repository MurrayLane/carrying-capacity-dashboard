# V20 report: re-check of the export counts and the corrected cross-method sentences

Checker: independent, blind until part C. No repository file changed.

## Tolerance and the deliberate wrong value
- Counts and names must match exactly; capacities and people counts within 0.5%; shares and ratios within one unit of the last printed digit.
- My own as-traded densities in A(ii) are mine, so they can only confirm the size of the high end, not its last digit.
- Deliberate wrong value: I ran `check.py --sabotage`, which sets wheat to 6,680 kcal/kg (double). The as-traded total went from 265.0 to 389.1 and wheat and rice from 125.5 to 249.6. Both are far outside tolerance, so the comparison can fail.

## Input note
The FBS extract does not have the per-capita elements the brief names (kcal per capita per day, kg per capita per year). It has totals: `Food supply (kcal)` in million kcal and `Food` in 1000 t. Their ratio gives kcal per kg directly, which is the same quantity as the brief's per-capita ratio times 365. Group rows were dropped. Eggs, Milk and Miscellaneous each appear twice, as a group and as an item, and I counted them once. The 2025 population is 27,608,200 (`results/2025-fixed.csv`, zone 1).

## A. Energy count of exports
Before opening anything, my figures were:
- **All foods, FAO balance energy:** 184.9 million. Every exported leaf item, each year's own density, mean of the three yearly counts. Pooling the three years' densities gives 185.5. Using the world's density everywhere gives 212.9.
- **All foods, my own as-traded densities:** 265.0 million. My densities in kcal/kg include wheat 3,340, rice 3,600, barley 3,320, canola seed 5,000, raw sugar 3,800, bovine meat 2,000, milk 640 and oils 8,840. The full list is the `TRADED` table in `check.py`.
- **Wheat and rice:** 86.6 (FAO) and 125.5 (as-traded).
- **Canola density:** pooled 2021-23, Australia gives 692 kcal/kg and the world 2,293. The mean of the yearly world values is 2,259.

Results against the claims:
- **184 (low end): holds.** My 184.9 is 0.49% above 184. The builder's printed value is 183.9.
- **264 (high end): holds.** My 265.0 is within 0.4% of it.
- **87 and 128 (wheat and rice): holds.** FAO 86.6 against 87. As-traded 125.5 against 128; the gap comes from my wheat value of 3,340 against the builder's 3,400, so it is my choice of density rather than an error.
- **Which items decide the gap: holds.** Of my 80.1 million gap between the two ways:
  - wheat 38.4 (the density 2,307 against about 3,400);
  - canola seed 28.1 (Australia's 692 against about 5,000);
  - barley 8.2.
  - Everything else is small.
  - Canola is the item where the low end depends on which FAO density is used. At the world's 2,293 it counts about 15.0 million instead of 4.5.

**My low end against the builder's.** After opening the files, my 184.9 against the builder's 183.9 (+1.0) comes from these items:
- **Leaf items the builder's 25-item list leaves out (+0.77):**
  - Miscellaneous 0.24;
  - spirits ("Beverages, Alcoholic") 0.14;
  - cocoa 0.10;
  - infant food 0.08;
  - potatoes 0.05;
  - soybeans, other oilcrops, coffee, honey, groundnuts, beer, millet, fermented beverages, other meat and spices, together about 0.16.
- **Pulses (+0.55):** the builder uses the Pulses group with its pooled density (3,287). I used beans, peas and other pulses one by one.
- **Sorghum (-0.47):** the builder uses Australia's pooled density, 3,343. For one year Australia has no food use, so I fell back to the world's density for that year.
- **Small density-averaging effects:** oats +0.10, barley +0.10, animal fats -0.12, wheat +0.05, cottonseed +0.05.
- **Requirement:** the builder uses 365.25 days a year where I used 365, which costs the builder about 0.07%.

**The previous check's 194.** It matches the builder's list with canola seed at the world's FAO density instead of Australia's: 183.9 - 4.51 + 14.9 = 194.3. On my item set the same swap gives 195.4. I did not read V16, so this is an inference from the arithmetic.

## B. Proportional count
Domestic use is production + imports - exports - stock variation, over every leaf item, mean 2021-23. Ratios are production over domestic use, weighted by FAO food energy per kg; people are the ratio times 27.6082 million.

| Weighting | With feed | Without feed |
|---|---|---|
| Australia's density first | 2.459 (67.9 M) | 3.668 (101.3 M) |
| World's density first | 2.536 (70.0 M) | 3.751 (103.5 M) |

- **Mass:** 1.662 with feed.
- **Year by year (Australia first):** 2.43 to 2.48 with feed and 3.40 to 3.88 without. The claimed ranges are the spread between the two density bases, not between years.
- **Wheat 2022:** the balance closes with the sign convention used.

Results against the claims:
- **68 to 70 million with feed (2.46 to 2.54): holds.** The builder has 2.461 and 2.538, giving 68.0 and 70.1.
- **101 to 104 million without feed (3.67 to 3.75): holds.** The builder has 3.667 and 3.752, giving 101.2 and 103.6.
- **Mass ratio 1.66: holds.** The builder has 1.662.

## C. Files under test

### Differences in figures
- **`energy_exports.csv` against my figures:**
  - all foods 183.9 against 184.9;
  - as-traded 263.9 against 265.0;
  - wheat and rice 86.5 and 127.6 against 86.6 and 125.5;
  - world-first 211.7 against 212.9.
  - All are explained above (item coverage, group rows, sorghum, my own densities). No figure is outside tolerance.
  - One item reading differs at item level: sorghum, 9.08 against my 8.61.
- **`proportional_count.csv`:** no difference. Every ratio and count matches mine to the printed digit.
- **`analysis/comparators_2025/README.md`, exports passages (lines 47 and 48 and table row 92):** these are consistent with both CSVs.
  - 87 to 128, 184 to 264, wheat 3,400 against 2,308, canola 4,900 against 692, world-first 212, and the six added items at about 6 million (5.82) all check.
  - The proportional figures check: 2.46 to 2.54, 3.67 to 3.75, 68 to 70, 101 to 104, 64.5 to 66.5, 96 to 98, and 1.66 by mass (45.9, printed as 46).

### Sentences
1. **"The ladder's energy step is the midpoint 223.9 of 184 to 264": holds.**
   - (183.9 + 263.9) / 2 = 223.9; `ladder.csv` has 223.9 and the README prints 224.
   - My own midpoint would be 224.9, which still prints as 224 to 225, so this depends on the low end above.
2. **"The export design-choice factor is 4.4 to 6.4": holds.**
   - 183.9 / 41.5 = 4.43 and 263.9 / 41.5 = 6.36.
   - My low end gives 184.9 / 41.5 = 4.46. That is within one unit of 4.4, but it would print as 4.5, so the factor is sensitive to the item coverage above.
3. **"The corrected range (36.3 to 45.8) contains Fearnside's average-year point (41.5) and the meat readings (40 to 41) but not the 1-in-10 point (30.8), and the improved range contains none": holds.**
   - The ranges come from `analysis/sensitivity_2025/monte_carlo_2025-fixed_all_summary.csv`: corrected p5 to p95 is 36.33 to 45.76, improved 46.18 to 60.12.
   - My own evaluator runs on `2025-fixed`: base 41.50 and resilience 10 gives 30.81.
   - The meat readings come from `foran_poldy_balance.csv`: 40 and 41.
   - None of 41.5, 40, 41 or 30.8 lies in 46.2 to 60.1.
4. **"The improved long term (18.5, 15.9 to 19.4) sits on the 1-in-100 point (18.9) and the corrected (15.6) is 17% below": holds.**
   - Improved long term is 18.50 (my run). The Monte Carlo range is 15.87 to 19.42.
   - The corrected run at resilience 100 gives 18.92 (my run).
   - "Sits on" is a reading: 18.5 is 2.2% below 18.9, and 18.9 lies inside the improved long-term range.
   - Corrected long term 15.62 (my run): (18.92 - 15.62) / 18.92 = 17.4%, so 17% holds.
5. **"Land matters least (1.09), with waste (1.17 to 1.33) and the Australian settings (1.29) next": holds.**
   - My runs: doubling cropland out of non-agricultural land gives 45.12 / 41.50 = 1.087.
   - No avoidable waste gives 55.29 / 41.50 = 1.332 (corrected) and 62.92 / 53.64 = 1.173 (improved).
   - Improved over corrected gives 53.64 / 41.50 = 1.293.
   - 1.09 is the smallest factor among the design choices in `design_choices.csv`. The Monte Carlo 1.26 is uncertainty, not a design choice.

## Found but not asked
- **Different bases in the two scripts.** `energy_exports.py` uses a fixed 25-entry list that mixes group rows (Pulses, Vegetable Oils, Fruits, Vegetables, Animal fats, Treenuts, Offals, Fish) with items. `proportional_count.py` uses every leaf item. So the two exports scripts count on different bases.
  - The fixed list leaves out about 0.8 million of exported food energy (Miscellaneous, spirits, cocoa, infant food and others).
  - Its docstring says the 25 items are the exported food items. That is close, but not every one.
  - Counted leaf by leaf, the low end prints as 185 and the factor as 4.5.
- **Year length.** `energy_exports.py` uses 365.25 days; the FAO per-capita convention is 365. The effect is about 0.07%.
- **Second set of ranges.** `results/likely_range_2025-fixed.csv` gives a quick range of 35.9 to 45.8 for the corrected short term, and the improved file gives 45.5 to 59.8 and 15.6 to 19.3. These are the 34-run quick range, not the Monte Carlo range. The README cites the Monte Carlo summary correctly, but a reader comparing with the dashboard's map ranges will see different numbers.
- **Canola world figure.** 2,293 does not appear in the files under test, only in the brief. It matches the pooled 2021-23 world density; the mean of the yearly values is 2,259.

## Commands to rerun (from /home/user/carrying-capacity-dashboard)
```
python3 -I /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v20/check.py
python3 -I /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v20/check.py --sabotage | grep -E 'TOTAL|wheat\+rice'
python3 -I /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v20/diff.py
node /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v20/runs.mjs
```
`diff.py` holds the builder's item values, typed in after part C.

## Files read
- qa/briefs/_checker_rules_results_wave.md
- qa/briefs/V20_exports_recheck.md
- analysis/method_tests_2025/fbs_au_world_2021_23.csv
- results/2025-fixed.csv (nation rows)
- results/2025-improved.csv (nation rows)
- results/2025-resilience.csv and results/2025-land.csv (nation rows; not the needed scenarios)
- results/likely_range_2025-fixed.csv and results/likely_range_2025-improved.csv
- results/README.md (lines 15 and 16)
- analysis/sensitivity_2025/evaluate.mjs
- analysis/sensitivity_2025/monte_carlo_2025-fixed_all_summary.csv and monte_carlo_2025-improved_all_summary.csv (Australia rows)
- web/src/model/evaluator.js (INPUT_ORDER)
- web/public/data/2025-fixed/ and web/public/data/2025-improved/ (model.json and regions.json, through the evaluator)
- Part C:
  - analysis/comparators_2025/energy_exports.py and energy_exports.csv
  - analysis/comparators_2025/proportional_count.py and proportional_count.csv
  - analysis/comparators_2025/README.md (the exports lines)
  - analysis/method_tests_2025/ladder.csv, design_choices.csv, fearnside_failure_curve.csv and foran_poldy_balance.csv
  - analysis/method_tests_2025/README.md (the cross-method and design-choice sections)
