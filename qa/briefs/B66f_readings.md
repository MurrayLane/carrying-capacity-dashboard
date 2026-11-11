# Reading brief B66f: Paper B sections 4 and 8: nutrition optimisation, integrated models, water-bounded capacity, what no method does (targeted reads)

Write only `qa/reports/B66f_readings.csv` and `qa/reports/B66f_readings.md`.

Rules. Plain language; no time words; no em dashes. Decision 33 applies: say what a paper does and what it finds; no verdicts on other authors' shortcomings. Do not edit `qa/literature_register.csv` or any file other than your two outputs. No git; no subagents; no network. The papers are on disk under `/home/user/carrying-capacity-models/Literature review/` at the `local_path` in each register row (drop the leading `carrying-capacity-models/`); use `pdftotext` (and `pdftotext -layout` for tables); a `.md` file is a full text rendered from PubMed Central and is read as is. Open each file and confirm first that it is the paper the row names (title, authors, year); if it is not, say so and stop on that row.

Each row carries a current characterisation: its `what_taken` text and the "why" line in its `notes` (from the B61 or B63 sweeps, written from the abstract or the record). Your job is to test that characterisation against the paper and record what the paper actually supports, with page numbers.

Depth. TARGETED: read the abstract, introduction, results summary, conclusions and any table or figure the characterisation rests on; enough to confirm or correct the line and take the one or two facts the paper is wanted for. FULL: read the whole paper; take every figure the paper is wanted for and the method and base year behind each. The list below says which.

Output 1: `qa/reports/B66f_readings.csv` with columns `id, file_ok, depth, holds, what_taken, figures, flags, notes`. `holds` is yes / partly / no (does the current characterisation hold?). `what_taken` is the new register text, at most 70 words, concrete, with page numbers. `figures` lists each number taken as "value; unit; base year; page". `flags` names anything that changes a claim in the papers or a line in `papers/A_results/OUTLINE.md` or `papers/B_methods/OUTLINE.md` (name the section), or "none". Quote page numbers from the PDF's own pagination.

Output 2: `qa/reports/B66f_readings.md`: one paragraph per paper (plain language, at most 120 words), then a closing list of flags, then the register rows you touched (all the ids below), then the words "Wrong-value check:" with one deliberate example of a characterisation that would NOT hold, so a checker can see the test can fail (mark it clearly as an example, not a finding).

Depth for every row in this brief: TARGETED.

Rows:
- L204: Chaudhary 2019, "Country-Specific Sustainable Diets Using Optimization Algorithm", Environmental Science & Technology 53(13): 7694-7703. doi:10.1021/acs.est.8b0
  file: Literature review/Chaudhary2019.pdf
  current: Nonlinear optimisation of diets for 152 countries meeting 29 nutrient targets and five per-capita environmental limits; the national-scale representative.
  why: priority 1; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (section 4, B4.7 Nutrition optimisation of diets at national scale)
- L205: Gazan 2018, "Mathematical Optimization to Explore Tomorrow's Sustainable Diets: A Narrative Review", Advances in Nutrition 9(5): 602-616. doi:10.1093/advances/n
  file: Literature review/Gazan2018_Advances_in_Nutrition_Mathematical_Optimization_to_Explore_Tomorrow_s_Sustainable_Diets_A_fulltext_PMC.md
  current: Narrative review of 67 diet-optimisation studies: objective functions, constraints and what infeasibility signals.
  why: priority 1; open access yes; filed 2026-11-10: open-access full text from PubMed Central (JATS XML and a text rendering; not the publisher PDF) fetched by the coordinator (Europe PMC API)
  used by: methods paper (section 4, B4.7 Nutrition optimisation of diets at national scale)
- L206: Ridoutt 2021, "Diets within planetary boundaries: What is the potential of dietary change alone?", Sustainable Production and Consumption 28: 802-810. doi:10.10
  file: Literature review/Ridoutt2021.pdf
  current: 9,341 Australian adult diets scored on climate, water-scarcity and cropland-scarcity footprints against the dietary guidelines.
  why: priority 2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (section 4, B4.7 Nutrition optimisation of diets at national scale)
- L208: Gao 2017, "Finding pathways to national-scale land-sector sustainability", Nature 544(7649): 217-222. doi:10.1038/nature21694
  file: Literature review/Gao2017.pdf
  current: Pathways to national-scale land-sector sustainability for Australia from an integrated land-use model; title only.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (section 4, B4.8 Integrated resource-flow or stocks-and-flows models)
- L209: Navarro Garcia 2022, "Multi-target scenario discovery to plan for sustainable food and land systems in Australia", Sustainability Science 18(1): 371-388. doi:10
  file: Literature review/NavarroGarcia2022_Sustainability_Science_Multi_target_scenario_discovery_to_plan_for_sustainable_food_fulltext_PMC.md
  current: Multi-target scenario discovery for sustainable food and land systems in Australia (FABLE); title only.
  why: priority 1; open access yes; filed 2026-11-10: open-access full text from PubMed Central (JATS XML and a text rendering; not the publisher PDF) fetched by the coordinator (Europe PMC API)
  used by: methods paper (section 4, B4.8 Integrated resource-flow or stocks-and-flows models)
- L210: Herrington 2020, "Update to limits to growth: Comparing the World3 model with empirical data", Journal of Industrial Ecology 25(3): 614-626. doi:10.1111/jiec.13
  file: Literature review/Herrington2020.pdf
  current: World3 scenarios compared with empirical data, updating Turner's comparisons; the Limits to Growth line of integrated models.
  why: priority 2; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (section 4, B4.8 Integrated resource-flow or stocks-and-flows models)
- L215: Yi 2018, "Research Methods of Water Resources Carrying Capacity: Progress and Prospects", Journal of Resources and Ecology 9(5): 455-460. doi:10.5814/j.issn.167
  file: Literature review/Yi2018.pdf
  current: Review of water resources carrying capacity methods (trend, system dynamics, multi-objective, comprehensive evaluation).
  why: priority 2; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (section 4, B4.9 Water-bounded capacity)
- L216: Cottrell 2019, "Food production shocks across land and sea", Nature Sustainability 2(2): 130-137. doi:10.1038/s41893-018-0210-1
  file: Literature review/Cottrell2019.pdf
  current: Food production shocks 1961 to 2013 across crops, livestock, fisheries and aquaculture; shock frequency has risen.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (section 8, B8.1 What no method does: variability)
- L221: Bentham 2020, "Multidimensional characterization of global food supply from 1961 to 2013", Nature Food 1(1): 70-75. doi:10.1038/s43016-019-0012-2
  file: Literature review/Bentham2020_Nature_Food_Multidimensional_characterization_of_global_food_supply_from_1961_to.pdf
  current: Global food supply 1961 to 2013 characterised along several dimensions; title only.
  why: priority 2; open access yes; filed 2026-11-10: open-access PDF fetched by the coordinator (Unpaywall location)
  used by: methods paper (section 8, B8.4 What no method does: diet dynamics)
