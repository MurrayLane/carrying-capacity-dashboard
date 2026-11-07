# V19 report: which route evaluates a diet as the model defines it (defect X083, decision 31)

All runs: improved release (`2025-improved`), Australia (zone 1), short preset, through `web/src/model/evaluator.js`. My code is in the scratch folder (commands at the end). I wrote nothing in the repository.

## Short answer

The gap between the two routes has nothing to do with `meategg`. The left-over 12% share reaches no land cell. The server's write-back loses information in two places in the Base sheet:

* **Beans:** rows 166 to 168 read their group share from row 169.
* **The "Other" group:** row 297's three sub-groups each take the whole group's serves.

With those two places corrected, the server matches the direct route exactly (to 0.001 million) for every guideline diet and for the default. The direct route is the model's own definition of a diet. On it, no meat share beats none: 0% gives 103.6 million and is the highest point.

## 1. How `meategg` and the serves and shares enter the land requirement (workbook formulas)

I checked this in `model/model.xls` (converted to xlsx with soffice) and in the release's `model.json`. The structure is the same in both. The workbook uses `LOOKUP` where the release uses `INDEX/MATCH`, and the workbook's own preset is 0.13 against the release's 0.12.

* **Exactly one cell reads `meategg` (Settings!B10): Diet!C2** = `Settings!B10*1000+Settings!B12*1000`. This is the diet key: the meat share plus activity.
  * Diet!C3:C20 look the key up in the 31 diet columns (E to CS: "Sed 0%" to "Sed 15%" and so on).
  * Diet!B3:B19 copy them, except B10 and B11, which split meat by `redmeat` (Diet!B2 = Settings!B11): `B10 = B2*(C10+C11)`, `B11 = (1-B2)*(C10+C11)`.
* **The Diet sheet reaches the Base sheet in two ways:**
  * (a) The 17 group TOTAL rows' serves a week: Base R54, R89, R106, R126, R143, R165, R174, R179, R195, R210, R229, R233, R260, R265, R282, R297, R321 = Diet!B3 to B19.
  * (b) **Base Z266**, the on/off switch for butter: `=IF(SUM(Diet!C5:C7)=0,0,IF(AA266=0,0,1))`, which reads the three dairy groups' serves straight from the Diet sheet.
  * No other cell in any sheet reads the Diet sheet, `meategg` or `activity`. `Settings!$B$9` in the land rows Settings 33 to 46 is `food`, not `meategg`.
* **How serves and shares make land.**
  * Each unit's food is Y = N × Q × R × U × X: losses, serve size, group serves (R, which copies the group TOTAL row), share within a sub-group (U, from S) and share within the group (X, from V through W).
  * Land is AC = Y / yield.
  * Settings rows 33 to 46 sum AC by land type.
  * The grams eaten are AD = Q × R × X. Nutrients are AF to AK, on the same Q × R × X.
* **The server overwrites (a).** So `meategg` can reach land on the server route only through Z266.
  * At the preset 12%, Z266 stays 1, even for a diet with no dairy.
  * This does no harm to the guideline diets: their butter grams are 0 wherever dairy is 0, so the written share V266 is 0 and W266 = 0.
  * There is no double counting and no left-over 12% share acting anywhere.
  * Proof: passing `meategg` to the server's `eval` gives the same capacities to the last digit (88.00, 96.74, 100.26, 66.86, 58.72, 53.50, 48.18).
  * The only place the left-over share could ever act is an optimised diet that keeps butter while eating no dairy. Then the server would keep butter where the workbook would switch it off.

## 2. Reproduction and the cells where the routes part

| Meat and eggs | Direct (`meategg` only) | Server route (as is) | Server + `meategg` | Corrected write-back |
|---|---|---|---|---|
| 0% | 103.60 | 88.00 | 88.00 | 103.60 |
| 2.5% | 100.39 | 96.74 | 96.74 | 100.39 |
| 5% | 103.28 | 100.26 | 100.26 | 103.28 |
| 7.5% | 66.94 | 66.86 | 66.86 | 66.94 |
| 10% | 58.84 | 58.72 | 58.72 | 58.84 |
| 12% (default) | 53.64 | 53.50 | 53.50 | 53.64 |
| 15% | 48.33 | 48.18 | 48.18 | 48.33 |

All values are million people. These reproduce V17's numbers.

I compared every cell between the routes. Only the units of two groups get different grams, and AC differs only on those rows (and the total, AC322).

**Place 1: beans (legume group, rows 166 to 174).**

* How the workbook holds beans:
  * The black, lima and soy bean rows take their group share from the beans sub-group row: `X166 = X$169` (and the same for 167 and 168).
  * They split it by `U = T/T$169` (S = 1/3 each).
  * The beans' group preference sits on **V169**, a row the server does not treat as a unit, because it has no land cell.
* What the server does:
  * Its grams Q × R × X give each of the three bean rows the **whole** beans amount. At 0%: 1,475 g a week each, against a true total of 1,475.
  * On write-back it adds all three to the group's serves. Legume serves go from 32 to 71 a week.
  * It writes the bean grams into V166 to V168, which nothing reads.
  * It leaves V169 at the workbook's 0.61, while the other legume units get preferences in serves (3.4, 5.7, 0.9, 2.3).
* The result at 0% meat:
  * Beans fall to 254 g.
  * Lentils go from 429 to 2,366 g, chickpeas from 254 to 1,400 g, split peas from 67 to 367 g and tofu from 175 to 964 g.
  * The legume total goes from 2,400 to 5,351 g a week.
  * The legume land cell Settings!C36 goes from 378 to 891 m2 a person a year, and cropland binds.
* This is the whole of the 0% gap and most of the low-meat gap.

**Place 2: the "Other" group (rows 283 to 297).**

* How the workbook holds the group:
  * Beer and wine, coffee, tea and soft drinks, and sugar and honey are three sub-groups.
  * Each is normalised to one on its own (for example `X283 = W283/W$289`).
  * Each takes the **full** group serves R297 at its own serve sizes.
  * The total divides by three: `X297 = SUM(X289,X293,X296)/3`.
* What the server does: it sets R297 to the **sum** of the three sub-groups' serves. Every Other unit's grams therefore triple (beer 984 to 2,952 g a week at 12%).
* This is the whole of the gap at 12% and 15%. Other has 0 serves at 0%.

**Split of the gap** (correcting one place only):

| Meat and eggs | Direct | Server | Beans corrected only | Other corrected only |
|---|---|---|---|---|
| 0% | 103.60 | 88.00 | 103.60 | 88.00 |
| 2.5% | 100.39 | 96.74 | 100.06 | 97.05 |
| 5% | 103.28 | 100.26 | 102.81 | 100.71 |
| 12% | 53.64 | 53.50 | 53.51 | 53.64 |
| 15% | 48.33 | 48.18 | 48.18 | 48.33 |

**Corrected write-back used in the table above** (`serverFixed` in `routes.mjs`):

* Write the beans' serves once, into V169, and leave the bean split to S.
* Set R297 to the mean of the Other sub-groups' serves, not their sum.

## 3. Which route is the model's definition of a diet

**The direct route.**

* **The thesis (chapter 8.3.3 and 8.6.1, pp. 197 to 227):**
  * A diet is chosen by the meat-eggs, red meat and activity parameters.
  * The serve amounts per food group "change depending on user choices in the Meat-eggs, Red meat and Activity levels parameters" (Appendix Table 29, 31 diets from 0 to 15% in steps of 0.5).
  * Serve sizes and the category and sub-category preferences "are constants in the calculations".
* **The workbook does the same:** the Settings inputs pick a Diet column, and the Base shares are fixed values.

So a guideline diet is exactly what you get by setting `meategg` (and `redmeat` and `activity`). The server's grams route is meant as a neutral way to express the same diet in grams, and it is not neutral.

**What the server would have to do to agree.** Setting `meategg` to the diet's share when writing back does not help: the results are identical, because the share reaches nothing the server has not overwritten. Instead:

1. Treat the beans sub-group as one unit. Write its serves to V169, and either leave S166:S168 alone or write the within-beans split there. Count beans once in the group's serves, and take bean grams as Q × R × U × X, or from row 169's AD.
2. Write R297 as the mean of the three Other sub-groups' serves.
   * This is exact for any diet whose three sub-groups have equal serves, which every workbook diet has.
   * The workbook cannot represent an arbitrary diet whose sub-groups are out of that proportion.
   * The optimiser holds Other at the default, so this limit does not bite at present.
3. For completeness, set `meategg` to the diet's share, or set Z266 from the written dairy serves, so that butter follows the written diet's dairy as the workbook does.

With steps 1 and 2, the server reproduces the direct route to 0.001 million at all seven shares.

## 4. Consequences: every figure that depends on the server route

**`analysis/comparators_2025/diet_land.csv` and the 2b table in `comparators_2025/README.md`.**

* Only the people-fed column goes through the server's `eval`.
* The land-per-person columns come from the family grams times the unit coefficients. They already equal the direct route: total 0.271, 0.282, 2.581, 4.881, 5.630, 6.229 and 6.975 ha against the CSV's 0.27, 0.28, 2.58, 4.88, 5.63, 6.23 and 6.98. They stand.
* People fed (million), as is against the direct route:

| Row | As is | Direct route |
|---|---|---|
| Default diet | 53.5 | 53.6 |
| 15% | 48.2 | 48.3 |
| 12% | 53.5 | 53.6 |
| 10% | 58.7 | 58.8 |
| 7.5% | 66.9 | 66.9 (unchanged) |
| 5% | 100.3 | 103.3 |
| 2.5% | 96.7 | 100.4 |
| 0% | 88.0 | 103.6 |

* **Optimised A, B, C.** The CSV holds the stale 84.1, 133.1 and 248.7 (decision 30).
  * The repository chain, which I reran into scratch, gives 85.10, 188.95 and 342.50 on the server.
  * The corrected write-back gives **85.46 (+0.4%), 197.11 (+4.3%) and 383.75 (+12.0%)** for the same diets.
  * The optimiser holds legumes and Other at the default diet (`FIXED` in `optimise.py`), so both faults are inside every optimised diet.
  * Re-optimising on a corrected server could move these further. I did not do that.
  * The optimiser's "default 53.64" denominator is already the direct value, so its gains mix the two routes.

**The "a little meat beats none" reading.** It appears in:
* `comparators_2025/README.md` 2b ("5% feeds 100 million, none 88")
* claim B216
* `papers/B_methods/SECTION7_DRAFT.md` line 38 ("a peak at an intermediate share because a little pasture-fed meat uses land crops cannot")

On the direct route (improved, short, 0 to 15% in steps of 0.5):

* Capacity is 103.60 at 0% and dips to 100.39 at 2.5%.
* It recovers to 103.42 at 4 to 4.5% and is 103.28 at 5%.
* It falls off a cliff after 5.5% (101.1, then 89.7 at 6% and 66.9 at 7.5%).
* So capacity is still not monotone (the dip at 2.5%), but **no meat share beats none**. The maximum is 0%, and 4 to 5% comes within 0.2%. The reading should go.
* The server curve rises from 88.0 at 0% to 100.3 at 5%. That rise is the beans fault: the server inflates legumes most when meat and dairy are lowest.
* `analysis/scale_curve_2025/diet_scale.csv` and `diet_templates/best_diet.mjs` use the direct route on other releases. On the fixed release, 2.5% (118.0) does beat 0% (112.4). So the sentence would hold only for that release, not for the improved table it sits beside.

**Design-choice figures.**

* `analysis/method_tests_2025/design_choices.csv`, Diet row: 48.2, 100.3, 2.08 becomes **48.3, 103.3, 2.14**.
* `method_tests_2025/README.md` line 274: "2.1" holds either way.
* The Diet (optimised) row's default 53.5 becomes 53.6. Its C value is under decision 30, and on a corrected server it would be about 383.8 (factor 7.2) before re-optimisation.

**Claims register.**

| Claim | As is | Direct route |
|---|---|---|
| B179 | 100.3 | 103.3 |
| B181 | 2.08 | 2.14 |
| B206 | 0% 88.0 | 103.6; land 0.27 stands |
| B207 | 2.5% 96.7 | 100.4 |
| B208 | 5% 100.3 | 103.3 |
| B216 | 5% beats none | withdraw |

The same figures appear in `qa/reports/pack_2026-11-07.md`.

**Not dependent on the server route:**

* **`analysis/scale_curve_2025/diet_binding_test.mjs`, `diet_scale_test.mjs` and `diet_templates/best_diet.mjs`:** they set `meategg` directly.
* **`analysis/scale_curve_2025/food_land_by_category.py`:** it uses only `defaultgrams` times the unit coefficients, which is route-neutral (as with the land columns).
* **`papers/A_results/DISCUSSION_MEASURES.md` "+85%" at 5%:** this matches the fixed release's direct route (76.8 / 41.5).

**All of `analysis/nutrition_lp_2025/` results** (`variants.csv`, `variants_family95.csv`, `staples*.csv`, and the README tables A 85.1 and B 189) are server evaluations. They carry the same faults. I measured the size only for zone 1, short term, with micronutrients (above).

## Recommendation for decision 31

Adopt the direct route as the definition: a guideline diet is the meat-and-egg, red-meat and activity setting, as the thesis and the workbook define it. Correct the server's write-back rather than add `meategg` to it, since `meategg` has no effect there. The correction is to write the beans sub-group once into V169 and to give the Other group the mean, not the sum, of its sub-groups' serves. With it, the server reproduces the direct route exactly, and it stays usable for the optimised diets. Then:

* regenerate `diet_land.csv` (guideline rows 103.6, 100.4, 103.3, 66.9, 58.8, 53.6, 48.3; land columns unchanged) and the design-choice Diet row (48.3, 103.3, 2.14);
* withdraw "a little meat beats none" from comparators 2b, claim B216 and the Paper B section 7 draft, for the improved release;
* run decision 30's re-optimisation on the corrected server, not the current one, because the corrected server alone moves C from 342.5 to about 383.8.

The cost is small, a few lines in `server.mjs` plus the reruns. My confidence is high: the corrected write-back matches the direct route at every share tested.

## Commands to rerun (repository root)

```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v19
node $S/routes.mjs                                  # direct, server, server+meategg at 0..15%; cell diffs to $S/routes.json
MEATS=0.075 FIXCHECK=1 GRID=1 OUT=$S/routes075.json node $S/routes.mjs   # corrected write-back check and the 0.5% grid
MEATS=0.12 OUT=$S/routes012.json node $S/split.mjs    # which fault makes which part of the gap
O=analysis/nutrition_lp_2025/optimise.py              # chain into $S/lp as run_variants.sh does (fixcap3, famcap3, free, micro)
MEATS=0.12 OUT=$S/routes012.json node $S/opt_fix.mjs  # A, B, C on the server and on the corrected write-back
```

## Files read

* **The brief, and earlier work:** `qa/briefs/V19_diet_route.md`, `qa/reports/V17_design_choices.md`, `qa/DECISIONS.md` (rows 30 and 31), `qa/defects.csv` (X083).
* **Model and code:** `analysis/nutrition_lp_2025/server.mjs`, `optimise.py` (header and FIXED), `run_variants.sh`, README (grep), `web/src/model/evaluator.js`, `web/public/data/2025-improved/model.json` (Diet and Base sheets, Settings formulas) and `regions.json`.
* **Workbook and thesis:** `model/model.xls` (converted to xlsx in scratch: Diet, Base, Settings formulas); thesis `/home/user/carrying-capacity-models/Papers and manuscripts/Lane-2014-PhD-thesis-QUT-eprint-67485.pdf` (chapter 8.3.3, 8.6.1).
* **Figures that may depend on the route:** `analysis/comparators_2025/diet_land.py`, `diet_land.csv` and README section 2b; `analysis/scale_curve_2025/diet_binding_test.mjs` (head), `diet_scale_test.mjs` (grep), `food_land_by_category.py` (grep), `diet_scale.csv`; `analysis/diet_templates/README.md` (grep) and `best_diet.mjs` (grep); `analysis/method_tests_2025/design_choices.csv` and README (grep); `papers/A_results/DISCUSSION_MEASURES.md` (lines 10 to 20); `papers/B_methods/SECTION7_DRAFT.md` (lines 36 to 40); `qa/claims_register.csv` and `qa/reports/pack_2026-11-07.md` (grep).
