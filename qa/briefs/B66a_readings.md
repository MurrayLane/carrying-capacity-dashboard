# Reading brief B66a: Paper A section 1: population debate, food security in planning (targeted reads)

Write only `qa/reports/B66a_readings.csv` and `qa/reports/B66a_readings.md`.

Rules. Plain language; no time words; no em dashes. Decision 33 applies: say what a paper does and what it finds; no verdicts on other authors' shortcomings. Do not edit `qa/literature_register.csv` or any file other than your two outputs. No git; no subagents; no network. The papers are on disk under `/home/user/carrying-capacity-models/Literature review/` at the `local_path` in each register row (drop the leading `carrying-capacity-models/`); use `pdftotext` (and `pdftotext -layout` for tables); a `.md` file is a full text rendered from PubMed Central and is read as is. Open each file and confirm first that it is the paper the row names (title, authors, year); if it is not, say so and stop on that row.

Each row carries a current characterisation: its `what_taken` text and the "why" line in its `notes` (from the B61 or B63 sweeps, written from the abstract or the record). Your job is to test that characterisation against the paper and record what the paper actually supports, with page numbers.

Depth. TARGETED: read the abstract, introduction, results summary, conclusions and any table or figure the characterisation rests on; enough to confirm or correct the line and take the one or two facts the paper is wanted for. FULL: read the whole paper; take every figure the paper is wanted for and the method and base year behind each. The list below says which.

Output 1: `qa/reports/B66a_readings.csv` with columns `id, file_ok, depth, holds, what_taken, figures, flags, notes`. `holds` is yes / partly / no (does the current characterisation hold?). `what_taken` is the new register text, at most 70 words, concrete, with page numbers. `figures` lists each number taken as "value; unit; base year; page". `flags` names anything that changes a claim in the papers or a line in `papers/A_results/OUTLINE.md` or `papers/B_methods/OUTLINE.md` (name the section), or "none". Quote page numbers from the PDF's own pagination.

Output 2: `qa/reports/B66a_readings.md`: one paragraph per paper (plain language, at most 120 words), then a closing list of flags, then the register rows you touched (all the ids below), then the words "Wrong-value check:" with one deliberate example of a characterisation that would NOT hold, so a checker can see the test can fail (mark it clearly as an example, not a finding).

Depth for every row in this brief: TARGETED.

Rows:
- L145: Parr 2018, "What sort of population policy should Australia adopt? Suggestions for migration, fertility and population research policy", Australian Population S
  file: Literature review/Parr2018.pdf
  current: Commentary in Australian Population Studies on what population policy Australia should adopt (migration, fertility, size); title and venue only, content not seen.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 1, A1.1 Australian population debate and planning, 2011 to 2025)
- L147: McDonald 2017, "International migration and employment growth in Australia, 2011–2016", Australian Population Studies 1(1): 3-12. doi:10.37970/aps.v1i1.8
  file: Literature review/McDonald2017.pdf
  current: Immigration and employment growth 2011 to 2016: the skilled-migration basis of population growth in the years Paper A covers.
  why: priority 2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 1, A1.1 Australian population debate and planning, 2011 to 2025)
- L148: Summerhayes 2026, "Transforming food security policymaking in Australia: a three-tiered food systems-centred and rights-based approach", Food Security 18(4): 96
  file: Literature review/Summerhayes2026.pdf
  current: 102 food policies, 25 interviews and 500 surveys in Queensland, Victoria and Western Australia; food security agendas found inadequate at local, state and national levels; proposes a three-tier, rights-based approach.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 1, A1.4 Food security in Australian planning and policy)
- L149: Summerhayes 2024, "Trans-Governance and Food Systems (Tr-GaF) for food policy integration: A case study of the Australian food policy landscape", Food Policy 12
  file: Literature review/Summerhayes2024.pdf
  current: Same 102-policy corpus: limited integration of food policy in Australia, little attention to food in urban planning, fragmentation across levels of government.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 1, A1.4 Food security in Australian planning and policy)
- L150: Summerhayes 2025, "Integrating urban land use planning with food systems in Australia: Policy integration challenges and opportunities", International Journal o
  file: Literature review/Summerhayes2025.pdf
  current: Interviews with 25 senior planners and policymakers: agricultural land and food retail are the only food elements that planning integrates; land scarcity and market pressure limit more.
  why: priority 2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 1, A1.4 Food security in Australian planning and policy)
- L151: James 2016, "Planning for Peri-urban Agriculture: a geographically-specific, evidence-based approach from Sydney", Australian Geographer 47(2): 179-194. doi:10.
  file: Literature review/James2016.pdf
  current: Sydney Basin farmland 1992 to 2011: the data on peri-urban food production are contested, so planners cannot say whether metropolitan supply is at risk.
  why: priority 2; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 1, A1.4 Food security in Australian planning and policy)
- L154: Falster 2024, "How unusual was Australia's 2017–2019 Tinderbox Drought?", Weather and Climate Extremes 46: 100734. doi:10.1016/j.wace.2024.100734
  file: Literature review/Falster2024b.pdf
  current: The 2017 to 2019 Tinderbox Drought: cool-season and annual rainfall deficits in the Murray-Darling Basin were unprecedented in the instrumental record.
  why: priority 2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 1, A1.5 Observed drought and climate effects on Australian farming since 2011)
- L224: Lawrence, Richards and Lyons 2013, "Food security in Australia in an era of neoliberalism, productivism and climate change", Journal of Rural Studies 29: 30-39.
  file: Literature review/Lawrence2013.pdf
  current: nothing yet; filed for reading
  why: filed 2026-11-10: PDF uploaded by Murray
  used by: A1.4 Regional food self-sufficiency and food security in Australian planning
