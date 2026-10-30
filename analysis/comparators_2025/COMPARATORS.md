# Other estimates to compare the model with (candidate article)

Murray, 2026-10-30: could one article compare the modelling with other authors' estimates made with different methods? Yes. The comparison is meaningful only after the estimates are put on a common footing, because they answer different questions. This register lists the candidates, what each measures, and what has and has not been verified. **"Found" means a search result reported it; nothing here has yet been checked against the primary source.** Verify each before it goes in a paper.

## The model's own figures to compare (Australia, millions of people; `results/`)

Short term (today's diet, today's settings): 49.4 published method, 41.5 corrected, 45.7 improved. Long term (low-meat diet, no avoidable waste, 100% organic, 100-year drought allowance): 14.1, 15.6, 14.6. The 2011 thesis result was 40.4 and 9.4; 33.3 and 15.35 corrected. Quick range of the improved cell: 39 to 50 short term, 13 to 17 long term. Optimised-diet bounds: 69 (better choice of food within today's groups), 195 and 387 (group-free, macronutrients only).

## Candidates

| Class | Estimate | Found | What it measures | Method | Comparable how |
|---|---|---|---|---|---|
| Same author | Lane et al. 2014 (*Ecological Modelling*), 2015, 2017 (*Population and Environment*) | 40 million national, 9 to 40 million by time frame, 23 million summed over regions | Domestic land-based capacity, one diet | This model | The baseline: show the corrected and updated figures against it |
| Production and trade | Bellotti, *The Conversation* 2017, "How many people can Australia feed?" | Exports feed about 36.6 million; with the population, about 61 million "fed" | People supplied with food energy from Australian output, exports included | Energy balance of production | The model's production-over-consumption check (`analysis/external_anchors_2025`) is the same family; reconcile by netting exports and imports and by diet |
| Production and trade | CSIRO and University of Queensland, national food-system stocktake (June 2025) | About 100 million fed, 27 million of them Australians | Energy supplied by the food system, exports at the diets they feed | Food-system accounting | As above (`analysis/external_anchors_2025/README.md`) |
| Production and trade | Industry claims (National Farmers' Federation and others) | "Feeds 75 million" (reported by Country News); grain harvest enough for about 60 million in an average year and 30 million in a bad drought year (reported) | People supplied by production, exports included | Calories per person | The model's drought treatment (resilience table) gives the same two numbers a defined meaning |
| Integrated resource model | Foran and Poldy, *Future Dilemmas*, CSIRO 2002 | Three population paths to 2050: 20, 25 and 32 million; Foran later argued 26 to 28 million would be more resilient | Resource, energy, water and materials flows under population scenarios | Integrated system model of physical flows | Not a capacity figure; compare method (what binds first) rather than number |
| Parliamentary / expert | Australian Academy of Science 1995 | Stabilise at about 23 million | A policy position | Expert judgement | Context only |
| Parliamentary / expert | House of Representatives inquiry (Jones, 1994) | 30 to 35 million if food limits and bad seasons are allowed for | A committee's estimate | Evidence and judgement | Close to the model's short term corrected, with a drought allowance |
| Advocacy | Sustainable Population Australia | Stabilise below 30 million | Advocacy position | Argument | State the nature of the source; do not treat as an estimate |
| Land-based diet models (other countries) | Peters et al. 2016, *Elementa* 4: ten diet scenarios for US agricultural land | Carrying capacity higher for less meat diets; lacto-vegetarian highest; highly sensitive to the cropland assumed | People supported by US agricultural land under 10 diets | Land and diet simulation (the family the model belongs to) | Same method class: compare the ordering of diets and the sensitivity to land, not the number |
| Land-based diet models | Peters et al. 2009, New York foodsheds | Most population centres could source most food in-state except New York City | Spatial self-sufficiency | GIS and optimisation | Compare with the scale paper (paper 2) |
| Yield metric | Cassidy et al. 2013, *Environmental Research Letters* 8: 034015 | People nourished per hectare, not tonnes per hectare | Calories and protein delivered to people | Crop use accounting | Compare with the nutrition-constrained results (`analysis/nutrition_lp_2025`) |
| Footprint | Alexander et al. 2016, *Global Environmental Change* 41: 88: the HALF index | Land to feed the world on a country's average diet, as a share of habitable land | Land for diet | Per-capita land by commodity | Convert the model's land per person on the Australian diet to the same metric |
| Global biophysical | FAO and IIASA agro-ecological zones (Fischer and others), the FAO "potential population supporting capacities of lands" studies | Not searched | Potential of land for food at defined input levels | Agro-ecological suitability | Upper-bound comparison (SCOPE E12, GAEZ not yet done) |
| Footprint | Global Footprint Network, ecological footprint and biocapacity accounts | Not searched | Biocapacity against demand | Footprint accounting | A different quantity (renewable resource demand); cite with care |

## What a fair comparison needs

1. **A shared definition.** Domestic people fed on a stated diet from domestic land (the model), or people supplied with energy including exports (CSIRO, Bellotti, industry)? Say which, and convert.
2. **The same diet and the same year.** Meat share, waste, drought allowance, organic share, fuel and the land base all differ; the model can be re-run under each source's assumptions where they are stated (for example, no avoidable waste; energy only; average rather than worst-year yields).
3. **A method class for each**: energy-balance of production, grain-per-capita, integrated resource model, land-and-diet simulation, expert or policy judgement, advocacy. The article's point can be that the estimates differ by 5 to 10 times mostly because of the definition, and by a factor of 1.5 to 2 within the land-based class.

## Next steps if the article is written

* Fetch and read the primary sources (Foran and Poldy 2002; the Jones committee report; the Academy report; Bellotti 2017; the CSIRO stocktake; Peters 2016; Alexander 2016; Cassidy 2013) and replace "found" with the exact numbers and definitions.
* Build the harmonisation table (each estimate, its definition, and the model re-run on the same definition where possible).
* Decide where it sits in `PUBLICATIONS.md` (a fifth paper, or a section of paper 1 or paper 3).
