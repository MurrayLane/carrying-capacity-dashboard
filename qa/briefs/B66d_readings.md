# Reading brief B66d: Paper A section 12: self-sufficiency, urban agriculture, water (targeted reads)

Write only `qa/reports/B66d_readings.csv` and `qa/reports/B66d_readings.md`.

Rules. Plain language; no time words; no em dashes. Decision 33 applies: say what a paper does and what it finds; no verdicts on other authors' shortcomings. Do not edit `qa/literature_register.csv` or any file other than your two outputs. No git; no subagents; no network. The papers are on disk under `/home/user/carrying-capacity-models/Literature review/` at the `local_path` in each register row (drop the leading `carrying-capacity-models/`); use `pdftotext` (and `pdftotext -layout` for tables); a `.md` file is a full text rendered from PubMed Central and is read as is. Open each file and confirm first that it is the paper the row names (title, authors, year); if it is not, say so and stop on that row.

Each row carries a current characterisation: its `what_taken` text and the "why" line in its `notes` (from the B61 or B63 sweeps, written from the abstract or the record). Your job is to test that characterisation against the paper and record what the paper actually supports, with page numbers.

Depth. TARGETED: read the abstract, introduction, results summary, conclusions and any table or figure the characterisation rests on; enough to confirm or correct the line and take the one or two facts the paper is wanted for. FULL: read the whole paper; take every figure the paper is wanted for and the method and base year behind each. The list below says which.

Output 1: `qa/reports/B66d_readings.csv` with columns `id, file_ok, depth, holds, what_taken, figures, flags, notes`. `holds` is yes / partly / no (does the current characterisation hold?). `what_taken` is the new register text, at most 70 words, concrete, with page numbers. `figures` lists each number taken as "value; unit; base year; page". `flags` names anything that changes a claim in the papers or a line in `papers/A_results/OUTLINE.md` or `papers/B_methods/OUTLINE.md` (name the section), or "none". Quote page numbers from the PDF's own pagination.

Output 2: `qa/reports/B66d_readings.md`: one paragraph per paper (plain language, at most 120 words), then a closing list of flags, then the register rows you touched (all the ids below), then the words "Wrong-value check:" with one deliberate example of a characterisation that would NOT hold, so a checker can see the test can fail (mark it clearly as an example, not a finding).

Depth for every row in this brief: TARGETED.

Rows:
- L179: Clapp 2017, "Food self-sufficiency: Making sense of it, and when it makes sense", Food Policy 66: 88-96. doi:10.1016/j.foodpol.2016.12.001
  file: Literature review/Clapp2017b.pdf
  current: Self-sufficiency is defined and measured in several ways; argues for a continuum rather than a choice between home production and open trade. As A12.1: self-sufficiency and trade are a continuum.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 12, A12.1 Self-sufficiency as a policy concept); methods paper (section 8, B8.2 What no method do
- L181: Schreiber 2021, "Quantifying the foodshed: a systematic review of urban food flow and local food self-sufficiency research", Environmental Research Letters 16(2
  file: Literature review/Schreiber2021.pdf
  current: Systematic review of 42 foodshed studies: capacity, flow and hybrid types; most from the Global North.
  why: priority 2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 12, A12.1 Self-sufficiency as a policy concept)
- L184: Payen 2022, "How Much Food Can We Grow in Urban Areas? Food Production and Crop Yields of Urban Agriculture: A Meta‐Analysis", Earth's Future 10(8). doi:10.1029
  file: Literature review/Payen2022_Earth_s_Future_How_Much_Food_Can_We_Grow_in_Urban_Areas_fulltext_PMC.md
  current: Meta-analysis of 200 studies (2,062 observations): urban crop yields on par with or above conventional averages.
  why: priority 1; open access yes; filed 2026-11-10: open-access full text from PubMed Central (JATS XML and a text rendering; not the publisher PDF) fetched by the coordinator (Europe PMC API)
  used by: results paper (section 12, A12.2 Urban agriculture)
- L187: Prosser 2021, "Adapting Water Management to Climate Change in the Murray–Darling Basin, Australia", Water 13(18): 2504. doi:10.3390/w13182504
  file: Literature review/Prosser2021.pdf
  current: Critical review of how well Murray-Darling Basin water management is adapted to climate change.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 12, A12.3 Water for food)
- L188: Grafton 2018, "Economics of Water Recovery in the Murray-Darling Basin, Australia", Annual Review of Resource Economics 10(1): 487-510. doi:10.1146/annurev-reso
  file: Literature review/Grafton2018.pdf
  current: Murray-Darling water recovery: efficiency subsidies reduced return flows; buy-backs cost less; little basin-wide gain in flows.
  why: priority 1; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 12, A12.3 Water for food)
- L189: Grafton 2018, "The paradox of irrigation efficiency", Science 361(6404): 748-750. doi:10.1126/science.aat9314
  file: Literature review/Grafton2018b.pdf
  current: The paradox of irrigation efficiency: higher efficiency rarely lowers water consumption (Australian co-authors).
  why: priority 2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 12, A12.3 Water for food)
- L222: Badami and Ramankutty 2015, "Urban agriculture and food security: A critique based on an assessment of urban land constraints", Global Food Security 4: 8-15. do
  file: Literature review/Badami2015.pdf
  current: nothing yet; filed for reading
  why: filed 2026-11-10: PDF uploaded by Murray
  used by: A12.2 Urban agriculture
