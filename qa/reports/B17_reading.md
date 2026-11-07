# B17: priority literature read into the register

Register rows added: L073 to L090 (`qa/literature_register.csv`, 18 new rows, CRLF and all 12 columns kept, existing rows untouched). No PDF was placed in a repository. Copies were read from the session scratch area, or from the library folder for Peters 2009.

## What "read" means in this report
* `read` (full text opened): Khorsandi 2022, Khorsandi 2023, Peters 2009, Kastner 2012, Springmann 2018, Gerten 2020, Erb 2016, Blomqvist 2013, and the Goldfinger et al. reply. Two caveats: Springmann and Gerten are the authors' accepted manuscripts from the Potsdam repository, not the journal layout; Goldfinger is the author copy hosted by Global Footprint Network.
* `abstract only`: Hatfield-Dodds 2015, Bryan 2016, Peters 2022, Ridoutt 2017, Willett 2019, Chapman and Byron 2018. The abstract text came from the publisher page (Hatfield-Dodds), the OpenAlex record (Bryan, Chapman and Byron), the Wageningen research portal (Willett), a retailer preview (Peters 2022) and a search-engine summary of index records (Ridoutt, the weakest basis).
* `not reached`: Giampietro and Saltelli 2014 (paywalled; I know their argument only through the Goldfinger reply), Sobels 2010 (the macrobusiness copy returned 503, the Adelaide repository connection failed), and the CSIRO Australian National Outlook 2015 report (not opened).
* Several open-access full texts (Bryan, Chapman and Byron, Willett, Springer pages) were refused to the session or sat behind a bot check. A request to fetch one through a web-archive mirror was blocked by the permission system, so I stopped and did not try other routes. Those papers stay `abstract only`.

## The list, with one-line use

### 1. Khorsandi and co-authors on Iran
**Khorsandi, Homayouni and van Oel 2022**, Science of the Total Environment 817: 153038, doi:10.1016/j.scitotenv.2022.153038.
* Argues: carrying capacity (K) for Iran can be bounded by three limits taken in turn: suitable agricultural land (from a satellite-based suitability index, replicating Mesgaran et al. 2017), water available for evapotranspiration, and a realistic yield set by human appropriation of net primary production (HANPP, 25% of NPP, 3,000 kcal a day). Nine scenarios, four spatial scales (nation, basins, sub-basins, 609 water units). Self-sufficient, no trade by assumption.
* Family: resource-based land and diet, with a water limit (an energy-balance flavour through HANPP).
* Numbers: theoretical K 130.2 million at national water scale falling to 76.8 million when each of 609 local units must be self-sufficient; realistic K 35.5 million (national water) and 20.2 million (local), against 84 million people. These bear on Australia only as a design lesson: the answer falls by about 40% as the self-sufficient unit shrinks.
* Use: **catalogue and comparator**. A post-2011 national method that the thesis method can be tested against; it also supports the scale design choice.
* Lane: **yes**. Cites Lane 2014 (thesis) and Lane, Dawes and Grace 2014 for local-scale studies, for the time index K(t) and for the point that social capacity lies below biophysical capacity; also cites Lane 2014 for local food production. Does not cite the 2015 or 2017 papers.

**Khorsandi, Bateni and van Oel 2023**, Heliyon 9: e15079, doi:10.1016/j.heliyon.2023.e15079.
* Argues: the complex 2022 model can be replaced by a simple formula (K = A/B at unlimited yield, with a HANPP-based version) that reproduces the multi-scale results. Capacity rises with the area considered in a logarithmic pattern, read as diminishing returns. Checked against ecological footprint biocapacity for Iran as a bound.
* Family: resource-based land and diet (meta-model of it); touches footprint.
* Numbers: none for Australia. The shape result (logarithmic in area) is the item that bears on a scale curve.
* Use: **comparator and context** for the scale design choice (section 6).
* Lane: **yes**. References 3 to 5 are Lane 2017 (time frames), Lane, Dawes and Grace 2014 and the thesis; Lane is named in the text as one of the authors who explained that K modelling spans many disciplines.

### 2. The ten works in B14
**Hatfield-Dodds et al. 2015**, Nature, doi:10.1038/nature16065 (abstract only).
* Argues: a linked set of models of energy, water, food, rural land use, materials and climate shows Australia's environmental pressures to 2050 could more than double, stabilise or fall markedly depending on policy, with growth strong in all scenarios; no evidence decoupling is automatic and no shift in values is required.
* Family: scenario model. Numbers: no capacity figure in the abstract.
* Use: **context**; a scenario outlook answers "what happens under choices", not "how many can be supported". The full report (L090) was not opened. Lane: cannot be told.

**Bryan et al. 2016**, Global Environmental Change 38, doi:10.1016/j.gloenvcha.2016.03.002 (abstract only).
* Argues: the LUTO land-use model, run on 1.1 km grid cells annually from 2013 to 2050 under global and domestic policy scenarios, finds large possible shifts from agriculture to carbon and environmental plantings and biofuels, with food and fibre output not greatly hurt under strong abatement incentives; water is the main governance risk.
* Family: scenario model. Numbers: none in the abstract. Use: **comparator** (nearest published Australian gridded land-use model). Lane: cannot be told.

**Peters et al. 2009**, Renewable Agriculture and Food Systems 24(1): 72-84, doi:10.1017/S1742170508002457 (full text; library copy).
* Argues: a map-based allocation of New York State production zones to population centres by least distance shows the state could supply 34% of its food within an average 49 km; most centres could be fed in-state except New York City. Uses the 2007 complete-diet land model for per-person need.
* Family: resource-based land and diet, with a spatial allocation. Numbers: none for Australia.
* Use: **catalogue and scale comparator** (the within-region view of self-sufficiency). Lane: no.
* **Peters 2022 chapter** (Food Systems Modelling, doi:10.1016/b978-0-12-822112-9.00007-2; abstract only): treats foodshed analysis and carrying capacity estimation as two linked questions that are hard to tell apart. Use: **catalogue and concept**. Lane: cannot be told. Peters 2009 is a new row; L040 ("Peters (New York State)") is the 2007 paper and still stands as it was.

**Ridoutt et al. 2017**, Food Security 9(2): 211-226, doi:10.1007/s12571-017-0650-x (abstract only, weakest basis).
* Argues: Australian food intake scenarios to 2050 set against linear projections of production by basic food group; population 23 million (2015) to 37.5 million (2050); demand outruns local production for most commodities, so net exports fall and import dependence rises.
* Family: commodity balance. Use: **comparator** for the commodity-balance family on Australian data. Lane: cannot be told.

**Kastner et al. 2012**, PNAS 109(18), doi:10.1073/pnas.1117054109 (full text).
* Argues: using FAO data for 1961 to 2007, cropland needed per person fell in most regions while diets became richer; a decomposition separates population, yield and diet. Yield gains were offset by population and diet change; diet may overtake population as the main driver.
* Family: land per diet. Numbers: Oceania was among the highest, above 3,000 m2 of cropland per person per year in 2005 (a dry region with large annual variability). Use: **context and critique** support for "what moves the number" (section 6). Lane: no; it does not use the phrase carrying capacity.

**Willett et al. 2019** (EAT-Lancet), The Lancet 393: 447-492, doi:10.1016/S0140-6736(18)31788-4 (abstract only) and **Springmann et al. 2018**, Nature 562, doi:10.1038/s41586-018-0594-0 (full text, accepted manuscript).
* Willett: a reference healthy diet and targets for food production for about 10 billion people on no additional land (yield gaps cut by at least 75%; red meat and sugar down by over 50%; nuts, fruit, vegetables and legumes up by over 100%). Springmann: a global food model with country detail finds environmental impacts could rise 60 to 90% from 2010 to 2050 without action, 2010 cropland was 12.6 million km2, and no single measure keeps the system within all boundaries.
* Family: nutrition optimisation (Willett); scenario model (Springmann). Neither gives a population capacity or an Australian figure. Use: **context** for the diet assumption any diet-based capacity must state. Lane: no (Springmann); cannot be told (Willett).

**Gerten et al. 2020**, Nature Sustainability 3: 200-208, doi:10.1038/s41893-019-0465-1 (full text, accepted manuscript).
* Argues: with four planetary boundaries (biosphere integrity, land-system change, freshwater, nitrogen) strictly respected, the present food system gives a balanced diet (2,355 kcal) to 3.4 billion; a transformed system with redistributed cropland, better water and nutrient management, less waste and diet change could support 10.2 billion. Trade is not modelled in the global figure.
* Family: nutrition optimisation / land boundary. Numbers: global only. Use: **comparator** for the idea of a capacity range with named conditions. Lane: no.

**Erb et al. 2016**, Nature Communications 7: 11382, doi:10.1038/ncomms11382 (full text).
* Argues: of 500 global scenarios for 2050 (yield, cropland expansion, feed, livestock efficiency, diet) with no deforestation, over 40% are not feasible; all vegan and 94% of vegetarian scenarios are feasible, about two thirds of business-as-usual diets and 15% of rich-meat diets; diet matters more than yield or cropland, and grazing limits shrink the option space.
* Family: land per diet / biomass balance. Numbers: global; North America and Oceania are one region (a net exporter). Use: **support for reporting a range** and for the grazing design choice (section 6). Lane: no.

**Giampietro and Saltelli 2014** (Ecological Indicators 46, doi:10.1016/j.ecolind.2014.01.030; not reached), **Goldfinger et al. 2014** reply (full text) and **Blomqvist et al. 2013**, PLoS Biology 11: e1001700, doi:10.1371/journal.pbio.1001700 (full text).
* Blomqvist: the global overshoot ("1.5 Earths") is almost wholly the carbon footprint, which rests on one assumed forest sequestration rate (0.97 t C per ha per year); omit carbon and biocapacity exceeds footprint by about 45% (2008), and at 2.6 t C per ha per year the overshoot vanishes; at national scale the footprint measures self-sufficiency, not sustainability. Goldfinger (by footprint-network authors): the critique targets a version of the accounts nobody uses; the footprint reflects actual productivity and is not a full sustainability measure. Giampietro and Saltelli, as summarised in the reply: the footprint does not answer the question it claims to, is fragile, and its overshoot comes from the carbon treatment.
* Family: footprint. Use: **critique and catalogue** (both sides, section 4 footprint family). Lane: no (Blomqvist; the opening pages of Goldfinger).

**Chapman and Byron 2018**, Global Ecology and Conservation 13: e00365, doi:10.1016/j.gecco.2017.e00365 (abstract only).
* Argues: a review of ecosystem studies since the 1950s finds carrying capacity defined and used in very many ways, usually as K, the number of individuals the environment can support, with unclear treatment of change over time; used mostly in conservation, rangeland and wildlife management, aquaculture and fisheries.
* Family: concept review. Use: **context** for section 2. Lane: cannot be told.

### 3. Sobels et al. 2010
Not reached (see above). Described by a search summary only: a scenario study of how long-term net overseas migration levels could affect the natural and built environment over fifty years, using the Australian Stocks and Flows Framework. Use if opened: **context and comparator** (scenario model). Row L089.

## Things that change or sharpen the paper's argument
1. **A post-2011 national capacity method that cites Lane.** Khorsandi 2022 and 2023 are independent, peer-reviewed, and cite the thesis, the 2014 paper and the 2017 paper. This is outside engagement with the author's work, which the competing-interests disclosure and the section 3 "papers since 2011" selection can use. Its HANPP-plus-suitability-plus-water recipe is a method family the catalogue does not yet have as a separate entry. Whether it can be run on Australian 2025 data (it needs a land suitability map, water by unit and NPP) is a decision for the test plan, not settled here.
2. **Scale.** Khorsandi shows a 40% fall in capacity from nation to 609 local units (130.2 to 76.8 million theoretical) and a logarithmic capacity-area relation. This supports treating scale as a design choice with its own curve (section 6) and is a published parallel for the shape.
3. **Diet decides the answer.** Kastner (diet may override population growth), Erb (diet is the strongest determinant of the option space) and the EAT-Lancet reference diet all point the same way. This backs the paper's argument that diet and grazing assumptions move a capacity number more than data differences do.
4. **The footprint family needs both sides.** Blomqvist's point that national footprint is a self-sufficiency measure and that the overshoot rests on one carbon assumption bears on how the paper rates footprint-based Australian figures (Simpson, Lenzen and Murray, Wackernagel). The footprint-network reply is the defence to cite beside it. Giampietro and Saltelli should be read in full before the paper quotes them.
5. **Scenario studies versus capacity.** Hatfield-Dodds and Bryan are about what happens under choices, not how many can be supported; the paper should say they are not capacity methods and keep them as context. Ridoutt 2017 is the closest Australian commodity-balance comparator but was read at abstract level through a secondary summary only.

## Open items the reading did not close
* Full text still needed for Bryan 2016, Hatfield-Dodds 2015 (and the CSIRO report), Ridoutt 2017, Peters 2022, Willett 2019, Chapman and Byron 2018, Giampietro and Saltelli 2014, Sobels 2010. If Murray holds institutional copies, place them in the models archive's `Literature review/` folder and the rows can be raised to `read`.
* Not looked at: Rees and Wackernagel's reply to Blomqvist, and the further Giampietro and Saltelli reply (a search record gives Ecological Indicators 46: 260-263, doi:10.1016/j.ecolind.2014.06.019, unconfirmed).
* Bibliographic details to confirm against Crossref before any citation: Ridoutt author list (index records disagree), the DOI of the Goldfinger reply, page ranges not printed on the files I read.
* Lane: for the six abstract-only papers and Giampietro and Saltelli, whether they cite Lane is unknown; only the full texts can say.
