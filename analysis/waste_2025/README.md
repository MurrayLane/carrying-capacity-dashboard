# Avoidable food waste and recycling (SCOPE.md E4 and E15)

**Two lines.** This page is line 1: the thesis method on current data (release `2025-fuel`). Line 2, the improved recycling method (split by stage, origin and dry matter; release `2025-recycling-stage`), is `README_stages.md`.

## What the setting is

The model's **avoidable waste** setting is the retail and consumer waste that could be avoided, as a share of all food produced: 12% by default, adjustable from 0 to 20% (thesis section 8.3.6). The thesis built the 12% item by item for its 746 foods from US data, because it found no detailed Australian figures:
retail loss averaged 10% (Buzby and Wells, USDA) and consumer loss, in households and food service, 22% (Muth et al., USDA), unweighted averages; a UN study (Gustavsson 2011) had put Australia in the same group as the United States and Canada.
Inedible parts, cooking losses and processing losses are not adjustable. **Recycling** (0% today, 100% in the long term) returns the nutrients of avoidable waste to farming.
The long-term setting of 0% avoidable waste is the thesis's fossil-free, frugal scenario; the national strategy target is a 50% cut.

## What Australia has measured since

The National Food Waste Baseline (Arcadis, 2019, for 2016-17) found 7.3 million tonnes of food waste (298 kg a person). The updated baseline in the National Food Waste Strategy Feasibility Study (FIAL, 2021, 2018-19 data), which Australia tracks its target against, is **7.6 million tonnes, 312 kg a person**, with this split by stage (as reported by the OECD, *A Stocktaking of Food Loss and Waste Policies: Australia*, 2025):

| Primary production | Food processing | Wholesale | Retail | Hospitality and food services | Public food procurement | Households |
|---|---|---|---|---|---|---|
| 22% | 17% | 3% | 7% | 16% | 3% | 32% |

The national target is to halve food waste across the whole chain by 2030 (Roadmap, FIAL 2020; National Food Waste Strategy 2017). I found no official measurement after 2018-19 (one non-official site reports food waste to landfill falling from 127 to 102 kg a person between 2016-17 and 2022-23; unverified).

## Is the 12% about right?

* Retail, hospitality, procurement and household waste, the stages the thesis counts as retail and consumer losses, are 58% of 312 kg: about **181 kg a person a year**. This includes parts that cannot be eaten.
* The FAO food supply for Australia is about 895 kg a person (mean 2021-23, `data/2025/consumption_proxies.json`), so that waste is about **20%** of the food supply if every kilogram counts, and about **14%** if only the edible part does (the FIAL feasibility study, which holds the baseline, states that Australia's food waste is 70% edible and 30% inedible overall; the split by stage is only in a figure I could not read).
* The thesis's denominator is food produced, which is larger than the food supply at retail, so its percentage would be a little lower than these.
* **So the Australian evidence is consistent with the thesis's 12%** within what the definitions and the overall edible share (the split by stage is not available) allow, roughly 12 to 14%. It does not show that the US figure was wrong. I have kept 12% (SCOPE.md rule: if in doubt, 2011) and not built a release. The FIAL feasibility study (2021) is the primary source used here; the original Arcadis 2019 report was not reachable (agriculture.gov.au and dcceew.gov.au are blocked from the assistant's environment).

## Where the waste actually goes

The thesis said that almost no food waste is recycled into the food system, because feeding scraps to pigs is illegal and plant and animal scraps are hard to separate, so "most animal and plant scraps are sent to land-fill only" (section 8.3.7). Its recycling setting is therefore animal feed only (compost was left out for want of data).
The FIAL feasibility study (2021, 2018-19 data, Table 3) gives the destination of every stage's waste. Thousand tonnes a year (`fial_destinations.csv`):

| Destination | Households | Hospitality | Retail | Public food procurement | Manufacturing |
|---|---|---|---|---|---|
| Landfill | 1,788 | 830 | 286 | 249 | 79 |
| Composting (home and commercial) | 524 | 131 | 216 | 2 | 773 |
| Sewer (wastewater treatment) | 151 | 257 | 0 | 0 | 328 |
| Anaerobic digestion, energy | 0 | 0 | 24 | 0 | 44 |
| On-farm disposal | 0 | 0 | 0 | 0 | 52 |
| Total waste | 2,463 | 1,218 | 526 | 251 | 1,276 |
| Recovered as animal feed (not counted as waste) | 0 | 0 | 68 | 0 | 6,253 |
| Other recovery (food rescue, new food, non-food products, export) | 0 | 0 | 35 | 0 | 3,602 |

* **For the stages the avoidable-waste setting covers (retail, hospitality, procurement, households: 4,458 thousand tonnes of waste) the thesis was right about animal feed and landfill.** Of those tonnes and the 103 recovered at retail, **69% goes to landfill, 19% is composted, 9% goes down the sewer, 1.5% to animal feed and 0.8% to food rescue.** Households send 73% of their food waste to landfill and 21% to compost.
* **Composting is a real route the model does not count** (19% of consumer-level waste; the thesis left it out for lack of data on compost and yields). It returns nutrients rather than feed, so its effect on capacity is unknown; leaving it out is conservative.
* **The thesis missed the largest recycling route, which is upstream.** Food manufacturing sends **6.25 million tonnes a year to animal feed** (56% of all its residual streams: bran, molasses, oilseed meal, brewers' grains, whey and the like), 6.5 million tonnes with the other stages. The national baseline does not count this as waste. The model's processing yields (canola seed to oil 42%, wheat to flour 129%) show the by-product as a loss; in reality most of it is already feed.
* **The legal limit is real.** Feeding food waste containing meat or dairy to pigs or ruminants is banned in every state and territory (and to poultry in Queensland). The long-term setting of 100% recycling assumes all scraps can be fed, which today's rules allow for plant waste only.

What this means for the model's two settings:

1. **Short-term recycling of 0% is right for consumer-level waste and too low for processing waste.** The processing residues are already feed. Line 2 measured it (`README_stages.md`): weighting each stage's feed pool by what was fed in 2018-19 gives 16% in the short term, worth 0.06 million people.
2. **Long-term recycling of 100% is the thesis's scenario and is not feasible.** Measured in line 2 (`README_stages.md`): the thesis counts wet grams against dry-feed ratios, feeds animal-origin waste (48% of the short-term pool), counts shells, bagasse and pomace as feed, and at 100% feeds the whole pig, poultry, egg and farmed fish industry on waste. The best systems in the world (Japan, South Korea, with the law changed) feed about 40% of their food waste. Corrected and at 40% uptake, long-term capacity falls from 14.05 to 12.71 million.
3. Neither moves the headline much, because recycling has little leverage in the model; avoidable waste itself (below) has far more.

## What the setting is worth

Capacity of Australia, millions of people, release `2025-fuel`, by level of avoidable waste (`ladder.mjs`, `ladder.csv`):

| | 20% | 14% | 12% | 9% | 6% | 3% | 0% |
|---|---|---|---|---|---|---|---|
| Short term (recycling 0%) | 37.6 | 45.4 | 48.0 | 52.0 | 56.0 | 60.0 | 64.1 |
| Long term (recycling 100%) | 10.6 | 12.0 | 12.3 | 12.9 | 13.3 | 13.7 | 14.1 |

* **In the short term each percentage point of avoidable waste is worth about 1.3 million people** (2.7% of capacity). A 12% default that should be 14% would cost 2.6 million; halving waste to 6%, the national target, would add 8.0 million; no avoidable waste, 16.1 million.
* **In the long term the setting is worth much less**, because the long-term result is limited by cropland (zero waste against 12%: 14.1 against 12.3 million).
* **Recycling is worth little at the national level:** at 12% waste, 0% to 100% recycling moves the short term from 48.0 to 49.2 million, and the long term from 12.5 to 14.1 million at zero waste.
* By zone (short term):

| Zone | 12% (default) | 14% | 6% (halved) | 0% |
|---|---|---|---|---|
| Australia | 48.00 | 45.39 | 55.98 | 64.14 |
| NSW and ACT | 11.99 | 11.32 | 14.01 | 16.08 |
| Victoria | 6.96 | 6.62 | 7.90 | 8.78 |
| Queensland | 8.84 | 8.10 | 11.00 | 13.09 |
| Western Australia | 3.56 | 3.42 | 3.96 | 4.34 |

## Decisions

1. Keep the short-term default at 12%, with the Australian cross-check recorded here.
2. Offer the strategy target as a named scenario in the dashboard (avoidable waste 6%: short term 56 million), next to the thesis's 0% for the long term.
3. Recycling: keep the short-term 0% and the long-term 100% as the thesis settings; record that the thesis's description holds for consumer waste (69% landfill, 19% compost, 1.5% feed) but not for processing residues (6.25 million tonnes a year to feed) and that 100% exceeds what the swill rules allow. A named long-term scenario of 50% (plant waste only) is available.
4. Optional: if Murray can supply the Arcadis report, the 12% can be re-checked item by item with the edible split by stage.
