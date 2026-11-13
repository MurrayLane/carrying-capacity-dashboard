# V31c: second route for cited one-route claims (decision 83)

Checker: blind checker, brief `qa/briefs/V31c_claims.md`, rules `qa/briefs/_checker_rules_results_wave.md`. No git, no subagents, no network. No register edited. Scripts are in `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/V31c/`.

## Tolerance (set before comparing)

* Counts, names, labels, yes/no statuses: exact.
* Model outputs (capacities in people): within 0.5% of my evaluator value.
* Rounded figures as printed (millions to one decimal, thousands, ratios, percentages): within one unit of the last printed digit.

No claim in this set is tier A, so no row needs two agreeing routes for promotion; for every row my route is the second route beside the cited output file.

## Deliberate wrong values (the check can fail)

* `measures_check.mjs 40000000`: fed a reference short-term capacity of 40,000,000; my code printed `DELIBERATE WRONG reference short 40000000 vs mine 41503536.97 MISMATCH`.
* `regions_check.py 193162`: fed Swan's 2011 capacity as 193,162; my code printed `DELIBERATE WRONG Swan cap2011 193162 vs 170101 MISMATCH`.

## My routes

* **R1, measures** (`measures_check.mjs`, plus `measures_check_narrow.mjs` and `measures_check_all.mjs` for the yield-group variants): loads `web/public/data/2025-fixed/` and calls `Evaluator.evaluate` for zone 1 with one setting, land area or yield group changed at a time, both presets. My own groups first (field crops rows 4 to 20, 94, 112 to 115, 122, 125; horticulture rows 21 to 93 and the other fruit, vegetable and nut rows; livestock rows 95 to 103, 135, 136), then the script's narrower groups (field 4 to 20 and 94; horticulture 21 to 93) after deriving.
* **R2, regions** (`regions_check.py`): reads `results/2011-fixed.csv` and `results/2025-fixed.csv` (the 53 regions: kind `region` plus NT), not `movers.csv`.
* **R3, land layer alone**: `analysis/comparison_2025/capacity_by_cause_corrected.csv` (corrected tier), ratio = (capacity_2011 + land_only) / capacity_2011; cross-read against `capacity_by_cause.csv` (published tier).
* **R4, drought years and regional pooling** (`shock_check.mjs`): evaluator on `2025-fixed` and `2011-fixed`, short preset with `resilience` set to 1, 10, 20, 100, and the long preset, for the nation and each of the 53 regions.
* **R5, method tiers**: `results/2011-corrected.csv`, `2011-fixed.csv`, `2011-improved.csv` (and the 2025 trio) for status counts; `results/method_effects.csv` for each module alone on the published base.
* **R6, meat**: FAOSTAT files `analysis/method_tests_2025/fao_au_production_1997_2023.csv` (QCL) and `fbs_au_world_2021_23.csv` (food balance).
* **R7, documents**: `analysis/paper_a/README.md`, `papers/A_results/OUTLINE.md`, `papers/A_results/DISCUSSION_MEASURES.md`, `analysis/land_2011/README.md`, `analysis/paper_a/regional_flips.py`.

## Claims

### A044 (tier B)
Route: R2, status of each capital-city region in both years and presets; README line 22 for what "the coast" means.
My value: over capacity in both years and presets: Hawkesbury - Nepean - Sydney, Port Phillip and Westernport, South East Qld, Adelaide - Mount Lofty Ranges, Swan, South Tasmania (Hobart), NT (Darwin). Murrumbidgee - ACT short term under in 2011 (2.24) and 2025 (2.08); long term over in both. "The coast is mixed" is defined in the README by example: Wet Tropics, Mackay Whitsunday, North Tasmania flip over to under, Corangamite under to over (short term); South Coast WA, Eyre Peninsula, Glenelg Hopkins under in both years. All seven confirmed.
Register value: description. Verdict: **pass with a note**. Status text: "independently verified (V31c); 'the coast is mixed' is checkable only against the README's named examples, which all hold."

### A045 (tier C)
Route: R7, `analysis/paper_a/README.md` line 23 ("**Limits.** Robustness is tested on the 2025 range only; a flip also needs its 2011 status to be robust and the 2011 inputs have no draws."); `regional_flips.py` tests `p5`/`p95` against the 2025 population only; `results/` holds ranges for 2025 releases only.
Verdict: **pass**. Status: "independently verified (V31c)".

### A047 (tier C)
Route: R7, README line 23 ("The test of an artefact is on capacity, not on whether the population change is real."); the script's artefact flag uses only `land_definition_effect_flag` and `boundary_older_2011`, both capacity or area tests.
Verdict: **pass**. Status: "independently verified (V31c)".

### A230 (tier B)
Route: R1, field-crop yields x1.2, short preset.
My value: 41,554,925 (+0.12%) with my wider group; 41,547,232 (+0.11%) with the script's group. Register: 41.5 million (0.1%). Within 0.13% and one unit of the last digit. Verdict: **pass with a note**: on my wider group the figure prints as 41.6; on the script's group (rows 4 to 20 and cotton) it prints 41.5. Status: "independently verified (V31c)".

### A233 (tier B)
Route: R1, horticulture yields x1.1, long preset.
My value: 15,652,030 (+0.18%) wider group; 15,649,029 (+0.17%) script group. Register: 15.6 million (0.2%). Verdict: **pass with a note**: the value sits on the rounding edge (15.65); my wider group prints 15.7, the script's group 15.6. Status: "independently verified (V31c)".

### A242 (tier B)
Route: R1, irrigation 0.02, short. My value: 41,799,149 (+0.71%). Register: 41.8 (0.7%). Verdict: **pass**.

### A245 (tier B)
Route: R1, irrigation 0.05, long. My value: 15,991,281 (+2.36%). Register: 16.0 (2.4%). Verdict: **pass**.

### A250 (tier B)
Route: R1, recycling 1, short. My value: 42,410,429 (+2.19%). Register: 42.4 (2.2%). Verdict: **pass**.

### A251 (tier B)
Route: R1, recycling 1, long (already 1). My value: 15,623,209 (0.00%). Register: 15.6 (0.0%). Verdict: **pass**.

### A252 (tier B)
Route: R1, cropping x1.25, pasture reduced by the same area, short. My value: 41,503,537 (0.00%). Register: 41.5 (0.0%). Verdict: **pass**.

### A253 (tier B)
Route: R1, same, long. My value: 15,623,209 (0.00%). Register: 15.6 (0.0%). Verdict: **pass**.

### A256 (tier B)
Route: R1, meategg 0.075, short. My value: 48,240,815 (+16.23%). Register: 48.2 (16.2%). Verdict: **pass**.

### A257 (tier B)
Route: R1, meategg 0.075, long (already 0.075). My value: 15,623,209 (0.00%). Register: 15.6 (0.0%). Verdict: **pass**.

### A273 (tier B)
Route: R4, national capacity over the sum of the 53 regional capacities.
My values: short average year 41,503,537 / 26,009,770 = 1.5957; 1 in 10: 30,810,607 / 16,895,922 = 1.8236; long 2025: 15,623,209 / 6,003,177 = 2.6025; long 2011: 15,350,146 / 5,118,307 = 2.9991; 1 in 100: 2.17.
Register: 1.60; 1.82; 2.60 (3.00 in 2011). Verdict: **pass with a note**: the register locator's "1/0.63 = 1.59" comes from a rounded share; the exact ratio 1.596 prints as 1.60, as the claim says. Status: "independently verified (V31c)".

### A275 (tier B)
Route: R1. My values, short term: field-crop +10/+20% +0.07/+0.12% (script group +0.06/+0.11), horticulture +0.05%, irrigation +0.71/+2.36%, cropland from pasture 0.00%: range 0 to 2.4%. Livestock +10% +9.73%. Meat and eggs 5% +84.97%. Red meat 30% +55.57%.
Register: 0 to 2.4; 9.7; 85; 56. Verdict: **pass**. (The register note's figures elsewhere, "livestock +9.6%", are not what the model gives: +9.7%.)

### A276 (tier B)
Route: R1, every measure's short-term change.
My value: livestock output +20% gives **+19.40%** (49,556,463), above 10%; all yields +10% gives +10.000001%, level with 10%. Diet (+16%, +85%, +56%) and waste (+16%, +33%) rows also exceed 10%.
Verdict: **fail**. The sentence is false as written: livestock output +20% also moves the short term by more than 10% (+19.4%, not the +19.2% in the register note). Correction: "Nothing but diet, waste and a 20% rise in livestock output moves the short term by more than 10%", or restrict the sentence to the +10% measures (livestock +9.7%, all yields +10.0%, cropland doubled +8.7%).

### A277 (tier C)
Route: R7 plus R1 and R5: every cell of `DISCUSSION_MEASURES.md` table A (lines 10 to 23) against my evaluator values, `measures.csv`, and `results/2025-store-1.csv`, `2025-store-2.csv` against `2025-improved.csv` (long term 27,425,369 and 30,373,031 against 18,496,334: +48.3% and +64.2%; short term unchanged).
All cells agree, including the waste-at-target long-term cell (-8.2%, 14.3; my value 14,349,912, -8.15%) and drought-proofing (+60% against `measures.csv` 59.7%). Table A leaves out three `measures.csv` rows (horticulture +10%, all yields +10%, meat and eggs 7.5%).
Verdict: **pass with a note**. The register note ("every number agrees except the waste-at-target long-term cell") is stale: that cell agrees. Status: "independently verified (V31c); table A restates a subset of measures.csv (three rows not shown)".

### A303 (tier B)
Route: R5, `results/method_effects.csv`, 2025, zone 1, effect alone over published capacity.
My values: long term reserve -5.77%, recycling by stage -9.73%; short term reserve -1.14%, recycling +0.12%. The short-term improvements (Australian loss factors +11.2%, dairy on good land +20.2%) are positive; the two long-term ones are negative. `results/2025-reserve.csv` and `2025-recycling-stage.csv` are on other parents, so not used.
Verdict: **pass with a note**: the base is the published-method release `2025-mirror` (49,389,414 short, 14,146,847 long), not `2025-fixed` as the register's release field reads first. Status: "independently verified (V31c)"; correct `release_or_data` to "2025-mirror (published-method base)".

### A308 (tier B)
Route: R5, sum of `over_capacity` over the 53 regions, 2011 short. My values: published (2011-corrected) 22, corrected (2011-fixed) 23, improved (2011-improved) 22. Register: 22; 23; 22. Verdict: **pass**.

### A311 (tier B)
Route: R5, regions whose 2011 long-term status differs between 2011-fixed and 2011-improved. My value: Western NSW, South East SA (2). Register: the same. Verdict: **pass**.

### A316 (tier B)
Route: R4 for the national factors (1 in 10: 30,810,607 / 41,503,537 = 0.7424; 1 in 20: 26,324,116 / 41,503,537 = 0.6343) and R6 for meat.
Meat production 2021-23 mean: food balance 4.645 Mt (4,373; 4,479; 5,083 kt); QCL 4.656 Mt. Domestic food use (food balance) 2.956 Mt.
My values: 4.645 x 0.7424 = 3.448; x 0.6343 = 2.946 (with QCL 4.656: 3.457 and 2.953). Register: 3.45; 2.95. 3.45 is above 2.96; 2.95 is level with it.
Verdict: **pass with a note**: the register note "Rounds: 3.44 not 3.45" is wrong; it used the factor rounded to 0.74, and the exact factor gives 3.45. The 4.65 is the food balance production mean; `DISCUSSION_MEASURES.md` line 27 prints 4.66 (the QCL mean), so the two documents use different production sources. The claim rests on the untested assumption that meat falls by the national capacity factor. Status: "independently verified (V31c), arithmetic and inputs; assumption untested".

### A323 (tier B)
Route: R1, biofuel 1 with the short-term settings otherwise unchanged; R7 for `DISCUSSION_MEASURES.md` line 43.
My value: 9,717,436 (9.7 million) is the **short-term** capacity with biofuel at 1. The 2025 long term is 15.6 million and already has biofuel at 1 (with biofuel set back to 0.0023 it is 16.1 million). The document says "cuts the short-term figure to 9.7".
Verdict: **fail** (wording). The number is right; the register statement's "long-term figure" is wrong. Correction: "The biofuel share alone (0.0023 to 1, other settings short term) cuts the 2025 short-term figure from 41.5 to 9.7 million."

### A339 (tier C)
Route: R7: `OUTLINE.md` line 45, section 9(a) ("Which status flips of section 3 hold across the 5th to 95th percentile ranges for each zone"); `regional_flips.py` reads `results/ranges_2025-fixed.csv` keyed by zone and setting (120 rows: 60 zones, short and long).
Verdict: **pass**. Status: "independently verified (V31c)".

### A343 (tier B)
Route: R4, North Tasmania 2025 short, resilience 10 and 100.
My values: 156,413 / 156,393 = 1.0001; 124,822 / 156,393 = 0.7981. Register: 1.000; 0.798. Verdict: **pass** (at 1 in 10 capacity exceeds population by 20 people, so "balanced").

### A344 (tier B)
Route: R4, Murrumbidgee - ACT 2025.
My values: average year 1,533,929 / 738,895 = 2.0760; long 303,975 / 738,895 = 0.4114; 1 in 100 460,650 / 738,895 = 0.6234. Register: 2.076; 0.411; 0.623. Verdict: **pass**.

### A049 (tier B)
Route: R2. My values: Swan short capacity 170,101 to 6,495; population 1,699,796 to 2,269,447; over in both. Register: 170 to 6; 1,700 to 2,269 thousand. Verdict: **pass**.

### A050 (tier B)
Route: R2. My values: 66,198 to 46,572; population 4,073,137 to 5,401,609; over in both. Register: 66 to 46. Verdict: **pass with a note**: the figures are truncated, not rounded (46,572 rounds to 47; 5,401,609 to 5,402); within one unit.

### A051 (tier B)
Route: R3. My value: Hawkesbury - Nepean - Sydney (66,198 - 33,698) / 66,198 = 0.491. Register: 0.49. Verdict: **pass with a note**: the register unit "thousand people" is wrong; this is a ratio.

### A052 (tier B)
Route: R3. My value: Swan (170,101 - 167,976) / 170,101 = 0.0125; older 2011 boundary confirmed in `analysis/land_2011/README.md` point 1. Register: 0.01. Verdict: **pass with a note**: unit should be "ratio", not "thousand people".

### A053 (tier B)
Route: R2. My values: 752,498 to 905,523; population 102,847 to 121,808; under in both. Register: 752 to 905. Verdict: **pass with a note** (truncated: 753, 906, 103, 122 if rounded).

### A055 (tier B)
Route: R2. My values: 971,132 to 1,080,065; population 55,850 to 69,727; under in both presets and years. Register: 971 to 1,080. Verdict: **pass with a note** (population truncated: 56 and 70 if rounded).

### A056 (tier B)
Route: R2. My values: 139,165 to 187,593; population 144,582 to 156,393; short term over in 2011, under in 2025. Register: 139 to 187. Verdict: **pass with a note** (truncated: 188 and 145 if rounded).

### A057 (tier B)
Route: R2 and R3. My values: 2,164 to 28,609; population 31,361 to 8,049; over to under (short); land layer alone 6.50 times. Register: 2 to 28. Verdict: **pass with a note** (28,609 rounds to 29).

### A060 (tier B)
Route: R2 and R3. My values: 217,967 to 384,476; land-only ratio 0.758 (inside 0.5 to 2, so no land-definition flag); not among the five older-boundary zones. Register: 218 to 384. Verdict: **pass**.

### A061 (tier B)
Route: R2, short-term capacity change sorted. My values: Central West NSW +464,456, Lachlan +456,182, Namoi +441,053, all under capacity in 2011 and 2025. Register: +464; +456; +441. Verdict: **pass**.

### A062 (tier B)
Route: R3 on the corrected tier.
My values: SA Arid Lands 6.50, Desert Channels 5.70, Southern Gulf 2.58, Northern Gulf 2.23; median of 53 = 0.914 (Fitzroy). Register: 6.5; 5.7; 2.6; 2.2; median 0.91.
Verdict: **pass with a note**. The claim's 0.91 is right for the corrected method. `movers.csv` (and `movers.md` line 23) give 0.90 because the `land_only_ratio` column of `movers.csv` matches the published-method decomposition (`capacity_by_cause.csv`) in all 53 rows, whose median is 0.8996 (NT), while its `cap2011` and `cap2025` columns are corrected-tier values. On the corrected tier five regions differ at the second decimal or more (Goulburn Broken 1.03 against 1.21, Western NSW 0.76 against 0.80, Northern and Yorke 1.10 against 1.09, South East SA 0.95 against 0.84, Corangamite 0.74 against 0.86); none crosses the 0.5 or 2 flag lines, so no flag changes. The register locator's "median 0.90" reads `movers.csv`, the mixed-tier file.

### A064 (tier B)
Route: R3 on both tiers.
My values (corrected tier, the claim's releases 2011-fixed and 2025-fixed): the land layer alone takes Swan from 170,101 to 2,125; population over capacity goes from 10.0 times (2011) to 349 times (2025). The claim's 193,162 to 2,413 and "9 to 356" are the published-method decomposition (`capacity_by_cause.csv`: 193,162, 2,413, 8.80, 356.0). `movers.md` line 22 mixes the two (193,162 to 2,413 with "10 to 349").
Verdict: **fail**. Correction: "Swan: the land layer alone takes capacity from 170,101 to 2,125, and over-capacity goes from 10 to 349 times" (corrected method); or keep 193,162 to 2,413 and 8.8 to 356 and label them the published method.

### A066 (tier B)
Route: R7, `analysis/land_2011/README.md` point 1 (line 20: "Five zones carry older boundaries. Desert Channels (+74,905 km2 ...), SA Murray Darling Basin (+16,332), Alinytjara Wilurara (+11,322), Swan (+9,798 ...) and Northern and Yorke (+267)").
My value: 5 zones, the same five names. Register: 5. Verdict: **pass**. (Aside: the SA overcount sums to 27,921 km2 from these three figures; `movers.md` prints 27,920, a rounding difference.)

### A067 (tier B)
Route: R2. My values: SA Arid Lands population 31,361 (2011-fixed) and 8,049 (2025-fixed). Register: the same. Verdict: **pass**.

### A329 (tier B)
Route: R2, ranks of capacity change and population change.
My values: largest short-term capacity gains Central West NSW, Lachlan, Namoi, Border Rivers - Gwydir, Border Rvs Maranoa-Balonne, Murrumbidgee - ACT (all inland); largest population gains Port Phillip and Westernport +1,402,824, Hawkesbury - Nepean - Sydney +1,328,472, South East Qld +1,000,590, Swan +569,651, Adelaide - Mount Lofty Ranges +263,155 (all coastal capitals, where capacity fell or rose little).
Verdict: **pass with a note**: Murrumbidgee - ACT gains both (+348,336 capacity, +209,387 people). Status: "independently verified (V31c), qualitative".

## Summary

| id | tier | verdict |
|---|---|---|
| A044 | B | pass with a note |
| A045 | C | pass |
| A047 | C | pass |
| A230 | B | pass with a note |
| A233 | B | pass with a note |
| A242 | B | pass |
| A245 | B | pass |
| A250 | B | pass |
| A251 | B | pass |
| A252 | B | pass |
| A253 | B | pass |
| A256 | B | pass |
| A257 | B | pass |
| A273 | B | pass with a note |
| A275 | B | pass |
| A276 | B | **fail** (livestock +20% gives +19.4%) |
| A277 | C | pass with a note |
| A303 | B | pass with a note |
| A308 | B | pass |
| A311 | B | pass |
| A316 | B | pass with a note |
| A323 | B | **fail** (9.7 is the short-term figure, not the long-term) |
| A339 | C | pass |
| A343 | B | pass |
| A344 | B | pass |
| A049 | B | pass |
| A050 | B | pass with a note |
| A051 | B | pass with a note |
| A052 | B | pass with a note |
| A053 | B | pass with a note |
| A055 | B | pass with a note |
| A056 | B | pass with a note |
| A057 | B | pass with a note |
| A060 | B | pass |
| A061 | B | pass |
| A062 | B | pass with a note |
| A064 | B | **fail** (corrected: 170,101 to 2,125; 10 to 349 times) |
| A066 | B | pass |
| A067 | B | pass |
| A329 | B | pass with a note |

37 pass (16 with a note, 21 plain), 3 fail.

## FAOSTAT year finding (A316)

The question arose for A316. In `fbs_au_world_2021_23.csv` the food balance cereals production lags the QCL crops file by one year (food balance 2022 56,335 kt against QCL 2021 55.0 Mt; food balance 2023 59,072 kt against QCL 2022 59.6 Mt and QCL 2023 43.1 Mt), consistent with V30c's wheat finding. Meat does not lag: food balance meat 4,373 / 4,479 / 5,083 kt against QCL 4,421 / 4,489 / 5,058 kt for 2021 / 2022 / 2023, the same year in each. A316 uses meat production and meat food use from the same years and, for 4.65 and 2.96, the same file (food balance), so it does not mix harvest years. Note that `foran_poldy_balance.csv` takes production from QCL (4.66) and food use from the food balance; for meat that is harmless, for its grain row (QCL cereals 2021-23 beside food-balance food use 2021-23) it would pair different harvests.

## Other findings

* `analysis/comparison_2025/movers.csv` mixes tiers: `cap2011`, `cap2025` and the statuses are corrected-tier, `land_only_ratio` is the published-method decomposition (A062, A064). Flags are unaffected; the median and five regional ratios are not.
* Register units for A051 and A052 should be "ratio".
* Register notes that are wrong: A316 ("3.44 not 3.45"), A277 (waste-at-target cell does agree), A276 and A275 notes (livestock +9.6% / +19.2%: the model gives +9.7% / +19.4%), A062 note ("movers.md says 0.91": movers.md says 0.90).

## Register rows touched

None.

## Ids checked

A044, A045, A047, A230, A233, A242, A245, A250, A251, A252, A253, A256, A257, A273, A275, A276, A277, A303, A308, A311, A316, A323, A339, A343, A344, A049, A050, A051, A052, A053, A055, A056, A057, A060, A061, A062, A064, A066, A067, A329.

## Rerun

From `/home/user/carrying-capacity-dashboard`:
```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/V31c
node $S/measures_check.mjs 40000000
node $S/measures_check_narrow.mjs
node $S/measures_check_all.mjs
python3 $S/regions_check.py 193162
node $S/shock_check.mjs
```
The land-only, method-tier, method-effect and FAOSTAT checks were inline Python over the files named under "My routes".
