# Paper B, methods: well-known carrying-capacity methods tested on common Australian data

First draft, assembled 2026-11-13 from B_s01-03.md, B_s04-05.md, B_s06-09.md. Every number traces to the claims csv beside each section file; sentences marked [gate 4] in those csvs use values awaiting Murray's gate 4 approval. Not for circulation.

# Paper B, sections 1 to 3 (first draft, D02; cut to the main-text limit, B98b)

## Abstract

Published estimates of how many people Australia can feed run from about 9 to 100 million, a factor of 10.6. This paper asks how much of that spread is the definition, the diet or the method, and which method suits which purpose. It is a critical review, with a narrative synthesis, of carrying capacity methods for food and land. The methods were sorted into families by the question each answers. Seven, including the author's own land-and-diet model, were applied to one 2025 Australian data set (FAOSTAT 2021-23) and checked against their authors' published figures where these could be reached. The design choices behind the published figures were measured one at a time in the model. The aggregate methods read 134 to 343 million, about three to eight times the model. Equalising inputs did not narrow the spread among methods, which stayed at 12 to 343 million: the gap between the methods is the method. By definition alone the model spans 18.9 to 55.3 million, while its spread across defensible settings is a factor of 1.26. No single method serves every purpose. Planners and analysts should choose the method by purpose and report a capacity figure with its question, diet, waste, weather allowance, land base, unit and time frame.

## 1. Introduction

Published estimates of how many people Australia can feed run from about 9 to 100 million, although one figure in Table 1, Henry and Godden's energy count of 109 million (1995, p. 100), sits above that span. Each was offered as a count of how many people Australia can feed. Both ends of that span are soft. The low end, 9.4 million, is the author's own long-term figure, from the thesis method as built on 2011 data before its errors were corrected (Lane 2014, p. 280). Run unchanged on 2025 data, the same method gives 14.1 million; this paper calls the 9 to 14 million figures the published method. The high end is the "around 100 million people in total" of a 2025 food system report: 27 million fed at home and another 63 million fed abroad, extrapolated from the share of production that is exported (CSIRO and University of Queensland 2025, p. 30). The two parts sum to 90 million. The report itself calls this metric misleading as an indicator of food security (p. 30).

Bellotti (2017) counted 61 million who would eat Australian food in 2017: the population plus 36.6 million people fed, at least in part, by exports. The published span from 9.4 to 100 million is a factor of 10.6. Because both ends are soft, the span shows that published figures differ by an order of magnitude; it is not a measured spread of independent estimates. Table 1 lists the published figures with the definition behind each.

The spread is old. Henry and Godden (1995, p. 97) reported a range of 10 to 480 million from a 1986 committee (Migration Committee 1986), taken in turn from a 1990 review, so it is known here only third-hand. A 1975 CSIRO submission, not held, gave 82 million on food energy and 60 million on protein, with all production eaten at home (Gifford et al. 1975, as reported in Henry and Godden 1995, p. 98, and Chisholm 2000, p. 21). At world scale, Cohen (1995, pp. 341 to 343) showed that estimates of human carrying capacity depend on natural constraints and on human choices about diet, technology, environment and wellbeing.

The spread matters because capacity figures enter debate about population, food security and land. Australian population planning draws on the Intergenerational Reports (Treasury 2021; Treasury 2023) and the Population Statement (Centre for Population 2025), and Bolleter (2018, p. 123) drew on Lane (2017) to weigh settlement scenarios for northern Australia against the carrying capacity of the land. Abroad, carrying capacity is assessed for European and Chinese cities (Świąder et al. 2020; Zhang et al. 2018) and used in China's regional functional planning (Qiu 2024).

This paper asks how much of the published spread is the definition, the diet or the method, and which method suits which purpose.

The paper follows the 2010 review of carrying capacity methods for land-use planning (Lane 2010) and chapter 6 of the thesis (Lane 2014), which reviewed Limits to Growth, the ecological footprint, the South East Queensland, Noosa and Douglas Shire studies, Peters for New York State, Fairlie for Britain and Fearnside for Brazil; the 2010 review covered the same methods except Douglas Shire and Peters. It adds the method families the earlier work did not cover (energy and protein balance, integrated resource flow, people per hectare, a land-per-diet index and a food-only footprint) and the literature since 2011, including a water-bounded method for Iran that cites the thesis (Khorsandi et al. 2022; not seen; cited from its abstract). Fearnside's method, reviewed in the earlier work, is applied here as a test. Each method is tested on the same 2025 Australian data, the effect of each design choice is measured, and the results are drawn into a guide.

One of the methods reviewed is the author's own, developed in a doctoral thesis (Lane 2014) and in papers to 2017 (Lane, Dawes and Grace 2014; Lane, Dawes and Grace 2015; Lane 2017; each not seen; cited from its abstract). It is entered as published and as built on, held to the same tests as the other methods, and named again in the competing-interests statement.

**Table 1.** Published estimates of how many people Australia can feed, with the definition behind each. Built from `analysis/comparators_2025/harmonisation.csv` (all rows except PMSEIC 2010) and `analysis/method_tests_2025/published_values.csv` (PMSEIC 2010, ladder row). "Read" means the figure was read in the source; "second-hand" means it was read in a source that reports it.

| Estimate | People (million) | Data year | Exports counted | Diet and waste | Drought allowance | Route to the figure |
|---|---|---|---|---|---|---|
| Gifford et al. 1975 | 82 (energy) or 60 (protein) | 1970s | no (all production eaten at home) | contemporary consumption, no waste allowance | none | second-hand (Henry and Godden 1995; Chisholm 2000) |
| Henry and Godden 1995 | 109 (energy) or 96 (protein), excluding wool and cotton | 1990-91 | no | energy and protein equivalents, no waste allowance | none | read |
| Foran and Poldy 2002 | 30 to 32 (meat) and 76 to 80 (grain with feed grain) | 1997-98 production, 2050 requirements | no (domestic requirement only) | requirement per person from their diet scenarios | none | read; derived here from their Table 2.5, as the authors give no capacity figure |
| PMSEIC 2010 | 60 | not given | by implication only | not given | not given | read; stated without a source |
| Lane, Dawes and Grace 2014, 2015; Lane 2017 | 40 national (9 to 40 by time frame; 23 summed over regions) | 2011 | no | default diet, waste 12% | long term: 100 years | the author's own (thesis method); read in Lane 2014, p. 280 |
| Bellotti 2017 | 61 (the population plus 36.6 fed by exports) | 2017 | yes (the larger part) | not stated | not stated | read |
| CSIRO and University of Queensland 2025 | about 100 (27 at home plus 63 abroad) | 2025 | yes | not stated | none | read |

## 2. The concept, its refinements and its critics

This section asks whether carrying capacity is a sound idea when applied to people, and why planners still use it. The thesis (Lane 2014, chapter 6) and the 2010 review (Lane 2010) give a fuller account, and supplementary section S1 the further positions summarised here in one sentence each.

The term has several roots. Sayre (2008) traced it from shipping, where it meant what a vessel could carry, to range management, where it meant the stock a pasture could hold, and Australian pastoral records are among the cases he cites (p. 124). From there it was joined to the asymptote of the logistic curve, the K of population ecology. Sayre separates a static reading, a fixed ceiling, from a variable reading, a ceiling that moves with conditions. A review of the term's ecological uses set human populations aside by design (Chapman and Byron 2018).

Some authors defend the concept and extend it. Hardin (1986) accepted that capacity is imprecise but held that it is needed: because overshoot is serious, "the conservative approach is to stay well below the best estimate of carrying capacity" (p. 601). He proposed a cultural carrying capacity, set by the quality of life a society chooses and always below the biological limit (p. 603). Meyer and Ausubel (1999) modelled a limit that itself rises. Hopfenberg (2003) tied human capacity to food availability. Gilland (2006, p. 2) held that an estimate can be defensible if its assumptions apply to a stated period and it is not taken as an ultimate limit.

Other authors question the concept. Seidl and Tisdell (1999) argued that once human activity is involved the concept becomes normative, so that there is "no longer an objective, single level of carrying capacity" (p. 405). Sayre (2008, p. 131) found that a static capacity is "theoretically elegant but empirically vacuous", while a variable one is "theoretically incoherent or at best question-begging". Price (1999, p. 17) concluded that the concept is "seriously flawed" and "may be no more than a self-validating belief". His example was the Tasmanian sheep population of the nineteenth century, which levelled out because farmers learned not to overstock their pastures, not because of a natural limit (pp. 9 to 10). Cohen (1995) held that capacity is dynamic and depends on human choices, and that human carrying capacity "cannot be defined for a nation independently of other regions if that nation trades with others" (p. 343). That point bears directly on Australia, which exports most of its agricultural production (CSIRO and University of Queensland 2025, p. 30).

The ecological footprint turned the question around. Rees (1992) asked not how many people an area can support but how much land a given population needs, and Rees (1996) built area-based indicators on world-average productivities. Chisholm (2000) argued in the Australian debate that resource limits do not set population limits in economies open to trade and new technology. Giampietro and Saltelli (2014) argued that the footprint protocol has no external referent.

The debate since 2016 has moved to planetary limits and overshoot. The planetary boundaries framework proposed boundaries that "define the safe operating space for humanity" (Rockström et al. 2009, p. 472); it does not use the words carrying capacity. Overshoot accounts had been built at world scale (Wackernagel et al. 2002), and Rees (2023) argues that humanity has exceeded its long-term carrying capacity. O'Neill et al. (2018) set social thresholds against shares of biophysical boundaries, nation by nation. Biermann and Kim (2020) appraised the approaches used to define planetary limits. Montoya et al. (2018) argued that the boundary for biodiversity lacks support for a global threshold. Herrington (2020) found that, of the World3 scenarios of Limits to Growth, comprehensive technology fitted most observed variables best, with a business-as-usual variant close behind. Wang (2022) framed land carrying capacity as a question of food security, to be set region by region.

Planners still need the concept, whatever its standing in ecology. They must judge whether a region's land and water can feed the population they plan for, and a capacity figure puts that judgement in numbers. The critics show what such a figure needs: a stated question, a stated standard of living and diet, and a stated time frame. Sections 5 and 6 make those choices explicit for each method. The thesis classed earlier methods by their inputs and outputs and by their scale (Lane 2014, chapter 6), and section 4 uses the same typology.

## 3. How the review was done

### 3.1 Review method (narrative and critical reviews)

This paper is a critical review in the sense of Grant and Booth (2009, p. 94): it draws on wide reading and critical evaluation and goes beyond description to a model, here a guide to which method fits which purpose. Its synthesis is narrative, which Greenhalgh et al. (2018, p. 2) argue serves a different purpose from a systematic review, not a lesser one; a question of method fit calls for interpretation across methods, not for pooling comparable results. A narrative review can be rigorous when it states its boundaries and justifies what it includes and excludes (Sukhera 2022, pp. 414 to 415), and any review should state its selection rule and what it left out (Snyder 2019, p. 337; Haddaway et al. 2020, p. 1583).

Works published from 2011 onwards, by year of publication, were eligible. Works published before 2011 were included only to trace the lineage of a method or concept. Within those bounds the review covered the well-known methods across the main approaches, and excluded index methods with no basis in food or land.

Works came from four routes: the author's citation exports and the OpenAlex list of works citing the author's papers; a sweep for each method family; a scoping search for the concept and the review method; and a recency sweep of Crossref. Government documents on population, food security and food waste were taken as grey literature.

Each cited work carries a reading label in the literature register in the paper's archive: read in full, read at page level, read in a targeted way (named passages only), reported (held only through another source, as the 1975 CSIRO figures are), or record only. Where no file of a work is held, the work is cited as reported in a held work that reports it; where no such work is held, the text says once that the work was not seen and is cited from its abstract.

The planning-oriented methods named in section 1 were covered by the earlier work and are not repeated. Section 5 sets out the test design: a common data set, and a fidelity check against each method's authors.

---


## 4. A catalogue of methods

This section sorts the methods into families by the question each answers, its inputs and outputs, and its scale, and states what each can and cannot see, so that the question behind each published figure is clear before section 5 compares any number. The planning-oriented studies of the earlier review (Lane 2010) get one line each. Table 2 carries inputs, outputs and scale, and supplementary section S2 gives the fuller account of each family.

[Table 2: the catalogue of methods (family, question answered, inputs, outputs, scale, sources); to be built from a catalogue csv that does not exist (see Drafter notes)]

[Figure 1: the methods mapped by the question each answers, from the same catalogue csv (not built)]

### 4.1 Resource-based land and diet

The method sets the land a population needs for a stated diet against the land available. Peters, Wilkins and Fick 2007 built a complete-diet land model for New York State, with land in three classes. Peters et al. 2016 applied the same frame to the United States under ten diets, and Fairlie 2007 drew a land budget for Britain under six farming regimes. The author's thesis method belongs here (Lane 2014): it pairs pasture-fed food with crops, charges land for waste, fuel, fibre and a reserve, and reads capacity as the population the land feeds on a stated diet. The foodshed is the spatial form of the same method, adding where the land lies relative to the people (Peters et al. 2009; Zumkehr and Campbell 2015; Kurtz et al. 2020). The method sees land, yields and diet together; it does not see trade, and sees variation between years only through an allowance.

### 4.2 Energy and protein balance

The method counts the food energy and the protein of domestic production, treats exports as food, scales production to a potential land base, and divides by a consumption factor per person (Henry and Godden 1995). It counts each nutrient alone, with no diet that has to balance, no waste and no pairing of pasture with crops. Its founding work (Gifford et al. 1975) and its land base, Nix's estimate of land for intensive production, are both cited as reported in Henry and Godden 1995 (p. 98). Shepon et al. 2016 (not seen; cited from its abstract) use the same currencies to estimate a gain from reallocating feed cropland, not a capacity.

### 4.3 Commodity balance and the nutritional food balance

A commodity balance asks whether domestic production covers the human requirement for each commodity, item by item. Foran and Poldy 2002 set the requirements for grain, meat and fish under three population paths to 2050 against production. They give no capacity figure; one can be read as production over the requirement per person, the smallest population binding. The method sees tonnes, not land, weather or a change of diet. Ridoutt et al. 2017 extend the balance to nutrition in an index that carries no people count.

### 4.4 Export-inclusive counts

Export-inclusive counts add the people fed abroad by Australian exports to the people fed at home. CSIRO and UQ 2025 extrapolate in proportion: if the share eaten at home feeds the population, the exported share feeds a proportional number abroad. PMSEIC 2010 states, with no source, that Australia produces enough food to feed 60 million people (p. 1), and on p. 15, citing the federal agriculture department, that production feeds some 40 million people outside Australia; it does not add the two. These counts are neither energy-based nor land-based, and assume that exports would be eaten in the proportions of the domestic diet.

### 4.5 Ecological footprint

The footprint inverts carrying capacity: it asks how much productive land a population appropriates, wherever that land lies (Rees 1992; Rees 1996). Wackernagel 1994 set out its rates: the land a tonne of each product needs at world-average productivity. The food row sums consumption per person times that land, so trade drops out; it becomes a capacity only when a country's own land is divided by the land a person needs. Simpson, Petroeschevsky and Lowe 2000 applied the method to Australia, and Lenzen and Murray 2001 modified it to count Australia's actual land use. Its critique and defence are in section 2 and section S2. The method sees the demand for land at world-average productivity, not the productivity of the actual land or any pairing of pasture with crops.

### 4.6 Land per diet and people per hectare

Land-per-diet indices express a diet as the land it needs at a stated productivity. Alexander et al. 2016 define the HALF index: the land the world would need if everyone ate a given country's diet, as a share of world land, at world-average production. Livestock are charged for their feed and ruminants take all pasture; the authors state that the index is not predictive (Alexander et al. 2016, p. 89). Cassidy et al. 2013 turn the measure around: people nourished per hectare of cropland, with feed calories returned as meat, eggs and dairy at fixed efficiencies, exports following the average use of the importing countries, and a diet of 2,700 kcal a day (p. 4). Cropland is the only land counted, so grazing is left out. These methods see land at world-average productivity, or crop calories, by diet, but not the productivity of a country's own land or a diet that has to balance.

### 4.7 Optimisation models (diet and land use)

Optimisation models choose a diet or land use that meets stated limits at least cost or least departure from what is observed. Chaudhary and Krishna 2019 optimised national diets against nutrient limits and per-person limits drawn from planetary boundaries; Gazan et al. 2018 and van Dooren 2018 review diet optimisation. LUTO, a land-use optimisation model of Australia, allocates land uses on a fine grid against land-sector targets (Gao and Bryan 2017). These models see trade-offs among nutrients, cost and environmental limits; a people count is not their output.

### 4.8 Integrated resource-flow models

Integrated resource-flow models trace stocks and flows of land, water, energy and materials through an economy. Foran and Poldy 2002 built the Australian framework behind their commodity balance; no method paper for it was reached. Hatfield-Dodds et al. 2015 and Bryan et al. 2016 ran national scenario models of Australia, and Navarro Garcia et al. 2022 ran the FABLE Calculator for Australia (Jones et al. 2023); none gives a people count. The World3 line asks whether the world system overshoots (Herrington 2020); Limits to Growth itself is covered in Lane 2010. These models see feedbacks and pressures, not how many people the land can feed.

### 4.9 Water-bounded capacity

Water-bounded methods cap capacity by land suitability, water and realistic yields. Khorsandi et al. 2022 combine land suitability, water and a cap on the share of net primary production that people take, at several spatial scales in Iran; their capacity falls as the units become smaller and more local. Khorsandi et al. 2023 (not seen; cited from its abstract) simplify the method, which is catalogued here and not tested in section 5. Land-suitability assessment is its basis (Fischer et al. 2002; Mesgaran et al. 2017). These methods treat as limits what the land and diet methods take as given.

### 4.10 Failure probability

Fearnside 1985 defines capacity as a relation between population density and the probability that settlers fail, not as one number. A settler fails in a year when consumption falls below a standard; Fearnside tests calories, total protein, animal protein and cash separately, with the calorie standard set at 2,550 kcal a person a day (Fearnside 1985, p. 352). Yields and weather are drawn from fitted distributions over runs of years at fixed densities. Capacity is read from the curve of the failure rate, the share of settler-years below the standard, against density, at the maximum failure probability the planner accepts. The method sees variation between years, which the other families average away.

### 4.11 Index methods and planning studies

Graymore, Sipe and Rickson 2010 rank regional indicators against thresholds in place of a carrying capacity they treat as not measurable, so their index gives no people count. Of the planning-oriented studies, Gutteridge 2005 set a footprint against a carrying capacity for South East Queensland. The Noosa and Douglas Shire studies applied carrying capacity to local planning; the Noosa study is cited through Lane 2010 and the Douglas Shire study through the thesis (Lane 2014, chapter 6) only.

## 5. Testing the methods on common Australian data

Each method was applied to the same Australian data and, where its authors' own figure could be reached, checked against it. Tables 3 to 5 carry the numbers; supplementary section S3 gives the implementation detail and the arithmetic of each fidelity check.

### 5.1 The common data set

Every method used one population, the model's 2025 figure of 27.6 million, and one data year, FAOSTAT 2021-23, with the model's 2025 data taken as the same vintage. The land base is Australia's 31.65 Mha of cropland and 331.87 Mha of pasture, 363.5 Mha in all, which equals the model's ABS holdings to within 0.01 Mha. The consumption basis is the FAO food balance per person for 2021-23, 3,525 kcal and 120.7 g of protein a day, which rests on FAO's head count of 26.20 million, not the model's population.

### 5.2 Fidelity check and test

A fidelity check compares an implementation with its authors' published figure on their data; the test applies the method to Australia on the common data. Each component checked was reported as reproduced or not reproduced on the sources the project had; where no published figure could be reached, the method was reported as implemented from its published description alone. The authors were not consulted; a second build, where one exists, was written independently from the same description.

### 5.3 Energy and protein balance

*Access.* Henry and Godden 1995 print the recipe, its 1990-91 production totals and the consumption factors they infer from Gifford et al. 1975 (p. 99).

*Fidelity.* Run on the printed totals, the recipe gave 108.9 million (energy) and 95.7 million (protein), against the published 109 and 96 (p. 100): reproduced within rounding. The 1990-91 totals were not rebuilt, because the factors for each item are not published.

*Test.* On the FAO food balance for 2021-23, with exports counted as food, the method reads 134 to 211 million: two currencies and three land-base cases, not an uncertainty range, with the 1990-91 in-use land carried forward (section S3.1).

*What it hides.* The land base, exports counted as if eaten at home, and a consumption factor nearly twice a plain requirement (section S3.1).

### 5.4 Ecological footprint, food row

*Access.* Simpson, Petroeschevsky and Lowe 2000 give a food row of 1.758 ha a person of pasture, 0.095 ha of crop land for feed and 0.312 ha of crop land for plant foods (Table 1, p. 14); the rebuild also drew on ABS 4306.0 for consumption in 1991-92, Wackernagel and Rees 1996, and the rates in Wackernagel 1994.

*Fidelity.* Three builds differ in how pasture is charged (section S3.2). Pasture is reproduced within 3% in build 3, at the sheep-meat rate Wackernagel's thesis prints (Wackernagel 1994, p. 285): 1.718 ha against 1.758. Build 1 also comes close, but not at that printed rate. Crop land for feed is reproduced by builds 1 and 2; build 3 is 22% high. Crop land for plant foods and the clothing row's wool pasture are not reproduced.

*Test.* Australia's land divided by the land a person needs on consumption in 2021-23 gives 146 to 343 million on current yields, and 103 million with build 3's yields held at their printed 1990 values. The readings are high chiefly because all of Australia's pasture, most of it rangeland, counts at world-average productivity, with no pairing of pasture-fed food with crops.

### 5.5 HALF index

*Access.* Alexander et al. 2016 and its supplement, which prints each country's index (their Table S5, p. SI-6); the rebuild used FAOSTAT's food balance series that starts in 2010, not the authors' download.

*Fidelity, on 2011 data.* The index is reproduced for the world, 34.4 against 35.13 (2.1% low as printed, 2.2% unrounded), and for Australia, 113.1 against 112.20 (0.8% high). New Zealand is not reproduced (94.8 against 135.76). A second, independent build agrees within 2%; Table 3 gives the other countries.

*Test.* Australia's diet in 2021-23 needs 1.32 ha a person at world-average production, a HALF of 81.0% of world land. Read in the footprint way, which HALF is not, Australia's 363.5 Mha divided by 1.318 ha a person gives about 276 million people.

### 5.6 People per hectare

*Access.* Cassidy et al. 2013 print the recipe, the feed-to-food efficiencies kept here (Table 1, p. 3) and results for the world and four countries (Table 2, p. 3). Their supplementary information was not read, so crop energy per kilogram and the grain-fed share of beef are assumptions.

*Fidelity, on 2011 data against the paper's years of about 2000.* The calorie shares and the delivered fraction come within a few points of the paper for the world, India, China and Brazil. The United States is not reproduced (section S3.4). People per hectare are 22 to 42% above the paper's, on 22 crop items against the paper's 41 crops (p. 4). A second, independent build agrees within 5% for Australia and 8% for the world on delivered calories.

*Test.* On 2021-23 data Australian cropland delivers 6.0 people a hectare, against 7.9 for the world. Read as a capacity, which Cassidy's measure is not, the delivered calories of Australia's 22 crop items feed 147 million people at 2,700 kcal a day, and 145 million in the second build. With each winter crop paired with the harvest it came from, all 31.65 Mha of cropland would feed about 183 million in place of about 190 (section S3.4).

### 5.7 Commodity balance

*Access.* Foran and Poldy 2002 set the 2050 requirements for grain, meat and fish against production in 1997-98 (Table 2.5, p. 64). They give no capacity figure, so the reading is this project's (section 4.3): each scenario's requirement divided by its population.

*Fidelity.* FAOSTAT reproduces their 1997-98 production of grain and meat within 1.2% each way, and their balance is positive for grain and meat and short for fish, as they conclude.

*Test.* On production in 2021-23, meat supports 40 million people on their requirement per person and 41 million on actual use, grain with its embodied feed grain 128 and 127 million, and fish 17 and 12 million. The fish reading counts a single commodity, with no diet change through which another food could replace fish.

### 5.8 Failure probability

*Access.* Fearnside 1985 gives the method and Fearnside 1990 one result for a Brazilian study area (p. 195), which Australian data cannot check, so the failure frame was applied as a test of the idea, not as an independent method.

*Assumptions.* The model's drought allowance scales the harvest to the worst year expected once in T years, from a 150-year record of wheat, oats and barley yields, so the capacity at return period T is the population the model feeds in a year with a failure probability of 1/T. The readings are the model's own runs (limits in section 8.1).

*Test.* On the corrected model with 2025 data, capacity is 41.5 million in an average year. At a maximum acceptable failure of 1 in 10 it is 30.8 million, 26% lower, and at 1 in 100 it is 18.9 million, 54% lower. At the 2025 population the failure probability is 5.8 to 6.1% a year, about 1 in 16 to 17, and it depends strongly on the method (section S3.6).

### 5.9 The author's model as an exemplar

The author's model (Lane 2014) was tested like the other methods at three tiers, each from a frozen release: the thesis method as built with its errors kept, the thesis method corrected, and an improved tier that builds on it with Australian settings (Table 4). Each tier carries a Monte Carlo range (section 6.9). On 2025 data the corrected tier, the baseline entry, reads 41.5 million in the short term (36.3 to 45.8) and 15.6 million in the long term (13.4 to 16.5).

Table 4. The model's entry for Australia, 2025 data, by tier (million people; Monte Carlo 5th to 95th percentile in brackets). Built from `analysis/method_tests_2025/model_entry.csv`.

| Release | Tier | Short term | Long term | Worst of 10 years | Worst of 100 years | Population |
|---|---|---|---|---|---|---|
| 2025-mirror | Thesis method as built, errors kept | 49.4 (43.4 to 54.3) | 14.1 (11.8 to 16.0) | 36.66 | 22.51 | 27.6 |
| 2025-fixed | Thesis method corrected (the baseline entry) | 41.5 (36.3 to 45.8) | 15.6 (13.4 to 16.5) | 30.81 | 18.92 | 27.6 |
| 2025-improved | Improved (built on) | 53.6 (46.2 to 60.1) | 18.5 (15.9 to 19.4) | 39.93 | 24.68 | 27.6 |

### 5.10 The methods side by side

In Table 3 the readings fall into three groups. The first is the aggregate methods (the energy and protein balance, the footprint, HALF and people per hectare), which count calories or land with no diet that has to balance. They read 134 to 343 million (the footprint 146 to 343 on current yields, 103 at 1990 yields), about three to eight times the model. The second, the commodity balance, reads 12 to 41 million; its low end is the single-commodity fish reading, and its meat reading of 40 to 41 million is bound, as the model is, by pasture-fed meat. The third, the failure view, is the model's own runs under the weather allowance, set beside the model rather than against it; its 1-in-10 point, 30.8 million, lies below the corrected range of 36.3 to 45.8 million.

Table 3. Each method's reading of Australia on current data (million people unless stated). Built from `analysis/method_tests_2025/cross_method.csv`; four cells differ from the csv, as the table note says.

| Method | What it counts | What it leaves out | Reading for Australia | Fidelity check against its authors |
|---|---|---|---|---|
| Energy and protein balance (Gifford; Henry and Godden) | calories and protein of production, exports as food, scaled to a land base | the diet, the pasture and crop pairing, waste | 134 to 211 | recipe reproduces 109 and 96 from their totals |
| Ecological footprint, food row (Simpson) | crop and pasture land at world-average productivity | productivity of the actual land, pairing, energy land not set against Australian land | 146 to 343 on current yields; 103 at 1990 world yields (cropland-bound reading 103 to 160; crop and pasture together 268 to 343; three builds) | feed crop matched by two of three builds (3.6% high, 1.1% low) and not by the other (22% high); pasture matched by two of three builds (1.2% low, 2.3% low) and not by the other (36% high); plant-food crop not reproduced by any of three builds |
| HALF index (Alexander) | land at world-average production, by diet | productivity of the actual land, pairing | 276 | Australia within 0.8%, world within 2.1%, US and Argentina within 5%, India within 8%; New Zealand not reproduced |
| People per hectare (Cassidy) | cropland calories delivered after feed and biofuel, exports by importers' use | grazing, protein, a balanced diet | 5.8 to 6.0 people a hectare delivered; 145 to 147 million (about 183 on all cropland, harvests matched) | calorie shares within a few points for the world, India, China and Brazil; United States not reproduced; people a hectare 22 to 42% above the paper; two builds agree within 5 to 8% |
| Commodity balance (Foran and Poldy) | tonnes of grain, meat and fish against a requirement per person | land, weather, diet change | 40 to 41 (meat), 12 to 17 (fish), 127 to 128 (grain with feed grain) | production within 1.2%; their balance reproduced; the 30 and 77 readings are derived here |
| Failure probability (Fearnside) | the harvest in a year of given probability against the diet | one criterion; weather as one factor on all yields | 41.5 (average year), 30.8 (1 in 10), 18.9 (1 in 100) | none possible (Brazilian data); idea applied |
| The model, thesis method corrected | land, yields, diet, waste, fuel, fibre, reserve | trade, variability between years beyond the allowance | 41.5 (36.3 to 45.8) | the baseline entry |
| The model, improved | as above, with Australian settings | as above | 53.6 (46.2 to 60.1) | built on |

*Table note.* The footprint cell names the yield basis of each end; the csv cell gives 103 to 343 without it, and the 146 on current yields is build 3 on 2021-23 world yields (`harmonised_comparison.csv`). The people-per-hectare cell gives the all-cropland reading with harvests matched (`cassidy_matched.csv`); the csv cell gives about 190, on the same-year pairing. The people-per-hectare and commodity-balance fidelity cells say what was checked against the authors.

[Figure 2: each method's reading of Australia, as run and harmonised, beside the model's corrected and improved ranges, from `cross_method.csv` and `harmonised_comparison.csv` (no plotting script)]

### 5.11 The harmonised comparison

Every method was run on the common inputs of section 5.1 and kept its defining choices, such as world-average productivity for the footprint and HALF and cropland only for people per hectare. No method was given the model's diet, yields or land classes, and the failure view took no equalised input (Table 5).

Equalising inputs narrows the spread within the energy and protein balance (145.2 to 148.8 million) and within people per hectare (110.9 to 112.9 million; section S3.4). The footprint keeps its definitional spread, and HALF and the meat reading barely move.

The spread among the methods does not narrow: it is 12 to 343 million as run and 12 to 343 million harmonised. Both lows are the single-commodity fish reading, and both ranges leave out the footprint's readings on pasture alone. On a ratio scale, inputs account for about 10% of the distance of each reading from the corrected model and the methods for about 90%, on one set of rows with the methods weighted equally; on other row sets the inputs' share is 10 to 18%. The gap between the methods is the method.

Wackernagel and Rees 1996 describe an adjustment for local productivity: a hectare twice as productive as the world average counts as two (p. 78). With Australia's land expressed as the world-average hectares that would grow its output in 2021-23, the footprint reads 64.8 million (build 1) and 84.6 million (build 3) with crop and pasture together, and HALF 76.0 million, against the model's 41.5 and 53.6 million. What remains above the model is consistent with the pairing of pasture-fed food with crops, which neither method carries; the pairing was not removed from the model to test it.

Table 5. The harmonised comparison: each method on the common inputs, with its defining choices kept (million people unless stated). Built from `analysis/method_tests_2025/harmonised_comparison.csv`, summarised by method as `make_readme_tables.py` summarises it; two cells differ from the csv, as the table note says.

| Method | (a) As the authors would run it | (b) Harmonised | (c) Input factor, b over a | (d) b over the corrected model | (e) Local-productivity adjustment (p. 78) |
|---|---|---|---|---|---|
| Energy and protein balance (Gifford; Henry and Godden) | 134 to 211 | 145.2 (energy), 148.8 (protein) | 0.69 to 1.11 | 3.50 to 3.59 | |
| Ecological footprint, food row (Simpson) | 103 to 343 (cropland-bound 103 to 160; together 268 to 343) | 139 to 343 (cropland-bound 139 to 160; together 278 to 343) | 1.00 to 1.42 | 3.36 to 8.27 | 64.8 to 117 (cropland-bound 113 to 117; together 64.8 to 84.6; pasture alone 53.9 to 77.9); builds 1 and 3 |
| HALF index (Alexander) | 276 | 275.8 | 1.00 | 6.65 | 76.0 |
| People per hectare (Cassidy) | 145 to 183 | 111 to 113 | 0.62 to 0.77 | 2.67 to 2.72 | |
| Commodity balance (Foran and Poldy) | meat 40, fish 17, grain 128 | meat 41, fish 12, grain 127 | 0.71 to 1.03 | 0.29 to 3.06 | |
| Failure probability (Fearnside) | 41.5 (average year), 30.8 (1 in 10), 18.9 (1 in 100) | blank: the readings are the model's own runs | | | |
| The model, thesis method corrected | 41.5 | 41.5 | 1.00 | 1.00 | |
| The model, improved | 53.6 | 53.6 | 1.00 | 1.29 | |

*Table note.* The people-per-hectare row uses the all-cropland reading with harvests matched, 183 million, and its factor of 0.62 to 112.9 (`cassidy_matched.csv`); the csv rows hold 190 and 0.594 on the same-year pairing.

### 5.12 Gap attribution

Each residual against a published figure was attributed by changing one candidate cause at a time; no output was adjusted to meet a published figure. For HALF, the world, United States and Argentina residuals are of the size and sign of the revisions to FAOSTAT since the authors' download. Australia's residual of 0.8% is partly explained by the supplement's cropland adjustment (42%) and is not closed by any cause tested. Simpson's pasture residual of 2.3% would be closed by a dairy share of about 57% of milk, but the paper prints no share. Table S1 gives the shares for every method, figure by figure (section S3.7).


# Paper B, sections 6 to 9 (first draft, D04; cut to the main-text limit, B98b)

## 6. What moves the number

This section measured, with the author's model on the same 2025 data, how far each design choice moved the answer, set at the ends the methods of section 4 take, with every other setting at the model's defaults. A factor here is the higher capacity over the lower one, not a ratio of people to capacity (Table 6; Figure 3). The comparison shows where each choice matters, not that the model's settings are right.

### 6.1 Exports counted or not

The proportional count of CSIRO and the University of Queensland (section 4.4) gave 27 million people fed at home and 63 million abroad, "around 100 million people in total" (CSIRO and UQ 2025, p. 30). An energy count of exports at 2,100 kcal a person a day, built here from the FAO food balance, fed 87 to 128 million from wheat and rice alone and 184 to 264 million from all foods. Against the model's 41.5 million in an average year, the proportional count moved the answer by a factor of 2.41 and the energy count by a factor of 4.4 to 6.4. The fruit, vegetables and dairy that bind the model's diet are exported far less than wheat and beef: 11 to 26% of production against 67 to 78%.

### 6.2 Grazing and pasture-fed food

Pasture is most of the land behind an Australian diet. Simpson, Petroeschevsky and Lowe (2000) counted 2.61 ha of pasture in a whole footprint of 5.96 ha a person in 1991-92 (p. 14): 44% of the whole footprint, not of the food row alone. Lenzen and Murray (2001), counting the land Australia actually uses, found their modified footprint mostly pasture: 8.1 of 13.6 ha a person in 1994-95 (p. 238). Alexander et al. (2016) attributed the high land-per-diet values of New Zealand, Argentina and Australia together to animal products, particularly beef, with no split for Australia alone (p. 91). In the model, crops and pasture-fed food are paired in a fixed diet, so whichever land runs short sets the capacity; on the improved release the default diet used 5.93 ha of pasture and 0.3 ha of cropland a person. Its Australian settings, beef output by state, dairy on land that can carry it and an organic factor for grazing ruminants in the long term, together with the waste and land-base settings, moved the short-term answer from 41.5 million on the corrected method to 53.6 million on the improved method, a factor of 1.29.

### 6.3 How waste is treated

Energy and protein balances and people per hectare count production as eaten (Henry and Godden 1995; Cassidy et al. 2013), and land-per-diet methods carry waste inside the diet. The thesis model applied loss factors from the United States (section 8.5); the improved model used Australian loss factors and limited its recycling credit to waste fit for feed. Taking avoidable waste from 12% to none moved the corrected method from 41.5 to 55.3 million, a factor of 1.33. On the improved method the same change moved it from 53.6 to 62.9 million, a factor of 1.17.

The model's 6% setting halves its retail-and-consumer loss share, mirroring UN Target 12.3 as Spang et al. (2019, p. 118) state it. Australia's own goal is whole-chain halving by 2030 (National Food Waste Strategy 2017, pp. 3, 8). The 2016-17 National Food Waste Baseline put Australia's food waste at 7.3 Mt (National Food Waste Baseline 2019, p. 3). The estimate of about 7.6 Mt a year is the 2021 Feasibility Study's, as the department reports it (DCCEEW, "Reducing Australia's food waste", web page).

### 6.4 Which land counts

Henry and Godden (1995) rested their answer on Nix's estimate of 70 Mha of land available for intensive production (p. 98), and report that Gifford et al. (1975) scaled intensive land from 40.5 to 70 Mha, a factor of 1.73 (p. 99). Peters, Wilkins and Fick (2007) divided New York State's 2.03 Mha into three classes of land (p. 148). The model takes the land as it is and sets aside a reserve. Doubling cropland out of non-agricultural land, the 1975 case, moved the model's answer from 41.5 to 45.1 million, a factor of 1.09. On the improved method the same case gave 58.3 million, a gain of 9% on both, which the model reads as the short-term diet being bound by pasture-fed meat and dairy, not by cropland.

### 6.5 Diet

Across the guideline diets from 15% to 5% meat and eggs, the improved release fed 48.3 to 103.3 million, a factor of 2.14. Against the default diet's 53.6 million, the nutrition-optimised diet with free choice and ten micronutrients fed 422.3 million, a factor of 7.88. Capacity was not monotone in the meat share on the improved release: there was a dip at 2.5% meat and eggs, and a cliff between 5% (103.3 million) and 7.5% (66.9 million). A little pasture-fed meat beat none on the corrected release only. The 103.3 million for 5% meat and eggs is the guideline diet on the improved release, set by the direct route; the same share applied alone as a measure to the corrected release gives 76.8 million. Willett et al. (2019) found that diet change alone moved global cropland use by 0 to 2% (p. 472). Table S2 gives every diet with its land.

### 6.6 The drought allowance

Most methods count an average year; in the model the drought allowance is a quantity. With an allowance for the worst year in 50, the corrected and improved releases fed 23 to 30 million; for the worst year in 100 they fed 19 to 25 million. From the average year to the worst year in 100, the corrected method moved from 41.5 to 18.9 million, a factor of 2.19. The Jones committee's figures (1994) are not quoted: the report was not available, and the summaries of it that were held disagree.

### 6.7 The unit of self-sufficiency

Three points from the model show the effect of the unit, on the corrected method, 2025 data, short term and the state yield basis. The nation fed 41.5 million. The states summed to 75% of that, and the SA2s to 37%. That 37% is 15.5 million: the sum over SA2s of their capacities. Nation against the SA2 sum is a factor of 2.67. The SA2 point sits on 2020-21 land and the others on the release land, which give the same national capacity. On the local yield basis, where each unit takes the yields of its own zone, the SA2 sum is 54%. The full curve is in the companion results paper.

### 6.8 The time frame

The thesis model set a short-term and a long-term setting side by side (Lane 2017). The long-term setting bundles a low-meat diet, organic yields, no avoidable waste, a 100-year drought allowance and a 30% reserve. On the corrected method it fed 15.6 million, against 41.5 million in the short term, a factor of 2.66.

### 6.9 How sure the answer is, as a method

A Monte Carlo of 1,000 draws over 13 uncertain choices (section S5) gives each release a 5th to 95th percentile range (Table 4). On the corrected method Australia's short-term capacity ran from 36.3 to 45.8 million, a factor of 1.26. These ranges are a spread across the settings the author judges defensible, not confidence intervals. One judged choice, the window of herd and meat data, explained 81% of the short-term variance (Table S3). Five range ends, among them the three-way meat-window choice, are the author's judgement and have no outside source (section S5).

### 6.10 The spread across settings against the definitions

By definition alone, one model on one data set spans 18.9 million (the worst year in 100) to 55.3 million (no avoidable waste) on the corrected method. With the improved settings the top reaches 62.9 million. The spread across defensible settings, a factor of 1.26, is small beside these definitions. Figure 3 sets the published estimates, which run from 9.4 million to 100 million, a factor of 10.6 (section 1), on a ladder of ten steps that multiply to the whole: 1.66 from 9.4 to 15.6 million, 4.03 from 15.6 to 62.9 and 1.59 from 62.9 to 100. The product holds for any steps chosen, so the ladder is a reading of the spread, not a decomposition. Its first step mixes a change of data, from 2011 to 2025, with the correction of the method; its low steps are on the corrected method and its high steps on the improved.

[Figure 3: the factor by which each design choice moved the answer, with the ladder of definitions; its steps from 9.4 to 100 million multiply to the 10.6, and its top step, the energy count of exports (223.9 million), lies beyond the published span; from `analysis/method_tests_2025/design_choices.csv` and `analysis/method_tests_2025/ladder.csv`]

### 6.11 The ordering of the design choices

In Table 6, land mattered least (1.09) and exports counted by energy (4.4 to 6.4) and the optimised diet (7.88) most. All but the land base, and waste on the improved method, moved the answer more than the spread across defensible settings.

**Table 6.** The design choices and the factor by which each moved the answer, in order of the factor. Built from `analysis/method_tests_2025/design_choices.csv` (script `design_choices.py`); the Monte Carlo row is shown last for comparison.

| Design choice | What is compared | Low (million) | High (million) | Factor | Method and release |
|---|---|---|---|---|---|
| Land available | cropland as it is against doubled out of non-agricultural land | 41.5 | 45.1 | 1.09 | corrected |
| Avoidable waste | 12% against none | 53.6 | 62.9 | 1.17 | improved |
| Australian settings | thesis method corrected against improved | 41.5 | 53.6 | 1.29 | short term |
| Avoidable waste | 12% (default) against none | 41.5 | 55.3 | 1.33 | corrected |
| Diet | guideline diets from 15% to 5% meat and eggs | 48.3 | 103.3 | 2.14 | improved |
| Drought allowance | average year; worst year of 5, 10, 20, 50, 100 | 18.9 | 41.5 | 2.19 | corrected |
| Exports counted | the model against the CSIRO and UQ proportional count (27 at home + 63 abroad) | 41.5 | 100.0 | 2.41 | published count |
| Time frame | long-term settings against short-term settings | 15.6 | 41.5 | 2.66 | corrected |
| Unit of self-sufficiency | nation against the sum over SA2s (state yield basis) | 15.5 | 41.5 | 2.67 | corrected |
| Exports counted (energy) | exports alone as an energy count, all foods, at FAO's own food energy per kg | 41.5 | 183.9 | 4.43 | energy count |
| Exports counted (energy) | exports alone as an energy count, all foods, at typed as-traded densities | 41.5 | 263.9 | 6.36 | energy count |
| Diet (optimised) | default diet against nutrition-optimised diet C (ten micronutrients) | 53.6 | 422.3 | 7.88 | improved |
| Uncertainty (Monte Carlo) | 5th to 95th percentile over 13 uncertain choices | 36.3 | 45.8 | 1.26 | corrected |

## 7. Which method for which purpose

### 7.1 The rating key and the methods

Table 7 rates seven methods against four purposes as well suited, partly suited or not suited, with the purposes in order of how strongly the tests support them. The planning-oriented studies of the earlier work (Peters, Wilkins and Fick 2007; Fairlie 2007; Gutteridge 2005; Noosa and Douglas Shire) were treated as the balance family at other scales. The ratings are the author's judgement, re-derived blind by a second reader, and are labelled as judgement.

**Table 7.** Which method for which purpose: the author's ratings. Typed from `papers/B_methods/SECTION7_DRAFT.md` (no csv exists).

| Purpose | Energy and protein balance | Footprint | HALF | People per hectare | Commodity balance | Failure probability | Land-and-diet balance |
|---|---|---|---|---|---|---|---|
| 1. Food security and drought risk | not suited | not suited | not suited | not suited | partly | well suited | well suited |
| 2. Why national estimates range from 9 to 100 million | partly | partly | partly | partly | partly | partly | well suited |
| 3. Regional and local land-use planning | not suited | partly | not suited | not suited | not suited | partly | well suited |
| 4. Diet change and land use | not suited | partly | well suited | partly | not suited | not suited | well suited |

### 7.2 Food security and drought risk

The balance and its failure view, one model read two ways, were rated well suited: the balance supplies the level, with a stated diet and the pasture-crop pairing, and the failure view reads it against the weather record (section 5.8). The commodity balance, which names the item that runs out first but carries no weather and no land, was rated partly suited. The aggregate methods, which count an average year at a single productivity, were rated not suited. A 2023 parliamentary inquiry recommended a National Food Plan (House of Representatives Standing Committee on Agriculture 2023).

### 7.3 Why national estimates range from 9 to 100 million

Only the balance was rated well suited to explaining the range, because one model run under each definition spans most of it (section 6.10). Each other method was rated partly suited, because each shows what one family of published estimates counts. The energy balance is the method of Henry and Godden (1995) and Gifford et al. (1975), and the commodity balance gives the 30 to 32 million meat count derived from Foran and Poldy's table. HALF, not predictive in its authors' words (Alexander et al. 2016, p. 89), and people per hectare, which counts cropland only, read high as capacities (section 5.10), which is part of explaining the range.

### 7.4 Regional and local land-use planning

Only the balance carries a unit of land, a diet and the pasture-crop pairing, and the unit decides the answer (section 6.7). The footprint was rated partly suited, because its own local-productivity adjustment sets a diet's demand against a given area (section 5.11). The failure view was rated partly suited: Fearnside's own application covered a 23,600 ha study area, and he states that his simulation needs too much data for large areas (Fearnside 1990, p. 195). The other methods, national or global in construction, were rated not suited.

### 7.5 Diet change and land use

HALF, reproduced closely on 2011 data (section 5.5), was rated well suited for comparisons across countries; it measures a diet's land at world-average production, on which Australia's value in 2021-23 was 2.4 times the world average. The balance was rated well suited for what Australia's land can feed, with the dip and the cliff of section 6.5; a little meat beats none on the corrected release only. The footprint and people per hectare were rated partly suited, and the other methods not suited.

### 7.6 The short reading

No single method serves all four purposes. Read as capacities, the aggregate methods give 134 to 343 million (the footprint 146 to 343 on current yields, 103 at 1990 yields), about three to eight times the balance. This is consistent with none of them carrying the pairing of pasture-fed food with crops that binds the model in Australia, an interpretation not tested (section 5.11). For a security claim, report a level and a failure probability from the balance run through the failure view, and add a commodity balance for the item that fails first.

### 7.7 A minimum reporting checklist

Table S4 gives a minimum reporting checklist of twelve items (section S6). Items 2 to 8 are the design choices measured in section 6, and items 1 and 9 to 12 what a reader needs to use the number. The land base stays on the list, although it moved the answer least, because readers argue most about it.

### 7.8 Cautions

A figure of people fed is not a forecast or a target. The ratings, the author's judgement on seven methods tested on Australian data, may differ where grazing is a small share of food land. The failure view here is the model's own runs read through Fearnside's frame, not Fearnside's own simulation.

## 8. Limitations and what no method yet does

This section states, in the same terms for every method, what no method reviewed can do and what the author's own method lacks.

### 8.1 Variability

Every method reviewed but the failure view works in an average year. Production shocks have become more frequent, and national totals smooth sudden losses in a large country such as Australia (Cottrell et al. 2019, pp. 130, 135). Bad wheat years across the southern states are partly correlated (Anderson et al. 2019), and Australian wheat yield potential since 1990 has fallen in simulation while actual yields held flat (Hochman et al. 2017, p. 2071). The failure view here carries one criterion, the default diet, where Fearnside tested four (section 4.10). It treats the weather as one factor on every yield and reads the failure probability from six run points, interpolated. No method reviewed gives the probability of a failure in the herd cycle.

### 8.2 Trade

Most methods treat the region as closed or count exports at full value; in the footprint and HALF trade drops out. Reserves and trade set a country's exposure to supply shocks (Marchand et al. 2016), and self-sufficiency is better read as a continuum than as a yes or no (Clapp 2017). Production within 100 km can meet the demand for a given crop for only 11 to 28% of the world's people (Kinnunen et al. 2020, p. 229), a range across crops, not an uncertainty. About 16% of the world's people meet their needs with food traded between countries (Fader et al. 2013, as reported in Clapp 2017, p. 91). The model is self-sufficient by design; trade is a way around its constraint, not part of it.

### 8.3 Energy

Simpson, Petroeschevsky and Lowe (2000) counted 0.43 ha of energy land in the food row, about a sixth (16%) of that row (p. 14); the model counts none. Energy after the farm gate is documented (Ladha-Sabur et al. 2019), but no Australian figure for the energy used in farming was found. The model's farm diesel share is its own statement, with the National Farmers' Federation figure as Soliman Hunter and Taylor (2021) quote it; its bioenergy yields are from Geoscience Australia and ABARE (2010).

### 8.4 Diet dynamics

Each method fixes one diet, but diets move with the nutrition transition (Bodirsky et al. 2020) and with income (Tilman and Clark 2014), and capacity is tied to a period and a dietary standard (Gilland 2006). Erb et al. (2016; not seen; cited from its abstract) report the option space under several diets, as section 6.5 does.

### 8.5 Borrowed constants and data limits

The thesis model borrowed constants from the United States: loss factors (Buzby 2010; Muth 2011; both as reported in Lane 2014, pp. 201 to 202) and a carcase-to-retail factor for beef (USDA Handbook 697, as reported in the archive's errata). Its nutrient values came from AUSNUT 2007, as reported in Lane 2014 (p. 202). These constants are declared as assumptions, and their corrections are listed in the errata. An audit found red meat the heaviest group of constants, because red meat is most of the land in the default diet, and many constants carry no recorded source. The model cannot carry soil, fertiliser, labour, a water ceiling on irrigation, or climate effects on pasture and livestock.

### 8.6 Implementations resting on description alone

Simpson's 0.312 ha of crop land for plant foods (the rebuild gave 0.107 ha) and 0.854 ha of pasture for clothing were not reproduced (Simpson, Petroeschevsky and Lowe 2000, p. 14), and the footprint test omitted pulses from 1991-92 consumption and did not rebuild energy land. HALF for New Zealand was not reproduced, for a cause unknown (section 5.5). The people-per-hectare test typed crop energy, feed shares and livestock values as assumptions, and the energy and protein test was rebuilt on FAO food balance data, not the model's production layer.

### 8.7 Where another method does better

HALF does better than the balance for comparisons across countries, and a failure probability better than a single level for risk. The guide of section 7 holds only within these limits.

## 9. Conclusions, data and code availability

### 9.1 The answer

Published estimates differ because they answer different questions by different methods. One model on one data set spans 18.9 to 55.3 million by definition alone on the corrected method, and reaches 62.9 million with the improved settings; counting exports takes the published figures to 100 million. Across the settings the author judges defensible, the answer moves by a factor of 1.26, small beside the definitions. Each figure keeps its basis: the method tier, 2025 data and yields, and a range that is a spread across judged settings.

### 9.2 Equalised inputs

With inputs equalised, the gap between methods is the method. Equalising narrowed the spread within the energy balance and people per hectare, the footprint kept its definitional spread, and the spread among methods did not narrow (section 5.11). Inputs accounted for 10% of the distance between the methods and the corrected model, a share that runs from 10 to 18% with the set of rows chosen.

### 9.3 What to do

Choose the method by purpose, as section 7 sets out. Report the twelve items of the checklist (Table S4) with every capacity figure. Distrust a capacity figure given without its definition.

### 9.4 Data and code availability

The model, its frozen releases, the data pipeline, the scripts that built every table and figure, and the claims and sources registers are in the repository github.com/MurrayLane/carrying-capacity-dashboard. The releases used are 2025-mirror, 2025-fixed and 2025-improved, identified by hash in `results/releases.json`, and each table names the file it was built from. Code is under the MIT licence; the model workbook, default inputs, 2011 baseline and analysis outputs are under CC BY 4.0, and source data keep their publishers' licences (`LICENSE-DATA.md`). The archive has no DOI. Its deposit on Zenodo is on hold at the author's decision.

### 9.5 Competing interests

The model tested here is the author's own. It was tested by the same procedures as every other method.

---


---

## Appendix: drafter notes (not for the paper)

### From B_s01-03.md
## Drafter notes (not for the paper)

**What could not be sourced and was left out.**
1. The Jones committee figures (30 to 35 million; 50 plus million; L006, B196, B197). The scope asks for the 30 to 35 to be quoted "as summarised in the thesis", but V31b (defect X120) found the thesis gives a different summary (ecologists 20 to 25 million; economists and demographers 50 and 60) and no 30 to 35. The report is not on disk (decision 89). So the figure has no source this draft can quote, and the four-figure opening became three figures (100, 61, 9 to 14) plus PMSEIC's 60. The Jones row is also left out of Table 1. Restore it after the page read of paragraphs 2.13 to 2.16.
2. Cohen 2017 (L106), Tucker 2020 (L107) and the Productivity Commission 2011 (L099): not reached at page level, or no file (B85). The scope says cite only if read or fetched, so they are left out.
3. Section 3 point 3: no csv holds the selection record (scope gap 1), so the counts by route (found, read, cited, excluded) are not given and the optional table is not placed. The routes are named without counts. Point 3 and the reading-label paragraph will need the counts once the record exists.
4. Section 2 has no claims rows (scope gap 3), so no figure from a concept source is quoted. Cohen's range of world estimates and Herrington's closest-fit counts (CT 7, BAU2 6) are given in words only.
5. Rows of `harmonisation.csv` with no claims row or a weak route were left out of Table 1: Griffith Taylor, Borrie, the National Population Council and the NFF (B163, unverified; scope section 6 drops it). Also left out: the footprint ratios (section 4 and 6 material) and Peters et al. 2016 (United States). The Migration Committee's 10 to 480 million is in the prose only, because neither Table 1 csv holds it.
6. Van den Bergh and Rietveld 2004 (scope gap 2): not acquired and not in the register.
7. The Simpson footprint and the HALF index are described but not named by author in section 1, because their register rows were not in the section 1 source table.
8. Figures: none are planned for sections 1 to 3, and none were placed.

**Conflicts named, not resolved.**
1. The brief says the section 3 selection rule is "decision 57". Decision 57 is the section 4 renaming of the diet-optimisation family. The selection rule is decision 42, which the scope cites. This draft follows decision 42.
2. As above: scope section 1 point 1 (Jones "as summarised in the thesis") conflicts with V31b and X120 (the thesis has no 30 to 35).
3. B162: its value is 100, while its notes, the `harmonisation.csv` cell and the report's own sentence give 27 + 63 = 90 "around 100". Q9 option (a) was taken (see the flags in the claims csv).
4. B229's sources are L012 to L014, which have no file (B85: "not reached: no file"). The draft cites the thesis (L020, p. 280, Table 16) for 40, 9 to 40 and 23. That page was opened, and it prints the long-term 9,431,487, "over 40 million" short term, and "about 23 million" aggregated. The 9.4 short form follows B160 and the `published_values.csv` ladder cell.
5. L009 (Bellotti) is labelled "read; unverified" in the literature register, while B161 is "independently verified with notes" against the corrected file. The draft cites it as read.
6. OUTLINE.md still tags B1-2.a "decision 52" (Q2, housekeeping). The draft does not quote the tag.
7. Headings: the scope's labels B1-2.a and B1-2.b do not take the form "n.m", so sections 1 and 2 have no subheadings. B3.1 is used as "### 3.1".
8. Outline "Decisions still open" item 4 (authors and order) is open, with no recommended option. The disclosure is worded with "the author" as the scope words it. The competing-interests statement is not drafted here.
9. The brief and scope say Section 1 "opens with" the span with "both soft ends stated". The 15.6 corrected long-term figure (B091, 2025-fixed) was added in the opening to make the low end's softness concrete. It is a register row, Tier A, independently verified.

10. Three year bounds in the prose rest on decision rows, not on a claims row or csv cell: "from 2011" and "before 2011" (decision 42) and "since 2016" (decision 43). The claims csv names the decision row for each.
11. Page numbers were taken from the files on disk, not copied from the register: L010 p. 30; L136 pp. 1 and 15; L020 p. 280 (Table 16); L003 pp. 97, 98 and 100 (scan read as images; Table 5 is on p. 100, not p. 98); L143 p. 21; L007 p. 64; L146 p. 123; L049 p. 343; L044 pp. 601 and 603; L045 p. 405; L046 pp. 124, 126 and 131; L048 pp. 9 to 10 and 17; L142 p. 2; L240 p. 472; L223 p. 94; L201 p. 2 of 6; L202 p. 414; L203 p. 337; L200 p. 1583. Rees 1992 (L139) has no text layer, so it is cited without a page.

**Register rows touched:** none.

**B98b cut (decision 92).** The main text was cut to under 8,000 words of prose with detail moved to `supplementary.md` (sections S1 to S6, Tables S1 to S4); its claims are in `supplementary_claims.csv`. Table numbers in the notes above are those of the first draft: old Tables 7, 8 and 10 are Tables S2, S3 and S4, and old Table 9 is Table 7. Sentence numbers in the claims csvs were renumbered on the cut text. The record of what moved, merged or was cut is `qa/reports/B98b_cut_paper_B.md`.


### From B_s04-05.md
## Drafter notes (not for the paper)

Job D03, sections 4 and 5. Claims are in `papers/B_methods/draft/B_s04-05_claims.csv`. Page numbers were read from the files on disk under `/home/user/carrying-capacity-models/`, not copied from the register.

**Could not source, so left out or left as a placeholder.**
1. Table 2 and Figure 1 (the catalogue): no catalogue csv or script exists (scope section 4, gap 4). Placeholders only; no table was hand-typed.
2. Figure 2: no plotting script over `cross_method.csv` and `harmonised_comparison.csv` (scope section 5, gap 4). Placeholder only.
3. Supplementary Table S1 (fidelity checks and gap attribution): no script assembles it. The prose points to it and names `gap_attribution.csv`.
4. The Jones committee's "30 to 35 million" set beside the 1-in-10 point (L006, B138): L006 has no file on disk, and the thesis (L020, printed p. 98) summarises the inquiry as 20 to 25 million against 50 to 60 million, not 30 to 35. Left out until the report is read (decision 89).
5. Section 4 families with no claim row (foodshed, footprint critique and defence, integrated, optimisation, water-bounded; scope section 4, gap 5): described from the literature register's `what_taken` only, and kept free of numbers. Figures I could not page-check on disk were dropped: the 42 diets of Peters, Wilkins and Fick 2007, the scenario counts of Hatfield-Dodds et al. 2015, Bryan et al. 2016 and Gao and Bryan 2017, and the four boundaries of Gerten et al. 2020 (no file).
6. No method paper for the stocks-and-flows framework (scope section 4, gap 2): the prose says the framework is described from Foran and Poldy 2002 alone.
7. Left out for the word budget or the cross-paper rules: Fearnside's protein and cash standards (B122); the wool and plant-crop test readings (README); the energy land of 0.43 ha (B047); the grain-direct reading of 486 million (B152); Foran and Poldy's population paths (Table 1.1, p. 31); HALF's fall from 2011 to 2021-23 (B067) and the 2011 failure probability (B131), both 2011-to-2025 material for Paper A (X-11); the thesis's 9.4 million (B160), which is 2011 data (X-10, X-11); the unverified author figures B009, B011 and B031.

**Conflicts between scope, README, csv and register (named, not resolved).**
1. Heading numbers. The brief says to number headings as the scope numbers them. The scope's content list puts "B4.8 Integrated" at point 7, "B4.7 Optimisation" at point 8 and "B4.9 Water-bounded" at point 10. Resolved in B96b: the blocks were reordered whole, so B4.7 Optimisation, B4.8 Integrated and B4.9 Water-bounded fall on headings 4.7, 4.8 and 4.9, and failure probability is 4.10; the one in-text reference (Limits to Growth, section 4.8) was updated.
2. Cassidy all-cropland reading. B084 and B273 carry gate 4 values: 183 million and a factor of 0.618, harvest-matched. `cross_method.csv` and `harmonised_comparison.csv` still hold 190 and 0.594, from the same-year pairing. Tables 3 and 5 print the gate 4 values, and each table note says so.
3. B276 (Tier A, not marked pending) gives input factors of 0.59 to 1.42 and the 10% and 90% split. Both were computed with the Cassidy factor of 0.594. With the matched 0.618, the lowest input factor would be 0.62. The prose quotes B276's 10%, 90% and 10 to 18% as registered, and leaves out the 0.59 to 1.42 range.
4. Statements pending gate 4 that the README has not caught up with:
   * B083: 22 crop items, not 21. The README application table and its text still say 21. B079 and the scope also say 22.
   * B156: the B94 wording, with "the model's range" dropped. The README's "What the comparison shows" still reads "about two to eight times" and keeps the containment sentences.
   * B277: 12 to 343 as run. The README still says 17 to 343.
   The draft follows the register's pending values in each case.
5. Footprint row of Table 3. The scope asks for the yield basis of each end (B94), but the `cross_method.csv` cell reads "103 to 343" without it. The table adds the 146 on current yields from B046 and B268, and the table note says so.
6. Cassidy fidelity cell in `cross_method.csv`. It describes the agreement between the two builds, not a check against the authors. B96b rewords the Table 3 cell (V34b S6); the csv cell needs the same edit.
7. Simpson gap attribution. The README's "Wording for the papers" says that the readings of year, population and dairy share "each move the result by more than the 2.3% residual". But `gap_attribution.csv` gives the population readings as 30% and 56% of the residual. The prose states the shares (B297 to B300) and drops the README sentence.
8. B141 notes that the meat residual is 1.22%, marginally outside "within 1.2%". The prose uses B326's "1.2% each way".
9. L050 (Wackernagel and Rees 1996) is unverified in the register, and its `what_taken` leads with the withdrawn 2.8 factor (scope section 5, gap 2). It is cited for p. 78 only, read from the filed page image. The prose says "the adjustment the book describes", not "sanctioned".
10. B012 and B013 (Henry and Godden's totals, 70 and 45.7 Mha) are unverified in the register. This drafter read them on the scan at p. 99; their status is unchanged.
11. Cassidy page locators. The register and README call the results table "Table 1". In the file on disk, Table 1 (p. 3) is the conversion efficiencies, and Table 2 (p. 3) holds the crop allocations and people per hectare. The prose cites them by the file.

**Open questions taken.** None. Section 4's Q3 is settled by decision 57, and section 5's Q4 by decision 58. No `[open: Qn]` flag is used.

**Register rows touched: none.**

**B98b cut (decision 92).** The main text was cut to under 8,000 words of prose with detail moved to `supplementary.md` (sections S1 to S6, Tables S1 to S4); its claims are in `supplementary_claims.csv`. Table numbers in the notes above are those of the first draft: old Tables 7, 8 and 10 are Tables S2, S3 and S4, and old Table 9 is Table 7. Sentence numbers in the claims csvs were renumbered on the cut text. The record of what moved, merged or was cut is `qa/reports/B98b_cut_paper_B.md`.


### From B_s06-09.md
## Drafter notes (not for the paper)

**What could not be sourced and was left out.**
* NFF "feeds 75 million" (B163, L011): untraced; dropped rather than cited through L229 (scope gap 7, decided at drafting).
* Jones committee figures (B196, B197, B198, B138): L006 not on disk, and V31b found the thesis summary differs (ecologists 20 to 25 million; economists and demographers 50 and 60) with no 30 to 35. Decision 89 says quote "as summarised in the thesis", but the thesis summary does not hold the figures the scope sets beside the model. No Jones figure is quoted; sections 6.6 and 7.2 say why in one sentence each.
* Reutter et al. 2017 "about 3.4 times": the PDF has no text layer and the factor is derived, not printed; cited without the number.
* Farm diesel share 84% (decision 53): no claims-register row; stated without the number.
* Kastner et al. 2012, Poore and Nemecek 2018, Roos et al. 2017, van Zanten et al. 2016, Ridoutt et al. 2020, Tilman and Clark 2014 (section 6 rows), Peters et al. 2016 diet land range (B202), Cohen 2017, Khorsandi et al. 2023, Bentham et al. 2020 (gap 1: accepted manuscript unchecked), Kastner Oceania variability, Fearnside 1990 in section 6: left out to keep to the word budgets or because no page-checked figure was needed. Bentham is the only one left out for a sourcing reason.
* The loss-factor data sources (D40) have no literature row (section 6 gap 3); the Australian loss factors are named as a model setting only.
* The three-point scale table has no script (gap 4); the three points are given in prose (section 6.7), not as a table. Figure 3 has no plotting script.
* Competing interests: only the disclosure the scope names is written; any further declaration is the author's.

**Conflicts named, not resolved.**
* Fearnside 1990: the 23,600 ha and the KPROG2 sentence are printed on p. 195 of the filed copy (file page 4; printed numbers 192 to 196 on file pages 1 to 5); B244's note and the register cite p. 194. The draft cites p. 195.
* Fearnside 1985: the separate failure criteria (calories, total protein, animal protein, cash) are stated on p. 345 of the filed copy; B244's note cites pp. 352 to 354. The draft cites p. 345.
* B215 gives Optimised C land as 0.09 ha cropland and 0.0 pasture; `diet_land.csv` gives 0.06, 0.13 and 0.19. Table 7 follows the csv. B213 gives Optimised A total 3.8; the csv gives 3.74.
* B216 is self-checked only; its note carries superseded values (96.7, 88.0).
* Gap 6: no register row holds the full ordering of Table 6 and section 6.11; it is built from B194 and the per-choice rows.
* B251 unit: register now reads "share of meat" (B95), matching A341; B252 carries the improved-release note. No conflict left in text.
* Scope section 7 point 5 cites the improved-release cliff "after 5.5%" in the old draft; the draft uses B216's corrected wording (between 5% and 7.5%).
* B166 says "41 to 54 million" for the model's average year; the draft uses 41.5 (design_choices.csv) and does not repeat the range.
* Section 7.3 "145 to 183 million": 145 to 147 is B083 (its statement pending gate 4 for 22 crop items, value unchanged); 183 is B084's gate 4 value replacing 190.
* Outline "Decisions still open" item 2 (improvements as settings in section 6) is open with Murray; the draft follows the scope's proposal.
* The repository URL in 9.4 is the one in `CITATION.cff`; whether the paper should name it before the archive is released is for Murray.

**Numbers that rest on a literature register row, not a claims row.** The waste tonnages and goal (L230, L231, L242; decision 72), Nix's 70 Mha and Gifford's 40.5 Mha (L003 pp. 98 to 99, with B232), New York State's 2.03 Mha (L040 p. 148), Willett's 0 to 2% (L081 p. 472) and Kinnunen's 11 to 28% within 100 km (L180 p. 229). Each page was opened on disk for this draft. None has a claims-register row; a register job may want rows for them.

**Not listed in the claims csv.** Section, table and figure numbers, citation years and page numbers (pages are in the page column of the row they support). "SA2" is a unit name.

**Flags.** "[gate 4]": B084 (183, B93) in 7.3 and B277 (12 to 343 as run, B92b statement) in 9.2. B083 and B156 carry gate 4 notes on wording only; the draft does not use the words that change. "[open: Q8]": the span is quoted as B003 (18.9 to 55.3 million by definition alone, corrected) with 62.9 for the improved settings, in 6.10 and 9.1; "a factor of 4" is not used, and 4.03 appears only as a ladder step. "[open: Q9]": 100 million kept, with the parts' sum of 90 stated at first use (6.1).

**Register rows touched:** none.

**B98b cut (decision 92).** The main text was cut to under 8,000 words of prose with detail moved to `supplementary.md` (sections S1 to S6, Tables S1 to S4); its claims are in `supplementary_claims.csv`. Table numbers in the notes above are those of the first draft: old Tables 7, 8 and 10 are Tables S2, S3 and S4, and old Table 9 is Table 7. Sentence numbers in the claims csvs were renumbered on the cut text. The record of what moved, merged or was cut is `qa/reports/B98b_cut_paper_B.md`.
