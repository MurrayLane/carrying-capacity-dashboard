# External anchors for the people-fed result (SCOPE.md E12)

Two outside checks on the model's short-term result (Australia, today's diet: 41.5 million corrected, 49.4 published, 45.7 improved; population 27.6 million).

## 1. CSIRO's national stocktake (June 2025)

The first national stocktake of Australia's food system (CSIRO and the University of Queensland, Food System Horizons) reports that the system feeds about **100 million people, 27 million of them Australians** (the rest, about 73 million, abroad through exports). That is a count of food energy produced against a daily requirement, with exports at the diets they feed. The model asks a different question: how many people the land can feed a complete Australian diet, with the meat the diet contains, the losses between farm and plate and the land of the other needs. The two are not comparable as numbers and are not meant to agree: wheat exported as energy feeds many people at 0.3 hectares each; a diet with beef at today's share needs several times that. The model's answer is lower than 100 million for that reason, and a nutrition-constrained version (SCOPE E11) is the way to reconcile them.

## 2. Production against consumption, by food group (`production_scaling.py`, `production_scaling.csv`)

FAO food balance sheet for Australia, mean 2021-23: if all of the production of a food stayed at home and people ate as they do now, the people it would feed are production over the quantity eaten as food, times the population (26.2 million in the FAO series):

| Group | Production over food eaten | People it would feed, million |
|---|---|---|
| Cereals; pulses; sugar | 19; 17; 4.7 | 496; 440; 124 |
| Beef and veal; mutton and goat | 3.0; 3.0 | 77; 79 |
| Fruit | 1.6 | 43 |
| Milk (excluding butter) | 1.5 | 39 |
| Eggs; poultry; vegetable oils | 1.2; 1.1; 1.2 | 32; 28; 32 |
| Starchy roots; pork; vegetables | 0.84; 0.66; 0.54 | 22; 17; 14 |

Reading: the groups Australia produces for export (grains, pulses, sugar, red meat) could feed several times the population; the groups it mostly eats itself or imports (milk, fruit, poultry, eggs) bind at 1.1 to 1.6 times the population, which is **28 to 43 million**, and pork, vegetables and starchy roots are supplemented by imports (275, 2,251 and 554 thousand tonnes; vegetable production in this series, 2.2 million tonnes, looks low against the ABS and should not be leaned on). The model's short term (41.5 million corrected, 45.7 improved, 49.4 published) sits at the top of that band and well below the exporting groups: consistent with a land-based answer that is limited by pasture-fed milk and meat and by cropland, and not contradicted by the production data.

This is a sanity check, not a validation: production is not land, imports and exports of the same food are not netted, and the FAO production series differs from the ABS for several vegetables.
