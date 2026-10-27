# The long-term settings: what each is worth, and what could be improved

Release `2025-organic`, Australia, long-term settings: **12.3 million** (today's settings: 48.0). The long-term settings are not a forecast. They ask what the land could support if the country planned to be self-sufficient for 100 years of weather,
with a low-meat diet, no avoidable food waste, full nutrient recycling, organic farming, almost no fossil liquid fuel and 30% of the land in reserve. Reproduce: `node analysis/long_term_2025/long_term_levers.mjs analysis/long_term_2025/levers.csv`, then `python3 analysis/long_term_2025/write_readme.py`.

## What each setting is worth (Australia)

"Alone": the short-term settings with only this long-term setting switched on. "Without": the long-term settings with only this one put back to its short-term value. Millions of people (change against the 48.0 and 12.3 baselines).

| Setting (short to long value) | Alone | Without |
|---|---|---|
| resilience (1 to 100) | 21.9 (-54%) | 27.0 (+119%) |
| meategg (0.12 to 0.075) | 54.6 (+14%) | 12.9 (+5%) |
| redmeat (0.578 to 0.5) | 53.0 (+10%) | 12.3 (+0%) |
| activity (1 to 3) | 33.1 (-31%) | 13.8 (+12%) |
| recycling (0 to 1) | 49.2 (+2%) | 11.1 (-10%) |
| losses (0.12 to 0) | 64.1 (+34%) | 11.0 (-11%) |
| organic (0.07 to 1) | 39.4 (-18%) | 15.2 (+23%) |
| fuel (2360 to 253) | 48.1 (+0%) | 1.7 (-86%) |
| biofuel (0.0023 to 1) | 4.6 (-90%) | 18.3 (+49%) |
| fibre (23 to 11.5) | 49.4 (+3%) | 12.1 (-2%) |
| fibreNat (0.5 to 1) | 45.5 (-5%) | 12.3 (+0%) |
| fibreWool (0.12 to 0.9) | 35.5 (-26%) | 12.2 (-0%) |
| timber (0.8 to 5) | 48.0 (+0%) | 12.3 (+0%) |
| infrastr2 (730 to 500) | 48.0 (+0%) | 12.3 (+0%) |
| nature2 (0.26 to 0.3) | 48.0 (+0%) | 12.3 (+0%) |

Timber, infrastructure area and the 30% reserve target change nothing for Australia as a whole (non-agricultural land absorbs them, see below), and the dietary meat share matters less than the headline settings.
**The largest are** the 100-year resilience setting (without it the long term would be 27.0 million), the pair of liquid fuel and biofuel (they act together: see section 2), organic farming, activity level 3, no avoidable waste and full recycling.
The settings are a mix: demanding on resilience, biofuel, activity and organic farming (each lowers capacity), generous on fuel, waste and recycling (each raises it). The long-term figure answers one specific scenario, and the mix has not been checked for coherence.

## 1. The resilience setting is a statistical estimate, and it is the largest lever

| Years of recurrence | 1 | 5 | 10 | 20 | 50 | 100 | 150 |
|---|---|---|---|---|---|---|---|
| Capacity (million) | 27.0 | 23.4 | 20.0 | 16.2 | 14.9 | 12.3 | 9.7 |
| Share of the 1-year figure | 100% | 87% | 74% | 60% | 55% | 46% | 36% |

The setting scales the whole harvest by a factor read from a table (the `resilience` sheet of the workbook). The thesis (chapter 8, Figure 34) built it from the ABS yields of wheat, oats and barley for Australia and each state from 1861 (about 150 years): each year's average grain yield divided by its ten-year moving average,
the years ranked from worst to best, and the rank read as a return period (the worst year in 150 is a one-in-150-year event). For Australia the worst year, 1915, gave 36% of the moving average; the factor at 100 years is 0.46.
This is the most statistical part of the model and the least examined. What could be done:

* **Update the series** with the 15 years since the thesis, which include the 2018-19 drought and the record 2022-23 harvest. The ABS series (7124.0) ended with the 2010-11 edition; later years would have to be stitched from the ABS and ABARES crop data.
* **Use a fitted distribution, not a rank.** A one-in-100 event estimated as about the second-worst of 150 values has a wide uncertainty that the table hides. Fit an extreme-value distribution and report an interval (the capacity at 100 years could be given as a range).
* **Detrend properly.** A ten-year moving average is itself pulled down by droughts and up by booms; a smooth trend would give cleaner deviations. Early years (1915: 0.3 against 0.8 t/ha) reflect the farming practices and the marginal land of the time, which may not recur. Test whether variability has changed.
* **Cover more than three grains**, and pasture and livestock, which the factor also scales.
* **Droughts last several years.** Self-reliance means surviving a run of bad years (the 2001-09 drought, the 1895-1903 drought), not one. A factor for a single year ignores storage and carry-over.
* **Regional zones use their state's curve**, so a small region's variability is understated.
Consistency check with the year-by-year runs (`analysis/reliability_2025/`): the worst of eight recent years gives a long-term capacity about 85% of their mean, about a one-in-eight year; the table gives 0.87 at five years and 0.74 at ten. Recent years do not contradict the table.

## 2. Liquid fuel and biofuel

The long-term settings assume 253 L of liquid fuel a person (a tenth of today's 2,520 L) and that all of it is biofuel grown on the land. Millions of people, Australia:

| Liquid fuel per person (L) | 100% biofuel | 50% biofuel | 30% biofuel | 10% biofuel |
|---|---|---|---|---|
| 253 | 12.3 | 17.5 | 17.8 | 18.1 |
| 500 | 7.2 | 12.4 | 17.3 | 18.0 |
| 860 | 4.5 | 8.1 | 12.1 | 17.7 |
| 1500 | 2.7 | 5.0 | 7.8 | 17.3 |

Capacity is very sensitive to this pair. Outside sources suggest 253 L is optimistic: aviation, heavy freight, mining, rail and shipping are the hard sectors to electrify; secondary reports of a CEFC-commissioned Deloitte study say they would still need up to 30 billion litres by 2050 (about 800 L a person at 35 million people, if the figure is right),
and CSIRO is reported to put the biogenic supply at up to 12.8 billion litres. I have not read either report. The long-term fuel and biofuel settings need a stated source and a transition path (electrification, e-fuels not made from land, biofuel for the remainder), and the pair should be varied together.

## 3. Where the extra reserve comes from

The 30% reserve target is 338 thousand km2 more than the existing reserve in Australia. The model takes reserve and infrastructure land from non-agricultural land first (the arid rangelands), so for Australia this costs nothing.
If instead it came from pasture and cropping in proportion (an "ecologically representative" reserve, in the sense of the Kunming-Montreal framework's Target 3, which asks for protected areas that are ecologically representative; this is from search results, not read in full):

| Zone | Reserve deficit (thousand km2) | Long term, model's rule (million) | Taken from pasture and cropping (million) | Change |
|---|---|---|---|---|
| Australia | 338 | 12.31 | 11.16 | -9.3% |
| NSW and ACT | 164 | 2.13 | 1.43 | -32.8% |
| Victoria | 0 | 0.82 | 0.82 | +0.0% |
| Queensland | 348 | 0.75 | 0.55 | -27.0% |
| South Australia | 3 | 0.89 | 0.89 | -0.7% |
| Western Australia | 177 | 1.86 | 1.45 | -22.4% |
| Tasmania | 0 | 0.03 | 0.03 | -1.6% |
| Northern Territory | 0 | 0.01 | 0.01 | +0.0% |

**Published as the alternate release `2025-reserve`** (an alternate of `2025-resilience`, three formulas changed in Settings!C55:E55, `make_release_reserve.py`): any shortfall of reserve and infrastructure land is shared by cropping, pasture and non-agricultural land in proportion to their areas. This is gentler than the table above, which put the whole shortfall on pasture and cropping.

| Zone | Short term: 2025-resilience | 2025-reserve | Long term: 2025-resilience | 2025-reserve | Change |
|---|---|---|---|---|---|
| Australia | 48.00 | 47.47 | 12.31 | 11.60 | -5.8% |
| NSW and ACT | 11.99 | 11.84 | 2.13 | 1.66 | -22.1% |
| Victoria | 6.96 | 6.92 | 0.82 | 0.82 | +0.0% |
| Queensland | 8.84 | 8.78 | 0.75 | 0.58 | -22.2% |
| South Australia | 2.38 | 2.37 | 0.88 | 0.88 | -0.4% |
| Western Australia | 3.56 | 3.55 | 1.78 | 1.62 | -9.1% |
| Tasmania | 0.30 | 0.29 | 0.03 | 0.03 | -0.1% |
| Northern Territory | 0.06 | 0.06 | 0.01 | 0.01 | +0.0% |

The short term moves by about 1% in Australia only because the short-term reserve setting is the raster share rounded to a whole percent (0.26 against 0.256), which makes a small shortfall. The long-term fall (Australia -6%, New South Wales and Queensland about 22%) comes from the 30% target exceeding the existing reserve. Arid land counted as equal to farmland makes the alternate generous; a reserve weighted toward the productive east and south-west would cost more.

Where the reserve comes from is a large, silent assumption. In the regional zones the reserve and infrastructure settings already change capacity (23 of 60 zones in the short term, 18 in the long term).

## 4. The other long-term settings

* **Avoidable waste 0%** (today 12%, a US figure, SCOPE.md E4) and **recycling 100%**: both extreme. I believe Australia's strategy aims to halve food waste by 2030 (the global target is to halve it; I did not find the Australian document); a ladder of 0%, 50% and the baseline would show what is realistic.
* **Organic 100%** costs 19% of the long-term figure, by the update's factors (Ponisio et al. 2015, Kniss et al. 2016); the nitrogen supply an all-organic system needs (legume rotations, recycling) is not modelled (SCOPE.md E6).
* **Activity level 3** (the most active) adds 12% to the energy needed; it is a population-health assumption, not a physical one, and should be stated as such.
* **Diet**: 7.5% meat and eggs with half of it red meat is a moderate change from today (12%, 58%), not a vegetarian diet. A named reference diet (Australian Dietary Guidelines, or the EAT-Lancet reference diet) with item-level foods would let the long-term diet be checked against nutrition (SCOPE.md E7).
* **Yields are today's.** For a 100-year horizon the yields do not respond to climate change, water limits or soil and nutrient decline (SCOPE.md E2, E3).
