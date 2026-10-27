# Data after 2020-21: what exists, what it needs, and what it shows

Findings from the ABS Data API and release files, 27 October 2026. Everything listed here is open: no login, no payment.
`fetch_recent.py` downloads it; `spread_test.py` and `proxy_test.py` produce the numbers below.

## Why the first refresh stopped at 2020-21

The ABS ended the Agricultural Census and the annual Rural Environment and Agricultural Commodities Survey. 2020-21 is the last year of
census-based regional tables (NRM regions, SA4, SA2). The 2021-22 release has a reduced item set at national and state level only. From
2022-23 the ABS publishes a new series, *Australian Agriculture* (broadacre crops, horticulture, livestock), built from levy and
administrative data, in new files and an API. The earlier refresh used the cubes that fitted the 2011 method; this note covers the rest.

## What exists after 2020-21

| Source | Geography | Years | Covers | Gaps |
|---|---|---|---|---|
| Data API `AG_BROADACRE` | SA2 (2,482), ASGS 2021 | 2022-23 to 2024-25 | Area, levied production, local value, levy-payer count for wheat, barley, oats, canola, sorghum, maize, rice, chickpeas, faba beans, field peas, lentils, lupins, cotton, sugar cane | Production is *levied* production (levy payers only). Suppressed cells are blank (`n`). No 2021-22. No soybeans, sunflower, mung beans, triticale |
| Data API `AG_HORTICULTURE` | SA2 (573) | 2022-23 to 2024-25 | Area, production, value, businesses | Only avocados, macadamias, bananas, wine grapes |
| Horticulture workbook (Hort Innovation estimates, republished by the ABS) | Australia and state | 2020-21 to 2024-25 | 29 fruits, 33 vegetables, 7 nuts: production (t) and farm gate value | **No area**, so no yield. No regions below state |
| Broadacre state workbooks | Australia and state | 2022-23 to 2024-25 | Total crop area, levied production, value | Three years |
| Livestock series workbooks | Australia and state | 2005 to 2025 | Total beef cattle, dairy cattle, sheep and lambs; wool and milk value | Totals only, not the class counts the DSE method needs |
| Census cubes, ASGS Edition 3 | SA2, SA4 | 2020-21 only | Every item the ABS kept | The last census |

Licence: ABS releases are CC BY 4.0, including the tables that carry Hort Innovation's estimates. The Hort Innovation *Handbook* (which has
planted area for most crops) is a separate document whose introduction says it may not be reproduced without Hort Innovation's written
consent. Not used here.

Not tested: ABS TableBuilder and DataLab (registration or accreditation), ABARES, Meat & Livestock Australia, Dairy Australia. None is needed for the
sources above. They are the places to look for regional livestock class counts and horticulture area.

## Is the 2020-21 jump in regions a trend or an artefact?

The question: the 2020-21 NRM cube shows many more regions growing each crop (oats 59, against about 30 the year before). Does that mean production is
spreading out, away from regional concentration? `spread_test.py`, five field crops, area:

* **The NRM jump is the method.** The ABS apportions 2020-21 SA2 figures to NRM regions by area, so a small amount in one SA2 appears in every NRM
  region it overlaps. The count rises with no change on the ground.
* **SA4 (direct figures) rises too, but boundaries explain most of it.** Oats SA4 count: 42 (2018-19), 37 (2019-20), 55 (2020-21). ASGS 2021
  has 107 SA4s against 89 in 2016. The measures that do not depend on the number of regions barely move: the share held by the five largest SA4s is
  0.66, 0.61, 0.66 for oats; the effective number of regions is 7.1, 6.8, 6.7.
* **Same boundaries, different source.** SA2 2020-21 (census) against SA2 2022-23 to 2024-25 (levy-based): the count of SA2s falls by half
  (oats 382 to 156-182) because the levy data omits small growers. Concentration is flat for wheat (effective number 51.9 against 50-51.5),
  canola (42.8 against 41-44), barley (46.5 against 39-45) and sorghum (20 against 15-20). Oats is the only crop that looks more concentrated (47
  against 34-40), and that is confounded with the change of source.

Conclusion: no evidence here of a move from regional to national production. The count of regions is not a safe indicator; concentration measures
are, and they are stable. This tests where crops are *grown*. Whether regions are *self-sufficient* needs production set against regional
demand and, for most crops, distribution beyond the farm, which none of these tables show. Two further lines would answer the question properly: a long
same-boundary series (state shares of national production, 2005 to 2025, from the state tables in each release), and trade flows (ABS freight and
interstate trade, not examined). Either could be a paper.

## Proxy for crops the ABS no longer reports

The 44 model crops absent from the NRM cubes: 34 now have some current source. Whatever the source, every absent crop takes the group trend (B10); the current sources are checks and, for field peas and faba beans, real data.

| Group | Crops | Current source |
|---|---|---|
| Vegetables, fruit, nuts | 32 (artichokes, asparagus, beetroot, chillies, celery, eggplant, garlic, ginger, leeks, parsnips, sweet potatoes, zucchini, watermelons, plums, lemons, limes, grapefruit, pecans, walnuts, lychees, blueberries, berries, kiwifruit, pawpaws and others) | Hort Innovation state production and value, 2020-21 to 2024-25. **Production only, no area** |
| Broadacre | field peas, field (faba) beans | `AG_BROADACRE`, SA2 area and levied production: a full update. Cotton has area but no production, so cotton lint takes the group trend |
| None found | mung beans, soybeans, sunflower, okra, radish, spring onions, swedes and turnips, cashews, guavas | Nothing current and open |

Because production without area gives no yield, the proxy has to be a yield *change*. The test (`proxy_test.py`): take crops the ABS still reports,
pretend each is missing, predict its change in national yield since 2006-2010 from the median change of the others in its group, and compare with
keeping the old yield. Median error, 80th percentile:

| Group | Crops tested | Median change in yield | Group-median proxy | Keep old yield |
|---|---|---|---|---|
| Field crops | 9 | +25% | **14%, 38%** | 25%, 45% |
| Vegetables | 16 | +6% | 22%, 32% | **16%, 30%** |
| Fruit | 15 | +3% | 20%, 40% | **16%, 43%** |
| Nuts | 2 | +27% | too few to test | |

Field crops move with their group (the 2006-2010 drought years were low); for vegetables and fruit a group trend is somewhat worse than keeping the old
yield for any one crop. Murray chose the group trend for every group so that one rule applies throughout (SCOPE.md B10); the cost is the extra 4 to 6 points of median error for vegetables and fruit. The rule and its first run on the newest data are in `pipeline/yields/recent/`. For vegetables, fruit and nuts the update that the data
supports is the *level of production* (Hort Innovation state tonnes), used to rescale how much of each crop is grown where, and as a consistency check
on the yield (implied area = production / yield, compared with the old area). Sources of area for these crops are the Hort Innovation Handbook (needs
Hort Innovation's consent), the 2020-21 census cubes for the items they kept, and state agencies.

## Livestock

The series give totals by state (beef cattle, dairy cattle, sheep and lambs) and the value of wool and milk. The method needs counts by class (the 2011
work used harmonised classes by region) and production totals by product. The state totals allow rescaling the 2011 class structure to the current herd; the
class structure itself is not updated by any open source found. That is a decision for Murray: SCOPE.md B12.

## ABS TableBuilder and the missing livestock inputs (checked 2026-10-27)

The ABS list of available TableBuilder and microdata products ([Available Microdata and TableBuilder](https://www.abs.gov.au/statistics/microdata-tablebuilder/available-microdata-tablebuilder),
the whole page searched for agriculture, farm, livestock and crop) has **no agriculture dataset**: no Agricultural Census, no Agricultural Commodities, no REACS. The
nearest products are Census of Population and Housing (industry of employment, not farm output), Business Longitudinal Analysis Data Environment, Motor Vehicle Use and
Road Freight Movements. So TableBuilder is not a route to the livestock classes, whoever holds the login. The ABS's own Agricultural Commodities data is published only as
the cubes already used.

What the cubes do hold, 2015-16 to 2020-21: sheep (lambs, breeding ewes, other), dairy cattle (cows, calves, heifers 1 to 2, heifers over 2, other), meat cattle (calves, cows,
other), pigs, poultry, and one lump "all other livestock" (1.5 million head in 2020-21, against 68 million sheep and 24 million cattle). Goats were published separately in 2015-16 only
(0.4 million managed goats). Deer, horses and buffaloes are inside the lump in every year. Feedlot numbers, breeding bulls and grazing area by region are not published after 2015-16. The
classes the cubes lack are small in dry-sheep-equivalent terms; feedlot numbers and production totals are the ones that matter, and they come from industry sources (the Australian
Lot Feeders' Association survey for cattle on feed; ABS Livestock Products for national meat, wool and milk).

Still unchecked from here, because the sites blocked this environment: the ABARES Australian Agricultural Census 2020-21 dashboards (SA2 and local government area) and MLA's regional
herd and flock tables (both built from ABS data, so they add no new classes unless they carry their own estimates).
