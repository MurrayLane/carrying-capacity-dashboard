# Analyses for Paper A (results), by section

One script per analysis, each reading `results/` and `analysis/comparison_2025/`; the outputs are the tables and figures of `papers/A_results/OUTLINE.md`. Corrected method (`2011-fixed` against `2025-fixed`) unless stated.

## Section 3 and 9: which regional status flips are real (`regional_flips.py`, `regional_flips.csv`)

Run: `python3 -I analysis/paper_a/regional_flips.py` from the repository root. The 53 regions (52 NRM regions and the Northern Territory), short and long term. A flip is a change in the sign of population minus capacity between 2011 and 2025. Each flip is tested three ways: the land-definition and older-boundary flags of `analysis/comparison_2025/movers.csv` (the capacity change is mostly the land layer, or the 2011 zone was drawn on an older boundary); robustness of the 2025 status to the 5th to 95th percentile of the Monte Carlo draws (the 2011 inputs were not sampled, so 2011 has no range); and both.

<!-- generated: analysis/paper_a/make_readme_tables.py regional_flips -->
<!-- source: regional_flips.csv; commit: ff3945b -->
| | Regions over capacity 2011 | Over capacity 2025 | Flips | Land-definition or boundary artefacts | Not robust to the 2025 range | **Clean and robust** |
|---|---|---|---|---|---|---|
| Short term | 23 | 16 | 9 (8 over to under, 1 under to over) | 3 | 3 | **3** |
| Long term | 36 | 32 | 4 (all over to under) | 3 | 2 | **1** |
<!-- end generated -->

**Short-term flips.** Clean and robust: **Mackay Whitsunday, North Tasmania, North East Victoria** (all over to under). Land-definition artefacts: Desert Channels, Southern Gulf, SA Arid Lands. Not robust to the range: Wet Tropics, Rangelands (WA), and Corangamite (the one region that moves from under to over capacity).

**Long-term flips.** Clean and robust: **South West Queensland**. Artefacts: Desert Channels and SA Arid Lands (land definition), Northern and Yorke (older 2011 boundary). SA Arid Lands and Northern and Yorke are also not robust to the range.

**What this means for the paper.** The status-flip headline of the plan (eight regions over to under, one under to over) is three genuine flips in the short term and one in the long term. The net fall in the number of regions over capacity (23 to 16 short term, 36 to 32 long term) is more than the clean flips alone explain; the rest are the flagged and non-robust cases, so the count of regions over capacity is not itself a finding without the tests. Capital cities and the coast stay over capacity in both years.

**Limits.** Robustness is tested on the 2025 range only; a flip also needs its 2011 status to be robust and the 2011 inputs have no draws. The land-definition flag is the rule of `movers.csv` (the land layer alone moves capacity by more than 2 times or less than 0.5). The test of an artefact is on capacity, not on whether the population change is real.

## Section 8: the regions under a bad year (`shocks_by_region.mjs`, `shocks_summary.py`; `shocks_by_region.csv`, `shocks_summary.csv`, `scenarios_by_region.csv`)

Run: `node analysis/paper_a/shocks_by_region.mjs analysis/paper_a/shocks_by_region.csv` then `python3 -I analysis/paper_a/shocks_summary.py` from the repository root. The 52 NRM regions and the Northern Territory (53 regions), corrected method, both vintages, short-term settings, at drought return periods of 1 (average year), 5, 10, 20, 50 and 100 years against the release's own population; and the named scenarios of `results/scenarios.csv` (improved release, 2025). The model's drought allowance scales every yield (crops, pasture products and livestock) by one factor from the 150-year record of wheat, oats and barley (tested: scaling all yields by the 1-in-10 factor of 0.74 reproduces the 1-in-10 capacity exactly).

**Corrected method, national and regional (53 regions):**

<!-- generated: analysis/paper_a/make_readme_tables.py shocks_summary -->
<!-- source: shocks_summary.csv; commit: ff3945b -->
| | Return period | National capacity over population | Regions over capacity | Population living in over-capacity regions | Sum of regional capacities over national |
|---|---|---|---|---|---|
| 2011 | average year | 1.49 | 23 | 82% | 0.63 |
| 2011 | 1 in 10 | 1.11 | 24 | 84% | 0.56 |
| 2011 | 1 in 20 | 0.89 | 27 | 87% | 0.53 |
| 2011 | 1 in 100 | 0.68 | 33 | 92% | 0.47 |
| 2025 | average year | 1.50 | 16 | 81% | 0.63 |
| 2025 | 1 in 10 | 1.12 | 21 | 85% | 0.55 |
| 2025 | 1 in 20 | 0.95 | 24 | 89% | 0.51 |
| 2025 | 1 in 100 | 0.69 | 28 | 91% | 0.46 |
<!-- end generated -->

* **The national margin is gone at a 1-in-20 year in both vintages** (0.89 in 2011, 0.95 in 2025): the nation feeds itself in an average year with 50% to spare, in a 1-in-10 year with about 12%, and not in a 1-in-20 year.
* **About 80% of the population lives in regions that are over capacity even in an average year** (the cities), 85% at a 1-in-10 year and 91% at a 1-in-100, in both vintages: the weather moves the margin of the regions that are already under capacity, not the cities.
* **Regional self-sufficiency fails sooner than national**: the regions together hold 63% of the national capacity in an average year and 55% (16.9 million against a population of 27.6) in a 1-in-10 year.
* **More regions are on the edge in 2025 than in 2011**: five regions are under capacity in an average year and over it at 1 in 10 in 2025 (Wet Tropics, North East Victoria, Rangelands, Mackay Whitsunday, Burnett Mary), one in 2011 (Corangamite).

**Named scenarios (improved reference 2025: 53.6 million short term, 18.5 long term; 15 regions over capacity short term, 36 long term):**

<!-- generated: analysis/paper_a/make_readme_tables.py named_scenarios -->
<!-- source: scenarios_by_region.csv; commit: ff3945b -->
| Scenario | Short term | Long term | Regions over capacity, long term |
|---|---|---|---|
| Field-crop yields 12% lower | -0.1% | -0.4% | 36 |
| Field-crop yields 24% lower | -0.3% | -5.3% | 36 |
| Waste at the national target (6%) | +8.7% | -4.1% | 36 |
| No avoidable waste | +17.3% | 0% | 36 |
| Recycling none or half | -0.1% | -0.1% to -0.2% | 36 |
| Liquid fuel 156 litres (electric vehicles) | 0% | +1.0% | 35 |
| Liquid fuel 340 litres (CSIRO) | 0% | -18.8% | 37 |
| Grain store of one year | 0% | **+48%** | 27 |
| Grain store of two years | 0% | **+64%** | 25 |
<!-- end generated -->

* **A field-crop shock barely moves the short term** (-0.3% at 24% lower yields), unlike the drought allowance (-26% at 1 in 10), because the short-term capacity is bound by pasture-fed meat and dairy, not field crops; the allowance bites because it scales every yield, pasture products included. Whether a drought year cuts pasture-fed meat by the same factor as it cuts wheat is not tested here (the herd cycle runs across the years, `analysis/reliability_2025/`).
* **A grain store is worth more than any other single setting in the long term**: one year of stored grain raises long-term capacity by 48% and takes nine regions out of over capacity (36 to 27).
* **Fuel matters in the long term only**: a 340-litre allowance (CSIRO) takes 19% off the long-term capacity.

**Limits.** The regional drought runs use the state's resilience table for each region (the model's rule), so regions of one state tip together; the scenarios are on the improved release and the drought runs on the corrected one, so the over-capacity counts differ (15 and 16).

## Section 7: the long term by region (`long_term_and_measures.mjs`; `long_term_regions.csv`, `long_term_levers.csv`)

Run: `node analysis/paper_a/long_term_and_measures.mjs analysis/paper_a` from the repository root (also writes `measures.csv`, `store_equivalence.csv`, `transfers.csv`, below). Long-term settings (100-year allowance, low-meat diet, no avoidable waste, full recycling, organic, almost no fossil liquid fuel, 30% reserve), corrected method.

<!-- generated: analysis/paper_a/make_readme_tables.py long_term_national -->
<!-- source: long_term_regions.csv; commit: ff3945b -->
| | Nation, capacity over population | Regions over capacity (of 53) | Regions under capacity | Population living in over-capacity regions | Sum of regional capacities over the national |
|---|---|---|---|---|---|
| 2011 | 15.4 / 22.3 = 0.69 | 36 | 17 | 94% | 5.1 / 15.4 = 33% |
| 2025 | 15.6 / 27.6 = 0.57 | 32 | 21 | 94% | 6.0 / 15.6 = 38% |
<!-- end generated -->

* **Regions that can feed themselves in the long term** (2025, ratio of capacity to population): the cropping belts and the inland plains: South Coast WA (8.1), Avon (7.3), Border Rivers - Maranoa - Balonne (7.1), Western NSW (6.1), Border Rivers - Gwydir (4.6), Northern Agricultural (3.9), Northern Gulf, South West Qld, Lachlan and others. The 17 of 2011 (the thesis's "13 of 60" corrected) become 21.
* **94% of the population lives in regions that are over capacity in the long term, in both years**: the plan fails where people live, not where food is grown, and the regions together hold only 33% to 38% of the national capacity.
* **The gap widened because the population grew, not because capacity fell**: capacity 15.4 to 15.6 million (inside the uncertainty range) against a population up 24%.

**What each long-term setting is worth** (Australia, 2025; millions; "without" is the long-term settings with this one put back to its short-term value, against 15.6):

<!-- generated: analysis/paper_a/make_readme_tables.py long_term_levers -->
<!-- source: long_term_levers.csv; commit: ff3945b -->
| Setting | Without it (long term becomes) |
|---|---|
| 100-year drought allowance | 34.3 (+119%) |
| Liquid fuel (2,360 to 210 litres a person) | 3.7 (-76%) |
| No avoidable waste | 13.0 (-17%) |
| Organic farming | 19.0 (+22%) |
| Activity level 3 | 16.2 |
| Biofuel share | 16.1 |
| Fibre (23 to 11.5) | 11.1 (-29%) |
| Fibre from natural sources (0.5 to 1) | 19.7 (+26%) |
| Fibre from wool (0.12 to 0.9) | 22.8 (+46%) |
| Red-meat share, meat and egg share | 14.7 and 11.7 (both help capacity) |
| Timber, infrastructure area, the 30% reserve | 15.6 (no effect: non-agricultural land absorbs them) |
<!-- end generated -->

The weather allowance, then fuel, is the long term's largest lever on both sides: the long-term figure is mainly a statement about planning for bad years. The 2011 table (`long_term_levers.csv`) has the same order.

## Ameliorative measures, tested one at a time (`measures.csv`, `store_equivalence.csv`, `transfers.csv`)

Australia, 2025, corrected method; each measure applied alone to the short-term and long-term settings (millions of people; change on 41.5 and 15.6):

<!-- generated: analysis/paper_a/make_readme_tables.py measures -->
<!-- source: measures.csv, scenarios_by_region; commit: ff3945b -->
| Measure | What it does in the model | Short term | Long term |
|---|---|---|---|
| Field-crop yields +10% / +20% | wheat, barley, other field crops, cotton | 41.5 (+0.1%) / 41.5 (+0.1%) | 15.7 (+0.2%) / 15.7 (+0.3%) |
| Horticulture yields +10% | vegetables, fruit, nuts | 41.5 (0%) | 15.6 (+0.2%) |
| **Livestock output +10% / +20%** | meat, wool and milk per hectare | **45.5 (+9.6%) / 49.5 (+19.2%)** | **17.1 (+9.4%) / 18.6 (+18.7%)** |
| All yields +10% | every food yield | 45.6 (+9.8%) | 17.2 (+9.8%) |
| **Drought-proofing: the worst year loses half as much** | long term, the 100-year factor 0.46 to 0.73 | n/a | **24.6 (+57%)** |
| Irrigated share of cropland 2% / 5% (now 0.7%) | more irrigation; water not constrained | 41.8 (+0.7%) / 42.5 (+2.4%) | 15.7 (+0.7%) / 16.0 (+2.4%) |
| Waste at the national target (6%) | avoidable waste 0.06 | 48.3 (+16%) | 14.3 (-8.2%; the long-term settings assume no avoidable waste, so a 6% target is a step back) |
| No avoidable waste | avoidable waste 0 | 55.3 (+33%) | n/a |
| Full recycling of food waste | recycling 1 | 42.4 (+2.2%) | n/a (already 1) |
| Cropland +25% taken from pasture | more cropping, less pasture | 41.5 (0%) | 15.6 (0%) |
| Cropland doubled from non-agricultural land | the 1975 CSIRO case | 45.1 (+8.7%) | 17.0 (+8.7%) |
| **Diet: meat and eggs 5% of the diet** | the meat and egg share | **76.8 (+85%)** | **19.6 (+26%)** |
| Diet: meat and eggs 7.5% | | 48.2 (+16%) | n/a (already 7.5%) |
| **Diet: red meat 30% of meat (more poultry and pork)** | red-meat share of meat | **64.6 (+56%)** | **18.5 (+19%)** |
| Liquid fuel 156 litres a person | electrified transport | 41.5 (+0.1%) | 15.7 (+0.8%) |
| Grain store of one year / two years (improved release, `results/scenarios.csv`) | a buffer against the weather | 0% | **+48% / +64%** |
<!-- end generated -->

**What the grain store is worth in years of weather** (improved release, long term; `store_equivalence.csv`): a one-year store lifts the long-term figure to 27.4 million, the same as planning for a drought of about 16 years instead of 100; a two-year store (30.4 million) is equivalent to planning for about a 10-year drought.

**The regions as a pool** (`transfers.csv`, 2025 corrected, short term): in an average year the regions over capacity are short by 20.7 million people-equivalents and the regions under capacity have 19.1 million to spare, against a national surplus of 13.9 million. At a 1-in-10 year the excess is 21.5 million and the regional spare 10.8 million (national surplus 3.2). The national capacity is 1.6 to 1.8 times the sum of regional capacities because the regions' pasture and cropland complement each other: exchanging products between regions (trade within the country) recovers the pooling gap, about 15.5 million people-equivalents short term and 9.6 million long term.

**Reading.**
* **What binds decides what helps.** Short-term capacity is set by pasture-fed meat and dairy, so measures aimed at field crops (yields, irrigation, more cropland) do almost nothing (0 to 2.4%), while measures aimed at pasture-fed livestock and the diet's composition do a lot (livestock output +10% gives +9.6%; the meat and egg share down to 5%, +85%; a switch from red to white meat, +56%). The long term is set by the weather allowance, so drought-proofing and storage matter most (+57%; +48% to +64%).
* **Nothing but diet, waste and livestock productivity moves the short term by more than 10%** (livestock output +20% gives +19%).

**Limits.** One measure at a time on the corrected release (the grain store on the improved release, where the stores were built); the effects are not additive; cost, time and feasibility are not modelled; the store is free in the model; irrigation is not water-limited; the yield increases are applied to every region at once.

## Section 9(b): the effect of each method choice region by region (`method_effects_by_region.py`, `plot_method_effects.py`; `method_effects_by_region.csv`, `method_effects_summary.csv`, `method_status.csv`, `method_effects_heatmap.png` and `.svg`)

Run: `python3 -I analysis/paper_a/method_effects_by_region.py` then `python3 -I analysis/paper_a/plot_method_effects.py` from the repository root. Each module's effect alone is the capacity change when only that module is applied to the published-method release, as a share of the published capacity (2025 data; 2011 alongside in the CSVs). The two corrections are biodiesel-yield and beef-carcase-yield; the other six are improvements. Figure 7 is the heat map (two panels, 53 regions, diverging scale clipped at 40%, cells of 10% or more labelled).

**National effect alone and regional spread (2025, % of published):**

<!-- generated: analysis/paper_a/make_readme_tables.py method_effects_national -->
<!-- source: method_effects_summary.csv; commit: ff3945b -->
| Module | Tier | Short term: nation (regional min to max) | Long term: nation (regional min to max) |
|---|---|---|---|
| Beef carcase yield 0.705 | correction | -16.0 (-21.5 to 0) | 0 (-7.7 to 0) |
| Biodiesel yield | correction | +0.1 (0 to +6.9) | +20.7 (+3.4 to +97.9) |
| Australian loss factors | improvement | +11.2 (+0.8 to +22.6) | 0 |
| Dairy on land that can carry it | improvement | +20.2 (-27.3 to +22.1) | +3.0 (-12.4 to +53.1) |
| Beef output by state | improvement | 0.0 (-7.4 to +9.9) | 0.0 (-5.0 to +3.9) |
| Reserve pro rata | improvement | -1.1 (-5.4 to 0) | -5.8 (-29.1 to 0) |
| Recycling by stage | improvement | +0.1 (0 to +4.3) | -9.7 (-18.2 to -1.5) |
| Organic ruminant factor | improvement | 0 | 0 (0 to +7.6) |
<!-- end generated -->

**What it shows**
* **The two corrections act in different places.** The beef carcase correction lowers the short term by 16% nationally, by 10% to 22% in 17 beef and cropping regions and by 3% to 9% in eight more (Wet Tropics -22%, Lower Murray Darling -16%, the Murray-Darling basin regions -14% to -16%), and nothing elsewhere. The biodiesel correction is a long-term correction (+21% nationally) and +50% to +98% in the coastal and northern regions (South East Queensland +98%, Burdekin +96%, South Tasmania +84%), almost nothing there in the short term (in the long term Avon +19% and South Coast WA +16%).
* **Dairy on good land is the largest improvement and the one that moves regions in both directions** (+20% nationally, -27% to +22% by region): it lowers the arid and northern regions that had been credited with dairy at the pasture average (SA Arid Lands -27%, Southern Gulf -16%) and raises the dairy-dependent and rangeland regions (Wet Tropics, Rangelands, Lower Murray Darling +22%; Rangelands +53% in the long term).
* **Beef output by state redistributes without changing the national figure** (0.0% nationally, -7% to +10% by region): the southern and Murray-Darling regions gain (Lower Murray Darling +10%, Murrumbidgee +9%), the west and north lose (Northern Agricultural, Wet Tropics, Avon -7%).
* **Australian loss factors raise every region in the short term, by 1% to 23% (median 9%)** (Swan +23%, Southern Gulf +18%, Mackay Whitsunday +15%).
* **Reserve pro rata and recycling by stage act in the long term only** and lower it (reserve -29% in Condamine, -28% in Lower Murray Darling; recycling -18% in the arid regions): the long-term improvements pull in the opposite direction to the short-term ones.

**Status under each tier (regions over capacity, of 53):**

<!-- generated: analysis/paper_a/make_readme_tables.py method_status -->
<!-- source: method_status.csv; commit: ff3945b -->
| | Published | Corrected | Improved | Regions that change status, corrected to improved |
|---|---|---|---|---|
| 2025 short term | 15 | 16 | 15 | Corangamite |
| 2025 long term | 36 | 32 | 36 | Mallee, Kangaroo Island, SA Arid Lands, SA Murray Darling Basin, South East SA, South West WA |
| 2011 short term | 22 | 23 | 22 | Mackay Whitsunday |
| 2011 long term | 39 | 36 | 38 | Western NSW, South East SA |
<!-- end generated -->

* **The short-term count of over-capacity regions is robust to the method tier (15, 16, 15) but the long-term count is not (36, 32, 36)**: six regions in the south and west change status between the corrected and improved long term. The long-term regional picture therefore depends on judgement-based method choices as well as on the weather allowance, and the six are the regions that sit closest to their population.

**Limits.** Effects are one at a time (the interaction is not small nationally: in 2025 the modules together give +4.25 million short term where the sum of their effects alone would give 7.1, an interaction of -2.9; the long-term correction effect applied in sequence is +10% on the published figure, not the +21% of the biodiesel module alone; see `results/method_effects.csv`); the share of the published capacity is not defined where the published capacity is near zero (Alinytjara Wilurara, a blank row in the figure); the colour scale is clipped at 40%, so the largest long-term biodiesel effects (up to +98%) show as the darkest blue and are read from the labels.
