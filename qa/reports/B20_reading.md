# B20: remaining sweep candidates read into the register

Register rows added: L091 to L131 (`qa/literature_register.csv`, 41 new rows, CRLF and all 12 columns kept, existing rows untouched). No PDF was placed in a repository; copies were read as text in the scratch folder `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/b20`.

## Counts

| Status | Works |
|---|---|
| read (full text opened) | 11 |
| abstract only | 21 |
| record only | 9 |
| not reached (nothing at all) | 0 |
| Total | 41 |

The 41 works are the rows of `qa/reports/B14_literature_sweep.csv` not in the register by DOI or title. Where a "read" text is an accepted manuscript or an XML copy of the article, the entry says so. The web was not refused for more than ten works in a row, so the stop line was not reached.

## What "read" means here

* `read`: Hadjikakou 2017, Ridoutt et al. 2020, Hendrie et al. 2014, Productivity Commission 2011, Fader et al. 2013, Cohen 2017, Tucker 2020, Muller et al. 2017, Bajzelj et al. 2014, Schader et al. 2015, Wiedmann and Lenzen 2018.
* `abstract only`: the abstract was read from the OpenAlex, Crossref, Europe PMC or RePEc record; the full text sits behind a paywall or a publisher host that refused (see the last section).
* `record only`: no abstract could be reached; the entry rests on title, venue and the B14 note, and says so.

## 1. Australian works

### L091: Graymore

* **Citation:** Graymore, Sipe and Rickson 2010, Ecological Economics 69(3): 459-468, "Sustaining Human Carrying Capacity: A tool for regional sustainability assessment". https://doi.org/10.1016/j.ecolecon.2009.08.016
* **Read:** abstract only
* **What it estimates or argues:** Proposes the Sustaining Human Carrying Capacity (SHCC) framework, which judges the sustainability of regional human activity by the pressure those activities put on regional ecosystems. It follows the authors' own earlier test of existing sustainability tools at regional scale, which found global, national and state tools not effective at that scale. SHCC was tested at regional scale (the sweep record places it in South East Queensland).
* **Method family:** index
* **Numbers:** None in the abstract. No population or land figure for any Australian region could be taken.
* **Use in the methods paper:** Catalogue (index family) and context for section 2: an Australian regional use of the phrase "carrying capacity" for a planning tool, not a people-count.
* **Lane:** Not told. Only the abstract (RePEc page) was read.
* **Note:** Abstract text from the RePEc (IDEAS) page. Publisher page not tried. Online 2009, issue date January 2010.

### L092: Candy et al. 2019

* **Citation:** Candy et al. 2019, Economia Agro-Alimentare (2019)(3): 371-399, "Quantifying Melbourne's Foodprint: a scenario modelling methodology to determine the environmental impact of feeding a city". https://doi.org/10.3280/ecag2018-003007
* **Read:** abstract only
* **What it estimates or argues:** A city-scale scenario model (the Australian Stocks and Flows Framework) of the land, water, food waste and emissions needed to feed Greater Melbourne, run for 2014 and 2050. It is a demand-side requirement for a city, not a capacity of a region. The abstract says it forms part of a larger Foodprint Melbourne project on the foodbowl.
* **Method family:** scenario model
* **Numbers:** Stated in the abstract: 758 gigalitres a year of water and 16.3 million hectares a year of land to feed Melbourne in 2014; in 2050, 1,598 gigalitres (an increase of 111%) and 32.3 million hectares (98%). The abstract does not give the population or whether the hectares are all in Victoria, so no per-person figure can be derived without the full text.
* **Use in the methods paper:** Comparator for the land-per-diet side of a city (section 4 scenario model) and for section 6 (scale): a requirement figure to set beside a capacity figure for the same food.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. Full text is closed access. The 16.3 Mha figure is large for one city; check what land it counts (grazing, imports) before using it.

### L093: Lee 2013 (review of an edited volume)

* **Citation:** Lee 2013 (review of an edited volume), International Journal of Agricultural Sustainability 12(4): 490-491, "Food security in Australia. Challenges and prospects for the future". https://doi.org/10.1080/14735903.2013.835901
* **Read:** record only
* **What it estimates or argues:** The record is a two-page book review of an edited volume of Australian food security research by 68 contributors, not an original study. Only the opening of the review text (introduction and the first part headings) is on the record. The B14 sweep listed it as a study of "challenges and prospects"; it is the review of the volume.
* **Method family:** concept review
* **Numbers:** None.
* **Use in the methods paper:** Context only; the volume itself, not this review, would be the source to cite for Australian food security.
* **Lane:** Not told (record only).
* **Note:** OpenAlex record shows 200 characters of text and the page range 490-491. No open copy found.

### L094: Millar and Roots 2012

* **Citation:** Millar and Roots 2012, International Journal of Agricultural Sustainability 10(1): 25-39, "Changes in Australian agriculture and land use: implications for future food security". https://doi.org/10.1080/14735903.2012.646731
* **Read:** abstract only
* **What it estimates or argues:** A qualitative review of what changes in Australian farm numbers, land use and ownership, water rules, input costs, farm labour and climate mean for food security, using current information and scenarios. It starts from a projection of 35 million people by 2050. It concludes that Australia will keep producing enough food for domestic and export markets in the short term, and that longer-term food security is threatened by climate impacts, poor planning controls over urban and mining use of productive land, labour shortages and low farm research spending.
* **Method family:** concept review
* **Numbers:** The 35 million by 2050 projection is a premise, not a result. No people-count or land figure in the abstract.
* **Use in the methods paper:** Context for section 4 and 6 (what limits Australian capacity beyond land area: land loss to urban and mining use, water, labour); supports the point that area alone does not set the number.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. A green copy sits at the CSU repository; it returned 403 (bot block). That host was not retried.

### L095: Hadjikakou 2017

* **Citation:** Hadjikakou 2017, Ecological Economics 131: 119-128, "Trimming the excess: environmental impacts of discretionary food consumption in Australia". https://doi.org/10.1016/j.ecolecon.2016.08.006
* **Read:** read
* **What it estimates or argues:** Uses environmentally extended input-output analysis (Eora) on household expenditure and the Australian Health Survey to estimate what share of the life-cycle impact of Australian diets comes from discretionary foods (alcohol, baked goods, confectionery and condiments, sugary drinks, processed meat). It is a footprint study of what is eaten, not a capacity study.
* **Method family:** footprint
* **Numbers:** Discretionary foods are 39% of food life-cycle energy use, 35% of water use, 35% of the ecological footprint (global hectares) and 33% of food-related greenhouse gas emissions (results section). The abstract labels the four shares "water use, energy use, carbon dioxide equivalent and land use" as 35, 39, 35 and 33, which does not match the results text, which has GHG at 33% and the footprint at 35%. The footprint is all land types plus carbon uptake land, not cropland.
* **Use in the methods paper:** Context for section 6 (diet assumption): roughly a third of the impact of an Australian diet is discretionary food, so the diet assumed moves any land-per-person figure. Do not quote its "land use" share.
* **Lane:** No (no hit for Lane in the text; it does not use the phrase carrying capacity).
* **Note:** Full text is the accepted manuscript from the UNSW repository (open copy); the page numbers and layout are the manuscript's. The abstract and the results text disagree on which indicator carries the 33% (see numbers); use the results text.

### L096: Ridoutt et al. 2020

* **Citation:** Ridoutt et al. 2020, Nutrients 12(5): 1212, "Cropland Footprints of Australian Dietary Choices". https://doi.org/10.3390/nu12051212
* **Read:** read
* **What it estimates or argues:** Life cycle assessment of three cropland footprints (scarcity, biodiversity, malnutrition) for the diets of 9,341 adults in the 2011-12 National Nutrition and Physical Activity Survey. Cropland is expressed in m2 year-equivalents of cropland of global average productivity. Compares each diet with a cropland target set from the proposed planetary boundary for cropland.
* **Method family:** land per diet
* **Numbers:** Mean cropland scarcity footprint 7.1 m2 yr-e per person per day, against a target of 6.1 (the text gives 2,226 m2 per person per year, from 15% of ice-free land shared among 9 billion people). Higher-quality, lower-footprint diets need 4.2; recommended diets built from that group need 5.9. Discretionary foods contribute most, then fresh meat and alternatives, breads and cereals. About 45% of the spread between people is explained by energy intake. The 7.1 figure is about 2,590 m2 a year (calculated here, 7.1 times 365), on cropland of global average productivity, so it cannot be turned into a count of Australians without an Australian productivity factor.
* **Use in the methods paper:** Comparator for the diet assumption (section 6) and context for the Australian land-per-diet family (section 4): the one Australian per-person cropland figure in the batch, with a planetary-boundary target that is a different rule (fair share) from a land-supply capacity.
* **Lane:** No (no hit for Lane; no use of carrying capacity).
* **Note:** Full text from Europe PMC (PMC7282022, the open XML copy); the MDPI host refused (403) and was not retried.

### L097: Hendrie et al. 2014

* **Citation:** Hendrie et al. 2014, Nutrients 6(1): 289-303, "Greenhouse Gas Emissions and the Australian Diet: Comparing Dietary Recommendations with Average Intakes". https://doi.org/10.3390/nu6010289
* **Read:** read
* **What it estimates or argues:** Joins an environmentally extended input-output model of the Australian economy to food intake from the 1995 National Nutrition Survey to estimate the greenhouse gas emissions of the average Australian diet and of diets that follow the Australian Dietary Guidelines. It is a diet footprint study with no land or capacity result.
* **Method family:** footprint
* **Numbers:** Average diet 14.5 kg CO2e per person per day; recommended dietary patterns about 25% lower; red meat 8.0 kg and non-core foods 3.9 kg CO2e a day (27% of diet emissions).
* **Use in the methods paper:** Context only for section 6 (diet assumption): shows how far an Australian diet can move by composition. Not a capacity method.
* **Lane:** No (no hit for Lane).
* **Note:** Full text from Europe PMC (PMC3916862). Intake data are from the 1995 survey, which Hadjikakou 2017 notes as an older edition.

### L098: Bryan et al. 2014

* **Citation:** Bryan et al. 2014, Global Environmental Change 28: 166-181, "Supply of carbon sequestration and biodiversity services from Australia's agricultural land under global change". https://doi.org/10.1016/j.gloenvcha.2014.06.013
* **Read:** abstract only
* **What it estimates or argues:** Uses a simplified version of the Land Use Trade-Offs (LUTO) model with a global integrated assessment model to estimate how much carbon storage and biodiversity service the intensive agricultural land of Australia could supply from 2013 to 2050 under four global outlooks, given a carbon price and a biodiversity payment. Food demand is one input to each outlook; food capacity is not the output.
* **Method family:** scenario model
* **Numbers:** Carbon supply in 2050 from 0 to 189 MtCO2 a year depending on outlook; sharp rise above a carbon price of about 50 dollars a tonne in 2015 and 65 in 2050. No people-count or food figure.
* **Use in the methods paper:** Context for section 4 (scenario model): shows the main Australian land-use model is used for carbon and biodiversity competition for farmland, which is the land-competition reason a fixed 2025 land base is a design choice.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the Crossref record. The figshare copy returned an empty reply (202) and was not retried. Bryan 2016 (L076) is the closer comparator.

### L099: Productivity Commission 2011

* **Citation:** Productivity Commission 2011, A 'Sustainable' Population? Key Policy Issues, roundtable proceedings, 21-22 March 2011 (Canberra). https://www.pc.gov.au/inquiries-and-research/sustainable-population; PDF https://assets.pc.gov.au/research/supporting/sustainable-population/sustainable-population-proceedings.pdf
* **Read:** read
* **What it estimates or argues:** Proceedings of a government roundtable on whether Australia's population has limits, with 13 chapters and discussant comments; the session on limits has a chapter by Don Henry of the Australian Conservation Foundation on environmental and resource constraints. The chairman's introduction argues for attention to "absorption capacity" (a dynamic idea about rate of change) instead of static "carrying capacity", and says outcomes two or three decades out are close to impossible to predict (the last two Intergenerational Reports differed by 8 million people).
* **Method family:** concept review
* **Numbers:** Henry cites a Victorian EPA 2008 estimate of Australia's footprint of 7.8 global hectares per person against 2.1 the planet regenerates, 2.8 times the global average, and half of it from carbon dioxide. The background chapter quotes Doctors for the Environment Australia asking that population numbers rest on "the ecological carrying capacity of Australia". The proceedings give no carrying capacity number and no food-based estimate. The 36 million population projection in the third Intergenerational Report is the premise.
* **Use in the methods paper:** Context for section 2: how Australian government economists frame the concept (rejecting a static target in favour of rate of change) and where a footprint is used as the capacity stand-in.
* **Lane:** No (no hit for Lane in the 98,000 words of the proceedings).
* **Note:** Full 3.8 MB PDF opened (assets.pc.gov.au) and read as text in the scratch folder; no copy kept in the repository. Origin page: https://www.pc.gov.au/inquiries-and-research/sustainable-population

### L100: CSIRO Futures 2019

* **Citation:** CSIRO Futures 2019, Australian National Outlook 2019: Australia 2060 (CSIRO with NAB and more than 20 partners). https://www.csiro.au/en/news/All/News/2019/June/Australia-2060-Our-crossroads-today-future-prosperity-or-slow-decline
* **Read:** record only
* **What it estimates or argues:** Second national outlook, to 2060, comparing a "Slow Decline" with an "Outlook Vision" through five shifts (industry, urban, energy, land, culture). The land shift is described as investing in food and fibre industries, finding new profitable land uses, and building climate resilience. Only the 18 June 2019 CSIRO news release was opened; the report and technical report were not.
* **Method family:** scenario model
* **Numbers:** From the news release: GDP per person up to 36% higher in the Outlook Vision than Slow Decline in 2060; net zero emissions by 2050. No land, food or people-count figure on the page.
* **Use in the methods paper:** Context for section 4 (scenario model), alongside the 2015 outlook (L090); the news release gives nothing for a capacity range.
* **Lane:** Not told (record only).
* **Note:** News release read at csiro.au (the first address in the sweep file returned 404; the Title-case address worked). The report link csiro.au/ano returned 503 and was not retried.

## 2. Foodshed and local-capacity works

### L101: Peters et al. 2009 (online 2008)

* **Citation:** Peters et al. 2009 (online 2008), Renewable Agriculture and Food Systems 24(1): 1-7, "Foodshed analysis and its relevance to sustainability". https://doi.org/10.1017/s1742170508002433
* **Read:** abstract only
* **What it estimates or argues:** A short framing paper arguing that foodsheds, the geographic areas that feed population centres, give a tool for relating where food is produced to where it is eaten, so that energy efficiency and vulnerability of the food system can be judged. It sets up the Peters group method used in the 2009 New York paper (L077).
* **Method family:** land per diet
* **Numbers:** None in the abstract.
* **Use in the methods paper:** Catalogue (foodshed entry) and context for section 4 and 2: the foundational statement of the foodshed idea.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. Print issue is 2009 (24(1)); the sweep and Crossref online date give 2008. Full text closed access.

### L102: Horst and Gaolach 2014 (issue 2015)

* **Citation:** Horst and Gaolach 2014 (issue 2015), Renewable Agriculture and Food Systems 30(5): 399-407, "The potential of local food systems in North America: A review of foodshed analyses". https://doi.org/10.1017/s1742170514000271
* **Read:** abstract only
* **What it estimates or argues:** Reviews 22 foodshed analyses done in the USA and Canada between 2000 and 2013, comparing their authorship, spatial extent, goals, consumption and production methods, data, and findings. It finds significant room for relocalising food systems, and lists a research agenda including more standard models for production, consumption and pathways.
* **Method family:** concept review
* **Numbers:** 22 studies reviewed; the abstract gives no capacity percentages.
* **Use in the methods paper:** Catalogue and critique for section 4: a published review that shows foodshed studies differ in method and need standard models, which backs the paper's case for naming the method with every number.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. Full text closed access.

### L103: Zumkehr and Campbell 2015

* **Citation:** Zumkehr and Campbell 2015, Frontiers in Ecology and the Environment 13(5): 244-248, "The potential for local croplands to meet US food demand". https://doi.org/10.1890/140246
* **Read:** abstract only
* **What it estimates or argues:** Spatially explicit estimate of how much of US food demand the existing cropland could meet through local food networks, simulated for 1850 to 2000 across a range of diets, food waste, population distribution, cropland area and yields. Finds that local potential has declined over time, but that the current potential is large.
* **Method family:** land per diet
* **Numbers:** Up to 90% of national food demand could be met from existing US cropland through local networks (the stated upper potential).
* **Use in the methods paper:** Comparator for section 5 and 6: an upper-bound share figure whose size depends on the diet and waste assumed; not Australian.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. The green copy (doi 10.58079/aud4, OpenEdition) returned a bot-check page; not retried.

### L104: Kurtz et al. 2020

* **Citation:** Kurtz et al. 2020, Environmental Science & Technology 54(19): 12434-12446, "Mapping U.S. Food System Localization Potential: The Impact of Diet on Foodsheds". https://doi.org/10.1021/acs.est.9b07582
* **Read:** abstract only
* **What it estimates or argues:** Models the biophysical capacity of regional food systems from agricultural land area and productivity, population and seven diet scenarios from current consumption to vegan, for 378 US metropolitan centres in a closed national system that favours local supply. Reports foodshed size as weighted average distance and how many people could be fed within 250 km.
* **Method family:** land per diet
* **Numbers:** Foodshed distance 351-428 km for cultivated cropland, 80-492 km for perennial forage cropland, 117-799 km for grazing land. Within 250 km, 35-53% of the population on cultivated cropland, 39-94% on perennial forage, 26-88% on grazing land, by diet. All seven diet scenarios leave some land unused.
* **Use in the methods paper:** Comparator for section 6 (diet assumption): shows that the same US land supports very different shares of people depending on the diet; supports the paper's grazing-land design choice.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. Full text closed access.

### L105: Fader et al. 2013

* **Citation:** Fader et al. 2013, Environmental Research Letters 8(1): 014046, "Spatial decoupling of agricultural production and consumption: quantifying dependences of countries on food imports due to domestic land and water constraints". https://doi.org/10.1088/1748-9326/8/1/014046
* **Read:** read
* **What it estimates or argues:** Uses the LPJmL crop and water model with country consumption and trade data to find, for 11 major food and fodder crops, whether a country has enough land and water to produce on its own territory what its people consume in the base year, in 2000 and for three 2050 scenarios of productivity, cropland expansion and population. A country is over its boundary when the extra cropland or water needed for self-sufficiency exceeds what is available.
* **Method family:** commodity balance
* **Numbers:** In 2000, 66 countries could not be self-sufficient on land or water limits: 22 above the water boundary and 62 above the land boundary. About 16% of world population relies on trade. In the A2r scenario up to 5.2 billion people (51%) would depend on outside land and water by 2050. Available land and water globally: 1,322 million hectares and 17,953 cubic kilometres. Australia is not named in the text; results are by country in figures and the appendix, which were not opened.
* **Use in the methods paper:** Comparator and critique for section 5: a country land-and-water boundary against present diets with trade held out, near to the paper's land-boundary idea; it states it is not a projection.
* **Lane:** No (no hit for Lane). It cites Rees 1996 on area-based carrying capacity.
* **Note:** Full text opened: the open IOP PDF, from the OpenAlex location (read as text in the scratch folder). The Australia result is in figures that were not read.

## 3. Concept works

### L106: Cohen 2017

* **Citation:** Cohen 2017, The Journal of Population and Sustainability 2(1): 37-42, "How many people can the Earth support?". https://doi.org/10.3197/jps.2017.2.1.37
* **Read:** read
* **What it estimates or argues:** Short essay by the author of the 1995 book of the same name. Argues that human carrying capacity is a "specious metaphor" from wildlife and cattle management because people choose what and how much to eat, make, and consume, and because food is not the single limit people often assume. The scatter of published estimates is evidence that there is no single right answer.
* **Method family:** concept review
* **Numbers:** At least ninety further estimates since 1679 (van Leeuwenhoek: not more than 13.4 billion) range from under one billion to more than a billion billion billion, with no trend and rising scatter. Cereal output of about 2.5 billion tonnes could feed 10-12 billion people, but in 2015-16 only 43% fed humans, 36% animals and 21% other uses.
* **Use in the methods paper:** Context and critique for section 2: the strongest short statement that a capacity figure depends on named choices; supports reporting a range with named methods and not a single number.
* **Lane:** No (no hit for Lane).
* **Note:** Full text opened (open access PDF from the journal). Cohen 1995 (the book) sits in the library folder.

### L107: Tucker 2020

* **Citation:** Tucker 2020, The Journal of Population and Sustainability 5(1): 77-85, "We know how many people the earth can support". https://doi.org/10.3197/jps.2020.5.1.77
* **Read:** read
* **What it estimates or argues:** A comment that answers Cohen's question with one figure: the Earth's long-term ecological carrying capacity "optimistically" supports about 3 billion modern industrialised people, so humanity has long overshot it. The calculation is in the author's 2019 book and is not given in the article, which says the author will "forgo a defense" of it. The rest argues for lower fertility (a total fertility rate of 1.5 by 2030).
* **Method family:** footprint
* **Numbers:** 3 billion people at modern industrial living; world population peaking at 9.7 billion in 2064 under projections cited; the human footprint stated to be perhaps 10 times larger than the carbon footprint.
* **Use in the methods paper:** Context (a single-number claim, with the method outside the article) for section 2; useful as the contrast to Cohen. Not a method to catalogue because the article shows none.
* **Lane:** No (no hit for Lane).
* **Note:** Full text opened (open access PDF). The book A Planet of 3 Billion (2019) was not opened.

### L108: Qiu 2024

* **Citation:** Qiu 2024, "Carrying Capacity: Theory and Research Methods", chapter 1 of a Springer book on carrying capacity of resources, environment, population and economy in China. https://doi.org/10.1007/978-981-99-9046-7_1
* **Read:** record only
* **What it estimates or argues:** Chapter 1 of a Springer book on China's resource, environment, population and economy carrying capacity. By title and series, it sets out the theory and the research methods of the Chinese planning tradition. Nothing of the text was reached.
* **Method family:** concept review
* **Numbers:** None.
* **Use in the methods paper:** Context for section 2 and the index family in section 4 (the Chinese planning-index tradition that dominates the citing literature in B15); would need the chapter to be cited for any claim.
* **Lane:** Not told (record only).
* **Note:** Closed access; OpenAlex holds no abstract and no open copy was found.

### L109: Wang et al. 2022

* **Citation:** Wang et al. 2022, Land 11(4): 484, "Managing Land Carrying Capacity: Key to Achieving Sustainable Production Systems for Food Security". https://doi.org/10.3390/land11040484
* **Read:** abstract only
* **What it estimates or argues:** A review of the natural resources that limit food production and of options to feed 9 billion people in 2050 and beyond. It argues that measures must be region-specific because socioeconomic and natural carrying capacity differ, that urban expansion deepens arable land shortage in some regions, and that food trade also faces risks.
* **Method family:** concept review
* **Numbers:** None in the abstract.
* **Use in the methods paper:** Context for section 2 (the phrase "land carrying capacity" used for a review of limits to food production); not a method to catalogue.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. The MDPI host refused (403) and was not retried.

### L110: Ma 2017

* **Citation:** Ma 2017, AIP Conference Proceedings 1890: 040106, "Literature review on land carrying capacity of the coordinated development of population, resources, environment and economy". https://doi.org/10.1063/1.5005308
* **Read:** abstract only
* **What it estimates or argues:** A short literature review of the theory and research methods of land carrying capacity, framed by the Chinese population, resources, environment and economy approach. It treats land carrying capacity as an index for land resource evaluation and planning, and lists problems in the field.
* **Method family:** concept review
* **Numbers:** None.
* **Use in the methods paper:** Context for section 2 and 4 (index family): a statement of the Chinese land carrying capacity tradition.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record (765 characters). Full text closed access.

## 4. Diet and land works

### L111: Tilman et al. 2011

* **Citation:** Tilman et al. 2011, PNAS 108(50): 20260-20264, "Global food demand and the sustainable intensification of agriculture". https://doi.org/10.1073/pnas.1116437108
* **Read:** abstract only
* **What it estimates or argues:** Projects global crop demand in 2050 from the link between income and per-person demand for calories and protein, then compares two ways of meeting it: continued extensification in poorer countries with intensification in richer ones, or moderate intensification focused on under-yielding nations.
* **Method family:** scenario model
* **Numbers:** Crop demand up 100-110% from 2005 to 2050; about 1 billion hectares cleared under current trends against about 0.2 billion with focused intensification.
* **Use in the methods paper:** Context for section 6 (yield and demand assumptions that move any 2050 number).
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. The pnas.org copy returned 403; Europe PMC rendering returned 403. Not retried.

### L112: Smith 2013 (online 2012)

* **Citation:** Smith 2013 (online 2012), Global Food Security 2(1): 18-23, "Delivering food security without increasing pressure on land". https://doi.org/10.1016/j.gfs.2012.11.008
* **Read:** record only
* **What it estimates or argues:** By title and venue, a review of options to meet food demand without taking more land. No abstract was reachable.
* **Method family:** concept review
* **Numbers:** None.
* **Use in the methods paper:** Context for section 6 only if the full text is read.
* **Lane:** Not told (record only).
* **Note:** No abstract in OpenAlex, Crossref or Europe PMC; closed access.

### L113: Hunter et al. 2017

* **Citation:** Hunter et al. 2017, BioScience 67(4): 386-391, "Agriculture in 2050: Recalibrating Targets for Sustainable Intensification". https://doi.org/10.1093/biosci/bix010
* **Read:** abstract only
* **What it estimates or argues:** Argues that the usual claim that food production must double by 2050 is imbalanced, and sets quantitative mid-century targets for both production and environment. Finds that a rise of about 25-70% above current production may meet 2050 crop demand, while nutrient losses and agricultural greenhouse gas emissions must fall sharply.
* **Method family:** scenario model
* **Numbers:** Production need of +25-70% on current levels for 2050 crop demand.
* **Use in the methods paper:** Context for section 6: the range of 2050 demand claims, from +25% to double, is itself a source of spread.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. Full text closed access.

### L114: Schon and Bohringer 2023

* **Citation:** Schon and Bohringer 2023, Sustainability 15(11): 8675, "Land Consumption for Current Diets Compared with That for the Planetary Health Diet: How Much Land Does a Region Need?". https://doi.org/10.3390/su15118675
* **Read:** abstract only
* **What it estimates or argues:** Builds a framework to calculate land consumption in square metres per person for different diets, and applies it to Hesse, Germany, with attention to livestock. Finds that the region lacks the land to feed its present livestock population, but could support a smaller one on the planetary health diet, especially with crop rotation and more extensive husbandry.
* **Method family:** land per diet
* **Numbers:** No figure in the abstract; the result is stated qualitatively.
* **Use in the methods paper:** Comparator (land per diet) for section 4 and 6: a regional square-metres-per-person method with a healthy-diet variant, the same shape as the paper's diet side.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. The MDPI and preprints.org hosts both refused (403) and were not retried. The B14 title is shortened; the subtitle is as given by Crossref.

### L115: Poore and Nemecek 2018

* **Citation:** Poore and Nemecek 2018, Science 360(6392): 987-992, "Reducing food's environmental impacts through producers and consumers". https://doi.org/10.1126/science.aaq0216
* **Read:** abstract only
* **What it estimates or argues:** Meta-analysis of five environmental indicators over 38,700 farms and 1,600 processors, packaging types and retailers. Finds impact varies 50-fold among producers of the same product, and that the lowest-impact animal products typically exceed the impacts of vegetable substitutes.
* **Method family:** footprint
* **Numbers:** 38,700 farms; up to 50-fold spread between producers of one product.
* **Use in the methods paper:** Context for section 6 (diet assumption): the spread within one food is as large a lever as the choice of food, so a land-per-kilogram factor needs a named source.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. Closed access.

### L116: Roos et al. 2017

* **Citation:** Roos et al. 2017, Global Environmental Change 47: 1-12, "Greedy or needy? Land use and climate impacts of food in 2050 under different livestock futures". https://doi.org/10.1016/j.gloenvcha.2017.09.001
* **Read:** abstract only
* **What it estimates or argues:** Estimates global land use and greenhouse gas emissions of food in 2050 under four livestock futures (intensification, plant-based eating, artificial meat and dairy, and livestock fed only on ecological leftovers), each with a trend diet and a healthy diet, with variants for yield gaps and waste. Finds available cropland suffices only if animal products fall, yield gaps close by half and waste falls by half, or protein is replaced by hypothetical artificial products.
* **Method family:** land per diet
* **Numbers:** The leftovers-only scenario uses much less cropland and could supply 40-56 kg of red meat per person per year, with no fall in agricultural emissions on present levels.
* **Use in the methods paper:** Comparator for the grazing design choice in section 6: it treats pasture and food waste as a distinct feed source.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. The ScienceDirect link returned a bot-check page and was not retried.

### L117: van Zanten et al. 2016 (online 2015)

* **Citation:** van Zanten et al. 2016 (online 2015), International Journal of Life Cycle Assessment 21(5): 747-758, "Global food supply: land use efficiency of livestock systems". https://doi.org/10.1007/s11367-015-0944-1
* **Read:** abstract only
* **What it estimates or argues:** Defines a land use ratio for livestock systems: the human-digestible protein that food crops could make on the land used to grow the feed, divided by the human-digestible protein in the animal food. Illustrated with laying hens and dairy cows on sandy and peat soils. A ratio below 1 means the animal system makes more protein per square metre than crops would.
* **Method family:** land per diet
* **Numbers:** Laying hens 2.08; dairy cows 2.10 on sandy soil and 0.67 on peat soil.
* **Use in the methods paper:** Comparator and critique for the grazing design choice in section 6: land that cannot grow food crops is treated separately from arable land.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. Springer and WUR hosts returned a script or error page; not retried.

### L118: Muller et al. 2017

* **Citation:** Muller et al. 2017, Nature Communications 8: 1290, "Strategies for feeding the world more sustainably with organic agriculture". https://doi.org/10.1038/s41467-017-01410-w
* **Read:** read
* **What it estimates or argues:** Uses the SOL-model, a country-level mass-flow model of the global food system, to compare conversion to organic farming with the FAO reference for 2050, alone and together with cuts to food waste and to feed from arable land. A full organic conversion needs more land; with waste and feed reductions the land use stays below the reference.
* **Method family:** commodity balance
* **Numbers:** Reference 2050 cropland occupation +6% on 2005-09; full organic adds 16-33% for low to high yield gaps; with climate impacts the rise is up to +55% (no organic) and 71-81% (all organic) on the base year. Global only; Australia is not named in the text.
* **Use in the methods paper:** Context for section 6: shows how diet, waste and yield-gap assumptions together move land demand by tens of percent, the same sensitivity the paper reports.
* **Lane:** No (no hit for Lane).
* **Note:** Full text opened: the open Nature Communications PDF (nature.com), read as text in the scratch folder.

### L119: Clark and Tilman 2017

* **Citation:** Clark and Tilman 2017, Environmental Research Letters 12(6): 064016, "Comparative analysis of environmental impacts of agricultural production systems, agricultural input efficiency, and food choice". https://doi.org/10.1088/1748-9326/aa6cd5
* **Read:** abstract only
* **What it estimates or argues:** A meta-analysis of life cycle assessments covering 742 agricultural systems and over 90 foods. Finds organic systems need more land per unit of food, grass-fed beef needs more land than grain-fed, and plant-based foods have the lowest impacts, with ruminant meat about 100 times higher. Concludes that diet shifts and input efficiency matter more than switching to organic or grass-fed.
* **Method family:** land per diet
* **Numbers:** Ruminant meat impacts about 100 times those of plant foods; 742 systems.
* **Use in the methods paper:** Context for section 6 (land-per-food factors and the diet lever).
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. IOP and Oxford ORA pages returned bot-check pages; not retried.

### L120: Tilman and Clark 2014

* **Citation:** Tilman and Clark 2014, Nature 515(7528): 518-522, "Global diets link environmental sustainability and human health". https://doi.org/10.1038/nature13959
* **Read:** abstract only
* **What it estimates or argues:** Argues that rising incomes drive a dietary transition toward refined sugars, fats, oils and meat, and that if unchecked this will drive an 80% rise in agricultural greenhouse gas emissions by 2050 and more land clearing. Mediterranean, pescatarian and vegetarian diets would cut emissions and land clearing and lower disease rates.
* **Method family:** land per diet
* **Numbers:** About 80% rise in global agricultural GHG emissions by 2050 under unchecked dietary trends.
* **Use in the methods paper:** Context for section 6 (diet assumption).
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from Europe PMC (PubMed record). Nature paywalled.

### L121: Bajzelj et al. 2014

* **Citation:** Bajzelj et al. 2014, Nature Climate Change 4(10): 924-929, "Importance of food-demand management for climate mitigation". https://doi.org/10.1038/nclimate2353
* **Read:** read
* **What it estimates or argues:** Builds a data-based biophysical model of the global land system and biomass flows (2009 base year) and shows that, even if yield gaps close, projected demand drives further farmland expansion. Then quantifies demand-side options: improved diets and less food waste are essential to limit emissions and secure food in 2050. The reading was the open author manuscript (University of Cambridge repository).
* **Method family:** commodity balance
* **Numbers:** Food delivered is 0.7 PgC a year (2,490 kcal per person per day) from cropland productivity of 8.3 PgC a year; meat and dairy hold about 2.6% of livestock feed carbon; grazing on land unsuitable for crops is about 14% of livestock feed. Without demand-side change cropland expands by 5-42% and pasture by 13-15% by 2050 (text range). Global only.
* **Use in the methods paper:** Context for section 6 and comparator for the grazing design choice: a biomass-flow model that separates pasture on land unsuited to crops from cropland feed.
* **Lane:** No (no hit for Lane).
* **Note:** Full text opened: author manuscript at the Cambridge repository. Page and figure numbering are the manuscript's.

### L122: Mottet et al. 2017

* **Citation:** Mottet et al. 2017, Global Food Security 14: 1-8, "Livestock: On our plates or eating at our table? A new analysis of the feed/food debate". https://doi.org/10.1016/j.gfs.2017.01.001
* **Read:** record only
* **What it estimates or argues:** By title, venue and the sweep note, an analysis of how much of livestock feed competes with human food, bearing on grazing land versus cropland. No abstract was reachable.
* **Method family:** land per diet
* **Numbers:** None.
* **Use in the methods paper:** Context for section 6 (grazing design choice) if the full text is read.
* **Lane:** Not told (record only).
* **Note:** OpenAlex holds no abstract; the WUR repository page returned a script page. Not retried.

### L123: Schader et al. 2015

* **Citation:** Schader et al. 2015, Journal of the Royal Society Interface 12(113): 20150891, "Impacts of feeding less food-competing feedstuffs to livestock on global food system sustainability". https://doi.org/10.1098/rsif.2015.0891
* **Read:** read
* **What it estimates or argues:** Uses the SOL-model to test reducing livestock feed that competes with human food, down to animals fed only on grassland and by-products. For 2050 this could still supply the same human-digestible energy and protein-to-calorie ratio as the reference, with lower environmental impact, because animal products in human diets fall sharply.
* **Method family:** commodity balance
* **Numbers:** In the extreme case of zero human-edible concentrate feed: greenhouse gas emissions -18%, arable land occupation -26%, N-surplus -46%, P-surplus -40%, freshwater use -21%; protein intake from livestock products down 71%. Global only; Australia is not named.
* **Use in the methods paper:** Comparator for the grazing design choice in section 6: a global mass-flow result that frees arable land by restricting livestock to grassland and by-products.
* **Lane:** No (no hit for Lane).
* **Note:** Full text from Europe PMC (PMC4707862, the open XML copy).

### L124: Shepon et al. 2016

* **Citation:** Shepon et al. 2016, Environmental Research Letters 11(10): 105002, "Energy and protein feed-to-food conversion efficiencies in the US and potential food security gains from dietary changes". https://doi.org/10.1088/1748-9326/11/10/105002
* **Read:** abstract only
* **What it estimates or argues:** Quantifies caloric and protein feed-to-food conversion efficiencies for US livestock categories, and uses them to calculate the food gain from replacing beef in the US diet with poultry or a plant-based alternative.
* **Method family:** energy balance
* **Numbers:** Average caloric and protein efficiencies 7-8%; beef 3% in both; moving beef feed land to poultry feed could meet the calorie and protein needs of about 120 and 140 million more people on the mean American diet (about 40% of the current US population).
* **Use in the methods paper:** Comparator for section 6 (diet assumption): a US conversion-efficiency result that gives a people-count gain from a diet change; the nearest published form of "extra people from a diet change".
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. The IOP page returned a bot-check page; not retried.

## 5. Footprint works

### L125: Borucke et al. 2013

* **Citation:** Borucke et al. 2013, Ecological Indicators 24: 518-533, "Accounting for demand and supply of the biosphere's regenerative capacity: The National Footprint Accounts' underlying methodology and framework". https://doi.org/10.1016/j.ecolind.2012.08.005
* **Read:** record only
* **What it estimates or argues:** By title and venue, the methods paper of the National Footprint Accounts (Global Footprint Network), which set a country's consumption footprint against its biocapacity. No abstract was reachable.
* **Method family:** footprint
* **Numbers:** None.
* **Use in the methods paper:** Catalogue (footprint family: the account itself) for section 4; the text should be opened before any claim about how biocapacity is computed.
* **Lane:** Not told (record only).
* **Note:** OpenAlex, Crossref and Europe PMC hold no abstract; closed access. Year per volume 24 is 2013 (Crossref online 2012).

### L126: van den Bergh and Grazi 2014 (online 2013)

* **Citation:** van den Bergh and Grazi 2014 (online 2013), Journal of Industrial Ecology 18(1): 10-19, "Ecological Footprint Policy? Land Use as an Environmental Indicator". https://doi.org/10.1111/jiec.12045
* **Read:** abstract only
* **What it estimates or argues:** Reviews the ecological footprint as an accounting tool and aggregate indicator from the angles of indicator methodology and welfare economics, and assesses its policy relevance. Concludes that it "does not offer any meaningful information for public policy".
* **Method family:** footprint
* **Numbers:** None.
* **Use in the methods paper:** Critique for section 4 (footprint family): a third published critique, with Giampietro and Saltelli (L085) and Blomqvist (L087).
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. Closed access.

### L127: Galli et al. 2012

* **Citation:** Galli et al. 2012, Ecological Indicators 16: 100-112, "Integrating Ecological, Carbon and Water footprint into a Footprint Family of indicators: Definition and role in tracking human pressure on the planet". https://doi.org/10.1016/j.ecolind.2011.06.017
* **Read:** record only
* **What it estimates or argues:** By title and venue, a framework that places the ecological, carbon and water footprints into one family of indicators. No abstract was reachable.
* **Method family:** footprint
* **Numbers:** None.
* **Use in the methods paper:** Catalogue (footprint family) for section 4 once opened.
* **Lane:** Not told (record only).
* **Note:** No abstract in OpenAlex, Crossref or Europe PMC; closed access.

### L128: Moore et al. 2012

* **Citation:** Moore et al. 2012, Ecological Indicators 16: 3-10, "Projecting future human demand on the Earth's regenerative capacity". https://doi.org/10.1016/j.ecolind.2011.03.013
* **Read:** record only
* **What it estimates or argues:** By title and venue, a projection of footprint and biocapacity forward in time. No abstract was reachable.
* **Method family:** footprint
* **Numbers:** None.
* **Use in the methods paper:** Context for section 4 (footprint family) once opened.
* **Lane:** Not told (record only).
* **Note:** No abstract in OpenAlex, Crossref or Europe PMC; closed access.

### L129: Wackernagel et al. 2019

* **Citation:** Wackernagel et al. 2019, Sustainability 11(7): 2164, "Defying the Footprint Oracle: Implications of Country Resource Trends". https://doi.org/10.3390/su11072164
* **Read:** abstract only
* **What it estimates or argues:** Argues that mainstream competitiveness and development analyses neglect a country's resource security, and uses the Global Footprint Network accounts (1961 to 2014, in global hectares) to predict countries' socio-economic prospects from biophysical trends. Finds that financial assessments and biophysical ones disagree, and offers a way to reconcile them.
* **Method family:** footprint
* **Numbers:** None in the abstract.
* **Use in the methods paper:** Catalogue (footprint family, the accounts' own side) for section 4, balancing the critiques.
* **Lane:** Not told (abstract only).
* **Note:** Abstract text from the OpenAlex record. The MDPI host refused (403) and was not retried.

### L130: Niccolucci et al. 2012

* **Citation:** Niccolucci et al. 2012, Ecological Indicators 16: 23-30, "Biocapacity vs Ecological Footprint of world regions: A geopolitical interpretation". https://doi.org/10.1016/j.ecolind.2011.09.002
* **Read:** record only
* **What it estimates or argues:** By title and venue, a comparison of footprint with biocapacity for world regions read in geopolitical terms. No abstract was reachable.
* **Method family:** footprint
* **Numbers:** None.
* **Use in the methods paper:** Context for section 4 (footprint family) once opened.
* **Lane:** Not told (record only).
* **Note:** No abstract in OpenAlex, Crossref or Europe PMC; closed access.

### L131: Wiedmann and Lenzen 2018

* **Citation:** Wiedmann and Lenzen 2018, Nature Geoscience 11(5): 314-321, "Environmental and social footprints of international trade". https://doi.org/10.1038/s41561-018-0113-9
* **Read:** read
* **What it estimates or argues:** A review of multi-region input-output footprint work on trade: a large and rising share of global environmental and social impact is tied to traded goods, mostly moving from developed to developing countries. It argues that national targets can be undone by shifting production abroad and that footprint indicators belong in the Sustainable Development Goals. Australia appears only as an example (bauxite mined in Australia).
* **Method family:** footprint
* **Numbers:** No Australian capacity or food figure.
* **Use in the methods paper:** Context for section 4 and 8: explains why a production-side land count for Australia (a net food exporter) differs from a consumption-side footprint.
* **Lane:** No (no hit for Lane; the text does not use carrying capacity).
* **Note:** Full text opened: the accepted manuscript from the UNSW repository (open copy).

## What changes the paper's argument

Nothing in the 41 works overturns the paper's argument. Seven points bear on it.

1. **No engagement with Lane in this batch.** The 11 full texts have no hit for Lane, and none of the 41 DOIs is in the B15 list of works that cite Lane's papers. For the 30 works read by abstract or record, the question cannot be answered. The only outside engagement found so far remains Khorsandi 2022 and 2023 (B17).
2. **The Australian line is thin, and this batch supports saying so.** Of the 10 Australian works, none estimates how many people Australian land and water could feed. They are diet footprints (Hendrie, Hadjikakou, Ridoutt), a land-use scenario for carbon and biodiversity (Bryan 2014), a city requirement (Candy), qualitative reviews (Millar and Roots; the Lee book review), a regional sustainability index (Graymore), policy proceedings (Productivity Commission), and a national outlook (CSIRO 2019, news release only). Six of these rest on an abstract or less, so the statement should be hedged to "none found".
3. **Ridoutt 2020 is a usable diet comparator for section 6, with one limit.** Australian adult diets average 7.1 m2 yr-e of cropland per person per day against a planetary-boundary target of 6.1 (2,226 m2 a year); lower-footprint diets need 4.2 and recommended diets built from them 5.9. The target is a fair-share rule, not a supply-side capacity, and the unit is cropland of global average productivity, so it cannot be turned into a number of Australians without an Australian productivity factor. Decision row for Murray: whether section 6 names this as the diet-side comparator.
4. **Two sharp poles on the concept (section 2).** Cohen 2017 calls human carrying capacity a "specious metaphor" and shows about ninety estimates since 1679 with no narrowing scatter. Tucker 2020 gives one figure (3 billion people at modern industrial living) with the calculation left in a book. The Productivity Commission chairman, in the 2011 proceedings, prefers "absorption capacity" (rate of change) to a static target. The paper's stance (a range under named methods and assumptions, not a target) sits between these, and Cohen's scatter is the best single citation for needing it.
5. **Fader 2013 is the closest national land-and-water boundary comparator** (66 countries cannot be self-sufficient on land or water limits in 2000; 62 on land). Australia is not named in the text. The country result sits in figures and the appendix, which were not opened; open them before saying anything about Australia.
6. **One number must not be quoted from its abstract.** Hadjikakou 2017's abstract gives 35, 39, 35 and 33 percent for water, energy, carbon dioxide equivalent and land use, but the results text gives energy 39%, water 35%, ecological footprint 35% and greenhouse gas 33%. The abstract's "land use" share is the footprint, which covers all land types and carbon uptake land. Use the results text.
7. **Corrections to the B14 sweep rows.** Lee 2013 is a two-page book review of an edited volume, not a study. Peters, Bills, Wilkins and Fick appears in print in 2009 (issue 24(1)); Graymore, Sipe and Rickson is dated 2010 in the volume and 2009 online. Candy 2019 states 16.3 million hectares a year to feed Greater Melbourne; that is large for one city and the abstract does not say what land it counts, so check the full text before using it.

## Works not reached in full, with the reason

Abstract only (full text not opened), 21 works:

* Graymore 2010: closed access; abstract from RePEc.
* Candy 2019, Peters 2008, Horst and Gaolach 2014, Kurtz 2020, Hunter 2017, Ma 2017, Poore and Nemecek 2018, van den Bergh and Grazi 2013: closed access, no open copy found.
* Millar and Roots 2012: the CSU repository copy returned 403.
* Bryan 2014: the figshare copy returned an empty reply (202); the publisher page is closed.
* Zumkehr and Campbell 2015: the OpenEdition copy returned a bot-check page.
* Tilman 2011: pnas.org and the Europe PMC PDF render both returned 403.
* Schon and Bohringer 2023: mdpi.com and preprints.org both returned 403.
* Wang 2022 and Wackernagel 2019: mdpi.com returned 403.
* Roos 2017: ScienceDirect returned a bot-check page.
* van Zanten 2016: the Springer and WUR pages returned script or error pages.
* Clark and Tilman 2017 and Shepon 2016: iopscience.iop.org and the Oxford ORA page returned bot-check pages.
* Tilman and Clark 2014: paywalled; the abstract is from Europe PMC.

Record only (no abstract), 9 works:

* Lee 2013 (book review; 200 characters of text on the record), Qiu 2024, Smith 2013, Mottet 2017, Borucke 2013, Galli 2012, Moore 2012, Niccolucci 2012: closed access, and OpenAlex, Crossref and Europe PMC hold no abstract.
* CSIRO Australian National Outlook 2019: the news release was read, but the report and the technical report were not; the report page (csiro.au/ano) returned 503. No land or food figure is on the news release.

Hosts that refused and were not retried: mdpi.com, preprints.org, pnas.org, iopscience.iop.org, sciencedirect.com, researchoutput.csu.edu.au, OpenEdition, ora.ox.ac.uk, the Europe PMC PDF render, Semantic Scholar (429), and one Crossref lookup (429). The refusals came from different hosts and were never ten in a row on the web as a whole, so the stop line was not reached.
