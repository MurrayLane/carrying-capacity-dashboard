# Reading brief B66e: Paper B sections 1 to 3: the post-2016 debate, capacity in planning, review method (targeted reads)

Write only `qa/reports/B66e_readings.csv` and `qa/reports/B66e_readings.md`.

Rules. Plain language; no time words; no em dashes. Decision 33 applies: say what a paper does and what it finds; no verdicts on other authors' shortcomings. Do not edit `qa/literature_register.csv` or any file other than your two outputs. No git; no subagents; no network. The papers are on disk under `/home/user/carrying-capacity-models/Literature review/` at the `local_path` in each register row (drop the leading `carrying-capacity-models/`); use `pdftotext` (and `pdftotext -layout` for tables); a `.md` file is a full text rendered from PubMed Central and is read as is. Open each file and confirm first that it is the paper the row names (title, authors, year); if it is not, say so and stop on that row.

Each row carries a current characterisation: its `what_taken` text and the "why" line in its `notes` (from the B61 or B63 sweeps, written from the abstract or the record). Your job is to test that characterisation against the paper and record what the paper actually supports, with page numbers.

Depth. TARGETED: read the abstract, introduction, results summary, conclusions and any table or figure the characterisation rests on; enough to confirm or correct the line and take the one or two facts the paper is wanted for. FULL: read the whole paper; take every figure the paper is wanted for and the method and base year behind each. The list below says which.

Output 1: `qa/reports/B66e_readings.csv` with columns `id, file_ok, depth, holds, what_taken, figures, flags, notes`. `holds` is yes / partly / no (does the current characterisation hold?). `what_taken` is the new register text, at most 70 words, concrete, with page numbers. `figures` lists each number taken as "value; unit; base year; page". `flags` names anything that changes a claim in the papers or a line in `papers/A_results/OUTLINE.md` or `papers/B_methods/OUTLINE.md` (name the section), or "none". Quote page numbers from the PDF's own pagination.

Output 2: `qa/reports/B66e_readings.md`: one paragraph per paper (plain language, at most 120 words), then a closing list of flags, then the register rows you touched (all the ids below), then the words "Wrong-value check:" with one deliberate example of a characterisation that would NOT hold, so a checker can see the test can fail (mark it clearly as an example, not a finding).

Depth for every row in this brief: TARGETED.

Rows:
- L193: Biermann 2020, "The Boundaries of the Planetary Boundary Framework: A Critical Appraisal of Approaches to Define a “Safe Operating Space” for Humanity", Annual 
  file: Literature review/Biermann2020.pdf
  current: Review of the planetary boundaries concept and the criticisms of it from earth-system science, development studies and science and technology studies.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (sections 1 and 2, B1-2.a Post-2016 debate on human carrying capacity and planetary limits (critics and de
- L194: Rees 2023, "The Human Ecology of Overshoot: Why a Major ‘Population Correction’ Is Inevitable", World 4(3): 509-527. doi:10.3390/world4030032
  file: Literature review/Rees2023.pdf
  current: A defender of limits: humanity in overshoot, with a population correction argued to be inevitable.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (sections 1 and 2, B1-2.a Post-2016 debate on human carrying capacity and planetary limits (critics and de
- L195: O’Neill 2018, "A good life for all within planetary boundaries", Nature Sustainability 1(2): 88-95. doi:10.1038/s41893-018-0021-4
  file: Literature review/O'Neill2018.pdf
  current: Social thresholds against biophysical boundaries country by country; title only.
  why: priority 2; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (sections 1 and 2, B1-2.a Post-2016 debate on human carrying capacity and planetary limits (critics and de
- L196: Montoya 2018, "Planetary Boundaries for Biodiversity: Implausible Science, Pernicious Policies", Trends in Ecology & Evolution 33(2): 71-73. doi:10.1016/j.tree.
  file: Literature review/Montoya2018.pdf
  current: Critique of a planetary boundary for biodiversity; title only.
  why: priority 2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (sections 1 and 2, B1-2.a Post-2016 debate on human carrying capacity and planetary limits (critics and de
- L197: Świąder 2020, "The application of ecological footprint and biocapacity for environmental carrying capacity assessment: A new approach for European cities", Envi
  file: Literature review/Swiader2020.pdf
  current: Ecological footprint and biocapacity used to assess environmental carrying capacity at city level for planning.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (sections 1 and 2, B1-2.b Use of capacity in planning)
- L198: Zhang 2018, "Index system of urban resource and environment carrying capacity based on ecological civilization", Environmental Impact Assessment Review 68: 90-9
  file: Literature review/Zhang2018.pdf
  current: Index system for urban resource and environment carrying capacity in China; among the most cited works citing Lane 2010; title only.
  why: priority 1; open access no; cites Lane  (Lane 2010); filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (sections 1 and 2, B1-2.b Use of capacity in planning)
- L199: Qiu 2024, "Carrying Capacity and China’s Regional Functional Planning", Carrying Capacity of China’s Resources, Environment, Population, and Economy: 151-210. d
  file: Literature review/Qui2024.pdf
  current: Carrying capacity in China's regional functional planning; same book as register L108; title only.
  why: priority 2; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (sections 1 and 2, B1-2.b Use of capacity in planning)
- L200: Haddaway 2020, "Eight problems with literature reviews and how to fix them", Nature Ecology & Evolution 4(12): 1582-1589. doi:10.1038/s41559-020-01295-x
  file: Literature review/Haddaway2020.pdf
  current: Eight common problems with literature reviews in environmental science and how to fix them; title only.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (section 3, B3.1 Review method (narrative and critical reviews))
- L201: Greenhalgh 2018, "Time to challenge the spurious hierarchy of systematic over narrative reviews?", European Journal of Clinical Investigation 48(6). doi:10.1111
  file: Literature review/Greenhalgh2018_European_Journal_of_Clinical_Time_to_challenge_the_spurious_hierarchy_of_systematic_over.pdf
  current: Narrative reviews interpret and critique; they complement rather than rank below systematic reviews.
  why: priority 1; open access yes; filed 2026-11-10: open-access PDF fetched by the coordinator (Unpaywall location)
  used by: methods paper (section 3, B3.1 Review method (narrative and critical reviews))
- L203: Snyder 2019, "Literature review as a research methodology: An overview and guidelines", Journal of Business Research 104: 333-339. doi:10.1016/j.jbusres.2019.07
  file: Literature review/Snyder2019.pdf
  current: Overview of review types with guidelines for conducting and judging a literature review.
  why: priority 2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: methods paper (section 3, B3.1 Review method (narrative and critical reviews))
- L223: Grant and Booth 2009, "A typology of reviews: an analysis of 14 review types and associated methodologies", Health Information and Libraries Journal 26(2): 91-1
  file: Literature review/Grant2009.pdf
  current: nothing yet; filed for reading
  why: filed 2026-11-10: PDF uploaded by Murray
  used by: B3.1 What a critical narrative review is
