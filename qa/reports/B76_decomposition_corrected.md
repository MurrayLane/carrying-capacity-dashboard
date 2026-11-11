# B76: the Paper A change decomposition on the corrected releases (decision 62)

## What was done

A new script, `analysis/comparison_2025/decompose_corrected.mjs`, rebuilds the layer walk on the corrected tier. It writes `analysis/comparison_2025/capacity_by_cause_corrected.csv` (both presets, all 60 zones) and adds the section "Corrected-tier decomposition" to `analysis/comparison_2025/README.md`. The section's numbers come from the script, not typed by hand. `capacity_by_cause.csv` was made by `decompose.mjs` (Node), so the new script is Node too. No release, method module, evaluator, published-tier csv or published-tier script was changed. `npm run results` and `build-data.mjs` were not run. The script checks that the built data in `web/public/data` matches its source hashes (it did for all 12 releases used, and it matches `results/releases.json`), so neither was needed.

## Method

* **Start.** Release `2011-corrected`, with the corrected tier's method modules applied in memory: state-population-sum, biodiesel-yield and beef-carcase-yield, the modules of `2011-fixed`. They are applied the way the release resolver and `build-data.mjs` apply them: cell overrides on the release's model, and state populations set to the sum of their regions. The script checks that this start equals `2011-fixed` evaluated from its own built data.
* **Layers.** The 2025 layers are then added one at a time in chain order, each with the same modules applied: `2025-land`, `2025-population`, `2025-yields`, `2025-livestock`, `2025-consumption`, `2025-organic`, `2025-resilience`, `2025-fuel` and `2025-diet` (layer 9, the red meat mix).
* **End.** The last step equals `2025-fixed`. That release is `2025-diet` with biodiesel-yield and beef-carcase-yield; state-population-sum makes no difference to capacity on the 2025 data.
* **Layer effect.** A layer's effect is the rounded capacity after it minus the rounded capacity before it. The effects therefore add up, in whole people, to `2025-fixed` minus `2011-fixed`. There is no interaction term, but each effect depends on the order: a layer is measured on top of the layers before it.
* **Organic share.** Its split follows the published table. The consumption step leaves the short-term organic share at 2011's 2%. The organic step moves it to 7%, together with the 2025-organic factors and baseline constant.
* **Population.** Population is reported as a status change, not a cause. The csv gives the 2025 capacity against both the 2011 and the 2025 populations: `population_2011_over_capacity_2025` and `population_over_capacity_2025`.
* **csv columns.** The csv has `tier` plus the column names of `capacity_by_cause.csv`. Three columns are added: `infrastructure_land_only`, `red_meat_mix_only` and `population_2011_over_capacity_2025`. In this file the cause columns hold each layer's change in capacity (people), not a capacity. `all_2025` is the 2025-fixed capacity and `interaction` is the residual of the sum check.

Rerun: `cd analysis/comparison_2025 && node decompose_corrected.mjs` (about a minute).

## National table, corrected tier (people)

| Australia | Short term | Long term |
|---|---|---|
| 2011, corrected (`2011-fixed`) | 33,307,814 | 15,350,146 |
| Land (2025-land) | -2,621,910 | -1,208,326 |
| Infrastructure land that follows population (2025-population) | 0 | 0 |
| Crop yields (2025-yields) | +115,575 | +219,940 |
| Livestock (2025-livestock) | +4,703,257 | +599,578 |
| Consumption, without the organic share (2025-consumption) | +4,183,947 | 0 |
| Organic update (share 7% and 2025-organic) | 0 | +172,682 |
| Resilience table (2025-resilience) | 0 | -7 |
| Long-term liquid fuel (2025-fuel) | 0 | +90,858 |
| Red meat mix of the diet (2025-diet, layer 9) | +1,814,854 | +398,338 |
| 2025, corrected (`2025-fixed`) | 41,503,537 | 15,623,209 |
| Sum of the layers | +8,195,723 | +273,063 |
| 2025-fixed minus 2011-fixed | +8,195,723 | +273,063 |

Population, status not cause (Australia, 22,326,388 to 27,608,200 people; the ratio is people over capacity, and above 1 is over capacity):

| Ratio | Short | Long |
|---|---|---|
| 2011 people / 2011 capacity | 0.670 | 1.454 |
| 2011 people / 2025 capacity | 0.538 | 1.429 |
| 2025 people / 2025 capacity | 0.665 | 1.767 |

By region (the 52 NRM regions and the Northern Territory), the layer with the largest absolute effect is:

* Short term: livestock in 27 regions, land in 21, consumption in 4, crop yields in 1.
* Long term: crop yields in 19, livestock in 18, land in 15, fuel in 1.

## Sum check

Tolerance: an exact residual of 0 in whole people on the rounded figures, and 1e-6 people on the unrounded capacities. The check covers 120 cells: all 60 zones (national, 7 state groups, 52 regions) in both presets.

* **Start.** It equals `2011-fixed`, with a largest unrounded difference of 0 people.
* **End.** It equals `2025-fixed`, with a largest unrounded difference of 0 people.
* **Layer sum.** The layers add to the rounded release difference with a residual of exactly 0 in every cell; the `interaction` column is 0 everywhere. The largest unrounded residual is 2.9e-11 people.
* **Result.** The check passed in all 120 cells.
* **Second route.** A separate Python read of the csv against `results/comparison_cells.csv` (columns `capacity_2011_corrected`, `capacity_2025_corrected`, `data_effect_corrected`) found 0 mismatches in the 120 rows.

## Layers whose definition differs from the published-tier table (`capacity_by_cause.csv`)

1. **Measurement.** The published table applies each cause alone to the 2011 data and reports the remainder as an interaction. The corrected table walks the layers cumulatively, so it has no interaction and its effects depend on the order. In particular, the published table measures organic, resilience and fuel on the 2011 data; here they sit on top of all the earlier layers.
2. **End point.** The published `all_2025` is `2025-fuel`, which lacks layer 9. Here it is `2025-fixed`, the full chain. Red meat mix is a new layer: +1.81 million short term and +0.40 million long term nationally.
3. **Every layer passes through the corrected method.** The layer data are the same, but the model applies beef carcase-to-retail 0.705 (Base!K175) and biodiesel from oilseeds counted once (Base!K336:K344).
   * Livestock, the red meat share in consumption and the red meat mix act through the beef conversion.
   * Short-term fuel and biofuel, and the long-term fuel layer, act through the biodiesel conversion.
   * So these layers measure the same data change on different conversion factors.
4. **Infrastructure land is a new column, not a population cause.** `decompose.mjs` says that 2025-land and 2025-population give identical capacities. That is not true in one zone on either tier. In Northern and Yorke (zone 45), which has no non-agricultural land, the infrastructure land of the population layer (population x 730 m2) moves capacity:
   * corrected tier: -228 short term and -65 long term;
   * published tier: -264 and -67 (`results/2025-land.csv` against `results/2025-population.csv`).

   A probe confirms the cause: the population input alone moves nothing, and the infrastructure land alone moves all of it. The published table folds nothing for this. That is harmless there, because that table is not a sum, but the claim in its comment is wrong for one zone. I left it as it is (a published-tier file).
5. **2011 state populations.** These are the sum of their regions (state-population-sum, error 6). For example, NSW-ACT is 7,591,160 here against 7,454,854 in the published table, and Queensland 4,513,849 against 3,908,395. So the state-level 2011 ratios differ. The national population and all capacities are unaffected.
6. **Crop yields.** The step takes the whole `2025-yields` release. That release also rewrites the 2011 animal rows at 6 significant figures (660 cells, largest relative change 9.4e-6). The published table took only the crop rows. The effect is negligible.
7. **Organic.** Same split as the published table: the share goes in the organic column, not consumption.

## Effect on Paper A section 4 and the claims register (not edited)

* **Claim rows on section 4.** Only A072 and A073 carry section 4. Both read `results/comparison_cells.csv` `data_effect_corrected`. This walk reproduces their values exactly (8,195,723 and 273,063), so their values do not need re-deriving, and the decomposition can serve as their second route.
* **Points 3 to 6 of the scope's section 4 evidence table.** These have no claim rows (gap 2) and cite the published-tier `capacity_by_cause.csv`. They need re-deriving from `capacity_by_cause_corrected.csv`.
* **Points that change on the corrected walk:**
  * Point 4 (long term: crop yields the largest cause, then fuel, land small) does not hold. Land is the largest effect (-1.21 million). Then come livestock (+0.60), the red meat mix (+0.40), crop yields (+0.22), organic (+0.17) and fuel (+0.09).
  * Point 5 (the causes do not add; interaction reported) no longer applies: the walk adds exactly.
  * Point 3 (short term) holds, with the red meat mix added as a third large positive layer.
* **Section 4 Purpose and argument.** These sentences repeat point 4's long-term reading (crop yields and fuel) and need the same re-derivation.
* **N-A4.** This job implements option (a).

## Files written

* `analysis/comparison_2025/decompose_corrected.mjs` (new)
* `analysis/comparison_2025/capacity_by_cause_corrected.csv` (new, 120 rows)
* `analysis/comparison_2025/README.md` (the section "Corrected-tier decomposition" appended; nothing above it changed). `write_readme.py` rewrites the whole README and would drop this section. After running it, run `decompose_corrected.mjs` again, which replaces the section. I did not change `write_readme.py` because it is a published-tier file.
* `qa/reports/B76_decomposition_corrected.md` (this report)
* Probes only, outside the repository: `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/` (fresh.mjs, probe.mjs to probe4.mjs, README.before.md).

Wrong-value check: example only, not made. Suppose the walk stopped at `2025-fuel`, as the published decomposition does. The short-term layers would then sum to 8,195,723 - 1,814,854 = +6,380,869, against the release difference `2025-fixed` minus `2011-fixed` of +8,195,723. The residual of 1,814,854 people is far above the tolerance of 0, so the check would fail in the Australia short-term cell, and in every cell where the red meat mix moves capacity.
