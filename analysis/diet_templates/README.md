# Regional diets (SCOPE.md E16): design note and first results

Murray, 2026-10-28: what if the Northern Territory ate as the tropical north does (Papua New Guinea), or the south ate more meat? This note records what the model's diet is, what the model's own diets already say zone by zone, what a tropical diet would need, and a plan. Nothing here changes a release.

## What the model's diet is

The Diet sheet holds the **NHMRC food-modelling diets** (thesis chapter 8, which cites the NHMRC modelling for sedentary, moderate and high activity): servings a week of 15 food groups for each activity level (sedentary, moderate, high) and each meat and egg share from 0 to 15% in half-point steps, 93 columns in all. Each is nutritionally adequate by the NHMRC's reference values. The model picks the column from the meat and egg share and the activity level, and splits the meat into red and white by the red meat share; the item mix within a food group (which cereal, which vegetable) is the national consumption pattern. Every zone eats the same diet. A regional diet therefore means a different set of group amounts and a different item mix within the groups, and for crops the model does not have, yields.

## What the model's own diets say, zone by zone (first step, done)

`best_diet.mjs` tries the model's diets (meat and egg share 0 to 15%, red meat share 0 to 100%) in every zone with everything else at the release's defaults and records the capacity of each (`best_diet_2025-mirror.csv`, release `2025-mirror`, both presets, 60 zones). Capacity in thousands of people:

| Zone | Default diet (12% meat and eggs, 58% red) | Best diet | Best diet's capacity | Population |
|---|---|---|---|---|
| Australia | 48,004 | 2.5% meat, no red | 114,075 | 27,608 |
| NSW and ACT | 11,988 | 2.5% meat, no red | 32,469 | 9,077 |
| Victoria | 6,957 | 2.5% meat, no red | 13,142 | 7,074 |
| Queensland | 8,845 | 2.5% meat, no red | 14,825 | 5,670 |
| South Australia | 2,383 | no meat | 6,722 | 1,902 |
| Western Australia | 3,562 | no meat | 10,682 | 3,044 |
| **Tasmania** | 304 | **13% meat, all red** | 478 | 576 |
| **Northern Territory** | 61 | **13% meat, all red** | 129 | 265 |

* **The best diet differs by zone, in the direction your question suggests.** Where the land is cropland the most people are fed by a low-meat diet. Where the land is mostly pasture and the cropland is little (the Northern Territory, Tasmania) the best diet is meat-heavy and red, because pasture feeds people through cattle and sheep and crops cannot. In the Northern Territory the default diet feeds 61 thousand, a plant-only diet 60 thousand and an all-red-meat diet 129 thousand; the tropical-staples diet is not in the model.
* **Of the 52 regions in the short term, 17 are best at no meat, 13 at a high-meat, mostly red diet and 22 in between; in the long term (already low in meat) 27 are best at a high-meat, mostly red diet,** which shows how much of the long-term result is a statement about pasture.
* **Reading it.** This maximises people fed from the zone's own land with the model's nutritionally adequate diets. It is not a prediction of what anyone will eat and it ignores preference, trade, culture and cost: a Victoria that fed 13.1 million on a 2.5% meat diet would be doing so by changing what 7 million people eat. It is a scenario about land.

## What a tropical diet would need

FAO food balance sheets, kcal per person per day, 2023 (`fao_diet.py`; `png_food_supply_2023.csv`, `australia_food_supply_2023.csv`):

| | Papua New Guinea | Australia |
|---|---|---|
| Total energy supply | 2,177 | 3,562 |
| Cereals (rice and wheat, imported) | 26.5% | 20.7% |
| Starchy roots (sweet potato 7.4, other roots incl. taro 6.1, yams 3.8, cassava 2.1) | 19.5% | 3.3% |
| Fruit (bananas 8.9) and coconuts | 14.5% and 7.6% | 3.2% and 0 |
| Vegetable oils (palm oil 8.6) | 10.5% | 17.7% |
| Meat (mostly "other meat", 7.5; pigs 2.5) | 11.6% | 13.0% |
| Milk, eggs, pulses | 0 | 10.4%, 0.8%, 3.4% |

* **The real PNG diet is not a template.** Four-fifths of its energy is still rice, wheat, palm oil and sugar bought in, it has no dairy or pulses in the balance sheet, and its energy supply is a fifth lower. It would not meet the NHMRC's nutrient reference values. A tropical template has to be a nutritionally adequate diet built around tropical staples (roots, banana, coconut, fish, leafy greens, nuts and tropical legumes), not a copy of the national average of another country.
* **The model lacks the staples.** It has cassava, sweet potato, banana and tapioca. It has no taro or other roots (6.1% of PNG energy), yams (3.8%), coconut (7.6%) or palm oil (8.6%): about a quarter of PNG energy, and the core of a tropical template. The ABS reports none of them for the Northern Territory, so their yields would come from FAO production and area data and GAEZ (SCOPE E12), checked against the Torres Strait and northern Queensland where there are records.
* **The model's tropical yields are weak.** The Northern Territory has so little recorded cropping that its crop yields are the group-trend proxy; a tropical diet would be tested against yields that are placeholders. This must be flagged or fixed first.

## Plan (in order)

1. **Done:** the best of the model's own diets by zone (this note).
2. **Diet templates as data:** a template is the 15 group amounts and the item mix within groups. Start with those buildable from existing data: national recommended (the model's), actual intake (NNPAS, E7), a low-meat template and a pasture-based template (the best diets above, as named scenarios). Then a Mediterranean template if wanted.
3. **A tropical-staples template:** first the added crops and their yields (E12, a short list), then the template built by a small linear programme: minimise the distance from a staples-weighted preference subject to the NHMRC nutrient reference values, with group composition from AUSNUT (`prelim models/ausnut07full.xls` in the archive has 58 nutrients for 6,356 foods).
4. **Nutrition-constrained optimisation (E11):** the diet that feeds the most people from each zone's land, subject to the same constraints, instead of choosing a template. Steps 2 and 3 are its special cases; this is the second model of the papers.
5. **On the dashboard (the rebuild):** a diet picker per zone ("model default", "best for this land", "low meat", "pasture-based", "tropical staples"), shown beside the likely range (DELIVERY.md) and never as a prediction.

## Decisions for Murray

* Is the "best diet for the land" shown as a scenario only ("what this land could feed on a diet that suits it"), as it is written above? I recommend yes: it is evidence about land use, not advice about what people should eat.
* Add the tropical crops (taro and other roots, yams, coconut, a palm oil share) as a short list with FAO and GAEZ yields, in step 3?
* Which of the model's dimensions should the templates also vary: the activity level, avoidable waste, the share of food eaten that is imported (zero by the model's design)?
