# Australian loss factors (SCOPE.md E4)

The thesis took its consumer, retail and primary-to-retail loss factors from US studies because it found no detailed Australian figures (Base columns G, I and L: Muth 2011 and Buzby 2010). This analysis sets them against the two sources that now exist, and builds the one change they support as a method module, `loss-factors-australia` (improved tier, line 2).

`loss_factors.mjs` does all of it (`compare`, `module`, `effect`); the data are `fial_table5_2018_19.csv`, `fbs_au_food_2018_19.csv`, `fao_region2_loss.csv` and `abs_apparent_consumption_2018_24.csv` (ABS, *Apparent Consumption of Selected Foodstuffs, Australia, 2023-24*, Table 1.1, tonnes by AUSNUT food group; CC BY 4.0).

## The sources

| Source | What it gives | Limits |
|---|---|---|
| FIAL 2021 (National Food Waste Strategy Feasibility Study, 2018-19), Table 5 | Tonnes of waste by 18 food groups and 7 stages (primary, processing, distribution, retail, household, hospitality, institutional) for Australia | Group tonnes come from a fraction-of-throughput method, not from disposal statistics; the retail stage agrees with the baseline (527 against 526 thousand tonnes) but consumption is 4,640 thousand tonnes against 3,932 in the baseline. It has no supply by group, so the supply is taken from the FAO food balance for Australia (mean 2018 and 2019, "Food"), whose bases differ (carcase weight, milk equivalent, grain equivalent) |
| Gustavsson et al. (FAO 2011), Annex 4, "North America and Oceania" | Percent wasted at each step by seven commodity groups | One region of USA, Canada and Oceania; mostly US and Canadian data; distribution and retail are one step |

## What the comparison shows (`compare.csv`)

Mean loss in the model (weighted by the mass of food bought in the short-term default diet) against the two sources, per cent:

| Stage | Model (US factors) | FIAL Australia | FAO Region 2 |
|---|---|---|---|
| Retail, all foods | **9.4** | **3.1** of the 16.8 million tonnes to market (retail 526 thousand tonnes) | 0.5 to 12 by group |
| Consumption stages (households, hospitality, institutional), all foods | 21.6 | 23.4 (baseline, 3,932 thousand tonnes) to 27.6 (Table 5) | 4 to 33 by group |
| Distribution and primary to retail | 2.0 | 1.5 (distribution only) | |

* **Retail is the clear gap.** The model loses three times what Australian retail measured: cereals 12% (FIAL 0.5%, FAO 2%), dairy 7 to 12% (0.7%, 0.5%), fruit 11.5% (3.2%, 12%), vegetables 6 to 11% (3.0%, 12%), red meat 6.4% (1.9%, 4%), poultry, eggs and seafood 6.8% (3.3%, 4 to 9%), nuts 6% (0.5%, 1%). Both sources agree on the direction in every group except that FAO's fruit and vegetables (12%) is close to the model's, and FAO combines distribution with retail.
* **Consumption is consistent in total and not by group.** The model is 2 to 6 points below FIAL in total. By group the FIAL shares over the FAO supply are 7.5% for cereals (the "complex products" group, 546 thousand tonnes, which includes much cereal food, is unassigned), 10 to 15% for meat and dairy, 28% for vegetables, 40% for fruit, against 20 to 28% in the model for meat, dairy and cereals and 25% for fruit: too uncertain on the supply bases to set group by group, so only the total is aligned.
* **Primary to retail (L) is not comparable.** FIAL's primary and processing stages include crops left in the field (already outside the model's harvested yields) and by-products (the processing yield K and the recycling stage handle those). FIAL's distribution stage alone (1.5%) is below the model's 2.0%. L is unchanged.

## The module and its effect (`effect.csv`)

Retail loss rescaled by category to the FIAL retail tonnes over the FAO supply (each food keeps its share of its category's loss; categories without a FIAL group unchanged), and consumer loss rescaled by one factor to the FIAL baseline for the consumption stages (24.6% of the food reaching them). Australia, release `2025-fixed`, million people:

| Variant | Short term | Change | Long term |
|---|---|---|---|
| Current (US factors) | 39.52 | | 15.92 |
| Retail to FIAL only | 41.63 | +5.3% | 15.92 |
| Consumer to FIAL baseline only | 38.16 | -3.4% | 15.92 |
| **Both (the module)** | **40.20** | **+1.7%** | 15.92 |
| Retail to FIAL and consumer by group, household waste over ABS sales (sensitivity) | 43.95 | +11.2% | 15.92 |
| Retail to FAO Region 2 only (sensitivity) | 40.91 | +3.5% | 15.92 |
| Retail to FAO Region 2 and consumer to FIAL (sensitivity) | 39.51 | 0.0% | 15.92 |

* **The change is small in total because it moves waste between stages.** The retail saving (+2.1 million) is almost cancelled by the larger consumer loss (-1.4 million). The sign of the net effect depends on the retail source, so it is inside the uncertainty of the sources and is not a finding about capacity; the finding is that the thesis's US factors put too much of the waste at retail and slightly too little at the consumer.
* **The long term is unaffected** because the long-term default is zero avoidable waste (the thesis's frugal scenario).
* **Where it matters:** the stage split decides what a waste-reduction policy can achieve (retail waste is a minor part of the Australian total; halving household waste is the lever) and what can be recycled (the recycling pool is stage-specific); the 12% setting now denotes Australian measured waste, which is what the national target of a 50% cut is measured against.

## Group-level consumer loss with ABS sales (2026-10-29, sensitivity)

The ABS publishes *Apparent Consumption of Selected Foodstuffs* (experimental, 2023-24 release; retail-sector sales in tonnes by AUSNUT food group for 2018-19 to 2023-24, `abs_apparent_consumption_2018_24.csv`), which gives the missing product-weight supply for the households' side. Household waste of Table 5 (scaled by 2,463 / 3,172 to the baseline) over the 2018-19 sales, per cent: red meat 14 (model 21), poultry 21 (model 28 for poultry, eggs and seafood), milk and cheese 21 (model 20 to 24), fruit 26 (model 25), bread and cereal products 12.5 (model 20 to 23), vegetables 39 (model 17 to 30), nuts 20 (model 11). Seafood (53%) and eggs (0.1%) are implausible and show that FIAL's group tonnes and the ABS sales do not always cover the same food. The ABS sales leave out food service and markets, so the denominators are not those of the model's consumer stage (households, hospitality and institutions together).

**This matters for capacity, unlike the total.** Setting the consumer loss by group in these proportions (the total kept at the module's 24.6%) with the retail change gives Australia 43.95 million in the short term (+11.2% on the US factors; the module is +1.7%): meat carries the land, and its consumer loss falls from 21% to about 14% while vegetables and cereals rise. The evidence is not good enough to adopt (it mixes two sources with different coverage and one scaling assumption for FIAL's group tonnes), so it stays a sensitivity, and the module aligns only the total. A decision for Murray: adopt the by-group consumer loss as an alternate release, or wait for a better source (the ABS also publishes household expenditure and food-service sales separately, which could fix the denominators).

## Not done

* Group-level consumer factors in the module: see the section above (a sensitivity of up to +11%). Recorded in `DISCUSSION.md` row 18.
* Primary-to-retail factors for fruit and vegetables (4 to 10% in the model, 4.4% FIAL distribution plus FAO's post-harvest 4%): not enough to distinguish from the model's values.
* Whether the 12% slider should scale retail and consumer losses together (it does, as in the thesis).

## In the comparison grid

Australia, `results/comparison_cells.csv` and `method_effects.csv`: alone, the module adds 0.91 million (2011 data) and 1.05 million (2025 data) in the short term and nothing in the long term. The improved cells are now 2011 33.62 and 2025 39.85 million short term (33.31 and 39.52 corrected); long term 12.56 and 14.85 (15.35 and 15.92 corrected).
