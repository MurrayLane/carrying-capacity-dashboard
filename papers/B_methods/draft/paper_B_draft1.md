# Paper B, methods: well-known carrying-capacity methods tested on common Australian data

First draft, assembled 2026-11-18 from B_s01-03.md, B_s04-05.md, B_s06-09.md, B_s10_declarations.md. Every number traces to the claims csv beside each section file; sentences marked [gate 4] in those csvs use values awaiting Murray's gate 4 approval. Not for circulation.

# Paper B, sections 1 to 3 (first draft, D02; cut to the main-text limit, B98b)

## Abstract

Published estimates of how many people Australia can feed run from about 9 to 100 million. Five published methods and the author's own land-and-diet model, read two ways, were applied to Australian data for 2021 to 2023 (FAOSTAT 2025; the model on its own 2025 layer) and checked against their authors' figures where these could be reached; the implementations reproduce them in part. With the footprint and the HALF land-per-diet index at Australia's own productivity, the aggregate methods give about 65 to 211 million, about 1.6 to 5 times the model; in world-average hectares, 134 to 343 million, about three to eight times. Whether equalising inputs narrows the spread depends on where the line between input and method is drawn. With the productivity basis counted as part of the method, equalising closed 4.1% of the log distance to the model and did not narrow the spread of method centres; counted as an input, it closed 38.5% and narrowed that spread by about a third. With the model's pairing of pasture-fed food with crops relaxed and the diet's energy held, it reads 81.7 million against 41.5. Weather and waste take the model from 18.9 to 55.3 million; across the settings varied together it moves by a factor of 1.58 (5th to 95th percentile). This narrative critical review finds that no single method serves every purpose. Analysts should choose the method by purpose and report a capacity figure with its question, diet, waste, weather allowance, land base, unit and time frame.

## 1. Introduction

Published estimates of how many people Australia can feed run from about 9 to 100 million, although one figure in Table 1, Henry and Godden's energy count of 109 million (1995, p. 100), sits above that span. Both ends of that span are soft. The low end, 9.4 million, is the author's own long-term figure, from the thesis method as built on 2011 data before its errors were corrected (Lane 2014, p. 280). Run unchanged on 2025 data, the same method gives 14.1 million; this paper calls the 9 to 14 million figures the published method. The high end is the "around 100 million people in total" of a 2025 food system report: 27 million fed at home and 63 million abroad, extrapolated from the exported share of production (CSIRO and University of Queensland 2025, p. 30). The two parts sum to 90 million. The report itself calls this metric misleading as an indicator of food security (p. 30).

Because both ends are soft, the span shows that published figures differ by an order of magnitude; it is not a measured spread of independent estimates.

The spread is old. Henry and Godden (1995, p. 97) reported a range of 10 to 480 million from a 1986 committee (Migration Committee 1986), taken in turn from a 1990 review, so it is known here only third-hand. The Jones committee (House of Representatives Standing Committee for Long Term Strategies 1994) accepted that "in subsistence terms Australia has the arable land to produce food for 50 plus million people", but, "allowing a safety margin for the possibility of a run of bad seasons", put the population "carrying capacity" at 30 to 35 million "in terms of the food constraint" (para 2.16, p. 40). It called even serious estimates "little more than 'guesstimates'" (para 2.13, pp. 39 to 40) and proposed no target (para 8.10, p. 144). At world scale, Cohen (1995, pp. 341 to 343) showed that estimates of human carrying capacity depend on natural constraints and on human choices about diet, technology, environment and wellbeing.

The spread matters because capacity figures enter debate about population, food security and land. Australian population planning draws on the Intergenerational Reports (Treasury 2021; Treasury 2023) and the Population Statement (Centre for Population 2026), and Bolleter (2018, p. 123) drew on Lane (2017) to weigh settlement scenarios for northern Australia against the carrying capacity of the land.

The 2010 review of carrying capacity methods for land-use planning (Lane 2010) compared method designs against planning criteria and argued that a workable model could be built from their components. The author built that model (Lane 2014; Lane, Dawes and Grace 2014; Lane, Dawes and Grace 2015; Lane 2017). This paper returns to the 2010 question by a different route, running each well-known method on the same 2025 Australian data and comparing the outputs, with the author's own model among the methods tested, entered as published and as built on. The model is also the reference of the comparison and the instrument of section 6, which no other method is, and sections 7.1 and 9.5 say how that bears on the design.

Chapter 6 of the thesis reviewed Limits to Growth, the ecological footprint, the South East Queensland, Noosa and Douglas Shire studies, Peters for New York State, Fairlie for Britain and Fearnside for Brazil; the 2010 review covered the same methods except Douglas Shire and Peters. This paper adds the families neither covered (energy and protein balance, integrated resource flow, people per hectare, a land-per-diet index and a food-only footprint), the literature since 2011, including a water-bounded method for Iran that cites the thesis (Khorsandi et al. 2022), and a test of Fearnside's method.

The paper finds that how much of the spread the inputs account for depends on where the line between input and method is drawn: with the productivity basis counted as part of the method, equalising the inputs closes 4.1% of the distance between the methods and the model, and counted as an input, 38.5% (section 5.11). The question is how much of the spread is the definition, the diet or the method, and which method suits which purpose; section 6 measures each design choice in one model, and section 7 draws the implication for practice.

Table 1. Published estimates of how many people Australia can feed, with the definition behind each. Built from `analysis/comparators_2025/harmonisation.csv` (all rows except PMSEIC 2010 and the four marked "from the report") and `analysis/method_tests_2025/published_values.csv` (PMSEIC 2010, ladder row). "Read" means the figure was read in the source; "second-hand" means it was read in a source that reports it.

| Estimate | People (million) | Data year | Exports counted | Diet and waste | Drought allowance | Route to the figure |
|---|---|---|---|---|---|---|
| Taylor 1922 | 65 (1922); 20 (a later estimate, dated 1937 in the report) | not given | not given | the 1937 figure assumes a much higher standard of living than the 1922 one | not given | from the report, p. 8 |
| Gifford et al. 1975 | 82 (energy) or 60 (protein) | 1970s | no (all production eaten at home) | contemporary consumption, no waste allowance | none | second-hand (Henry and Godden 1995; Chisholm 2000) |
| National Population Inquiry 1975 (Borrie) | 50 to 60 | not given | not given | not given; "comfortably" | not given | from the report, p. 17 and p. 143 |
| National Population Council 1992 | 50 (a maximum) | not given | not given | not given | not given | from the report, p. 40 |
| Jones committee 1994 | 50 plus (subsistence terms); 30 to 35 (food constraint) | not given | not given | not given | 30 to 35 allows a safety margin for a run of bad seasons; none stated for 50 plus | from the report, p. 40 |
| Henry and Godden 1995 | 109 (energy) or 96 (protein), excluding wool and cotton | 1990-91 | no | energy and protein equivalents, no waste allowance | none | read |
| Foran and Poldy 2002 | 30 to 32 (meat) and 76 to 80 (grain with feed grain) | 1997-98 production, 2050 requirements | no (domestic requirement only) | requirement per person from their diet scenarios | none | read; derived here from their Table 2.5, as the authors give no capacity figure |
| PMSEIC 2010 | 60 | not given | by implication only | not given | not given | read; stated without a source |
| Lane, Dawes and Grace 2014, 2015; Lane 2017 | 40 national (9 to 40 by time frame; 23 summed over regions) | 2011 | no | default diet, waste 12% | long term: 100 years | the author's own (thesis method); read in Lane 2014, p. 280 |
| Bellotti 2017 | 61 (the population plus 36.6 fed by exports) | 2017 | yes (the larger part) | not stated | not stated | read |
| CSIRO and University of Queensland 2025 | about 100 (27 at home plus 63 abroad) | 2025 | yes | not stated | none | read |

Table 1 note. The four rows marked "from the report" are taken from the Jones committee report (House of Representatives Standing Committee for Long Term Strategies 1994), not from the two csv files above; the page is given in the route column. The Taylor, National Population Inquiry (Borrie) and National Population Council figures are second-hand, as the report cites them; the report dates the National Population Council work 1992 in its notes and 1991 once, in para 2.15, and 1992 is kept. The Jones committee is the House of Representatives Standing Committee for Long Term Strategies. "Not given" means the report does not state it.

## 2. The concept, its refinements and its critics

This section asks whether carrying capacity is a sound idea for people; supplementary section S1 gives further positions.

The term has several roots. Sayre (2008) traced it from shipping, where it meant what a vessel could carry, to range management, where it meant the stock a pasture could hold. From there it was joined to the asymptote of the logistic curve, the K of population ecology. Sayre separates a static reading, a fixed ceiling, from a variable reading, a ceiling that moves with conditions.

Some authors defend the concept and extend it. Hardin (1986) accepted that capacity is imprecise but held that it is needed: because overshoot is serious, "the conservative approach is to stay well below the best estimate of carrying capacity" (p. 601). He proposed a cultural carrying capacity, set by the quality of life a society chooses and always below the biological limit (p. 603).

Other authors question the concept. Seidl and Tisdell (1999) argued that once human activity is involved the concept becomes normative, so that there is "no longer an objective, single level of carrying capacity" (p. 405). Sayre (2008, p. 131) found that a static capacity is "theoretically elegant but empirically vacuous", while a variable one is "theoretically incoherent or at best question-begging". Price (1999, p. 17) concluded that the concept is "seriously flawed" and "may be no more than a self-validating belief". Cohen (1995) held that human carrying capacity "cannot be defined for a nation independently of other regions if that nation trades with others" (p. 343). That bears directly on Australia, which exports most of its agricultural production (CSIRO and University of Queensland 2025, p. 30). At world scale, van den Bergh and Rietveld (2004) pooled 69 studies giving 115 estimates, with a median of 7.7 billion people for those built on a stated method (pp. 195, 199, 200).

The ecological footprint turned the question around. Rees (1992) asked not how many people an area can support but how much land a given population needs; Wackernagel and Rees (1996) set out the method, and Lenzen and Murray (2001) modified it to count the land Australia actually uses. Chisholm (2000) argued in the Australian debate that resource limits do not set population limits in economies open to trade and new technology.

The debate since 2016 has moved to planetary limits and overshoot. The planetary boundaries framework proposed boundaries that "define the safe operating space for humanity" (Rockström et al. 2009, p. 472); it does not use the words carrying capacity. Overshoot accounts had been built at world scale (Wackernagel et al. 2002), and Rees (2023) argues that humanity has exceeded its long-term carrying capacity. O'Neill et al. (2018) set social thresholds against shares of biophysical boundaries, nation by nation. Biermann and Kim (2020) appraised the approaches used to define planetary limits. Wang (2022) framed land carrying capacity as a question of food security, to be set region by region.

Planners need the concept, whatever its standing in ecology. They must judge whether a region's land and water can feed the population they plan for, and a capacity figure puts that judgement in numbers. The critics show what such a figure needs: a stated question, standard of living and diet, and time frame. Sections 5 and 6 make those choices explicit for each method. The thesis classed methods by their inputs and outputs and by their scale (Lane 2014, chapter 6), and section 4 uses the same typology.

## 3. How the review was done

### 3.1 Review method (narrative and critical reviews)

This paper is a critical review in the sense of Grant and Booth (2009, p. 94): it draws on wide reading and critical evaluation and goes beyond description to a model, here a guide to which method fits which purpose. Its synthesis is narrative, which Greenhalgh et al. (2018, p. 2) argue serves a different purpose from a systematic review, not a lesser one; a question of method fit calls for interpretation across methods, not for pooling comparable results. A narrative review can be rigorous when it states its boundaries and justifies what it includes and excludes (Sukhera 2022, pp. 414 to 415), and any review should state its selection rule and what it left out (Snyder 2019, p. 337; Haddaway et al. 2020, p. 1583).

Works published from 2011 onwards, by year of publication, were eligible. Works published before 2011 were included only to trace the lineage of a method or concept. Within those bounds the review covered the well-known methods across the main approaches, and excluded index methods with no basis in food or land.

Works came from four routes: the author's citation exports and the OpenAlex list of works citing the author's papers; a sweep for each method family; a scoping search for the concept and the review method; and a recency sweep of Crossref. Government documents on population, food security and food waste were taken as grey literature.

Each cited work carries a reading label in the literature register: read in full, at page level or in a targeted way, reported (held only through another source, as the 1975 CSIRO figures are), or record only. Where no file of a work is held, it is cited through a held work that cites it or, where none is held, from its abstract; the claims files record which.

Section 5 sets out the test design: a common data set, and a fidelity check against each method's authors.

---


## 4. A catalogue of methods

This section sorts the methods into families by the question each answers and states what each can and cannot see, so that the question behind each published figure is clear before section 5 compares numbers. Table 2 carries inputs, outputs and scale and Figure 1 maps the families; supplementary section S2 gives the fuller account.

[Table 2: the catalogue of methods (family, question answered, inputs, outputs, scale, sources); to be built from a catalogue csv that does not exist (see Drafter notes)]

[Figure 1: the methods mapped by the question each answers, from the same catalogue csv (not built)]

### 4.1 Resource-based land and diet

The method sets the land a population needs for a stated diet against the land available. Peters, Wilkins and Fick 2007 built a complete-diet land model for New York State. Peters et al. 2016 applied the same frame to the United States under ten diets, and Fairlie 2008 drew a land budget for Britain under six farming regimes. The author's thesis method belongs here (Lane 2014): it pairs pasture-fed food with crops, charges land for waste, fuel, fibre and a reserve, and reads capacity as the population the land feeds on a stated diet. The method sees land, yields and diet together; it does not see trade, and sees variation between years only through an allowance.

### 4.2 Energy and protein balance

The method counts the food energy and the protein of domestic production, treats exports as food, scales production to a potential land base, and divides by a consumption factor per person (Henry and Godden 1995). It counts each nutrient alone, with no diet that has to balance, no waste and no pairing of pasture with crops.

### 4.3 Commodity balance and the nutritional food balance

A commodity balance asks whether domestic production covers the human requirement for each commodity. Foran and Poldy 2002 set the requirements for grain, meat and fish under three population paths to 2050 against production. They give no capacity figure; one can be read as production over the requirement per person, the smallest population binding. The method sees tonnes, not land, weather or a change of diet.

### 4.4 Export-inclusive counts

Export-inclusive counts add the people fed abroad by Australian exports to the people fed at home. CSIRO and University of Queensland 2025 extrapolate in proportion: if the share eaten at home feeds the population, the exported share feeds a proportional number abroad. PMSEIC 2010 states, with no source, that Australia produces enough food to feed 60 million people (p. 1) and, citing the federal agriculture department, that production feeds some 40 million people outside Australia (p. 15); it does not add the two. These counts are neither energy-based nor land-based, and assume exports would be eaten in the proportions of the domestic diet.

### 4.5 Ecological footprint

The footprint inverts carrying capacity: it asks how much productive land a population appropriates, wherever that land lies (Rees 1992; Rees 1996; Wackernagel and Rees 1996). Wackernagel 1994 set out its rates: the land a tonne of each product needs at world-average productivity. The food row sums consumption per person times that land, so trade drops out; it becomes a capacity only when a country's own land is divided by the land a person needs. Wackernagel et al. 1999 took the method to national accounts on 1993 data, with footprint and bio-capacity both in hectares of world-average productivity, not of the nation's own land (pp. 377, 380, 386). Simpson, Petroeschevsky and Lowe 2000 applied the method to Australia, and Lenzen and Murray 2001 modified it to count Australia's actual land use. The method sees the demand for land at world-average productivity, not the productivity of the actual land or any pairing of pasture with crops.

### 4.6 Land per diet and people per hectare

Land-per-diet indices express a diet as the land it needs at a stated productivity. Alexander et al. 2016 define the HALF index: the land the world would need if everyone ate a given country's diet, as a share of world land, at world-average production. The authors state that the index is not predictive (Alexander et al. 2016, p. 89). Cassidy et al. 2013 turn the measure around: people nourished per hectare of cropland, on a diet of 2,700 kcal a day (p. 4). Cropland is the only land counted, so grazing is left out. These methods see land at world-average productivity, or crop calories, by diet, but not the productivity of a country's own land or a diet that has to balance.

### 4.7 Optimisation models (diet and land use)

Optimisation models choose a diet or land use that meets stated limits at least cost or least departure from what is observed. Chaudhary and Krishna 2019 optimised national diets against nutrient limits and per-person limits drawn from planetary boundaries; Gazan et al. 2018 and van Dooren 2018 review diet optimisation. LUTO, a land-use optimisation model of Australia, allocates land uses on a fine grid against land-sector targets (Gao and Bryan 2017). These models see trade-offs among nutrients, cost and environmental limits; a people count is not their output.

### 4.8 Integrated resource-flow models

Integrated resource-flow models trace stocks and flows of land, water, energy and materials through an economy. Foran and Poldy 2002 built the Australian framework behind their commodity balance; no method paper for it was reached. Hatfield-Dodds et al. 2015 and Bryan et al. 2016 ran national scenario models of Australia, and Navarro Garcia et al. 2023 ran the FABLE Calculator for Australia (Jones et al. 2023); none gives a people count. These models see feedbacks and pressures.

### 4.9 Water-bounded capacity

Water-bounded methods cap capacity by land suitability, water and realistic yields. Khorsandi et al. 2022 combine land suitability, water and a cap on the share of net primary production that people take, at several spatial scales in Iran; their capacity falls as the units become smaller and more local. Khorsandi et al. 2023 simplify the method, which is catalogued here and not tested in section 5. These methods treat as limits what the land and diet methods take as given.

### 4.10 Failure probability

Fearnside 1985 defines capacity as a relation between population density and the probability that settlers fail, not as one number. A settler fails in a year when consumption falls below a standard; Fearnside tests calories, total protein, animal protein and cash separately, with the calorie standard set at 2,550 kcal a person a day (Fearnside 1985, p. 352). Capacity is read from the curve of the failure rate, the share of settler-years below the standard, against density, at the maximum failure probability the planner accepts. The method sees variation between years, which the other families average away.

### 4.11 Index methods and planning studies

Graymore, Sipe and Rickson 2010 rank regional indicators against thresholds in place of a carrying capacity they treat as not measurable, so their index gives no people count. Of the planning-oriented studies, Gutteridge 2005 set a footprint against a carrying capacity for South East Queensland. The Noosa and Douglas Shire studies applied carrying capacity to local planning; the Noosa study is cited through Lane 2010 and the Douglas Shire study through the thesis (Lane 2014, chapter 6) only.

## 5. Testing the methods on common Australian data

Tables 3 to 7 carry the numbers; supplementary section S3 gives the implementation detail and the arithmetic of each fidelity check.

### 5.1 The common data set

Every method used one data year, FAOSTAT (2025) data for 2021 to 2023. The land base is Australia's 31.65 Mha of cropland and 331.87 Mha of pasture, 363.5 Mha in all. The consumption basis is the FAO food balance per person for 2021-23, 3,525 kcal and 120.7 g of protein a day, which includes retail and household waste. The per-person bases are FAO's head count for the same years, 26.20 million; the model's 2025 population of 27.6 million enters no method reading, only the model's own rows and the failure probability.

### 5.2 Fidelity check and test

A fidelity check compares an implementation with its authors' published figure on their data; the test applies the method to Australia on the common data. Each component checked was graded on the rebuild from the authors' printed inputs where one exists, and otherwise on the rebuild as run: reproduced (within the rounding of the published figure, or within 2%), partly (within 10%) or not reproduced (beyond 10%). Where no published figure could be reached, the method was reported as implemented from its published description alone. The authors were not consulted; a second build, where one exists, was written independently from the same description.

### 5.3 Energy and protein balance

*Access.* Henry and Godden 1995 print the recipe, its 1990-91 production totals and the consumption factors they infer from Gifford et al. 1975 (p. 99).

*Fidelity.* Run on the printed totals, the recipe gave 108.9 million (energy) and 95.7 million (protein), against the published 109 and 96 (p. 100): reproduced within rounding. The 1990-91 totals were not rebuilt, because the factors for each item are not published.

*Test.* On the FAO food balance for 2021-23, with exports counted as food, the method reads 134 to 211 million: two currencies and three land-base cases, not an uncertainty range, with the 1990-91 in-use land carried forward (section S3.1).

### 5.4 Ecological footprint, food row

*Access.* Simpson, Petroeschevsky and Lowe 2000 give a food row of 1.758 ha a person of pasture, 0.095 ha of crop land for feed and 0.312 ha of crop land for plant foods (Table 1, p. 14).

*Fidelity.* Three builds differ in how pasture is charged (section S3.2). At the sheep-meat rate Wackernagel's thesis prints (build 3; Wackernagel 1994, p. 285), pasture is 1.718 ha against 1.758, 2.3% low: partly reproduced. Build 1 is 1.2% low, but not at that printed rate. Crop land for feed is 21.6% high on the thesis rates (not reproduced), though builds 1 and 2 come within 4%. Crop land for plant foods, the crop-plus-pasture total (11.9% low) and the clothing row's wool pasture are not reproduced.

*Test.* With Australia's land counted at the productivity of its own output (section 5.11), the footprint reads 64.8 to 117.0 million, and 64.8 to 84.6 with crop and pasture together. Counted in world-average hectares, Australia's land divided by the land a person needs on consumption in 2021-23 gives 146 to 343 million on current yields, and 103 million with build 3's yields held at their printed 1990 values.

### 5.5 HALF index

*Access.* Alexander et al. 2016 and its supplement, which prints each country's index (their Table S5, p. SI-6).

*Fidelity, on 2011 data.* The index is partly reproduced. On the current FAOSTAT revision the world is 2.2% low (34.4 against 35.13) and Australia 0.8% high (113.1 against 112.20); on the inputs the authors printed the world is 2.8% high and Australia 8.4% high (121.6). On the printed inputs the gap is mostly the world pasture area, 3,364 Mha in the HALF supplement against 3,182 Mha in the current revision (section S3.3). New Zealand is not reproduced (94.8 against 135.76). Table S6 gives the other countries.

*Test.* Australia's diet in 2021-23 needs 1.32 ha a person at world-average production, a HALF of 81.0% of world land. Read in the footprint way, which HALF is not, Australia's 363.5 Mha divided by 1.318 ha a person gives about 276 million people at world-average production and 76.0 million at Australia's own productivity (section 5.11).

### 5.6 People per hectare

*Access.* Cassidy et al. 2013 print the recipe, the feed-to-food efficiencies kept here (Table 1, p. 3) and results for the world and four countries (Table 2, p. 3). Their supplementary information was not read, so crop energy per kilogram and the grain-fed share of beef are assumptions.

*Fidelity, on 2011 data against the paper's years of about 2000.* The delivered share of calories is partly reproduced (the world 61% against 59%), but the United States feed share is not (41% against 67%), nor its other-use share (32% against 6%). People per hectare are not reproduced: they run 22 to 42% above the paper's, on 22 crop items against the paper's 41 crops (p. 4), and 5 to 25% above on current FAOSTAT yields for the paper's years (section S3.4).

*Test.* On 2021-23 data Australian cropland delivers 6.0 people a hectare, against 7.9 for the world. Read as a capacity, which Cassidy's measure is not, the delivered calories of Australia's 22 crop items feed 147 million people at 2,700 kcal a day, and 145 million in the second build.

### 5.7 Commodity balance

*Access.* Foran and Poldy 2002 set the 2050 requirements for grain, meat and fish against production in 1997-98 (Table 2.5, p. 64). The capacity reading is this project's (section 4.3).

*Fidelity.* FAOSTAT reproduces their 1997-98 production of grain and meat within 1.2% each way, and their balance is positive for grain and meat and short for fish, as they conclude.

*Test.* On production in 2021-23, meat supports 40 million people on their requirement per person and 41 million on actual use, grain with its embodied feed grain 128 and 127 million, and fish 17 and 12 million.

### 5.8 Failure probability

*Access.* Fearnside 1985 gives the method and Fearnside 1990 one result for a Brazilian study area (p. 195), which Australian data cannot check, so the failure frame was applied as a test of the idea, not as an independent method.

*Assumptions.* The model's drought allowance scales the harvest to the worst year expected once in T years, from a 150-year record of wheat, oats and barley yields.

*Test.* On the corrected model with 2025 data, capacity is 41.5 million in an average year. At a maximum acceptable failure of 1 in 10 it is 30.8 million, 26% lower, and at 1 in 100 it is 18.9 million, 54% lower. At the 2025 population the failure probability is 5.8 to 6.1% a year, about 1 in 16 to 17, and it depends strongly on the method (section S3.6). The Jones committee's 30 to 35 million after a safety margin (para 2.16, p. 40) is of the size of the model's 30.8 million at 1 in 10, though not a return period (section 6.6).

### 5.9 The author's model as an exemplar

The author's model (Lane 2014) was run on the same data at three tiers, each from a frozen release: the thesis method as built with its errors kept, the thesis method corrected, and an improved tier that builds on it with Australian settings (Table 4).

### 5.10 The methods side by side

In Table 3 and Figure 2 the readings fall into three groups. The first is the aggregate methods (the energy and protein balance, the footprint, HALF and people per hectare), which count calories or land with no diet that has to balance. With the footprint and HALF at Australia's own productivity, the primary reading (section 5.11), they read about 65 to 211 million, about 1.6 to 5 times the model: the footprint 64.8 to 117.0 million (1.56 to 2.82 times) and HALF 76.0 (1.83 times). In world-average hectares they read 134 to 343 million, about three to eight times (Table 3). The second, the commodity balance, reads 12 to 41 million; its low end is the single-commodity fish reading, and its meat reading of 40 to 41 million is bound, as the model is, by pasture-fed meat. The third, the failure view, is the model's own runs read through Fearnside's frame; its 1-in-10 point, 30.8 million, lies just below the corrected range of 31.1 to 49.2 million.

Table 3. Each method's reading of Australia on current data (million people unless stated), with the grade of its fidelity check (section 5.2). A dagger marks a method graded partly or not reproduced on some component. Built from `analysis/method_tests_2025/cross_method.csv` and `cross_method_local.csv` for the readings and from `analysis/method_tests_2025/fidelity.csv` for the grades (feed cropland +21.6%, crop plus pasture -11.9%, HALF's Australia +8.4% on the printed inputs). Both model ranges are the widened ones, 2,000 draws each: corrected 31.1 to 49.2 (19 settings, `results/ranges_2025-fixed_wide.csv`) and improved 37.9 to 60.0 (18 settings, `results/ranges_2025-improved_wide.csv`), as `cross_method.csv` prints them. The footprint cell names the yield basis of each end; the csv cell gives 103 to 343 without it, and the 146 on current yields is build 3 on 2021-23 world yields. The people-per-hectare cell gives the all-cropland reading on the same-year pairing, as the csv does; matching harvests lowers it to about 183 (section S3.4). `cross_method_local.csv` still prints the earlier 13-setting improved range and needs regenerating.

| Method | What it counts | What it leaves out | Primary reading for Australia | Reading in world-average hectares | Fidelity check against its authors |
|---|---|---|---|---|---|
| Energy and protein balance (Gifford; Henry and Godden) | calories and protein of production, exports as food, scaled to a land base | the diet, the pasture and crop pairing, waste | 134 to 211 | none: counts Australia's own production | reproduced: 109 and 96 from their printed totals, within rounding |
| Ecological footprint, food row (Simpson) † | crop and pasture land | the pairing, energy land not set against Australian land | 64.8 to 117.0 at Australia's own productivity (crop and pasture together 64.8 to 84.6) | 146 to 343 on current yields; 103 at 1990 world yields (cropland-bound 103 to 160; crop and pasture together 268 to 343; three builds) | partly: pasture 2.3% low on the thesis rates; not reproduced: feed cropland 21.6% high, plant-food cropland, crop plus pasture 11.9% low, wool |
| HALF index (Alexander) † | land at world-average production, by diet | the pairing | 76.0 at Australia's own productivity | 276 | partly: Australia 0.8% high and the world 2.2% low on current data, 8.4% and 2.8% high on the authors' printed inputs; New Zealand not reproduced |
| People per hectare (Cassidy) † | cropland calories delivered after feed and biofuel, exports by importers' use | grazing, protein, a balanced diet | 5.8 to 6.0 people a hectare delivered; 145 to 147 million (about 190 on all cropland) | none: counts Australia's own delivered calories | not reproduced: people a hectare 22 to 42% above the paper's (5 to 25% on current yields for its data years) and the United States feed and other-use shares; delivered shares partly; two builds agree within 5 to 8% |
| Commodity balance (Foran and Poldy) | tonnes of grain, meat and fish against a requirement per person | land, weather, diet change | 40 to 41 (meat), 12 to 17 (fish), 127 to 128 (grain with feed grain) | none | reproduced: production within 1.2%, their balance as they conclude; the 30 and 77 readings are derived here |
| The model read through Fearnside's failure frame | the harvest in a year of given probability against the diet | one criterion; weather as one factor on all yields | 41.5 (average year), 30.8 (1 in 10), 18.9 (1 in 100) | none | not checked: his data are Brazilian; the idea applied |
| The model, thesis method corrected | land, yields, diet, waste, fuel, fibre, reserve | trade, variability between years beyond the allowance | 41.5 (31.1 to 49.2) | none | the reference; the thesis method as built reproduces the thesis figures exactly |
| The model, improved | as above, with Australian settings | as above | 53.6 (37.9 to 60.0) | none | built on |

Table 4. The model's entry for Australia, 2025 data, by tier (million people; Monte Carlo 5th to 95th percentile in brackets). Built from `analysis/method_tests_2025/model_entry.csv`. The corrected and improved rows carry the widened range (2,000 draws; 19 and 18 settings, section S5; `results/ranges_2025-fixed_wide.csv` and `results/ranges_2025-improved_wide.csv`); the mirror row keeps its 13-setting range of 1,000 draws, run before six settings were added, and not rerun.

| Release | Tier | Short term | Long term | Worst of 10 years | Worst of 100 years | Population |
|---|---|---|---|---|---|---|
| 2025-mirror | Thesis method as built, errors kept | 49.4 (43.4 to 54.3) | 14.1 (11.8 to 16.0) | 36.66 | 22.51 | 27.6 |
| 2025-fixed | Thesis method corrected (the baseline entry) | 41.5 (31.1 to 49.2) | 15.6 (13.3 to 18.8) | 30.81 | 18.92 | 27.6 |
| 2025-improved | Improved (built on) | 53.6 (37.9 to 60.0) | 18.5 (15.7 to 22.1) | 39.93 | 24.68 | 27.6 |

[Figure 2: each method's reading of Australia, as run and harmonised, beside the model's corrected and improved ranges, from `cross_method.csv` and `harmonised_comparison.csv` (no plotting script)]

### 5.11 The harmonised comparison

Every method was run on the common inputs of section 5.1 and kept its defining choices, such as cropland only for people per hectare; none was given the model's diet, yields or land classes (Table 5). Equalising inputs narrows the spread within the energy and protein balance (145.2 to 148.8 million) and within people per hectare (110.9 to 112.9 million; section S3.4). The footprint keeps its definitional spread, and HALF and the meat reading barely move.

Whether equalising narrows the spread among the methods depends on where the line between input and method is drawn, so the comparison is reported under two classifications. On line (a) the productivity basis, world-average hectares for the footprint and HALF, is part of the method and stays. On line (b) it is an input: the footprint (builds 1 and 3) and HALF take Australia's land expressed as the world-average hectares that would grow its output in 2021-23, the adjustment Wackernagel and Rees (1996, p. 78) describe, in which a hectare twice as productive as the world average counts as two.

The distance of a method's readings from a reference is their mean absolute natural-log ratio to it, and the share closed is the fall in that distance on harmonising over the distance as run, with the five methods weighted equally. The references are the corrected model (41.5 million) and the median and geometric mean of the five method centres, each stage against its own centres (Table 6).

On line (a) equalising closes 4.1% of the distance to the model, and the spread of method centres does not narrow: the standard deviation of their logs goes from 0.646 to 0.702 and highest over lowest from 6.22 to 6.95. On line (b) it closes 38.5%, and the spread of method centres narrows by about a third, to 0.440 and 3.70; over all 19 readings the narrowing is about a sixth. Against the median and geometric mean of the centres the shares are -4.9% and -6.3% on line (a) and 16.0% and 17.2% on line (b). Which line holds is a classification, not a finding; the productivity basis is the largest single input once it is counted as one.

Table 5. The harmonised comparison by method: each method on the common inputs, with its defining choices kept (million people unless stated). Built from `analysis/method_tests_2025/harmonised_comparison.csv`, summarised by method as `make_readme_tables.py` summarises it. Column (e) is the primary reading of the footprint and HALF.

| Method | (a) Each method's own setup, on the common data | (b) Harmonised | (c) Input factor, b over a | (d) b over the corrected model | (e) Australia's own productivity (p. 78) |
|---|---|---|---|---|---|
| Energy and protein balance (Gifford; Henry and Godden) | 134 to 211 | 145.2 (energy), 148.8 (protein) | 0.69 to 1.11 | 3.50 to 3.59 | |
| Ecological footprint, food row (Simpson) | 103 to 343 (cropland-bound 103 to 160; together 268 to 343) | 139 to 343 (cropland-bound 139 to 160; together 278 to 343) | 1.00 to 1.42 | 3.36 to 8.27 | 64.8 to 117 (cropland-bound 113 to 117; together 64.8 to 84.6; pasture alone 53.9 to 77.9); builds 1 and 3 |
| HALF index (Alexander) | 276 | 275.8 | 1.00 | 6.65 | 76.0 |
| People per hectare (Cassidy) | 145 to 190 | 111 to 113 | 0.59 to 0.77 | 2.67 to 2.72 | |
| Commodity balance (Foran and Poldy) | meat 40, fish 17, grain 128 | meat 41, fish 12, grain 127 | 0.71 to 1.03 | 0.29 to 3.06 | |
| Failure probability (Fearnside) | 41.5 (average year), 30.8 (1 in 10), 18.9 (1 in 100) | blank: the readings are the model's own runs | | | |
| The model, thesis method corrected | 41.5 | 41.5 | 1.00 | 1.00 | |
| The model, improved | 53.6 | 53.6 | 1.00 | 1.29 | |

Table 5 note. The people-per-hectare row is the same-year pairing, as `harmonised_comparison.csv` holds it: 190 million on all cropland and an input factor of 0.594 to 112.9. Matching harvests lowers the all-cropland reading to about 183 (section S3.4). Column (d) uses the csv's whole millions, so the commodity balance's grain multiple reads 3.06 here and 3.05 in Table S7, which carries 126.6.

Table 6. The harmonised comparison under both classifications of the productivity basis: distance of the readings from each reference, and the spread among them, as run and harmonised (natural-log units; highest over lowest as a ratio). The paired set is 19 readings of the five methods; footprint build 2, Fearnside's method and the model are outside it. Built from `analysis/method_tests_2025/harmonised_comparison_lines.csv` (script `harmonised_lines.py`). The share closed is (as run less harmonised) over as run; for the highest over lowest it is taken on the log scale. A negative share means the readings sit further apart or further from the reference. Reference values (million): median of method centres 164.7 as run, 147.0 harmonised on line (a) and 82.0 on line (b); geometric mean 150.3, 135.8 and 83.6. A second measure, the factor split to 41.5 (the mean absolute log of each method's input factor, over that plus the mean absolute log of its method factor, five methods weighted equally), gives 9.6% on line (a) and 41.3% on line (b).

| Reference or measure | (a) as run | (a) harmonised | (a) share closed | (b) as run | (b) harmonised | (b) share closed |
|---|---|---|---|---|---|---|
| Distance to the corrected model (41.5) | 1.411 | 1.353 | 4.1% | 1.411 | 0.867 | 38.5% |
| Distance to the median of the method centres | 0.530 | 0.556 | -4.9% | 0.530 | 0.445 | 16.0% |
| Distance to the geometric mean of the method centres | 0.535 | 0.569 | -6.3% | 0.535 | 0.443 | 17.2% |
| Standard deviation of log method centres | 0.646 | 0.702 | -8.6% | 0.646 | 0.440 | 31.8% |
| Highest over lowest method centre | 6.22 | 6.95 | -6.0% | 6.22 | 3.70 | 28.4% |
| Standard deviation of log readings (19) | 0.718 | 0.768 | -7.0% | 0.718 | 0.604 | 15.9% |
| Highest over lowest reading (19) | 22.69 | 32.14 | -11.2% | 22.69 | 12.40 | 19.4% |

### 5.12 Gap attribution

Each residual against a published figure was attributed by changing one candidate cause at a time; no output was adjusted to meet a published figure. Table S1 prints a cause's share of a residual only where the residual is 5% or more of the published figure; below that a share is ill-conditioned, so the table prints the change each cause makes in the figure's own unit and, for HALF's Australia, in people. HALF's Australian residual is 0.92 points, and the HALF supplement's world pasture alone moves the figure 5.76 points the other way, 9.2 million people on Australia's 2011 cropland and pasture (396.1 Mha). For the world, the United States and Argentina the residuals are of the size and sign of the revisions to FAOSTAT since the authors' download (section S3.7).

### 5.13 An intake basis

FAO's food supply includes retail and household waste, while the model charges its waste separately. As a variant, each food's per-person use was multiplied by the share eaten, on FAO's waste factors for North America and Oceania and on the model's own loss factors (Table S7). On FAO's factors the energy balance reads 169.7 million (energy) and 182.3 (protein), people per hectare 132.0, HALF 324.3, the footprint 189.0 (cropland-bound) to 404.8 (crop and pasture together), and the commodity balance 48.1 (meat), 19.7 (fish) and 137.2 (grain). The gap to the model widens for every reading above it, fish narrows, and meat, level with the model on supply, crosses above it. The calorie and land readings rise from 2.7 to 9.3 times the corrected model to 3.1 to 10.9 times on FAO's factors and 3.3 to 12.9 on the model's.

### 5.14 The pairing of pasture-fed food with crops, relaxed

After the adjustment for productivity, what remains above the model is consistent with a feature that the model carries and neither the footprint nor HALF does. The model pairs pasture-fed food with crops and cedes the cropland the crops do not need to pasture, which then binds. The pairing was relaxed in the corrected release in two ways (Table 7); a third, stronger relaxation is reported in the repository. Variant 1 replaces the pasture-fed meat and dairy that the pasture cannot carry, kilojoule for kilojoule, by the diet's cropland foods; it alone relaxes the pairing and changes nothing else. Variant 2 lowers the meat-and-egg share within the model's own diet family to what the pasture carries, a mix of its 3.5% and 4.0% diets.

Variant 1 reads 81.7 million, above HALF's 76.0 and the footprint's 64.8 and 93% of the way to the footprint's 84.6, at the diet's energy and with protein falling from 93 to 81 g a day. Variant 2 passes all three readings but also changes the diet. Variant 2 reads 107.7 million, with energy 0.5 to 0.6% above the base and protein 4.2% below; the best single diet of the family, 2.5% meat and eggs, reads 118.0. Relaxing the pairing alone therefore brings the model past the readings of HALF and footprint build 1 and most of the way to build 3, though the test cannot show it is the only cause, and variant 2 tests the fixed diet as much as the pairing. Variants that keep the diet's energy within 0.6% give 82 to 108 million, short of the unadjusted 134 to 343 million.

Table 7. The corrected model with the pairing of pasture-fed food with crops relaxed, Australia, 2025 data (million people), and the share of the gap from 41.5 to each adjusted reading that the variant closes (above 100% the variant passes the reading). Built from `analysis/pasture_2025/pairing_relaxed.csv` (script `pairing_relaxed.py`); the readings are column (e) of Table 5.

| Variant | What changes | Short term | Long term | Footprint build 1 (64.8) | HALF (76.0) | Footprint build 3 (84.6) |
|---|---|---|---|---|---|---|
| Base (corrected release) | nothing: pasture binds, idle cropland ceded to it | 41.50 | 15.62 | | | |
| 1. Energy substitution | pasture-fed food the pasture cannot carry replaced by cropland foods at equal energy; the pairing alone relaxed | 81.70 | 21.87 | 173% | 117% | 93% |
| 2. Meat share to the pasture | meat-and-egg share 3.79% in place of 12.0%, a mix of the 3.5% and 4.0% diets; the diet also changes | 107.69 | 21.90 | 284% | 192% | 154% |


# Paper B, sections 6 to 9 (first draft, D04; cut to the main-text limit, B98b)

## 6. What moves the number

This section measured, with the author's model on the same 2025 data, how far each design choice moved the answer, set at the ends the methods of section 4 take, with every other setting at the model's defaults. A factor here is the higher capacity over the lower one, not a ratio of people to capacity (Table 8; Figure 3). The comparison shows where each choice matters, not that the model's settings are right.

### 6.1 Exports counted or not

The proportional count of CSIRO and the University of Queensland (section 4.4) gave "around 100 million people in total" (section 1). An energy count of exports at 2,100 kcal a person a day, built here from the FAO food balance, fed 87 to 128 million from wheat and rice alone and 184 to 264 million from all foods. Against the model's 41.5 million in an average year, the proportional count moved the answer by a factor of 2.41 and the energy count by 4.4 to 6.4.

### 6.2 Grazing and pasture-fed food

Pasture is most of the land behind an Australian diet. In the model, crops and pasture-fed food are paired in a fixed diet, so whichever land runs short sets the capacity. Its Australian settings, beef output by state, dairy on land that can carry it and an organic factor for grazing ruminants in the long term, together with the waste and land-base settings, moved the short-term answer from 41.5 million (corrected method) to 53.6 million (improved), a factor of 1.29.

### 6.3 How waste is treated

Energy and protein balances and people per hectare count production as eaten (Henry and Godden 1995; Cassidy et al. 2013), and land-per-diet methods carry waste inside the diet. The thesis model applied loss factors from the United States (section 8.5); the improved model used Australian loss factors and limited its recycling credit to waste fit for feed. Taking avoidable waste from 12% to none moved the corrected method from 41.5 to 55.3 million, a factor of 1.33. On the improved method the same change moved it from 53.6 to 62.9 million, a factor of 1.17.

The model's 6% setting halves its retail-and-consumer loss share, mirroring UN Target 12.3 as Spang et al. (2019, p. 118) state it.

### 6.4 Which land counts

Henry and Godden (1995) rested their answer on Nix's estimate of 70 Mha of land available for intensive production (p. 98), and report that Gifford et al. (1975) scaled intensive land from 40.5 to 70 Mha, a factor of 1.73 (p. 99). The model takes the land as it is and sets aside a reserve. Doubling cropland out of non-agricultural land, the 1975 case, moved the answer from 41.5 to 45.1 million, a factor of 1.09. On the improved method the same case gave 58.3 million, a gain of 9% on both, which the model reads as the short-term diet being bound by pasture-fed meat and dairy, not by cropland.

### 6.5 Diet

Across the guideline diets from 15% to 5% meat and eggs, the improved release fed 48.3 to 103.3 million, a factor of 2.14. Against the default diet's 53.6 million, the nutrition-optimised diet with free choice and ten micronutrients fed 422.3 million, a factor of 7.88. Capacity was not monotone in the meat share on the improved release, with a dip at 2.5% meat and eggs and a cliff between 5% (103.3 million) and 7.5% (66.9 million).

### 6.6 The drought allowance

In the model the drought allowance is a quantity. With an allowance for the worst year in 50, the corrected and improved releases fed 23 to 30 million; for the worst year in 100, 19 to 25 million. From the average year to the worst year in 100, the corrected method moved from 41.5 to 18.9 million, a factor of 2.19. The Jones committee's margin for a run of bad seasons (section 1) is a stated allowance, not a return period, so its 30 to 35 million cannot be placed on the model's curve of failure probability.

### 6.7 The unit of self-sufficiency

Three points show the effect of the unit, on the corrected method, 2025 data, short term and the state yield basis. The nation fed 41.5 million. The states summed to 75% of that, and the SA2s to 37%. That 37% is 15.5 million: the sum over SA2s of their capacities. Nation against the SA2 sum is a factor of 2.67. The SA2 point sits on 2020-21 land and the others on the release land, which give the same national capacity. On the local yield basis, where each unit takes the yields of its own zone, the SA2 sum is 54%. The full curve is in the companion results paper.

### 6.8 The time frame

The thesis model set a short-term and a long-term setting side by side (Lane 2017). The long-term setting bundles a low-meat diet, organic yields, no avoidable waste, a 100-year drought allowance and a 30% reserve. On the corrected method it fed 15.6 million, against 41.5 million in the short term, a factor of 2.66.

### 6.9 How sure the answer is, as a method

A choice is a definition when it changes what the number means: what is counted, the unit of self-sufficiency, the time frame, the diet standard or the weather allowed for. It is a setting when it is a value within one meaning, such as a loss factor, a yield window or a calibration. Definitions (sections 6.1 and 6.4 to 6.8) are reported one at a time, as are waste and the Australian settings (sections 6.2 and 6.3), which by this rule are settings; settings are otherwise drawn together. A Monte Carlo of 2,000 Latin hypercube draws over 19 settings (section S5), 18 of which vary on this release, gives the corrected release a short-term capacity of 31.1 to 49.2 million at the 5th to 95th percentile, a factor of 1.58, and a long-term capacity of 13.3 to 18.8 million (Table 4). These ranges are a spread across the settings varied here, not confidence intervals. The release is not central: five of the six settings added have the release at one end of their range, so the median, 39.0 million, lies below 41.5. First-order shares add to 97% and interactions carry about 3%. Three settings carry four-fifths of the short-term variance: the source of the land areas (32%), the energy requirement (27%) and the window of herd and meat data (24%). Six settings rest on the author's judgement, these three among them; the energy window (PAL 1.4 to 1.8) is part of the NHMRC range of 1.2 to 2.2 (section S5).

### 6.10 The spread across settings against the definitions

Across the weather allowance, a definition, and avoidable waste, a setting by the rule of section 6.9, one model on one data set spans 18.9 million (the worst year in 100) to 55.3 million (no avoidable waste) on the corrected method. With the improved settings the top reaches 62.9 million. The spread across the settings varied here is narrower than that span. Figure 3 sets the published estimates, which run from 9.4 million to 100 million, a factor of 10.6 between two soft ends (section 1), on a ladder of nine rungs and eight steps that multiply to the whole, grouped here in three: 1.66 from 9.4 to 15.6 million, 4.03 from 15.6 to 62.9 and 1.59 from 62.9 to 100. The product holds for any steps chosen, so the ladder is a reading of the spread, not a decomposition. Its first step mixes a change of data, from 2011 to 2025, with the correction of the method; its low steps are on the corrected method and its high steps on the improved.

[Figure 3: the factor by which each design choice moved the answer, with the ladder of definitions; its steps from 9.4 to 100 million multiply to the 10.6, and its top rung, the midpoint of the two energy counts of exports (223.9 million, from 184 and 264), lies beyond the published span; from `analysis/method_tests_2025/design_choices.csv` and `analysis/method_tests_2025/ladder.csv`]

### 6.11 The ordering of the design choices

In Table 8, land mattered least (1.09) and exports counted by energy (4.4 to 6.4) and the optimised diet (7.88) most. The factor across the settings varied here, 1.58, is above the land base (1.09), waste (1.17 on the improved method, 1.33 on the corrected) and the Australian settings (1.29), and below the guideline diets (2.14), the drought allowance (2.19), exports (2.41 and more), the time frame (2.66) and the unit (2.67). From lowest to highest draw the factor is 2.22, which passes the guideline diets and the drought allowance.

Table 8. The design choices and the factor by which each moved the answer, in order of the factor. Built from `analysis/method_tests_2025/design_choices.csv` (script `design_choices.py`), whose Monte Carlo row prints the 13-setting range (36.3 to 45.8, factor 1.26) and needs regenerating; the Monte Carlo row here is from `results/ranges_2025-fixed_wide.csv` (19 settings, 2,000 draws: 31.1 to 49.2, factor 1.58) and is shown last for comparison.

| Design choice | What is compared | Low (million) | High (million) | Factor | Method and release |
|---|---|---|---|---|---|
| Land available | cropland as it is against doubled out of non-agricultural land | 41.5 | 45.1 | 1.09 | corrected |
| Avoidable waste | 12% against none | 53.6 | 62.9 | 1.17 | improved |
| Australian settings | thesis method corrected against improved | 41.5 | 53.6 | 1.29 | short term |
| Avoidable waste | 12% (default) against none | 41.5 | 55.3 | 1.33 | corrected |
| Diet | guideline diets from 15% to 5% meat and eggs | 48.3 | 103.3 | 2.14 | improved |
| Drought allowance | average year; worst year of 5, 10, 20, 50, 100 | 18.9 | 41.5 | 2.19 | corrected |
| Exports counted | the model against the CSIRO and University of Queensland proportional count (27 at home + 63 abroad) | 41.5 | 100.0 | 2.41 | published count |
| Time frame | long-term settings against short-term settings | 15.6 | 41.5 | 2.66 | corrected |
| Unit of self-sufficiency | nation against the sum over SA2s (state yield basis) | 15.5 | 41.5 | 2.67 | corrected |
| Exports counted (energy) | exports alone as an energy count, all foods, at FAO's own food energy per kg | 41.5 | 183.9 | 4.43 | energy count |
| Exports counted (energy) | exports alone as an energy count, all foods, at typed as-traded densities | 41.5 | 263.9 | 6.36 | energy count |
| Diet (optimised) | default diet against nutrition-optimised diet C (ten micronutrients) | 53.6 | 422.3 | 7.88 | improved |
| Uncertainty (Monte Carlo) | 5th to 95th percentile over 19 uncertain settings | 31.1 | 49.2 | 1.58 | corrected |

## 7. Which method for which purpose

### 7.1 The rating key and the methods

The matrix in Table 9 rates five published methods and the author's own model, read two ways, against four purposes as well suited, partly suited or not suited. A method is well suited to a purpose when the tests show it sees what the purpose turns on, partly suited when it does so with a stated limit that touches the core or only beside another method, and not suited when it cannot see it (section S7). The planning-oriented studies (Peters, Wilkins and Fick 2007; Fairlie 2008; Gutteridge 2005; Noosa and Douglas Shire) were treated as the balance family at other scales. The author rated each cell from the test records. A second rating was made by a blind checker session of an AI model, not a person, which was given the test records and not the draft. The two ratings agreed on 25 of the 28 cells, and the three differences, judgement calls on other methods, were adopted (section S7). The model's eight ratings agreed, although the second rater called its rating for regional planning a judgement call. No outside person has rated the table.

Table 9. Which method for which purpose: the author's ratings, checked by a second blind rating (section S7). Typed from `papers/B_methods/SECTION7_DRAFT.md` (no csv exists). The model's own limits (section 8) are not rated in the table: no trade, no herd-cycle risk, and constants without recorded sources.

| Purpose | Energy and protein balance | Footprint | HALF | People per hectare | Commodity balance | The model read through Fearnside's failure frame | The model as a land-and-diet balance |
|---|---|---|---|---|---|---|---|
| 1. Food security and drought risk | not suited | not suited | not suited | not suited | partly | well suited | well suited |
| 2. Why national estimates range from 9 to 100 million | partly | partly | partly | partly | partly | partly | well suited |
| 3. Regional and local land-use planning | not suited | partly | not suited | not suited | not suited | partly | well suited |
| 4. Diet change and land use | not suited | partly | well suited | partly | not suited | not suited | well suited |

### 7.2 Food security and drought risk

The balance and its failure view, one model read two ways, were rated well suited: the balance supplies the level, with a stated diet and the pasture-crop pairing, and the failure view reads it against the weather record (section 5.8). The commodity balance, with no weather and no land, was rated partly suited, and the aggregate methods, which count an average year, not suited.

### 7.3 Why national estimates range from 9 to 100 million

Only the balance was rated well suited to explaining the range, because one model run under the choices of section 6 spans 15.5 to 62.9 million, and a proportional count of exports reaches the published 100 million (section 6.10). Each other method was rated partly suited, because each shows what one family of published estimates counts: the energy balance is the method of Henry and Godden (1995) and Gifford et al. (1975), and the commodity balance gives the 30 to 32 million meat count derived from Foran and Poldy's table. HALF and people per hectare read high as capacities (section 5.10), which is part of explaining the range.

### 7.4 Regional and local land-use planning

Only the balance carries a unit of land, a diet and the pasture-crop pairing, and the unit decides the answer (section 6.7). The footprint was rated partly suited, because its own local-productivity adjustment sets a diet's demand against a given area (section 5.11). The failure view was rated partly suited: Fearnside's own application covered a 23,600 ha study area, and his simulation needs too much data for large areas (Fearnside 1990, p. 195).

### 7.5 Diet change and land use

HALF, partly reproduced on 2011 data (section 5.5), was rated well suited for comparisons across countries; at world-average production Australia's value in 2021-23 was 2.4 times the world average. The balance was rated well suited for what Australia's land can feed, with the dip and the cliff of section 6.5.

### 7.6 The short reading

No single method serves all four purposes. Read as capacities, the aggregate methods give about 65 to 211 million at Australia's own productivity, about 1.6 to 5 times the balance, and 134 to 343 million in world-average hectares, about three to eight times. What remains above the model is consistent with the footprint and HALF not carrying the pairing of pasture-fed food with crops that binds the model: relaxing the pairing alone brings the model to 81.7 million (section 5.14). For a security claim, report a level and a failure probability from the balance run through the failure view, and add a commodity balance for the item that fails first.

### 7.7 A minimum reporting checklist

Table S4 gives a minimum reporting checklist of twelve items (section S6). The land base stays on the list, although it moved the answer least, because it moves the energy and protein balance by 31% (section S3.1).

### 7.8 Cautions

A figure of people fed is not a forecast or a target. The ratings, the author's judgement on five methods and the model tested on Australian data, may differ where grazing is a small share of food land. The failure view here is the model's own runs read through Fearnside's frame, not Fearnside's own simulation.

## 8. Limitations and what no method does

This section states, in the same terms for every method, what no method reviewed can do and what the author's own method lacks.

### 8.1 Variability

Every method reviewed but the failure view works in an average year. Production shocks have become more frequent, and national totals smooth sudden losses in a large country such as Australia (Cottrell et al. 2019, pp. 130, 135). The failure view here carries one criterion, the default diet, where Fearnside tested four (section 4.10). No method reviewed gives the probability of a failure in the herd cycle.

### 8.2 Trade

Most methods treat the region as closed or count exports at full value; in the footprint and HALF trade drops out. Reserves and trade set a country's exposure to supply shocks (Marchand et al. 2016), and self-sufficiency is better read as a continuum than as a yes or no (Clapp 2017). Production within 100 km can meet the demand for a given crop for only 11 to 28% of the world's people (Kinnunen et al. 2020, p. 229), a range across crops, not an uncertainty. The model is self-sufficient by design; trade is a way around its constraint, not part of it.

### 8.3 Energy

Simpson, Petroeschevsky and Lowe (2000) counted 0.43 ha of energy land in the food row, about a sixth (16%) of that row (p. 14); the model counts none. Energy after the farm gate is documented (Ladha-Sabur et al. 2019), but no Australian figure for farm energy use was found.

### 8.4 Diet dynamics

Each method fixes one diet, but diets move with the nutrition transition (Bodirsky et al. 2020) and with income (Tilman and Clark 2014). Erb et al. (2016) report the option space under several diets, as section 6.5 does. The fixed diet is the decisive assumption: within the model's own diet family, a meat-and-egg share of 3.8% against 12%, a mix of its 3.5% and 4.0% diets, feeds 107.7 million against 41.5 (section 5.14).

### 8.5 Borrowed constants and data limits

The thesis model borrowed constants from the United States: loss factors (Buzby 2010; Muth 2011; both cited in Lane 2014, pp. 201 to 202) and a carcase-to-retail factor for beef (USDA Handbook 697, cited in the archive's errata). Its nutrient values came from AUSNUT 2007 (cited in Lane 2014, p. 202). These constants are declared as assumptions, and their corrections are listed in the errata. The model cannot carry soil, fertiliser, labour, a water ceiling on irrigation, or climate effects on pasture and livestock.

### 8.6 Implementations reproduced in part

Three of the five published methods rest on implementations reproduced in part or not at all (Table 3). Simpson's 0.312 ha of crop land for plant foods (the builds gave 0.074 to 0.142 ha), 0.854 ha of pasture for clothing and the crop-plus-pasture total were not reproduced (Simpson, Petroeschevsky and Lowe 2000, p. 14), and the footprint test omitted pulses from 1991-92 consumption and did not rebuild energy land. HALF is partly reproduced, and people per hectare is not; the people-per-hectare test typed crop energy, feed shares and livestock values as assumptions. The energy and protein test was rebuilt on FAO food balance data, not the model's production layer.

### 8.7 Where another method does better

HALF does better than the balance for comparisons across countries, and a failure probability better than a single level for risk. The guide of section 7 holds only within these limits.

## 9. Conclusions, data and code availability

### 9.1 The answer

How much of the spread the inputs account for depends on where the line between input and method is drawn. With the productivity basis counted as part of each method, equalising the inputs closed 4.1% of the distance between the methods and the corrected model, and the spread among method centres did not narrow. Counted as an input, it closed 38.5% and narrowed that spread by about a third (section 5.11). With the footprint and HALF at Australia's own productivity, the aggregate methods read about 1.6 to 5 times the model, not three to eight, and relaxing the pairing of pasture-fed food with crops alone brings the model to 81.7 million, above HALF and footprint build 1, 93% of the way to build 3 and below the footprint's top reading of 117.0 (section 5.14). The implementations reproduce Henry and Godden's figures within rounding and the thesis's exactly, HALF and Simpson's pasture in part, and not Simpson's feed cropland on the thesis rates, plant-food cropland or crop-plus-pasture total, or people per hectare (section 5.2; Table S6).

### 9.2 One model under each definition

Across the weather allowance and avoidable waste, one model on one data set spans 18.9 to 55.3 million on the corrected method, and reaches 62.9 million with the improved settings; counting exports takes the published figures to 100 million. Across the settings varied here, the answer moves by a factor of 1.58 (5th to 95th percentile; 2.22 from lowest to highest draw), narrower than that span.

### 9.3 The implication for practice

Choose the method by purpose, as section 7 sets out. Report the twelve items of the checklist (Table S4) with every capacity figure. Distrust one given without its definition.

### 9.4 Data and code availability

The model, its frozen releases, the data pipeline, the scripts that built every table and figure, and the claims and sources registers are in the repository github.com/MurrayLane/carrying-capacity-dashboard. The releases used are 2025-mirror, 2025-fixed and 2025-improved, identified by hash in `results/releases.json`, and each table names the file it was built from. Code is under the MIT licence; the model workbook, default inputs, 2011 baseline and analysis outputs are under CC BY 4.0, and source data keep their publishers' licences (`LICENSE-DATA.md`). On 18 November 2026 the archive has no DOI and the author has not deposited it on Zenodo.

### 9.5 Competing interests

The model tested here is the author's own. It was run on the same data and checked against its own published figures, as the other methods were. It was also the reference of the comparison and the instrument of section 6, which no other method was, and its ratings in Table 9 are the author's judgement (section 7.1).

---


## Declaration of generative AI and AI-assisted technologies in the writing process

During the preparation of this work I used Claude (Anthropic; the Opus [model name and version: author to enter from the account's usage history] and Sonnet [model name and version: author to enter] models) in the Claude Code agent environment to rebuild and run the model and its analyses under my direction, to retrieve and read sources, to check every number and citation by independent re-derivation, to draft text from my outline and the verified registers, and to simulate referee review. I set the question, the methods and every decision on them, and approved each verified result myself. After using these tools, I reviewed and edited the content as needed and take full responsibility for the content of the published article.

## Declaration of competing interests

The model tested in this paper is my own: I built it for my doctoral thesis and the papers that followed. It was tested by the same procedures as every other method, and the paper says where it is the exemplar (sections 7.1 and 9.5). I have no other competing interests to declare.

## Funding

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## CRediT authorship contribution statement

**[Author name]:** Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Resources, Data curation, Writing (original draft), Writing (review and editing), Visualization, Project administration.


---

## Appendix: drafter notes (not for the paper)

### From B_s01-03.md
## Drafter notes (not for the paper)

**What could not be sourced and was left out.**
1. Three works were not reached at page level, or have no file (B85). The scope says cite only if read or fetched, so they are left out and not named here (B126b: naming them in these notes put them in the reference list).
2. Section 3 point 3: no csv holds the selection record (scope gap 1), so the counts by route (found, read, cited, excluded) are not given and the optional table is not placed. The routes are named without counts. Point 3 and the reading-label paragraph will need the counts once the record exists.
3. Section 2 has claims rows only for the van den Bergh and Rietveld figures (B334 to B336, B108); no other figure from a concept source is quoted. Cohen's range of world estimates and Herrington's closest-fit counts (CT 7, BAU2 6) are given in words only.
4. Rows of `harmonisation.csv` with no claims row or a weak route were left out of Table 1: the NFF (B163, unverified; scope section 6 drops it). Griffith Taylor, Borrie and the National Population Council are in Table 1, from the Jones committee report (B100). Also left out: the footprint ratios (section 4 and 6 material) and Peters et al. 2016 (United States). The Migration Committee's 10 to 480 million is in the prose only, because neither Table 1 csv holds it.
5. Van den Bergh and Rietveld 2004 (scope gap 2): L245, read on the scan and cited in section 2 (B108), world scale only; the 7.7 billion median is of its method-based estimates.
6. The Simpson footprint and the HALF index are described but not named by author in section 1, because their register rows were not in the section 1 source table.
7. Figures: none are planned for sections 1 to 3, and none were placed.

**Conflicts named, not resolved.**
1. The brief says the section 3 selection rule is "decision 57". Decision 57 is the section 4 renaming of the diet-optimisation family. The selection rule is decision 42, which the scope cites. This draft follows decision 42.
2. Scope section 1 point 1 asks for the Jones figure "as summarised in the thesis", but V31b and X120 found the thesis has no 30 to 35. The draft quotes the report itself (para 2.16, p. 40; B99, B100) and the thesis summary is not used.
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

**B101 reframing for Ecological Economics (decision 93).** The abstract and section 1's closing paragraphs lead with the method finding; the 'follows the 2010 review' sentence is replaced by the relationship decision 93 states; section 2 cites Wackernagel and Rees 1996 (L050) and Lenzen and Murray 2001 (L022) for the footprint lineage. Repeats cut in sections 1, 2 and 3. No number was changed, added to or removed from any claims row; rows were renumbered where sentences moved, and new rows carry only wording claims or numbers already registered elsewhere in the paper. The record, with every passage before and after, is `qa/reports/B101_paperB_for_EE.md`.

**B109 trim (decision 92).** Prose cut from 8,290 to 7,949 words by `qa/tools/wordcount.py B`. In these sections: four tightenings in sections 1 and 2 (no sentence moved or cut; no number changed). The record is `qa/reports/B109_paperB_trim.md`.

**B118 revision (decisions 105 to 111, 115, 118, 119).** Abstract rewritten (250 words or fewer): both classifications of the productivity basis, the local-productivity readings primary, five published methods plus the model read two ways, the widened range, the factor of 10.6 dropped. Section 1: the factor of 10.6 and the Bellotti sentence (Table 1 holds the figure) cut; the closing paragraph states the 4.1% and 38.5% shares; the "not seen" parentheticals are out of the prose (the claims csvs carry the reading label; the literature register is the record, and B119 reconciles it). Section 2: Gilland's sentence, Price's example, the van den Bergh and Rietveld second sentence, Montoya and Herrington moved to supplementary S1. Section 3.1 states that a work with no file is cited as reported or from its abstract. Table 1's caption and note are set in the caption form ("Table n.") the word counter treats as captions. No uncited work is named by register id here.

**B126b patch (V45b).** Abstract: the data wording (the model on its own 2025 layer), the span sentence (weather and waste, figures unchanged under decision 118), "narrative critical review" and "Analysts" for the word cap. Section 1: the Jones committee named in full at first use; the sentence on the implementations cut (abstract and 9.1 carry it). Table 1: Taylor 1922 only (the 1937 figure is a date in the report's note 13), the National Population Inquiry (Borrie), the National Population Council kept at 1992 (note). Section 3.1 says "cited through a held work". Claims rows: Treasury, Centre for Population, and the labels of L012 to L014 and L073 (read, B119). The record is `qa/reports/B126b_patch_paper_B.md`.


### From B_s04-05.md
## Drafter notes (not for the paper)

Job D03, sections 4 and 5. Claims are in `papers/B_methods/draft/B_s04-05_claims.csv`. Page numbers were read from the files on disk under `/home/user/carrying-capacity-models/`, not copied from the register.

**Could not source, so left out or left as a placeholder.**
1. Table 2 and Figure 1 (the catalogue): no catalogue csv or script exists (scope section 4, gap 4). Placeholders only; no table was hand-typed.
2. Figure 2: no plotting script over `cross_method.csv` and `harmonised_comparison.csv` (scope section 5, gap 4). Placeholder only.
3. Supplementary Table S1 (fidelity checks and gap attribution): no script assembles it. The prose points to it and names `gap_attribution.csv`.
4. Section 4 families with no claim row (foodshed, footprint critique and defence, integrated, optimisation, water-bounded; scope section 4, gap 5): described from the literature register's `what_taken` only, and kept free of numbers. Figures I could not page-check on disk were dropped: the 42 diets of Peters, Wilkins and Fick 2007, the scenario counts of Hatfield-Dodds et al. 2015, Bryan et al. 2016 and Gao and Bryan 2017, and the four boundaries of Gerten et al. 2020 (no file).
5. No method paper for the stocks-and-flows framework (scope section 4, gap 2): the prose says the framework is described from Foran and Poldy 2002 alone.
6. Left out for the word budget or the cross-paper rules: Fearnside's protein and cash standards (B122); the wool and plant-crop test readings (README); the energy land of 0.43 ha (B047); the grain-direct reading of 486 million (B152); Foran and Poldy's population paths (Table 1.1, p. 31); HALF's fall from 2011 to 2021-23 (B067) and the 2011 failure probability (B131), both 2011-to-2025 material for Paper A (X-11); the thesis's 9.4 million (B160), which is 2011 data (X-10, X-11); the unverified author figures B009, B011 and B031.

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

**B101 reframing for Ecological Economics (decision 93).** Section 4.5 adds Wackernagel and Rees 1996 (L050) to the footprint's lineage. Repeats cut in 4.8, the section 5 opening, 5.7, 5.8 and 5.9. No number was changed, added to or removed from any claims row; rows were renumbered where sentences moved, and new rows carry only wording claims or numbers already registered elsewhere in the paper. The record, with every passage before and after, is `qa/reports/B101_paperB_for_EE.md`.

**B109 trim (decision 92).** Prose cut from 8,290 to 7,949 words by `qa/tools/wordcount.py B`. Section 4: the opening's one-line-each sentence cut (4.11 does it), the three land classes left to 6.4, HALF and Cassidy recipe detail and Fearnside's simulation sentence moved to S2.6 and S2.10. Section 5: implementation detail moved to S3 (5.1 vintage, ABS holdings and FAO head count; 5.4 further sources; 5.5 FAOSTAT series and second build; 5.6 second build; 5.12 Australia's HALF residual), 5.12's Simpson sentence cut (S3.7 carries it), 5.9's second sentence cut (Table 4 carries it), 5.4's explanation of the high readings cut (4.5 and 5.11 carry it). No number was changed; section 5 claims rows were renumbered (5.8's Jones row 44a is now 42a) and moved rows carry a B109 note in `supplementary_claims.csv`. The record is `qa/reports/B109_paperB_trim.md`.

**B118 revision (decisions 105 to 111, 115, 118, 119).** Sections 5.1 (bases; the one-population sentence corrected), 5.2 (the three grades), 5.4 to 5.6 (fidelity restated from `fidelity.csv` as V42 and the B122 amendments leave it), 5.9 (Table 4 carries the widened range for the corrected release; the other two rows keep the 13-setting range, not rerun), 5.10 (local-productivity readings primary; Table 3 gains a world-average column and a grade column), 5.11 (both classifications, formula, three references, Table 5a), 5.12 (the 5% rule), and new 5.13 (intake basis) and 5.14 (pairing test, Table 7). Main-text tables are numbered 1 to 9 in order of appearance after Table 5: the harmonised comparison under both classifications is Table 6, the pairing test Table 7, the design choices Table 8 and the purpose matrix Table 9 (the notes above this paragraph use the older numbers). Moved to the supplement: the footprint's printed Australian remainder (S2.5), the harvest-matching sentence (S3.4), the failure-view assumption (S3.6), the fish caution (S3.5). Cut: the foodshed sentence, the Shepon and Ridoutt 2017 sentences (S2.2 and S2.3 hold them), the Gifford founding-work sentence (S2.2 holds it), the "What it hides" line (S3.1 holds it). Variant 3's 172.31 was not reached by V40 and is flagged unverified in the claims csv; it is kept out of the abstract and highlights. Cassidy's people per hectare are graded not reproduced, as `fidelity.csv` stands after B122; the brief's wording said partly (decision row in the B118 report). Table notes are set in caption form.

**B126b patch (V45b).** Table 4 moved below Table 3 (tables in order of appearance); Figures 1 and 2 cited in the prose; Table 3 and Table 5 print the csv values for people per hectare (190 on all cropland, input factor 0.59), with the harvest-matched 183 named in S3.4 and the Table 5 note: this replaces drafter conflict item 2 and the B276 note above. Simpson feed cropland is 21.6% as `fidelity.csv` prints it. Captions name the widened range file and the csvs that need regenerating. 5.8 and 5.12 and the Jones sentence reworded; 5.5 points to Table S6 for the other countries. The record is `qa/reports/B126b_patch_paper_B.md`.

**B129 patch (decisions 122 to 129).** Tables 3 and 4 carry the improved widened range (37.9 to 60.0; 15.7 to 22.1; 18 settings, 2,000 draws; checker pending V46); the mirror row keeps its 13-setting range because no widened mirror run exists. Variant 3 (172.31) is out of 5.14 and Table 7, and the claims rows for it are removed; the README keeps it. The Cassidy and delivered-share gradings and the 18.9 to 55.3 wording were checked and already read as decisions 122 and 128 set them. `cross_method_local.csv` still prints the 13-setting improved range.


### From B_s06-09.md
## Drafter notes (not for the paper)

**What could not be sourced and was left out.**
* NFF "feeds 75 million" (B163, L011): untraced; dropped rather than cited through L229 (scope gap 7, decided at drafting).
* One "about 3.4 times" factor from a report with no text layer: the factor is derived, not printed, so the factor and the report are left out and not cited.
* Farm diesel share 84% (decision 53): no claims-register row; stated without the number.
* Kastner et al. 2012, Roos et al. 2017, van Zanten et al. 2016, Ridoutt et al. 2020, Tilman and Clark 2014 (section 6 rows), Peters et al. 2016 diet land range (B202), Khorsandi et al. 2023, Kastner Oceania variability, Fearnside 1990 in section 6, and two further works that are not cited: left out to keep to the word budgets or because no page-checked figure was needed. One of the two was left out for a sourcing reason (an accepted manuscript unchecked).
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

**Flags.** "[gate 4]": B084 (183, B93) in 7.3 and B277 (12 to 343 as run, B92b statement) in 9.1 (9.2 before B101). B083 and B156 carry gate 4 notes on wording only; the draft does not use the words that change. "[open: Q8]": the span is quoted as B003 (18.9 to 55.3 million by definition alone, corrected) with 62.9 for the improved settings, in 6.10 and 9.2 (9.1 before B101); "a factor of 4" is not used, and 4.03 appears only as a ladder step. "[open: Q9]": 100 million kept, with the parts' sum of 90 stated at first use (6.1).

**Register rows touched:** none.

**B98b cut (decision 92).** The main text was cut to under 8,000 words of prose with detail moved to `supplementary.md` (sections S1 to S6, Tables S1 to S4); its claims are in `supplementary_claims.csv`. Table numbers in the notes above are those of the first draft: old Tables 7, 8 and 10 are Tables S2, S3 and S4, and old Table 9 is Table 7. Sentence numbers in the claims csvs were renumbered on the cut text. The record of what moved, merged or was cut is `qa/reports/B98b_cut_paper_B.md`.

**B101 reframing for Ecological Economics (decision 93).** Section 9.1 leads with the method finding (old 9.2 merged into it); the old 9.1 is 9.2, "One model under each definition"; 9.3 is "The implication for practice". Repeats cut in 6.6, 7.2 to 7.5, 8.4 and 8.6. No number was changed, added to or removed from any claims row; rows were renumbered where sentences moved, and new rows carry only wording claims or numbers already registered elsewhere in the paper. The record, with every passage before and after, is `qa/reports/B101_paperB_for_EE.md`.

**B109 trim (decision 92).** Prose cut from 8,290 to 7,949 words by `qa/tools/wordcount.py B`. Sections 6, 8 and 9: tightenings only, plus two repeats cut (6.2's default-diet land, which Table S2 carries; 6.10's factor of 1.26, which 6.9 states). Section 7 was not touched: it is at 469 words, below its 70% floor of 630, before and after this job. No number was changed. The record is `qa/reports/B109_paperB_trim.md`.

**B118 revision (decisions 105 to 111, 115, 118, 119).** 6.9 states the rule separating definitions from settings, the widened range (2,000 draws, 19 settings, 18 vary), the indices and the six judged settings; "defensible" and "only" are out; 6.10 and 6.11 compare 1.58 with each definitional row (it is above the land base, waste and the Australian settings, below the rest). Decision 118's span by definition (18.9 to 55.3; 62.9) stands as decided; V41 notes that the new rule treats the waste-to-zero row (55.3) as a setting and that corrected definition rows reach 15.5, a tension left for the coordinator. 7.1 publishes the rubric (supplementary S7), discloses the second rating (a blind checker session of an AI model; 25 of 28; three differences adopted) and counts five published methods plus the model read two ways; Table 9's last two columns (Table 7 in the earlier numbering) are one model. 7.6, 8.4 (the fixed diet), 8.6, 9.1, 9.2 and 9.5 rewritten. Moved to supplementary S8: the pasture shares of the footprint studies, the waste goal and baselines, New York State's 2.03 Mha, Willett's 0 to 2%, the farm-diesel and bioenergy sources, the audit of constants, the correlated wheat years, the Fader sentence and the parliamentary inquiry. Table 8's last row (Table 6 in the earlier numbering) now reads 31.1 to 49.2 (1.58). The second-rating paragraph starts "The matrix in Table 9" so that the counter counts it as prose.

**B126b patch (V45b).** 6.9 and 6.10 state the rule and that waste is a setting under it (decision 118 figures unchanged; decision row for Murray); ladder, 7.1 (eight ratings), 7.3, 7.5, 7.7, 8.5, 8.6, 9.1, 9.2 and 9.4 corrected as the read lists them; the flags "[gate 4] B084 in 7.3" and "145 to 183 million" above are stale (7.3 no longer quotes them). The declarations are in `B_s10_declarations.md`. The record is `qa/reports/B126b_patch_paper_B.md`.


### From B_s10_declarations.md
## Drafter notes (not for the paper)

Source: `papers/DECLARATIONS.md` sections 1, 3, 4 and 5 (B121), inserted in B126b as the journal's sections after the conclusions. Open for the author: the model names and versions (bracketed above); the heading, to be checked against the journal's guide at submission; the "doctoral thesis" wording, funding and the CRediT roles (B121 "The author must confirm or change", items 1 to 7); the author name and affiliation, left blank by design. Section 9.5 stays as the in-text statement; the "(sections 7.1 and 9.5)" in the competing-interests paragraph is the one addition to the DECLARATIONS.md text. This file holds no number, so it has no claims csv; the word counter skips it because it sits outside the numbered sections.
