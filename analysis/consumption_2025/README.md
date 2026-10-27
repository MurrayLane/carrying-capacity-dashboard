# Has the standard Australian diet changed since 2011? And the other consumption defaults

Murray's rule (2026-10-27): look for an alternate source or a proxy for the change in every default; keep the 2011 value only when those avenues are exhausted. `consumption_proxies.py` does the sums; the result is
`data/2025/consumption_proxies.json` and release `2025-consumption`. Only the short-term settings (today's consumption) are touched: the long-term settings are scenarios, not measurements.

## What the model's "standard Australian diet" is

Not a food-by-food table. The default diet is set by two numbers, **meat and eggs as a share of all food (13%)** and **red meat as a share of all meat (64%)**, plus a sedentary activity level. Around them the model builds a diet of
serves per week for each food group from Byron et al. (2011), the NHMRC draft revision of the Australian Guide to Healthy Eating, with the "preferences" inside each group from the 1995 National Nutrition Survey (Foods Eaten),
nutrient composition from AUSNUT 2006, and losses from US studies (Muth 2011, Buzby 2010). "Red meat" in the model is beef, lamb, veal and pork; "white meat etc." is poultry, eggs, fish and seafood.
So updating the standard diet means updating those two numbers, and the item-level inputs are a separate piece of work (SCOPE.md E4 and E7).

## Has it changed? Yes, in the meat

FAO food balance sheet for Australia (kg per person per year of food supply, mean of 2010-12 against 2021-23):

| | 2010-12 | 2021-23 | Change |
|---|---|---|---|
| Beef and veal | 39.1 | 25.9 | -34% |
| Mutton and goat | 9.8 | 9.7 | 0% |
| Pork | 23.4 | 25.8 | +10% |
| Poultry | 47.0 | 50.3 | +7% |
| All meat | 121.5 | 112.8 | -7% |
| Meat and eggs, share of all food by weight | 14.5% | 13.5% | x0.926 |
| Red meat (beef, mutton, pork) share of red meat and poultry | 61.3% | 55.4% | x0.903 |

The FAO figures for 2010-12 sit close to the model's 13% and 64% (14.5% and 61.3%), which is why a ratio on the same series is a fair way to carry the 2011 values forward.
The ABS 2011-12 and 2023 national surveys agree on direction: discretionary foods supplied 35.4% of energy in 2011-12 and 31.3% in 2023; only 4.3% of people in 2023 met the vegetable recommendation (ABS National Nutrition and
Physical Activity Survey 2023, Consumption of food groups from the Australian Dietary Guidelines). The 2023 per-person serves by food group are in the ABS tables (`ADGDC` files); the 2011-12 equivalents are in the archived
4364.0.55.012. They are on a different basis from the model's serves, so they are used here as a check on direction, not as an input.

## Proposed values and what each does to capacity

Release `2025-consumption`, short-term settings. Effect on Australia's short-term capacity, each change alone on release `2025-livestock` (43.3 million people):

| Default | 2011 | Proposed | Source of the change | Effect alone |
|---|---|---|---|---|
| Meat and eggs, share of food | 13% | 12% | FAO food balance sheet, x0.926 | +2.8% |
| Red meat, share of meat | 64% | 57.8% | FAO food balance sheet, x0.903 | +7.6% |
| Liquid fuel per person | 2,520 L | 2,360 L | Australian Petroleum Statistics, sales per person 2011 to 2025, x0.937 | 0.0% |
| Biofuel share | 0.5% | 0.23% | same, ethanol-blended fuel as a share of sales, x0.462 | +0.2% |
| Timber per person | 1 m3 | 0.8 m3 | FAO forestry, sawnwood, panels and fuel wood per person, x0.820 | 0.0% |
| Organic share of farmland | 2% | 7% (see below) | Certified organic hectares, 12 Mha in the 2011 basis (your 2016 organic paper) to 44.4 Mha (Australian Organic Market Report 2026), x3.70 | -1.0% on its own; 0 once the baseline constant in the workbook moves with it (`analysis/organic_2025/`, release `2025-organic`) |
| All six together | | | | +9.7% (47.5 million) in `2025-consumption`; +10.8% (48.0 million) with the organic baseline moved |

The diet shares are the ones that matter. Fuel, biofuel and timber hardly move the result, because the land they need is small and non-agricultural land is in surplus nationally.

## Not updated: no series with a 2011 baseline, or not a measurement

| Default | 2011 | Why it stays | What would unlock it |
|---|---|---|---|
| Textiles per person | 23 kg | The 2011 source is not recorded. Current estimates disagree because of what they count: 14.8 kg of clothing a head in 2018-19 (Australian Fashion Council), 27 kg of new clothing (Monash, Australia Institute), 860 kt of textile waste in 2020-21 (National Waste Report; about 33 kg a head, all textiles) | The source of the 23 kg, so the same definition can be updated |
| Natural fibre share | 50% | Polyester is "more than half" of clothing sold (Australia Institute); no dated share | A fibre-mix figure for Australian consumption |
| Wool share of natural fibre | 12% | No series | as above |
| Avoidable food waste | 12% | US figures; the National Food Waste Baseline (2019) is the Australian source, and replacing them is a method change (SCOPE.md E4) | E4 |
| Recycling of food waste to animals | 0% | Still negligible commercially | |
| Activity level | 1 (sedentary) | A user choice, not a measurement | |
| Resilience | 1 year | A user choice | |
| Long-term settings | various | Scenarios | |

## Sources

* FAO, [Food balance sheets](https://www.fao.org/faostat/en/#data/FBS) and [Forestry production and trade](https://www.fao.org/faostat/en/#data/FO), bulk files for Oceania.
* Department of Climate Change, Energy, the Environment and Water, Australian Petroleum Statistics (data.gov.au, extract of August 2026).
* ABS, National Nutrition and Physical Activity Survey 2023 and Australian Health Survey 2011-12.
* Murray Lane, draft paper on organic agriculture in carrying capacity modelling (February 2016; `Organic yeild comparisons 040216.docx` and `Organic comparisons for paper.xls` in the archive): the 2% default is "just over 12 million hectares" of certified organic land. Australian Organic Market Report, snapshot 2026: 44.4 million hectares (about 12% of agricultural land as the report puts it). The reports of 2021 (35.7 Mha), 2023 (53 Mha) and 2026 (44.4 Mha) disagree, so organic is the least certain default. Scaling by hectares keeps the paper's own definition.
