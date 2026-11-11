# Reading brief B66b: Paper A section 11: livestock, food waste, grain reserves (targeted reads)

Write only `qa/reports/B66b_readings.csv` and `qa/reports/B66b_readings.md`.

Rules. Plain language; no time words; no em dashes. Decision 33 applies: say what a paper does and what it finds; no verdicts on other authors' shortcomings. Do not edit `qa/literature_register.csv` or any file other than your two outputs. No git; no subagents; no network. The papers are on disk under `/home/user/carrying-capacity-models/Literature review/` at the `local_path` in each register row (drop the leading `carrying-capacity-models/`); use `pdftotext` (and `pdftotext -layout` for tables); a `.md` file is a full text rendered from PubMed Central and is read as is. Open each file and confirm first that it is the paper the row names (title, authors, year); if it is not, say so and stop on that row.

Each row carries a current characterisation: its `what_taken` text and the "why" line in its `notes` (from the B61 or B63 sweeps, written from the abstract or the record). Your job is to test that characterisation against the paper and record what the paper actually supports, with page numbers.

Depth. TARGETED: read the abstract, introduction, results summary, conclusions and any table or figure the characterisation rests on; enough to confirm or correct the line and take the one or two facts the paper is wanted for. FULL: read the whole paper; take every figure the paper is wanted for and the method and base year behind each. The list below says which.

Output 1: `qa/reports/B66b_readings.csv` with columns `id, file_ok, depth, holds, what_taken, figures, flags, notes`. `holds` is yes / partly / no (does the current characterisation hold?). `what_taken` is the new register text, at most 70 words, concrete, with page numbers. `figures` lists each number taken as "value; unit; base year; page". `flags` names anything that changes a claim in the papers or a line in `papers/A_results/OUTLINE.md` or `papers/B_methods/OUTLINE.md` (name the section), or "none". Quote page numbers from the PDF's own pagination.

Output 2: `qa/reports/B66b_readings.md`: one paragraph per paper (plain language, at most 120 words), then a closing list of flags, then the register rows you touched (all the ids below), then the words "Wrong-value check:" with one deliberate example of a characterisation that would NOT hold, so a checker can see the test can fail (mark it clearly as an example, not a finding).

Depth for every row in this brief: TARGETED.

Rows:
- L156: Mayberry 2019, "Pathways to carbon-neutrality for the Australian red meat sector", Agricultural Systems 175: 13-21. doi:10.1016/j.agsy.2019.05.009
  file: Literature review/Mayberry2019.pdf
  current: CSIRO pathways to carbon neutrality for the Australian red meat sector, built on national herd and productivity assumptions; title only.
  why: priority 1; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.1 Livestock productivity in Australia)
- L157: Wiedemann 2016, "Resource use and greenhouse gas emissions from grain-finishing beef cattle in seven Australian feedlots: a life cycle assessment", Animal Produ
  file: Literature review/Weidermann2015.pdf
  current: Life cycle assessment of seven eastern Australian feedlots: water, fossil energy and emissions per kg of liveweight gain.
  why: priority 2; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.1 Livestock productivity in Australia)
- L158: Malau-Aduli 2022, "Genetics and nutrition impacts on herd productivity in the Northern Australian beef cattle production cycle", Veterinary and Animal Science 1
  file: Literature review/MalauAduli2022_Veterinary_and_Animal_Science_Genetics_and_nutrition_impacts_on_herd_productivity_in_the_fulltext_PMC.md
  current: Review of genetic and nutritional limits on northern Australian beef herd productivity on phosphorus-deficient tropical pastures.
  why: priority 2; open access yes; filed 2026-11-10: open-access full text from PubMed Central (JATS XML and a text rendering; not the publisher PDF) fetched by the coordinator (Europe PMC API)
  used by: results paper (section 11, A11.1 Livestock productivity in Australia)
- L160: Reutter 2017, "The challenge of characterising food waste at a national level: An Australian example", Environmental Science & Policy 78: 157-166. doi:10.1016/j
  file: Literature review/Reutter2017.pdf
  current: Characterising food waste at the national level for Australia, published the year of the National Food Waste Strategy; title only (its Lane is a co-author of that name, not the model's author).
  why: priority 1; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.3 Australian food waste (National Food Waste Strategy and baseline))
- L161: Mirosa 2020, "Food Waste in Australia and New Zealand", Routledge Handbook of Food Waste: 225-236. doi:10.4324/9780429462795-18
  file: Literature review/Mirosa2020.pdf
  current: Reviews food-waste research and the history of food-waste policy in Australia and New Zealand.
  why: priority 2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.3 Australian food waste (National Food Waste Strategy and baseline))
- L162: Ananda 2023, "Quantifying the effects of food management routines on household food waste", Journal of Cleaner Production 391: 136230. doi:10.1016/j.jclepro.202
  file: Literature review/Ananda2023.pdf
  current: National Australian household survey (n = 4324) linking food planning and storage routines to the amount wasted.
  why: priority 2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.3 Australian food waste (National Food Waste Strategy and baseline))
- L163: Spang 2019, "Food Loss and Waste: Measurement, Drivers, and Solutions", Annual Review of Environment and Resources 44(1): 117-156. doi:10.1146/annurev-environ-1
  file: Literature review/Spang2019.pdf
  current: Global synthesis: definitions of loss and waste are inconsistent and data gaps large; context for any national baseline.
  why: priority 3; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.3 Australian food waste (National Food Waste Strategy and baseline))
- L166: Han 2024, "Strategic cropland reserves can strengthen China’s food security", Nature Food 5(7): 535-538. doi:10.1038/s43016-024-01015-9
  file: Literature review/Han2024.pdf
  current: Strategic cropland reserves for China: land held in reserve as an alternative to grain stocks; title only.
  why: priority 2; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.4 Grain reserves and strategic stocks)
- L167: Timmer 2024, "Managing world food crises: the role of domestic food grain reserves and international trade", Future Food Systems: 229-239. doi:10.1016/b978-0-44
  file: Literature review/Timmer2024.pdf
  current: Domestic grain reserves and trade in world food crises (book chapter); title only.
  why: priority 3; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.4 Grain reserves and strategic stocks)
- L225: Wright and Cafiero 2011, "Grain reserves and food security in the Middle East and North Africa", Food Security 3(S1): 61-76. doi:10.1007/s12571-010-0094-z
  file: Literature review/Wright2011.pdf
  current: nothing yet; filed for reading
  why: filed 2026-11-10: PDF uploaded by Murray
  used by: A11.4 Grain storage
