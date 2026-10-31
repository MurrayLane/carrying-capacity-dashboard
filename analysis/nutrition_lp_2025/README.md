# A second model alongside the first: nutrition-constrained diets (SCOPE.md E11)

The accounting model asks how many people a land base feeds on a given diet. This asks the other way round: given the land and the model's own food, loss, yield and land accounting, **which diet feeds the most people while meeting the energy, protein, fibre and macronutrient balance of the model's own guideline diets**, and how many people is that (the "people nourished per hectare" view of Cassidy et al. 2013)? It does not replace the accounting model, which stays the comparison model; it uses it. The result is an upper bound on what choice of diet is worth, not a forecast of what anyone will eat.

Files: `server.mjs` (the model as a service: set a diet in grams of each accounting unit, get the model's capacity), `optimise.py` (the optimisation), `run_variants.sh` (Australia and the seven states, both settings, three variants), `variants.csv` (the results).

## How it works

* **A diet is grams a day of each of 178 accounting units** (composite foods such as breads and yoghurts, and single foods; the rows of the Base sheet that carry a food's land). It is written into the workbook through the model's own cells (serves of each of 17 food groups, and each unit's share of its group), so ingredient mixes, losses, yields, land, recycling and the allocation of land types are all the model's own. Round trip: the default diet read out and written back gives the default capacity to 0.2%.
* **The search is successive linear programming.** At the current diet, the value of one square metre of cropland and of pasture is the change in the log of the capacity when that land's diet is scaled by 5%; a linear program (scipy, HiGHS) then minimises the value of the land a person uses subject to the constraints below; the model evaluates the result; the step is halved until the capacity rises. Two to three rounds suffice. Its answer is a local optimum of the real model, not of a linear approximation of it.
* **Constraints** (the same for every variant): energy, protein and fibre at least those of the least demanding diet in the model's own family (the Diet sheet's sedentary diets at meat shares 0 to 15%), valued with the same unit coefficients; fat 20 to 35%, protein 10 to 25% and carbohydrate 45 to 65% of energy; serves a week of each food group between the minimum and maximum of that family (the guideline diets always contain fruit, vegetables, cereals, dairy and so on).

## Results (Australia, improved method, million people)

| | Short term | Long term |
|---|---|---|
| The model's diet | 45.7 | 14.6 |
| **A. Better choice of food within today's food groups** (group serves unchanged, no food above 3 times its present intake, a food nobody eats stays out) | **69.0** (x1.5) | **19.6** (x1.35) |
| B. Food-group serves free within the guideline range, same cap of 3 times | 268 (x5.9) | 33.8 (x2.3) |
| C. Free choice, no cap | 458 (x10.0) | 36.0 (x2.5) |

State results are in `variants.csv` (global search, see stage 4); short term A / B: NSW-ACT 18.2 / 64.0 against 12.9, Victoria 8.7 / 15.0 against 7.2, Queensland 16.6 / 30.6 against 10.1, South Australia 2.9 / 5.9 against 2.3, Western Australia 4.4 / 9.2 against 3.0.

* **What variant A does**: it changes the items, not the food groups. Beef gives way to lamb and pork, regular milk to skim milk and low-fat yoghurt, and white rice and refined cereals replace some wholegrain cereals; pasture use falls by 36% and cropland by 37%. It is the same lever as the red meat mix (SCOPE E7), taken further, and it needs no change in what a food group is.
* **Variant B** is where the guidelines let the diet go: red meat falls from 90 to 10 grams a day, dairy from 390 to 90, wholegrain cereals and vegetables rise, and capacity is 4 times higher because the land used per person (cropland and pasture together) falls by 86%. **Variant C** is a plant diet of brown rice, tofu, potato and banana: the result is an upper bound on what macronutrient adequacy alone allows.
* **Reconciling with CSIRO's 100 million (SCOPE E12)**: the nutrition-limited bounds (268 and 458 million) are well above CSIRO's energy count of 100 million (27 million of them at home), which is the expected order: the energy count is not limited by land use, and the accounting model's 41 to 49 million is a statement about the diet Australians eat, the losses between farm and plate and the land of the other needs.

## What it does not do (and what the numbers must not be read as)

* **Only macronutrients and fibre are constrained.** The workbook has energy, protein, fat, carbohydrate, sugar and fibre for each food and nothing else. Vitamin B12 (found only in animal foods and fortified products), iron, zinc, calcium, iodine and vitamin A are not checked, so the diets of variants B and C, which drop most animal foods, would not be adequate without fortification or supplements. The archive's AUSNUT 2007 table (`prelim models/ausnut07full.xls`) has 20 of those nutrients per food but not B12, and the model's 178 units are mixtures of its foods, so a micronutrient version needs the mapping from units to AUSNUT foods (not done). The current AUSNUT 2023 table (3,742 foods, with vitamin B12, calcium, iron, zinc, iodine and vitamin A; `Foundation diets/AUSNUT2023/` in the models archive) has all of them, which makes the mapping worth doing. Variant A moves less between food groups, which is why it is the one to quote.
* **Taste, cost, culture, availability and processing are not modelled.** The cap of 3 times the present intake is a guard against absurd diets, not a measured limit.
* **The land accounting is the model's**: cropland and pasture are not interchangeable (pasture cannot grow rice), which is why the bounds are finite; the national result pools land, so the states do not add to Australia (as in the accounting model).
* **The sweeteners and legume groups stay at the default** (their shares do not sum to one in the workbook), and cheeses and some composite foods have no nutrient data and so count as zero nutrition, which is conservative for them.

## Stage 2: with micronutrients (2026-10-30)

`match_ausnut.py` gives each of the 178 units the micronutrients of the AUSNUT 2023 foods (FSANZ, 2025; `Foundation diets/AUSNUT2023/` of the models archive) whose energy, protein, fat, carbohydrate and fibre per 100 g are closest to the unit's own, within the right food group (`unit_micronutrients.csv`): the median distance is 0.5 of a standard step and the 90th percentile 2.8, so the match is close for most units; 15 units that the workbook gave no macronutrients (cheeses, some legumes, drinks and sweeteners) take AUSNUT's. Sanity check: the model's default diet then supplies per day calcium 881 mg, iron 12.2, zinc 11.5, iodine 161 ug, vitamin B12 4.8 ug, vitamin A 644 ug RE, folate 597 ug, vitamin C 100 mg, magnesium 348 mg, potassium 3,558 mg, and the model's own vegan-end diet (meat share 0) has 0.1 ug of B12 (the expected shortfall). `optimise.py ... micro` adds the recommended daily intake of ten nutrients as constraints (calcium 1,000 mg, iron 13, zinc 11, iodine 150, B12 2.4, vitamin A 800 ug RE, folate 400 ug DFE, vitamin C 45, magnesium 365, potassium 3,300: the average of men and women aged 19 to 50 from the NHMRC nutrient reference values **as remembered, not yet checked against the NHMRC table** (BLOCKED_SOURCES.md)). The model's own default diet is short of three (calcium 88%, vitamin A 80%, iron 94%, magnesium 95%).

Australia, improved method, million people (`variants.csv`):

| Variant | Short term, macronutrients only | Short term, with micronutrients | Long term, macronutrients only | Long term, with micronutrients |
|---|---|---|---|---|
| The model's diet | 45.7 | | 14.6 | |
| A. Better choice within today's food groups (cap 3 times) | 69.0 | **67.7** | 19.6 | **19.6** |
| B. Food-group serves free in the guideline range (cap 3 times) | 268 | **193** | 33.8 | **31.4** |
| C. Free choice | 458 | **384** | 36.0 | **35.8** |

* **Variant A is almost untouched by the micronutrient constraints** (67.7 against 69.0 million): it changes foods within each group and keeps meat, dairy, vegetables and fruit, so the nutrients follow. It meets every nutrient at 100% or above. This is the figure to quote.
* **Variant B gives up 28%** (193 against 268 million) and the diet that results is dairy-led: skim milk 465 g a day, wholegrain cereals 393 g, red meat 4 g, vegetables up; B12 (173% of the intake) comes from the milk. A diet with almost no red meat and a lot of dairy is the cheapest way to feed people in land terms, because beef costs about 25 times more land a kilogram than milk in the model.
* **Variant C gives up 16%** (384 against 458 million) and relies on soy milk and tofu: the AUSNUT soy milk is fortified with calcium and B12, so the diet's B12 (103% of the intake) is met by a fortified food, not a natural source.
* **Intakes checked against the source** (2026-10-30, NHMRC Nutrient Reference Values v1.2, `Foundation diets/` of the models archive): calcium 1,000 mg, iron 13 mg (average of 8 for men and 18 for women to 50), zinc 11 (14 and 8), iodine 150 ug, B12 2.4 ug, vitamin A 800 ug RE (900 and 700), folate 400 ug DFE, vitamin C 45 mg, magnesium 365 (400 to 420 and 310 to 320), potassium 3,300 mg (adequate intake 3,800 and 2,800). They are adult values; children and pregnancy are not weighted in.
* **Not constrained**: the bioavailability of iron and zinc from plant foods (the NHMRC raises the iron requirement of vegetarians by 80%), vitamins D, E and K, selenium, omega-3 fatty acids, and protein quality. Iron is met at 100% in variant A and at 132% in variant C, which would not survive the bioavailability adjustment in a plant-based diet.

## Stage 3: a tropical-staples diet (E16, 2026-10-30; re-run with the global search of stage 4, 2026-10-31)

`run_staples.sh` forces at least 0, 10, 20 or 30% of the diet's energy to come from the staples the workbook has (banana, cassava, sweet potato, orange sweet potato; no taro, yam, sago or coconut, see `analysis/diet_templates/tropical_crops.md`) and otherwise keeps the micronutrient model (cap 3 times the present intake on every other food). Three versions, each starting from the stricter one: **family95** (protein floor of the model's family diets, 95 g), **range** (floor 55 g, the NHMRC protein RDI averaged over men and women; the default) and **relaxed** (also no upper limit on starchy vegetables and fruit, no lower limit on cereals). Results in `staples.csv`. Improved method, thousands of people, short term:

| Minimum staple share of energy | Australia | Queensland | Northern Territory |
|---|---|---|---|
| none (the model's diet) | 45,701 | 10,070 | 72 |
| 0% (free choice) | 192,719 | 23,032 | 177 |
| 10% | 230,595 | 28,834 (relaxed 29,979) | 176 |
| 20% | 229,924 | 28,752 (relaxed 30,077) | 163 |
| 30% | infeasible | infeasible | infeasible |

(Protein floor 55 g. With the family diets' 95 g floor: Australia 172,130 / 176,319 / 172,332 at 0 / 10 / 20%, Queensland 20,582 / 22,354 / 20,740, Northern Territory the same as above: `staples_family95.csv`.)

* **A tropical-staples diet costs nothing nationally and little in the north.** At 20% of energy from roots and bananas (Papua New Guinea's roots, banana and coconut together are about 36%, with coconut and taro unavailable here) Australia's figure is as high as without the requirement (230 against 193 million; the 0% figure is a search shortfall, the same diet class), Queensland's too, and the Northern Territory feeds 163 thousand against 177 thousand (-8%). What limits these zones is pasture, not which crops feed the people. (The first version of this table showed a 25% cost for Australia; that was the search stopping early, stage 4.)
* **The ceiling is about a quarter of energy.** At 25% the Northern Territory run is feasible and at 28% it is not. With the macronutrient ranges (carbohydrate at most 65% of energy, fat at least 20%, protein 10 to 25%), the food-group serves and the fixed groups, roots at 30% leave no diet that meets all of them, whatever the protein floor.
* **The protein floor matters more than the staples, and is now the NHMRC's.** The model's family diets contain at least 95 g of protein a day; that is a by-product of guideline food patterns, not a requirement. The headline now uses the NHMRC and NZ Ministry of Health protein RDI averaged over men (64 g) and women (46 g), 55 g (Nutrient Reference Values v1.2, chosen 2026-10-31). Effect in the short term, with micronutrients: Australia free serves 172 to 193 million, free choice 378 to 384; variant A and the long term do not change. `variants_family95.csv` and `staples_family95.csv` keep the 95 g results; `protfloorfamily` reproduces them.
* **Reading it.** The numbers say how the model's land copes with a root-and-banana diet, not what such a diet is like to eat; the iron and zinc of roots are poorly absorbed (not modelled).
* **Search spread.** Results are not always ordered as the constraints imply (Australia, short term, protein 55 g: 196 million with no staples requirement, 231 with 10%), which shows a spread of at least 15% from the search; the Northern Territory and the long term are stable.
* Options of `optimise.py`: `staplesF`, `relaxgroups`, `protfloorG`, `start=FILE`, and environment variables `RDI_OFF=key,key` (drop micronutrient intakes), `UNITS_OFF=row,row` (remove accounting units), `YIELD_SCALE=row:factor` (scale Yield-sheet rows of the zone), `MAXIT`, `NOSCAN=1`.

## Stage 4: a better search (2026-10-31)

The first version of `optimise.py` was a successive linear program that could stop early: after a step where it found no gain it ended, even when a more relaxed problem (a superset of the constraints) had been solved to a higher value. Australia, short term, group serves free, no micronutrients: 195 million, against 125 for the problem with the group limits lifted, which contains the first. Two changes: (1) after the successive search the program scans the relative price of pasture land against cropland on a logarithmic grid, takes the best frontier diet and runs the successive search again from it; (2) `start=FILE` begins a run from the diet of the stricter problem it relaxes, so a relaxation cannot score below it (`run_variants.sh` chains fixed serves, then free serves with the cap, then no cap). Results with this search are in `variants.csv` (96 runs).

* **The earlier numbers were too low, by up to 31% for Australia's short term** (group serves free: 195 to 256 million; free choice 387 to 446; long term 32.6 to 33.8 and 32.9 to 36.0). Variant A (the one to quote) did not move in the short term (69.0) and rose 8% in the long term (18.2 to 19.6). Nesting holds in all 32 chains (fixed serves <= free serves <= no cap).
* **Still not a proof of optimality.** The search is a heuristic on a model whose capacity is not a smooth function; from a default start the lifted-limit problem ends at 161 million where its stricter subset reaches 172, so a spread of 5 to 10% in the short term must be assumed. The micronutrient version of variant B (172 million) was not changed by the new search while the macronutrient version rose by a third; it may be under-searched. With micronutrients the free-choice optimum is above the macronutrient-only one in 11 of 32 cases (largest: Queensland short term 56.0 against 52.0 million) because the two modes value units without workbook macronutrients differently and so are not strictly nested.
* The staples table (`staples.csv`, stage 3) was re-run with this search.

## What the maximised diets look like (Australia, short term, ten micronutrients, protein floor 55 g; grams a day)

| Group | Model's diet | A: foods swapped within groups | B: serves free in the guideline range | C: free choice |
|---|---|---|---|---|
| Red meat | 90 | 90 | 0 | 0 |
| White meat (chicken, pork, fish) | 101 | 129 | 89 | 0 |
| Dairy (all kinds) | 387 | 390 | 607 | 722 |
| Wholegrain cereals | 151 | 133 | 387 | 470 |
| Refined cereals | 186 | 144 | 231 | 0 |
| Vegetables (all kinds) | 252 | 253 | 414 | 239 |
| Fruit | 166 | 166 | 139 | 139 |
| Plant protein (tofu as meat alternative) | 0 | 0 | 0 | 262 |
| Land per person, m2 (crop / pasture) | 8.1 / 195 | 7.5 / 125 | 3.6 / 30 | 1.3 / 7 |
| People fed (million) | 45.7 | 67.7 | 192.7 | 384.2 |

Beer and other drinks stay fixed at 271 g a day in every column. Energy is 8.2 to 9.8 MJ against 8.0 today. Largest items: A skim milk 157 g, regular milk 108, white bread 76, pasta 73, potato 72; B skim milk 329, oats 186, white rice 185, regular milk 175, tomato 103, potato 94; C soy milk 586, brown rice 470, tofu 262, banana 139, cassava 99. Variant C is not a realistic diet; the AUSNUT soy milk is fortified with calcium and B12. These are land-efficiency results, not predictions.
