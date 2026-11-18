# Paper A, results: Australia's carrying capacity 2011 to 2025 by region on the corrected releases

First draft, assembled 2026-11-18 from A_s01-04.md, A_s05-08.md, A_s09-12.md. Every number traces to the claims csv beside each section file; sentences marked [gate 4] in those csvs use values awaiting Murray's gate 4 approval. Not for circulation.

## Abstract

How many people can Australia's regions feed from their own land, and has that changed since 2011? The author's land-use model is brought forward from 2011 to 2025 with the method frozen. It compares capacity with population in 53 regions (52 NRM regions and the Northern Territory), splits the change by layer, sums capacity down to 2,450 SA2s and tests them against bad years, Monte Carlo ranges and method choices. National short-term capacity rose from 33.3 to 41.5 million people and the population from 22.3 to 27.6 million, so capacity stayed about 1.5 times the population. Averaged over all orderings of the data layers, livestock, consumption and the red meat mix account for the rise: consumption and the red meat mix, a diet with less beef, add 5.6 million, and land and livestock, which share one grazing area, together add 2.4 million. On a cereal-yield weather allowance, the margin is above balance in a 1-in-10 year and below it in a 1-in-20 year at the base settings, but the full Monte Carlo range at each contains the 2025 population. A 100-year self-sufficiency plan would cover 57% of the 2025 population. If every SA2 must feed itself, their capacities sum to 37% of national short-term capacity on state yields, because in the model cropland can carry pasture-fed food but pasture cannot carry crops. One at a time and free of cost, livestock output, diet and waste move short-term capacity most, and drought-proofing and grain stores long-term capacity.

## 1. Introduction

### 1.1 Australian population debate and planning

How many people Australia can feed from its own land is an old question. It returned as the population grew between 2011 and 2025. The 2023 Intergenerational Report projected 26.5 million people in 2022-23 rising to 40.5 million in 2062-63 (Treasury 2023, p. 39). The 2025 Population Statement put the population at 27.5 million in the March quarter of 2025 and forecast 41 million by 2065-66 (Centre for Population 2026, p. 1). Section 8.1 sets these projections against capacity.

Growth of 5 million over two decades "has been described as unexpected, unprecedented, and unplanned" (Davies 2024, p. 149), but "Australia's population growth is highly managed" (Davies 2024, p. 150). This paper sets capacity against each data year's own population, which rose by about 24% (section 3). Published estimates of how many people Australia can feed scatter widely, mostly because they answer different questions (Henry and Godden 1995; Foran and Poldy 2002; CSIRO and University of Queensland 2025).

### 1.3 The model, what was left open, and the questions

The model is the author's own. It was built for a doctoral thesis (Lane 2014), and its essential parameters were published (Lane et al. 2014). Lane et al. (2015) found that capacity shrinks as the unit of self-sufficiency shrinks from the nation to states and regions. Lane (2017) set a short and a long time frame side by side, and a planning study has applied it to scenarios for settling northern Australia (Bolleter 2018, p. 123). The earlier papers gave one data year and, for the long term, one national and regional picture; work citing them was not checked.

The paper asks five questions. First, which regions moved between under and over capacity, and how much of the change in capacity is land, yields, livestock and diet, given that population changes status, not capacity? Second, what would a 100-year self-sufficiency plan ask of each region, and how has that changed? Third, how do the regional results hold under shocks? Fourth, how sure are the regional results? Fifth, how much of the national margin survives as the unit of self-sufficiency shrinks to the smallest statistical areas, and has that changed since 2011? Sections 3 and 4 answer the first, 7 the second, 8 the third, 9 the fourth, and 5 and 6 the fifth. A companion methods paper compares the published estimates and carries the choice of method.

### 1.4 Food security in Australian planning and policy

Food security and regional self-sufficiency appear in Australian planning and policy only in patches. The government's expert panel framed food security at the national scale (PMSEIC 2010). Of 102 food-related policy documents from Queensland, Western Australia, Victoria and the federal government, nine set food security as a specific goal, and none of the nine was federal or from Queensland (Summerhayes and Baker 2026b, pp. 963-964). Of 25 senior planners and policymakers interviewed, 21 agreed that food is a stranger to urban planning (Summerhayes and Baker 2026a, p. 534). The federal committee's 2023 inquiry made a National Food Plan its key recommendation (House of Representatives Standing Committee on Agriculture 2023, p. iii). A regional capacity result could inform such a plan: which regions could feed their own people from their own land.

### 1.5 Observed drought and climate effects on Australian farming

Since 1990 the climate has lowered the simulated water-limited yield potential of Australian wheat, by 27% to 2015 (Hochman et al. 2017, p. 2071). National actual yields did not decline over the same period (Hochman et al. 2017, p. 2078). The 2017 to 2019 drought was a three-year rainfall deficit across the Murray-Darling Basin, unprecedented in the instrumental record (Falster et al. 2024, p. 1). The national series read here give an export share of 71% of production by volume in the three years to 2024-25 (ABARES 2026b, p. 5) and farm incomes from 2005-06 to 2024-25 (ABARES 2026a, p. 2); none is an annual series of farm output, so no source read here measures output across 2011 to 2025. Section 8 tests the margin against this dependence on the weather.

## 2. Method and data in brief

Capacity here is the number of people a region's land could feed on a stated diet and settings, with no trade in or out. A region is over capacity when its population exceeds that number. Status is reported as people over capacity, so a value above 1 is over capacity. The model, its constants and its construction, published from 2014 to 2017 (section 1.3), are summarised in Supplementary Section S8.

The model is run under two presets. The short term takes the diet and production of the data year in an average year. The long term takes the settings of a 100-year self-sufficiency plan, defined in section 7. Table S1 gives the settings of both presets in both years. The model has 60 zones: the nation, seven state zones and 52 NRM regions; the regional results use 53 regions (52 NRM regions and the Northern Territory).

The 2011 inputs are those of the thesis, except the populations; the 2025 inputs were brought forward layer by layer, in the order of section 4, each layer a release whose inputs are recorded by hash. The method is frozen, so within one method tier the change between 2011 and 2025 is a data change. Both years' regional populations are the ABS estimated resident population at 30 June of the year, by 2021 SA2, shared among the zones by residential land where an SA2 straddles a boundary; the 2011 figures use the same series and allocation as 2025. The thesis's own 2011 figures had no recorded source and differed from these by more than 10% in 23 zones. The national population row (22,326,388 in 2011) is a published input and is left as it is; the 53 regions sum to 22,336,514, which is 10,126 more. Supplementary Section S8 lists the data sources by year.

The method has three tiers: published, corrected and improved. The corrected tier applies two corrections to the published method, the biodiesel yield per tonne of oilseed (Geoscience Australia and ABARE 2010, p. 331) and the carcase-to-retail yield of beef (USDA undated; AUS-MEAT 2005), and for 2011 sets each state's population to the sum of its regions, which moves the state ratios but no capacity. The paper reports the corrected releases, `2011-fixed-3` and `2025-fixed`, unless a figure names another release.[^1] Putting all 53 regional populations on the ABS figures in `2011-fixed-3` leaves every capacity unchanged (section 3). The named scenarios and grain stores of sections 8 and 11 are on `2025-fixed`, with each store taking the resilience table of the frozen release `2025-store-1` or `2025-store-2`.

The weather allowance scales every yield by one factor per state, taken from the record of wheat, oats and barley yields (Lane 2014, p. 193). It is a cereal factor. For Australia it is built from 153 seasons from 1861 to 2024-25, each season's yield over the mean of the ten observations around it, and its 1-in-10 and 1-in-20 values are 0.742 and 0.634 (the 2011 releases use the thesis table, 0.599 at 20 years). Each region takes its state's factor (section 8). Applying a cereal factor to pasture-fed output has not been tested; section 8.1 gives a crop-only bound.

The 2025 national results carry Monte Carlo ranges over 19 sampled choices, of which 18 vary on the corrected release. A definition (what is counted, the unit, the time frame, the diet standard, the weather allowed for) changes what the number means and is reported separately; a setting is a value within one meaning, drawn over the range its source gives. The regional ranges that test the flips come from the first 13 choices (12 vary). Section 6 of the companion methods paper describes and tests the method; Supplementary Section S4 gives the shares. The 2011 results have no ranges.

[^1]: The 2011 values published in Lane et al. (2015) and Lane (2017) were computed before the two method corrections, before each 2011 state's population was set to the sum of its regions and before the regional populations were put on the ABS figures; correction notes to those papers set out the change.

## 3. The short-term picture, 2011 to 2025

On the corrected releases, Australia's short-term capacity was 33.3 million people in 2011 (`2011-fixed-3`) against a population of 22.3 million. In 2025 (`2025-fixed`) it was 41.5 million against 27.6 million (Figure 1). Capacity was about 1.5 times the population in both years: 1.49 times in 2011 and 1.50 times in 2025. Capacity grew by 24.6% and the population by 23.7%, so the national margin held its multiple.

[Figure 1: national short-term capacity against population, 2011 (`2011-fixed-3`) and 2025 (`2025-fixed`), from `results/comparison_cells.csv`, Australia rows, columns `capacity_2011_corrected`, `capacity_2025_corrected`, `population_2011`, `population_2025`]

The regional picture moved more. Of the 53 regions (52 NRM regions and the Northern Territory), 22 were over capacity in the short term in 2011 (`2011-fixed-3`) and 16 in 2025 (`2025-fixed`). In the long term, 35 and 32 regions were over capacity. The net fall of six regions in the short term is larger than the two flips that pass the tests below. The count of regions over capacity is therefore not a finding on its own.

Eight regions changed status in the short term: seven moved from over to under capacity and one, Corangamite, from under to over. Each flip was tested three ways (Table 1). The first asks whether the land layer alone moves the region's capacity by more than 2 times or less than 0.5 times, a sign that land was defined differently, not used differently. The second asks whether the 2011 zone was drawn on an older boundary. The third asks whether the 2025 status holds across the 5th to 95th percentile of the 2025 Monte Carlo range. Three flips are land-definition artefacts: Desert Channels, Southern Gulf and SA Arid Lands. Three are not robust to the 2025 range: Wet Tropics, Rangelands (Western Australia) and Corangamite. Two are clean and robust, both from over to under capacity: Mackay Whitsunday and North Tasmania.

Table 1. Regional status flips between 2011 and 2025, by test, for the 53 regions (52 NRM regions and the Northern Territory), corrected method (`2011-fixed-3` against `2025-fixed`). Built from `analysis/paper_a/regional_flips-3.csv`. A flip can fail more than one test.

| Preset | Regions over capacity, 2011 | Regions over capacity, 2025 | Flips | Land-definition or boundary artefacts | Not robust to the 2025 range | Clean and robust |
|---|---|---|---|---|---|---|
| Short term | 22 | 16 | 8 (7 over to under, 1 under to over) | 3 | 3 | 2 |
| Long term | 35 | 32 | 3 (all over to under) | 2 | 1 | 1 |

The two clean flips carry qualifications. Mackay Whitsunday is under capacity in 2011 on the improved release (`2011-improved-3`), so it does not flip on that release. North Tasmania's 2011 status sits close to balance, at 143,631 people against a capacity of 139,165 (`2011-fixed-3`), and the 2011 inputs have no range. North East Victoria counted as a third clean flip before the 2011 populations were put on the ABS footing: its thesis population was a copy of Goulburn Broken's 204,651. At the ABS figure of 98,604 it is under capacity in 2011 as well as 2025, so it does not flip. Section 7 takes up the three long-term flips.

Capacity grew most in the inland cropping and basin regions. The largest short-term gains were in Central West NSW (464 thousand people), Lachlan (456 thousand) and Namoi (441 thousand), all under capacity at both dates (`2011-fixed-3` to `2025-fixed`). People grew most on the coast and in the capitals: by 1.3 million in Port Phillip and Westernport, 1.0 million in Hawkesbury-Nepean-Sydney and 1.0 million in South East Queensland. Murrumbidgee-ACT, which holds Canberra, gained both, 348 thousand in capacity and 141 thousand in people. Figure 2 maps the change by region and marks the flips.

[Figure 2: change in short-term capacity and population by region, 2011 (`2011-fixed-3`) to 2025 (`2025-fixed`), with the status flips marked by test, from `analysis/paper_a/regional_flips-3.csv` and `analysis/population_2011/movers-3.csv`]

The capital-city regions are over capacity in both years and both presets, except Murrumbidgee-ACT, which is under capacity in the short term in both years. Swan, which holds Perth, is the clearest boundary case (Supplementary Section S1). The land layer alone takes its capacity to 0.01 of the 2011 value, because the 2011 zone was drawn before the Perth boundary change. Swan's 2025 status can be used, but its 2011 status cannot.

The cautions are these. Five zones carry older 2011 boundaries. The land-definition flag is a fixed threshold at 2 and 0.5 times. Robustness is tested on the 2025 range only (section 9). The artefact test is made on capacity, not on whether the population change is real; putting the 2011 populations on the ABS footing removed one long-term flip, Northern and Yorke, and no short-term flip, after North East Victoria's had gone. The flips have not been tested against the method tier (section 9).

## 4. What drove the change

The change in capacity was taken apart layer by layer on the corrected releases. The layers are the 2025 data added to the 2011 inputs one set at a time: land, population, crop yields, livestock, consumption, the organic update, the resilience table, long-term liquid fuel and the red meat mix of the diet. A layer's effect depends on the order, so the walk was run forward (the order of the release chain), in reverse and in each of the 362,880 orderings. The main figures are the average over all orderings; the forward and reverse walks bound it. Each ordering's effects sum exactly to the change, so there is no interaction term. Kastner et al. (2012) split a change in land need into population, yield and diet effects; here population is not one of the causes.

Population does not enter capacity in this model; it changes whether a zone is over or under it. Nationally, people over capacity was 0.670 in the short term and 1.454 in the long term in 2011, and 0.665 and 1.767 in 2025 (Table 2). The short-term status held, while the long-term status worsened because the population grew and long-term capacity barely moved. The population layer moves capacity only through the infrastructure land that follows population, which changes capacity by 0 people nationally.

Table 2. National decomposition of the change in capacity, 2011 to 2025, corrected releases (`2011-fixed` to `2025-fixed`), people: the average over all 362,880 orderings of the nine layers, with the forward walk (the order of the release chain) and the reverse walk as bounds. Built from `analysis/comparison_2025/capacity_by_cause_corrected_orders.csv`, zone 1 (Australia). The averages sum to the change within 3 people.

| | Short term, average | Short term, forward | Short term, reverse | Long term, average | Long term, forward | Long term, reverse |
|---|---|---|---|---|---|---|
| Capacity 2011 (`2011-fixed`) | 33,307,814 | 33,307,814 | 33,307,814 | 15,350,146 | 15,350,146 | 15,350,146 |
| Land | -3,064,101 | -2,621,910 | -3,546,205 | -1,248,192 | -1,208,326 | -1,334,901 |
| Infrastructure land that follows population | 0 | 0 | 0 | 0 | 0 | 0 |
| Crop yields | +162,372 | +115,575 | +220,269 | +257,755 | +219,940 | +253,434 |
| Livestock | +5,502,789 | +4,703,257 | +6,374,770 | +628,764 | +599,578 | +743,648 |
| Consumption (without the organic share) | +4,156,557 | +4,183,947 | +4,090,572 | 0 | 0 | 0 |
| Organic update | 0 | 0 | 0 | +173,183 | +172,682 | +180,979 |
| Resilience table | 0 | 0 | 0 | -7 | -7 | -7 |
| Long-term liquid fuel | 0 | 0 | 0 | +124,764 | +90,858 | +114,983 |
| Red meat mix of the diet | +1,438,106 | +1,814,854 | +1,056,317 | +336,796 | +398,338 | +314,927 |
| Capacity 2025 (`2025-fixed`) | 41,503,537 | 41,503,537 | 41,503,537 | 15,623,209 | 15,623,209 | 15,623,209 |
| Land and livestock together (sum of two rows) | +2,438,688 | +2,081,347 | +2,828,565 | -619,428 | -608,748 | -591,253 |
| People over capacity, 2011 | 0.670 | | | 1.454 | | |
| People over capacity, 2025 | 0.665 | | | 1.767 | | |

In the short term capacity rose by 8.2 million. On the average of all orderings livestock added 5.5 million (67% of the change), consumption 4.2 million and the red meat mix 1.4 million, while land took 3.1 million off and crop yields added 0.2 million. The consumption and red-meat-mix layers together add 5.6 million (68%): the diet with less beef (the red-meat share of meat fell from 0.64 to 0.578, and FAO beef and veal supply per person from 39.1 to 25.9 kg). The consumption layer also carries the fuel, biofuel and timber settings, so it is not wholly diet. The forward and reverse walks bound livestock at 4.7 and 6.4 million and the red meat mix at 1.8 and 1.1 million.

The land and livestock layers are not independent. The 2025 livestock yields divide output by the 2020-21 grazing area of the land layer, so a smaller grazing area lowers capacity in the land layer and raises the livestock yield (Supplementary Section S1 gives Avon's arithmetic). Land and livestock together add 2.4 million (30%) on the average, and 2.5 million when treated as one layer. So the livestock figure overstates, and the land figure understates, what each did alone. The organic share is counted in the organic step, not in consumption (on the release chain as built, consumption would carry 3.8 million and the organic step 0.4 million). Crop yields add little, because short-term capacity is bound by pasture-fed meat and dairy rather than by field crops (section 6).

In the long term capacity rose by 0.27 million. Land is the largest effect in the forward walk, the reverse walk and the average, at -1.25 million on the average; with livestock the pair is -0.62 million. Livestock added 0.63 million, the red meat mix 0.34 million, crop yields 0.26 million, the organic update 0.17 million and liquid fuel 0.12 million. The resilience table moved capacity by -7 people.

Figure 3 gives the effect of each layer in each of the 53 regions (52 NRM regions and the Northern Territory), in both presets, on the forward walk; Supplementary Section S1 gives the regional detail. The order changes which layer is largest in a few regions: the forward walk names a different largest layer from the average in 7 of the 53 regions in the short term and 2 in the long term, the reverse walk in 3 and 1. On the forward walk livestock carried 65% to 86% of the short-term gain in Central West NSW, Lachlan, Namoi and the two Border Rivers regions.

[Figure 3: effect of each layer on capacity by region, short and long term, forward walk, corrected releases (`2011-fixed` to `2025-fixed`), from `analysis/comparison_2025/capacity_by_cause_corrected.csv`, zone rows]

Two further caveats apply. The livestock layer rests on a five-year window of herd and meat data, 2020-21 to 2024-25, that ends in two years of heavy slaughter; section 9 gives the range when the window is restricted to full herd cycles. The crop layer includes two very good winter-crop years, but it weighs little.

---


## 5. The scale curve: where the margin goes

This section asks how much of the national capacity is left when every unit feeds itself from its own land: the sum of the units' capacities as a share of the national capacity. It was computed for 7 states, 53 regions (52 NRM regions and the Northern Territory), 89 SA4s, 336 SA3s and 2,450 SA2s. Every unit kept the national settings for diet and waste. The curve in Figure 4 is on the state-yield basis: every unit took the yields, climate zone and settings of its state. This is the conservative bound and the only basis used for the curve in the main text; section 5.4 gives the other bound in one sentence. The loss follows from the model's substitution rule (section 6): cropland can carry pasture-fed products but pasture cannot carry crops, so a unit whose land mix differs from the nation's loses capacity to the sum.

### 5.1 The curve and its stability

On the 2025 corrected release the states summed to 75% of the national short-term capacity, the regions to 44%, the SA4s to 58%, the SA3s to 44% and the SA2s to 37% (Table 3). On 2011 data the states gave 77%, the regions 44%, the SA4s 60%, the SA3s 46% and the SA2s 40%. The shares barely changed between the two data years. The long-term curve fell further at every level, to 20% for the SA2s in 2025 (Table 3).

[Figure 4: the scale curve, the sum of capacities as a share of national capacity at each level from the nation to SA2, 2011 and 2025, short and long term, state-yield basis, corrected releases (2011-fixed, 2025-fixed); from `results/scale_curve.csv`, drawn by `analysis/scale_curve_2025/plot_scale_curve.py` (`scale_curve.png`)]

The finding of Lane et al. (2015) that capacity falls as the unit shrinks (section 1.3) held on the corrected method. On 2011 data the national short-term capacity was 33.3 million, the states summed to 25.7 million and the 53 regions to 14.7 million, and the curve extends the finding to SA2. In Iran, capacity summed over local units fell below the national figure (Khorsandi et al. 2022), and a meta-model of those results related capacity to area with diminishing returns (Khorsandi et al. 2023).

### 5.2 The boundary effect and its cause

The 53 regions lost as much as the 336 SA3s, 44% against 44% in the short term in 2025. They lost far more than the 89 SA4s, which kept 58%. Rebuilding the regions from whole SA2s gave the same 44%, so the gap is a property of the partition, not of the land data. The gap lay where rangeland meets cropland, in New South Wales, South Australia and Western Australia (Supplementary Section S2).

Section 6 gives the cause. South Australia's Arid Lands region holds 326,000 km2 of pasture and 221 km2 of cropland. Its capacity was 41 thousand people, far less than SA4 406, which joins that arid country with the cropland of the Eyre Peninsula. Supplementary Section S2 gives the other stranded pasture. In the long term the gap between the regions and the SA4s was 12 points, 23% against 35%.

### 5.3 How much a better drawing of regions keeps

Random groupings and an ideal contiguous split bound how much a better drawing of regions would keep (Supplementary Section S2). The best contiguous split found at 53 regions kept 76% of national capacity in the short term and 69% in the long term. These come from two splits, each optimised for its own term; the short-term split kept 66.1% in the long term. The search was heuristic, so 76% and 69% are lower bounds on the best split.

### 5.4 Reading the curve

The curve is read for its shape, not for any single administrative SA2. For the 2011 cells the SA levels used land of 2020-21, against a reference of 30.7 million rather than the 33.3 million of the 2011 zones, so the 2011 SA shares are not exactly comparable with the zone levels. The other bound lets each unit keep its own yields: the 2025 short-term share is then 75% for the states and 54% for the SA2s, so yield differences within states are worth about 17 points at SA2 level, and the truth for SA2s lies between 37% and 54% (Supplementary Table S6). The regions' sums in sections 7, 8 and 11 are on each zone's own yields, which is why they differ from the curve's 44%.

Table 3. Sum of capacities as a share of national capacity, by level, state-yield basis, corrected releases (2011-fixed, 2025-fixed), short and long term. Built from `results/scale_curve.csv` (column `share_of_national`, `yield_basis` state). For the 2011 cells the SA4, SA3 and SA2 shares are against a reference on 2020-21 land (row "Australia (SA land)"), not the 2011 zones. Supplementary Table S6 gives the same table on each unit's own yields.

| Level | Units | 2011 short | 2011 long | 2025 short | 2025 long |
|---|---|---|---|---|---|
| Australia | 1 | 100% | 100% | 100% | 100% |
| State | 7 | 77% | 44% | 75% | 49% |
| NRM region | 53 | 44% | 20% | 44% | 23% |
| SA4 | 89 | 60% | 32% | 58% | 35% |
| SA3 | 336 | 46% | 23% | 44% | 24% |
| SA2 | 2,450 | 40% | 18% | 37% | 20% |

## 6. The mechanism

One rule drives most of these results. A diet in the model needs cropland and pasture in nearly fixed proportion, so a unit's capacity is set by whichever land type runs short. Cropland can carry pasture-fed products when pasture falls short, but pasture is not necessarily fit for crops (Lane 2014, p. 266), and in the model it cannot carry them. Lane (2014, p. 3) found the share of cropping land to be the most significant determinant of capacity. Nationally the diet needs only 141,000 km2 of food cropland (below), so cropland binds only at a share well below the 10% at which the national test starts; in that test, on the 2025 corrected release, capacity was unchanged for every cropland share from 10% to 99% of the combined area. In a rangeland region such as SA Arid Lands, with 221 km2 of cropland, cropland decides capacity (section 5). The test was run for Australia only, so the rule is not shown for regions.

On the reference diet of the 2025 corrected release, pasture binds nationally. The diet needs 3.49 million km2 of pasture against 3.32 million km2 held. About 175,000 km2 of cropland therefore grazes animals, and 141,000 km2 grows food crops. No pasture is left unused; the 1.96 million km2 of unused land is non-agricultural land. This is why measures aimed at field crops barely move the 2025 short term while livestock output does (section 11). It is also why field-crop yields 24% lower took 0.2% off the short term, against 26% off at a 1-in-10 drought, which scales every yield (both on the 2025 corrected release).

On the 2025 corrected release a little pasture-fed meat beats none: a diet of 2.5% meat and eggs fed 118.0 million, against 112.4 million with none. On the 2025 improved release the diet with no meat or eggs was the highest point, at 103.6 million, so the gain from a little meat holds on the corrected release only.

The model has one pasture land type, and within a zone dairy and beef cattle are credited with the same average pasture yield. The dairy-on-good-land improvement moves dairy's land to the cropping column, at the observed yield of dairy farms, and it moves regions both ways (section 9). Grazing on land unsuited to crops is common ground with the wider literature: 65% of the grass ruminants eat grows on such land (Poore and Nemecek 2018, p. 990), and livestock on it use land that crops cannot (van Zanten et al. 2016; Roos et al. 2017).

## 7. The long term: a 100-year plan

The long-term settings follow Lane (2014) and Lane (2017). They plan for the worst year in 100 of weather, through the cereal factor of section 2. They set a low-meat diet, with meat and eggs at 7.5% of the diet against 12% in the short term. They assume no avoidable waste, full recycling of food waste, organic farming and liquid fuel cut from 2,360 to 210 litres a person. They also set activity level 3, three fibre settings, timber, infrastructure area and a 30% reserve. The land for the remaining fuel rests on a biodiesel yield of 400 litres per tonne of oilseeds (Geoscience Australia and ABARE 2010, p. 331).

### 7.1 National capacity in both years

On the corrected method the long-term capacity was 15.35 million on 2011 data and 15.6 million on 2025 data (Table 4). A plan on that basis would cover 69% of the 2011 population and 57% of the 2025 population. Capacity rose by 0.27 million while the population grew by 5.28 million. The 2011 figure lies inside the 2025 range across input choices, 13.3 to 18.8 million; 2011 was not sampled, so this is not a test of whether the change is real (section 9).

Table 4. Long-term capacity of Australia and its regions, corrected releases (2011-fixed-3, 2025-fixed), regional sums on each zone's own yields. Built from `analysis/paper_a/long_term_regions.csv`; the 2011 share of the population in over-capacity regions is from `results/2011-fixed-3.csv`.

| | 2011 | 2025 |
|---|---|---|
| National long-term capacity (million) | 15.35 | 15.6 |
| Population (million) | 22.3 | 27.6 |
| Share of the population a 100-year plan covers | 69% | 57% |
| Population living in regions over capacity | 93% | 94% |
| Sum of regional long-term capacities over national | 33% | 38% |

### 7.2 What each setting is worth

Each setting was put back to its short-term value with the others held (Table 5). The weather allowance, the cereal factor, was the largest. Without it the 2025 long-term figure would be 34.3 million rather than 15.6. Liquid fuel was the largest on the other side: with short-term fuel use the figure would be 3.7 million. The long-term figure is therefore mainly a statement about planning for bad years. No avoidable waste, the low meat-and-egg share, the lower red-meat share and the lower fibre need, from 23 to 11.5, each raise capacity. Organic farming and the natural-fibre and wool-fibre shares lower it. Timber, infrastructure area and the 30% reserve have no effect, because non-agricultural land absorbs them.

Table 5. What each long-term setting is worth, Australia, 2025 corrected release (2025-fixed): the long-term capacity with that one setting put back to its short-term value, against 15.6 million. Built from `analysis/paper_a/long_term_levers.csv` (zone 1, column `without`).

| Setting (short-term to long-term value) | Long term without it (million) | Change on 15.6 |
|---|---|---|
| Weather allowance, return period (1 to 100 years) | 34.3 | +119% |
| Liquid fuel (2,360 to 210 litres a person) | 3.7 | -76% |
| Avoidable waste (0.12 to 0) | 13.0 | -17% |
| Recycling of food waste (0 to 1) | 15.4 | -1% |
| Organic farming share (0.07 to 1) | 19.0 | +22% |
| Activity level (1 to 3) | 16.2 | +4% |
| Biofuel share (0.0023 to 1) | 16.1 | +3% |
| Fibre need (23 to 11.5) | 11.1 | -29% |
| Fibre from natural sources (0.5 to 1) | 19.7 | +26% |
| Fibre from wool (0.12 to 0.9) | 22.8 | +46% |
| Red-meat share of meat (0.578 to 0.5) | 14.7 | -6% |
| Meat and egg share of the diet (0.12 to 0.075) | 11.7 | -25% |
| Timber (0.8 to 5), infrastructure area (730 to 500), reserve (0.26 to 0.3) | 15.6 | 0% |

### 7.3 The regions

The cropping belts and inland plains feed themselves in the long term. In 2025 the strongest were South Coast WA, Avon, Border Rivers - Maranoa - Balonne, Western NSW, Border Rivers - Gwydir and Northern Agricultural. Their populations were 0.12 to 0.26 times their long-term capacity. Northern Gulf (which carries a land-definition flag), South West Qld and Lachlan also fed themselves. Of the 53 regions (52 NRM regions and the Northern Territory), 35 were over capacity in the long term on 2011 data and 32 on 2025 data, leaving 18 and 21 under capacity. This count is read with the flip tests. Three regions changed long-term status, all from over to under capacity. Two of the three carry an artefact flag: Desert Channels and SA Arid Lands, both for the land definition. SA Arid Lands is also not robust to the 2025 range. One flip is clean and robust, South West Qld. The net fall of 3 is therefore more than the 1 clean flip explains.

Nearly the whole population lives in regions over capacity in the long term, 93% in 2011 and 94% in 2025. On each zone's own yields the regions together held 33% of the national long-term capacity in 2011 and 38% in 2025. On the state-yield basis of section 5 the regions' long-term share was 20% in 2011 and 23% in 2025. The plan fails where people live, not where food is grown. The long-term regional count also depends on the method tier (section 9).

[Figure 5: what each long-term setting is worth for Australia in 2025, and long-term capacity by region as people over capacity in 2011 and 2025, corrected releases (2011-fixed-3, 2025-fixed), each zone's own yields; from `analysis/paper_a/long_term_levers.csv` and `analysis/paper_a/long_term_regions.csv`; no plotting script exists]

## 8. Shocks and food security by region

The weather allowance of section 2 scales every yield, crops, pasture products and livestock alike, by a factor taken from wheat, oats and barley yields. The 53 regions (52 NRM regions and the Northern Territory) each take their state's factor. Regions of one state therefore share a factor, but they do not all tip together: the five regions that tip at 1 in 10 in 2025 are in three states.

### 8.1 The national margin

As a multiple of the population, national short-term capacity was about 1.5 in an average year in both years (Table 6; section 3), 1.11 and 1.12 in a 1-in-10 year (30.8 million against 27.6 million in 2025) and 0.68 and 0.69 in a 1-in-100 year (18.9 million in 2025). In a 1-in-20 year the population exceeded capacity; as a status ratio, people over capacity was 1.12 in 2011 and 1.05 in 2025. At the base settings the margin is above balance at 1 in 10 and below it at 1 in 20 in both data years, but the settings decide the sign. Across the 5th to 95th percentile of the original 13-choice range, 2025 capacity is 27.0 to 34.0 million at 1 in 10 (central 30.8) and 23.0 to 29.0 million at 1 in 20 (central 26.3). The population of 27.6 million lies inside both, and the 19-choice range of section 9 is wider at both ends. With the meat window restricted to the four windows that span a full herd cycle, the ranges narrow to 29.2 to 32.5 million at 1 in 10, above the population in every draw, and 25.0 to 27.8 million at 1 in 20, below it in about 92% of draws. 1 in 20 is not a threshold. At the 2025 population the failure probability is about 5.8% a year, 1 in 17, on the corrected method (Supplementary Section S8).

Capacity held at 2025 data (41.5 million in an average year) is about equal to the 40.5 million projected for 2062-63 and the 41 million for 2065-66 (section 1.1); in a 1-in-10 year (30.8 million) it falls short of both. This holds capacity fixed and projects nothing.

The allowance is a cereal factor: for Australia the 1-in-10 factor (0.742) is the 15th-worst of 153 seasons of wheat, oat and barley yield and the 1-in-20 factor (0.634) the 8th-worst. It has not been tested on pasture-fed output, and almost all (about 97%) of the short-term drought effect at 1 in 10 falls on pasture-fed food. Applied to crops alone, with pasture-fed output at its average-year level, national short-term capacity is 41.2 million at 1 in 10 against 30.8 million with the factor on all output, and long-term capacity at 1 in 100 is 24.7 million against 15.6 million. The short-term drought results are therefore a statement about pasture-fed output in a drought, which the cereal record does not measure. National totals smooth out local shocks in a large country such as Australia (Cottrell et al. 2019, p. 135).

Table 6. The nation and its regions under a bad year, corrected releases (2011-fixed-3, 2025-fixed), short term; regional figures on each zone's own yields. Shares are of the 53 regions' population; "about" marks a share on a rounding edge (81.55% and 91.48% in 2011). Built from `analysis/paper_a/shocks_summary-3.csv`.

| Year | Return period | National capacity (million) | Population (million) | National capacity as a multiple of the population | Population living in regions over capacity | Sum of regional capacities (million) | Sum over national |
|---|---|---|---|---|---|---|---|
| 2011 | average year | 33.3 | 22.3 | 1.49 | about 82% | 21.0 | 0.63 |
| 2011 | 1 in 10 | 24.7 | 22.3 | 1.11 | 85% | 13.9 | 0.56 |
| 2011 | 1 in 20 | 20.0 | 22.3 | 0.89 | 88% | 10.6 | 0.53 |
| 2011 | 1 in 100 | 15.2 | 22.3 | 0.68 | about 91% | 7.2 | 0.47 |
| 2025 | average year | 41.5 | 27.6 | 1.5 | 81% | 26.0 | 0.63 |
| 2025 | 1 in 10 | 30.8 | 27.6 | 1.12 | 85% | 16.9 | 0.55 |
| 2025 | 1 in 20 | 26.3 | 27.6 | 0.95 | 89% | 13.4 | 0.51 |
| 2025 | 1 in 100 | 18.9 | 27.6 | 0.69 | 91% | 8.7 | 0.46 |

### 8.2 The regions by return period

On each zone's own yields, about 82% of the population of the 53 regions lived in regions over capacity even in an average year in 2011, and 81% in 2025. The share rose to 85% at 1 in 10 in both years and to about 91% at 1 in 100 in 2011 and 91% in 2025. The count of regions over capacity rose from 16 in an average year to 21 at 1 in 10 in 2025, and from 22 to 25 in 2011. These counts are read with the flip classification. In 2025 five regions were under capacity in an average year and over it at 1 in 10: Wet Tropics, North East Victoria, Rangelands, Mackay Whitsunday and Burnett Mary. In 2011 three were (Corangamite, North East Victoria and Burnett Mary), and at 1 in 20 four. Of the five, Mackay Whitsunday is a clean and robust flip between 2011 and 2025; Wet Tropics and Rangelands also flipped, but their 2025 average-year status is not robust to the range; North East Victoria and Burnett Mary did not flip, and their 2025 status is robust. The flip tests were not applied to the 1-in-10 status itself, so the rise from three regions to five is not a finding on its own.

Regional self-sufficiency fails sooner than national: on each zone's own yields the regions together held 63% of national capacity in an average year in 2025 and 55% at 1 in 10, or 16.9 million against a population of 27.6 million. The 44% of section 5 is on the state-yield basis and is a different measure.

[Figure 6: exposure to shocks by region, people over capacity in each of the 53 regions at each return period, 2011 and 2025, corrected releases (2011-fixed-3, 2025-fixed), with the named scenarios by region on the 2025 corrected release; from `analysis/paper_a/shocks_by_region-3.csv` and `analysis/paper_a/scenarios_by_region.csv`; no plotting script exists]

### 8.3 Named scenarios

The named scenarios were run on the 2025 corrected release (2025-fixed), against a reference of 41.5 million in the short term and 15.6 million in the long term; Supplementary Section S3 and Table S2 give them all. The grain stores applied the resilience tables of the frozen store releases (2025-store-1, 2025-store-2), so they rest on the same cereal factor. The waste scenario sets avoidable waste to 6%, which halves the model's retail-and-consumer loss share (section 11); it raised the short term by 16.4% and lowered the long term by 8.15%, because the long-term settings assume no avoidable waste. A store of one year of grain raised the long-term capacity by 48.45% and a store of two years by 64.47%, with no short-term effect: more than any other named scenario in the long term, but less than the weather allowance itself (section 7).

### 8.4 What a single-year shock does not describe

A single-year shock does not describe a drought of several years. The 2017 to 2019 drought was exceptional as a three-year deficit (section 1.5), while its single years mostly fell within the expected range (Falster et al. 2024, pp. 6, 9). Bad wheat years are also partly correlated across the southern states (Anderson et al. 2019): ENSO and the Indian Ocean Dipole together explain 30 to 41% of wheat variability in Australia and East Africa. An export-inclusive count sits beside the model's (Supplementary Section S9).

---


## 9. How sure are the regional results

### 9.1 The ranges and the status flips

This section tests the regional results for the 53 regions (52 NRM regions and the Northern Territory), each on its own yields. The national range comes from 2,000 Latin hypercube draws of 19 sampled choices, 18 of which vary; the regional ranges that test the flips come from 1,000 draws of the first 13 choices, 12 of which vary, because the six added choices were drawn nationally only.

On the corrected 2025 release (2025-fixed), the 5th to 95th percentile of national capacity is 31.1 to 49.2 million people in the short term, a factor of 1.58 (26.2 to 58.1 from lowest to highest draw, a factor of 2.22), and 13.3 to 18.8 million in the long term. Three choices carry four-fifths of the short-term variance: the source of the land areas (32%), the energy requirement per person (27%) and the window of herd and meat data (24%). Each rests on a judgement: equal chances between two land sources and between three meat windows, and a moderately active population at the top of the energy range. If the meat window of the 13-choice draws is restricted to the four windows that span a full herd cycle, the short-term range is 39.4 to 43.8 million and the long-term range 13.9 to 16.2 million, and the red-meat share of the diet then explains 85% of the short-term variance.

The 2011 capacities, 33.3 million in the short term and 15.35 million in the long term, lie inside the 2025 ranges, and 2011 was not sampled. The short-term rise holds at the base settings and in every single year of data from 2016-17 to 2024-25 (2025-organic release, Supplementary Section S4), but it is a comparison of two years at fixed settings, not a test across the settings.

Each status flip was tested against its region's 2025 range on 2025-fixed. A flip holds when the 2025 population lies outside the region's 5th to 95th percentile of capacity. The test covers the 2025 status only, because the 2011 inputs have no draws. Of the eight short-term flips of section 3, three are not robust to the 2025 range: Wet Tropics, Rangelands (WA) and Corangamite, the one region that moved from under to over capacity. Two pass every test in hand: Mackay Whitsunday and North Tasmania. Of the three long-term flips, one passes every test (section 7). The method tier is not a flip test: it moves Corangamite in the short term between the corrected and improved 2025 releases, and Mackay Whitsunday on 2011 data.

Five range ends of the regional draws rest on the author's judgement: the three-way choice of the meat data window (equal chances), the low ends of the meat-and-egg share (0.115) and of the red-meat share (0.528), the equal weight on the leave-one-out resilience table, and the low end of the long-term feeding benchmark (0.30), which has no effect on the corrected release. Supplementary Section S4 gives the shares of the variance.

### 9.2 What each method choice does, region by region

Each method choice was applied alone to the published-method release on 2025 data (2025-mirror), the published method of Lane (2014). Its effect is given as a share of the published capacity (Figure 7; Supplementary Section S4 and Table S3). Two modules are the corrections of section 2, the beef carcase yield and the biodiesel yield; the other six are improvements. The beef carcase correction lowers the short-term national capacity by 16.0%, most in the beef and cropping regions, and leaves the long-term figure unchanged. The biodiesel correction is a long-term correction, +20.7% nationally and +97.9% in South East Queensland. Dairy on land that can carry it is the largest improvement, +20.2% in the short term nationally, and it moves regions both ways.

[Figure 7: the effect of each method choice by region, 2025 data, short and long term, as a percentage of the published-method capacity (53 regions, diverging scale clipped at 40%), from `analysis/paper_a/method_effects_heatmap.png` (data `analysis/paper_a/method_effects_by_region.csv`)]

The short-term count of regions over capacity in 2025 is robust to the method tier: 15, 16 and 15 under the published, corrected and improved methods (Supplementary Table S4). The long-term count is not: 36, 32 and 36. The corrected tier is lowest in both years, with 35 regions over capacity in 2011 against 36 on the improved tier; on the corrected tier the long-term count falls by 3 between 2011 and 2025, and on the improved tier it does not fall (36 in both years). The long-term regional map of section 7 therefore depends on judgement-based method choices as well as on the weather allowance. The modules interact, so the one-at-a-time effects are not additive: in the 2025 short term the modules together add 4.25 million people to the published capacity, where the sum of their effects alone is 7.13 million (an interaction of -2.88 million), and in the long term they add 4.35 million against 1.15 million alone (+3.20 million).

## 10. Regions in depth

Five regions were chosen, one of each type, from the largest movers among the 53 regions (52 NRM regions and the Northern Territory): a capital with hinterland, a Murray-Darling Basin pair, a south-west Western Australian cropping region, Tasmania, and an arid region set beside a cropping neighbour. Each is read through the short term, the long term, drought and the 2025 range. All figures are on the corrected releases (2011-fixed-3 and 2025-fixed) and on each region's own yields (Table 7). Supplementary Section S5 gives the full reading of Hawkesbury-Nepean-Sydney, the Murray with Murrumbidgee-ACT, Avon, and SA Arid Lands with the Eyre Peninsula.

Those four regions show what the counts mean on the ground. Hawkesbury-Nepean-Sydney is over capacity in both years and both terms; even the 95th percentile of its 2025 short-term capacity is 48,520 people, against a population of 5,401,609. Its fall in capacity carries the land-definition flag: with only the 2025 land layer swapped in, capacity is 0.491 of the 2011 figure, just below the rule's lower bound of 0.5. The Murray is under capacity in both years and both terms. Murrumbidgee-ACT, which holds Canberra, is under capacity in an average year, with its 2025 population 0.482 times its capacity. It is over capacity in the long term (2.431 times) and at a 1-in-100 drought (1.604 times). The Basin accounts for about 40% of national farm output (Wittwer and Waschik 2021, p. 919), but the model carries no water limit (section 12). Avon is a cropping region under capacity throughout, and in the long term its 2025 population is 0.14 times its capacity. At a 1-in-100 drought its 2025 short-term capacity is 508,513 people, with yields scaled by Western Australia's worst-year factor. SA Arid Lands moved from over to under capacity in the short term, but the land layer alone raises its capacity 6.5 times, so the change is read as a change in the land definition. In the long term its 2025 status is not robust to the range. Its cropping neighbour, the Eyre Peninsula, carries no flag and is under capacity in both years and both terms.

**North Tasmania.** North Tasmania is the flip that passes the land, boundary and range tests in hand. It was over capacity in 2011 and is under capacity in 2025. Its short-term capacity rose from 139,165 to 187,593 against a population of 143,631 to 156,393. Its 2025 status holds across the range: the 5th percentile of capacity, 174,487, is above the 2025 population. It sits on the edge in a bad year. At a 1-in-10 drought in 2025 it is balanced (population 1.000 times capacity), and at 1 in 100 it is over capacity (1.253 times). Its 2011 status sits close to balance and has no range. In the long term it is over capacity in both years, with capacity of 36,954 and 58,798.

Table 7. The regions in depth, 2025 (2025-fixed; local basis), with the 2011 short-term status (2011-fixed-3). People. Built from `analysis/paper_a/regions_in_depth.csv`.

| Region | Short-term status, 2011 to 2025 | Population 2025 | Short-term capacity 2025 | 5th to 95th percentile, short term | Capacity at 1 in 100 | Long-term capacity 2025 | Flag |
|---|---|---|---|---|---|---|---|
| Hawkesbury-Nepean-Sydney | over to over | 5,401,609 | 46,572 | 42,815 to 48,520 | 13,986 | 6,106 | land definition |
| Murray | under to under | 121,808 | 905,523 | 801,061 to 991,917 | 271,935 | 151,868 | none |
| Murrumbidgee-ACT | under to under | 738,895 | 1,533,929 | 1,360,739 to 1,683,767 | 460,650 | 303,975 | none |
| Avon | under to under | 69,727 | 1,080,065 | 1,032,863 to 1,113,424 | 508,513 | 506,614 | none |
| North Tasmania | over to under | 156,393 | 187,593 | 174,487 to 196,161 | 124,822 | 58,798 | none |
| SA Arid Lands | over to under | 8,049 | 28,609 | 27,016 to 30,939 | 10,108 | 8,217 | land definition |
| Eyre Peninsula | under to under | 59,255 | 384,476 | 360,755 to 402,602 | 135,844 | 139,828 | none |

Figure 8 redraws the migration map of Lane et al. (2015) on the corrected 2025 release (2025-fixed). Each region is a proportional circle at its centroid, which is derived from the SA2 centroids, and each circle is sized by population less short-term capacity. The verbal conclusion of the 2015 map was not re-tested, and it is not restated here.

[Figure 8: the 2015 migration map redrawn, population less short-term capacity by region, 2025-fixed, proportional circles on region centroids, from `analysis/paper_a/migration_map.png`]

## 11. Discussion: what would widen the margin

A measure is worth what it does to the constraint that binds. Each measure below was applied alone to the corrected 2025 release (2025-fixed), against a reference of 41.5 million in the short term and 15.6 million in the long term (Supplementary Table S5), and each is free of cost in the model. Short-term capacity is bound by pasture-fed meat and dairy (section 6), so field-crop yields, irrigation and cropland taken from pasture move it by only 0 to 2.4%. Doubling cropland from non-agricultural land, the 1975 CSIRO case (Gifford et al. 1975, as reported in Henry and Godden 1995), raises both terms by 8.7%, to 45.1 and 17.0 million. Supplementary Section S6 gives these measures, which have no read source beyond the model; the five below have one.

### 11.1 Livestock productivity

Livestock output 10% higher raises the short term to 45.5 million (+9.7%) and the long term to 17.1 million (+9.4%), on 2025-fixed. Output 20% higher gives 49.6 million (+19.4%) and 18.6 million (+18.8%). Across five-year averages from 1981-85 to 2006-10, the average daily gain of steers in the national beef herd rose from 0.39 to 0.72 kg (Wiedemann et al. 2015, their Table 1, p. 111). Beef produced per breeding cow mated rose 32%, from 301 to 396 kg, mainly from heavier steers (p. 113).

### 11.2 Diet composition

Setting the meat-and-egg share alone to 5% raises the short term to 76.8 million (+85.0%) and the long term to 19.6 million (+25.7%), on 2025-fixed. A red-meat share of 30% of meat, with more poultry and pork, gives 64.6 million (+55.6%) and 18.5 million (+18.6%). Studies of Australian and global diets give the land and emissions of observed and recommended diets (Hendrie et al. 2014; Tilman and Clark 2014; Ridoutt et al. 2020).

### 11.3 Food waste

The model's 6% setting halves the model's retail-and-consumer loss share, a choice that mirrors UN Target 12.3. Australia's own goal is to halve food waste by 2030 across the whole supply and consumption chain (DCCEEW 2017, pp. 3, 8). The National Food Waste Baseline estimated 7.3 Mt of food waste for 2016-17 (DCCEEW 2019, p. 3) and the 2021 Feasibility Study about 7.6 Mt a year (DCCEEW n.d.); the two are from different projects and are not combined. Section 8 gives the effect of the 6% setting.

### 11.4 Grain reserves

The store sizes of one and two years are the model's own scenarios; no Australian source sets them. With the store resilience tables applied to 2025-fixed, a one-year grain store raises the long term by 48%, to 23.2 million, and a two-year store by 64%, to 25.7 million (section 8). Both rest on the cereal factor. A one-year store is worth the same as planning for a drought of about 16 years instead of 100, and a two-year store about 10 years, read by interpolation between rows of the planning table. On one release, a two-year store (+64%) and drought-proofing (+60%, section 11.5) are the two largest long-term measures, and both act on the worst year. The store is free in the model. A one-year store for domestic use is about 11.5 Mt, about a fifth of an average national cereal crop (Supplementary Section S6). Reserves and trade together set exposure to supply shocks (Marchand et al. 2016).

### 11.5 Drought resilience

Drought-proofing the worst year, so that it loses half as much, moves the 100-year cereal factor for Australia from 0.46 to 0.73 of trend. On 2025-fixed it raises the long term by 60%, to 24.9 million, and leaves the short term unchanged. The Future Drought Fund embodies a shift to supporting preparedness and makes $100 million a year available for drought resilience (Productivity Commission 2023, pp. 3, v).

### 11.6 The regions as a pool

On each zone's own yields and on 2025-fixed, the national short-term capacity is 1.60 times the sum of the capacities of the 53 regions (52 NRM regions and the Northern Territory) in an average year; Supplementary Section S6 gives bad years and the long term. Trade in products between regions recovers at most about 15.5 million people-equivalents in the short term: the national 41.5 million less the regional sum of 26.0 million. In the long term it recovers 9.6 million. This is an upper bound, because it assumes products move without loss or cost. Because bad wheat years are partly correlated across the southern states (Anderson et al. 2019; section 8), a pool of regions does not escape a widespread drought.

### 11.7 Measures the model cannot carry

The capacities assume that all production is eaten at home. In 2021-23 Australia produced 4.66 Mt of meat and ate 2.96 Mt, a surplus of 57% (FAOSTAT 2025). This is a different measure from the model's capacity of 1.50 times the population, and the two are not compared directly. Farmers produce some 93% of the food eaten at home (Lawrence et al. 2013, p. 32). Trade raises supply diversity but also import dependence (Kummu et al. 2020). Supplementary Section S6 gives the other measures the model cannot carry; water and fuel are limitations (section 12). Each measure was applied alone, so the effects are not additive; cost, time and feasibility are not modelled; and settings such as the 5% meat share bound what is possible, not what is likely.

## 12. Limitations and conclusions

The model is a closed land-use account for each region. It carries no trade, disease or biosecurity, and no limits from nutrients, soil or labour. It leaves out Indigenous food systems and wild harvest. Its named climate scenarios scale field-crop yields only; its weather allowance scales every yield by a cereal factor that is untested for pasture. The 2011 inputs were not sampled, and five zones carry older 2011 boundaries.

### 12.1 Self-sufficiency as a policy concept

Self-sufficiency means production relative to consumption, so it does not rule out trade (Clapp 2017, p. 89). Local self-sufficiency is rarely possible: only 11 to 28% of the world's people could meet their demand for a given crop from within 100 km (Kinnunen et al. 2020, p. 229). The closed region of this paper is therefore a bound, not a policy goal.

### 12.2 Urban agriculture and other adaptations

Under forced local self-sufficiency, diet raises capacity at every scale but does not close the scale loss. On 2025-fixed and the state-yield basis, the sum of SA2 capacities stays between 33% and 45% of the national capacity on the same diet (Supplementary Section S7). Swaps within food groups raise the national capacity by about three fifths (+62%) on the improved release (2025-improved), and gardens add little (2025-fixed). Urban agriculture could supply 15.0% of food energy for the residents of the Sydney blocks modelled, in a 25% land-use scenario (Mcdougall et al. 2020, p. 8).

### 12.3 Water for food

The model has no water limit, so its irrigation results are an upper bound. Raising the irrigated share of cropland to 5% adds 2.4% to the 2025 short term (2025-fixed). In the Murray-Darling Basin, median projected streamflow falls about 20% under 2 °C of warming (Prosser et al. 2021, p. 4).

### 12.4 Fuel and energy in food production

The model carries fuel only through its liquid fuel setting, the second-largest long-term setting (section 7). With the biofuel share at 1 and the other settings at their short-term values, the 2025 short term falls from 41.5 to 9.7 million (2025-fixed). Australia's emergency oil stocks equalled 61 days of net imports against an obligation of 90 days (Soliman Hunter and Taylor 2021, PDF p. 11). Energy used after the farm gate is outside the model.

**Conclusions.** First, national short-term capacity rose from 33.3 to 41.5 million on the corrected method. On the average of every ordering of the data layers, the consumption and red-meat-mix layers, the diet with less beef, added 5.6 million, and land and livestock together added 2.4 million, because the two layers share one grazing area; crop yields added 0.2 million. Population changes status, not capacity: people over capacity moved from 0.670 to 0.665 in the short term and from 1.454 to 1.767 in the long term. Second, a 100-year self-sufficient plan covered 69% of the population in 2011 and 57% in 2025. Third, at the base settings the worst of ten years leaves 30.8 million against 27.6 million people in 2025, and the population is 1.05 times capacity in a 1-in-20 year, a failure probability of about 5.8% a year, 1 in 17; across the settings varied the range at each return period contains the population, and the weather allowance is a cereal factor. Fourth, two short-term flips pass the tests in hand (Mackay Whitsunday and North Tasmania), and one long-term flip (South West Queensland). The short-term count of regions over capacity is robust to the method tier, while the long-term count is not. Fifth, on the state-yield basis the sum of SA2 capacities is 37% of the national short-term capacity in 2025, because in the model cropland can carry pasture-fed food but pasture cannot carry crops.

**Data and code availability.** The model, its releases, the data pipeline and the results files that generate every table and figure are in the repository at https://github.com/MurrayLane/carrying-capacity-dashboard (results in its `results/` folder). The claims and sources registers are published with the archive (DOI: [to be added at release]).

---


---

## Appendix: drafter notes (not for the paper)

### From A_s01-04.md
## Drafter notes (not for the paper)

**B117 (revision to the response plan R03a, decisions 100 to 104, 111, 115 to 117).** Sections 1 to 4 and the abstract were revised; every new figure carries a row in `A_s01-04_claims.csv` naming its builder report and checker. Changes by section:
* Abstract: the driver sentence now names livestock, consumption and the red meat mix on the average of all orderings, with the consumption and red-meat-mix layers (5.6 million) and land with livestock (2.4 million, one grazing area) separated; the 1-in-10 and 1-in-20 sentence names the cereal basis and says the Monte Carlo range at each return period contains the population; the 37% carries its basis (state yields) and its mechanism (the substitution rule). Population changes status is dropped from the abstract (it is true by construction; section 4 keeps it).
* Section 1: the 2021 Intergenerational Report, the growth-rate sentence and McDonald are cut (the projections are used in section 8.1 instead); the Lawrence sentence and the sentence on food-related urban planning in 1.4, and four sentences of 1.5 (ABARES 18% profit effect, the $53 billion welfare loss, the simulated farm profit and its caveat), are cut for length.
* Section 2: the 2011 populations are the ABS estimated resident population (23 zones differ from the thesis figures by more than 10%; the national row is kept, ERRATA error 10); the release is `2011-fixed-3` (frozen, decision 116); the cereal factor is described; the Monte Carlo is 19 choices nationally and 13 for the regional flip tests; the model summary, the data sources and the failure probability are in Supplementary Section S8.
* Section 3: every 2011 regional count is on `2011-fixed-3` (long term 35, long-term flips 3); population growth by region is recomputed from `regional_flips-3.csv` (Port Phillip and Westernport +1.28 million, Hawkesbury-Nepean-Sydney +1.01 million, South East Queensland +0.99 million, Murrumbidgee-ACT +141 thousand) and is arithmetic on checked cells, not a register value.
* Section 4: Table 2 is the average of all 362,880 orderings with forward and reverse as bounds; land and livestock are reported together; the livestock share (67%), the diet layers (5.6 million, 68%), the largest-layer counts by region and the Avon arithmetic (supplement) come from B111 and V37.

**Conflicts and limits named, not resolved.**
1. The brief says the long-term land layer is "largest in every ordering". B111 and V37 check the forward walk, the reverse walk and the average (and A365's ranking on all three); not all 362,880 orderings. The text says "the forward walk, the reverse walk and the average".
2. The red-meat share of meat (0.64 to 0.578) and meat-and-egg share (0.13 to 0.12) are from the settings columns of `results/2011-fixed-3.csv` and `results/2025-fixed.csv`. The FAO beef and veal supply (39.1 to 25.9 kg a person, mean of 2010-12 against 2021-23) is from `analysis/consumption_2025/README.md`, quoted by R03a issue 4; no builder and checker pair covers it.
3. The 2011 land windows (five-year mean of 2005-06 to 2009-10, four years for grazing) and the ABS category change of 2016 are from R03a issue 2 reading `analysis/land_2011/README.md`; no checker report covers them.
4. The consumption layer carries the fuel, biofuel and timber presets as well as the diet shares (V37 wording point); the text says so.
5. The Kitagawa and Das Gupta lineage of the decomposition named in the B111 README is not in the literature register and is not cited.
6. Pages: Hochman 2017 actual yields not declining, printed p. 2078; Falster 2024 is cited to its abstract; L012, L013, L014, L062 and L063 have no file on disk (marked "not seen" in the claims csv, not in the prose).
7. Davies is quoted as printed ("In reality, Australia's population growth is highly managed").
8. The subsection numbers follow the outline labels (1.1, 1.4, 1.5, 1.3).

**Register rows touched.** None.


### From A_s05-08.md
### Drafter notes (not for the paper)

**B117 (revision to the response plan R03a, decisions 100 to 104, 111, 115 to 117).** Sections 5 to 8 were revised; every new or changed figure carries a row in `A_s05-08_claims.csv` naming its builder report and checker. Changes by section:
* Section 5: one yield basis in the main text. The curve and Table 3 are on the state-yield basis, named as the conservative bound; the own-yield bound is one sentence in 5.4 and Supplementary Table S6. The substitution rule (cropland can carry pasture-fed food, pasture cannot carry crops) is stated at the head of the section beside the shares. The 2011 regions figure is the state-basis 14.7 million (A075), not the own-yield 21.0 million. The Zumkehr and Campbell sentence and the "On its own yields SA Arid Lands" sentence are cut for length.
* Section 6: the rule is named the substitution rule; one sentence reconciles the national cropland-share test with the thesis finding that cropland share decides capacity (cropland binds only far below the 10% at which the test starts, and decides capacity in a rangeland region).
* Section 7: the 2011 count is 35 (18 under), long-term flips are 3 (two with an artefact flag, one not robust), the net fall is 3 against 1, and the 2011 share of people in over-capacity regions is 93% (from `results/2011-fixed-3.csv`, A144; `long_term_and_measures.mjs` was not rerun). The weather allowance is named as the cereal factor in 7 and 7.2. The 2011 figure lies inside the 2025 long-term range of 13.3 to 18.8 million; the sentence "the change is within the uncertainty" is not used (V41).
* Section 8: ranges on the 1-in-10 and 1-in-20 figures (13-choice draws, B112 and V38), the herd-cycle basis (92% of draws below 27.6 million at 1 in 20, V38 wording), the projections compared with capacity (the 2023 Intergenerational Report and the 2025 Population Statement, held fixed), the cereal factor and the crop-only bound once, the failure probability derived in Supplementary Section S8 (5.8% a year, 1 in 17; Paper B's upper figure of 6.1% is not reproduced by this derivation), Table 6 on `2011-fixed-3` (82% and 91% marked "about"), tipping regions 3 at 1 in 10 and 4 at 1 in 20 in 2011. The export-inclusive count moved to Supplementary Section S9.

**Conflicts and limits named, not resolved.**
1. The shocked ranges 27.0 to 34.0 and 23.0 to 29.0 million are on the 13-choice draws (B112). Decision 115 replaces the 13-choice range with the 19-choice range; the 19-choice draws were run nationally on the average-year capacity and not multiplied by the factor, so no shocked 19-choice figure is printed. The text says the 19-choice range is wider at both ends (31.1 and 49.2 against 36.3 and 45.8). A shocked 19-choice range is a small computation (the national range scales exactly, V38 method point 3).
2. The regional ranges that test the flips are the 13-choice zone ranges (the six added choices were drawn nationally only, B115 limits).
3. V38 method point 1: each draw's own resilience table is not carried into the shock; the release table's factor is applied to every draw. With a draw's own table the ranges would be 26.27 to 33.64 and 22.21 to 28.74 million; 27.6 million is inside both either way. Not printed.
4. The 97% pasture-fed share is at 1 in 10 (V38 method: the pasture-fed rows alone give 31,083,890 against 30,810,607 with the factor on all output, and 41,017,763 with the factor on every other row).
5. The single-year check of the weather factor (2018-19 and 2019-20 near the median, 2020-21 the lowest at 0.90 of it) is in Supplementary Section S4, on the 2025-organic release as built and unverified (A317, X118); it is not in the main text.
6. The failure probability of Paper B (5.8 to 6.1%) and this paper's 5.8% differ at the top end; the coordinator should reconcile.
7. Table 6's 2011 regional sums are capacity sums and do not move; only the population shares and counts moved.
8. A223's value (-26% at a 1-in-10 drought, all yields) is cited in section 6 at its register value; the crop-only bound (-0.8% at 1 in 10, V38) supports its reading and sits in Supplementary Table S10.

**Could not source, left out (carried from the earlier draft).** A113 (the rejected cropland-weighted method), A110 and the urban-garden and diet-scale results of the scale-curve README have no place in the scope's content list. A095 to A097 (own-yield NRM, SA4 and SA3 shares in 2025) are unverified and appear only as cells of Supplementary Table S6. The 2011 own-yield columns have no claim row. The diet-grid results and the Eyre Peninsula result have no claim rows; "cropland binds at every diet tested in SA Arid Lands" rests on `diet_binding_test.mjs` and is stated without a number. A346's statement is "10% to 99%"; the V31b note says the test is flat from 8%. No count of regions is given for the named scenarios (decision 66, N-A3). The 340-litre allowance is described without the CSIRO attribution (L072 not reached). Soliman Hunter 2021 has no printed page numbers; Anderson 2019 has no printed page in the text on disk.

**Register rows touched:** none.


### From A_s09-12.md
### Drafter notes (not for the paper)

**B117 (revision to the response plan R03a, decisions 100 to 104, 111, 115 to 117).** Sections 9 to 12 were revised; every new or changed figure carries a row in `A_s09-12_claims.csv` naming its builder report and checker. Changes by section:
* Section 9: the national range is the widened 19-choice range (31.1 to 49.2 million, factor 1.58, lowest to highest 26.2 to 58.1, factor 2.22; long term 13.3 to 18.8), with the three largest variance shares named and their judgements stated by name (V41); the herd-cycle range (39.4 to 43.8 million; red-meat share 85%) is stated for the 13-choice draws; the "rise holds" sentence follows decision 115 (holds at the base settings and in every single year of data, 2011 lies inside the 2025 range, not a test across the settings); the long-term flips are three; the tier paragraph reports the 2011 counts on the corrected (35) and improved (36) tiers.
* Section 10: North Tasmania's 2011 population is 143,631; the North East Victoria paragraph is cut (it is in section 3); the Hawkesbury, Murray, Avon and SA Arid Lands readings are shortened (the full reading is in Supplementary Section S5).
* Section 11: the stores and drought-proofing results are tied to the cereal factor; the Paper B comparison sentences in 11.2 and 11.6 are cut so the paper stands alone; the industry-forecast sentence (L156, L159), the Wright and Cafiero sentence (L225) and the freight-cost sentence (L172) are cut for length.
* Section 12: the limitations name the cereal factor; the Beltran-Pena, Schreiber, Botterill, Grafton, Ladha-Sabur and D'Odorico sentences are cut (R03a issue 14 asks for shorter literature summaries); the conclusions use the all-orderings average, the cereal basis and the derived failure probability.

**Conflicts and limits named, not resolved.**
1. The long-term count on the improved tier is 36 in both years (2011-improved-3 and 2025-improved), so R03a section (c)'s statement that the long-term fall holds on every tier (3, 4 and 2 regions) no longer holds on the improved tier on the `-3` releases (corrected: 35 to 32; improved: 36 to 36). The text reports both and does not assert a fall on every tier. The published tier was not rerun on the ABS populations (A310's 39 is the old basis).
2. A038 (the not-robust flips) is unchanged on the 13-choice zone ranges. B112 suggests Wet Tropics may leave the not-robust list on the herd-cycle basis; `regional_flips.py` was not rerun on it.
3. The single-year statement (every year from 2016-17 to 2024-25 above 2011) rests on A317, unverified (X118), on the 2025-organic release.
4. The 2011 populations in Supplementary Section S5 (Hawkesbury-Nepean-Sydney 4,394,612; Murray 105,924; Murrumbidgee-ACT 597,750; Avon 60,913; SA Arid Lands 10,613; Eyre Peninsula 57,595) are the ABS cells of `zone_population_2011_comparison.csv` (V36 checked all 53).
5. L012 (Lane et al. 2014), L013 and L014 are not on disk (marked "not seen" in the claims csv, not in the prose).

**Could not source, left out (carried from the earlier draft).** The supporting table of the 2025 range for every zone has no generator. The long-term and drought cells of `regions_in_depth.csv` have no claim rows. No read source is specific to farming in North Tasmania or the arid pastoral country. The 303 kg a person is not printed in its source and no page is given; it is in Supplementary Section S6 only. L062 and L063 are unverified. The scope sources not cited for length are listed in `SECTION_SCOPE.md`. L242 carries no publication year ("DCCEEW n.d."; the page reads "Last updated: 19 December 2025"). The migration map reads `2025-fixed` only, so the 2011 correction does not move it.

**Register rows touched:** none.
