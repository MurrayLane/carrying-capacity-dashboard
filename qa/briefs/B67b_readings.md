# Reading brief B67b: Number-bearing papers: urban agriculture, water, energy, synchronous failures (full reads)

Write only `qa/reports/B67b_readings.csv` and `qa/reports/B67b_readings.md`.

Rules. Plain language; no time words; no em dashes. Decision 33 applies: say what a paper does and what it finds; no verdicts on other authors' shortcomings. Do not edit `qa/literature_register.csv` or any file other than your two outputs. No git; no subagents; no network. The papers are on disk under `/home/user/carrying-capacity-models/Literature review/` at the `local_path` in each register row (drop the leading `carrying-capacity-models/`); use `pdftotext` (and `pdftotext -layout` for tables); a `.md` file is a full text rendered from PubMed Central and is read as is. Open each file and confirm first that it is the paper the row names (title, authors, year); if it is not, say so and stop on that row.

Each row carries a current characterisation: its `what_taken` text and the "why" line in its `notes` (from the B61 or B63 sweeps, written from the abstract or the record). Your job is to test that characterisation against the paper and record what the paper actually supports, with page numbers.

Depth. TARGETED: read the abstract, introduction, results summary, conclusions and any table or figure the characterisation rests on; enough to confirm or correct the line and take the one or two facts the paper is wanted for. FULL: read the whole paper; take every figure the paper is wanted for and the method and base year behind each. The list below says which.

Output 1: `qa/reports/B67b_readings.csv` with columns `id, file_ok, depth, holds, what_taken, figures, flags, notes`. `holds` is yes / partly / no (does the current characterisation hold?). `what_taken` is the new register text, at most 70 words, concrete, with page numbers. `figures` lists each number taken as "value; unit; base year; page". `flags` names anything that changes a claim in the papers or a line in `papers/A_results/OUTLINE.md` or `papers/B_methods/OUTLINE.md` (name the section), or "none". Quote page numbers from the PDF's own pagination.

Output 2: `qa/reports/B67b_readings.md`: one paragraph per paper (plain language, at most 120 words), then a closing list of flags, then the register rows you touched (all the ids below), then the words "Wrong-value check:" with one deliberate example of a characterisation that would NOT hold, so a checker can see the test can fail (mark it clearly as an example, not a finding).

Depth for every row in this brief: FULL.

Rows:
- L183: Mcdougall 2020, "Urban agriculture could provide 15% of food supply to Sydney, Australia, under expanded land use scenarios", Land Use Policy 94: 104554. doi:10
  file: Literature review/McDougall2020.pdf
  current: Urban agriculture could provide 15% of Sydney's food under expanded land use; Australian and quantified; title only.
  why: priority 1; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 12, A12.2 Urban agriculture)
- L186: Clinton 2018, "A Global Geospatial Ecosystem Services Estimate of Urban Agriculture", Earth's Future 6(1): 40-60. doi:10.1002/2017ef000536
  file: Literature review/Clinton2018.pdf
  current: Global estimate: 100 to 180 million tonnes of food a year under intensive urban agriculture.
  why: priority 3; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 12, A12.2 Urban agriculture)
- L190: Rosa 2020, "Global agricultural economic water scarcity", Science Advances 6(18). doi:10.1126/sciadv.aaz6031
  file: Literature review/Rosa2020_Science_Advances_Global_agricultural_economic_water_scarcity.pdf
  current: Economic water scarcity on up to 25% of cropland; sustainable irrigation there could feed 840 million more people.
  why: priority 3; open access yes; filed 2026-11-10: open-access PDF fetched by the coordinator (Unpaywall location)
  used by: results paper (section 12, A12.3 Water for food)
- L192: Ladha-Sabur 2019, "Mapping energy consumption in food manufacturing", Trends in Food Science & Technology 86: 270-280. doi:10.1016/j.tifs.2019.02.034
  file: Literature review/LadhaSabur2019.pdf
  current: Energy used in food manufacturing and distribution; over 98% of UK food moves by road. As A12.4: energy in food manufacturing and transport.
  why: priority 2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 12, A12.4 Fuel and energy in food production); methods paper (section 8, B8.3 What no method does
- L218: Anderson 2019, "Synchronous crop failures and climate-forced production variability", Science Advances 5(7). doi:10.1126/sciadv.aaw1976
  file: Literature review/Anderson2019_Science_Advances_Synchronous_crop_failures_and_climate_forced_production_variability_fulltext_PMC.md
  current: Climate modes (ENSO, IOD and others) account for 18, 7 and 6% of global maize, soybean and wheat variability.
  why: priority 2; open access yes; filed 2026-11-10: open-access full text from PubMed Central (JATS XML and a text rendering; not the publisher PDF) fetched by the coordinator (Europe PMC API)
  used by: methods paper (section 8, B8.1 What no method does: variability)
