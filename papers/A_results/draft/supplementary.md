# Paper A supplementary information

The sections below hold detail moved from the main text to keep it under 8,000 words (decision 92). Each section names the main-text section it supports; the main text keeps the essential finding and a pointer. Release names, yield bases and flags follow the main-text rules.

Table S1. The settings of both presets in both data years, Australia, corrected releases (2011-fixed-3, 2025-fixed). Built from the settings columns of `results/2011-fixed-3.csv` and `results/2025-fixed.csv` (zone 1). The other long-term settings (activity level, the three fibre settings, timber, infrastructure area and the reserve) are those of Table 5; they are not columns of the results files.

| Setting | 2011 short term | 2011 long term | 2025 short term | 2025 long term |
|---|---|---|---|---|
| Weather allowance, return period (years) | 1 | 100 | 1 | 100 |
| Meat and eggs, share of the diet | 0.13 | 0.075 | 0.12 | 0.075 |
| Red meat, share of meat | 0.64 | 0.5 | 0.578 | 0.5 |
| Avoidable waste | 0.12 | 0 | 0.12 | 0 |
| Recycling of food waste | 0 | 1 | 0 | 1 |
| Organic farming share | 0.02 | 1 | 0.07 | 1 |
| Liquid fuel (litres a person) | 2,520 | 253 | 2,360 | 210 |
| Biofuel share | 0.005 | 1 | 0.0023 | 1 |

## S1. Regional detail for sections 3 and 4

Swan, which holds Perth, is the clearest boundary case of section 3. Its short-term capacity falls from 170 thousand to 6 thousand while its population rises from 1.72 to 2.27 million (`2011-fixed-3` to `2025-fixed`).

Elsewhere on the coast the picture is mixed: Wet Tropics, Mackay Whitsunday, North Tasmania and Corangamite flip in the short term, while South Coast WA, Eyre Peninsula and Glenelg Hopkins are under capacity in both years in the short term.

The regional decomposition of section 4 (Figure 3) is on the corrected releases (`2011-fixed` to `2025-fixed`) and on the forward walk. In Central West NSW, Lachlan and Namoi most of the short-term gain is livestock: in Central West NSW livestock added 356,807 people to a capacity that rose from 1,333,553 to 1,798,009. Elsewhere inland the share differs: livestock carried 21% of the short-term gain in Murrumbidgee-ACT, and in the Murray it took 97,458 people off a gain of 153,025. In Swan the forward walk gives the land layer -167,976 against a 2011 capacity of 170,101, the boundary case of section 3, and the reverse walk -1,120,638. In Fitzroy consumption took 62,789 and the red meat mix 38,290 off short-term capacity, and in the long term crop yields added 34,818 there against 658 from livestock.

**The order of the layers.** Across the 53 regions the largest layer on the average of all orderings is land in 26 regions and livestock in 25 in the short term (consumption and crop yields in one each), and crop yields in 19, land in 17 and livestock in 16 in the long term (fuel in one). With land and livestock as one layer, that layer is largest in 42 regions in the short term and 31 in the long term. The forward walk names a different largest layer from the average in 7 regions in the short term and 2 in the long term, and the reverse walk in 3 and 1. Infrastructure land moves capacity only in Northern and Yorke.

**The land and livestock overlap: Avon.** The land layer cuts Avon's pasture from 24,368 to 15,309 km2, a ratio of 1.592. The 2025 livestock yields divide output by the 2020-21 grazing area of the land layer plus hay, 1,594,996 ha, where the 2011 yields divided by 2,537,931 ha, the mean of the archive years 2006 to 2010: a ratio of 1.591. Avon's milk yield rises from 32.75 to 67.54 g/m2, 2.062 times, which is 1.591 times from the area and 1.296 times from output and the dairy share. Pasture times milk yield therefore changes only 1.296 times, and the area cancels. In the forward walk the land layer takes 134,628 people off Avon's short-term capacity and the livestock layer returns 125,905, together -8,723; in the long term the two are -68,404 and +52,121, together -16,283. For Australia the two ratios are 1.097 (pasture of the land layer, 3,639,794 to 3,318,689 km2) and 1.104 (the livestock denominator). Where feed grain is part of a yield's land (meat) or cropland binds, the cancelling is only partial.

## S2. The partition: boundary detail and the best contiguous split (section 5)

All figures in this section are on the 2025 corrected release (`2025-fixed`) and the state-yield basis unless named otherwise.

As shares of national capacity, the regions of New South Wales summed to 17.6% against 25.3% for its SA4s. In South Australia the figures were 1.2% against 4.8%, and in Western Australia 2.0% against 5.1%. The other states were about equal on the two partitions.

SA4 406 joins the arid country of SA Arid Lands with the cropland of the Eyre Peninsula and had a capacity of 1.7 million. The two regions apart had 41 thousand and 132 thousand. In Western Australia the Rangelands region, with 646,000 km2 of pasture and 937 km2 of cropland, had a capacity of 241 thousand. SA4 511 had 1.5 million. Units with more than 1,000 km2 of pasture and cropland under 2% of that pasture held 71% of the nation's pasture among the regions (8 units), 72% among the SA3s (18) and 51% among the SA4s (3). The land the partitions left unused rose from 1.96 million km2 for the nation to 3.67 million for the SA4s and 4.50 million for the regions.

Capacity was exactly proportional to land: 0.5, 0.1 and 0.01 times the national land gave 100.0% of the same fraction of national capacity. A split in which every unit had the national land mix would therefore lose nothing. On the national yield vector, random groupings of the SA2s into 53 groups kept 68 to 81% of national capacity, against 33% for the 53 regions (52 NRM regions and the Northern Territory) as drawn. These are spreads across five draws, not uncertainty ranges. The SA4s, at 54%, were slightly worse than random groupings of their number (56 to 69%), and the SA3s, at 35%, were about equal to random (34 to 44%). The best contiguous split found at 53 regions was searched with each region capped at 650,000 km2 of land (Supplementary Figure S1).

Foodshed reach varies with diet and land type (Kurtz et al. 2020).

[Supplementary Figure S1: the best contiguous split found at 53 regions with each region capped at 650,000 km2 of land, 2025 corrected release (2025-fixed), short term; from `analysis/regionalise_2025/summary.csv` and `analysis/regionalise_2025/ideal_K53_cap650k.png`, drawn by `map_regions.py`]

**The two yield bases.** The main text reports the scale curve on the state-yield basis, the conservative bound: every unit takes the yields, climate zone and settings of its state. The other bound lets each unit keep its own yields; it is generous for units that span several yield zones, and the truth for a unit lies between the two. Table S6 gives both.

Table S6. Sum of capacities as a share of national capacity, by level, corrected releases (2011-fixed, 2025-fixed), short and long term, on both yield bases. Built from `results/scale_curve.csv` (column `share_of_national`). For the 2011 cells the SA4, SA3 and SA2 shares are against a reference on 2020-21 land (row "Australia (SA land)"), not the 2011 zones.

| Level | Units | State-yield basis, 2011 short | State-yield basis, 2011 long | State-yield basis, 2025 short | State-yield basis, 2025 long | Own-yield basis, 2011 short | Own-yield basis, 2011 long | Own-yield basis, 2025 short | Own-yield basis, 2025 long |
|---|---|---|---|---|---|---|---|---|---|
| Australia | 1 | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 100% |
| State | 7 | 77% | 44% | 75% | 49% | 77% | 44% | 75% | 49% |
| NRM region | 53 | 44% | 20% | 44% | 23% | 63% | 33% | 63% | 38% |
| SA4 | 89 | 60% | 32% | 58% | 35% | 82% | 43% | 80% | 52% |
| SA3 | 336 | 46% | 23% | 44% | 24% | 64% | 35% | 64% | 40% |
| SA2 | 2,450 | 40% | 18% | 37% | 20% | 54% | 28% | 54% | 32% |

## S3. Named scenarios (section 8)

Table S2 gives every named scenario on the 2025 corrected release (2025-fixed), against a reference of 41.5 million in the short term and 15.6 million in the long term. Recycling and the two fuel allowances moved either term by less than 2%. The 340-litre fuel allowance took 1.8% off the long term on the corrected release and 18.8% on the improved release (2025-improved), a method effect that has not been explained.

Table S2. Named scenarios, change in national capacity on the reference, 2025 corrected release (2025-fixed; grain stores with the resilience tables of 2025-store-1 and 2025-store-2). Built from `analysis/paper_a/scenarios_by_region.csv` (rows with `reference_release` 2025-fixed, column `change on reference`). The fuel scenarios set the long-term fuel only (`scenarios/scenarios.json`); Table S5 gives the 156-litre measure set in both terms.

| Scenario | Short term | Long term |
|---|---|---|
| Reference (national capacity, million) | 41.5 | 15.6 |
| Field-crop yields 12% lower | -0.09% | -0.28% |
| Field-crop yields 24% lower | -0.2% | -0.65% |
| Waste at 6% | +16.4% | -8.15% |
| No avoidable waste | +33.21% | 0% |
| No recycling | 0% | -1.21% |
| Half recycling | +1.7% | -0.28% |
| Liquid fuel 156 litres a person | 0% | +0.78% |
| Liquid fuel 340 litres a person | 0% | -1.83% |
| Grain store of one year | 0% | +48.45% |
| Grain store of two years | 0% | +64.47% |

## S4. Ranges and method effects by region (section 9)

**The ranges.** The regional ranges that test the status flips come from 1,000 Latin hypercube draws of 13 sampled choices. Twelve of them vary in the corrected and published 2025 releases (2025-fixed and 2025-mirror); the thirteenth, the long-term feeding benchmark, has no effect in those releases and is drawn in the improved release (2025-improved), with a negligible national effect. On 2025-fixed the meat window alone explains 81% of the variance of the short-term national capacity and 36% of the long-term on these 13 choices. The national range of the main text comes from 2,000 draws of 19 choices: the 13, with six added. The six are avoidable waste (uniform from 12% to 14%), the retail and consumer loss factors (a weight from 0 to 1 between the thesis's US factors and Australian factors), the source of the land areas (ABS holdings or the ABARES land-use raster, with equal chances), the meat calibration (a weight from 0 to 1 between the ABS tables as published and the archive's 2010 level), the energy requirement per person (a food amount from 1.000 to 1.286 times the sedentary requirement, which is physical activity levels of 1.4 to 1.8 within a range of 1.2 to 2.2 in the source) and the crop-yield trend window (between the field-crop factors of 2022-25 and of 2016-21). Eighteen of the 19 vary, because the long-term feeding benchmark is fixed on this release. A definition changes what the number means (what is counted, the unit of self-sufficiency, the time frame, the diet standard, the weather allowed for) and is reported separately; a setting is a value within one meaning and is drawn. Where no source gives an end or a weight, it is the author's judgement.

Table S7. The Monte Carlo range of national capacity, 2025 corrected release (2025-fixed), millions of people: 5th to 95th percentile, with the factor between them, and lowest to highest draw. Built from `results/ranges_2025-fixed.csv`, `results/ranges_2025-fixed_wide.csv` and `results/ranges_2025-fixed_herdcycle.csv`. The release's base is 41.5 million (short term) and 15.6 million (long term).

| Draws | Short term, 5th to 95th (factor) | Short term, lowest to highest (factor) | Long term, 5th to 95th (factor) | Long term, lowest to highest (factor) |
|---|---|---|---|---|
| 13 choices, 1,000 draws (three meat windows) | 36.3 to 45.8 (1.26) | 34.6 to 47.7 (1.38) | 13.4 to 16.5 (1.23) | 12.9 to 16.9 (1.31) |
| 19 choices, 2,000 draws | 31.1 to 49.2 (1.58) | 26.2 to 58.1 (2.22) | 13.3 to 18.8 (1.41) | 12.4 to 19.9 (1.60) |
| 19 choices, holdings land only (1,000 draws) | 29.8 to 43.1 (1.45) | | 13.0 to 16.2 (1.24) | |
| 13 choices, four full-cycle meat windows (1,000 draws) | 39.4 to 43.8 | | 13.9 to 16.2 | |

The 19-choice range has a median of 39.0 million in the short term and 15.8 million in the long term, so the base is not central: several added choices have the release at one end of their range. The widening comes from judged choices: with the land source held to ABS holdings, the short-term range is 29.8 to 43.1 million. The 5th to 95th factor of 1.58 is below the spans of the diet standard (2.14), the weather allowance (2.19), exports (2.41 to 6.36), the time frame (2.66) and the unit of self-sufficiency (2.67), and above those of avoidable waste (1.33) and the land available (1.09), as tested in the companion methods paper. The four full-cycle windows are 8, 10, 15 and 20 years ending 2024-25; with the three-year windows out, the window choice hardly matters and the diet shares carry the short-term range.

Table S8. Share of the variance of national capacity carried by each choice alone (first order) and with its interactions (total order), 2025 corrected release (2025-fixed), 19 choices; Saltelli (2010) and Jansen (1999) estimators over 42,000 runs. Built from `analysis/sensitivity_2025/sobol_2025-fixed.csv`. Choices not listed carry under 1% in both terms.

| Choice | Short term, first order | Short term, total order | Long term, first order | Long term, total order |
|---|---|---|---|---|
| Source of the land areas | 32% | 33% | 58% | 56% |
| Energy requirement per person | 27% | 25% | 0% | 0% |
| Window of herd and meat data | 24% | 23% | 14% | 14% |
| Retail and consumer loss factors | 6% | 6% | 0% | 0% |
| Red-meat share of the diet | 4% | 5% | 0% | 0% |
| Meat calibration | 3% | 3% | 1% | 1% |
| Avoidable waste | 1% | 1% | 0% | 0% |
| Resilience table | 0% | 0% | 20% | 20% |
| Organic yield factor | 0% | 0% | 4% | 4% |

The choices act almost separately: interactions carry about 3% of the variance. On the four full-cycle meat windows the short-term shares change: the red-meat share of the diet 85%, the meat-and-egg share 16% and the window 1% (the shares add to 106% at the noise floor of the estimate); in the long term the resilience table carries 81%, the organic yield factor 14% and the window 2%.

**The shocked ranges.** Capacity in a bad year is the average-year capacity times the weather factor of the return period, so each draw's shocked capacity is its average-year capacity times the factor, and the national range scales exactly.

Table S9. National short-term capacity in a 1-in-10 and a 1-in-20 year, 2025 corrected release (2025-fixed), millions of people, 5th to 95th percentile, against a population of 27.6 million; capacity over population in brackets. The 19-choice range is the headline range of section 8.1; the 13-choice range and the four full-cycle meat windows are labelled alternatives. Built from `analysis/paper_a/shocks_ranges_wide.csv` (19 choices) and `analysis/paper_a/shocks_ranges.csv` (the others).

| Return period | Factor | Central | 19-choice range | 13-choice range | Four full-cycle meat windows |
|---|---|---|---|---|---|
| 1 in 10 | 0.742 | 30.8 | 23.1 to 36.5 (0.84 to 1.32) | 27.0 to 34.0 (0.98 to 1.23) | 29.2 to 32.5 (1.06 to 1.18) |
| 1 in 20 | 0.634 | 26.3 | 19.7 to 31.2 (0.72 to 1.13) | 23.0 to 29.0 (0.83 to 1.05) | 25.0 to 27.8 (0.90 to 1.01) |

On the 19-choice range 27.6 million lies inside both ranges: 37% of the draws are below it at 1 in 10 and 78% at 1 in 20, against 0.45% in an average year. It also lies inside both 13-choice ranges. On the four full-cycle windows every draw at 1 in 10 is above 27.6 million, and at 1 in 20 about 92% of draws are below it. The regional counts that follow are on the 13-choice zone ranges, because the 19-choice draws are national and state only. By region, at 1 in 10 there are 21 regions over capacity at the central figure, 21 at the 95th-percentile capacity and 22 at the 5th, and North Tasmania is the one region whose population lies inside its range; at 1 in 20, 24 regions are over capacity at every point of the range and none lies inside. In an average year the regions inside their ranges are Corangamite, Wet Tropics and Rangelands. In 2011 four regions tip over capacity at 1 in 20.

**The weather factor.** The drought allowance is the resilience table of the model. For Australia and each state, each season's yield is the unweighted mean of the wheat, oat and barley yields in tonnes per hectare, from the ABS Historic Agricultural Commodities workbook (1860 to 2022) and the ABS 2022-23 to 2024-25 cubes: 153 seasons, those ending 1861, 1866 and 1871 and then every season from 1875-76 to 2024-25. Each season is divided by the mean of the ten observations from five before to four after it, held at the first or last ten at the ends. The 153 ratios are ranked from the worst, and rank k is read as a one-in-(n+1)/k year; the table takes anchors at 1, 3, 5, 10, 20, 30, 50 and 150 years and interpolates in a straight line between them. For Australia the 1-in-10 factor, 0.742, is the 15th-worst ratio (the season ending 1947), the 1-in-20 factor, 0.634, the 8th-worst (1896), and the 1-in-100 factor, 0.456, is the midpoint of the 50-year anchor (the 3rd-worst, 1941, 0.552) and the 150-year anchor (the worst, 1915, 0.359). The recent droughts appear as the seasons ending 2007 (0.567, the 4th-worst), 2003 (0.578) and 2020 (0.762, the 16th-worst). The model applies one factor to every yield of a zone, crops, pasture-fed and grain-fed animal products, fish, honey and timber alike. The 2011 releases use the thesis table (0.599 at 20 years).

Table S10. National capacity with the weather factor on all output (the model) and on crops alone, 2025 corrected release (2025-fixed), millions of people. Crop only: plant rows and the grain-fed animal rows (chicken, duck, turkey, eggs and pig meat, whose yield per hectare is a grain yield over a feed conversion ratio) take the factor; pasture-fed output (sheep meat, wool, milk, cattle meat, goat and sheep milk) and fish, honey and timber stay at the average-year level. Plant rows only: grain-fed animals also stay at the average-year level. Built from `analysis/resilience_2025/drought_bounds.csv`.

| Setting | Return period | Factor | Average year | Factor on all output | Crop only | Plant rows only |
|---|---|---|---|---|---|---|
| Short term | 1 in 10 | 0.742 | 41.50 | 30.81 | 41.19 | 41.32 |
| Short term | 1 in 20 | 0.634 | 41.50 | 26.32 | 40.99 | 41.20 |
| Short term | 1 in 100 | 0.456 | 41.50 | 18.92 | 40.45 | 40.88 |
| Long term | 1 in 100 | 0.456 | 34.27 | 15.62 | 24.68 | 24.68 |

Short-term capacity is bound by pasture-fed meat and dairy, so the crop-only bound barely moves it (-0.8% at 1 in 10, -2.5% at 1 in 100) and the short-term drought effect is the factor applied to pasture-fed output: the pasture-fed rows alone carry about 97% of the drop at 1 in 10. The long term is limited by cropping, and the crop-only bound takes 28% off the average year at 1 in 100 against 54% with the factor on everything. The two bounds bracket a drought that hits crops at the cereal factor: pasture-fed output does fall in a drought, by an amount the records do not give. The one observed check is the single-year series of the 2025-organic release as built (crops, herds and meat of each year from 2016-17 to 2024-25, no 2021-22): the drought years 2018-19 and 2019-20 give 48.8 and 48.3 million, near the median of 48.5, and the year after them, 2020-21, is the lowest at 43.5 million (0.90 of the median) as the herd rebuilt. That lag is not in the cereal factor, and eight years cannot name a return period. Every single year is above the 2011 value of 40.5 million used there. These single-year figures are unverified (the second route is blocked).

**The corrections by region.** Each method choice was applied alone to the published-method release on 2025 data (2025-mirror). The beef carcase correction (USDA undated; AUS-MEAT 2005) acts in the beef and cropping regions: Wet Tropics -21.5%, Lower Murray Darling -16.4% and Border Rivers-Maranoa-Balonne -15.4%. The biodiesel correction (Geoscience Australia and ABARE 2010) reaches +95.8% in Burdekin and +83.5% in South Tasmania. In the short term it moves the national figure by +0.1%.

**The improvements by region.** Dairy on land that can carry it has regional effects from -27.3% to +22.1% in the short term. It lowers SA Arid Lands (-27.3%) and Southern Gulf (-15.5%). It raises Wet Tropics (+22.1%), Rangelands (+22.0%) and Lower Murray Darling (+22.0%). In the long term it raises Rangelands by 53%. Australian loss factors raise nearly every region in the short term: +11.2% nationally and +0.8% to +22.6% by region, most in Swan. Reserve pro rata and recycling by stage act mainly in the long term, and they lower it: -5.8% and -9.7% nationally, against -1.1% and +0.1% in the short term. In the long term reserve pro rata takes up to 29.1% off a region (Condamine), and recycling by stage up to 18.2% (Southern Gulf). Beef output by state redistributes without changing the national figure: 0% nationally and -7.4% to +9.9% by region.

**Status under each tier.** The six southern and western regions that change long-term status between the corrected and improved releases are Mallee, Kangaroo Island, SA Arid Lands, SA Murray Darling Basin, South East SA and South West WA (Table S4).

Table S3. The effect of each method module applied alone, 2025 data, as a percentage of the published-method capacity (base release 2025-mirror): nation, with the regional minimum to maximum in brackets. Built from `analysis/paper_a/method_effects_summary.csv`.

| Module | Tier | Short term | Long term |
|---|---|---|---|
| Beef carcase yield | correction | -16.0 (-21.5 to 0.0) | 0.0 (-7.7 to 0.0) |
| Biodiesel yield | correction | +0.1 (0.0 to +6.9) | +20.7 (+3.4 to +97.9) |
| Australian loss factors | improvement | +11.2 (+0.8 to +22.6) | 0.0 (0.0 to 0.0) |
| Dairy on land that can carry it | improvement | +20.2 (-27.3 to +22.1) | +3.0 (-12.4 to +53.1) |
| Beef output by state | improvement | 0.0 (-7.4 to +9.9) | 0.0 (-5.0 to +3.9) |
| Reserve pro rata | improvement | -1.1 (-5.4 to 0.0) | -5.8 (-29.1 to 0.0) |
| Recycling by stage | improvement | +0.1 (0.0 to +4.3) | -9.7 (-18.2 to -1.5) |
| Organic ruminant factor | improvement | 0.0 (0.0 to 0.0) | 0.0 (0.0 to +7.6) |

Table S4. Regions over capacity (of 53) in 2025 under each method tier, and the regions that change status between the corrected and improved tiers. Releases 2025-mirror (published), 2025-fixed (corrected) and 2025-improved (improved). Built from `analysis/paper_a/method_status.csv` (2025 rows). On 2011 data the long-term counts are 35 on the corrected tier (2011-fixed-3) and 36 on the improved tier (2011-improved-3); the published tier was not rerun on the ABS populations.

| 2025 | Published | Corrected | Improved | Regions that change status, corrected to improved |
|---|---|---|---|---|
| Short term | 15 | 16 | 15 | Corangamite |
| Long term | 36 | 32 | 36 | Mallee, Kangaroo Island, SA Arid Lands, SA Murray Darling Basin, South East SA, South West WA |

## S5. Four regions in depth (section 10)

All figures except the method effects are on the corrected releases (2011-fixed-3 and 2025-fixed) and on each region's own yields (Table 7). The 2011 populations are the ABS figures of 2011-fixed-3.

**Hawkesbury-Nepean-Sydney.** The region is over capacity in both years and both terms. Its short-term capacity fell from 66,198 to 46,572 people while its population grew from 4,394,612 to 5,401,609. Its long-term capacity is 7,186 in 2011 and 6,106 in 2025. Even the 95th percentile of its 2025 short-term capacity is 48,520 people. The fall in capacity carries the land-definition flag. With only the 2025 land layer swapped in, capacity is 0.491 of the 2011 figure, just below the rule's lower bound of 0.5. Cropping land is 389 km2 on the 2011 layer and 191 km2 on the 2025 layer, on an unchanged boundary. The change is therefore not read as a change in what the land can feed. James and O'Neill (2016, p. 183) found Sydney Basin farm data too uncertain to show a trend, with error margins above 25% in many ABS figures.

**The Murray with Murrumbidgee-ACT.** The Murray region is under capacity in both years and both terms. Its short-term capacity rose from 752,498 to 905,523 against a population of 105,924 to 121,808. Murrumbidgee-ACT, which holds Canberra, is under capacity in an average year: its 2025 population is 0.482 times its capacity. It is over capacity in the long term (2.431 times) and at a 1-in-100 drought (1.604 times). Its short-term capacity rose from 1,185,593 to 1,533,929 while its population grew from 597,750 to 738,895. In both regions the largest short-term method effects are measured on the published base (2025-mirror, section 9): dairy on good land (+17.8% and +17.9%) and the beef carcase correction (-15.0%). The Basin accounts for about 40% of national farm output (Wittwer and Waschik 2021, p. 919). Its median projected streamflow is about 20% lower under 2 °C of global warming (Prosser et al. 2021, p. 4). In northern Victoria, raw milk output fell by 1.3 billion litres between 2001-02 and 2009-10 (Sysak and Beilin 2017, p. 416). The model carries no water limit, so none of this enters the capacities (section 12).

**Avon.** Avon is a cropping region under capacity throughout. Its short-term capacity rose from 971,132 to 1,080,065 against a population of 60,913 to 69,727. In the long term it is among the strongest regions: its 2025 population is 0.14 times its long-term capacity. At a 1-in-100 drought its 2025 short-term capacity is 508,513 people. The model scales its yields by Western Australia's worst-year factor. Hughes and Lawson (2017, p. 189) found a larger climate effect on cropping productivity in Western Australia than nationally: -7.63% against -4.71% for all cropping farms, 2000-01 to 2014-15 (their Table 8.3).

**SA Arid Lands beside the Eyre Peninsula.** SA Arid Lands moved from over to under capacity in the short term. Its capacity rose from 2,164 to 28,609 while its population fell from 10,613 to 8,049, both years on the same ABS estimated resident population and allocation (the thesis's 31,361 had no recorded source). The land layer alone raises its capacity 6.5 times, so the capacity change is a matter of definition and the flip is not read as a change on the ground. In the long term its 2025 status is not robust to the range: 7,194 to 9,031 people against a population of 8,049. Its cropping neighbour, the Eyre Peninsula, carries no flag. There, capacity rose from 217,967 to 384,476 against a population of 57,595 to 59,255, and the region is under capacity in both years and both terms.

## S6. Measures with no read source beyond the model, and other detail (section 11)

Each measure was applied alone to the corrected 2025 release (2025-fixed) unless Table S5 names another release.

**Field crops, irrigation and cropland.** Field-crop yields 10% and 20% higher raise the short term by 0.1% and the long term by 0.2% and 0.3%. Horticulture yields 10% higher leave the short term unchanged and raise the long term by 0.2%. All yields 10% higher raise both terms by 10.0%. An irrigated share of cropland of 0.02 or 0.05, against a base of 0.007, raises both terms by 0.7% or 2.4%. Cropland 25% larger, taken from pasture, changes neither term. In the model, cropland can carry pasture-fed products but pasture cannot carry crops, so capacity is the same for any cropland share from 10% to 99% of the combined area (section 6).

**Diet, waste and fuel.** A meat-and-egg share of 7.5% gives 48.2 million (+16.2%) in the short term. No avoidable waste raises the short term to 55.3 million (+33.2%), and full recycling of food waste adds 2.2%. Liquid fuel of 156 litres a person, set in both terms, moves the short term by +0.1% and the long term by +0.8%.

**The grain store.** A one-year store for domestic use is about 11.5 Mt: 3.1 Mt for direct use at 112 kg a person, and 8.4 Mt for the feed grain embodied in meat at 303 kg a person.

**The regions as a pool.** On each zone's own yields and on 2025-fixed, the national capacity is 1.60 times the sum of the regional capacities in an average year. The factor is 1.82 at a 1-in-10 year. In the long term it is 2.60, and 3.00 on 2011 data (2011-fixed). The regions' pasture and cropland complement each other. In an average year the regions over capacity are short by 20.7 million people-equivalents, and the regions under capacity have 19.1 million to spare. At a 1-in-10 year the shortfall is 21.5 million and the spare 10.8 million. Northern supply chains run over 1000 km on roads cut by seasonal flooding (Higgins et al. 2018b, p. 341). Few studies follow shocks along supply chains (Davis et al. 2020).

**Measures the model cannot carry.** If meat output fell by the national capacity factor, it would be about 3.45 Mt at a 1-in-10 year and 2.95 Mt at a 1-in-20 year; that assumption is untested. Fish imports, 593 thousand tonnes, are about as large as the food use of fish, 641 thousand tonnes. In the commodity balance fish is the item that runs out first, at 12 to 17 million people. Pulses, 4.4 Mt produced and mostly exported, keep for a long time. The herd is also a store: the single-year capacity runs from 43.5 to 55.4 million across 2016 to 2025 with the herd cycle, on the 2025-organic release as built, not on 2025-fixed. The national 100-year worst-year factor, 0.46 of trend, is milder than those of New South Wales (0.30), Victoria (0.22), Queensland (0.35) and South Australia (0.35). It is not milder than those of Western Australia (0.47) or Tasmania (0.67). Spreading production across states therefore lowers national variability. In the long term 94% of the population lives in regions over capacity (2025-fixed; section 7). Settlement policy changes where food must travel, not the national capacity. Aquaculture, seasonal forecasting, household and community stocks, and finance and insurance are further measures the model cannot carry.

**Caution.** The drought, store and livestock results rest on one cereal weather factor applied to every yield.

Table S5. The measures one at a time, Australia, 2025: capacity in millions of people and the change on each release's own reference. Built from `analysis/paper_a/measures.csv` (release named in each row; the grain stores on 2025-fixed use the resilience tables of 2025-store-1 and 2025-store-2). The 156-litre row sets the fuel in both terms, so it moves the short term (+0.1%); the named scenario of Table S2 sets it in the long term only (0%). Both are right for their settings, and in the long term they agree: +0.78% in Table S2 is +0.8% at one decimal.

| Measure | Release | Short term | Long term |
|---|---|---|---|
| Reference | 2025-fixed | 41.5 | 15.6 |
| Field-crop yields +10% | 2025-fixed | 41.5 (+0.1%) | 15.7 (+0.2%) |
| Field-crop yields +20% | 2025-fixed | 41.5 (+0.1%) | 15.7 (+0.3%) |
| Horticulture yields +10% | 2025-fixed | 41.5 (0.0%) | 15.6 (+0.2%) |
| Livestock output +10% | 2025-fixed | 45.5 (+9.7%) | 17.1 (+9.4%) |
| Livestock output +20% | 2025-fixed | 49.6 (+19.4%) | 18.6 (+18.8%) |
| All yields +10% | 2025-fixed | 45.7 (+10.0%) | 17.2 (+10.0%) |
| Drought-proofing: the worst year loses half as much | 2025-fixed | 41.5 (0.0%) | 24.9 (+59.7%) |
| Irrigated share of cropland 0.02 (base 0.007) | 2025-fixed | 41.8 (+0.7%) | 15.7 (+0.7%) |
| Irrigated share of cropland 0.05 (base 0.007) | 2025-fixed | 42.5 (+2.4%) | 16.0 (+2.4%) |
| Avoidable waste 6% | 2025-fixed | 48.3 (+16.4%) | 14.3 (-8.2%) |
| No avoidable waste | 2025-fixed | 55.3 (+33.2%) | 15.6 (0.0%) |
| Full recycling of food waste | 2025-fixed | 42.4 (+2.2%) | 15.6 (0.0%) |
| Cropland +25% from pasture | 2025-fixed | 41.5 (0.0%) | 15.6 (0.0%) |
| Cropland doubled from non-agricultural land | 2025-fixed | 45.1 (+8.7%) | 17.0 (+8.7%) |
| Meat and eggs 7.5% of the diet | 2025-fixed | 48.2 (+16.2%) | 15.6 (0.0%) |
| Meat and eggs 5% of the diet | 2025-fixed | 76.8 (+85.0%) | 19.6 (+25.7%) |
| Red meat 30% of meat | 2025-fixed | 64.6 (+55.6%) | 18.5 (+18.6%) |
| Liquid fuel 156 litres a person | 2025-fixed | 41.5 (+0.1%) | 15.7 (+0.8%) |
| Grain store of one year | 2025-fixed (store table of 2025-store-1) | 41.5 (0.0%) | 23.2 (+48.4%) |
| Grain store of two years | 2025-fixed (store table of 2025-store-2) | 41.5 (0.0%) | 25.7 (+64.5%) |

## S7. Diet and gardens under forced local self-sufficiency (section 12)

On 2025-fixed and the state-yield basis, the sum of SA2 capacities is 37% of the national capacity on the base diet. It is 33% on a 2.5% meat-and-egg diet and 45% with no meat or eggs, each against the national capacity on the same diet. Against the national figure on the base diet, the SA2 sum on the 2.5% diet reaches 95%. Swaps within food groups raise the national capacity by about three fifths (+62%), from 53.6 to 86.9 million, on the improved release (2025-improved). Gardens add little: covering all fruit and vegetable land from gardens would free only about 7% of the cropland a person needs (2025-fixed).

## S8. The model, the data and the failure probability (sections 2 and 8)

**The model.** The model is the author's workbook (sheets Base, Yield, Diet, Recycle, Settings and resilience), set out in a doctoral thesis (Lane 2014) and three papers (Lane et al. 2014, 2015; Lane 2017). For each of its 60 zones it holds land areas (cropping, pasture, reserve, infrastructure and non-agricultural land), a population, yields in g/m2 for 135 rows (crops, animal products, fish, honey and timber) and the settings of Table S1. Capacity is the number of people whose diet the zone's own land can supply, once land for fuel, fibre, timber, infrastructure and a reserve is set aside. A diet needs cropland and pasture in nearly fixed proportion, so the land type that runs short sets capacity (section 6). Every yield row is the zone yield times one weather factor, so capacity is linear in the yields.

**The data.** Table S11 names the source of each input in both years. The 2011 and 2025 populations are the same ABS series on the same allocation, so the two years differ by data, not by method.

Table S11. Data sources by input and year. Built from the sources register; the 2011 land windows are those of the 2011 land method.

| Input | 2011 | 2025 |
|---|---|---|
| Regional population | ABS estimated resident population at 30 June 2011 by 2021 SA2, shared among the 2011 NRM zones by residential land (class 5.4 of the ABARES land-use raster); the thesis's own figures, of unrecorded source, are not used | ABS estimated resident population at 30 June 2025, same series and allocation |
| National population row | 22,326,388, the thesis row, a published input kept as it is (the 53 regions sum to 22,336,514) | 27,608,200 |
| Cropland and pasture | ABS agricultural holdings, land mainly used for crops and total grazing, a five-year mean of 2005-06 to 2009-10 (four years for grazing) | The same two ABS items for 2020-21 (ABS Agricultural Commodities 2020-21); the ABS changed its land-use categories in 2016, so part of the national pasture fall, from 3,639,794 to 3,318,689 km2, is a change of definition |
| Reserve and total area | ABARES Catchment Scale Land Use of Australia (update December 2023, ALUM version 8, 50 m) on the 2011 NRM boundaries | The same raster and boundaries |
| Crop yields | ABS Agricultural Commodities NRM data cubes 2006-07 to 2009-10, with the thesis's adjustments | ABS NRM cubes 2016-17 to 2020-21 and ABS Data API series by SA2 for 2022-23 to 2024-25 |
| Livestock output (meat, wool, milk) | The archive years 2006 to 2010, a five-year mean, divided by each year's grazing area | ABS livestock products and Australian Agriculture 2024-25 workbooks, with wool, cattle on feed and milk series, a five-year window 2020-21 to 2024-25, divided by the 2020-21 grazing area of the land layer |
| Diet and consumption | The thesis defaults | The thesis defaults moved by the change in the FAO food balance series for Australia, mean of 2010-12 to 2021-23 |
| Liquid fuel | The thesis defaults | Australian Petroleum Statistics (extract of August 2026) and Australian Energy Statistics 2025 |
| Weather allowance | The thesis table (0.599 at 20 years) | ABS Historic Agricultural Commodities 1860 to 2022 and the ABS 2022-23 to 2024-25 cubes: 153 seasons (0.634 at 20 years) |
| Statistical areas for the scale curve | Not used | ASGS Edition 3 (2021) boundaries: SA2 (2,450 units), SA3 (336) and SA4 (89) |

**The failure probability.** At the base settings the model feeds the 2025 population of 27,608,200 when the weather factor is 27,608,200 divided by 41,503,537, which is 0.665. The table's factors for Australia are 0.742 at 10 years and 0.634 at 20 years, and it interpolates in a straight line between its anchors, so 0.665 falls at 10 + 10 x (0.742 - 0.665) / (0.742 - 0.634) = 17.1 years. The failure probability a year is the reciprocal, 5.8%, about 1 in 17. Paper B reports 5.8 to 6.1% because it also reads the capacities at 10 and 20 years (30.81 and 26.32 million) linearly in the logarithm of the return period, which gives 16.4 years and 6.1%; reading them linearly in the return period, the rule of the model's own table, gives 17.1 years and 5.8%, the figure used here, so the two papers agree and 5.8% is the lower end of Paper B's range. It rests on the cereal factor (section 8.1), the interpolation rule and the method tier.

## S9. An export-inclusive count (section 8)

Lawrence et al. (2013, p. 30) give about 22 million people fed at home and 40 million fed abroad, with no base year stated. PMSEIC (2010, p. 15) is the source of the 40 million abroad. PMSEIC's own figure is 60 million (p. 1), stated without source, and the report does not add the two. This count includes exports and the diet as eaten, so its basis differs from the model's self-sufficient capacity.
