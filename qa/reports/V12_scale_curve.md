# V12 checker report: the scale curve, national to SA2

## Method and tolerance (set before comparing)

My own code (`curve.mjs`) loads each release (`2025-fixed`, `2011-fixed`) and calls `Evaluator.evaluate(region, inputs)` once per unit and preset. The rule, as the brief states it: every unit is evaluated with the **state zone's region record** (yields and climate zone) and the national preset, except that irrigation and nature2 come from the state zone's preset for that term. The unit supplies its own land and population. Units: the 7 state zones; the 53 NRM units (52 `kind=region` zones and the NT zone, each under its `parent` state); SA4/SA3/SA2 built from `data/sa2/land_2011_method_by_sa2.csv` by code prefix (3/5/9 digits). The state comes from the first digit: 1, 8 and 9 (Jervis Bay) go to NSW-ACT; 2 VIC, 3 QLD, 4 SA, 5 WA, 6 TAS, 7 NT. Population is the ERP of the vintage year (2025 or 2011). Denominators: the national zone on its own land. For the 2011 SA levels I also evaluated the national zone on the summed SA2 land.

Tolerance: counts and names exact; capacities within 0.5%. Shares and rounded figures must be within one unit of the last printed digit (so a share printed as "75%" holds for 74.0 to 76.0).

Can-fail test: `compare.mjs --wrong` feeds the wrong claim "2025 states short = 73%". It reported `DOES NOT HOLD ... claim 73 mine 75.37` (11 mismatches against 10). A first wrong value of 76 was inside the tolerance and passed, so I changed it to 73.

Checks on the method: the national zone gives 41,503,537 short and 15,623,209 long (2025-fixed). The sum of the 7 states with full state presets is 7,677,637 long. Both match `results/2025-fixed.csv`, which is not under test. In my tests capacity does not depend on population, short or long term.

## A. The curve, 2025-fixed (denominator: national zone, 41,503,537 short, 15,623,209 long)

| Level | Units | Short claim / mine | Long claim / mine |
|---|---|---|---|
| States | 7 | 75% / 75.4% **holds** | 70% / 49.1% **does not hold** |
| NRM | 53 | 44% / 44.0% **holds** | 35% / 23.3% **does not hold** |
| SA4 | 89 | 58% / 58.1% **holds** | 49% / 34.9% **does not hold** |
| SA3 | 336 | 44% / 43.9% **holds** | 36% / 24.5% **does not hold** |
| SA2 | 2,450 | 37% / 37.4% **holds** | 30% / 19.8% **does not hold** |

Unit counts 7/53/89/336/2,450 **hold**. The SA2 land sums to the national zone's land within 0.02% (nonAg +346 km2, reserve +203 km2). The SA reference is 41,503,535, equal to the national capacity.

SA2s over capacity: short 2,182 is in the claimed range. Long is 2,299 against a claimed maximum of 2,277, so **does not hold** for the long cell. With 2011 ERP on the 2011-fixed cells I get 2,170 and 2,286, so 2,286 is also outside the range.

## B. The curve, 2011-fixed

Reference: states and NRM use the national zone, 33,307,814 short and 15,350,146 long. The SA levels use the national zone on the 2020-21 SA2 land: **30,685,903 short** (the claimed 30.7 million **holds**) and 14,141,819 long.

| Level | Short claim / mine | Long claim / mine |
|---|---|---|
| States | 77% / 77.1% **holds** | 59% / 43.6% **does not hold** |
| NRM | 44% / 44.2% **holds** | 29% / 19.7% **does not hold** |
| SA4 | 60% / 59.7% **holds** | 44% / 32.1% **does not hold** |
| SA3 | 46% / 46.3% **holds** | 33% / 22.9% **does not hold** |
| SA2 | 40% / 39.8% **holds** | 26% / 18.0% **does not hold** |

Against the 2011 zone reference instead, the SA levels would be 55.0/42.7/36.6% short.

## C. Mechanism claims, 2025-fixed, short term

* SA Arid Lands zone: pasture 326,126 km2, cropping 221 km2, capacity 41,460. **Holds.**
* Eyre Peninsula zone: 131,592. **Holds** (132 thousand).
* SA4 406: cropping 17,587, pasture 341,043, capacity 1,695,213. **Holds** (1.7 million). Its land is about the Arid Lands plus Eyre Peninsula zones (17,442 cropping, 336,744 pasture).
* Rangelands WA zone: 646,203 pasture, 937 cropping, 241,368. **Holds.**
* SA4 511: 355,565 pasture, 26,426 cropping, 1,499,707. **Holds.**
* Stranded pasture (cropping under 2% of pasture). Shares **hold**: NRM 71.2%, SA3 71.6%, SA4 51.1%. Counts **do not hold** under the rule as written:
  * NRM: 9 units, claim 8. The extra unit is Alinytjara Wilurara, with 64 km2 of pasture.
  * SA3: 39 units, claim 18.
  * SA4: 5 units, claim 3 (119 and 121 have 10 and 6 km2 of pasture).
  * The claimed counts appear only with an unstated floor of roughly 850 to 1,225 km2 of pasture, which drops the near-empty urban units.
* By state, NRM against SA4 (state). **All hold**:
  * NSW: 17.6 against 25.3 (25.5).
  * SA: 1.2 against 4.8 (5.0).
  * WA: 2.0 against 5.1 (7.5).

## D. Files under test

**Cause of every long-term difference.** `make-scale-curve.mjs` evaluates every unit with this call:

`ev.evaluate({ ...R, yield: u.yield }, ...)`

Here `R` is the national region, so the evaluator is handed `climateZone` 1 (the nation) with the state's yield vector. The workbook's long-term result depends on that region id; the short-term result for whole states does not.

`climate.mjs` evaluates the 7 states with the state's own id and with the national id. Short term is identical (for example NSW-ACT 10,566,157 both ways). Long term differs: NSW-ACT 2,457,622 against 3,726,084, VIC 1,187,454 against 2,477,023, TAS 62,940 against 43,117. Long sums: 7,677,637 (own id, equal to the release's own state capacities in `results/2025-fixed.csv`) against 10,873,947 (the script's value in `scale_curve.csv`).

So the script's long-term state row does not reproduce the release's own state zones. All the long-term state-basis numbers inherit this, and so do the local-basis ones, which use the same call. Short term matches me exactly at the SA levels (for example SA4 24,120,267, SA2 15,531,155, 2011 SA4 18,317,046). The NRM level differs slightly: 18,274,606 against my 18,263,542 (0.06%), and 2011 14,757,052 against 14,723,989 (0.22%). This is the same region-id effect, small in short term.

**Smaller differences in the script.**
* Jervis Bay (first digit 9) is mapped to zone 1, the nation (`STATE_ZONE 9: 1`), not to NSW-ACT. It has no land in use, so the effect is nil, but it breaks "its state's zone".
* Population is floored at 1 (`Math.max(u.pop, 1)`). This has no effect because capacity does not depend on population.

**`results/scale_curve.csv`** agrees with the README table everywhere, so the README faithfully reports a CSV whose long-term values are wrong as above.

**README table.** The 2011 short and 2025 short columns hold. The 2011 long and 2025 long columns **do not hold**, as in A and B. I did not derive the two local-yield columns independently: they are consistent with the CSV, but their long-term values carry the same region-id problem.

**README "Reading it".**
* "75, 58, 44, 37% short" holds. "Long term falls further (70%, 49%, 36%, 30%)" does not hold: mine is 49, 35, 24, 20.
* "2011: 77, 60, 46, 40" holds.
* "NRM 44 against SA3 44, SA4 58" holds.
* "national 40, states 28, regions 23 million": these are the 2011-corrected local-basis CSV rows (40,450,144; 28,279,790; 23,013,813). I did not derive them independently.
* "the model's capacity does not depend on population at all" holds in my tests. But a later bullet of the same section says capacity "depends on ... its population (infrastructure per person)". The README contradicts itself, and the second claim is wrong by my tests.
* "with the national yield vector 76, 54, 35, 28%" holds (`natvec.mjs`: 75.8, 53.6, 34.8, 27.8 with all-national settings).
* "Each unit's dominant-zone yields, states 109%": not derived.
* "Within-state yield differences about 17 points at SA2 (37 to 54)": consistent with the CSV; 54 not derived independently.

**README "Method and limits".**
* "Sums to the national zone's land" holds within 0.02%.
* "Equal to the national capacity for the 2025 cells" holds.
* "30.7 against 33.3 million" holds.
* "2,147 to 2,277 of 2,450 SA2s are over capacity in every cell" **does not hold**:
  * Across the CSV's six cells the range is 2,136 (2011-improved short local) to 2,293 (2025-mirror long state).
  * Within 2011-fixed alone, local short is 2,143.
  * The quoted range is the 2025-fixed range only.
  * My corrected long-term counts (2,299 for 2025, 2,286 for 2011) are also outside it.
* "National yield vector understates the regional sum, 10.8 against 21.0 million on the 2011 zones" holds (`natvec.mjs` 2011-fixed NRM 10.80 million; the CSV has 21,009,675 local).
* "National unit reached 77 million, not 33": not derived; 33 matches 33,307,814.

**README "Why the NRM regions do so badly".**
* "Rebuilding the NRM regions from whole SA2s gives the same 44%": cannot determine (needs the SA2-to-NRM allocation, which I did not build).
* The by-state figures hold. "Victoria, Queensland, Tasmania and NT are about equal" holds (VIC 12.5/11.9, QLD 9.8/10.2, TAS 0.8/0.8, NT 0.1/0.1).
* The Arid Lands, Eyre, SA4 406, Rangelands and SA4 511 figures hold. One wording error: "the Eyre Peninsula's 17,600 km2 of cropping" does not hold for the zone. The Eyre Peninsula zone has 17,221 km2 (the README itself says 17,200 in its diet section); 17,600 is SA4 406's total cropping (17,587).
* Stranded pasture: the shares hold; the counts (8, 18, 3) do not hold under the stated rule (9, 39, 5), as in C. "SA4 outback units pair about 20 points more" holds (71.2 against 51.1).
* "Excess land: national 1.96 million km2, SA4s 3.67, NRM 4.80": not derived.
* Limits bullet: "the same size in the long term (14 points: NRM 35%, SA4 49%)" **does not hold**. Mine is NRM 23.3%, SA4 34.9%, a gap of 11.6 points.

## Found but not asked

* The state-basis curve is monotone along the ASGS levels in my long-term values too (49, 35, 24, 20), so the shape claim survives, but every long-term level is about 30% lower than published.
* The README diet table lists "States 8" units; the scale curve has 7.
* The `nrm_vs_sa_diagnosis.mjs`, `yield_assignment_test.mjs` and `ideal_split_test.mjs` scripts likely use the same `{ ...R, yield }` call. I did not check them, but any long-term figure they produce should be rechecked.

## Commands to rerun (from the repository root)

```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v12
node $S/curve.mjs $S/units.json            # all units, both releases, both presets (about 6 minutes)
node $S/summarise.mjs $S/units.json        # curve, references, over-capacity, mechanism, stranded, by state
node $S/compare.mjs $S/units.json          # pass/fail against A and B
node $S/compare.mjs $S/units.json --wrong  # can-fail test (feeds 73% for 2025 states short)
node $S/climate.mjs 2025-fixed             # region id effect: state id against national id
node $S/variants.mjs 2025-fixed            # alternative preset rules, long term (none reaches 70%)
node $S/natvec.mjs 2025-fixed; node $S/natvec.mjs 2011-fixed   # national yield vector variant
```

## Files read

`qa/briefs/_checker_rules_results_wave.md`, `qa/briefs/V12_scale_curve.md`, `web/src/model/evaluator.js`, `analysis/sensitivity_2025/evaluate.mjs`, `web/public/data/2025-fixed/{model,regions}.json`, `web/public/data/2011-fixed/{model,regions}.json`, `data/sa2/land_2011_method_by_sa2.csv`, `data/sa2/population_erp.csv`, `results/2025-fixed.csv` (zone rows only, as a check of the evaluator). Read only in part D: `web/scripts/make-scale-curve.mjs`, `results/scale_curve.csv`, `analysis/scale_curve_2025/README.md`.
