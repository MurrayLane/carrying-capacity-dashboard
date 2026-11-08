# Method tests for the methods paper (Paper B, sections 5 and 6)

Murray's rule (2026-11-06): the test is the method applied to Australian data, wherever its author first used it; matching an author's own figure is only a fidelity check on the implementation.
One folder per method as each is run. This is the first.

## Energy and protein balance (Gifford et al. 1975; Henry and Godden 1995)

Run: `python3 -I analysis/method_tests_2025/henry_godden.py` from the repository root (reads `fbs_au_world_2021_23.csv`, the FAOSTAT food balance extract made by `extract_fbs.py`). Outputs: `henry_godden_items.csv` (each commodity), `henry_godden_summary.csv`.

**Fidelity check (arithmetic only).** Henry and Godden's own 1990-91 totals (404 x 10^15 J and 306 x 10^10 g, excluding wool and cotton), scaled by Nix's 70 Mha over the 45.7 Mha in use and divided by the consumption factors they inferred from Gifford (0.1760 and 0.2041), give **108.9 and 95.7 million**, their published 109 and 96 (Table 5). So the recipe is implemented as they describe it. The production totals are not rebuilt for 1990-91, because the paper's energy and protein conversion factors are not published (the ABARE 2010 volume lacks fruit, vegetable and egg tonnages; ABS 7503.0 1990-91 is in `Comparators/` if a closer check is wanted).

**Application to current Australian data** (FAO food balance sheets, mean 2021-2023; food products only, imports ignored, exports counted as food, feed, seed, non-food use, losses and processing removed; energy and protein per tonne are FAO's own world averages, nothing typed):

<!-- generated: analysis/method_tests_2025/make_readme_tables.py henry_godden_application -->
<!-- source: henry_godden_summary.csv; commit: df9803e -->
| | Energy (million people) | Protein (million people) |
|---|---|---|
| Production as it is, no scale-up | 138 | 134 |
| Scaled to Nix's 70 Mha, in-use land taken as 1990-91 sown pasture plus 2025 cropping (59.95 Mha) | 161 | 156 |
| Scaled with Henry and Godden's 1990-91 in-use land unchanged (45.7 Mha) | 211 | 205 |
<!-- end generated -->

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

Run: `python3 -I analysis/method_tests_2025/simpson_food.py` (reads `fao_world_land_production.csv`, made by `extract_fao_world.py` from two FAOSTAT bulk files, the food balance extract above, `wackernagel_1994_food_factors.csv`, `second_build_values.csv` and `published_values.csv`; writes `simpson_food.csv`). Consumption 1991-92 is ABS 4306.0 Tables 1 and 3 (`Comparators/`, read from the scan, so values are as printed there; eggs are not collected after 1978-79 and 12.4 kg is carried forward); consumption 2021-23 is the FAO food balance sheet.

**Sources used.** The reconstruction rests on published sources only: the 2000 paper (Research Methods, Results and Table 1, pp. 12 to 14); ABS 4306.0, 1991-92; Wackernagel and Rees 1996, pp. 76 to 85; Wackernagel's 1994 UBC thesis, pp. 279 to 296, with Tables A2.3 and A2.4 on pp. 297 to 298; and, for the wool test only, ABS 7503.0, 1990-91. The authors were not consulted (Murray's decision). The paper gives the recipe and the results; the consumption quantities and productivities behind each cell are taken here from these sources, with the assumptions listed per component, and each component is reported as reproduced or not reproduced on that basis.

**Recipe.** Per-person consumption of each food times the land a tonne needs at world-average productivity, summed to crop land and pasture; imports and exports drop out (a consumption count; paper p. 13). Simpson's energy land (0.43 ha), garden (0.03) and packaging forest (0.08) are not rebuilt: this is the crop-and-pasture part of the food row. Three builds:

* **Build 1** (this script, FAOSTAT 1990-92 world yields): pasture shared among beef, sheep and goat meat and milk by edible protein; pigmeat, poultry and eggs on feed crops (Alexander et al. 2016 feed conversion ratios over the world cereal yield); fruit and vegetables on crop land.
* **Build 2** (V04, `qa/reports/V04_simpson_food.md`): an independent implementation from the same description; pasture shared by production times feed conversion ratio. Its figures are read from `second_build_values.csv`.
* **Build 3, "thesis rates"** (decision 32): the rates Wackernagel's thesis prints, read from `wackernagel_1994_food_factors.csv`, on the same ABS 1991-92 consumption. Assumptions: all red meat (beef, veal, lamb and mutton, carcase weight, 58.4 kg a person, ABS 4306.0 Table 3) on pasture at the sheep-meat rate, and no dairy on pasture; cereals at ABS product weight, each kind at its own grain's yield (flour at wheat, oatmeal at oats, table rice at rice) and other breakfast foods at the cereals average; sugar as cane at 13 kg of cane a kg of sugar (ABS lists cane sugar; the beet ratio of 6:1 is not used); oils and tree nuts at the thesis's placeholder yield of 1,000 kg/ha (flagged: the thesis prints no oil yield); peanuts at the groundnut yield; fruit and vegetables as garden at 15 t/ha; pork, poultry and eggs on feed crop at 6 J of feed a J of food, by food energy, over the cereal food energy and the cereals yield.

**Rates of build 3, with page citations (Wackernagel 1994).** Sheep meat 34 kg/ha/yr (5.5 kg a sheep x 5 sheep an animal unit x 1.24 animal units a hectare, Ensminger 1978, pp. 284 to 285). Wool 10.5 kg/ha/yr gross and 14.2 kg/ha/yr net, with 26% of sheep pasture to meat (p. 285); the wool is scoured (clean) wool (Table A2.3, p. 297). Cattle pasture 0.00322 ha yr a kg of all meat and feed cropland 0.00457 (p. 284; used here only for comparison). World crop yields FAO 1990, Table A2.2 (pp. 295 to 296): cereals 2,646 kg/ha, wheat 2,381, rice 3,350, oats 1,821, potatoes 15,315, sugar cane 60,229, groundnuts 1,124; sugar conversion 13:1 for cane (p. 295). Garden at 15 t/ha (c11, p. 279). Feed ratio 6 for pork, turkey, chicken and eggs and cereal food energy 13,020 kJ/kg (d12, p. 281); food energy of meat 13,000 and eggs 6,120 MJ/t (Table A2.3, p. 297).

**The three builds against Simpson's food row, 1991-92 (ha a person; from `simpson_food.csv`):**

| | Simpson | Build 1 | Build 2 | Build 3 (thesis rates) |
|---|---|---|---|---|
| Pasture (food row) | 1.758 | 1.737 | 2.385 | 1.718 |
| Crop land for animal products (feed) | 0.095 | 0.098 | 0.094 | 0.116 |
| Crop land for plant foods | 0.312 | 0.107 | 0.142 | 0.074 |
| Crop land, food row (plant foods plus feed) | 0.407 | 0.205 | 0.236 | 0.190 |
| Garden | 0.032 | counted in crop | counted in crop | 0.014 |
| Crop plus pasture | 2.165 | 1.942 | 2.621 | 1.907 |

Build 1 in detail:

<!-- generated: analysis/method_tests_2025/make_readme_tables.py simpson_fidelity -->
<!-- source: simpson_food.csv; commit: df9803e -->
| | Rebuilt here | Simpson | |
|---|---|---|---|
| Pasture (beef, sheep, milk) | 1.737 | 1.758 | 1.2% lower |
| Crop land for animal products (feed) | 0.098 | 0.095 | 3.6% higher |
| Crop land for plant foods | 0.107 | 0.312 | **not reproduced (2.9 times lower)** |
| Crop plus pasture | 1.942 | 2.165 | 10% lower |
<!-- end generated -->

**Verdict per component, on the sources used.**
* **Pasture: reproduced within 3% at the thesis's sheep-meat rate (Wackernagel 1994, p. 285)**: 1.718 against 1.758, 2.3% low, with all red meat on pasture and no dairy, which matches the paper's text (pasture for meat and wool, p. 13). Build 1 is 1.2% low and build 2 36% high; the two differ in how world pasture is shared among beef, sheep and milk. At the thesis's cattle rate the pasture would be 0.188.
* **Feed crop: reproduced by builds 1 and 2** (3.6% high and 1.1% low). Build 3 gives 0.116 (22% high) with the Table A2.3 food energies and 0.086 (9% low) with the Table A2.4 energies (meat 11,000, poultry 8,000, eggs 6,000 kJ/kg), so 0.095 lies inside the range the thesis rates give but is not matched by either.
* **Plant-food crop: not reproduced from the published sources.** Build 3 gives 0.074, builds 1 and 2 0.107 and 0.142; none of the readings tested below reaches 0.312.
* **Wool (clothing row, 0.854): not reproduced from the published sources.** Neither the paper nor ABS 4306.0 gives an Australian wool consumption figure; the readings tested are below.
* **Garden:** 0.014 at 15 t/ha against 0.032.
* Simpson's text gives world-average yields with no weighting, so no equivalence factor applies (checker V07).

**Wool test (thesis rates; `simpson_food.csv`, period "1991-92 tests").** 0.854 ha requires 12.13 kg of clean wool a person at 14.2 kg/ha net, or 8.97 kg at 10.5 kg/ha gross. Readings, each with its assumption:
* The thesis's own rule (world wool 0.373 kg a person times an OECD factor of 5, 1.8 kg; p. 285) gives 0.127 ha.
* A per-person share of national production: Australian wool 1990-91 is taken as ABS 7503.0 total wool gross value ($4,180.9 million, Table 22) over the average unit gross value ($3.93 a kg, Table 26), 1,063.8 kt greasy; converted to clean at 0.58 (the thesis's world scoured wool for 1989 over FAO world greasy wool for 1990, the nearest year on hand); over the 1990-91 population (ABS 4306.0, 17,176,910), 35.9 kg clean a person. That gives 2.529 ha at the net rate and 3.42 ha at the gross rate.
* A domestic-use reading (production less exports): 0.854 ha is 33.8% of national production a person at the net rate (25.0% at the gross rate), so it would be reproduced only if exports took the remainder; the sources used hold no Australian wool export figure, so this reading is not tested.

**Plant-crop test (thesis rates; one reading at a time).** Build 3 on food use gives 0.074 ha; with the other items fixed, 0.312 needs 726 kg of grain a person at the cereals yield.
* (a) Total domestic grain use including feed and seed: ABS 4306.0 Table 3 lists grain products for food only (flour, breakfast foods, rice; 89.2 kg a person) with no feed, seed or industrial use, so this reading cannot be built for 1991-92. As a labelled proxy from another period, FAO 2021-23 Australian domestic grain use of 570 kg a person (all uses) gives 0.253 ha, and 229 kg (all uses less feed, since feed sits in the 0.095) gives 0.124 ha. Neither reaches 0.312.
* (b) Total cropland rather than harvested area: the thesis's world ratio of crop land to added-up crop area, 1.159 (p. 296), gives 0.086 ha; its Canadian ratio, 1.737 (p. 296), gives 0.129 ha, and 0.152 ha with garden added. None reaches 0.312.
* (c) The Canadian plant-food crop of 0.183 ha (d11, p. 296) scaled by consumption: by kilograms of the crop foods (cereals, sugar, pulses, nuts, oils, potatoes; Canada 214.0 kg, Table A2.4, against Australia 224.9 kg) it gives 0.192 ha; by cereals alone, 0.212 ha. Neither reaches 0.312.

Result: not reproduced from the published sources. Readings that would need sources not used here (Australian rather than world yields; a 1991-92 Australian grain use including feed and seed) are left open.

**Application to current data (2021-23).** To read a footprint as a capacity, Australia's own cropland and pasture (FAOSTAT land use) are divided by the land a person needs. Build 1:

<!-- generated: analysis/method_tests_2025/make_readme_tables.py simpson_application -->
<!-- source: simpson_food.csv; commit: df9803e -->
| | 1991-92 | 2021-23 |
|---|---|---|
| Crop land, ha a person | 0.205 | 0.198 |
| Pasture, ha a person | 1.737 | 0.860 |
| Crop plus pasture | 1.942 | **1.059** |
| People Australia's cropland supports at that footprint (million) | 85 | 160 |
| People Australia's pasture supports (million) | 257 | 386 |
| People, crop plus pasture together (million) | 238 | **343** |
<!-- end generated -->

Build 3 on 2021-23 consumption, with the thesis rates held at their printed 1990 values and garden counted on cropland: crop land 0.307 ha a person (garden included), pasture 1.047, together 1.354; Australia's cropland supports 103 million at that footprint, its pasture 317 million, and the two together 268 million. Build 2 gives 140 million on cropland and 307 million together (V04).

* The footprint of Australian food land fell by 45% between the two periods in build 1, almost all in pasture: beef consumption fell from 37 to 26 kg and sheep meat from 21 to 10 kg, and world pasture needed per kilogram of ruminant protein fell from 0.105 to 0.060 ha as world output rose.
* Read as a capacity the method gives 103 to 343 million people across the three builds (cropland-bound 103 to 160; crop and pasture together 268 to 343), about two to eight times the accounting model (41 to 54 million short term). The low end is build 3, whose yields are held at 1990 values. The reason the readings are high is the one the method builds in: all of Australia's pasture (332 Mha) counts at world-average productivity, though most of it is rangeland that cannot feed anyone without cropland alongside, and the method has no pairing of pasture-fed food with crops. It is an accounting of land demand, not of a limit.
* Energy land (0.43 ha a person in 1991-92, 16% of Simpson's food row and 22% of the crop-and-pasture part rebuilt in build 1) is a demand on land anywhere, not on Australia's, so it cannot be set against Australia's land in this reading.

**Limits.** Build 1: world yields are FAO group averages (cereals, roots, pulses, vegetables, fruit, treenuts); the oil yield is oil equivalent over the area of ten oil crops; sugar is the world sugar-to-crop ratio; milk is whole-milk equivalent from milk solids at 12.5% solids (1991-92); feed conversion uses carcase weight as edible weight (a slight overstatement). Build 3: oils and tree nuts rest on the thesis's placeholder yield; cereals are product weight, not grain equivalent; the 2021-23 reading keeps 1990 yields. All builds: 1991-92 consumption omits pulses (not in ABS Table 1). Wool pasture is not counted in the food row, as in Simpson's food row.

## Human Appropriation of Land for Food, the HALF index (Alexander et al. 2016)

Run: `python3 -I analysis/method_tests_2025/half_index.py` from the repository root (reads the `half_*.csv` extracts made by `extract_fao_half.py` from three FAOSTAT bulk files; writes `half_index.csv`). The recipe is the paper's and its supplementary information (`Literature review/Alexander2016_SI.pdf`): world cropland allocated by use by mass, processed area shared to products by value (oil crops 50:50, palm 78:11:11, sugar cane 70:26:4 and so on), livestock feed from feed conversion ratios with ruminants taking all pasture, land per tonne at world-average production, and a diet's HALF as the land the world would need if everyone ate it, as a percentage of world land.

**Fat treatment (defect X037).** Raw animal fats get no land of their own (they are a by-product of the meat animals already charged); butter and cream get land through milk's processing share, shared between them by fat content (butter 0.82, cream 0.35 of mass, times world production); cheese stays inside the whole-milk equivalent of milk. This is the reading that reproduces the paper's totals.

**Fidelity check, 2011 data** (HALF, % of world land; the paper's value in brackets; all values from `half_index.csv` after the fix):

<!-- generated: analysis/method_tests_2025/make_readme_tables.py half_fidelity -->
<!-- source: half_index.csv; commit: df9803e -->
| | Rebuilt | Paper | Difference |
|---|---|---|---|
| World | 34.4 | 35.13 | -2.1% |
| United States | 94.5 | 97.73 | -3.3% |
| India | 14.6 | 15.76 | -7.4% |
| Argentina | 109.6 | 114.88 | -4.6% |
| **Australia** | **113.1** | 112.20 | **+0.8%** |
| New Zealand | 94.8 | 135.76 | **-30.2%** |
<!-- end generated -->

World area per person 0.636 ha (paper 0.65). Cropland-to-harvested adjustment 1.165 (paper 1.129); feed cropland 438 Mha (paper 497); pasture 3,182 Mha (paper 3,203); world feed pool 1,147 Mt of dry matter (paper 1,515; independent rebuild 1,106) (script printout). The world and Australia are reproduced within 2.1% and 0.8%; the United States, India and Argentina are 3% to 7% below the paper; New Zealand is not reproduced (30% below) and the cause is not known (dairy and beef dominate its diet, so the treatment of milk, the new food balance's dairy accounting or the omitted commodities are candidates). The earlier version of this section gave Australia 120.9 and the world feed pool as 293: the cake series (tonnes) had been added to feed in thousand tonnes, which made the pool wrong by a factor of a thousand, and monogastric land was then allocated as need over pool (defect X036). Both are fixed, and animal feed cropland now sums to the feed cropland.

**Independent rebuild.** A separate rebuild of the recipe (`half_v02.py`, run by the checker) under the same fat reading gives world 2011 34.07, Australia 2011 112.44, Australia 2021-23 79.81 and Australia's 2021-23 diet on the 2011 production system 86.10. This implementation gives 34.4 (+1.0%), 113.1 (+0.6%), 81.0 (+1.5%) and 86.98 (+1.0%; 2021-23 diet on the 2011 world, with the 2011 population and land). All four agree within 2%.

**Where the land goes, 2011** (Mha; script printout). Pasture: bovine meat 2,131, mutton and goat 255, other meat 129, milk 667 (total 3,182). The paper's bovine share is 1,982 of 3,364 Mha. Here bovine takes 67% of pasture (its share of ruminant feed need); the paper's is 59%. Feed cropland (438) goes wholly to monogastrics, as their need (1,197 Mt) exceeds the pool (1,147 Mt): pigmeat 254, poultry 124, eggs 59. The paper's total food area (4,484 Mha) does not equal its parts, 871 + 3,700 (defect X038).

It is a reconstruction on the new FAOSTAT food balance (2010 onward), not the 2015 download the authors used, and 70 of their 90 commodities (beverages, stimulants, spices, fish, offals, raw animal fats are left out).

**Application to current data (2021-23)** (from `half_index.csv`)

<!-- generated: analysis/method_tests_2025/make_readme_tables.py half_application -->
<!-- source: half_index.csv; commit: df9803e -->
| | HALF, % of world land | Hectares a person | of which animal products |
|---|---|---|---|
| Australia 2011 | 113.1 | 2.09 | 1.98 |
| **Australia 2021-23** | **81.0** | **1.32** | **1.22** |
| United States 2021-23 | 91.9 | 1.50 | 1.38 |
| India 2021-23 | 19.2 | 0.31 | 0.21 |
| World 2021-23 | 34.1 | 0.56 | 0.45 |
<!-- end generated -->

* Australia's HALF fell by 28% between 2011 and 2021-23 on world-average production, because beef and mutton consumption fell and world output per hectare rose. It is still 2.4 times the world average, and 92% of it is animal products.
* HALF is not a capacity and the authors say it is not predictive. Read in the Footprint way, Australia's agricultural land (363.5 Mha of cropland and pasture, FAOSTAT 2021-23) divided by the 1.318 ha a person of its diet at world-average production gives about **276 million people**, the same order as the footprint reading (343 million) and for the same reason: all Australian pasture counts at world-average productivity.
* The model's land per person on the same diet is about 5.9 hectares of pasture and 0.3 of cropland (improved method, `analysis/comparators_2025/diet_land.csv`): about 4.7 times the HALF value (6.2 over 1.318), because Australian beef and dairy come from extensive rangeland, not the global average system.

**Limits.** Stock variation is treated as the paper does (subtracted from the sum of uses); eggs have no processing; milk processed is charged to butter and cream (`Butter, Ghee`, `Cream`), and cheese is inside the whole-milk equivalent of milk; raw animal fats carry no land. Feed dry matter uses assumed shares (cereals and pulses 0.88, oilseed 0.9, roots 0.35, sugar crops 0.25, fruit and vegetables 0.12, milk 0.13), cake from the FAO cake-equivalent series. Feed conversion ratios are the paper's Table 1; the paper's livestock quantities came from the old food balance.

## People nourished per hectare (Cassidy, West, Gerber and Foley 2013)

Run: `python3 -I analysis/method_tests_2025/cassidy_people_per_hectare.py` from the repository root (reads `half_fbs_countries.csv` and `fao_qcl_countries.csv`, the latter made by `extract_fao_countries.py`; writes `cassidy.csv`). The recipe is the paper's: for each major crop the calories produced and the cropland it uses; the crop's calories allocated to human food, animal feed and other uses (biofuels, industrial) from the food balance; feed calories reaching people only as meat, eggs and dairy at the paper's feed-to-food efficiencies (dairy 40%, eggs 22%, chicken 12%, pork 10%, beef 3%); exports allocated by the average use of importing countries; calories over a 2,700 kcal a day diet (985,500 a year) and over cropland gives people fed per hectare, on calories produced and on calories delivered. Cropland only: the authors leave grazing out (beef counts only if grain-fed, sheep and goats not at all).

**Fidelity check.** The paper's years are about 2000 and ours are 2011, so absolute levels should be higher; the structure should match. It does:

<!-- generated: analysis/method_tests_2025/make_readme_tables.py cassidy_fidelity -->
<!-- source: cassidy.csv; commit: df9803e -->
| | Food % | Feed % | Other % | Delivered % | People per ha, produced | People per ha, delivered |
|---|---|---|---|---|---|---|
| World, rebuilt (2011) | 56 | 34 | 11 | 61 | 12.3 | 7.5 |
| World, paper | 55 | 36 | 9 | 59 | 10.1 | 6.0 |
| United States, rebuilt | 27 | 41 | 32 | 33 | 21.0 | 6.9 |
| United States, paper | 27 | 67 | 6 | 34 | 16.1 | 5.4 |
| India, rebuilt | 88 | 10 | 3 | 89 | 8.8 | 7.9 |
| India, paper | 89 | 6 | 5 | 90 | 6.5 | 5.9 |
| China, rebuilt | 60 | 33 | 7 | 65 | 18.4 | 11.9 |
| China, paper | 58 | 33 | 9 | 62 | 13.5 | 8.4 |
| Brazil, rebuilt | 41 | 46 | 13 | 48 | 14.1 | 6.8 |
| Brazil, paper | 45 | 41 | 14 | 50 | 10.6 | 5.2 |
<!-- end generated -->

The calorie shares and the delivery fraction come within a few points of the paper for the world, India, China and Brazil, and the US food share and delivery fraction match (34% against 33%); the US feed share is lower and other uses higher, as expected from the 2000 to 2011 rise of maize ethanol the paper itself describes (6% of maize to ethanol in 2000, 38% in 2010). People per hectare are 22 to 42% higher than the paper's, the size of the world yield gain between the two periods (the crop set also differs: 21 crops, 1,061 Mha, against 41 and 947 Mha).

**Application to current data (2021-23)**

<!-- generated: analysis/method_tests_2025/make_readme_tables.py cassidy_application -->
<!-- source: cassidy.csv; commit: df9803e -->
| | Cropland of the 21 crops (Mha) | Food / feed / other % | Delivered % | People per ha, produced | People per ha, delivered |
|---|---|---|---|---|---|
| Australia | 24.5 | 51 / 42 / 7 | 57 | 10.5 | **6.0** |
| World | 1,162 | 52 / 37 / 11 | 58 | 13.7 | 7.9 |
| United States | 92.5 | 26 / 47 / 28 | 33 | 24.1 | 8.0 |
| India | 164 | 82 / 16 / 2 | 84 | 10.8 | 9.0 |
<!-- end generated -->

* Australian cropland, on these crops, feeds 6 people a hectare on delivered calories, below the world average (7.9) and well below India (9.0); its yields are low (10.5 on produced calories against 13.7 for the world) and 42% of its calories reach feed once its exports follow the importers' average use.
* Read as a capacity (Cassidy's measure is not one), the delivered calories of Australia's 21 crops feed **147 million** people at 2,700 kcal a day on this build (145 to 147 million across the two independent builds), wherever they live; scaled to all 31.65 Mha of cropland at the same rate about 190 million. It is a calorie count: it needs no balanced diet, no protein, and takes nothing from pasture.
* The answer is insensitive to the assumed grain-fed share of beef (0 to 100% moves Australia's delivered figure only from 6.1 to 5.8 people a hectare).

**Independent rebuild (V05, 2026-11-07, `qa/reports/V05_cassidy.md`).** A second implementation, written blind by a different model with about 50 crops on 25.1 Mha (this build: 21 crops on 24.5 Mha), gives Australia 2021-23 at 9.96 people a hectare produced and 5.77 delivered (this build 10.5 and 6.0), 5% and 4% apart; Australia 2011 at 7.55 and 4.26 (this build 7.2 and 4.1); world 2021-23 at 12.8 and 7.3 (this build 13.7 and 7.9), 7% and 8% apart. Calorie shares agree within two points. People fed by Australia's delivered calories: about 145 million (5.77 x 25.1) against 147 here. The choice of how exported crops are allocated alone moves Australia's delivered figure by up to 0.8 people a hectare, more than the gap between the two builds. The Cassidy reading is therefore reported as a range: 5.8 to 6.0 people a hectare delivered, 145 to 147 million (about 190 on all cropland).

**Limits.** Crop energy per kg and the grain-fed share of beef are assumptions typed in the script (the paper's SI was not read); livestock product energy values used only to weight the feed efficiencies are typed too. Oilseed processing is split 50:50 oil and cake by calories. Australia's other crops (vegetables, fruit, cotton, nuts, oil palm and coconut, which Cassidy's 41 may include) are left out.

## Failure probability (Fearnside 1985 and 1990)

Run: `python3 -I analysis/method_tests_2025/fearnside_failure_curve.py` from the repository root (reads `analysis/comparators_2025/rerun.csv`, the model's capacity at each drought return period; writes `fearnside_failure_curve.csv`). Murray's rule applies: there is no fidelity check against Fearnside's Brazilian results (0.24 persons a hectare for a 23,600 ha Trans-Amazon study area); the idea is applied to Australia.

**Fearnside's method.** Capacity is a relation between population density and the probability of failure, not one number: a settler fails in a year when consumption falls below a minimum standard (calories, total protein, animal protein, cash); the failure probability at each density comes from repeated simulations with variable yields (`Literature review/Fearnside1985_stochastic_model_Spanish_translation.pdf`); capacity is the density at which that probability reaches a maximum acceptable level chosen by the planner. His deterministic runs show no failure over densities where the stochastic runs fail often.

**How the model carries it.** The model's drought allowance scales the harvest to the worst year expected once in T years from the 150-year record of wheat, oats and barley yields (`analysis/resilience_2025/`), so capacity at return period T is the population the model feeds in a year of failure probability 1/T. Failure is the model's: the harvest cannot supply the default diet. One criterion, crops only; the herd cycle is handled separately (`analysis/reliability_2025/`).

**Result (corrected method, millions of people):**

<!-- generated: analysis/method_tests_2025/make_readme_tables.py fearnside_result -->
<!-- source: fearnside_failure_curve.csv; commit: df9803e -->
| | Average year (deterministic) | 1 in 5 (20%) | 1 in 10 (10%) | 1 in 20 (5%) | 1 in 50 (2%) | 1 in 100 (1%) | Population | Failure probability a year at the population |
|---|---|---|---|---|---|---|---|---|
| 2011 data | 33.3 | 28.8 | 24.7 | 20.0 | 18.4 | 15.2 | 22.3 | 6.7 to 7.1% (about 1 in 14 to 15) |
| 2025 data | 41.5 | 37.0 | 30.8 | 26.3 | 22.9 | 18.9 | 27.6 | 5.8 to 6.1% (about 1 in 16 to 17) |
<!-- end generated -->

* **Variability is what the average hides, as Fearnside found.** The deterministic figure (41.5 million) says the population is safe; at a maximum acceptable failure of 1 in 10 capacity is 30.8 million (26% lower), at 1 in 100 it is 18.9 million (54% lower). The Jones committee's "30 to 35 million allowing for a run of bad seasons" is the 1-in-10 point.
* **The failure risk at today's population is about 6% a year, close to 2011's 7%.** The margin in an average year is the same (1.5 times the population in both), and so is the weather risk. This agrees with the national headline of Paper A.
* **Every release has the same ratio** of its 1-in-10 capacity to its average-year capacity (0.74), because the allowance scales every yield in the model (crops, pasture products and livestock alike; tested 2026-11-06: scaling all yields by the 0.74 factor reproduces the 1-in-10 capacity exactly) by one factor; the improved method (53.6 and 39.9) puts the failure risk at about 1.5% and the published method at about 2% (2025 data). The risk at the population is therefore as dependent on the method as the capacity.
* The reading here is coarse: six run points, interpolated (the range in the table is linear in T against log T).

**Limits.** One criterion (the default diet) where Fearnside uses four; weather as one factor on every yield, taken from the national wheat, oats and barley record, a proxy for the whole harvest (a field-crop-only shock behaves very differently: 24% lower field-crop yields cut short-term capacity by 0.26%, `results/scenarios.csv`); no feedback of population on yields. The model gives no separate probability of a herd-cycle failure.

## Commodity balance (Foran and Poldy 2002)

Run: `python3 -I analysis/method_tests_2025/foran_poldy_balance.py` from the repository root (reads `fao_au_production_1997_2023.csv` and the food balance extract; writes `foran_poldy_balance.csv`). Their numbers are from the full report (`Comparators/Foran-Poldy-2002-Future-Dilemmas-full-report-02-01.pdf`, Table 1.1 and Table 2.5): 2050 populations 20.6, 25.1 and 32.5 million (zero, 70,000 a year and 0.67% a year net immigration); requirements of grain 2.136, 2.713 and 3.568 Mt, meat 2.278, 2.893 and 3.804 Mt, fish 0.346, 0.439 and 0.577 Mt; 1997-98 production of grain 31.578, meat 3.514 and fish 0.223 Mt; grain embodied in meat a further 6.0, 7.6 and 10.0 Mt.

**The method.** A balance question, not a capacity question: under three population paths and a diet that stays much as it is, does domestic production cover the human requirement of grain, meat and fish? Their answer: yes for every item but fish. The capacity reading, as `analysis/comparators_2025/` derived it, is production over the requirement per person, commodity by commodity; the smallest population binds.

**Fidelity check.**
* FAOSTAT 1997-98 production against their ABS figures: grain 31.95 against 31.58 Mt, meat 3.47 against 3.51 Mt (grain 1.2% higher, meat 1.2% lower).
* Their balance on their own numbers (production over the base-case requirement): grain 11.6, meat 1.21, fish 0.51: positive except fish, as they conclude.
* The capacity reading on 1997-98 production: meat 30 million, grain with feed grain 77, fish 13: the register's 30 to 32 and 76 to 80.
* Their requirement per person is today's diet: grain 108 kg (FAO food use 2021-23: 112), meat 115 kg (113); fish 17 kg (25: Australians now eat more fish than they assumed).

**Application to current data (mean 2021-23 production: grain 52.6 Mt, meat 4.66 Mt, fish 0.29 Mt)**

<!-- generated: analysis/method_tests_2025/make_readme_tables.py foran_poldy_application -->
<!-- source: foran_poldy_balance.csv; commit: df9803e -->
| | On their requirement per person | On actual 2021-23 use per person |
|---|---|---|
| Meat | **40 million** | **41 million** |
| Grain, direct | 486 million | n/a |
| Grain with embodied feed grain | 128 million | 127 million |
| Fish | 17 million | 12 million |
<!-- end generated -->

* The balance is positive for grain and meat and short for fish, as in their 2002 result. The binding commodity among the main items is fish (12 to 17 million people from Australian fish production) and, setting fish aside, meat at **40 to 41 million**.
* **The meat count agrees with the accounting model** (41.5 million in an average year on the corrected method, 53.6 improved), for the same reason: both are bound by pasture-fed meat. The grain figures are three to twelve times larger because grain, most of it exported, is not what limits the diet.
* A balance is a statement about production and a requirement, with no diet balance, no land and no weather: the answer is the commodity that runs out first, and the method has no view of what could replace it (the model's diet changes would).

**Limits.** Their 2050 requirements are scenario outputs; the per-person values are derived by dividing by the scenario populations. FAO cereals are not identical to their 'total grain' (they differ by 1% in 1997-98). Fish production (FAO food balance) includes aquaculture; imports are ignored.

## The model's own entry, and the methods side by side (`cross_method.py`; `model_entry.csv`, `cross_method.csv`)

Run: `python3 -I analysis/method_tests_2025/cross_method.py` from the repository root. It reads the outputs above, `results/` and `analysis/comparators_2025/rerun.csv` and writes the two tables. Every reading, low, high and fidelity text in `cross_method.csv` is built from those outputs; the second builds' figures (Simpson 140 and 307 from V04, with the third Simpson build, thesis rates, read from `simpson_food.csv`; Cassidy 5.77 people a hectare on 25.1 Mha, about 145 million, from V05) are read from `second_build_values.csv`, and the authors' own figures from the folder's table of published values.

**The model's entry (Australia, millions of people; Monte Carlo 5th to 95th percentile, 1,000 draws, 13 uncertain choices; population 27.6 million):**

<!-- generated: analysis/method_tests_2025/make_readme_tables.py model_entry -->
<!-- source: model_entry.csv; commit: df9803e -->
| Tier | Short term | Long term | Worst of 10 years | Worst of 100 years |
|---|---|---|---|---|
| Thesis method as built, errors kept (`2025-mirror`) | 49.4 (43.4 to 54.3) | 14.1 (11.8 to 16.0) | 36.7 | 22.5 |
| **Thesis method, corrected** (`2025-fixed`, the baseline entry) | **41.5 (36.3 to 45.8)** | **15.6 (13.4 to 16.5)** | **30.8** | **18.9** |
| **Improved** (`2025-improved`) | **53.6 (46.2 to 60.1)** | **18.5 (15.9 to 19.4)** | **39.9** | **24.7** |
<!-- end generated -->

**Each method's reading of Australia on current data:**

<!-- generated: analysis/method_tests_2025/make_readme_tables.py cross_method -->
<!-- source: cross_method.csv, fearnside_failure_curve; commit: df9803e -->
| Method | What it counts | What it leaves out | Reading (million) |
|---|---|---|---|
| Energy and protein balance (Gifford; Henry and Godden) | calories and protein of production, exports as food, scaled to a land base | the diet, the pasture and crop pairing, waste | 134 to 211 |
| Ecological footprint, food row (Simpson) | crop and pasture land at world-average productivity | productivity of the actual land, pairing, energy land not set against Australian land | 103 to 343 (cropland-bound reading 103 to 160; crop and pasture together 268 to 343; three builds: two pasture-sharing rules and the thesis rates) |
| HALF index (Alexander) | land at world-average production, by diet | productivity of the actual land, pairing | 276 |
| People per hectare (Cassidy) | cropland calories delivered after feed and biofuel, exports by importers' use | grazing, protein, a balanced diet | 5.8 to 6.0 people a hectare delivered; 145 to 147 million (about 190 on all cropland) |
| Commodity balance (Foran and Poldy) | tonnes of grain, meat and fish against a requirement per person | land, weather, diet change | 40 to 41 (meat), 12 to 17 (fish), 127 to 128 (grain with feed grain) |
| Failure probability (Fearnside) | the harvest in a year of given probability against the diet | one criterion; weather as one factor on all yields | 41.5 (average year), 30.8 (1 in 10), 18.9 (1 in 100) |
| **The model, thesis method corrected** | land, yields, diet, waste, fuel, fibre, reserve | trade, variability between years beyond the allowance | **41.5 (36.3 to 45.8)** |
| **The model, improved** | as above | as above | **53.6 (46.2 to 60.1)** |
<!-- end generated -->

*Table note.* The energy and protein balance reading (134 to 211) is the three land-base scenarios of `henry_godden_summary.csv`; the script's row filter leaves out the 243 million of the plain 8.8 MJ requirement, which changes the consumption factor, not the land base. The Fearnside cell is the same in `cross_method.csv` and here.

**What the comparison shows.**
* **Three groups.** The methods that count calories or land without a diet that has to balance (energy and protein balance, the two land-per-diet methods, people per hectare) read 103 to 343 million, about two to eight times the model. The methods that find the binding commodity (commodity balance: meat 40 to 41, fish 12 to 17) or allow for the weather (Fearnside: 41.5 down to 18.9) read 12 to 41 million; the meat count and Fearnside's average-year point sit at the model's own figure, the fish count and the 1-in-100 point below it.
* **The corrected range (36.3 to 45.8) contains Fearnside's average-year point (41.5) and the commodity-balance meat readings (40 to 41)**, but not the 1-in-10 point (30.8), which lies below it; the improved range (46.2 to 60.1) contains none of them. On the long term, the improved long term (18.5, range 15.9 to 19.4) sits on Fearnside's 1-in-100 point (18.9), because the long-term settings include a 100-year allowance; the corrected (15.6) is 17% below it.
* **Why the high methods are high.** Each takes a quantity (calories, land at world-average productivity) and divides by a per-person need, so exported grain and the whole of the rangeland count at full value. None carries the model's pairing of pasture-fed food with crops, which is what binds Australia; the commodity balance reaches the same figure only because meat is the binding item.
* **The 9 to 100 million spread** of published estimates is therefore partly definition (exports counted or not, drought allowance or not) and partly method (what the method has no way to see); the corrected model on its own data spans 15.6 (long-term settings) or 18.9 (worst of 100 years) to 55.3 (no avoidable waste) by definition alone; 62.9 with the improved settings.
* **The improved tier raises the model's own readings** by about 12 million on the short term and 3 on the long term over the corrected one (beef output by state, dairy on land that can carry it, Australian loss factors), so the choice of Australian settings matters about as much as the corrections (Paper A reports it region by region).

## What moves the number (Paper B, section 6; `design_choices.py`; `design_choices.csv`, `ladder.csv`)

Run: `python3 -I analysis/method_tests_2025/design_choices.py` from the repository root. Each design choice measured with the model on the same data (Australia, 2025, corrected method unless stated; millions of people):

<!-- generated: analysis/method_tests_2025/make_readme_tables.py design_choices -->
<!-- source: design_choices.csv; commit: df9803e -->
| Design choice | Compared | Low | High | High over low |
|---|---|---|---|---|
| Drought allowance | average year against worst of 5, 10, 20, 50, 100 years | 18.9 | 41.5 | 2.2 |
| Avoidable waste | 12% against none (corrected; improved 53.6 to 62.9, 1.17) | 41.5 | 55.3 | 1.33 |
| Land available | cropland as it is against doubled | 41.5 | 45.1 | 1.09 |
| Unit of self-sufficiency | nation against the sum over SA2s (states 75%, NRM regions 44%, SA4 58%, SA3 44%, SA2 37%) | 15.5 | 41.5 | 2.7 |
| Diet | guideline diets from 15% to 5% meat and eggs (improved) | 48.3 | 103.3 | 2.1 |
| Diet, optimised | default against nutrition-optimised diet C (improved) | 53.6 | 422.3 | 7.9 |
| Australian settings | corrected against improved | 41.5 | 53.6 | 1.29 |
| Time frame | long-term settings against short-term settings | 15.6 | 41.5 | 2.7 |
| Exports counted | the model against the CSIRO and UQ proportional count (100) | 41.5 | 100 | 2.4 |
| Exports counted (energy, FAO energy per kg) | the model against the energy count of exports alone, all foods, at FAOSTAT's own food energy per kg | 41.5 | 184 | 4.4 |
| Exports counted (energy, as-traded densities) | the model against the energy count of exports alone, all foods, at typed as-traded densities | 41.5 | 264 | 6.4 |
| Uncertainty | Monte Carlo 5th to 95th percentile, 13 uncertain choices | 36.3 | 45.8 | 1.26 |
<!-- end generated -->

**What drives the model's own uncertainty** (Monte Carlo, share of variance): short term, the herd and meat data window 81% and the red-meat share 16%; long term, the resilience table 52% and the herd and meat data window 36%.

**The ladder: one model, one data set, different definitions** (`ladder.csv`):

<!-- generated: analysis/method_tests_2025/make_readme_tables.py ladder -->
<!-- source: ladder.csv; commit: df9803e -->
| Step | Million |
|---|---|
| The thesis's long-term figure as built (2011 data, biodiesel error kept) | 9.4 |
| Long term, corrected (2025) | 15.6 |
| Worst of 100 years, today's diet | 18.9 |
| Worst of 10 years (the Jones committee's 30 to 35) | 30.8 |
| Average year | 41.5 |
| Average year, improved settings | 53.6 |
| Average year, no avoidable waste | 55.3 |
| Average year, improved, no avoidable waste | 62.9 |
| Exports counted as a proportion (CSIRO and UQ) | 100 |
| Energy count of exports alone | 224 |
<!-- end generated -->

The ladder's energy step is the midpoint (224) of the two readings, 184 (FAO balance energy) and 264 (as-traded densities).

**Reading.**
* **The model's own uncertainty is small beside the definitions.** The 5th to 95th percentile of 13 uncertain choices is a factor of 1.26; the weather allowance is 2.2, the time frame 2.7, the unit of self-sufficiency 2.7, diet 2.1 to 7.9 and exports 2.4 (the proportional count) to 4.4 to 6.4 (the energy count, by the density basis). The answer depends on which question is asked far more than on how well the inputs are known.
* **The published spread (9.4 to 100, a factor of 10.6) can be read along the ladder**: 1.7 from the thesis's own long-term figure to its corrected value (9.4 to 15.6: the 9 is the author's biodiesel error), 4.0 from definitions inside the model (long term 15.6 to improved and no-waste 62.9) and 1.6 from counting exports (62.9 to 100). The three factors multiply to 10.6 by construction (100 over 9.4), so this is a reading of where the spread sits, not a decomposition; the order of the steps is a choice and the ladder mixes the corrected and improved tiers. The order changes the individual factors (corrected to improved is 1.29 at 12% waste and 1.14 with none) but not their product, which chains the same two endpoints.
* **Without counting exports one model spans a factor of 4 from its long-term settings (15.6 to 62.9), or 3.3 from its worst-of-100-years point (18.9)**.
* **Land matters least** (1.09, the smallest factor), with waste (1.17 to 1.33) and the Australian settings (1.29) next: the dispute about how much land could be cropped, and about waste, moves the answer less than the dispute about diet or weather.

**Limits.** The ladder mixes tiers (corrected for the low steps, improved for the high ones), so its steps are not additive and the product is a reading, not a decomposition; the diet rows use the improved method and the nutrition model's ten-micronutrient diets (optimised on the corrected nutrition server, `analysis/nutrition_lp_2025/diets_2025-improved/`); the exports rows are published counts and an energy calculation, not model runs.
