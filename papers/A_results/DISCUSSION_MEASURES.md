# Paper A, section 11 (draft for Murray): what would widen the margin

Drafted 2026-11-06. The measures are tested one at a time on the model (`analysis/paper_a/README.md`, `analysis/paper_a/measures.csv`), the rest are ideas the model cannot carry and are discussed, not measured. Numbers are Australia, 2025, corrected method unless stated (short term 41.5 million, long term 15.6; population 27.6).

## The frame: what binds decides what helps
Short-term capacity is set by pasture-fed meat and dairy, so measures aimed at field crops do almost nothing and measures aimed at livestock, diet and waste do a lot. The long term is set by the weather allowance: the weather allowance is the largest single setting, and drought-proofing (+60%) and a two-year grain store (+64%) are the two largest measures, both acting on the worst year. A measure is worth what it does to the binding constraint.

## A. Tested on the model

| Measure | Short term | Long term | Reading |
|---|---|---|---|
| Grain store, one year / two years (improved release) | 0% | +48% / +64% | equal to planning for a 16-year or a 10-year drought instead of 100 |
| Drought-proofing farming (worst year loses half as much) | n/a | +60% | the weather allowance is the largest single setting; drought-proofing (+60%) and a two-year grain store (+64%) are the two largest measures, both acting on the worst year |
| Livestock output +10% / +20% | +9.7% / +19.4% | +9.4% / +18.8% | herd productivity and pasture improvement go straight to the binding constraint |
| Meat and eggs 5% of the diet | +85% | +26% | on the corrected release the model's best meat-and-egg share is 2.5% (118.0 million against 112.4 with none and 76.8 at 5%; `diet_scale.csv`; a little pasture-fed meat uses land crops cannot) |
| Red meat 30% of meat (more poultry and pork) | +56% | +19% | shifts food from pasture to feed grain |
| Avoidable waste at the national target (6%) / none | +16% / +33% | -8.2% (14.3) / 0% | the long-term settings already assume none, so the 6% target is a step back |
| Full recycling of food waste | +2.2% | already assumed | feed-grade, lawful waste only |
| Cropland doubled from non-agricultural land | +8.7% | +8.7% | the 1975 CSIRO case |
| Irrigated share of cropland 2% / 5% (now 0.7%) | +0.7% / +2.4% | the same | water is not a constraint in the model, so this is an upper bound |
| Field-crop yields +10% / +20% | +0.1% | +0.2% to +0.3% | field crops are not what binds |
| Cropland +25% taken from pasture | 0% | 0% | in the model cropland can carry pasture-fed products but pasture cannot carry crops, so capacity is the same for any cropland share from 10% to 99% of the combined area and moving land from pasture to cropping changes nothing while cropland stays above its own need (reading from an evaluator test, not from the workbook formulas) (national pasture need 3.49 million km2 against 3.32 held, the gap met from spare cropland; the 1.96 million km2 unused is non-agricultural land) |
| Liquid fuel 156 litres (electrified transport) | +0.1% | +0.8% | fuel matters only in the long-term settings (without the low-fuel setting the long term is 3.7 million) |

## B. Implied by what the model assumes (the model's capacity already contains them)

* **Export diversion.** The capacity figures assume all production is eaten at home. In 2021-23 Australia produced 4.66 million tonnes of meat and ate 2.96 (a surplus of 57%, the model's 1.5 times); two thirds of beef goes abroad. A margin of 1.5 times in an average year therefore exists only if exports yield to domestic need in a bad year. At a 1-in-10 year meat production falls to about 3.45 million tonnes, still above domestic use; at a 1-in-20 year it is 2.95, level with it: the model's margin vanishes at 1 in 20. Whether markets, contracts and governments would divert exports is a policy question the model assumes away, and the figures are an upper bound without it.
* **The herd as a store.** In a drought the herd is sold down, so meat supply rises for a year and falls for several after (the single-year capacity runs 43.5 to 55.4 million across 2016 to 2025 with the herd cycle). A model with one allowance for all yields misses the lag.
* **A store covers every yield in the model, not just grain.** A grain store protects crop food; the binding food is pasture-fed meat and dairy, whose analogue is a fodder reserve that holds the herd through a drought. The size of a one-year grain store for domestic use is about 11.5 million tonnes (3.1 for direct use at 112 kg a person and 8.4 for the feed grain embodied in meat, Foran and Poldy's 303 kg a person), about a fifth of an average national cereal crop (52.6 million tonnes).

## C. The regions as a pool

In the short term the national capacity is 1.60 times the sum of the regions' in an average year and 1.82 at a 1-in-10 year, because pasture and cropland complement each other across regions; in the long term it is 2.60 times in 2025 (3.00 in 2011). Trade in products between regions (the transport, processing and cold-chain system) recovers about 15.5 million people-equivalents in the short term and 9.6 in the long term (where the multiplier is 2.60). In an average year the over-capacity regions are short by 20.7 million people-equivalents and the others have 19.1 million to spare; at a 1-in-10 year the shortfall is 21.5 and the spare 10.8. Measures that raise interregional capacity (rail and road freight, cold chain, regional processing) are a measure of the margin as much as farm output is.

## D. Ideas the model cannot carry, to discuss

1. **Imports and trade diversification.** Australia's fish imports (593 thousand tonnes) are about as large as its food use of fish (641) and it imports much of its fruit, vegetables and pork; the commodity balance finds fish, not grain or meat, the item that runs out first (12 to 17 million people). Trade is the buffer a closed-system capacity leaves out; the opposite risk is dependence on a few trading partners.
2. **Aquaculture and fishery management.** The only commodity in deficit in Foran and Poldy's balance. Fish need grain and fish meal (two to four kilograms of grain per kilogram), so the gain moves the constraint.
3. **Strategic stocks of other kinds.** Pulses (4.4 million tonnes produced, mostly exported, long shelf life), frozen or canned protein, seed stocks.
4. **Seasonal forecasting and early warning.** Better forecasts let growers adjust sowing and stocking before a drought, which narrows the worst-year loss: the same effect as drought-proofing without the farming change.
5. **Crop and regional diversification.** The national worst year (the 100-year factor 0.46 of trend) is milder than the factors of New South Wales (0.30), Victoria (0.22), Queensland (0.35) and South Australia (0.36), because the states do not fail together, though not milder than Western Australia's (0.49) or Tasmania's (0.67); spreading production across regions and varieties lowers national variability, and a region that depends on its own state's weather alone carries the harsher state factor.
6. **Water.** Storage, efficiency and desalination for horticulture; the model has irrigation as a share of cropland, with no water limit.
7. **Fuel and energy security.** Farm diesel is the long term's biggest hidden dependence (without the low-fuel setting the long term falls to 3.7 million); on-farm electrification or biodiesel competes for land (switching the biofuel share to 1 with today's other settings cuts the short-term figure to 9.7; `analysis/paper_a/long_term_levers.csv`).
8. **Population distribution.** In the long term 94% of the population lives in regions that are over capacity; settlement policy changes where food must travel, not the national capacity.
9. **Household and community resilience.** Stockpiles, community and household gardens (earlier tests: gardens add little; fruit and vegetables are 7% of cropland), local procurement. Small in the model, large in what people can do in a shortfall.
10. **Finance and insurance.** Crop insurance, drought finance, futures: they move the cost of a bad year, not the supply.

## E. Cautions
* The effects are one at a time and not additive; cost, time, feasibility and side effects (emissions from more livestock, water for irrigation, fuel for stores) are not modelled.
* The grain-store, drought-proofing and herd-productivity effects rest on the model's uniform weather factor on every yield; a drought that hits pasture and wheat differently is not tested.
* Several measures (the 5% meat share, no waste) are policy settings far from today's practice; they bound what is possible, not what is likely.
