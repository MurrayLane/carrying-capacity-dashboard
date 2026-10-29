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
* **Consumption is 2 to 6 points low in total, and the split by group is better measured with the ABS sales and a bin audit (next sections).** By group on the FAO supply the FIAL shares are 7.5% for cereals (the "complex products" group, 546 thousand tonnes, which includes much cereal food, is unassigned), 10 to 15% for meat and dairy, 28% for vegetables, 40% for fruit, against 20 to 28% in the model for meat, dairy and cereals and 25% for fruit; the FAO supply bases (carcase weight, milk equivalent, grain equivalent) make that comparison weak.
* **Primary to retail (L) is not comparable.** FIAL's primary and processing stages include crops left in the field (already outside the model's harvested yields) and by-products (the processing yield K and the recycling stage handle those). FIAL's distribution stage alone (1.5%) is below the model's 2.0%. L is unchanged.

## The module and its effect (`effect.csv`)

Retail loss rescaled by category to the FIAL retail tonnes over the FAO supply (each food keeps its share of its category's loss; categories without a FIAL group unchanged). Consumer loss: the total aligned to the FIAL baseline for the consumption stages (24.6% of the food reaching them), and the differences between food groups taken from the Burnside bin audit (next section). Australia, release `2025-fixed`, million people:

| Variant | Short term | Change | Long term |
|---|---|---|---|
| Current (US factors) | 39.52 | | 15.92 |
| Retail to FIAL only | 41.63 | +5.3% | 15.92 |
| Consumer total to FIAL baseline only | 38.16 | -3.4% | 15.92 |
| Retail and consumer total (the first version of the module) | 40.20 | +1.7% | 15.92 |
| **Retail to FIAL and consumer by group from the bin audit (the module)** | **43.86** | **+11.0%** | 15.92 |
| Same with the group shape from FIAL tonnes over ABS sales (cross-check) | 43.98 | +11.3% | 15.92 |
| Retail to FAO Region 2 only (sensitivity) | 40.91 | +3.5% | 15.92 |
| Retail to FAO Region 2 and consumer total to FIAL (sensitivity) | 39.51 | 0.0% | 15.92 |

* **The totals alone move little (+1.7%); the split between foods moves capacity by 11%.** Red meat carries most of the land in the short term, so the share of waste put on meat decides how many people the same food supply feeds.
* **The long term is unaffected** because the long-term default is zero avoidable waste (the thesis's frugal scenario).
* **The 12% setting now denotes Australian measured waste**, which is what the national target of a 50% cut is measured against, and the stage split decides what a waste-reduction policy can achieve and what can be recycled.

## Consumer loss by food group: two independent lines agree (2026-10-29)

The ABS publishes *Apparent Consumption of Selected Foodstuffs* (experimental, 2023-24 release; retail-sector sales in tonnes by AUSNUT food group for 2018-19 to 2023-24, `abs_apparent_consumption_2018_24.csv`), the product-weight supply that was missing. It leaves out food service, markets and some greengrocers. Two ways of asking which foods Australians waste, per cent of the food bought:

| Food | Model (US) | FIAL Table 5 (scaled to the baseline) over ABS sales | Bin audit over ABS sales |
|---|---|---|---|
| Red meat | 21 | 14 | 15 (meat, poultry and fish) |
| Poultry | 28 | 21 | 15 (as above) |
| Fruit | 25 | 26 | 38 |
| Vegetables | 17 to 30 | 39 | 30 |
| Bread, cereals | 20 to 23 | 12.5 | 34 |
| Dairy | 20 to 24 | 21 | (not used: liquids go down the drain) |

The bin audit is the Burnside (South Australia) kerbside audit of 2022 (`bin_audit_burnside_2022.csv`, Fight Food Waste CRC, University of Adelaide and Rawtec): 175 households with three bins each, food weighed by type, 3.56 kg of food a household a week, 27% not assignable to a type (shared out in proportion). It is the only direct measurement of household waste by food type found; the NSW EPA 2023 bin-audit analysis and the ACT 2024 audit do not report food types. The two lines disagree on vegetables and cereals (the ABS sales undercount fresh vegetables bought outside supermarkets, which would inflate FIAL's 39%) and agree on the finding that matters: **meat is wasted at about half the rate of fruit and vegetables, not at the model's equal rate**, and the capacity effect of the group pattern is the same (+11.0% and +11.3%).

Limits: one council (Burnside is an Adelaide suburb) and kerbside bins only, so sewer disposal, home compost and pet feed are missed; inedible parts are included (a bone is waste); the denominators are household purchases, while the model's consumer stage includes hospitality and institutions. A national set of audits by food type (the CRC study in ACT and NSW sorted 13 categories, `endfoodwaste.com.au/wp-content/uploads/2023/11/kerbside_bin_audits.pdf`, but its results are in figures that were not readable as text) would replace this.

## Not done

* A national set of household audits by food type, and the consumer loss of hospitality and institutions by food type (nothing found). Recorded in `DISCUSSION.md` row 18.
* Primary-to-retail factors for fruit and vegetables (4 to 10% in the model, 4.4% FIAL distribution plus FAO's post-harvest 4%): not enough to distinguish from the model's values.
* Whether the 12% slider should scale retail and consumer losses together (it does, as in the thesis).

## In the comparison grid

Australia, `results/comparison_cells.csv` and `method_effects.csv`: alone, the module adds 4.67 million (2011 data) and 5.26 million (2025 data) to the published method's short term and nothing in the long term. The improved cells are now **2011 36.81 and 2025 43.45 million short term** (33.31 and 39.52 corrected); long term 12.56 and 14.85 (15.35 and 15.92 corrected). The improvements as a whole (reserve, recycling, loss factors) now add 3.5 million (2011) and 3.9 million (2025) in the short term and remove 2.8 and 1.1 million in the long term.
