# V31e: second route for cited one-route claims (decision 83)

Blind checker report. Rules: `qa/briefs/_checker_rules_results_wave.md`, as amended by the brief (report here, not in the scratch folder). No register edited. My code: `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/V31e/` (`cap.mjs`, `land.mjs`, `req.mjs`, `res.mjs`, `fao_land.py`, `compare.py`).

## Tolerance

- Counts, labels, years: exact.
- Model outputs: within 0.5%.
- Rounded figures: within one unit of the last printed digit (so "37.0" passes for 36.9 to 37.1; "9" passes for 8 to 10). Where a figure passes only by that widening and would not round to the printed figure, I mark it "pass with a note".

## The check can fail (deliberate wrong values)

`python3 -I compare.py --wrong` fed my own 2025-fixed values against wrong stated figures: 37.033 against "37.5" gives FAIL (difference 0.467, tolerance 0.1); 30.811 against "31.8" gives FAIL (0.989 against 0.1). The real run then failed three items on its own (B225 improved, B199 both upper bounds), so the comparator does report mismatches.

## My route (common to the R1, R2, R3 claims)

`cap.mjs` loads `web/public/data/<release>/model.json` and `regions.json`, runs `Evaluator.evaluate` for Australia (region 1) on the short-term preset, and varies one thing: resilience 1, 5, 10, 20, 50, 100 (R1); cropping doubled with the added area taken from non-agricultural land (R2); avoidable waste 0 (R3). Anchor: my resilience-1 values equal the committed `results/<release>.csv` Australia short rows to the person (2025-fixed 41,503,537; 2025-improved 53,643,731; 2025-mirror 49,389,414; 2011-fixed 33,307,814). Only after deriving my values did I open `analysis/comparators_2025/rerun.csv` (route 1); every cell I needed agrees with mine to two decimals.

My values (million people, Australia, short term):

| release | R1 1 | R1 5 | R1 10 | R1 20 | R1 50 | R1 100 | R2 average | R3 average |
|---|---|---|---|---|---|---|---|---|
| 2025-fixed | 41.504 | 37.033 | 30.811 | 26.324 | 22.925 | 18.918 | 45.117 | 55.285 |
| 2025-improved | 53.644 | 47.920 | 39.931 | 34.277 | 29.877 | 24.681 | 58.314 | 62.919 |
| 2025-mirror | 49.389 | 44.070 | 36.665 | 31.326 | 27.280 | 22.513 | 53.690 | 66.009 |
| 2011-fixed | 33.308 | 28.844 | 24.685 | 19.956 | 18.398 | 15.182 | 35.891 | 44.421 |

## One block per claim

**B069** (tier B). Route: `req.mjs` reads the model's land-requirement rows (Settings rows 91 to 107) for 2025-improved, Australia, short term; "Food Total" is 62,259 m2 a person, cropland used at capacity 160,778 km2 over 53.64 million. HALF denominator from `analysis/method_tests_2025/half_index.csv` (Australia 2021-23, 1.318 ha a person). Mine: total 6.23 ha, cropland 0.30, pasture 5.93 (total less cropland), ratio 6.226 / 1.318 = 4.72. Register: 5.93; 0.3; 4.7. Verdict: **pass with a note**. My cropland figure includes the small biofuel and fibre cropland, so the pasture/cropland split is checked to the printed digit only; `diet_land.csv` (opened last) gives 0.3, 5.93, 6.23 and 53.6. The ratio 4.7 depends on the HALF value after fix X036 (1.371 before gave 4.5). Status: "independently verified (V31e; split to the printed digit)".

**B095** (tier B). Route: `cap.mjs`, 2025-fixed, resilience 5. Mine 37.033. Register 37.0. **Pass**. Status: "independently verified (V31e)".

**B097** (tier B). Route: as above, resilience 20. Mine 26.324. Register 26.3. **Pass**. Status: "independently verified (V31e)".

**B103** (tier B). Route: 2025-improved, resilience 100. Mine 24.681. Register 24.7. **Pass**. Status: "independently verified (V31e)".

**B104** (tier B). Route: 2025-mirror, resilience 10. Mine 36.665. Register 36.7. **Pass**. Status: "independently verified (V31e)".

**B105** (tier B). Route: 2025-mirror, resilience 100. Mine 22.513. Register 22.5. **Pass**. Status: "independently verified (V31e)".

**B106** (tier B). Route: 2025-fixed, cropping 2 x 316,499 km2, non-agricultural 2,063,387 less 316,499. Mine 45.117. Register 45.1. **Pass**. Status: "independently verified (V31e)".

**B107** (tier B). Route: as B106 on 2025-improved. Mine 58.314. Register 58.3. **Pass**. (The 49.7 found elsewhere for this case is wrong; see B225.) Status: "independently verified (V31e)".

**B109** (tier B). Route: my R2 over my R1 setting 1: 45.117 / 41.504 = +8.71% (2025-fixed); 58.314 / 53.644 = +8.71% (2025-improved). Mine 8.7%. Register 9. **Pass with a note**: 8.7 rounds to 9; "45 to 58" also holds. The cause clause ("bound by pasture-fed meat and dairy") is consistent with my run (2025-improved pasture is the binding land: 110,984 km2 short, cropland 155,721 km2 in excess) but is a reading, not a number. Status: "independently verified (V31e)".

**B123** (tier B). Route: 2011-fixed, resilience 1. Mine 33.308. Register 33.3. **Pass**. Status: "independently verified (V31e)".

**B198** (tier B). Route: my R1 settings 1 and 10 and R3 average year, 2025-fixed and 2025-improved. Mine: average year 41.5 to 53.6; no waste 55.3 to 62.9; 10-year 30.8 and 39.9. Register: 41 to 54; 55 to 63; 31 and 40. **Pass with a note**: 41.504 is written "41", which is within one unit but rounds to 42. Recommended correction: "41.5 to 53.6" (or "42 to 54"). Status: "independently verified (V31e; lower bound truncated)".

**B199** (tier B). Route: my R1 settings 50 and 100, 2025-fixed and 2025-improved. Mine: 22.9 to 29.9 at 50 years; 18.9 to 24.7 at 100. Register: 22 to 25; 19 to 21. **Fail**. Right values: **23 to 30 million at 50 years and 19 to 25 at 100** (2025-fixed to 2025-improved). No other cell reproduces "22 to 25" and "19 to 21" (2011-fixed 18.4 and 15.2; 2025-mirror 27.3 and 22.5; route 1 for 2011-corrected and 2011-improved: 22.34 / 23.18 and 18.44 / 19.14). Status: "fails V31e: 23 to 30 and 19 to 25".

**B200** (tier B). Route: my R2 average year, both 2025 releases. Mine 45.1 to 58.3. Register 45 to 58. **Pass**. The "60 to 70" reading of Gifford is not checked here (it is not the value). Status: "independently verified (V31e; model range only)".

**B204** (tier B). Route: my 2025-improved short-term capacity 53.644 million; model cropping plus pasture 316,499 + 3,318,689 km2 = 363.52 Mha, which equals FAOSTAT 2021 cropland plus pasture 31.65 + 331.87 Mha (my `fao_land.py`). Register 54; 363. **Pass with a note**: the unit column says "million people" for 363, which is Mha; the locator's "(53.5)" is stale, `diet_land.csv` now prints 53.6. The US figures (433 Mha, 402 million) are not in any value field and were not checked. Status: "independently verified (V31e; Australian figures only; unit of 363 is Mha)".

**B225** (tier B). Route: my R2 average year. Mine 45.117 (corrected), 58.314 (improved). Register 45.1; 49.7. **Fail** on the improved figure. Right value: **58.3** (route 1, `rerun.csv`, agrees: 58.31). 49.7 is no cell of the re-run (2011-improved R2 is 44.92; 2025-mirror R2 is 53.69). Status: "fails V31e: improved is 58.3, not 49.7".

**B226** (tier B). Route: my R1 settings 1 and 10 and R3 average year. Mine 41.504, 53.644, 55.285, 62.919, 30.811, 39.931. Register 41.5; 53.6; 55; 63; 30.8; 39.9. **Pass**. Status: "independently verified (V31e)".

**B228** (tier B). Route: `req.mjs` for 2025-improved with meat and eggs at 12% (default) and 0%. Mine: Food Total 6.226 ha and 0.271 ha a person. Register 6.2; 0.27. **Pass with a note**: the US 1.08 and 0.13 are not in the value field and were not checked (1.08 equals 433 / 402 of B204). Status: "independently verified (V31e; Australian figures only)".

**B245** (tier B). Route: 2025-fixed, resilience 10. Mine 30.811. Register 30.8. **Pass**. The Jones "30 to 35" was not opened. Status: "independently verified (V31e; model value only)".

## Summary table

| id | tier | verdict |
|---|---|---|
| B069 | B | pass with a note |
| B095 | B | pass |
| B097 | B | pass |
| B103 | B | pass |
| B104 | B | pass |
| B105 | B | pass |
| B106 | B | pass |
| B107 | B | pass |
| B109 | B | pass with a note |
| B123 | B | pass |
| B198 | B | pass with a note |
| B199 | B | **fail**: 23 to 30 (50 years), 19 to 25 (100 years) |
| B200 | B | pass |
| B204 | B | pass with a note |
| B225 | B | **fail**: improved 58.3, not 49.7 |
| B226 | B | pass |
| B228 | B | pass with a note |
| B245 | B | pass |
| A321 (flagged, outside the 18) | B | **fail**: SA 0.35, WA 0.47 |
| B045 (flagged, outside the 18) | B | **fail on the label**: 17.38 and 445.4 are FAOSTAT 1991, not 1991-92 |

No tier A rows are in the list, so no two-route agreement was required; my route is the second route for each row.

## The two flagged items

These two ids are not in the brief's list of 18; I checked them because the caller named them.

**A321.** Route: `res.mjs` evaluates the nation and each state at resilience 100 and 1 on release 2025-resilience (and, for contrast, 2011-fixed); the capacity ratio equals the 100-year factor. Mine, 2025-resilience: Australia 0.4558, NSW-ACT 0.3003, Victoria 0.2176, Queensland 0.3470, South Australia 0.3533, Western Australia 0.4708, Tasmania 0.6654. On 2011 data: South Australia 0.3588, Western Australia 0.4914, Tasmania 0.6694, the others the same. `analysis/resilience_2025/tables.csv` column "100" (opened after) agrees: "thesis (archive data)" rows give 0.358753, 0.491409, 0.669346; "data: ABS to 2021-22" and "data: ABS to 2024-25" rows give 0.353322, 0.470817, 0.665388. The register cites release 2025-resilience but quotes the thesis-archive row for SA (0.36) and WA (0.49). **Fail.** Right values under 2025-resilience: **South Australia 0.35, Western Australia 0.47**; Australia 0.46, NSW 0.30, Victoria 0.22, Queensland 0.35 and Tasmania 0.67 (0.6654) hold. The sentence's comparisons still hold (0.456 is above 0.353 and below 0.471). Correction: change 0.36 to 0.35 and 0.49 to 0.47, and point the locator at the "data: ABS to 2024-25" rows. Status: "fails V31e: SA 0.35, WA 0.47 under 2025-resilience".

**B045.** Route: `fao_land.py` reads the FAOSTAT land-use bulk file at `/tmp/claude-0/fao/Inputs_LandUse_E_All_Data_(Normalized).zip`, whose sha256 39b739fb...a6ca3f matches `qa/fao_bulk_hashes.csv`. Australia, element Area, 1000 ha:

| item | 1991 | 1992 | mean 1991-92 | 2021 | 2022 | 2023 | mean 2021-23 |
|---|---|---|---|---|---|---|---|
| Cropland | 17,382 | 16,404 | 16,893 | 31,650 | 31,650 (I) | 31,650 (I) | 31,650 |
| Permanent meadows and pastures | 445,400 | 449,600 | 447,500 | 331,869 | 331,869 (I) | 331,869 (I) | 331,869 |

The values 31.65 and 331.87 **pass**. The 1991-92 figures 17.38 and 445.4 are exactly the calendar-1991 rows; a 1991-92 mean would be 16.89 and 447.5. **Fail on the label.** Correction: write "17.38 and 445.4 Mha in 1991 (FAOSTAT)", or, if a 1991-92 average is meant, 16.89 and 447.5 Mha. Note also that 2022 and 2023 are imputed copies of 2021 (flag I), so "2021-23" is the 2021 survey figure. Status: "values verified (V31e); 1991-92 label wrong: the figures are FAOSTAT 1991".

## Thesis Table 16 against the 2014 article

- Thesis (`carrying-capacity-models/Papers and manuscripts/Lane-2014-PhD-thesis-QUT-eprint-67485.pdf`, sha256 f19e1380...a1ef, matches L020), Table 16, PDF page 280: "Short-term large-scale 40,439,187 | 10,033,151 | 5,975,944 | ...". The thesis text gives no other exact national figure (the Figure 50 axis carries tick labels only).
- 2014 article, accepted manuscript QUT eprint 65503 (local copy `scratchpad/papers/ecolmodel2014.pdf`, sha256 9c8318af...f297; not on the literature register), manuscript lines 573 to 575, PDF page 25: "Australia at the national scale has a population carrying capacity of 40,450,144 people with the land required for food being 48.9%, ...". This is the author's manuscript, not the version of record.
- 2015 article (QUT eprint 75171, Table 2) prints 40,439,187, the same as the thesis.
- The committed results match each one to the person: `results/2011-thesis.csv` 40,439,187; `results/2011.csv` and `results/2011-corrected.csv` 40,450,144.

**Finding.** The two differ, by 10,957 people (0.027%). They come from two versions of the model: the thesis and the 2015 paper use the thesis build (`2011-thesis`); the 2014 article uses the final online build (`2011`, reproduced by `2011-corrected`). The register should carry the figure of the document or release it cites: **40,450,144 when the source is the 2014 article (L012) or the published-method release 2011-corrected; 40,439,187 when the source is the thesis (L020) or the 2015 article (L013)**. At one decimal both are 40.4 and at whole millions both are 40, so only two-decimal or exact figures are affected. One row looks inconsistent: A019 carries 40.45 (correct for 2011-corrected and L012) but names L020, the thesis, as method source; the thesis prints 40,439,187, which is 40.44. Recommend A019 cite L012 for the figure, or keep L020 and say the thesis prints 40.44. B229 ("40", locator 40,439,187 from 2011-thesis, sources L012;L013;L014) holds at whole millions either way. I did not edit either row.

## FAOSTAT year finding

None of the 18 claims puts a food-balance year beside a crops year: the R1 to R3 claims are model runs, and the diet-land claims use the model's own coefficients. B045 uses the land-use domain only, and its issue is a calendar-year label, not a one-year booking shift. The HALF denominator of B069 (1.318, period 2021-23) is built from food balances; I did not test its harvest year, and a shift there would move the ratio, not the model figures.

## Register rows touched and ids checked

Register rows touched: none. Ids checked: B069, B095, B097, B103, B104, B105, B106, B107, B109, B123, B198, B199, B200, B204, B225, B226, B228, B245; and, at the caller's request, A321, B045, and the A019 / B229 Australian figure.

## Rerun

From the repository root:

```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/V31e
node $S/cap.mjs
node $S/req.mjs 2025-improved; node $S/req.mjs 2025-improved 0
node $S/res.mjs 2025-resilience 2011-fixed
python3 -I $S/fao_land.py "/tmp/claude-0/fao/Inputs_LandUse_E_All_Data_(Normalized).zip"
python3 -I $S/compare.py --wrong; python3 -I $S/compare.py
```

Files read: `web/src/model/evaluator.js`; `web/public/data/{2025-fixed,2025-improved,2025-mirror,2011-fixed,2025-resilience}/`; `results/{2025-fixed,2025-improved,2025-mirror,2011-fixed,2011,2011-thesis,2011-corrected}.csv` (Australia rows); `analysis/method_tests_2025/half_index.csv`; `analysis/resilience_2025/tables.csv`; `qa/fao_bulk_hashes.csv`; the thesis, 2014 and 2015 PDFs above; and, last, `analysis/comparators_2025/rerun.csv`, `rerun.mjs`, `diet_land.csv` and the header of `diet_land.py`.
