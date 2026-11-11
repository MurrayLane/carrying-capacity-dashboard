# Reading brief B67a: Number-bearing papers, Paper A: drought and climate on farming, livestock, self-sufficiency (full reads)

Write only `qa/reports/B67a_readings.csv` and `qa/reports/B67a_readings.md`.

Rules. Plain language; no time words; no em dashes. Decision 33 applies: say what a paper does and what it finds; no verdicts on other authors' shortcomings. Do not edit `qa/literature_register.csv` or any file other than your two outputs. No git; no subagents; no network. The papers are on disk under `/home/user/carrying-capacity-models/Literature review/` at the `local_path` in each register row (drop the leading `carrying-capacity-models/`); use `pdftotext` (and `pdftotext -layout` for tables); a `.md` file is a full text rendered from PubMed Central and is read as is. Open each file and confirm first that it is the paper the row names (title, authors, year); if it is not, say so and stop on that row.

Each row carries a current characterisation: its `what_taken` text and the "why" line in its `notes` (from the B61 or B63 sweeps, written from the abstract or the record). Your job is to test that characterisation against the paper and record what the paper actually supports, with page numbers.

Depth. TARGETED: read the abstract, introduction, results summary, conclusions and any table or figure the characterisation rests on; enough to confirm or correct the line and take the one or two facts the paper is wanted for. FULL: read the whole paper; take every figure the paper is wanted for and the method and base year behind each. The list below says which.

Output 1: `qa/reports/B67a_readings.csv` with columns `id, file_ok, depth, holds, what_taken, figures, flags, notes`. `holds` is yes / partly / no (does the current characterisation hold?). `what_taken` is the new register text, at most 70 words, concrete, with page numbers. `figures` lists each number taken as "value; unit; base year; page". `flags` names anything that changes a claim in the papers or a line in `papers/A_results/OUTLINE.md` or `papers/B_methods/OUTLINE.md` (name the section), or "none". Quote page numbers from the PDF's own pagination.

Output 2: `qa/reports/B67a_readings.md`: one paragraph per paper (plain language, at most 120 words), then a closing list of flags, then the register rows you touched (all the ids below), then the words "Wrong-value check:" with one deliberate example of a characterisation that would NOT hold, so a checker can see the test can fail (mark it clearly as an example, not a finding).

Depth for every row in this brief: FULL.

Rows:
- L152: Hughes 2022, "Modelling the effects of climate change on the profitability of Australian farms", Climatic Change 172(1-2). doi:10.1007/s10584-022-03356-5
  file: Literature review/Hughes2022.pdf
  current: ABARES farm model: post-2000 climate cut average farm profit by 22.3% against the 1950 to 2000 climate; projections for 2050 range from -2 to -50% against the same base; the farm-performance evidence the point asks for.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 1, A1.5 Observed drought and climate effects on Australian farming since 2011)
- L153: Hochman 2017, "Climate trends account for stalled wheat yields in Australia since 1990", Global Change Biology 23(5): 2071-2081. doi:10.1111/gcb.13604
  file: Literature review/Hochman2017.pdf
  current: Water-limited wheat yield potential fell 27% from 1990 to 2015 through lower rainfall and higher temperatures; technology gains hid the loss in actual yields. As A1.5: Australian wheat yield potential fell 27% from 1990 to 2015.
  why: priority 1 at A1.5; 2 at B8.1; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 1, A1.5 Observed drought and climate effects on Australian farming since 2011); methods paper (se
- L155: Wittwer 2021, "Estimating the economic impacts of the 2017–2019 drought and 2019–2020 bushfires on regional NSW and the rest of Australia", Australian Journal o
  file: Literature review/Wittwer2021.pdf
  current: Economic model of the 2017 to 2019 drought: national GDP 0.7% or more below base in 2018-19 and 2019-20; $53 billion welfare loss; farm capital and herds depleted.
  why: priority 2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 1, A1.5 Observed drought and climate effects on Australian farming since 2011)
- L159: Ridoutt 2024, "Pathways toward Climate-Neutral Red Meat Production", Methane 3(3): 397-409. doi:10.3390/methane3030022
  file: Literature review/Ridoutt2024.pdf
  current: Australian red meat emissions series 1990 to 2020, with business-as-usual growth of 13% in beef cattle and 18% in sheep to 2030.
  why: priority 3; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.1 Livestock productivity in Australia)
- L180: Kinnunen 2020, "Local food crop production can fulfil demand for less than one-third of the population", Nature Food 1(4): 229-237. doi:10.1038/s43016-020-0060-
  file: Literature review/Kinnunen2020.pdf
  current: Only 11 to 28% of people worldwide could meet their demand for a given crop within 100 km. As A12.1: local production meets crop demand for under a third of people.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 12, A12.1 Self-sufficiency as a policy concept); methods paper (section 8, B8.2 What no method do
