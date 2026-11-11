# V29: second route for the corrected-tier decomposition (decision 68)

Checker: independent, blind. Brief: `qa/briefs/V29_decomposition_second_route.md`; rules: `qa/briefs/_checker_rules_results_wave.md`. No repository file other than this report was changed; no git, no subagents, no network; `npm run results` and `build-data.mjs` were not run. My script and outputs are in the scratch folder `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v29/` (`chain.mjs`, `compare.py`, `layers_*.csv`).

## 1. Tolerance, stated before comparing

* A layer effect holds when my own value, the difference of rounded cumulative capacities (whole people), equals the builder's exactly ("to the person").
* The sum check holds when, for each cell, the nine layers add to `2025-fixed` minus `2011-fixed` (rounded capacities from `results/<release>.csv`) with a residual of exactly 0, and my walk's start and end equal those published capacities exactly.
* The long-term ordering holds when my ordering of the non-zero national long-term layers, by size of effect, is the builder's.

## 2. A deliberate wrong value, to show the check can fail

I added a switch `WRONG` to my script that adds 1,000 people to the cumulative capacity after the crop-yields step (Australia, long term).

* On my own sum check it made no difference (residual still 0): the layers telescope, so a wrong intermediate capacity moves two adjacent layers by +1,000 and -1,000 and cancels. The sum check can only catch a wrong start or end, so it is not on its own a test of the layer values. This is why the layer-by-layer comparison below is the real test.
* On the comparison with the builder's csv, the same wrong value gave 2 mismatches out of 1,080 layer values: crop yields 220,940 against 219,940 and livestock 598,578 against 599,578 (Australia, long). With the switch off there are 0. So a wrong value does show.

## 3. My route

From `results/README.md`, `releases/README.md`, `results/releases.json`, the `release.json` of each chain release and of `2011-fixed` and `2025-fixed`, the three method modules (`methods/<id>/method.json`) and `web/src/model/evaluator.js`:

* `2011-fixed` is `2011-corrected` with three modules: `state-population-sum` (state populations set to the sum of their regions; no capacity effect), `biodiesel-yield` (Base!K336:K344 replaced) and `beef-carcase-yield` (Base!K175 = 0.705). I confirmed from the built data that the `2011-fixed` model differs from the `2011-corrected` model, and the `2025-fixed` model from the `2025-diet` model, in exactly those ten Base cells and nothing else, and that no chain release itself changes any of those ten cells.
* The chain: `2025-land` extends `2011-corrected`, then population, yields, livestock, consumption, organic, resilience, fuel, diet, each extending the one before.
* My script loads each release's committed `model.json` and `regions.json`, writes the cell overrides from the module files into the model, sets state populations to the sum of their regions, and evaluates every zone at the release's own short and long presets (`evaluate(region, {...land, ...preset, population})`), rounding each capacity. A layer's effect is the rounded capacity after it minus the one before.

## 4. My national table (Australia, people), built before opening the builder's files

Literal chain: each step is the release exactly as built, with the corrections applied.

| Step | Short term | Long term |
|---|---|---|
| Start, 2011-corrected + corrections | 33,307,814 | 15,350,146 |
| Land (2025-land) | -2,621,910 | -1,208,326 |
| Population and infrastructure land (2025-population) | 0 | 0 |
| Crop yields (2025-yields) | +115,575 | +219,940 |
| Livestock (2025-livestock) | +4,703,257 | +599,578 |
| Consumption (2025-consumption, as released, organic share 7% included) | +3,802,283 | 0 |
| Organic (2025-organic) | +381,664 | +172,682 |
| Resilience table (2025-resilience) | 0 | -7 |
| Long-term fuel (2025-fuel) | 0 | +90,858 |
| Red meat mix (2025-diet) | +1,814,854 | +398,338 |
| End, 2025-diet + corrections | 41,503,537 | 15,623,209 |
| Sum of the layers | +8,195,723 | +273,063 |
| 2025-fixed minus 2011-fixed | +8,195,723 | +273,063 |
| Residual | 0 | 0 |

Independent confirmation of the endpoints: `results/comparison_cells.csv`, zone 1, `capacity_2011_corrected` 33,307,814 (short) and 15,350,146 (long), `capacity_2025_corrected` 41,503,537 and 15,623,209; `results/2011-fixed.csv` and `results/2025-fixed.csv` give the same. My start and end equal them exactly. Extended to all 60 zones (done before opening the builder's files), my start and end equal the published `2011-fixed` and `2025-fixed` capacities and the layers sum with residual 0 in all 120 cells. The population step moves capacity in one zone only: Northern and Yorke (zone 45), -228 short and -65 long.

## 5. Comparison with the builder (Australia)

After opening the builder's files I found one difference of definition: the builder's consumption step keeps the short-term organic share at its 2011 value (2%) and moves it in the organic step instead. I added this as a switch (`SPLIT`) to my script, taking the 2011 share from `2011-corrected`'s own presets. Both columns are shown.

| Layer | Builder | Mine, literal chain | Difference | Mine, builder's split | Difference |
|---|---|---|---|---|---|
| Short: land | -2,621,910 | -2,621,910 | 0 | -2,621,910 | 0 |
| Short: infrastructure land | 0 | 0 | 0 | 0 | 0 |
| Short: crop yields | +115,575 | +115,575 | 0 | +115,575 | 0 |
| Short: livestock | +4,703,257 | +4,703,257 | 0 | +4,703,257 | 0 |
| Short: consumption | +4,183,947 | +3,802,283 | -381,664 | +4,183,947 | 0 |
| Short: organic | 0 | +381,664 | +381,664 | 0 | 0 |
| Short: resilience | 0 | 0 | 0 | 0 | 0 |
| Short: fuel | 0 | 0 | 0 | 0 | 0 |
| Short: red meat mix | +1,814,854 | +1,814,854 | 0 | +1,814,854 | 0 |
| Long: land | -1,208,326 | -1,208,326 | 0 | -1,208,326 | 0 |
| Long: infrastructure land | 0 | 0 | 0 | 0 | 0 |
| Long: crop yields | +219,940 | +219,940 | 0 | +219,940 | 0 |
| Long: livestock | +599,578 | +599,578 | 0 | +599,578 | 0 |
| Long: consumption | 0 | 0 | 0 | 0 | 0 |
| Long: organic | +172,682 | +172,682 | 0 | +172,682 | 0 |
| Long: resilience | -7 | -7 | 0 | -7 | 0 |
| Long: fuel | +90,858 | +90,858 | 0 | +90,858 | 0 |
| Long: red meat mix | +398,338 | +398,338 | 0 | +398,338 | 0 |

Start, end, sum and residual: builder 33,307,814 / 41,503,537 / +8,195,723 / 0 (short) and 15,350,146 / 15,623,209 / +273,063 / 0 (long); mine the same.

**Holds** for every national layer under the builder's stated split. Under the literal chain, only the short-term consumption and organic layers differ, by the same 381,664 people in opposite directions, and their sum (+4,183,947) is the same.

## 6. All 120 cells

`compare.py` checks, for every zone and preset, the start (`capacity_2011`), the end (`all_2025`), `interaction` = 0 and all nine layer columns of `analysis/comparison_2025/capacity_by_cause_corrected.csv`: 120 cells, 1,080 layer values.

* Builder's split: **0 mismatches** in 1,080 layer values; starts, ends and residuals all agree. **Holds.**
* Literal chain: 118 mismatches, all in the short-term consumption and organic columns (59 zones each; in the remaining zone both are 0), each pair equal and opposite. No other column differs.
* Wrong-value run: 2 mismatches (section 2).

I also recounted the builder's region summary (the 53 regions: 52 NRM regions and the Northern Territory, zone 60): the layer of largest absolute effect is livestock in 27, land in 21, consumption in 4, crop yields in 1 (short), and crop yields in 19, livestock in 18, land in 15, fuel in 1 (long). Same as B76.

## 7. Long-term ordering

Mine, by size of the national long-term effect: land (-1,208,326), livestock (+599,578), red meat mix (+398,338), crop yields (+219,940), organic (+172,682), fuel (+90,858), then resilience (-7). B76: land, livestock, red meat mix, crop yields, organic, fuel. **Holds**: the six layers match in order. Note: seven layers are non-zero, not six; resilience is -7 people. B76's list leaves it out, while the README table shows it. It is too small to matter to the ordering, but a sentence saying "six non-zero layers" would be inexact; "six layers of any size, and resilience at -7" is accurate.

## 8. What I would do differently, and whether it changes a number

1. **Organic share split.** The literal chain puts the cost of the higher organic share (2% to 7%) in consumption and its recovery in organic, because 2025-consumption raises the share before 2025-organic moves the baseline constant (Yield!E2) to 7%. The builder moves the share into the organic step, where it and the baseline cancel to exactly 0 in every short-term cell. The builder's choice is stated in the README and follows the published-tier table, so I would keep it, but I would add one line: on the literal chain the short-term consumption layer is +3,802,283 and organic +381,664. It changes two short-term layer values, not any total, any long-term value or the ordering.
2. **Population step name.** My literal step and the builder's `infrastructure_land_only` are the same numbers; the builder's naming (population is status, not cause) is the clearer one. No change.
3. **Crop-yields step takes the whole 2025-yields release** (including animal rows rewritten at 6 significant figures). I did the same; the effect is below a person nationally. No change.
4. **The sum check is telescoping**, so it can only detect a wrong start or end (section 2). The builder's checks on start and end against the frozen releases are the meaningful part; its "wrong-value check" in B76 is an example, not a run. Not a number change.

## 9. Register

Register rows touched: none. Claims confirmed: **A072** (Australia, short, `data_effect_corrected` 8,195,723) and **A073** (Australia, long, 273,063), both by my walk's endpoints and by `results/comparison_cells.csv`. Claims I would add for section 4 points 3 to 6, if they are stated in Paper A: the national long-term land layer (-1.21 million), livestock (+0.60 million), red meat mix (+0.40 million) and the ordering of the long-term layers; and the short-term land (-2.62 million), livestock (+4.70 million), consumption (+4.18 million, under the stated split) and red meat mix (+1.81 million) layers; source `analysis/comparison_2025/capacity_by_cause_corrected.csv`, second route this report.

## 10. Rerun

From the repository root:

```
node /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v29/chain.mjs nation          # national, literal chain
node /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v29/chain.mjs zones           # all 60 zones, literal chain
node /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v29/chain.mjs zones SPLIT     # builder's organic split
node /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v29/chain.mjs zones SPLIT WRONG
cd /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v29 && python3 -I compare.py layers_zones_split.csv /home/user/carrying-capacity-dashboard/analysis/comparison_2025/capacity_by_cause_corrected.csv
```

## 11. Files read

Before comparing: `qa/briefs/V29_decomposition_second_route.md`, `qa/briefs/_checker_rules_results_wave.md`, `results/README.md`, `results/releases.json`, `releases/README.md`, `releases/<id>/release.json` for 2011-fixed, 2025-fixed and the nine chain releases, `methods/{state-population-sum,biodiesel-yield,beef-carcase-yield}/method.json`, `web/src/model/evaluator.js`, `analysis/sensitivity_2025/evaluate.mjs` (loader pattern), `web/public/data/<release>/{model,regions}.json` (data), `results/comparison_cells.csv`, `results/2011-fixed.csv`, `results/2025-fixed.csv`. At the end: `analysis/comparison_2025/capacity_by_cause_corrected.csv`, `analysis/comparison_2025/decompose_corrected.mjs`, the README section "Corrected-tier decomposition", `qa/reports/B76_decomposition_corrected.md`, and the A072 and A073 rows of `qa/claims_register.csv`.

Order note: the rules ask for a `report.md` in the scratch folder; the brief names this file as the only report, so I wrote only this one.
