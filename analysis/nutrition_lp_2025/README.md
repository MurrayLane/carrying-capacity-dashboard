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

* **Only macronutrients and fibre are constrained.** The workbook has energy, protein, fat, carbohydrate, sugar and fibre for each food and nothing else. Vitamin B12 (found only in animal foods and fortified products), iron, zinc, calcium, iodine and vitamin A are not checked, so the diets of variants B and C, which drop most animal foods, would not be adequate without fortification or supplements. The archive's AUSNUT 2007 table (`prelim models/ausnut07full.xls`) has 20 of those nutrients per food but not B12, and the model's 178 units are mixtures of its foods, so a micronutrient version needs the mapping from units to AUSNUT foods (not done). Variant A moves less between food groups, which is why it is the one to quote.
* **Taste, cost, culture, availability and processing are not modelled.** The cap of 3 times the present intake is a guard against absurd diets, not a measured limit.
* **The land accounting is the model's**: cropland and pasture are not interchangeable (pasture cannot grow rice), which is why the bounds are finite; the national result pools land, so the states do not add to Australia (as in the accounting model).
* **The sweeteners and legume groups stay at the default** (their shares do not sum to one in the workbook), and cheeses and some composite foods have no nutrient data and so count as zero nutrition, which is conservative for them.
