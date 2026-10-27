# Peters et al. 2016, "Carrying capacity of U.S. agricultural land: Ten diet scenarios"

Peters CJ, Picardy J, Darrouzet-Nardi AF, Wilkins JL, Griffin TS, Fick GW (2016). Elementa: Science of the Anthropocene 4: 000116, doi:10.12952/journal.elementa.000116 (published 22 July 2016, open access).
It is the national-scale successor of Peters, Wilkins and Fick (2007), the New York State study whose method the Dashboard follows. Gary Fick is a co-author of both and the referee named in Murray's organic paper.

## What it did

Ten diets for the contiguous United States: two reference diets from actual consumption (a baseline and a "positive control" with the excess discretionary calories removed) and eight "healthy diet" variants (five omnivorous
with 100%, 80%, 60%, 40% and 20% of the meat of the healthy omnivore diet, ovolacto-vegetarian, lacto-vegetarian, vegan). For each, a spreadsheet model ("U.S. Foodprint") converts servings to food mass, adds losses
and processing conversions and livestock feed, divides by national yields (2000-2010) to land per person, and divides the land available in three pools by it.
Results: 0.13 to 1.08 ha per person per year; carrying capacity 402 to 807 million (1.3 to 2.6 times the 2010 population); lowest for the baseline, highest for the lacto-vegetarian diet; the vegan diet fell between the 60% and
40% omnivore diets. The spreadsheet is open (Dataset S1).

## What bears on the Dashboard

1. **A binding constraint taken as a minimum over land pools.** Capacity = MIN of (cultivated cropland / cultivated need), (all cropland / cultivated + perennial need), (all land / total need): the same logic as the Dashboard's
   reallocation (cropland can do anything, pasture everything but cropping), but Peters limits how much cropland can be in cultivated crops in one year (71% in the base case, from the current share; the rest is hay, perennial
   forage and rotation), and shows that capacity is highly sensitive to that limit. The Dashboard's "cropping land" is the area in crops in the year (ABS "land mainly used for crops"), which already embeds a rotation share;
   in 2020-21 the ABS also reports 76.8 Mha of "land mainly used for cropping and improved pastures" against 31.6 Mha in crops, which is the cropland of Peters's kind. Worth a decision: a cultivated-share parameter, or keep the area-in-crops definition. (New row for SCOPE.md E.)
2. **Multi-use crops.** Land for soy and canola oil also yields meal that is fed to livestock, so the land is credited once ("MUCA"). Whether the Dashboard credits oilseed meal to the feed of animals needs checking in the Base and Recycle sheets.
3. **Dairy and beef are one system.** Culled dairy cows, veal and dairy calves supply part of the beef; with lacto-vegetarian diets the question of what happens to them is open (the authors say so). The Dashboard keeps dairy and beef land separate, and
   its livestock stage assigns all cattle meat to the beef herd's land share (SCOPE.md B12 and `pipeline/yields/recent/livestock_zone.py`); the cull-cow meat of the dairy herd is not credited.
4. **One-factor sensitivity over seven levels** (the cultivated share at -30% to +30% in 10% steps) and the plateau it shows: a template for the sensitivity runs proposed for the 2025 data.
5. **Diet scenarios as meat share and a healthy diet from guidelines**, as the Dashboard does (meat and egg share, Byron et al. 2011). Their omnivore scale (100% to 20% of the healthy meat) matches the Dashboard's slider in spirit. They also say
   that scenarios with *more* meat than the baseline, and partial adoption of guidelines, should be tested: the Dashboard's slider allows both.
6. **Productive land only.** Only land harvested or grazed counts; idle cropland, woodlots, farm roads and ponds are excluded: the Dashboard's separate non-agricultural and infrastructure classes do the same.
7. **Closed system, no trade**, stated as the purpose, as in the Dashboard.
8. **Stated gaps:** variability within a diet (the mix of beef, pork and chicken; fat), crop yields and food waste as sensitivity inputs, and diets above baseline meat: the first is the Dashboard's red meat share, the others are its yield and avoidable waste settings.

## Caution on comparison

The United States figure is a closed-system capacity on current agricultural land with healthy diets; the Dashboard's short-term figure is on the present diet. The ratio to population (1.3 to 2.6 for the US; 1.7 for Australia in the 2025 short-term run) is the
nearest comparison, and the US 402 million baseline is 1.3 times the 2010 population against the Dashboard's 1.8 times for Australia in 2011.
