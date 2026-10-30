# How many people can Australia feed? The model against other estimates (candidate paper 5)

Murray, 2026-10-30: compare the modelling with other authors' estimates made by other methods. This folder holds the verified register of those estimates and the model re-run under their definitions. Figures marked **read** were taken from the source text; **reported** from a search summary or a secondary source and still to be checked; **not reached** where the source could not be opened.

## 1. The estimates

| Estimate | Figure | Definition and method | Status |
|---|---|---|---|
| T. Griffith Taylor, 1920s (cited by the Jones inquiry and by Foran and Poldy) | 65 million "never more", later 20 million by 2000 | Soil and water resources from limited data; a geographer's judgement | **read** (as cited in House of Representatives 1994, para 1.28) |
| CSIRO submission to the National Population Inquiry (Borrie), 1975, Gifford, Kalma, Aston and Millington, *Search* 6(6): 212 | 60 to 70 million if the cropped area were doubled, everything eaten at home, no other constraint (as reported) | Biophysical food production | **reported**; the paper is cited in the Jones report (note to para 2.16) and was not reached |
| Borrie (National Population Inquiry) 1975 | 50 to 60 million possible; Professor Caldwell agreed in 1994 | Inquiry judgement | **read** (House of Representatives 1994, paras 1.61 and 8.4) |
| National Population Council, 1991 | 50 million as a maximum carrying capacity "involving significant social, economic and environmental costs" | Council report | **read** (as cited, House of Representatives 1994, para 2.15) |
| House of Representatives Standing Committee for Long Term Strategies (Jones), *Australia's population "carrying capacity": one nation, two ecologies*, December 1994 | "In subsistence terms Australia has the arable land to produce food for 50 plus million people. But, allowing a safety margin for the possibility of a run of bad seasons, we should regard 30 to 35 million people as the population carrying capacity in terms of the food constraint" | A committee's reading of "reliable estimates" (Gifford et al. 1975 and Henry and Godden 1994 are cited); it calls any such figure "little more than guesstimates" and notes that a trade-based economy is not bound by home-grown food | **read** (paras 2.13 to 2.16) |
| Foran and Poldy, *Future Dilemmas*, CSIRO 2002 | Three population paths: 20, 25 and 32 million in 2050 (17, 25 and 50 million in 2100); Australia keeps a positive food balance out to 2050 and beyond, with fish the exception | Integrated resource-flow modelling of population, technology, resources and environment; no carrying capacity figure | **read** (the summary "Dilemmas Distilled") |
| Bellotti, *The Conversation*, 12 July 2017, "How many people can Australia feed?" | 61 million "could eat Australian food" in 2017: the population plus 36.6 million fed by exports; 92 to 121 million in 2061 | Population plus people fed by exports; imports left out; about 65% of production exported; per-person consumption and drought years not stated | **read** |
| CSIRO and University of Queensland, *Towards a state of the food system report for Australia* (Food System Horizons), 2 June 2025 | The food system "feeds around 100 million people, including 27 million Australians" | Basis not given in the news release; the report (foodsystemhorizons.org) was not reachable (host not on this session's network allow-list) | **read** (release only) |
| National Farmers' Federation and industry | "Feeds 75 million"; grain for about 60 million in an average year, 30 million in a bad drought year | Production against consumption | **reported** |
| Lane, Dawes and Grace 2014, 2015; Lane 2017 | 40 million national, 9 to 40 million by time frame, 23 million summed over regions (thesis method, 2011 data) | This model | **read** (`analysis/model_archive/PAPERS.md`) |
| Peters et al. 2016, *Elementa* 4: 000116 | US agricultural land can support 402 to 807 million people (1.3 to 2.6 times the 2010 population) across ten diets; the average American diet the lowest; lacto-vegetarian highest; vegan lower than two healthy omnivore diets; results highly sensitive to the cropland assumed | Biophysical simulation with losses, processing, livestock feed, land suitability | **reported** (abstract and press releases; full text not reached) |
| Cassidy et al. 2013, *Environmental Research Letters* 8: 034015 | Global crop calories feed about 6 people per hectare delivered, 10.1 as produced; 36% of calories go to feed, 12% of that returns as animal products; growing food only for people could add up to 70% (4 billion people); the US delivers 5.4 people/ha against 16.1 possible | Crop production against use (EarthStat, FAO), conversion efficiencies | **read** (abstract) |
| Alexander et al. 2016, *Global Environmental Change* 41: 88 (HALF index) | The land needed to feed the world's population on a country's average diet, as a percentage of the world's habitable land: **Australia 158, United States 138, India 22, world 49.5 (2011)** | Per-capita land by commodity (FAO) | **read** (values from the Our World in Data table of the paper's data; the paper itself was not opened). The Australian diet is the most land-demanding of those listed, consistent with the model's finding that red meat takes most of the land (about 7 hectares of pasture and 0.3 of cropland a person) |
| Academy of Science 1995; Sustainable Population Australia | About 23 million; below 30 million | Position statements | **reported**; the Jones inquiry records a witness (Professor Stone) for 23 million in 2040; SPA is advocacy |
| FAO and IIASA agro-ecological zones; Global Footprint Network | Not searched | | |

## 2. The model re-run under their definitions (`rerun.mjs`, `rerun.csv`; Australia, today's diet and settings, millions)

| | Published method | Corrected | Improved |
|---|---|---|---|
| Average year (the model's short-term default) | 49.4 | 41.5 | 45.7 |
| **With a drought allowance, the worst year of 10** (the Jones "run of bad seasons") | | **30.8** | **34.0** |
| Worst year of 5; of 20; of 50; of 100 | | 37.0; 26.3; 22.9; 18.9 | 40.8; 29.2; 25.4; 21.0 |
| Cropland doubled out of non-agricultural land, everything eaten at home (the 1975 CSIRO case), average year | | 45.1 | 49.7 |
| No avoidable waste (as in energy and subsistence counts), average year | | 55.3 | 54.7 |
| The model's long term (low-meat, organic, 100-year drought allowance) | 14.1 | 15.6 | 14.6 |

* **The Jones committee's two figures are the model's average year and its 10-year drought allowance.** "50 plus million in subsistence terms" is the model's 41 to 49 (55 with no waste); "30 to 35 million allowing for a run of bad seasons" is the model's 31 to 34 at a 10-year return period. An independent 1994 judgement and the 2026 model agree on the shape of the answer, and the model supplies the drought allowance as a quantity (22 to 25 million at 50 years, 19 to 21 at 100).
* **The 1975 CSIRO estimate of 60 to 70 million with cropland doubled is not reproduced**: doubling cropland adds 9% in the model (to 45 to 50 million) because the short-term diet is bound by pasture-fed meat and dairy, not by cropland. The estimate rested on a grain-based diet and "no other constraints"; the model's own grain-based diets are the nutrition-limited bounds (`analysis/nutrition_lp_2025`: 195 and 387 million), so the 1975 figure sits between the model's present diet and its bounds.
* **The export-inclusive counts cannot be reproduced from energy** (`energy_exports.py`, `energy_exports.csv`): exports of wheat and rice alone supply 128 million people at 2,100 kcal a day, all cereals 183 million, with sugar, canola and pulses 241 million, all foods 258 million, against 36.6 million (Bellotti) and about 73 million (CSIRO and UQ, abroad). The published counts therefore use a smaller per-person basis (or count only food-use grain), which neither source states. This is the first thing to find out before the article compares them; the CSIRO report is the place.

## 3. What the comparison shows

Within the domestic, land-based family the estimates agree better than they first look: about 50 million (and up to 60 to 70 million on 1975 assumptions) in an average year, 30 to 35 million allowing for bad seasons, which the model reproduces (41 to 49 and 31 to 34). The estimates that differ by factors of 2 to 5 differ in definition (people supplied including exports: 61 and 100 million), in time frame (the model's long term, 9 to 15 million, with a 100-year drought allowance, organic farming and a low-meat diet) or in method (resource-flow scenarios without a capacity figure, expert and advocacy positions). Diet moves the land-based answer by 1.5 to 8 times (the optimised bounds), waste by about 1.2, and the drought allowance by 1.4 to 2.2.

## 4. Still to do for the article

* Read the CSIRO and UQ report for its basis; read Gifford et al. 1975, Henry and Godden 1994, Peters et al. 2016 in full; search the FAO agro-ecological studies and the footprint accounts.
* Re-run the model under Peters's own conditions (an Australian ten-diet table with the model's diets) for the like-for-like land-and-diet comparison.
* Decide where it sits in `PUBLICATIONS.md` (a fifth paper, or paper 1's discussion).
