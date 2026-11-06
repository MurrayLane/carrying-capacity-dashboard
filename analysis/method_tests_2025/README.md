# Method tests for the methods paper (Paper B, section 5)

Murray's rule (2026-11-06): the test is the method applied to Australian data, wherever its author first used it; matching an author's own figure is only a fidelity check on the implementation.
One folder per method as each is run. This is the first.

## Energy and protein balance (Gifford et al. 1975; Henry and Godden 1995)

Run: `python3 -I analysis/method_tests_2025/henry_godden.py` from the repository root (reads `fbs_au_world_2021_23.csv`, the FAOSTAT food balance extract made by `extract_fbs.py`). Outputs: `henry_godden_items.csv` (each commodity), `henry_godden_summary.csv`.

**Fidelity check (arithmetic only).** Henry and Godden's own 1990-91 totals (404 x 10^15 J and 306 x 10^10 g, excluding wool and cotton), scaled by Nix's 70 Mha over the 45.7 Mha in use and divided by the consumption factors they inferred from Gifford (0.1760 and 0.2041), give **108.9 and 95.7 million**, their published 109 and 96 (Table 5). So the recipe is implemented as they describe it. The production totals are not rebuilt for 1990-91, because the paper's energy and protein conversion factors are not published (the ABARE 2010 volume lacks fruit, vegetable and egg tonnages; ABS 7503.0 1990-91 is in `Comparators/` if a closer check is wanted).

**Application to current Australian data** (FAO food balance sheets, mean 2021-2023; food products only, imports ignored, exports counted as food, feed, seed, non-food use, losses and processing removed; energy and protein per tonne are FAO's own world averages, nothing typed):

| | Energy (million people) | Protein (million people) |
|---|---|---|
| Production as it is, no scale-up | 138 | 134 |
| Scaled to Nix's 70 Mha, in-use land taken as 1990-91 sown pasture plus 2025 cropping (59.95 Mha) | 161 | 156 |
| Scaled with Henry and Godden's 1990-91 in-use land unchanged (45.7 Mha) | 211 | 205 |

Production is 782 x 10^15 J and 656 x 10^10 g (1990-91: 404 and 306), cereals 65% of the energy.

**What it shows**
* The method gives 134 to 211 million for today's Australia, three to five times the accounting model (41 to 54 million short term), because it counts the calories of production, exports included, as if eaten as grain and ignores the diet; the model's limit is pasture-fed meat and dairy paired with crops.
* The answer depends on three assumptions the method hides: the land base (45.7 against 59.95 Mha moves the result 31%), whether exports are eaten at home, and the consumption factor. The factor Henry and Godden inferred from Gifford is 15.6 MJ a person a day, nearly twice a plain requirement of 8.8 MJ; with 8.8 the same production feeds 243 million.
* The tonnage of production has risen since 1990-91 by a factor of 1.9 (energy) and 2.1 (protein), so the 109 and 96 million of 1995 would roughly double on the same recipe.

**Limits (this is a reconstruction on FAO data, not on the model's own production data)**
* Years are FAO 2021-23, not the model's 2025 data layer; the model's production comes from ABS series and would differ in detail.
* Densities are FAO's world food-supply averages. Oilseed densities (canola 2,290 kcal/kg, cottonseed 5,790) rest on very small world food use and are rough; canola seed is probably undervalued by about half (about 110 PJ rather than 52), which would add about 7% to the energy total.
* Oilseed meal and tallow are not counted as food; wool and cotton fibre are excluded as in the paper; alcohol is excluded.
* The 2025 in-use land (sown pasture) is not measured here; 28.3 Mha is the 1990-91 value carried forward.

## Food-only ecological footprint (Simpson, Petroeschevsky and Lowe 2000)

Run: `python3 -I analysis/method_tests_2025/simpson_food.py` (reads `fao_world_land_production.csv`, made by `extract_fao_world.py` from two FAOSTAT bulk files, and the food balance extract above; writes `simpson_food.csv`). Consumption 1991-92 is ABS 4306.0 Table 1 (`Comparators/`, read from the scan, so values are as printed there; eggs are not collected after 1978-79 and 12.4 kg is carried forward); consumption 2021-23 is the FAO food balance sheet.

**Recipe.** Per-person consumption of each food times the land a tonne needs at world-average productivity (FAOSTAT yield of each crop group), summed to crop land and pasture; imports and exports drop out (a consumption count). Pasture is shared among beef, sheep and goat meat and milk by edible protein; pigmeat, poultry and eggs need feed crops (Alexander et al. 2016 feed conversion ratios over world cereal yield). Simpson's energy land (0.43 ha), garden (0.03) and packaging forest (0.08) are not rebuilt: this is the crop-and-pasture part of the food row. To read a footprint as a capacity, Australia's own cropland and pasture (FAOSTAT land use) are divided by the land a person needs.

**Fidelity check against Simpson's food row, 1991-92 (ha a person):**

| | Rebuilt here | Simpson | |
|---|---|---|---|
| Pasture (beef, sheep, milk) | 1.737 | 1.758 | within 1.2% |
| Crop land for animal products (feed) | 0.098 | 0.095 | within 3% |
| Crop land for plant foods | 0.107 | 0.312 | **not reproduced (2.9 times lower)** |
| Crop plus pasture | 1.942 | 2.165 | 10% lower |

The paper publishes neither its consumption inputs nor its world yields, so this is a reconstruction. The pasture and feed crop come close with different data, which suggests the recipe is right for animal products. The plant-food gap is unexplained; one possibility is that the crop land was weighted by an equivalence factor (Wackernagel and Rees used 2.8 for arable land: 0.107 x 2.8 = 0.298, close to 0.312), which would be inconsistent with the unweighted pasture. Not established.

**Application to current data (2021-23)**

| | 1991-92 | 2021-23 |
|---|---|---|
| Crop land, ha a person | 0.205 | 0.198 |
| Pasture, ha a person | 1.737 | 0.860 |
| Crop plus pasture | 1.942 | **1.059** |
| People Australia's cropland supports at that footprint (million) | 85 | 160 |
| People Australia's pasture supports (million) | 257 | 386 |
| People, crop plus pasture together (million) | 238 | **343** |

* The footprint of Australian food land fell by 45% between the two periods, almost all in pasture: beef consumption fell from 37 to 26 kg and sheep meat from 21 to 10 kg, and world pasture needed per kilogram of ruminant protein fell from 0.105 to 0.060 ha as world output rose.
* Read as a capacity the method gives 160 to 343 million people, four to eight times the accounting model (41 to 54 million short term). The reason is the one the method builds in: all of Australia's pasture (332 Mha) counts at world-average productivity, though most of it is rangeland that cannot feed anyone without cropland alongside, and the method has no pairing of pasture-fed food with crops. It is an accounting of land demand, not of a limit.
* Energy land (0.43 ha a person in 1991-92, a fifth to a third of the food row) is a demand on land anywhere, not on Australia's, so it cannot be set against Australia's land in this reading.

**Limits.** World yields are FAO group averages (cereals, roots, pulses, vegetables, fruit, treenuts); the oil yield is oil equivalent over the area of ten oil crops; sugar is the world sugar-to-crop ratio. 1991-92 consumption omits pulses (not in ABS Table 1). Milk is whole-milk equivalent from milk solids at 12.5% solids (1991-92). Feed conversion uses carcase weight as edible weight (a slight overstatement). Wool pasture is not counted, as in Simpson's food row.
