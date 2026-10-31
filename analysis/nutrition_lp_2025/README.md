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
| B. Food-group serves free within the guideline range, same cap of 3 times | 256 (x5.6) | 33.8 (x2.3) |
| C. Free choice, no cap | 446 (x9.8) | 36.0 (x2.5) |

State results are in `variants.csv` (global search, see stage 4); short term A / B: NSW-ACT 18.2 / 60.1 against 12.9, Victoria 8.7 / 15.0 against 7.2, Queensland 16.6 / 30.7 against 10.1, South Australia 2.9 / 5.9 against 2.3, Western Australia 4.4 / 9.2 against 3.0.

* **What variant A does**: it changes the items, not the food groups. Beef gives way to lamb and pork, regular milk to skim milk and low-fat yoghurt, and white rice and refined cereals replace some wholegrain cereals; pasture use falls by 36% and cropland by 37%. It is the same lever as the red meat mix (SCOPE E7), taken further, and it needs no change in what a food group is.
* **Variant B** is where the guidelines let the diet go: red meat falls from 90 to 10 grams a day, dairy from 390 to 90, wholegrain cereals and vegetables rise, and capacity is 4 times higher because the land used per person (cropland and pasture together) falls by 86%. **Variant C** is a plant diet of brown rice, tofu, potato and banana: the result is an upper bound on what macronutrient adequacy alone allows.
* **Reconciling with CSIRO's 100 million (SCOPE E12)**: the nutrition-limited bounds (256 and 446 million) are well above CSIRO's energy count of 100 million (27 million of them at home), which is the expected order: the energy count is not limited by land use, and the accounting model's 41 to 49 million is a statement about the diet Australians eat, the losses between farm and plate and the land of the other needs.

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
| B. Food-group serves free in the guideline range (cap 3 times) | 256 | **172** | 33.8 | **31.4** |
| C. Free choice | 446 | **378** | 36.0 | **35.8** |

* **Variant A is almost untouched by the micronutrient constraints** (67.7 against 69.0 million): it changes foods within each group and keeps meat, dairy, vegetables and fruit, so the nutrients follow. It meets every nutrient at 100% or above. This is the figure to quote.
* **Variant B gives up 33%** (172 against 256 million; but see stage 4: this one run was not improved by the better search and may be under-searched) and the diet that results is dairy-led: skim milk 465 g a day, wholegrain cereals 393 g, red meat 4 g, vegetables up; B12 (173% of the intake) comes from the milk. A diet with almost no red meat and a lot of dairy is the cheapest way to feed people in land terms, because beef costs about 25 times more land a kilogram than milk in the model.
* **Variant C gives up 15%** (378 against 446 million) and relies on soy milk and tofu: the AUSNUT soy milk is fortified with calcium and B12, so the diet's B12 (103% of the intake) is met by a fortified food, not a natural source.
* **Intakes checked against the source** (2026-10-30, NHMRC Nutrient Reference Values v1.2, `Foundation diets/` of the models archive): calcium 1,000 mg, iron 13 mg (average of 8 for men and 18 for women to 50), zinc 11 (14 and 8), iodine 150 ug, B12 2.4 ug, vitamin A 800 ug RE (900 and 700), folate 400 ug DFE, vitamin C 45 mg, magnesium 365 (400 to 420 and 310 to 320), potassium 3,300 mg (adequate intake 3,800 and 2,800). They are adult values; children and pregnancy are not weighted in.
* **Not constrained**: the bioavailability of iron and zinc from plant foods (the NHMRC raises the iron requirement of vegetarians by 80%), vitamins D, E and K, selenium, omega-3 fatty acids, and protein quality. Iron is met at 100% in variant A and at 132% in variant C, which would not survive the bioavailability adjustment in a plant-based diet.

## Stage 3: a tropical-staples diet (E16, 2026-10-30)

`run_staples.sh` forces at least 0, 10, 20, 30 or 40% of the diet's energy to come from the staples the workbook has (banana, cassava, sweet potato, orange sweet potato; no taro, yam, sago or coconut, which `analysis/diet_templates/tropical_crops.md` explains) and otherwise keeps the micronutrient model (cap 3 times the present intake on every other food). Results are in `staples.csv` (improved method, thousands of people in the table below, short term).

| Minimum staple share of energy | Australia | Queensland | Northern Territory |
|---|---|---|---|
| none (default diet / free choice) | 45,701 / 172,130 | 10,070 / 20,527 | 72 / 177 |
| 10% | 154,501 | 21,193 | 176 |
| 20% | 128,978 (165,204 with the protein floor at 55 g) | 20,548 (26,438) | 163 |
| 30% or 40% | infeasible | infeasible | infeasible |

* **A tropical-staples diet costs little in the model.** At 20% of energy from roots and bananas (the real Papua New Guinea figure for roots, banana and coconut together is about 36%, with coconut and taro unavailable here) the Northern Territory feeds 163 thousand against 177 thousand with free choice, and Queensland's long-term figure does not move (1.72 million). What limits these zones is pasture, not which crops feed the people.
* **The ceiling is about a quarter of energy.** At 25% the Northern Territory run is feasible (the gain falls to 1.4 times the default) and at 28% it is not. With the macronutrient ranges (carbohydrate at most 65% of energy, fat at least 20%, protein 10 to 25%), the food-group serves of the Diet sheet and the fixed groups, roots at 30% leave no diet that meets all of them. The protein floor of the model's family diets (94.8 g a day) is a separate limit; setting it to the NHMRC's 55 g (`protfloor55`) lifts Australia and Queensland but not the 30% ceiling.
* **Reading it.** The numbers say how the model's land copes with a root-and-banana diet, not what such a diet is like to eat; the iron and zinc of roots are poorly absorbed (not modelled), and the soy milk and dairy that fill the rest of the diet are the same foods the free optimum chooses.
* **The search is local.** Successive linear programming can stop at different diets from different constraints: Australia, short term, gives 125 million with the group limits relaxed and 172 million without, although the relaxed problem contains the other. Differences smaller than about 30% in Australia's short term should not be read; the Northern Territory and Queensland long term are stable.
* New options of `optimise.py`: `staplesF`, `relaxgroups` (no upper limit on starchy vegetables and fruit, no lower limit on cereals), `protfloorG`, and the environment variable `RDI_OFF=key,key` to drop micronutrient intakes when diagnosing an infeasible run.

## Stage 4: a better search (2026-10-31)

The first version of `optimise.py` was a successive linear program that could stop early: after a step where it found no gain it ended, even when a more relaxed problem (a superset of the constraints) had been solved to a higher value. Australia, short term, group serves free, no micronutrients: 195 million, against 125 for the problem with the group limits lifted, which contains the first. Two changes: (1) after the successive search the program scans the relative price of pasture land against cropland on a logarithmic grid, takes the best frontier diet and runs the successive search again from it; (2) `start=FILE` begins a run from the diet of the stricter problem it relaxes, so a relaxation cannot score below it (`run_variants.sh` chains fixed serves, then free serves with the cap, then no cap). Results with this search are in `variants.csv` (96 runs).

* **The earlier numbers were too low, by up to 31% for Australia's short term** (group serves free: 195 to 256 million; free choice 387 to 446; long term 32.6 to 33.8 and 32.9 to 36.0). Variant A (the one to quote) did not move in the short term (69.0) and rose 8% in the long term (18.2 to 19.6). Nesting holds in all 32 chains (fixed serves <= free serves <= no cap).
* **Still not a proof of optimality.** The search is a heuristic on a model whose capacity is not a smooth function; from a default start the lifted-limit problem ends at 161 million where its stricter subset reaches 172, so a spread of 5 to 10% in the short term must be assumed. The micronutrient version of variant B (172 million) was not changed by the new search while the macronutrient version rose by a third; it may be under-searched. With micronutrients the free-choice optimum is above the macronutrient-only one in 11 of 32 cases (largest: Queensland short term 56.0 against 52.0 million) because the two modes value units without workbook macronutrients differently and so are not strictly nested.
* The staples table (`staples.csv`, stage 3) was produced before this search and is being re-run.
