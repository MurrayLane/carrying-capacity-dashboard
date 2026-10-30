# A second model alongside the first: nutrition-constrained diets (SCOPE.md E11)

The accounting model asks how many people a land base feeds on a given diet. This asks the other way round: given the land and the model's own food, loss, yield and land accounting, **which diet feeds the most people while meeting the energy, protein, fibre and macronutrient balance of the model's own guideline diets**, and how many people is that (the "people nourished per hectare" view of Cassidy et al. 2013)? It does not replace the accounting model, which stays the comparison model; it uses it. The result is an upper bound on what choice of diet is worth, not a forecast of what anyone will eat.

Files: `server.mjs` (the model as a service: set a diet in grams of each accounting unit, get the model's capacity), `optimise.py` (the optimisation), `run_all.sh` (Australia and the seven states, both settings, three variants), `variants.csv` (the results).

## How it works

* **A diet is grams a day of each of 178 accounting units** (composite foods such as breads and yoghurts, and single foods; the rows of the Base sheet that carry a food's land). It is written into the workbook through the model's own cells (serves of each of 17 food groups, and each unit's share of its group), so ingredient mixes, losses, yields, land, recycling and the allocation of land types are all the model's own. Round trip: the default diet read out and written back gives the default capacity to 0.2%.
* **The search is successive linear programming.** At the current diet, the value of one square metre of cropland and of pasture is the change in the log of the capacity when that land's diet is scaled by 5%; a linear program (scipy, HiGHS) then minimises the value of the land a person uses subject to the constraints below; the model evaluates the result; the step is halved until the capacity rises. Two to three rounds suffice. Its answer is a local optimum of the real model, not of a linear approximation of it.
* **Constraints** (the same for every variant): energy, protein and fibre at least those of the least demanding diet in the model's own family (the Diet sheet's sedentary diets at meat shares 0 to 15%), valued with the same unit coefficients; fat 20 to 35%, protein 10 to 25% and carbohydrate 45 to 65% of energy; serves a week of each food group between the minimum and maximum of that family (the guideline diets always contain fruit, vegetables, cereals, dairy and so on).

## Results (Australia, improved method, million people)

| | Short term | Long term |
|---|---|---|
| The model's diet | 45.7 | 14.6 |
| **A. Better choice of food within today's food groups** (group serves unchanged, no food above 3 times its present intake, a food nobody eats stays out) | **69.0** (x1.5) | **18.2** (x1.25) |
| B. Food-group serves free within the guideline range, same cap of 3 times | 195 (x4.3) | 32.6 (x2.2) |
| C. Free choice, no cap | 387 (x8.5) | 32.9 (x2.3) |

State results are in `variants.csv`; short term A / B: NSW-ACT 18.5 / 46.9 against 13.0, Victoria 8.7 / 14.9 against 7.2, Queensland 16.5 / 22.3 against 10.1, South Australia 3.0 / 5.9 against 2.4, Western Australia 4.4 / 9.2 against 3.4.

* **What variant A does**: it changes the items, not the food groups. Beef gives way to lamb and pork, regular milk to skim milk and low-fat yoghurt, and white rice and refined cereals replace some wholegrain cereals; pasture use falls by 36% and cropland by 37%. It is the same lever as the red meat mix (SCOPE E7), taken further, and it needs no change in what a food group is.
* **Variant B** is where the guidelines let the diet go: red meat falls from 90 to 10 grams a day, dairy from 390 to 90, wholegrain cereals and vegetables rise, and capacity is 4 times higher because the land used per person (cropland and pasture together) falls by 86%. **Variant C** is a plant diet of brown rice, tofu, potato and banana: the result is an upper bound on what macronutrient adequacy alone allows.
* **Reconciling with CSIRO's 100 million (SCOPE E12)**: the nutrition-limited bounds (195 and 387 million) are well above CSIRO's energy count of 100 million (27 million of them at home), which is the expected order: the energy count is not limited by land use, and the accounting model's 41 to 49 million is a statement about the diet Australians eat, the losses between farm and plate and the land of the other needs.

## What it does not do (and what the numbers must not be read as)

* **Only macronutrients and fibre are constrained.** The workbook has energy, protein, fat, carbohydrate, sugar and fibre for each food and nothing else. Vitamin B12 (found only in animal foods and fortified products), iron, zinc, calcium, iodine and vitamin A are not checked, so the diets of variants B and C, which drop most animal foods, would not be adequate without fortification or supplements. The archive's AUSNUT 2007 table (`prelim models/ausnut07full.xls`) has 20 of those nutrients per food but not B12, and the model's 178 units are mixtures of its foods, so a micronutrient version needs the mapping from units to AUSNUT foods (not done). The current AUSNUT 2023 table (3,742 foods, with vitamin B12, calcium, iron, zinc, iodine and vitamin A; `Foundation diets/AUSNUT2023/` in the models archive) has all of them, which makes the mapping worth doing. Variant A moves less between food groups, which is why it is the one to quote.
* **Taste, cost, culture, availability and processing are not modelled.** The cap of 3 times the present intake is a guard against absurd diets, not a measured limit.
* **The land accounting is the model's**: cropland and pasture are not interchangeable (pasture cannot grow rice), which is why the bounds are finite; the national result pools land, so the states do not add to Australia (as in the accounting model).
* **The sweeteners and legume groups stay at the default** (their shares do not sum to one in the workbook), and cheeses and some composite foods have no nutrient data and so count as zero nutrition, which is conservative for them.

## Stage 2: with micronutrients (2026-10-30)

`match_ausnut.py` gives each of the 178 units the micronutrients of the AUSNUT 2023 foods (FSANZ, 2025; `Foundation diets/AUSNUT2023/` of the models archive) whose energy, protein, fat, carbohydrate and fibre per 100 g are closest to the unit's own, within the right food group (`unit_micronutrients.csv`): the median distance is 0.5 of a standard step and the 90th percentile 2.8, so the match is close for most units; 15 units that the workbook gave no macronutrients (cheeses, some legumes, drinks and sweeteners) take AUSNUT's. Sanity check: the model's default diet then supplies per day calcium 881 mg, iron 12.2, zinc 11.5, iodine 161 ug, vitamin B12 4.8 ug, vitamin A 644 ug RE, folate 597 ug, vitamin C 100 mg, magnesium 348 mg, potassium 3,558 mg, and the model's own vegan-end diet (meat share 0) has 0.1 ug of B12 (the expected shortfall). `optimise.py ... micro` adds the recommended daily intake of ten nutrients as constraints (calcium 1,000 mg, iron 13, zinc 11, iodine 150, B12 2.4, vitamin A 800 ug RE, folate 400 ug DFE, vitamin C 45, magnesium 365, potassium 3,300: the average of men and women aged 19 to 50 from the NHMRC nutrient reference values **as remembered, not yet checked against the NHMRC table** (BLOCKED_SOURCES.md)). The model's own default diet is short of three (calcium 88%, vitamin A 80%, iron 94%, magnesium 95%).

Australia, improved method, million people (`variants_micro.csv`):

| Variant | Short term, macronutrients only | Short term, with micronutrients | Long term, macronutrients only | Long term, with micronutrients |
|---|---|---|---|---|
| The model's diet | 45.7 | | 14.6 | |
| A. Better choice within today's food groups (cap 3 times) | 69.0 | **67.7** | 18.2 | **18.2** |
| B. Food-group serves free in the guideline range (cap 3 times) | 195 | **172** | 32.6 | **29.0** |
| C. Free choice | 387 | **304** | 32.9 | **32.7** |

* **Variant A is almost untouched by the micronutrient constraints** (67.7 against 69.0 million): it changes foods within each group and keeps meat, dairy, vegetables and fruit, so the nutrients follow. It meets every nutrient at 100% or above. This is the figure to quote.
* **Variant B gives up 12%** (172 against 195 million) and the diet that results is dairy-led: skim milk 465 g a day, wholegrain cereals 393 g, red meat 4 g, vegetables up; B12 (173% of the intake) comes from the milk. A diet with almost no red meat and a lot of dairy is the cheapest way to feed people in land terms, because beef costs about 25 times more land a kilogram than milk in the model.
* **Variant C gives up 21%** (304 against 387 million) and relies on soy milk and tofu: the AUSNUT soy milk is fortified with calcium and B12, so the diet's B12 (103% of the intake) is met by a fortified food, not a natural source.
* **Intakes checked against the source** (2026-10-30, NHMRC Nutrient Reference Values v1.2, `Foundation diets/` of the models archive): calcium 1,000 mg, iron 13 mg (average of 8 for men and 18 for women to 50), zinc 11 (14 and 8), iodine 150 ug, B12 2.4 ug, vitamin A 800 ug RE (900 and 700), folate 400 ug DFE, vitamin C 45 mg, magnesium 365 (400 to 420 and 310 to 320), potassium 3,300 mg (adequate intake 3,800 and 2,800). They are adult values; children and pregnancy are not weighted in.
* **Not constrained**: the bioavailability of iron and zinc from plant foods (the NHMRC raises the iron requirement of vegetarians by 80%), vitamins D, E and K, selenium, omega-3 fatty acids, and protein quality. Iron is met at 100% in variant A and at 132% in variant C, which would not survive the bioavailability adjustment in a plant-based diet.
