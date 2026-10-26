# Current ABS data for the yield pipeline

Maps the ABS Agricultural Commodities cubes at NRM level, 2016-17 to 2020-21, onto the model's 91 crop rows, in the cube layout the yield
pipeline already reads (`../yields.py`). The method does not change (SCOPE.md D1); only the input does.

| Step | File |
|---|---|
| Download the NRM cubes and item listings | `fetch_abs_current.py` |
| Read them (three file layouts across the years) | `abs_cube.py` |
| Which ABS items make which model crop | `build_commodity_map.py` writes `commodity_map.json` |
| Convert units, apply the mapping, record unreliable cells | `build_cubes.py` writes `data/abs-2016-21/cube_<year>.json` and `regions.json` |
| Check the mapping | `verify_mapping.py` (needs the downloaded cubes and the archive), `test_abs_current.py` (committed data only, runs in CI) |
| What is covered, crop by crop | `COVERAGE.md`, written by `coverage.py` |

Source: Australian Bureau of Statistics, Agricultural Commodities, Australia (cat. no. 7121.0), NRM region tables, licensed CC BY 4.0.

## What the ABS data looks like now

- **Geography.** 2016-17 to 2020-21 share one set of 64 regions: Australia, 8 states and territories, and 55 NRM regions of the 2016 edition
  (NSW is now in Local Land Services areas, so its regions differ from the 2011 zones). 2015-16 uses an older set and is not used.
  ACT appears twice (as a territory and as an NRM region). A crosswalk to the 2011 zones is still to be built (SCOPE.md D2, D8).
- **Reliability.** 2016-17 to 2019-20 mark each estimate with a symbol; the ones marked `**` (relative standard error over 50%, "too
  unreliable for general use") are recorded as unreliable, which replaces the hand deletions of the 2011 work. 2020-21 has no symbols: its NRM
  figures were made by apportioning SA2 figures by area, with suppressed cells set to zero. For that year the thesis's stated minimum
  (10 ha and 10 t) is applied instead.
- **Detail has shrunk.** The 2005-10 cubes gave about 90 crops by region; the NRM cubes now give 47 of the model's 91 crop rows (44 direct,
  3 grouped items assigned to one row). The other 44 are no longer published at NRM level: 24 vegetable rows (asparagus, beetroot, celery, garlic,
  leeks, radish, spinach and others), pulses and oilseeds other than chickpeas, lentils and canola (the ABS groups them), lemons, limes,
  grapefruit, plums, most nuts and berries, kiwifruit, cotton, and others. Zone-crop pairs with a yield in at least three of the five years:
  945, against 2,278 averaged yields in 2005-10. The model fills what a zone does not report, so the refreshed yields rely much more on the
  fill rule than the 2011 ones.
- **Units and codes changed.** Fruit and nut production is in kg to 2018-19 and in tonnes from 2019-20 (different codes); mushrooms and herbs
  are in m2 and kg; apricots and peas stop after 2018-19. The map lists each as an alternative, and the first code published that year is used.
- **Trees.** The 2005-10 cubes counted total trees, so total trees are used again (the ABS also gives trees of bearing age and its own yield per
  bearing tree, which would give higher yields; that would be a method change).
- **The 2016-21 window is not the 2005-10 window.** National wheat, barley and canola yields are about 35 to 50% higher than in 2005-10
  because 2005-10 was the millennium drought and 2016-21 contains record harvests, though also the 2018-19 drought.

## Checks (`verify_mapping.py`)

- Against yields the ABS publishes itself (t/ha): maize 138 of 139, sugar cane 47 of 47, wheat 172 of 198, barley 181 of 202, sorghum 101 of 114,
  rice 42 of 47 regions-years within 1%; the rest differ by apportionment or rounding. Bananas, pineapples and grapes differ by definition (the
  ABS divides by the area of bearing age; the 2011 method uses total area, as here).
- Against the 2005-10 national yields: most crops are within 0.8 to 1.5 times; flagged are lentils, peanuts, cucumber and herbs (one or two
  years of data and different definitions), and green peas (0.47: the ABS item now includes processing peas). The mushroom figure in the check is
  before the model's divisor of 839.

## Livestock and other inputs (not mapped yet)

The yield pipeline's livestock block needs, per zone and year, class counts, grazing and hay area, feedlot numbers, and national and zone
production totals. The cubes give most of the counts and areas, but not all:

| Needed | In the ABS NRM cubes? |
|---|---|
| Sheep: lambs, ewes (breeding, mated to lamb), all other | yes (item names change between 2018-19 and 2019-20) |
| Dairy cattle: cows, calves, heifers 1 to 2 and over 2, all other | yes, all years |
| Beef cattle: calves, cows and heifers, all other | yes; **breeding bulls are no longer separate** (they sit in "all other meat cattle", with steers) |
| Goats, deer, buffalo, horses (each with its own DSE factor) | **no**: one group "all other livestock n.e.c." |
| Grazing land (improved, other), hay and silage area | yes from 2017-18 (land use items start then); hay and silage as one group |
| Feedlot cattle and sheep, meat and wool and milk production | **no**: ABARES, MLA, Dairy Australia and ABS livestock products are the sources |

## Decisions needed

1. **Geography and window.** NRM 2016 for five years (as built); or NRM for the four years with ABS reliability symbols; or SA4 (87 regions, five
   consecutive years, also with symbols, but larger units). SA2 exists only for 2015-16 and 2020-21, so it cannot give five consecutive years.
   Recommendation: NRM five years as built. The 2020-21 apportionment spreads each SA2's area and tonnes by the same weights, so yields stay
   those of the neighbouring SA2s; it mainly adds zones with data.
2. **The 44 absent crops.** Leave them to the fill rule (the method as it stands), or add group proxies (for example the ABS "other pulses" for
   field beans, mung beans and field peas). Recommendation: the fill rule for the first release; test proxies as a separate, compared step.
3. **Combined items.** Lettuces to head lettuce, melons to rock and cantaloupe, herbs to other herbs, as mapped. Alternative: none of them,
   which leaves those rows to the fill rule.
