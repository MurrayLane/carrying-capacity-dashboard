# V37: blind check of B111, the decomposition in every order

Checker: independent, blind. Brief: `qa/briefs/V37_check_B111.md`. Rules: `qa/briefs/_checker_rules_results_wave.md`. This report is the only repository file I wrote. No git, no subagents, no network. `npm run results` and `build-data.mjs` were not run.

My scripts and outputs are in the scratch folder `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v37/`:
* `shap.mjs`: the value function over all 512 layer subsets, plus forward, reverse and the exact enumeration of the 9! orderings.
* `game8.py`: the eight-layer game, with land and livestock as one player.
* `compare.py`: the cell-by-cell comparison.
* `livestock_zone_2011pasture.py` and the `ls_2025/` and `ls_2011/` folders: the livestock rows.

**Verdict: pass on every number.** All 2,400 rows of `capacity_by_cause_corrected_orders.csv` agree with my figures within the tolerance. Every headline number and count in the B111 report and README agrees. There are three wording points (section 7) and one method point of my own (section 8). None of them changes a number.

## 1. Tolerance

I took this from the shared rules: counts and names exact, capacities within 0.5%, shares within one unit of the last printed digit. For this check I applied:

* **Forward and reverse layer effects:** exact, to the person. Both are differences of rounded capacities.
* **Shapley means, SDs, lowest and highest values:** within 1.5 people. My value function rounds each capacity before averaging; the builder averages unrounded capacities.
* **Counts of regions and the ranking of layers:** exact.
* **Printed millions and percentages:** within one unit of the last printed digit.

## 2. Wrong-value examples (to show the check can fail)

1. **csv comparison.** I fed `compare.py` my Australia short-term livestock forward effect raised by 1,000 people (4,704,257). It reported 1 failure: 4,703,257 against 4,704,257. With the switch off there are 0 failures.
2. **Value function.** I added 1,000 people to one subset value in `shap.mjs WRONG` (Australia, long term, after land, population, yields and livestock). The forward livestock effect moved by +1,000 and consumption by -1,000, so the forward check catches it. The Shapley values moved by only about 2 people, because one subset has a small weight in the average. So the Shapley columns are not a sensitive test on their own. The forward and reverse columns are the strict test.

## 3. My route

* **Layers.** Each layer is the set of inputs its release changes against the one before it in the chain `2011-corrected`, `2025-land` ... `2025-diet`. The inputs are region land, population, presets and yield vector, and workbook cells. I worked these out with my own diff (`diff.py`).
* **Corrections.** The three `2011-fixed` corrections are applied at every step, as in V29: the cell overrides of `biodiesel-yield` and `beef-carcase-yield`, and `state-population-sum`. The last has no capacity effect.
* **Model cells.** The organic, resilience and diet layers change disjoint sets of workbook cells.
* **Inputs shared between layers.**
  * Non-agricultural land is changed by both land and population.
  * The animal yield rows are changed by both crop yields (a 6-significant-figure rewrite) and livestock.
  * The short-term organic share moves in consumption and is matched by the organic layer's baseline.
* **The organic share.** I computed both the literal chain and the split that B76 and V29 use (the short-term organic share belongs to the organic layer). The split is the one compared below. The literal chain is in `nation_literal.log`.
* **Averaging.** For each subset, national level and both presets, I evaluated the corrected 2011 start with those layers applied. I then enumerated all 362,880 orderings exactly and checked the mean against the subset formula (difference below 1e-8). I also built the eight-layer game, with land and livestock as one player, and enumerated its 40,320 orderings. No sampling was used.
* **Zones.** I then extended the run to all 60 zones: 61,440 evaluations.

**My first composition rule, and the correction.** At first my rule for shared inputs was additive deltas. Nationally it gave the figures below. In about 14 regions it went wrong. The cause, found by testing the composition directly (`cmpcomp.mjs`):
* Where the livestock release sets an animal row to exactly 0 (sheep in Swan, milk in Wimmera and others), an additive delta on top of the crop-yields rewrite leaves about 1e-7 instead of 0.
* The workbook treats a tiny positive yield very differently from 0.

So a later absolute value must replace, not add. I changed the rule to "the animal rows take the value of the last layer in chain order that sets them". I also took non-agricultural land as the remainder of the total area, which differs from additive only in Northern and Yorke (zone 45), where non-agricultural land is held at 0.

I made this change after opening the builder's report. These are the same rules the builder states. I adopted them because the additive rule is demonstrably wrong at the zeros, not because the builder chose them. National figures differ between the two rules by at most 2 people.

## 4. The land-livestock overlap, from the code (holds)

* **`pipeline/yields/recent/livestock_zone.py`:**
  * Line 13 (docstring): grazing land is "the 2020-21 ABS grazing area of the zone (the land layer's pasture)".
  * Line 33 reads `pasture` from `data/2025-land/default-inputs-short-term.csv`.
  * Line 87 converts km2 to ha.
  * Line 100 sets `b['grazingHa'] = raw_pasture_ha[z]`.
* **`pipeline/yields/livestock.py`:**
  * Line 38: land = `grazingHa + hayHa`.
  * Line 56: milk = milk tonnes / (land x dairy DSE share).
  * Lines 47 and 63: sheep and cattle meat divide by the same land share plus feed-grain and feedlot hectares.
* **Reproduction.** I reran `livestock_zone.py` with the ABS files in the scratch folder `abs/ls/`, writing to scratch through `ZY_OUT`. Its output equals the committed `data/2025/yield_matrix_livestock.csv` byte for byte.

**Avon (zone 50), my arithmetic:**
* Pasture falls from 24,368 to 15,309 km2 (2011 over 2025: 1.592).
* The archive grazing plus hay, mean of 2006 to 2010, is 2,537,931 ha. The 2025 figure is 15,309 x 100 + 64,096 ha of hay = 1,594,996 ha. The ratio is 1.591.
* Milk (row 97) rises from 32.7489 to 67.5381 g/m2, which is 2.062 times. 2.062 / 1.591 = 1.296.
* Pasture times milk yield changes 1.296 times.
* Forward walk (from V29's zone file): land -134,628 and livestock +125,905 in the short term; -68,404 and +52,121 in the long term.

**Australia:** 3,639,794 / 3,318,689 = 1.097, and the archive denominator 368,480,563 ha over 333,836,257 ha = 1.104.

**Counterfactual.** I also reran the script with the 2011 land layer's pasture (`data/2011/default-inputs-short-term.csv`) in place of the 2025 one:
* Avon's milk becomes 43.07 g/m2, against 67.54. The area part alone is 1.568.
* Nationally, sheep meat gains +43% against 2011 with 2025 pasture and +30% with 2011 pasture. Milk: +12% against +2%. Cattle meat: +11% against +1%.

So most of the national livestock gain in milk and cattle meat comes from the smaller grazing area, not from more output.

## 5. My national figures (people; split organic share; capacities rounded before differencing)

Short term: 2011-fixed 33,307,814; 2025-fixed 41,503,537; change +8,195,723.

| Layer | Forward | Reverse | Shapley (exact, 9!) | SD |
|---|---|---|---|---|
| Land | -2,621,910 | -3,546,205 | -3,064,101 | 356,696 |
| Infrastructure land | 0 | 0 | 0 | 0 |
| Crop yields | +115,575 | +220,269 | +162,372 | 33,145 |
| Livestock | +4,703,257 | +6,374,770 | +5,502,789 | 485,892 |
| Consumption | +4,183,947 | +4,090,572 | +4,156,558 | 267,133 |
| Organic, resilience, fuel | 0 | 0 | 0 | 0 |
| Red meat mix | +1,814,854 | +1,056,317 | +1,438,106 | 386,153 |
| Land + livestock (sum per ordering) | +2,081,347 | +2,828,565 | +2,438,688 | 529,754 |
| Land and livestock as one player (8!) | +2,043,444 | +2,886,869 | +2,456,649 | 365,038 |

Long term: 15,350,146 to 15,623,209; change +273,063.

| Layer | Forward | Reverse | Shapley | SD |
|---|---|---|---|---|
| Land | -1,208,326 | -1,334,901 | -1,248,192 | 100,008 |
| Crop yields | +219,940 | +253,434 | +257,755 | 103,189 |
| Livestock | +599,578 | +743,648 | +628,764 | 113,970 |
| Consumption | 0 | 0 | 0 | 0 |
| Organic | +172,682 | +180,979 | +173,183 | 17,001 |
| Resilience | -7 | -7 | -7 | 0 |
| Fuel | +90,858 | +114,983 | +124,764 | 99,739 |
| Red meat mix | +398,338 | +314,927 | +336,796 | 89,563 |
| Land + livestock (sum) | -608,748 | -591,253 | -619,428 | 125,434 |
| Land and livestock as one player | -627,341 | -569,036 | -598,893 | 31,183 |

**The eight-layer game, other layers:**
* Short term: crop yields +161,723, consumption +4,149,655, red meat mix +1,427,697.
* Long term: crop yields +235,890, organic +176,975, fuel +103,056, red meat mix +356,042, resilience -7.

**The literal chain** (organic share left in consumption), short term: consumption Shapley +3,797,953 and organic +359,076. All other layers within about 600 people of the split.

**The 53 regions, largest layer by the Shapley value:**
* Short term: land 26, livestock 25, consumption 1, crop yields 1.
* Long term: crop yields 19, land 17, livestock 16, fuel 1.
* With land and livestock as one player: short term land and livestock 42, crop yields 7, consumption 4; long term land and livestock 31, crop yields 20, fuel 1, resilience 1.
* The forward walk names a different largest layer in 7 regions (short) and 2 (long); the reverse walk in 3 and 1.
* Largest forward-reverse gap in a region: land in Swan, -167,976 against -1,120,638 (short) and -84,184 against -275,328 (long).
* Infrastructure land moves capacity only in zone 45.

## 6. Comparison with the builder

| Item | Builder | Mine | Result |
|---|---|---|---|
| csv, nine layers, forward (1,200 values) | as in csv | same | pass, 0 differences |
| csv, nine layers, reverse (1,200) | | same | pass, 0 differences |
| csv, nine layers, Shapley mean (1,200) | | largest difference 0.83 | pass |
| csv, nine layers, SD (1,200) | | largest difference 0.78 | pass |
| csv, eight layers, forward / reverse (960 each) | | same | pass, 0 differences |
| csv, eight layers, mean / SD (960 each) | | largest differences 1.0 / 0.79 | pass |
| csv, total_change (240 rows x 3 columns) | | same | pass |
| Forward = old `capacity_by_cause_corrected.csv` | 0 mismatches | 0 in 1,080 (V29 `compare.py`) | pass |
| Old csv unchanged | sha256 50a02e7a...7ed2 | 50a02e7a...f7ed2 | pass |
| All national table cells (section 3 of the report, both README tables) | as section 5 | section 5 | pass, all within tolerance |
| Lowest to highest over orderings, Australia | e.g. livestock short +4,665,353 to +6,433,075 | +4,665,354 to +6,433,074 | pass (rounding) |
| Livestock 67% of the short-term change | 67% | 5,502,789 / 8,195,723 = 67.1% | pass |
| Land + livestock +2.44 M (30%) short | | +2,438,688, 29.8% | pass |
| Diet layers +5.59 M (68%) | | 5,594,663, 68.3% | pass (see wording 7.2) |
| Eight-layer ranking, short: consumption +4.15, L&L +2.46, red meat +1.43, yields +0.16 | | 4,149,655; 2,456,649; 1,427,697; 161,723 | pass |
| Eight-layer ranking, long: L&L -0.60, red meat +0.36, yields +0.24, organic +0.18, fuel +0.10 | | -598,893; 356,042; 235,890; 176,975; 103,056 | pass |
| Long term largest: land -1.25 M; with livestock -0.62 (one layer -0.60) | | -1,248,192; -619,428; -598,893 | pass |
| Forward differs from average, regions | 7 short, 2 long | 7, 2 | pass |
| Reverse differs from average (README) | 3, 1 | 3, 1 | pass |
| Largest layer by average, short | land 26, livestock 25 (README adds consumption 1, yields 1) | same | pass |
| Largest layer by average, long | yields 19, land 17, livestock 16 (README adds fuel 1) | same | pass |
| One-layer L&L largest | 42 short, 31 long | 42, 31 | pass |
| Swan land forward / reverse | -167,976 / -1,120,638; long -84,184 / -275,328 | same | pass |
| Infrastructure land moves only zone 45 | yes | yes | pass |
| Code lines (livestock_zone.py 13, 33, 87, 100; livestock.py 38, 56) | as cited | as cited | pass |
| Avon ratios 1.592 / 1.591, milk 32.75 to 67.54, 2.062, 1.296 | | same | pass |
| Avon forward land / livestock, short and long | -134,628 / +125,905; -68,404 / +52,121 | same | pass |
| Australia ratios 1.097 / 1.104 | | 1.0968 / 1.1038 | pass |
| Evaluations: 512 subsets, all 9! and 8! orderings, no sampling | yes | the same design (I counted 61,440 evaluations before removing duplicates; I did not check 30,720) | pass in substance |
| Column set (layer; preset; forward; reverse; shapley_mean; shapley_sd; zone) | present, plus extras | | pass |

## 7. Claim rows the builder says move, and the sentences

* **A354 to A362 (Tier A; forward-walk values): stand as values.** I confirm every forward value and the Shapley values the builder lists for new rows. They are within 1 person, and so are the land-and-livestock pair values.
* **A357, A358, A362, the driver sentence: the numbers hold; the wording needs two notes.**
  1. These three register rows hold layer values, not the sentence. The sentence to change is the Paper A abstract ("Livestock, consumption and the red meat mix of the diet drove the rise", `papers/A_results/draft/A_s01-04.md` and `paper_A_draft1.md`) and `highlights.md` line 4. The register job should attach the change to whatever row carries that sentence, not to A357, A358 and A362.
  2. "The diet layers ... +5.59 million" says a little more than the figures. The consumption layer also carries the short-term fuel, biofuel and timber presets, not only meat and egg share and red meat share. Better: "the consumption and red-meat-mix layers". Or split the consumption layer before calling all of it diet. The number does not change.
* **A365 (Tier A; ranking): stands.** Land > livestock > red meat mix > crop yields > organic > fuel holds forward, reverse and on the average. Resilience is -7 in all three. With land and livestock as one layer: land and livestock > red meat mix > crop yields > organic > fuel.
* **A072 and A073 (Tier B): stand.** 8,195,723 and 273,063 are reproduced exactly.
* **Other wording, minor and no number change:**
  * The README writes "resilience table -0.00 million". "-7 people" is clearer.
  * The README's long-term sentence names "land and livestock together" for both the sum (-0.62 M) and the one-layer value (-0.60 M). Use "as one layer" for the second.
  * The report's region counts in section 3 drop the 1-region categories (consumption 1, crop yields 1; fuel 1). The README lists them.

## 8. What I would do differently, and whether it changes a number

1. **Area and output split of the livestock layer (R03a issue 2).** The builder left this out because the raw ABS files are not in the repository. They are in the scratch folder, `abs/ls/`, and the script reproduces the committed rows exactly from them. The 2011-pasture rerun in section 4 gives the area part directly: Avon area part 1.568 and output part about 1.315; nationally, milk +2% and cattle meat +1% at 2011 pasture. A next job could run a land-layer variant on these rows. **No B111 number changes.**
2. **The 2011 denominator.** The 2011 rows divide by the archive mean grazing plus hay (25,379 km2 for Avon), not by the 2011 land layer's pasture (24,368 km2). Two variants are therefore possible, and I computed both:
   * The builder's area ratio, on the archive denominator: 1.591.
   * My ratio on the 2011 land layer's pasture: 1.568.

   The README should say which denominator it uses, and it does. **No number changes.**
3. **Composition rules.** Mine were additive at first and wrong at exact zeros; that changed about 14 regions before the fix. The builder's replacement and remainder rules are right. **No builder number changes.**
4. **Shapley on unrounded capacities (builder) against rounded (mine).** The difference is at most 1 person. No change.

## 9. Register

Register rows touched: none.

## 10. Rerun (from the repository root)

```
V=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v37
node $V/shap.mjs nation SPLIT REPL           # national, exact 9! (also writes v_nation_split_repl.json)
node $V/shap.mjs nation                      # literal organic chain
node $V/shap.mjs nation SPLIT REPL WRONG     # wrong-value run
for r in 2-15 16-30 31-45 46-60; do ZR=$r node $V/shap.mjs zones SPLIT REPL & done; wait
python3 -I -c "import json,glob; v={}; [v.update(json.load(open(f))) for f in glob.glob('$V/v_zones_*_split_repl.json')]; json.dump(v,open('$V/v_all_split_repl.json','w'))"
python3 -I $V/game8.py $V/v_nation_split_repl.json
python3 -I $V/game8.py $V/v_all_split_repl.json $(seq -s, 1 60) $V/g8_all.json
python3 -I $V/compare.py $V analysis/comparison_2025/capacity_by_cause_corrected_orders.csv [WRONG]
ZY_OUT=$V/ls_2025 python3 -I pipeline/yields/recent/livestock_zone.py /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/abs/ls
```

## 11. Files read

**Before comparing:**
* Briefs: `qa/briefs/V37_check_B111.md`, `qa/briefs/_checker_rules_results_wave.md`, `qa/briefs/B111_decomposition_orders.md`, `qa/briefs/V29_decomposition_second_route.md`.
* Reports and earlier work: `qa/reports/V29_decomposition_second_route.md`, V29's scratch `chain.mjs`, part of `qa/reports/R03a_response_plan_A.md`.
* Code: `web/src/model/evaluator.js`, `pipeline/yields/recent/livestock_zone.py`, `pipeline/yields/livestock.py`.
* Data: the `model.json` and `regions.json` of the ten chain releases, `methods/*/method.json` (three corrections), `pipeline/yields/archive_livestock_inputs.json`, `data/2011/` and `data/2025-land/` default inputs, `data/2025/yield_matrix*.csv`.

**At the end:**
* The builder's work: `qa/reports/B111_decomposition_orders.md`, `analysis/comparison_2025/capacity_by_cause_corrected_orders.csv`, the README section "Decomposition in every order (B111)", `analysis/comparison_2025/decompose_corrected.mjs` (lines 1 to 60 and 160 to 330), `decompose_orders_worker.mjs`.
* For the claim rows: the register rows A072, A073 and A354 to A365 (read only), the Paper A abstract and highlights.
