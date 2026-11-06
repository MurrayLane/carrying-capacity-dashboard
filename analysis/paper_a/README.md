# Analyses for Paper A (results), by section

One script per analysis, each reading `results/` and `analysis/comparison_2025/`; the outputs are the tables and figures of `papers/A_results/OUTLINE.md`. Corrected method (`2011-fixed` against `2025-fixed`) unless stated.

## Section 3 and 9: which regional status flips are real (`regional_flips.py`, `regional_flips.csv`)

Run: `python3 -I analysis/paper_a/regional_flips.py` from the repository root. The 53 regions (52 NRM regions and the Northern Territory), short and long term. A flip is a change in the sign of population minus capacity between 2011 and 2025. Each flip is tested three ways: the land-definition and older-boundary flags of `analysis/comparison_2025/movers.csv` (the capacity change is mostly the land layer, or the 2011 zone was drawn on an older boundary); robustness of the 2025 status to the 5th to 95th percentile of the Monte Carlo draws (the 2011 inputs were not sampled, so 2011 has no range); and both.

| | Regions over capacity 2011 | Over capacity 2025 | Flips | Land-definition or boundary artefacts | Not robust to the 2025 range | **Clean and robust** |
|---|---|---|---|---|---|---|
| Short term | 23 | 16 | 9 (8 over to under, 1 under to over) | 3 | 3 | **3** |
| Long term | 36 | 32 | 4 (all over to under) | 3 | 2 | **1** |

**Short-term flips.** Clean and robust: **Mackay Whitsunday, North Tasmania, North East Victoria** (all over to under). Land-definition artefacts: Desert Channels, Southern Gulf, SA Arid Lands. Not robust to the range: Wet Tropics, Rangelands (WA), and Corangamite (the one region that moves from under to over capacity).

**Long-term flips.** Clean and robust: **South West Queensland**. Artefacts: Desert Channels and SA Arid Lands (land definition), Northern and Yorke (older 2011 boundary). SA Arid Lands and Northern and Yorke are also not robust to the range.

**What this means for the paper.** The status-flip headline of the plan (eight regions over to under, one under to over) is three genuine flips in the short term and one in the long term. The net fall in the number of regions over capacity (23 to 16 short term, 36 to 32 long term) is more than the clean flips alone explain; the rest are the flagged and non-robust cases, so the count of regions over capacity is not itself a finding without the tests. Capital cities and the coast stay over capacity in both years.

**Limits.** Robustness is tested on the 2025 range only; a flip also needs its 2011 status to be robust and the 2011 inputs have no draws. The land-definition flag is the rule of `movers.csv` (the land layer alone moves capacity by more than 2 times or less than 0.5). The test of an artefact is on capacity, not on whether the population change is real.

## Section 8: the regions under a bad year (`shocks_by_region.mjs`, `shocks_summary.py`; `shocks_by_region.csv`, `shocks_summary.csv`, `scenarios_by_region.csv`)

Run: `node analysis/paper_a/shocks_by_region.mjs analysis/paper_a/shocks_by_region.csv` then `python3 -I analysis/paper_a/shocks_summary.py` from the repository root. The 52 NRM regions and the Northern Territory (53 regions), corrected method, both vintages, short-term settings, at drought return periods of 1 (average year), 5, 10, 20, 50 and 100 years against the release's own population; and the named scenarios of `results/scenarios.csv` (improved release, 2025). The model's drought allowance scales every yield (crops, pasture products and livestock) by one factor from the 150-year record of wheat, oats and barley (tested: scaling all yields by the 1-in-10 factor of 0.74 reproduces the 1-in-10 capacity exactly).

**Corrected method, national and regional (53 regions):**

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

* **The national margin is gone at a 1-in-20 year in both vintages** (0.89 in 2011, 0.95 in 2025): the nation feeds itself in an average year with 50% to spare, in a 1-in-10 year with about 12%, and not in a 1-in-20 year.
* **About 80% of the population lives in regions that are over capacity even in an average year** (the cities), 85% at a 1-in-10 year and 91% at a 1-in-100, in both vintages: the weather moves the margin of the regions that are already under capacity, not the cities.
* **Regional self-sufficiency fails sooner than national**: the regions together hold 63% of the national capacity in an average year and 55% (16.9 million against a population of 27.6) in a 1-in-10 year.
* **More regions are on the edge in 2025 than in 2011**: five regions are under capacity in an average year and over it at 1 in 10 in 2025 (Wet Tropics, North East Victoria, Rangelands, Mackay Whitsunday, Burnett Mary), one in 2011 (Corangamite).

**Named scenarios (improved reference 2025: 53.6 million short term, 18.5 long term; 15 regions over capacity short term, 36 long term):**

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

* **A field-crop shock barely moves the short term** (-0.3% at 24% lower yields), unlike the drought allowance (-26% at 1 in 10), because the short-term capacity is bound by pasture-fed meat and dairy, not field crops; the allowance bites because it scales every yield, pasture products included. Whether a drought year cuts pasture-fed meat by the same factor as it cuts wheat is not tested here (the herd cycle runs across the years, `analysis/reliability_2025/`).
* **A grain store is worth more than any other single setting in the long term**: one year of stored grain raises long-term capacity by 48% and takes nine regions out of over capacity (36 to 27).
* **Fuel matters in the long term only**: a 340-litre allowance (CSIRO) takes 19% off the long-term capacity.

**Limits.** The regional drought runs use the state's resilience table for each region (the model's rule), so regions of one state tip together; the scenarios are on the improved release and the drought runs on the corrected one, so the over-capacity counts differ (15 and 16).
