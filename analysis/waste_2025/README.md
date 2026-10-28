# Avoidable food waste and recycling (SCOPE.md E4 and E15)

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
* The FAO food supply for Australia is about 895 kg a person (mean 2021-23, `data/2025/consumption_proxies.json`), so that waste is about **20%** of the food supply if every kilogram counts, and about **14%** if only the edible part does (a secondary summary of the baseline says about 70% of food waste is edible; I could not verify it).
* The thesis's denominator is food produced, which is larger than the food supply at retail, so its percentage would be a little lower than these.
* **So the Australian evidence is consistent with the thesis's 12%** within what the definitions and the unverified edible share allow, roughly 12 to 14%. It does not show that the US figure was wrong. I have kept 12% (SCOPE.md rule: if in doubt, 2011) and not built a release. The original baseline report (Arcadis 2019 or the FIAL 2021 study) would give the edible share and the stage split in tonnes; agriculture.gov.au and dcceew.gov.au were not reachable.

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
3. Optional: if Murray can supply the Arcadis or FIAL report's edible and avoidable split, the 12% can be re-checked item by item.
