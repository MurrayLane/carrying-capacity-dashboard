# Tropical staples: what the data allow (SCOPE.md E16, step 3 groundwork)

Murray, 2026-10-28: add the tropical crops if possible; record what cannot be modelled or only with sketchy figures (`DISCUSSION.md`). This is the data side of that: FAO yields of taro, yams, cassava, sweet potato, bananas and plantains, coconuts, oil palm and sugar cane for Papua New Guinea, four other Pacific countries and Australia, 2019 to 2023 (`fao_crops.py`, `tropical_crops_fao.csv`; source FAOSTAT crops and livestock products, Oceania, https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_Oceania.zip).

## What the figures are

Yield, tonnes per hectare, mean of 2019 to 2023 (flags: A official, E estimated by FAO, X from international organisations):

| | Papua New Guinea (E) | Fiji (A) | Vanuatu (E) | Solomon Islands (E) | Model, Australia | Model, NT |
|---|---|---|---|---|---|---|
| Taro | 7.7 | 16.9 | 12.9 | 16.8 | none | none |
| Yams | 17.5 | 19.5 | 20.0 | 10.2 | none | none |
| Cassava | 9.8 | 19.8 | 16.0 | 16.1 | 31.2 (the sweet potato row) | 22.7 (same) |
| Sweet potato | 5.1 | 8.4 | 8.0 | 14.0 | 31.2 | 22.7 |
| Bananas | 16.4 | 13.2 | 10.5 | 2.3 | 28.0 | 14.3 |
| Plantains | none | 32.8 | none | none | none | none |
| Coconuts (in shell) | 6.7 | 5.6 | 4.1 (X) | 3.1 (X) | none | none |
| Oil palm fruit | 12.7 | none | none | 8.8 | none | none |

(Model yields are from release `2025-mirror`, grams per square metre divided by 100; the model's cassava row is the sweet potato yield.)

## What they say about feasibility

* **Taro, yams, coconut and oil palm cannot be modelled from a source that is both official and relevant to the Northern Territory.** The only official series (Fiji) is a small-island, rainfall-fed smallholder system; Papua New Guinea's figures are all FAO estimates (flag E, nearly constant year to year, which means a model, not a count); Vanuatu's and the Solomon Islands' are estimated or from international organisations. For a given crop the country values differ by a factor of two to three (taro 5.6 to 16.9, yams 3.2 to 20.0).
* **Pacific smallholder yields are not Australian yields.** Where both exist, the model's Australian figures are three to six times the Pacific ones (sweet potato 31 against 5 to 14 t/ha) because they are commercial and irrigated. A tropical template for the Northern Territory would be tested against the model's Australian-style yields, not against the Pacific ones, so the Pacific figures bound the downside, not the estimate.
* **The model's own tropical yields are proxies.** NT has almost no recorded cropping, so its sweet potato and banana yields come from the group trend and cassava borrows the sweet potato row. They are placeholders and a tropical template would lean on them.
* **Potential-yield sources (GAEZ) were not checked** for Australia (SCOPE E12); they would give attainable yields by location, crop and water supply and are the better basis for the Northern Territory.
* **The workbook cannot take new foods cheaply.** A crop needs a row on the Yield sheet and one or more food rows on the Base sheet (nutrients, processing yields, waste factors). That is workbook surgery; in the rebuilt dashboard foods would be a data table and a new crop a few lines. The interim route, using existing rows (sweet potato, cassava, banana, potato in the starchy and fruit groups) for the roots and bananas and leaving out coconut and palm oil, gives a tropical-roots template without new crops, but it is not nutritionally adequate by itself.
* **A tropical template must be nutritionally adequate, so it needs the linear programme of the plan** (nutrient reference values with AUSNUT composition) before any capacity is computed. A shifted diet that has not been checked for adequacy would give a misleading capacity, so none is reported here.

## Decision for Murray

Pursue the tropical-staples template in the rebuild, where foods are data (recommended), with the interim existing-rows version and the linear programme first? The yields above go into `DISCUSSION.md` as sketchy figures for the regional diets paper regardless.
