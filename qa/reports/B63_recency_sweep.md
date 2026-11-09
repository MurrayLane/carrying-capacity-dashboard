# B63: works from 2016 on for the thin and uncovered points of Papers A and B (decision 38)

Companion file: `qa/reports/B63_candidates.csv` (88 rows, one per candidate per point; 78 distinct works, so a work serving several points has a row for each). Working files: `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/b63` (Crossref and OpenAlex records in `meta.json`, open full texts under `ft/`, scripts under `scripts/`). Registers not edited.

## Basis

* Started from `qa/reports/B61_lit_review_scope.md` (the points marked thin or uncovered) and `qa/reports/B61_candidate_sources.csv`, and checked every candidate DOI against the DOIs in `qa/literature_register.csv`: none of the 78 is in the register. B61 candidates dated 2016 or later were kept where they still fit (21 of them); those before 2016 are left to B61.
* **Search.** Crossref bibliographic search (filtered to 2016 to 2026) and works known to fit each point; every candidate was then confirmed on the Crossref record (title, authors, year, venue, DOI, citation count) and on the OpenAlex record by DOI (citation count, open-access status, abstract, reference list). The OpenAlex search endpoint had no free quota left on this network, so OpenAlex was used by DOI only; no key was requested.
* **Year.** The Crossref issued year. Two works that B61 dated 2016 carry 2015 on Crossref (Carey et al., Smith et al.) and are noted under their points, not ranked.
* **Cites Lane.** Each OpenAlex reference list was matched against the five Lane works that have OpenAlex records: Lane 2010 (Land Use Policy), Lane and Dawes 2013, Lane et al. 2014 (Ecological Modelling), Lane et al. 2015 and Lane 2017 (Population and Environment). The thesis, the 2011 Urban Design paper and the 2015 IAFOR paper have no DOI and could not be matched. "unknown" means OpenAlex holds no reference list and no full text was read. Full texts read were also searched for "Lane". Two candidates cite Lane: Bolleter 2018 (Lane 2017) and Zhang et al. 2018 (Lane 2010). Reutter et al. 2017 has a co-author named Lane who is a different person.
* **Reading.** Full texts were fetched only from open copies, into the working folder, one folder per work; no PDF went into a repository. A host that refused (HTTP 401, 403, 429, 202 challenge or no connection) was not tried again: doi.org, sciencedirect.com, onlinelibrary.wiley.com, agupubs.onlinelibrary.wiley.com, academic.oup.com, advances.sciencemag.org, annualreviews.org, mdpi.com, meridian.allenpress.com, australianpopulationstudies.org, research.aalto.fi, research.birmingham.ac.uk, cgspace.cgiar.org, ebi.ac.uk, figshare.com and ageconsearch.umn.edu. link.springer.com, hal.archives-ouvertes.fr and pmc.ncbi.nlm.nih.gov served a short holding or challenge page instead of the text and were not pressed.
* **Labels.** *full text* = the open text was retrieved and read for the point and searched for Lane (16 works); *abstract* = the OpenAlex or publisher abstract (45 works); *record* = title, venue and metadata only, no abstract available on either service (17 works), and the "why" says "title only". Of the 78 works, 55 are open access on OpenAlex, but only 16 could be read in full for the host reasons above; the other 39 open works can be downloaded by hand (list at the end).
* **Priority.** 1 = the point needs it (Australian where the point is Australian, or the representative work of a family); 2 = good support; 3 = context.
* Titles are given as on Crossref except that an em dash inside three titles is written as a colon.
* Decision 33 applies: the "why" lines state what each work does and what it found, not what it lacks.

---

## Candidates by point

### Paper A, section 1 (introduction)

**A1.1 Australian population debate and planning, 2011 to 2025**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Davies 2024, *Changing Australia’s settlement geography: The repopulation of regional cities and towns*, Australian Urban Policy: Prospects and Pathways: 149-164. doi:10.22459/aup.2024.08 | Book chapter on Australian urban policy: population grew by 5 million in two decades, widely described as unplanned; follows growth into regional cities and cites the 2020 Population Statement; an academic account of settlement and planning to 2024. | full text | no | 1 | 0 |
| 2 | Parr 2018, *What sort of population policy should Australia adopt? Suggestions for migration, fertility and population research policy*, Australian Population Studies 2(2): 12-21. doi:10.37970/aps.v2i2.36 | Commentary in Australian Population Studies on what population policy Australia should adopt (migration, fertility, size); title and venue only, content not seen. | record | unknown | 1 | 5 |
| 3 | Bolleter 2018, *The consequences of three urbanisation scenarios for northern Australia*, Australian Planner 55(2): 103-125. doi:10.1080/07293682.2019.1620302 | Three settlement scenarios for the white paper's 5 million people in northern Australia by 2060; uses Lane 2017 to say the north's population already exceeds its regional capacity; ties a population target to planning. | full text | yes (Lane 2017) | 1 | 6 |
| 4 | McDonald 2017, *International migration and employment growth in Australia, 2011–2016*, Australian Population Studies 1(1): 3-12. doi:10.37970/aps.v1i1.8 | Immigration and employment growth 2011 to 2016: the skilled-migration basis of population growth in the years Paper A covers. | abstract | no | 2 | 9 |

Not found as Crossref or OpenAlex records in this sweep: the Intergenerational Reports (2015, 2021, 2023), the Centre for Population statements, and the 2016 Productivity Commission report on migrant intake. They are Australian government reports and can be cited from their own pages; Davies 2024 cites the 2020 Population Statement. No peer-reviewed account of the Big Australia debate as such turned up. B61's Hugo 2011 and Wilson 2015 fall before 2016.

**A1.4 Food security in Australian planning and policy**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Summerhayes and Baker 2026, *Transforming food security policymaking in Australia: a three-tiered food systems-centred and rights-based approach*, Food Security 18(4): 961-976. doi:10.1007/s12571-026-01655-8 | 102 food policies, 25 interviews and 500 surveys in Queensland, Victoria and Western Australia; food security agendas found inadequate at local, state and national levels; proposes a three-tier, rights-based approach. | abstract | no | 1 | 1 |
| 2 | Summerhayes and Baker 2024, *Trans-Governance and Food Systems (Tr-GaF) for food policy integration: A case study of the Australian food policy landscape*, Food Policy 128: 102736. doi:10.1016/j.foodpol.2024.102736 | Same 102-policy corpus: limited integration of food policy in Australia, little attention to food in urban planning, fragmentation across levels of government. | abstract | no | 1 | 7 |
| 3 | Summerhayes and Baker 2025, *Integrating urban land use planning with food systems in Australia: Policy integration challenges and opportunities*, International Journal of Urban and Regional Research 50(3): 527-544. doi:10.1111/1468-2427.70026 | Interviews with 25 senior planners and policymakers: agricultural land and food retail are the only food elements that planning integrates; land scarcity and market pressure limit more. | abstract | no | 2 | 2 |
| 4 | James and O'Neill 2016, *Planning for Peri-urban Agriculture: a geographically-specific, evidence-based approach from Sydney*, Australian Geographer 47(2): 179-194. doi:10.1080/00049182.2015.1130676 | Sydney Basin farmland 1992 to 2011: the data on peri-urban food production are contested, so planners cannot say whether metropolitan supply is at risk. | abstract | no | 2 | 34 |

Carey et al., *Opportunities and challenges in developing a whole-of-government national food and nutrition policy: lessons from Australia's National Food Plan*, Public Health Nutrition (doi:10.1017/s1368980015001834; B61 candidate) was read in full: the Plan did not deliver an integrated food policy, with nutrition and sustainability set aside. Crossref dates it 2015 (issue 19(1), 2016), so it sits just outside the window and is not ranked. The 2023 House of Representatives inquiry report on food security and the ABARES food-security analyses were not found on Crossref or OpenAlex; cite them from the Parliament and ABARES pages.

**A1.5 Observed drought and climate effects on Australian farming since 2011**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Hughes et al. 2022, *Modelling the effects of climate change on the profitability of Australian farms*, Climatic Change 172(1-2). doi:10.1007/s10584-022-03356-5 | ABARES farm model: post-2000 climate cut average farm profit by 22.3% against the 1950 to 2000 climate; projections for 2050 range from -2 to -50% against the same base; the farm-performance evidence the point asks for. | abstract | no | 1 | 30 |
| 2 | Hochman et al. 2017, *Climate trends account for stalled wheat yields in Australia since 1990*, Global Change Biology 23(5): 2071-2081. doi:10.1111/gcb.13604 | Water-limited wheat yield potential fell 27% from 1990 to 2015 through lower rainfall and higher temperatures; technology gains hid the loss in actual yields. | abstract | no | 1 | 301 |
| 3 | Falster et al. 2024, *How unusual was Australia's 2017–2019 Tinderbox Drought?*, Weather and Climate Extremes 46: 100734. doi:10.1016/j.wace.2024.100734 | The 2017 to 2019 Tinderbox Drought: cool-season and annual rainfall deficits in the Murray-Darling Basin were unprecedented in the instrumental record. | abstract | no | 2 | 9 |
| 4 | Wittwer and Waschik 2021, *Estimating the economic impacts of the 2017–2019 drought and 2019–2020 bushfires on regional NSW and the rest of Australia*, Australian Journal of Agricultural and Resource Economics 65(4): 918-936. doi:10.1111/1467-8489.12441 | Economic model of the 2017 to 2019 drought: national GDP 0.7% or more below base in 2018-19 and 2019-20; $53 billion welfare loss; farm capital and herds depleted. | abstract | no | 2 | 79 |

King et al. 2020, *The role of climate variability in Australian drought*, Nature Climate Change (doi:10.1038/s41558-020-0718-z, 201 citations) is the fifth candidate; record only (repository page not served). ABARES farm performance reports (Farm Surveys, Insights) were not found as records; Hughes 2022 and Hughes 2017 (A11.5) are the peer-reviewed ABARES outputs.


### Paper A, section 11 (discussion of measures)

**A11.1 Livestock productivity in Australia**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Mayberry et al. 2019, *Pathways to carbon-neutrality for the Australian red meat sector*, Agricultural Systems 175: 13-21. doi:10.1016/j.agsy.2019.05.009 | CSIRO pathways to carbon neutrality for the Australian red meat sector, built on national herd and productivity assumptions; title only. | record | no | 1 | 81 |
| 2 | Wiedemann et al. 2016, *Resource use and greenhouse gas emissions from grain-finishing beef cattle in seven Australian feedlots: a life cycle assessment*, Animal Production Science 57(6): 1149-1162. doi:10.1071/an15454 | Life cycle assessment of seven eastern Australian feedlots: water, fossil energy and emissions per kg of liveweight gain. | abstract | no | 2 | 21 |
| 3 | Malau-Aduli et al. 2022, *Genetics and nutrition impacts on herd productivity in the Northern Australian beef cattle production cycle*, Veterinary and Animal Science 15: 100228. doi:10.1016/j.vas.2021.100228 | Review of genetic and nutritional limits on northern Australian beef herd productivity on phosphorus-deficient tropical pastures. | abstract | no | 2 | 16 |
| 4 | Ridoutt 2024, *Pathways toward Climate-Neutral Red Meat Production*, Methane 3(3): 397-409. doi:10.3390/methane3030022 | Australian red meat emissions series 1990 to 2020, with business-as-usual growth of 13% in beef cattle and 18% in sheep to 2030. | abstract | no | 3 | 8 |

No ABARES livestock productivity series was found as a record; the candidates are Australian life-cycle and herd studies, not productivity indices.

**A11.3 Australian food waste (National Food Waste Strategy and baseline)**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Reutter et al. 2017, *The challenge of characterising food waste at a national level: An Australian example*, Environmental Science & Policy 78: 157-166. doi:10.1016/j.envsci.2017.09.014 | Characterising food waste at the national level for Australia, published the year of the National Food Waste Strategy; title only (its Lane is a co-author of that name, not the model's author). | record | no | 1 | 27 |
| 2 | Mirosa et al. 2020, *Food Waste in Australia and New Zealand*, Routledge Handbook of Food Waste: 225-236. doi:10.4324/9780429462795-18 | Reviews food-waste research and the history of food-waste policy in Australia and New Zealand. | abstract | unknown | 2 | 2 |
| 3 | Ananda et al. 2023, *Quantifying the effects of food management routines on household food waste*, Journal of Cleaner Production 391: 136230. doi:10.1016/j.jclepro.2023.136230 | National Australian household survey (n = 4324) linking food planning and storage routines to the amount wasted. | abstract | no | 2 | 57 |
| 4 | Spang et al. 2019, *Food Loss and Waste: Measurement, Drivers, and Solutions*, Annual Review of Environment and Resources 44(1): 117-156. doi:10.1146/annurev-environ-101718-033228 | Global synthesis: definitions of loss and waste are inconsistent and data gaps large; context for any national baseline. | abstract | no | 3 | 284 |

The National Food Waste Strategy (2017) and the National Food Waste Baseline (2019) were not found on Crossref or OpenAlex; cite from the Department's pages. Reutter et al. 2017 is the closest peer-reviewed national characterisation.

**A11.4 Grain reserves and strategic stocks**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Laio et al. 2016, *The past and future of food stocks*, Environmental Research Letters 11(3): 035010. doi:10.1088/1748-9326/11/3/035010 | 50 years of food stocks for 92 products in kcal: per-capita stocks are stationary; Oceania holds larger per-capita stocks with a higher chance of halving, linked to its net exports. | full text | no | 1 | 35 |
| 2 | Marchand et al. 2016, *Reserves and trade jointly determine exposure to food supply shocks*, Environmental Research Letters 11(9): 095009. doi:10.1088/1748-9326/11/9/095009 | Shock model for cereals: reserves and trade together set a country's exposure; Australia's reserve-to-supply ratio was 0.435 in 2009. | full text | no | 1 | 149 |
| 3 | Han et al. 2024, *Strategic cropland reserves can strengthen China’s food security*, Nature Food 5(7): 535-538. doi:10.1038/s43016-024-01015-9 | Strategic cropland reserves for China: land held in reserve as an alternative to grain stocks; title only. | record | no | 2 | 20 |
| 4 | Timmer 2024, *Managing world food crises: the role of domestic food grain reserves and international trade*, Future Food Systems: 229-239. doi:10.1016/b978-0-443-15690-8.00002-3 | Domestic grain reserves and trade in world food crises (book chapter); title only. | record | no | 3 | 0 |

No Australian work on grain reserves or strategic food stocks was found; the candidates are global or Chinese. The World Bank's 2025 report on strategic grain reserves (doi:10.1596/43131) exists but is not peer-reviewed.

**A11.5 Drought resilience and the Future Drought Fund**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Botterill 2021, *From National Drought Policy to National Drought Agreement: the evolution of Australia’s drought response*, The Rangeland Journal 43(3): 77-86. doi:10.1071/rj20065 | National Drought Policy from 1992 to the 2018 National Drought Agreement: self-reliance stays the stated aim while spending is still announced during severe drought. | abstract | no | 1 | 12 |
| 2 | Hughes et al. 2022, *Defining drought from the perspective of Australian farmers*, Climate Risk Management 35: 100420. doi:10.1016/j.crm.2022.100420 | ABARES outcome-based drought indicator for farms; farmers have shifted their idea of drought with the long-term change in climate. | abstract | no | 1 | 28 |
| 3 | Hughes and Lawson 2017, *Climate adjusted productivity on Australian cropping farms*, New Directions in Productivity Measurement and Efficiency Analysis. doi:10.4337/9781786432421.00012 | Climate-adjusted productivity of Australian cropping farms 1977-78 to 2014-15: a marked deterioration in cropping climate over the last 15 to 20 years of the series, mainly in the south. | abstract | unknown | 2 | 14 |
| 4 | Sysak and Beilin 2017, *Social Impacts of a National Drought Policy in Australia*, Handbook of Drought and Water Scarcity: 405-422. doi:10.1201/9781315226774-20 | Local social effects of national drought policy in an irrigated region of northern Victoria; drought policy has to be read with water policy. | abstract | no | 3 | 0 |

The Future Drought Fund itself has no peer-reviewed record in this sweep (Crossref holds a news commentary only). The Productivity Commission's review of the Fund was not found as a record.

**A11.6 Interregional freight and food supply chains**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Higgins et al. 2018, *Informing transport infrastructure investments using TraNSIT: A case study for Australian agriculture and forestry*, Computers and Electronics in Agriculture 154: 187-203. doi:10.1016/j.compag.2018.09.008 | TraNSIT, the CSIRO model of Australian agricultural and forestry freight, used to weigh transport investments; title only. | record | no | 1 | 19 |
| 2 | Higgins et al. 2018, *Informing major government programs for rural transport infrastructure in northern Australia*, The Rangeland Journal 40(4): 341-351. doi:10.1071/rj18008 | TraNSIT applied to the 2016 Beef Roads Program: farm-to-market distances over 1000 km on largely unsealed roads cut by seasonal flooding. | abstract | no | 2 | 5 |
| 3 | Davis et al. 2020, *Towards food supply chain resilience to environmental shocks*, Nature Food 2(1): 54-65. doi:10.1038/s43016-020-00196-3 | Scoping review of how environmental shocks pass along or are damped by food supply chains. | abstract | no | 2 | 575 |

Smith et al., *The resilience of long and short food chains: a case study of flooding in Queensland, Australia*, Agriculture and Human Values (doi:10.1007/s10460-015-9603-1, 138 citations) is the closest Australian supply-chain study but Crossref dates it 2015 (issue 2016); closed. No academic work on interstate food freight was found.

**A11.7 Import dependence**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Kummu et al. 2020, *Interplay of trade and food system resilience: Gains on supply diversity over time at the cost of trade independency*, Global Food Security 24: 100360. doi:10.1016/j.gfs.2020.100360 | 1987 to 2013: food supply diversity rose for most people at the cost of greater import dependence and fewer import partners. | abstract | no | 1 | 226 |
| 2 | Soliman Hunter and Taylor 2021, *Long-term and short-term liquid fuel security in Australia – What role for the Great Australian Bight?*, Energy Policy 157: 112472. doi:10.1016/j.enpol.2021.112472 | Australia's long-term and short-term liquid fuel security; the import dependence that farm and freight fuel rests on; title only. | record | unknown | 1 | 2 |
| 3 | Wood et al. 2018, *Trade and the equitability of global food nutrient distribution*, Nature Sustainability 1(1): 34-37. doi:10.1038/s41893-017-0008-6 | Trade and the distribution of food nutrients between countries; title only. | record | no | 2 | 169 |
| 4 | Ritzel et al. 2024, *Vulnerability assessment of food imports: Conceptual framework and empirical application to the case of Switzerland*, Heliyon 10(5): e27058. doi:10.1016/j.heliyon.2024.e27058 | An import vulnerability index (exporter and product factors) applied to Switzerland; a template for measuring import exposure. | abstract | no | 3 | 11 |

No Australian study of food import dependence was found; the candidates are global, and Soliman Hunter and Taylor 2021 covers the fuel side.


### Paper A, section 12 (limitations)

**A12.1 Self-sufficiency as a policy concept**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Clapp 2017, *Food self-sufficiency: Making sense of it, and when it makes sense*, Food Policy 66: 88-96. doi:10.1016/j.foodpol.2016.12.001 | Self-sufficiency is defined and measured in several ways; argues for a continuum rather than a choice between home production and open trade. | abstract | no | 1 | 573 |
| 2 | Kinnunen et al. 2020, *Local food crop production can fulfil demand for less than one-third of the population*, Nature Food 1(4): 229-237. doi:10.1038/s43016-020-0060-7 | Only 11 to 28% of people worldwide could meet their demand for a given crop within 100 km. | abstract | no | 1 | 243 |
| 3 | Schreiber et al. 2021, *Quantifying the foodshed: a systematic review of urban food flow and local food self-sufficiency research*, Environmental Research Letters 16(2): 023003. doi:10.1088/1748-9326/abad59 | Systematic review of 42 foodshed studies: capacity, flow and hybrid types; most from the Global North. | abstract | no | 2 | 100 |
| 4 | Beltran-Peña et al. 2020, *Global food self-sufficiency in the 21st century under sustainable intensification of agriculture*, Environmental Research Letters 15(9): 095004. doi:10.1088/1748-9326/ab9388 | 165 countries to 2100: self-sufficiency falls under middle and business-as-usual paths; Australia is among the surplus producers. | full text | no | 2 | 314 |

**A12.2 Urban agriculture**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Mcdougall et al. 2020, *Urban agriculture could provide 15% of food supply to Sydney, Australia, under expanded land use scenarios*, Land Use Policy 94: 104554. doi:10.1016/j.landusepol.2020.104554 | Urban agriculture could provide 15% of Sydney's food under expanded land use; Australian and quantified; title only. | record | no | 1 | 70 |
| 2 | Payen et al. 2022, *How Much Food Can We Grow in Urban Areas? Food Production and Crop Yields of Urban Agriculture: A Meta‐Analysis*, Earth's Future 10(8). doi:10.1029/2022ef002748 | Meta-analysis of 200 studies (2,062 observations): urban crop yields on par with or above conventional averages. | abstract | no | 1 | 137 |
| 3 | Langemeyer et al. 2021, *Urban agriculture: A necessary pathway towards urban resilience and global sustainability?*, Landscape and Urban Planning 210: 104055. doi:10.1016/j.landurbplan.2021.104055 | Essay on why planning keeps giving up urban and peri-urban farmland; three blind spots; frames self-sufficiency through urban agriculture. | full text | no | 2 | 394 |
| 4 | Clinton et al. 2018, *A Global Geospatial Ecosystem Services Estimate of Urban Agriculture*, Earth's Future 6(1): 40-60. doi:10.1002/2017ef000536 | Global estimate: 100 to 180 million tonnes of food a year under intensive urban agriculture. | abstract | no | 3 | 265 |

**A12.3 Water for food**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Prosser et al. 2021, *Adapting Water Management to Climate Change in the Murray–Darling Basin, Australia*, Water 13(18): 2504. doi:10.3390/w13182504 | Critical review of how well Murray-Darling Basin water management is adapted to climate change. | abstract | no | 1 | 83 |
| 2 | Grafton and Wheeler 2018, *Economics of Water Recovery in the Murray-Darling Basin, Australia*, Annual Review of Resource Economics 10(1): 487-510. doi:10.1146/annurev-resource-100517-023039 | Murray-Darling water recovery: efficiency subsidies reduced return flows; buy-backs cost less; little basin-wide gain in flows. | abstract | no | 1 | 193 |
| 3 | Grafton et al. 2018, *The paradox of irrigation efficiency*, Science 361(6404): 748-750. doi:10.1126/science.aat9314 | The paradox of irrigation efficiency: higher efficiency rarely lowers water consumption (Australian co-authors). | abstract | no | 2 | 1133 |
| 4 | Rosa et al. 2020, *Global agricultural economic water scarcity*, Science Advances 6(18). doi:10.1126/sciadv.aaz6031 | Economic water scarcity on up to 25% of cropland; sustainable irrigation there could feed 840 million more people. | abstract | no | 3 | 832 |

**A12.4 Fuel and energy in food production**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Soliman Hunter and Taylor 2021, *Long-term and short-term liquid fuel security in Australia – What role for the Great Australian Bight?*, Energy Policy 157: 112472. doi:10.1016/j.enpol.2021.112472 | As A11.7: Australian liquid fuel security; title only. | record | unknown | 1 | 2 |
| 2 | D'Odorico et al. 2018, *The Global Food‐Energy‐Water Nexus*, Reviews of Geophysics 56(3): 456-531. doi:10.1029/2017rg000591 | Food-energy-water nexus review: energy for food (US food system 16% of national energy), fertiliser, biofuel competition, trade in embodied water. | full text | no | 1 | 845 |
| 3 | Ladha-Sabur et al. 2019, *Mapping energy consumption in food manufacturing*, Trends in Food Science & Technology 86: 270-280. doi:10.1016/j.tifs.2019.02.034 | Energy used in food manufacturing and distribution; over 98% of UK food moves by road. | abstract | no | 2 | 311 |

Three candidates only; no Australian study of energy in food production since 2016 was found.


### Paper B, sections 1 and 2 (introduction; the concept and its critics)

**B1-2.a Post-2016 debate on human carrying capacity and planetary limits (critics and defenders)**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Biermann and Kim 2020, *The Boundaries of the Planetary Boundary Framework: A Critical Appraisal of Approaches to Define a “Safe Operating Space” for Humanity*, Annual Review of Environment and Resources 45(1): 497-521. doi:10.1146/annurev-environ-012320-080337 | Review of the planetary boundaries concept and the criticisms of it from earth-system science, development studies and science and technology studies. | abstract | no | 1 | 274 |
| 2 | Rees 2023, *The Human Ecology of Overshoot: Why a Major ‘Population Correction’ Is Inevitable*, World 4(3): 509-527. doi:10.3390/world4030032 | A defender of limits: humanity in overshoot, with a population correction argued to be inevitable. | abstract | no | 1 | 44 |
| 3 | O’Neill et al. 2018, *A good life for all within planetary boundaries*, Nature Sustainability 1(2): 88-95. doi:10.1038/s41893-018-0021-4 | Social thresholds against biophysical boundaries country by country; title only. | record | no | 2 | 1978 |
| 4 | Montoya et al. 2018, *Planetary Boundaries for Biodiversity: Implausible Science, Pernicious Policies*, Trends in Ecology & Evolution 33(2): 71-73. doi:10.1016/j.tree.2017.10.004 | Critique of a planetary boundary for biodiversity; title only. | record | no | 2 | 139 |

Defenders: Rees 2023; O'Neill et al. 2018 applies limits nation by nation. Critics: Biermann and Kim 2020 (a survey of criticisms), Montoya et al. 2018. All four are on planetary limits; no post-2016 work on human carrying capacity as such was found beyond those already in the register (L106, L107, L109).

**B1-2.b Use of capacity in planning**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Świąder et al. 2020, *The application of ecological footprint and biocapacity for environmental carrying capacity assessment: A new approach for European cities*, Environmental Science & Policy 105: 56-74. doi:10.1016/j.envsci.2019.12.010 | Ecological footprint and biocapacity used to assess environmental carrying capacity at city level for planning. | abstract | no | 1 | 154 |
| 2 | Zhang et al. 2018, *Index system of urban resource and environment carrying capacity based on ecological civilization*, Environmental Impact Assessment Review 68: 90-97. doi:10.1016/j.eiar.2017.11.002 | Index system for urban resource and environment carrying capacity in China; among the most cited works citing Lane 2010; title only. | record | yes (Lane 2010) | 1 | 279 |
| 3 | Qiu 2024, *Carrying Capacity and China’s Regional Functional Planning*, Carrying Capacity of China’s Resources, Environment, Population, and Economy: 151-210. doi:10.1007/978-981-99-9046-7_3 | Carrying capacity in China's regional functional planning; same book as register L108; title only. | record | unknown | 2 | 0 |
| 4 | Bolleter 2018, *The consequences of three urbanisation scenarios for northern Australia*, Australian Planner 55(2): 103-125. doi:10.1080/07293682.2019.1620302 | As A1.1: a planning paper that applies Lane 2017 to settlement scenarios. | full text | yes (Lane 2017) | 1 | 6 |

Bolleter 2018 is the only Australian planning work found that uses capacity; the others are Chinese and Polish planning applications.


### Paper B, section 3 (how the review was done)

**B3.1 Review method (narrative and critical reviews)**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Haddaway et al. 2020, *Eight problems with literature reviews and how to fix them*, Nature Ecology & Evolution 4(12): 1582-1589. doi:10.1038/s41559-020-01295-x | Eight common problems with literature reviews in environmental science and how to fix them; title only. | record | no | 1 | 313 |
| 2 | Greenhalgh et al. 2018, *Time to challenge the spurious hierarchy of systematic over narrative reviews?*, European Journal of Clinical Investigation 48(6). doi:10.1111/eci.12931 | Narrative reviews interpret and critique; they complement rather than rank below systematic reviews. | abstract | no | 1 | 1606 |
| 3 | Sukhera 2022, *Narrative Reviews: Flexible, Rigorous, and Practical*, Journal of Graduate Medical Education 14(4): 414-417. doi:10.4300/jgme-d-22-00480.1 | Narrative reviews as a distinct tradition (state-of-the-art, critical, integrative) that can be rigorous. | full text | no | 2 | 1162 |
| 4 | Snyder 2019, *Literature review as a research methodology: An overview and guidelines*, Journal of Business Research 104: 333-339. doi:10.1016/j.jbusres.2019.07.039 | Overview of review types with guidelines for conducting and judging a literature review. | abstract | no | 2 | 19702 |

Haddaway et al. 2020 is the only one from environmental science; its open copy is on a repository reached through doi.org, which refused.


### Paper B, section 4 (catalogue: families not yet covered)

**B4.7 Nutrition optimisation of diets at national scale**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Chaudhary and Krishna 2019, *Country-Specific Sustainable Diets Using Optimization Algorithm*, Environmental Science & Technology 53(13): 7694-7703. doi:10.1021/acs.est.8b06923 | Nonlinear optimisation of diets for 152 countries meeting 29 nutrient targets and five per-capita environmental limits; the national-scale representative. | abstract | no | 1 | 96 |
| 2 | Gazan et al. 2018, *Mathematical Optimization to Explore Tomorrow's Sustainable Diets: A Narrative Review*, Advances in Nutrition 9(5): 602-616. doi:10.1093/advances/nmy049 | Narrative review of 67 diet-optimisation studies: objective functions, constraints and what infeasibility signals. | abstract | no | 1 | 222 |
| 3 | Ridoutt et al. 2021, *Diets within planetary boundaries: What is the potential of dietary change alone?*, Sustainable Production and Consumption 28: 802-810. doi:10.1016/j.spc.2021.07.009 | 9,341 Australian adult diets scored on climate, water-scarcity and cropland-scarcity footprints against the dietary guidelines. | abstract | no | 2 | 49 |
| 4 | Van Dooren 2018, *A Review of the Use of Linear Programming to Optimize Diets, Nutritiously, Economically and Environmentally*, Frontiers in Nutrition 5. doi:10.3389/fnut.2018.00048 | Review of linear programming for diets (52 papers), 12 with ecological constraints compared in detail. | full text | no | 2 | 191 |

**B4.8 Integrated resource-flow or stocks-and-flows models**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Gao and Bryan 2017, *Finding pathways to national-scale land-sector sustainability*, Nature 544(7649): 217-222. doi:10.1038/nature21694 | Pathways to national-scale land-sector sustainability for Australia from an integrated land-use model; title only. | record | no | 1 | 460 |
| 2 | Navarro Garcia et al. 2022, *Multi-target scenario discovery to plan for sustainable food and land systems in Australia*, Sustainability Science 18(1): 371-388. doi:10.1007/s11625-022-01202-2 | Multi-target scenario discovery for sustainable food and land systems in Australia (FABLE); title only. | record | no | 1 | 18 |
| 3 | Herrington 2020, *Update to limits to growth: Comparing the World3 model with empirical data*, Journal of Industrial Ecology 25(3): 614-626. doi:10.1111/jiec.13084 | World3 scenarios compared with empirical data, updating Turner's comparisons; the Limits to Growth line of integrated models. | abstract | no | 2 | 243 |
| 4 | Jones et al. 2023, *Integrated modeling to achieve global goals: lessons from the Food, Agriculture, Biodiversity, Land-use, and Energy (FABLE) initiative*, Sustainability Science 18(1): 323-333. doi:10.1007/s11625-023-01290-8 | FABLE overview: participatory integrated food, land and energy models for 12 countries including Australia. | full text | no | 3 | 28 |

Gao and Bryan 2017 and Navarro Garcia et al. 2022 are Australian national integrated models (the latter in the FABLE series that Jones et al. 2023 introduces). MAgPIE 4 (Dietrich et al. 2019, doi:10.5194/gmd-12-1299-2019, read in full) is a fifth, global, option. No method paper for the Australian Stocks and Flows Framework after 2016 was found.

**B4.9 Water-bounded capacity**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Mesgaran et al. 2017, *Iran’s Land Suitability for Agriculture*, Scientific Reports 7(1). doi:10.1038/s41598-017-08066-y | Land suitability for crops in Iran from soil, terrain and climate; low rainfall and water limit food self-sufficiency. | full text | no | 1 | 207 |
| 2 | Rosa et al. 2018, *Closing the yield gap while ensuring water sustainability*, Environmental Research Letters 13(10): 104002. doi:10.1088/1748-9326/aadeef | Global irrigation could expand by 48% without breaching environmental flows; a water bound on production. | full text | no | 1 | 235 |
| 3 | Kummu et al. 2016, *The world’s road to water scarcity: shortage and stress in the 20th century and pathways towards sustainability*, Scientific Reports 6(1). doi:10.1038/srep38495 | Water shortage and stress over the 20th century; per-capita consumption in Australia-Pacific rose more than six-fold. | full text | no | 2 | 1020 |
| 4 | Yi et al. 2018, *Research Methods of Water Resources Carrying Capacity: Progress and Prospects*, Journal of Resources and Ecology 9(5): 455-460. doi:10.5814/j.issn.1674-764x.2018.05.001 | Review of water resources carrying capacity methods (trend, system dynamics, multi-objective, comprehensive evaluation). | abstract | no | 2 | 17 |

Mesgaran et al. 2017 and Rosa et al. 2018 bound production by land and water; neither converts to a population count, so they are family representatives, not comparators.


### Paper B, section 8 (what no method does)

**B8.1 What no method does: variability**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Cottrell et al. 2019, *Food production shocks across land and sea*, Nature Sustainability 2(2): 130-137. doi:10.1038/s41893-018-0210-1 | Food production shocks 1961 to 2013 across crops, livestock, fisheries and aquaculture; shock frequency has risen. | abstract | no | 1 | 382 |
| 2 | Gaupp et al. 2019, *Changing risks of simultaneous global breadbasket failure*, Nature Climate Change 10(1): 54-57. doi:10.1038/s41558-019-0600-z | Risk of simultaneous breadbasket failure is rising; rainfall risk for wheat increased in Australia. | full text | no | 1 | 307 |
| 3 | Anderson et al. 2019, *Synchronous crop failures and climate-forced production variability*, Science Advances 5(7). doi:10.1126/sciadv.aaw1976 | Climate modes (ENSO, IOD and others) account for 18, 7 and 6% of global maize, soybean and wheat variability. | abstract | no | 2 | 244 |
| 4 | Hochman et al. 2017, *Climate trends account for stalled wheat yields in Australia since 1990*, Global Change Biology 23(5): 2071-2081. doi:10.1111/gcb.13604 | As A1.5: Australian wheat yield potential fell 27% from 1990 to 2015. | abstract | no | 2 | 301 |

**B8.2 What no method does: trade**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Kinnunen et al. 2020, *Local food crop production can fulfil demand for less than one-third of the population*, Nature Food 1(4): 229-237. doi:10.1038/s43016-020-0060-7 | As A12.1: local production meets crop demand for under a third of people. | abstract | no | 1 | 243 |
| 2 | Clapp 2017, *Food self-sufficiency: Making sense of it, and when it makes sense*, Food Policy 66: 88-96. doi:10.1016/j.foodpol.2016.12.001 | As A12.1: self-sufficiency and trade are a continuum. | abstract | no | 1 | 573 |
| 3 | Kummu et al. 2020, *Interplay of trade and food system resilience: Gains on supply diversity over time at the cost of trade independency*, Global Food Security 24: 100360. doi:10.1016/j.gfs.2020.100360 | As A11.7: diversity gained through trade at the cost of import dependence. | abstract | no | 2 | 226 |
| 4 | Marchand et al. 2016, *Reserves and trade jointly determine exposure to food supply shocks*, Environmental Research Letters 11(9): 095009. doi:10.1088/1748-9326/11/9/095009 | As A11.4: reserves and trade jointly set exposure to shocks. | full text | no | 2 | 149 |

**B8.3 What no method does: energy**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | D'Odorico et al. 2018, *The Global Food‐Energy‐Water Nexus*, Reviews of Geophysics 56(3): 456-531. doi:10.1029/2017rg000591 | As A12.4: the food-energy-water nexus. | full text | no | 1 | 845 |
| 2 | Ladha-Sabur et al. 2019, *Mapping energy consumption in food manufacturing*, Trends in Food Science & Technology 86: 270-280. doi:10.1016/j.tifs.2019.02.034 | As A12.4: energy in food manufacturing and transport. | abstract | no | 2 | 311 |
| 3 | Soliman Hunter and Taylor 2021, *Long-term and short-term liquid fuel security in Australia – What role for the Great Australian Bight?*, Energy Policy 157: 112472. doi:10.1016/j.enpol.2021.112472 | As A11.7: Australian liquid fuel security; title only. | record | unknown | 2 | 2 |

**B8.4 What no method does: diet dynamics**

| Rank | Work | Why | Read | Cites Lane | Priority | Cited by (OpenAlex) |
|---|---|---|---|---|---|---|
| 1 | Bodirsky et al. 2020, *The ongoing nutrition transition thwarts long-term targets for food security, public health and environmental protection*, Scientific Reports 10(1). doi:10.1038/s41598-020-75213-3 | Nutrition transition to 2050: food demand rises from 30 to 45 EJ, diets shift to animal-source foods and empty calories. | full text | no | 1 | 255 |
| 2 | Whitton et al. 2021, *Are We Approaching Peak Meat Consumption? Analysis of Meat Consumption from 2000 to 2019 in 35 Countries and Its Relationship to Gross Domestic Product*, Animals 11(12): 3466. doi:10.3390/ani11123466 | Meat consumption in 35 countries 2000 to 2019: some near a peak, poultry up, beef and mutton down; Australian beef output fell 15% in the 2019 drought. | full text | no | 1 | 258 |
| 3 | Bentham et al. 2020, *Multidimensional characterization of global food supply from 1961 to 2013*, Nature Food 1(1): 70-75. doi:10.1038/s43016-019-0012-2 | Global food supply 1961 to 2013 characterised along several dimensions; title only. | record | no | 2 | 96 |

---

## Year mix per section

Register works are those B61 placed on hand for each section (its column (a); A1 includes the B1.1 works that A1.2 points to); a work counted in two sections of a paper is counted in each. "Undated" are register entries with no year (Nix, Sustainable Population Australia, the Noosa and Douglas Shire studies, the CSIRO 340-litre figure); they belong to the years before 2016 by context. Candidates are the distinct works in the csv for that section (Bolleter 2018 counts in A1 and in B1 and B2). The last column is the share from 2016 on, of all dated works.

| Section | Register: before 2016 | Register: 2016 to 2019 | Register: 2020 to 2026 | Register: undated | Candidates: 2016 to 2019 | Candidates: 2020 to 2026 | Candidates: before 2016 | All: before 2016 | All: 2016 to 2019 | All: 2020 to 2026 | Share 2016 on (all dated) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | 23 | 7 | 1 | 1 | 5 | 7 | 0 | 23 | 12 | 8 | 47% |
| A11 | 12 | 8 | 4 | 0 | 11 | 12 | 0 | 12 | 19 | 16 | 74% |
| A12 | 6 | 1 | 3 | 1 | 6 | 9 | 0 | 6 | 7 | 12 | 76% |
| B1 and B2 | 26 | 5 | 6 | 3 | 4 | 4 | 0 | 26 | 9 | 10 | 42% |
| B3 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 2 | 2 | 100% |
| B4 | 39 | 14 | 7 | 3 | 8 | 4 | 0 | 39 | 22 | 11 | 46% |
| B8 | 14 | 3 | 1 | 1 | 8 | 6 | 0 | 14 | 11 | 7 | 56% |

Reading the table: with the candidates added, every section of Paper A has at least as many works from 2016 on as before 2016 (A11 and A12 about three in four), while Paper B's concept and catalogue sections stay mostly older (B1 and B2 at 42%, B4 at 46%) because their founding literature is old by nature. B3 had nothing in the register and gets four works from 2018 to 2022.

## Twenty works worth acquiring that are not open

Ranked by need: Australian works for uncovered or thin points first, then works serving several points, then family representatives. All twenty are closed on OpenAlex. Three closed candidates are left off the list as lower priority: Timmer 2024 (A11.4), Sysak 2017 (A11.5) and Yi et al. 2018 (B4.9).

| # | Work | Points | Cited by (OpenAlex) | QUT library search | DOI |
|---|---|---|---|---|---|
| 1 | Hochman et al. 2017, "Climate trends account for stalled wheat yields in Australia since 1990", Global Change Biology 23(5): 2071-2081 | A1.5, B8.1 | 301 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Climate%20trends%20account%20for%20stalled%20wheat%20yields%20in%20Australia%20since%201990&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1111/gcb.13604 |
| 2 | Mcdougall et al. 2020, "Urban agriculture could provide 15% of food supply to Sydney, Australia, under expanded land use scenarios", Land Use Policy 94: 104554 | A12.2 | 70 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Urban%20agriculture%20could%20provide%2015%25%20of%20food%20supply%20to%20Sydney%2C%20Australia%2C%20under%20expanded%20land%20use%20scenarios&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1016/j.landusepol.2020.104554 |
| 3 | Reutter et al. 2017, "The challenge of characterising food waste at a national level: An Australian example", Environmental Science & Policy 78: 157-166 | A11.3 | 27 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,The%20challenge%20of%20characterising%20food%20waste%20at%20a%20national%20level%3A%20An%20Australian%20example&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1016/j.envsci.2017.09.014 |
| 4 | Botterill 2021, "From National Drought Policy to National Drought Agreement: the evolution of Australia’s drought response", The Rangeland Journal 43(3): 77-86 | A11.5 | 12 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,From%20National%20Drought%20Policy%20to%20National%20Drought%20Agreement%3A%20the%20evolution%20of%20Australia%E2%80%99s%20drought%20response&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1071/rj20065 |
| 5 | Soliman Hunter and Taylor 2021, "Long-term and short-term liquid fuel security in Australia – What role for the Great Australian Bight?", Energy Policy 157: 112472 | A11.7, A12.4, B8.3 | 2 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Long-term%20and%20short-term%20liquid%20fuel%20security%20in%20Australia%20%E2%80%93%20What%20role%20for%20the%20Great%20Australian%20Bight%3F&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1016/j.enpol.2021.112472 |
| 6 | Mayberry et al. 2019, "Pathways to carbon-neutrality for the Australian red meat sector", Agricultural Systems 175: 13-21 | A11.1 | 81 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Pathways%20to%20carbon-neutrality%20for%20the%20Australian%20red%20meat%20sector&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1016/j.agsy.2019.05.009 |
| 7 | Higgins et al. 2018, "Informing transport infrastructure investments using TraNSIT: A case study for Australian agriculture and forestry", Computers and Electronics in Agriculture 154: 187-203 | A11.6 | 19 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Informing%20transport%20infrastructure%20investments%20using%20TraNSIT%3A%20A%20case%20study%20for%20Australian%20agriculture%20and%20forestry&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1016/j.compag.2018.09.008 |
| 8 | Grafton and Wheeler 2018, "Economics of Water Recovery in the Murray-Darling Basin, Australia", Annual Review of Resource Economics 10(1): 487-510 | A12.3 | 193 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Economics%20of%20Water%20Recovery%20in%20the%20Murray-Darling%20Basin%2C%20Australia&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1146/annurev-resource-100517-023039 |
| 9 | Chaudhary and Krishna 2019, "Country-Specific Sustainable Diets Using Optimization Algorithm", Environmental Science & Technology 53(13): 7694-7703 | B4.7 | 96 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Country-Specific%20Sustainable%20Diets%20Using%20Optimization%20Algorithm&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1021/acs.est.8b06923 |
| 10 | Herrington 2020, "Update to limits to growth: Comparing the World3 model with empirical data", Journal of Industrial Ecology 25(3): 614-626 | B4.8 | 243 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Update%20to%20limits%20to%20growth%3A%20Comparing%20the%20World3%20model%20with%20empirical%20data&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1111/jiec.13084 |
| 11 | Zhang et al. 2018, "Index system of urban resource and environment carrying capacity based on ecological civilization", Environmental Impact Assessment Review 68: 90-97 | B1-2.b | 279 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Index%20system%20of%20urban%20resource%20and%20environment%20carrying%20capacity%20based%20on%20ecological%20civilization&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1016/j.eiar.2017.11.002 |
| 12 | O’Neill et al. 2018, "A good life for all within planetary boundaries", Nature Sustainability 1(2): 88-95 | B1-2.a | 1978 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,A%20good%20life%20for%20all%20within%20planetary%20boundaries&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1038/s41893-018-0021-4 |
| 13 | James and O'Neill 2016, "Planning for Peri-urban Agriculture: a geographically-specific, evidence-based approach from Sydney", Australian Geographer 47(2): 179-194 | A1.4 | 34 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Planning%20for%20Peri-urban%20Agriculture%3A%20a%20geographically-specific%2C%20evidence-based%20approach%20from%20Sydney&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1080/00049182.2015.1130676 |
| 14 | Wiedemann et al. 2016, "Resource use and greenhouse gas emissions from grain-finishing beef cattle in seven Australian feedlots: a life cycle assessment", Animal Production Science 57(6): 1149-1162 | A11.1 | 21 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Resource%20use%20and%20greenhouse%20gas%20emissions%20from%20grain-finishing%20beef%20cattle%20in%20seven%20Australian%20feedlots%3A%20a%20life%20cycle%20assessment&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1071/an15454 |
| 15 | Hughes and Lawson 2017, "Climate adjusted productivity on Australian cropping farms", New Directions in Productivity Measurement and Efficiency Analysis | A11.5 | 14 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Climate%20adjusted%20productivity%20on%20Australian%20cropping%20farms&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.4337/9781786432421.00012 |
| 16 | Wood et al. 2018, "Trade and the equitability of global food nutrient distribution", Nature Sustainability 1(1): 34-37 | A11.7 | 169 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Trade%20and%20the%20equitability%20of%20global%20food%20nutrient%20distribution&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1038/s41893-017-0008-6 |
| 17 | Spang et al. 2019, "Food Loss and Waste: Measurement, Drivers, and Solutions", Annual Review of Environment and Resources 44(1): 117-156 | A11.3 | 284 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Food%20Loss%20and%20Waste%3A%20Measurement%2C%20Drivers%2C%20and%20Solutions&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1146/annurev-environ-101718-033228 |
| 18 | Qiu 2024, "Carrying Capacity and China’s Regional Functional Planning", Carrying Capacity of China’s Resources, Environment, Population, and Economy: 151-210 | B1-2.b | 0 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Carrying%20Capacity%20and%20China%E2%80%99s%20Regional%20Functional%20Planning&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1007/978-981-99-9046-7_3 |
| 19 | Higgins et al. 2018, "Informing major government programs for rural transport infrastructure in northern Australia", The Rangeland Journal 40(4): 341-351 | A11.6 | 5 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Informing%20major%20government%20programs%20for%20rural%20transport%20infrastructure%20in%20northern%20Australia&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1071/rj18008 |
| 20 | Han et al. 2024, "Strategic cropland reserves can strengthen China’s food security", Nature Food 5(7): 535-538 | A11.4 | 20 | https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Strategic%20cropland%20reserves%20can%20strengthen%20China%E2%80%99s%20food%20security&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT | https://doi.org/10.1038/s43016-024-01015-9 |

## Open works not read here (host refused or served a holding page)

These 39 are open on OpenAlex and can be downloaded by hand from the publisher or repository: Parr 2018; McDonald 2017; Summerhayes and Baker 2024, 2025 and 2026; Hughes et al. 2022 (Climatic Change); Hughes et al. 2022 (Climate Risk Management); Falster et al. 2024; Wittwer and Waschik 2021; Malau-Aduli et al. 2022; Ridoutt 2024; Mirosa et al. 2020; Ananda et al. 2023; Davis et al. 2020; Kummu et al. 2020; Ritzel et al. 2024; Clapp 2017; Kinnunen et al. 2020; Schreiber et al. 2021; Payen et al. 2022; Clinton et al. 2018; Prosser et al. 2021; Grafton et al. 2018; Rosa et al. 2020; Ladha-Sabur et al. 2019; Biermann and Kim 2020; Rees 2023; Montoya et al. 2018; Świąder et al. 2020; Haddaway et al. 2020; Greenhalgh et al. 2018; Snyder 2019; Gazan et al. 2018; Ridoutt et al. 2021; Gao and Bryan 2017; Navarro Garcia et al. 2022; Cottrell et al. 2019; Anderson et al. 2019; Bentham et al. 2020. The DOIs are in the csv. The five to fetch first, because they carry Australian points at priority 1: Summerhayes and Baker 2026, Hughes et al. 2022 (both), Gao and Bryan 2017 and Navarro Garcia et al. 2022.

## Summary

The sweep found 78 works from 2016 to 2026 (38 from 2016 to 2019, 40 from 2020 to 2026) for the 23 thin or uncovered points, none already in the register; 16 were read in full, 45 from the abstract and 17 from the record alone, and two cite Lane (Bolleter 2018, Lane 2017; Zhang et al. 2018, Lane 2010). Paper A gains most: the food-security point gains an Australian policy literature from 2024 to 2026 (Summerhayes and Baker, three papers on 102 state and national food policies and on planning), observed drought has the ABARES farm-profit estimate (22.3% lower under post-2000 climate), the 27% fall in wheat yield potential and two studies of the 2017 to 2019 drought, and drought resilience has the history of the National Drought Agreement and the ABARES drought indicator. Points that stay thin are those where the evidence is Australian government reporting with no Crossref or OpenAlex record (the Intergenerational Reports and Population Statements, the 2023 parliamentary inquiry, the National Food Waste Baseline, the Future Drought Fund reviews) and those with no Australian academic work found at all (grain reserves, interregional food freight beyond the TraNSIT papers, food import dependence, energy in food production). For Paper B the sweep supplies the review-method literature that B3 lacked, national-scale diet optimisation (Chaudhary and Krishna 2019), two Australian integrated land-system models (Gao and Bryan 2017; Navarro Garcia et al. 2022) and water-bounded production work, while its concept and catalogue sections remain weighted to older founding works, as the year mix shows.
