# Paper B (methods): section-by-section scope

Scoping job S01, 2026-11-11, on Murray's instruction: scope each section, draft nothing. Rewritten by B92b, 2026-11-13 (decision 87), to the logic check V32b. This file holds no paper prose beyond the purpose sentences. Every number it repeats carries a claim id from `qa/claims_register.csv` or a named csv, and is there to show what a point rests on, not as text for the paper.

**Basis.** Read for S01: `papers/B_methods/OUTLINE.md` (labels as placed by B72), `papers/B_methods/SECTION7_DRAFT.md`, `qa/DECISIONS.md` (rows 1 to 54), `qa/CARD.md`, `qa/reports/B61_lit_review_scope.md`, `B63_recency_sweep.md`, `B68_reader_flags.md`, `B70_paperA_thin_points.md`, `B72_outline_numbering.md`, `qa/literature_register.csv`, `qa/claims_register.csv`, `qa/sources_register.csv` (data ids only), the READMEs of `analysis/method_tests_2025/`, `analysis/comparators_2025/`, `analysis/sensitivity_2025/`, `analysis/nutrition_lp_2025/` and `results/`, and `HANDOFF.md`. Read for B92b: `qa/reports/V32b_logic_B.md` in full, `qa/reports/V32a_logic_A.md` (cross-paper table), `qa/DECISIONS.md` rows 55 to 90, `qa/reports/B94_footprint_wording.md`, and both registers as they stand on 2026-11-13 (claims: 697 rows, 332 Paper B; literature: L001 to L242).

**Jobs running while this was rewritten.** B93 (decision 88: one-route check of the gap-attribution rows B278 to B332, and the Cassidy test rerun with harvests matched): no report on disk, so the gap-attribution shares and the people-per-hectare figures are left as they were and marked "pending B93". B94 (decision 85, footprint wording) finished while this job ran: its report is on disk and B046, B156 and B247 carry the reworded statements in the register, so its wording is applied here and marked "B94". B73 and B74 have finished; their rows (L146, L165, L191 page level; L226 to L234) are used below.

**How to read the tables.**
* *Evidence*: tier is the claims register's tier (A headline, B supporting, C context). "Two routes agree" is "yes" where the row's status is `independently verified`, with "with notes" or "after correction" added where the status says so and the note matters to the point; otherwise it says self-checked (one route) or unverified. Where no claim row exists, the cell names the register or csv cell the point rests on, or says "none needed".
* *Read status* is the literature register's `read_or_reported` field, then its `status` field, as they stand on 2026-11-13.
* *Year band* is by publication year (decision 42). Undated register rows are counted before 2016, as B63 did.
* *Open decisions* lists the settled rows that bind the section and, separately, the questions still open. Questions are numbered Q1 to Q9 across the file; a settled question keeps its row with the deciding decision named.

**Cross-paper resolutions (decision 87).** Each item where the two scopes disagreed, resolved on the side the decisions favour. The same resolutions go into Paper A's scope (B92a, same instruction).

| # | Item | Resolution for both papers | Rests on |
|---|---|---|---|
| X-1 | Waste | The model's 6% setting halves the model's retail-and-consumer loss share, mirroring UN Target 12.3; Australia's own goal (National Food Waste Strategy 2017, p. 8 printed) is whole-chain halving by 2030; the 2016-17 Baseline is 7.3 Mt (L231) and the later 7.6 Mt estimate is the 2021 Feasibility Study (L242), each named with year and source. | decision 72 (replaces 44); L230, L231, L242 |
| X-2 | PMSEIC and Lawrence | PMSEIC 2010 states on p. 1, with no source, that Australia produces enough food to feed 60 million people; its p. 15, citing DAFF 2009, says production feeds some 40 million people outside Australia; the report does not add the two (L136). The 22 million at home plus 40 million abroad is Lawrence, Richards and Lyons 2013 (L224, p. 30), quoted only in Paper A section 8, with its source and a line that its basis differs from the model's; Paper B does not quote it. | decision 46; L136, L224 |
| X-3 | Monte Carlo choices | 13 sampled, 12 vary in the 2025 corrected and published releases (2025-fixed, 2025-mirror); in 2025-improved the long-term benchmark is drawn but has almost no effect. Paper B section 6 point 9 states the test of the method (the additive shortcut checked against full runs, B116), so Paper A's "described and tested in Paper B" (A336) holds. | B253 (with V31d note), B116, A336 |
| X-4 | Red-meat low end 0.528 | Unit "share of meat" (the red-meat share of meat), in both papers. B251's unit field reads "share of diet" against its own statement; the register edit is listed for the next register job. | A341 (unit corrected by V31d), B251 |
| X-5 | "A little meat beats none" | On the corrected release only: 2.5% meat and eggs, 118.0 million, above none, 112.4; on the improved release the diet with no meat or eggs is the highest point (103.6). Neither paper states it as the model's general mechanism. | decision 31; B216 |
| X-6 | "5% meat and eggs" | Always named with its release and setting: 103.3 million on the improved release, guideline diet by the direct route (B179, decision 31); 76.8 million on the corrected release, the measure applied alone (A258). | B179, A258 |
| X-7 | Ratio convention | People over capacity; above 1 is over capacity. A factor between two capacities (a design-choice factor; "three to eight times") is not a people-over-capacity ratio and is called a factor. Paper B's scope states no people-over-capacity ratio; any the drafter adds follows this convention. | decision 87; V32a problem 7 |
| X-8 | 15.5 million | Never quoted bare. Paper B: the sum over SA2s of capacity, 15.5 million against the national 41.5 (B176; short term, 2025-fixed, state yield basis). Paper A: what trade in products between regions recovers, about 15.5 million people-equivalents in the short term (A274). | B176, A274 |
| X-9 | Cause of the published scatter | Published estimates differ because they answer different questions by different methods: within one model the definitions span a factor of about 4 (reading set by Q8), and between methods on equalised inputs the gap is the method. Paper A's "mostly by definition" reads "by definition and by method". | decision 35; B190, B276, B277 |
| X-10 | "9 to 14 million" | Called the published method wherever it appears: 9.4 on 2011 data as built (B160) and 14.1 on 2025 data as built (2025-mirror; B006 note). The corrected long-term figures are 15.35 on 2011 data (A007) and 15.6 on 2025 data (A008, B091). B189's step from 9.4 to 15.6 mixes a data change with the correction and is worded so. | decision 87; B006, B160, B189, A007, A008 |
| X-11 | 2011 to 2025 material | Paper A alone (outline relationship rule). The section 7 draft's "7% in 2011" (B131) and "fell 28% between 2011 and 2021-23" (B067) leave Paper B or point to Paper A. HALF's 2011 fidelity check stays in Paper B as a fidelity check. | outline rule; decision 58 |
| X-12 | Where the national margin fails | Where a threshold is meant, both papers give the failure probability a year: 5.8 to 6.1%, about 1 in 16 to 17 (B130). Paper A's "gone at a 1-in-20 year" (A196) is about the 1-in-20 year, not a threshold. | B130, A196 |
| X-13 | Statuses of L003, L010, L013 | As the register: L003 and L010 read (B85 page level), self-checked (B85); L013 read, unverified. | literature register |

---

## Section 1. Introduction

**1. Purpose and argument.** The section sets out the puzzle the paper answers: published estimates of how many people Australia can feed run from about 9 to 100 million, all offered as how many Australia can feed. Both ends are soft and the section says so at first use: the 9.4 is the author's own long-term figure before correction (published method), and the 100 is the report's "around 100" for 27 million at home plus 63 million abroad. The span therefore shows that published figures range by an order of magnitude, not a measured spread of independent estimates. The section says why the spread matters to land-use planners and sustainability analysts, who use capacity figures to argue about population, food security and land. It states the question (how much of the spread is the definition, the diet or the method, and which method suits which purpose) and that the paper follows the 2010 review and thesis chapter 6. It discloses at the outset that the model tested beside the others is the author's own, held to the same tests.

**2. Content list.**
1. Four figures all offered as how many Australia can feed (100, 61, 30 to 35, 9 to 14 million), and the published span of 9.4 to 100 million (factor 10.6 on 100; Q9). At first use: the 9.4 is the author's own thesis long-term figure before correction, and "9 to 14" is the published method (X-10); the 100 is "around 100" in the report's words for 27 + 63 (Q9); the 30 to 35 is quoted as summarised in the source actually read (the thesis, L020) until the Jones report is read (decision 89), and nothing says the model "reproduces" it.
2. The spread is old: a 1986 committee gave 10 to 480 million, known third-hand (Clarke 1990 as reported by Henry and Godden, L036); the 1975 CSIRO work is known through two second-hand routes, Henry and Godden and Chisholm (decision 39; B010, L143).
3. At world scale the scatter of capacity estimates is a known feature, and depends on the choices made (Cohen 1995, which carries the point alone; Cohen 2017 not reached at page level).
4. **B1-2.b Use of capacity in planning.** Why the spread matters: capacity figures enter Australian population debate and planning (Productivity Commission roundtable, cited only if its file is fetched, decision 82; a northern Australia settlement study that uses Lane 2017) and city and regional planning abroad. Government population planning documents: the 2021 and 2023 Intergenerational Reports and the 2025 Population Statement (L226 to L228, B74).
5. The question: which method suits which purpose, and how much of the spread is definition, diet or method.
6. What this paper adds to thesis chapter 6 and the 2010 review: method families not covered there, a test of each on the same 2025 Australian data, measured design choices, and a guide. The earlier-work list holds for chapter 6; Lane 2010 alone lacks Douglas Shire and Peters (B236), and Fearnside is named once, as reviewed in the earlier work and tested here.
7. Disclosure: the model is the author's (thesis 2014, papers to 2017), one of the methods reviewed, entered as published and as built on, and named again in the competing-interests statement.

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | B005 (9.4 to 100, factor 10.6; the 9.4 is the author's figure); B160 (9.4); B162 (100; 27 + 63 = 90, "around 100" in the report); B161 (61); B196 (30 to 35); B006 (the four figures named together) | B005, B160, B162: A, yes. B161: B, yes with notes (61 read; the 24.4 domestic population is not printed). B196: B, unverified (L006 not on disk; decision 89). B006: C, yes with notes (30 to 35 not reached; "all called carrying capacity" is the paper's framing, so the point is worded "offered as how many Australia can feed") |
| 2 | B010 (Gifford 82 and 60; two second-hand routes); register L036 (third-hand), L143 (p. 21); `analysis/comparators_2025/harmonisation.csv` rows for the 1986 committee and Gifford | B010: B, yes with notes (both routes second-hand). Register and csv cells are typed from sources (no second route) |
| 3 | register L049 (pp. 341 to 343); L106 | none needed; L049 carries the point; L106 not reached: no file (B85) |
| 4 | register L146, L197, L198, L199; L226, L227, L228; L099 | none needed; L099 not reached: no file (B85), so it is cited only if fetched (decision 82) |
| 5 | none needed | none needed |
| 6 | B236 (what the earlier work covered) | C, yes with notes (holds for chapter 6; Lane 2010 alone lacks Douglas Shire and Peters) |
| 7 | B229 (the author's published 40, 9 to 40, 23 million) | B, yes |

**4. Tables and figures.**
* Table 1, published Australian estimates with their definitions (exports, diet, drought allowance): from `analysis/comparators_2025/harmonisation.csv` and `analysis/method_tests_2025/published_values.csv`. No script makes a paper table from them; `harmonisation.csv` itself is typed from the sources, not generated. A script is needed. The table names the route for each figure (read, second-hand, third-hand, as summarised).

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L006 | Jones committee 1994 | read; unverified | 30 to 35 million and 50 plus, quoted as summarised in the thesis until Murray's copy is read (decision 89) | before 2016 |
| L036 | Migration Committee 1986 | reported; self-checked (B85) | the 10 to 480 million range, third-hand (Clarke 1990 as reported by Henry and Godden) | before 2016 |
| L002 | Gifford et al. 1975 | reported; self-checked (B85) | the 1975 CSIRO figures, second-hand through Henry and Godden and Chisholm (decision 39) | before 2016 |
| L143 | Chisholm 2000 | read; self-checked (B62 full text) | the second route to the 1975 CSIRO figures (p. 21) | before 2016 |
| L003 | Henry and Godden 1995 | read (B85 page level); self-checked (B85) | 109 and 96 million; route to Gifford and the Migration Committee | before 2016 |
| L007 | Foran and Poldy 2002 | read (B85 page level); self-checked (B85) | a commodity-balance estimate among the published figures | before 2016 |
| L136 | PMSEIC 2010 | read; self-checked (B52 full text) | 60 million on p. 1 with no source; p. 15, citing DAFF 2009, some 40 million fed abroad; the report does not add the two (X-2) | before 2016 |
| L009 | Bellotti 2017 | read; unverified | 61 million who "could eat Australian food" (the population plus those fed by exports); the "read" label is COMP's | 2016 to 2019 |
| L010 | CSIRO and UQ 2025 | read (B85 page level); self-checked (B85) | 27 million at home plus 63 abroad, "around 100 million" in the report's words (Q9) | 2020 to 2026 |
| L020 | Lane 2014 (thesis) | read (B85 page level); self-checked (B85) | the 9 to 14 million long-term figures (published method); the Jones summary; chapter 6 as the earlier review | before 2016 |
| L012 | Lane, Dawes and Grace 2014 | read; unverified | the author's published estimates (disclosure; figures confirmed in `results/2011-thesis.csv`) | before 2016 |
| L013 | Lane, Dawes and Grace 2015 | read; unverified | the author's published estimates and scale (disclosure) | before 2016 |
| L014 | Lane 2017 | read; unverified | short-term and long-term time frames (disclosure) | 2016 to 2019 |
| L055 | Lane 2010 | read (B85 page level); self-checked (B85) | the 2010 methodology review this paper follows | before 2016 |
| L049 | Cohen 1995 | read; self-checked (B62 full text) | world estimates scatter from under 1 to over 1,000 billion | before 2016 |
| L106 | Cohen 2017 | read; unverified | about ninety world estimates; capacity depends on choices (not reached: no file, B85; cite only if read) | 2016 to 2019 |
| L099 | Productivity Commission 2011 | read; unverified | capacity in Australian population policy debate (not reached: no file, B85; cite only if fetched, decision 82) | before 2016 |
| L226 | Treasury 2023 (Intergenerational Report) | read (B74 targeted); self-checked (B74) | government framing of population planning | 2020 to 2026 |
| L227 | Treasury 2021 (Intergenerational Report) | read (B74 targeted); self-checked (B74) | government framing; the first downward revision | 2020 to 2026 |
| L228 | Centre for Population 2025 | read (B74 targeted); self-checked (B74) | government framing of population planning | 2020 to 2026 |
| L146 | Bolleter 2018 | read (B73 page level); self-checked (B73) | an Australian planning use of Lane 2017 (northern Australia) | 2016 to 2019 |
| L197 | Świąder et al. 2020 | read (B66e targeted); self-checked (B66e) | footprint-based capacity in European city planning | 2020 to 2026 |
| L198 | Zhang et al. 2018 | read (B66e targeted); self-checked (B66e) | an urban capacity index in Chinese planning (no claim that it builds on Lane 2010; B68) | 2016 to 2019 |
| L199 | Qiu 2024 | read (B66e targeted); self-checked (B66e) | capacity in China's regional functional planning (publication year rule, decision 42) | 2020 to 2026 |
| L073 | Khorsandi et al. 2022 | read (B85 page level); self-checked (B85) | a recent method that cites the thesis and the 2014 paper | 2020 to 2026 |

Year mix (25 rows): before 2016: 13; 2016 to 2019: 5; 2020 to 2026: 7.

**6. Gaps.**
1. Closed (B74): government framing of population planning since 2011 is L226 to L228.
2. A synthesis of how methods spread capacity estimates, beyond Cohen: kind of source, a review such as van den Bergh and Rietveld 2004 (B61 candidate, not acquired). Job: acquisition, optional if Cohen 1995 carries the point (Cohen 2017 is not reached at page level).
3. Australian planning uses of capacity since 2011 beyond one paper (B63 found only Bolleter 2018): job, a targeted sweep of Australian planning and urban policy journals.
4. How others have taken up the model: about 60 citing works on the OpenAlex list, two read (B61 point B1.5), and the "among the most cited" line for L198 has no count source (B68). Job: a reading pass over the citing list with a named count source.
5. The Jones committee report (L006) is not on disk; B196 and B197 are unverified, and the thesis summarises the committee differently (V31b). Job: Murray's copy (decision 89), a page read of paragraphs 2.13 to 2.16 recorded in L006, then B196, B197, B138 and B245 rechecked. Until then the figures are quoted as summarised in the thesis.

**7. Open decisions.**
* Binding: 33 (tone), 36 (acquisitions), 39 (Gifford cited second-hand, saying so), 42 (selection rule), 23 (correction notes go out before submission, so the introduction can name corrected figures), 46 (Lawrence only in Paper A; PMSEIC per X-2), 82 (rows with no file: number-bearing ones fetched, the rest cited as reported), 87 (cross-paper resolutions), 89 (Jones report fetched by Murray).
* Open: outline "Decisions still open" item 4 (authors and order), which the competing-interests statement needs. Q9 (section 6) sets how the 100 is quoted here.

**8. Word budget and dependencies.** About **800 words**: seven points, most of one or two sentences, with Table 1 carrying the figures; long enough for one paragraph on planning use and one on disclosure. Dependencies: written after sections 5 and 6 so the framing quotes only verified figures; Table 1 script; the Jones report (decision 89); Q9; outline item 4 for the disclosure wording.

---

## Section 2. The concept, its refinements and its critics

**1. Purpose and argument.** The section asks whether carrying capacity is a sound idea for people at all, and why planners still need it. It sets the defenders who extend the concept (cultural capacity below the biological limit; a limit that moves) beside the critics (capacity is social and normative; a static capacity is empty and a variable one begs the question; the idea may validate itself; it depends on choices). It then takes in the debate since 2016 on planetary limits and overshoot in one paragraph (decision 43). Its argument for the rest of the paper is that a capacity figure is usable only with a stated question, standard and time frame, which is what the tests in sections 5 and 6 make explicit. It stays short (decision 37) and points back to thesis chapter 6 and the 2010 review.

**2. Content list.**
1. Where K comes from: range management and shipping to the logistic; the static and the variable reading (Sayre), with the ecological lineage only from Chapman and Byron.
2. Defenders who extend it: cultural capacity below the biological limit, so stay well below the best estimate (Hardin); a limit that itself rises (Meyer and Ausubel; Hopfenberg); capacity tied to a period and a nutrition standard (Gilland).
3. Critics: capacity as social and normative with no single objective level (Seidl and Tisdell); static capacity empirically vacuous, variable capacity question-begging (Sayre); the concept flawed and possibly self-validating (Price); capacity dynamic and choice-dependent, undefined for a trading nation (Cohen).
4. The footprint inversion: capacity turned into the land a population needs, at world-average productivity (Rees 1992, 1996); the open-economy counter-view from Australia (Chisholm); the critique that the footprint protocol lacks an external referent (Giampietro and Saltelli).
5. **B1-2.a Post-2016 debate on human carrying capacity and planetary limits.** The framework itself (Rockström et al. 2009, decision 56; the paper does not use the words "carrying capacity", L240); overshoot and limits (Rees 2023; overshoot accounts from Wackernagel 2002; O'Neill and others nation by nation); critics of planetary boundaries (Biermann and Kim, in their words "planetary limits"; Montoya and others); World3 against data, where the closest fit is CT (7 counts) with BAU2, a business-as-usual variant, one count behind (Herrington, L210); single world figures (Tucker, whose calculation is in a book not read; Cohen 2017), each cited only if read at page level.
6. Why planners still need the concept, and the thesis typology (inputs and outputs, scale) that organises section 4; pointer to thesis chapter 6 and the 2010 review.

**3. Evidence.** Paper B has no claims-register rows for section 2; the positions rest on the register's `what_taken` cells as the rows L044 to L049 and L139 to L143 record them (B62 full-text reads), on L193 to L196 and L210 (B66e, B66f) and on L240 (B82).

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | register L046 `what_taken` (pp. 120, 124, 126, 131); L088 (excludes human capacity by design, p. 3) | none needed (concept); single reading |
| 2 | register L044 (pp. 600 to 603), L047 (pp. 210 to 213), L141 (p. 114), L142 (pp. 1 to 2, 8, 11) | none needed |
| 3 | register L045 (pp. 399, 403 to 407), L048 (pp. 9 to 10, 17, 23), L049 (pp. 341 to 343) | none needed; a quoted range (Cohen's under 1 to over 1,000 billion) would need a claim row |
| 4 | register L139 (pp. 125 to 126), L140 (p. 207), L143, L085 | none needed |
| 5 | register L240 (pp. 472 to 475), L193 (pp. 498, 501 onward), L194, L195, L196, L210 (pp. 622 to 623; closest-fit counts CT 7, BAU2 6, BAU 4, SW 3), L024, L106, L107, L109 | none needed; L106 and L107 not reached: no file (B85) |
| 6 | register L020 (chapter 6), L055 | none needed |

**4. Tables and figures.** None.

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L046 | Sayre 2008 | read; self-checked (B62 full text) | the history of K; static capacity empirically vacuous, variable capacity question-begging | before 2016 |
| L088 | Chapman and Byron 2018 | read; self-checked (B54a full text) | the ecological lineage only (it excludes human capacity) | 2016 to 2019 |
| L044 | Hardin 1986 | read; self-checked (B62 full text) | cultural capacity below the biological limit; stay well below the best estimate | before 2016 |
| L047 | Meyer and Ausubel 1999 | read; self-checked (B62 full text) | a limit that itself rises (logistic with varying K) | before 2016 |
| L141 | Hopfenberg 2003 | read; self-checked (B62 full text) | capacity fitted to food availability (moving capacity) | before 2016 |
| L142 | Gilland 2006 | read; self-checked (B62 full text) | capacity tied to a period and a nutrition standard | before 2016 |
| L045 | Seidl and Tisdell 1999 | read; self-checked (B62 full text) | capacity is social and normative, no single objective level | before 2016 |
| L048 | Price 1999 | read; self-checked (B62 full text) | the concept flawed and possibly self-validating | before 2016 |
| L049 | Cohen 1995 | read; self-checked (B62 full text) | capacity is dynamic and choice-dependent; undefined for a trading nation | before 2016 |
| L139 | Rees 1992 | read; self-checked (B62 full text) | capacity inverted into the land a population needs; trade and the unit of analysis | before 2016 |
| L140 | Rees 1996 | read; self-checked (B62 full text) | area-based indicators; world-average productivities | before 2016 |
| L143 | Chisholm 2000 | read; self-checked (B62 full text) | the open-economy counter-view, Australian | before 2016 |
| L024 | Wackernagel et al. 2002 | read (B85 page level); self-checked (B85) | overshoot accounting at world scale | before 2016 |
| L085 | Giampietro and Saltelli 2014 | read; self-checked (B50a full text) | the critique of footprint-based capacity (also section 4) | before 2016 |
| L099 | Productivity Commission 2011 | read; unverified | absorption capacity and rate of change in the Australian debate (cite only if fetched, decision 82) | before 2016 |
| L240 | Rockström et al. 2009 | read (B82 targeted); self-checked (B82) | the planetary boundaries framework (decision 56) | before 2016 |
| L106 | Cohen 2017 | read; unverified | single-number claims and choices (cite only if read) | 2016 to 2019 |
| L107 | Tucker 2020 | read; unverified | a single long-term world figure, as an example of the claim type (cite only if read) | 2020 to 2026 |
| L109 | Wang 2022 | read; self-checked (B54b full text) | land capacity framed for food security (single author; its range is second-hand) | 2020 to 2026 |
| L194 | Rees 2023 | read (B66e targeted); self-checked (B66e) | overshoot: a defender of limits | 2020 to 2026 |
| L195 | O'Neill et al. 2018 | read (B66e targeted); self-checked (B66e) | social thresholds against biophysical boundaries, nation by nation | 2016 to 2019 |
| L193 | Biermann and Kim 2020 | read (B66e targeted); self-checked (B66e) | critiques of planetary boundaries; say "planetary limits" (decision 43) | 2020 to 2026 |
| L196 | Montoya et al. 2018 | read (B66e targeted); self-checked (B66e) | a critique of a biodiversity boundary | 2016 to 2019 |
| L210 | Herrington 2020 | read (B66f targeted); self-checked (B66f) | World3 against data; closest fit CT (7 counts), BAU2 one count behind (B68 flag) | 2020 to 2026 |
| L020 | Lane 2014 (thesis) | read (B85 page level); self-checked (B85) | the typology by inputs and outputs and by scale | before 2016 |
| L055 | Lane 2010 | read (B85 page level); self-checked (B85) | pointer to the earlier review of the concept | before 2016 |

Year mix (26 rows): before 2016: 17; 2016 to 2019: 4; 2020 to 2026: 5. The concept's founding works are old by nature (B63 found the same); decision 42 keeps works before 2011 for lineage only, so the drafter can cut points 2 and 3 to the fewest classics that carry them.

**6. Gaps.**
1. Closed by decision 56: Rockström et al. 2009 is L240 (read, B82).
2. Cohen 2017 (L106) and Tucker 2020 (L107) have a local path recorded but were not reached at page level (B85: "not reached: no file"). Job: a page read if either is quoted; otherwise point 5 drops them.
3. No claim rows exist for section 2. Any figure quoted from a concept source (for example Cohen's range of estimates) needs a claims-register row first. Job: register builder.

**7. Open decisions.**
* Binding: 33, 37 (reading pass, kept short), 42 (lineage only before 2011), 43 (one paragraph, "planetary limits" where the authors say so), 56 (Rockström 2009 for the planetary-limits paragraph), and the standing recency rule (CARD). B68 decision 4 is settled by 43.
* Open: Q2.

| # | Question | Options | Recommended | Confidence | Reason |
|---|---|---|---|---|---|
| Q1 | Acquire the founding planetary boundaries paper for the decision-43 paragraph | Settled by decision 56: Rockström et al. 2009 acquired (L240) | settled (56) | n/a | n/a |
| Q2 | The outline tags the B1-2.a bullet "(added 2026-11-11, decision 52)"; row 52 is Paper A's drought wording. The bullet comes from decision 45 (numbering, B72) and its content from decision 43. V32b found the tag still unchanged in OUTLINE.md | (a) correct the tag to decisions 43 and 45 at the next outline edit / (b) leave it | (a) | High | A wrong decision number sends a reader of the outline to the wrong row; the fix is one line in a file the coordinator may edit |

**8. Word budget and dependencies.** About **1,000 words**: six points over about 26 sources, one paragraph for the post-2016 debate (decision 43) and a closing paragraph on why planners still need the concept; decision 37 asks for a short section. Dependencies: Q2 is housekeeping only; page reads of L106 and L107 if quoted. Reading is otherwise done (B62, B66e, B66f, B82).

---

## Section 3. How the review was done

**1. Purpose and argument.** The section states the review type and how works were chosen, briefly and transparently. It names the type as a critical review with a narrative synthesis, citing Grant and Booth for the type and Greenhalgh and others for the narrative style (decision 42). It states the selection rule (works from 2011 by publication year, earlier works for lineage only, exclusions named), where the works came from and the reading label each cited work carries, so a reader can judge the coverage once the selection record exists (gap 1). It says what the earlier work already covered and is not repeated.

**2. Content list.**
1. **B3.1 Review method (narrative and critical reviews).** The type: a critical review in Grant and Booth's sense, written as a narrative synthesis in Greenhalgh's sense (decision 42 replaces the outline's single label "critical narrative review"); why that suits a question of method fit.
2. The selection rule (decision 42): publication year from 2011; earlier works for the lineage of a method or concept only; the well-known methods across the main approaches; exclusions named (for example index methods with no food or land basis).
3. Where the works came from: Murray's citation exports and the OpenAlex citing list; the B14 sweep; the B61 scoping; the B63 recency sweep (Crossref, 2016 to 2026); government documents as grey literature (B74, B82, B83). The counts for each route come from the selection record (gap 1).
4. How sources were used, in the register's own labels: read in full, read at page level, read in a targeted way (named passages), reported (held second-hand and cited as reported, as Gifford, decision 39), and record only; a work whose "read" label was inherited and cannot be checked against a file (L006, L009, L099, L106, L107) is cited as reported or fetched first (decision 82).
5. What thesis chapter 6 and the 2010 review covered, which this paper points to and does not repeat (B236: holds for chapter 6; Lane 2010 alone lacks Douglas Shire and Peters).
6. A pointer to section 5 for the test design (the common data set and the fidelity check).

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | register L223 (Table 1, p. 94), L201 (Key point box, p. 2 of 6) | none needed |
| 2 | `qa/DECISIONS.md` row 42 | none needed |
| 3 | no csv holds the counts (see gap 1) | needs a count before drafting |
| 4 | `qa/literature_register.csv` columns `read_or_reported` and `status` | none needed; the point names the labels the register uses |
| 5 | B236 | C, yes with notes (holds for chapter 6; Lane 2010 alone lacks Douglas Shire and Peters) |
| 6 | none needed | none needed |

**4. Tables and figures.** Optionally a small table or flow note of works by route and status (found, read, cited, excluded). No csv and no script exist; see gap 1.

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L223 | Grant and Booth 2009 | read (B66e targeted); self-checked (B66e) | "critical review" as a type (Table 1, p. 94) | before 2016 |
| L201 | Greenhalgh et al. 2018 | read (B66e targeted); self-checked (B66e) | narrative as a style of synthesis; no ranking below systematic reviews | 2016 to 2019 |
| L202 | Sukhera 2022 | read (B78 page level); self-checked (B78) | narrative reviews can be rigorous | 2020 to 2026 |
| L203 | Snyder 2019 | read (B66e targeted); self-checked (B66e) | reasoned, transparent inclusion criteria (p. 337) | 2016 to 2019 |
| L200 | Haddaway et al. 2020 | read (B66e targeted); self-checked (B66e) | state the selection rule and exclusions plainly (pp. 1583 to 1585) | 2020 to 2026 |
| L020 | Lane 2014 (thesis) | read (B85 page level); self-checked (B85) | what chapter 6 already covered | before 2016 |
| L055 | Lane 2010 | read (B85 page level); self-checked (B85) | what the 2010 review already covered | before 2016 |

Year mix (7 rows): before 2016: 3; 2016 to 2019: 2; 2020 to 2026: 2.

**6. Gaps.**
1. The selection record: how many works each route found, how many were read, cited and excluded, and why, with each cited work's reading label. No csv holds this. Job: a counting pass over the register, B14, B15, B61, B63 and the B74, B82 and B83 rows, written to a csv with a script. Points 3 and 4 carry the section's purpose and cannot be drafted without it.
2. Closed by decision 64: Sukhera 2022 (L202) has a page-level read (B78).

**7. Open decisions.**
* Binding: 42 (rule, citations for the type and style), 36 (acquisitions), 50 (government documents as grey literature), 64 (page-level reads), 82 (rows with no file). B68 decision 3 is settled by 42.
* Open: none.

**8. Word budget and dependencies.** About **450 words**: six short points; reviewers of a narrative review want the rule and the routes stated, not a protocol. Dependencies: the selection record (gap 1).

---

## Section 4. A catalogue of methods

**1. Purpose and argument.** The section sorts the methods into families, each by the question it answers, its inputs and outputs, and its scale, so a reader can see that the published figures answer different questions before any number is compared. Families new to the author's earlier work are treated in full; the planning-oriented studies of the 2010 review get one line each and a pointer. The catalogue sets up the tests: each family tested in section 5 is described here with what it counts and what it leaves out, stated as what the method can and cannot see (decision 33).

**2. Content list.**
1. Resource-based land and diet (the thesis method; Peters for New York State and the United States; Fairlie for Britain), with its spatial form, the foodshed (Peters 2009; Zumkehr and Campbell; Kurtz) (decision 57).
2. Energy and protein balance (Gifford, second-hand; Henry and Godden), scaled to Nix's intensive land base; Shepon as a gain, not a capacity.
3. Commodity balance (Foran and Poldy) and the nutritional food balance (Ridoutt 2017, an index with no people count).
4. Export-inclusive counts (Bellotti; CSIRO and UQ; PMSEIC as X-2 words it: 60 million on p. 1 with no source, and on p. 15, citing DAFF 2009, some 40 million fed abroad, not added by the report), with the statistics they draw on. No remark on how other authors cite PMSEIC (decision 33; B230's aside on Ridoutt 2017 is not used).
5. Ecological footprint: origin (Rees; Wackernagel 1994), Australian applications (Simpson; Lenzen and Murray), the accounts (Lin; Wackernagel 2019), and the critique and defence (Blomqvist; Giampietro and Saltelli; Goldfinger).
6. Land per diet indices (Alexander's HALF; Kastner; Röös; van Zanten; Schon and Bohringer; Ridoutt 2020) and people per hectare (Cassidy).
7. **B4.8 Integrated resource-flow models.** Stocks and flows (Foran and Poldy), Australian scenario models (Hatfield-Dodds; Bryan 2016), the FABLE Calculator (Navarro Garcia; Jones 2023) and the World3 line (Herrington); Limits to Growth by one line through the 2010 review.
8. **B4.7 Optimisation models (diet and land use)** (decision 57). Diet optimisation at national scale (Chaudhary and Krishna; Gazan; van Dooren), Ridoutt 2021 as a scored, not optimised, comparison, and LUTO as a land-use optimisation model (decision 41); EAT-Lancet as a judged diet, context only.
9. Failure probability (Fearnside 1985 and 1990): failure as the share of settler-years below a standard (calories at 2,550 kcal a person a day in the English original, B122), capacity read from a density-by-failure curve.
10. **B4.9 Water-bounded capacity.** Land-suitability, water and realistic-yield bounds (Khorsandi 2022 and 2023, catalogue only, decision 26; Fischer; Mesgaran; Rosa 2018; Kummu 2016; Li et al. 2018; Gerten 2020).
11. Index methods in regional assessment (Graymore) and the planning-oriented studies (South East Queensland, Noosa, Douglas Shire), one line each with a pointer to the 2010 review.

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | register L040 (pp. 148 to 152), L015, L041, L077, L103, L104 | none needed (descriptions) |
| 2 | B029 (what the balance counts); B010 (Nix's land is "intensive") | B029: C, yes. B010: B, yes with notes |
| 3 | B155 (what the commodity balance asks) | C, yes |
| 4 | B166 (published export counts are neither energy- nor land-based); register L136 (pp. 1, 15) | C, yes after correction (41 to 54 million). B230 not cited (decision 33) |
| 5 | B049 (food-row footprint recipe) | C, yes |
| 6 | B071 (HALF allocation); B087 (people per hectare allocation) | C, yes |
| 7 | register L007, L075, L076, L208 to L211 | none needed; L211 page-read (B78) |
| 8 | register L204 to L207, L208 (p. 217, linear programming), L081 | none needed; L207 page-read (B78) |
| 9 | B122 (Fearnside's four criteria; 2,550 kcal) | C, yes after correction (2,550 in the English original; 2,500 in the Spanish translation only) |
| 10 | register L073, L074, L029, L212 to L215, L083 | none needed; L212 to L214 page-read (B78) |
| 11 | register L091, L034, L055 | none needed |

**4. Tables and figures.**
* Table 2, the catalogue (family, question answered, inputs, outputs, scale, register ids): no csv and no script. A csv and a script are needed (gap 4).
* Figure 1, the methods mapped by the question each answers: from the same csv; no script.

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L020 | Lane 2014 (thesis) | read (B85 page level); self-checked (B85) | resource-based land and diet: the thesis method | before 2016 |
| L012 | Lane, Dawes and Grace 2014 | read; unverified | resource-based land and diet: essential parameters | before 2016 |
| L040 | Peters, Wilkins and Fick 2007 | read; self-checked (B62 full text) | complete-diet land model, New York State | before 2016 |
| L015 | Peters et al. 2016 | read (B85 page level); self-checked (B85) | US agricultural land under ten diets | 2016 to 2019 |
| L041 | Fairlie 2007 | read; self-checked (B62 full text) | UK land budget under six farming regimes (one line, planning-oriented) | before 2016 |
| L034 | Gutteridge 2005 | read (B85 page level); self-checked (B85) | South East Queensland (one line, planning-oriented) | before 2016 |
| L037 | Limits to Growth | not reached; unverified | one line, through the 2010 review only (not reached) | before 2016 (undated; by context) |
| L038 | Noosa study | not reached; unverified | one line, through the 2010 review only (not reached) | before 2016 (undated; by context) |
| L039 | Douglas Shire study | not reached; unverified | one line, through the 2010 review only (not reached) | before 2016 (undated; by context) |
| L077 | Peters et al. 2009 | read (B85 page level); self-checked (B85) | foodshed: spatial land and diet | before 2016 |
| L103 | Zumkehr and Campbell 2015 | read; self-checked (B54a full text) | foodshed: result turns on radius | before 2016 |
| L104 | Kurtz et al. 2020 | read; self-checked (B54a full text) | foodshed: US metropolitan shares | 2020 to 2026 |
| L003 | Henry and Godden 1995 | read (B85 page level); self-checked (B85) | energy and protein balance: the recipe | before 2016 |
| L002 | Gifford et al. 1975 | reported; self-checked (B85) | energy and protein balance: founding work, second-hand (decision 39) | before 2016 |
| L035 | Nix (70 Mha) | reported; self-checked (B85) | the intensive land base the balance scales to, second-hand | before 2016 (undated; by context) |
| L124 | Shepon et al. 2016 | read (B85 targeted); self-checked (B85) | energy and protein: a gain from reallocation, not a capacity | 2016 to 2019 |
| L007 | Foran and Poldy 2002 | read (B85 page level); self-checked (B85) | commodity balance; also integrated resource flow (stocks and flows) | before 2016 |
| L079 | Ridoutt et al. 2017 | read; self-checked (B54a full text) | nutritional food balance (an index, no people count) | 2016 to 2019 |
| L105 | Fader et al. 2013 | read; unverified | export-inclusive and land-boundary reading | before 2016 |
| L137 | Department of Agriculture 2014 | read; self-checked (B56 full text) | export-inclusive counts: source statistics | before 2016 |
| L139 | Rees 1992 | read; self-checked (B62 full text) | footprint: origin | before 2016 |
| L140 | Rees 1996 | read; self-checked (B62 full text) | footprint: world-average productivities | before 2016 |
| L134 | Wackernagel 1994 | read (B45, two passes on the tables); self-checked (B45) | footprint: rates (thesis, pp. 279 to 298) | before 2016 |
| L023 | Simpson, Petroeschevsky and Lowe 2000 | read (B85 page level); self-checked (B85) | footprint applied to Australia | before 2016 |
| L022 | Lenzen and Murray 2001 | read (B85 page level); self-checked (B85) | modified footprint for Australia | before 2016 |
| L025 | Lin et al. 2018 | read (B85 page level); self-checked (B85) | National Footprint Accounts method | 2016 to 2019 |
| L129 | Wackernagel et al. 2019 | read; self-checked (B54b full text) | footprint accounts, rationale and use | 2016 to 2019 |
| L085 | Giampietro and Saltelli 2014 | read; self-checked (B50a full text) | footprint: the critique | before 2016 |
| L086 | Goldfinger et al. 2014 | read; unverified | footprint: the defence | before 2016 |
| L087 | Blomqvist et al. 2013 | read; unverified | footprint: the critique | before 2016 |
| L131 | Wiedmann and Lenzen 2018 | read; unverified | footprints in general, context | 2016 to 2019 |
| L017 | Alexander et al. 2016 | read (B85 page level); self-checked (B85) | land per diet: the HALF index | 2016 to 2019 |
| L016 | Cassidy et al. 2013 | read (B85 page level); self-checked (B85) | people nourished per hectare | before 2016 |
| L080 | Kastner et al. 2012 | read (B85 targeted); self-checked (B85) | land per diet, global change | before 2016 |
| L114 | Schon and Bohringer 2023 | read; self-checked (B54b full text) | land per diet, German state and regions | 2020 to 2026 |
| L096 | Ridoutt et al. 2020 | read; unverified | cropland footprints of Australian diets | 2020 to 2026 |
| L116 | Roos et al. 2017 | read; unverified | land per diet, grazing | 2016 to 2019 |
| L117 | van Zanten et al. 2016 | read; self-checked (B54b full text) | land per diet, livestock on leftovers (protein only) | 2016 to 2019 |
| L075 | Hatfield-Dodds et al. 2015 | read; self-checked (B50a full text) | integrated scenario model, Australia (context) | before 2016 |
| L076 | Bryan et al. 2016 | read; self-checked (B50a full text) | integrated land-use scenarios, Australia (no people count) | 2016 to 2019 |
| L209 | Navarro Garcia et al. 2022 | read (B66f targeted); self-checked (B66f) | FABLE Calculator, Australia (no optimisation) | 2020 to 2026 |
| L211 | Jones et al. 2023 | read (B78 page level); self-checked (B78) | the FABLE initiative | 2020 to 2026 |
| L210 | Herrington 2020 | read (B66f targeted); self-checked (B66f) | World3, the Limits to Growth line | 2020 to 2026 |
| L208 | Gao and Bryan 2017 | read (B66f targeted); self-checked (B66f) | LUTO: optimisation models (diet and land use) (decisions 41, 57) | 2016 to 2019 |
| L204 | Chaudhary and Krishna 2019 | read (B66f targeted); self-checked (B66f) | diet optimisation at national scale | 2016 to 2019 |
| L205 | Gazan et al. 2018 | read (B66f targeted); self-checked (B66f) | review of diet optimisation | 2016 to 2019 |
| L207 | van Dooren 2018 | read (B78 page level); self-checked (B78) | linear programming for diets | 2016 to 2019 |
| L206 | Ridoutt et al. 2021 | read (B66f targeted); self-checked (B66f) | Australian diets against planetary limits (scored, not optimised) | 2020 to 2026 |
| L083 | Gerten et al. 2020 | read; unverified | land-boundary capacity, global | 2020 to 2026 |
| L081 | Willett et al. 2019 | read; self-checked (B50b full text) | a judged reference diet, not an optimisation (context only) | 2016 to 2019 |
| L042 | Fearnside 1985 | read (B85 page level); self-checked (B85) | failure probability: method detail (English original on file; 2,550 kcal) | before 2016 |
| L043 | Fearnside 1990 | read (B85 page level); self-checked (B85) | failure probability: overview and one result | before 2016 |
| L073 | Khorsandi et al. 2022 | read (B85 page level); self-checked (B85) | water-bounded capacity (catalogue only, decision 26) | 2020 to 2026 |
| L074 | Khorsandi et al. 2023 | read; unverified | water-bounded meta-model | 2020 to 2026 |
| L029 | Fischer et al. 2002 | read (B85 page level); self-checked (B85) | land suitability (GAEZ) | before 2016 |
| L212 | Mesgaran et al. 2017 | read (B78 page level); self-checked (B78) | land suitability, Iran | 2016 to 2019 |
| L213 | Rosa et al. 2018 | read (B78 page level); self-checked (B78) | water bound on irrigation expansion | 2016 to 2019 |
| L214 | Kummu et al. 2016 | read (B78 page level); self-checked (B78) | water scarcity over the 20th century | 2016 to 2019 |
| L215 | Li et al. 2018 | read (B66f targeted); self-checked (B66f) | water resources carrying capacity methods (cite as Li et al.) | 2016 to 2019 |
| L091 | Graymore et al. 2010 | read; self-checked (B50a full text) | a regional capacity index (pressure index, not food) | before 2016 |
| L010 | CSIRO and UQ 2025 | read (B85 page level); self-checked (B85) | export-inclusive count by proportion | 2020 to 2026 |
| L009 | Bellotti 2017 | read; unverified | export-inclusive count | 2016 to 2019 |
| L136 | PMSEIC 2010 | read; self-checked (B52 full text) | export-inclusive figure as X-2 words it | before 2016 |

Year mix (63 rows): before 2016: 32; 2016 to 2019: 20; 2020 to 2026: 11. Three of the rows before 2016 are not reached (L037 to L039) and are cited only through the 2010 review.

**6. Gaps.**
1. Closed: the English original of Fearnside 1985 is on file at L042's local path (the register's note corrects the earlier "Spanish translation" reading; B122 confirms 2,550 kcal).
2. No method paper for the stocks-and-flows framework (B61 point B4.8; B63 found none after 2016). Kind of source: a framework paper such as Turner et al. 2011 (B61 candidate). Job: acquisition, or describe the framework from Foran and Poldy 2002 alone and say so.
3. Closed by decision 64: L207, L211, L212, L213 and L214 have page-level reads (B78).
4. Table 2 and Figure 1 have no data file. Job: a catalogue csv with a script, each cell traced to a register row.
5. The family descriptions in the claims register are verified (V31: B029, B049, B071, B087, B155; B122 and B166 after correction), but there are none for the foodshed, footprint critique, integrated, optimisation and water-bounded families. Job: register rows and a one-route check of each description against its source page.

**7. Open decisions.**
* Binding: 24 and 26 (Khorsandi in the catalogue, not tested), 39 (Gifford second-hand), 41 (LUTO with optimisation models), 46 (PMSEIC per X-2), 57 (B4.7 renamed "optimisation models (diet and land use)"; the foodshed as the spatial form of resource-based land and diet), 64 (page reads), 33 (tone), 36 (acquisitions). B68 decision 2 is settled by 41.
* Open: none. Outline edit outside this file: OUTLINE.md's method-tests row says "2,500 kcal a person a day in the text, 2,550 in a figure caption", against B122.

| # | Question | Options | Recommended | Confidence | Reason |
|---|---|---|---|---|---|
| Q3 | Family headings in section 4 | Settled by decision 57: option (a), B4.7 renamed "optimisation models (diet and land use)", the foodshed as the spatial form of resource-based land and diet | settled (57) | n/a | n/a |

**8. Word budget and dependencies.** About **1,800 words**: eleven families at 120 to 250 words each, the planning studies in one line each, with Table 2 carrying inputs, outputs and scale so the prose can stay short. Dependencies: the catalogue csv; register rows for the five undescribed families (gap 5).

---

## Section 5. Testing the methods on common Australian data (the core)

**1. Purpose and argument.** This is the core of the paper: each method is applied to the same 2025 Australian data, wherever its author first used it, and checked against its author's own figure where that can be reached (a fidelity check, not the test). For each method the section states the access the project had (sources and pages), the assumptions made, and whether the authors' figure was reproduced or not reproduced on that basis, naming the build and the basis for each verdict (decision 33). The author's model is entered the same way, as published and as built on. The result is the methods side by side on one data set. The harmonised comparison shows that equalising inputs narrows the spread within the energy balance and people per hectare while the footprint keeps its definitional spread, and that the gap between methods does not narrow, so the gap is the method (decision 35).

**2. Content list.**
1. The common data set: one population, data year, land base and consumption basis for every method (2025 only; decision of 2026-11-06).
2. Fidelity check against test: what each is, and how each method is reported (fidelity-checked implementation, or implementation from the published description alone).
3. Energy and protein balance: the recipe's arithmetic reproduces 109 and 96 from Henry and Godden's printed totals; the 1990-91 totals themselves were not rebuilt (B015, L052, L053). On current data it reads 134 to 211 million, a spread across two currencies (energy, protein) and three land-base cases, not an uncertainty range; the 2025 in-use land is the 1990-91 value carried forward (B027). What it hides (land base, exports eaten at home, the consumption factor). Where the residual against 109 and 96 is within the published rounding, the text says "within rounding" and prints no percent-of-residual (pending B93).
4. Ecological footprint, food row: three builds (decisions 12 and 32). Pasture reproduced within 3% at the thesis's sourced rate in build 3 (1.718 ha against 1.758, B260; the paper quotes 1.718); feed crop reproduced in builds 1 and 2 (build 3 is 22% high, B034); build 1 reproduces both, but its pasture rate is not the thesis's printed rate. Plant-food crop and clothing wool not reproduced from the published sources. Read as a capacity: 146 to 343 million on current yields (103 million at 1990 world yields) (B94, decision 85).
5. HALF: reproduced for Australia and the world on 2011 data (world within 2.2% unrounded, 2.1% as printed; Australia within 0.8%), not for New Zealand; 2021-23 value and its capacity reading.
6. People per hectare: shares and delivered fraction reproduced within a few points for the world, India, China and Brazil, not for the United States (B073, B078); the 2011 rebuild uses 22 crop items (B079); two builds; 145 to 147 million delivered; about 190 on all cropland, a typed figure that scales build 1 only (B084). Figures pending B93 (Cassidy rerun with harvests matched).
7. Commodity balance: 1997-98 production and the published balance reproduced (grain within 1.2%; meat 1.22%, within about 1.2%, B141); meat, fish and grain readings on current data.
8. Failure probability: the model read through Fearnside's failure frame (its readings are the model's own runs, B275), applied as a test of the idea, not as an independent method on the data (no check against Fearnside's Brazilian figure); capacity by return period and today's failure probability.
9. The author's model as an exemplar: as published (thesis method as built), corrected, and improved, each with its Monte Carlo range.
10. The methods side by side: three groups (aggregate methods, the commodity balance and the failure view, the model). The aggregate methods read about three to eight times the model (B94); the commodity balance reads 12 to 41 million (fish 12 is a single-commodity reading); the failure view is the model's own runs. No sentence says one group's readings are "the model's range" or that the model's range contains the failure view's average-year point, since that holds by construction.
11. The harmonised comparison (decision 35): inputs equalised; the spread within the energy balance (145.2 and 148.8, B264) and people per hectare (B273) narrows, the footprint keeps a factor of about 2 (146 to 288 for build 3, B268; 160 to 343 for build 1, B267); the spread among methods does not narrow (B277; both lows are the single-commodity fish reading, B151, and the endpoints leave out the pasture-alone readings); inputs are 10% and methods 90% of the ratio-scale distance on one row set, 10 to 18% on other definitions (B276). The footprint at Australian productivity as the adjustment Wackernagel and Rees 1996 describe on p. 78 (B270).
12. Gap attribution (decision 34): how much each candidate cause explains of each residual against the authors' figures; where the residual is within the rounding of the published figure, "within rounding" and no percent-of-residual. Pending B93 (decision 88).

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | B094 (population 27.6); B262 (one land base, 363.5 Mha); B263 (common consumption basis) | B094, B262, B263: B, yes |
| 2 | none needed (rule: CARD, "Methods paper (B)") | none needed |
| 3 | B015 (arithmetic fidelity); B016 to B018, B019 (134 to 211); B020, B021; B022 to B025; B026 to B028 (limits); authors' figures B008 to B014; B321 (residuals within half a unit) | B019: A, yes. B015 to B018, B020 to B024, B026, B027: B, yes. B025: B, yes with notes. B028: C, yes. B008, B014: B, yes. B010: B, yes with notes. B009, B011 to B013: B, unverified. B321: pending B93 |
| 4 | B033, B034, B260 (reproduced, by build); B035, B261 (not reproduced); B036; B038 to B041, B044, B046 (146 to 343 on current yields; 103 at 1990 yields); B267, B268 (current yields); B042, B043, B045 (consumption and land behind the reading); B256 (second build); B047; B048 (limits); authors' figures B030 to B032; B037 withdrawn; B295 (why 1.713 differs) | B040, B046: A, yes (B046 reworded by B94). B033, B034, B036, B038, B039, B042 to B044, B256, B260, B261, B267, B268: B, yes. B041: B, yes (reconstruction, under-specified). B045, B047: B, yes after correction. B035: B, yes (records not reproduced). B048: C, yes. B030, B032: B, yes. B031: B, unverified. B037: C, withdrawn. B295: pending B93 |
| 5 | B058 (fidelity summary); B052 to B057; B059, B060; B062 to B067; B068 (276); B061 (limits); B249 | B058, B068: A, yes. B053, B055 to B057, B059, B060, B062 to B064, B066: B, yes. B052, B067, B249: B, yes with notes (B052: 2.2% unrounded). B054, B065: B, self-checked. B061: C, yes after correction |
| 6 | B078 (fidelity; world, India, China, Brazil); B072 to B077, B079, B080, B257; B081, B082, B083 (145 to 147), B084 (190, typed); B085; B258, B259 (second build); B086 (limits) | Pending B93 for the figures. As the register stands: B078, B083, B084: A, yes. B072, B076, B077, B081, B082, B257 to B259: B, yes. B079: B, yes after correction (22 crop items). B085: B, yes with notes. B073 to B075: B, self-checked. B080: C, yes with notes. B086: C, yes. B081 and B083 say "21 crops" (register edit listed) |
| 7 | B141 (fidelity); B142, B143; B140, B144; B145 to B152; B153 (summary); B154; B222 (register readings) | B153: A, yes. B140 to B142, B146 to B152, B222: B, yes. B143 to B145, B154: B, yes with notes |
| 8 | B137 (41.5 to 18.9); B130 (failure probability today); B131 to B134; B275 (the model's own runs); B121 (Fearnside's own result, context); B139 (limits); `fearnside_failure_curve.csv` | B130, B137: A, yes. B131, B134, B275: B, yes. B132, B133: B, self-checked. B121, B139: C, yes. B131 is a 2011 figure (X-11) |
| 9 | B088, B089, B104, B105, B110, B111 (as built); B090, B091, B112, B113 (corrected); B092, B093, B114, B115 (improved) | B090 to B093, B112, B114: A, yes. B088, B089, B104, B105, B110, B111, B113, B115: B, yes |
| 10 | B156 (three groups); B157; B159; B158; B247; B275 | B156, B159: A, yes (B156 reworded by B94; its clause "the model's range" goes, register edit listed). B157, B247: B, yes (B247 reworded by B94; B157's containment sentence goes, register edit listed). B158: B, yes with notes (2025 national readings only). B275: B, yes |
| 11 | B264, B266, B272, B273, B274, B276, B277; B265, B267 to B271; B275; B151 | B264, B266, B272 to B274, B276, B277: A, yes (B276: 10 to 18% by row set; B277: endpoints leave out pasture-alone readings, V26). B151, B265, B267 to B271, B275: B, yes. B277's "17 as run" against B151's 12 as run: register edit listed |
| 12 | B278 to B332 (gap attribution rows, decision 65); `analysis/method_tests_2025/gap_attribution.csv` (checked by V25) | B, unverified; one-route check pending B93 (decision 88) |

The 2011 rows of the model (B123 to B129, B131, B135) exist but belong in Paper A (decision 58; X-11).

**4. Tables and figures.**
* Table 3, each method's reading of Australia on current data: `analysis/method_tests_2025/cross_method.csv`; script `cross_method.py`, table writer `make_readme_tables.py` (exists). The footprint row names the yield basis of each end (B94).
* Table 4, the model's entry by tier with ranges: `analysis/method_tests_2025/model_entry.csv`; script `cross_method.py` (exists); ranges from `results/ranges_2025-*.csv`.
* Table 5, the harmonised comparison: `analysis/method_tests_2025/harmonised_comparison.csv`; script `harmonised_comparison.py` (exists).
* Supplementary table, fidelity checks and gap attribution: `published_values.csv`, `second_build_values.csv`, `simpson_food.csv`, `half_index.csv`, `cassidy.csv`, `foran_poldy_balance.csv`, `henry_godden_summary.csv`, `gap_attribution.csv`; scripts exist for each output; no script assembles the supplementary table. The Cassidy rows add `cassidy_matched.csv` once B93 writes it.
* Figure 2, the same data through each method: `cross_method.csv` and `harmonised_comparison.csv`; no plotting script.

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L003 | Henry and Godden 1995 | read (B85 page level); self-checked (B85) | the energy and protein recipe and Table 5 (arithmetic fidelity check) | before 2016 |
| L035 | Nix (70 Mha) | reported; self-checked (B85) | the intensive land base of the recipe, second-hand | before 2016 (undated; by context) |
| L023 | Simpson, Petroeschevsky and Lowe 2000 | read (B85 page level); self-checked (B85) | the food row and recipe (fidelity check) | before 2016 |
| L134 | Wackernagel 1994 | read (B45, two passes on the tables); self-checked (B45) | pasture and wool rates for the third build (decision 32) | before 2016 |
| L050 | Wackernagel and Rees 1996 | read (B44 from the filed scan); unverified | p. 78, the adjustment for local productivity (decisions 35, 65); its `what_taken` leads with the withdrawn 2.8 factor (register edit listed) | before 2016 |
| L051 | ABS 4306.0 (1991-92 data) | read (B85 page level); self-checked (B85) | 1991-92 consumption for the footprint fidelity check | before 2016 (undated; by context) |
| L052 | ABS 7503.0 (1990-91 data) | read (B85 page level); self-checked (B85) | 1990-91 unit values; not used to rebuild the 1990-91 totals | before 2016 (undated; by context) |
| L053 | ABARE 2010 | read (B85 targeted); self-checked (B85) | commodity statistics; cannot rebuild Henry and Godden's 1990-91 totals | before 2016 |
| L017 | Alexander et al. 2016 | read (B85 page level); self-checked (B85) | HALF recipe and supplement (fidelity check) | 2016 to 2019 |
| L016 | Cassidy et al. 2013 | read (B85 page level); self-checked (B85) | people per hectare recipe (fidelity check) | before 2016 |
| L007 | Foran and Poldy 2002 | read (B85 page level); self-checked (B85) | Table 2.5 requirements and 1997-98 production (fidelity check) | before 2016 |
| L042 | Fearnside 1985 | read (B85 page level); self-checked (B85) | failure-probability frame (English original) | before 2016 |
| L043 | Fearnside 1990 | read (B85 page level); self-checked (B85) | the one published result, context only | before 2016 |
| L030 | FAO, IIASA and UNFPA 1982 | reported; unverified | the comparison figure in Fearnside 1990, second-hand | before 2016 |
| L006 | Jones committee 1994 | read; unverified | 30 to 35 million set beside the 1-in-10 point, as summarised in the thesis until read (decision 89) | before 2016 |
| L020 | Lane 2014 (thesis) | read (B85 page level); self-checked (B85) | the thesis method as published | before 2016 |
| L014 | Lane 2017 | read; unverified | short-term and long-term settings | 2016 to 2019 |
| L083 | Gerten et al. 2020 | read; unverified | a comparator for a range (register use) | 2020 to 2026 |
| L105 | Fader et al. 2013 | read; unverified | a comparator for a range (register use) | before 2016 |

Data sources are in `qa/sources_register.csv`, not the literature register: FAOSTAT food balances, production and land use (D17 to D19) and the test extracts (D22 to D28), and the model's 2025 data (D47 to D49). They are cited in the data statement and the table notes.

Year mix (19 rows): before 2016: 16; 2016 to 2019: 2; 2020 to 2026: 1. The section cites the methods' own papers and their input statistics, which are old by nature; recent works enter in sections 4, 6 and 8.

**6. Gaps.**
1. Gap attribution (decision 34) has rows B278 to B332 (decision 65), all unverified; several shares are of residuals inside the published rounding (B302 "+731%", B296 "-1057%", B321). Job: B93's one-route check (decision 88), then only the checked rows are quoted, with "within rounding" where it applies. Pending B93.
2. Wackernagel and Rees 1996 (L050) is read from the filed scan (decision 65) but its status is unverified and its `what_taken` leads with the withdrawn equivalence factor 2.8 (B037). Job: register edit so the row leads with p. 78; the text says "the adjustment the book describes", not "sanctioned".
3. Five of the authors' own figures used for the fidelity checks are still unverified (B009, B011, B012, B013, B031). Job: a one-route recheck of each against the page it is read from.
4. Figure 2 has no plotting script. Job: a script over `cross_method.csv` and `harmonised_comparison.csv`.
5. The people-per-hectare figures (B081 to B084, B258, B259) wait on the Cassidy rerun with harvests matched (B93, `cassidy_matched.csv`); the crop count (21 in B081 and B083, 22 in B079) is settled in the same pass. Pending B93.

**7. Open decisions.**
* Binding: 8 (frozen releases), 12 (Simpson and Cassidy as ranges), 27 (Monte Carlo rerun), 32 (third Simpson build), 33 (tone), 34 (gap attribution), 35 (harmonised comparison; figures quoted only after V26, which is done), 39 (Gifford second-hand), 58 (no 2011 check column), 65 (gap-attribution rows; L050 read from the filed scan), 85 (footprint low end, applied by B94), 88 (gap-attribution check and Cassidy rerun, B93); the 2026-11-06 decisions (no reproduction gate; 2025 data only; the model as one exemplar).
* Open: none.

| # | Question | Options | Recommended | Confidence | Reason |
|---|---|---|---|---|---|
| Q4 | Keep one 2011 check column? | Settled by decision 58: no 2011 column; the harmonised comparison is the check | settled (58) | n/a | n/a |

**8. Word budget and dependencies.** About **2,300 words**, the largest section: seven tests at about 220 words each (access, assumptions, fidelity result with its build and basis, reading on current data), about 250 for the common data and the fidelity rule, and about 500 for the side-by-side and the harmonised comparison. The numbers sit in Tables 3 to 5 and the supplementary table, so the prose carries access, assumptions and verdicts. Dependencies: B93 (gap attribution and Cassidy); the L050 register edit (gap 2); the register edits to B156, B157, B277, B081, B083; Figure 2 script.

---

## Section 6. What moves the number

**1. Purpose and argument.** The section measures, with the model on the same data, what each design choice does to the answer: exports, diet, waste, a drought allowance, the land base, the unit of self-sufficiency, the yield basis, the time frame and uncertainty. It shows that the spread across the settings the author judges defensible (factor 1.26) is small beside the definitions, and that one judged choice, the herd and meat data window, drives most of that spread (81% of the short-term variance, B117). It reads the published spread along a ladder of definitions without calling it a decomposition. Three choices are where the model's Australian settings enter (grazing and pasture-fed food, waste, the land base), each introduced by what the other methods show; the paper says the comparison shows where each choice matters, not that it produced the improvements (outline caution). Uncertainty is treated as a design dimension through the Monte Carlo.

**2. Content list.**
1. Exports counted or not: the published export-inclusive counts and an energy count of exports, against the model. CSIRO and UQ: 27 million at home plus 63 abroad, "around 100 million" in the report's words (B162; Q9 sets whether the factors are given on 100 or 90). The NFF's "feeds 75 million" is untraced (B163, L011) and is dropped, or cited only as a submitter's claim reported by the 2023 House committee (L229, p. 24).
2. **Grazing and pasture-fed meat and dairy** (the yield basis): how each method treats it, and the model's Australian setting (beef output by state, dairy on land that can carry it, the organic ruminant factor). Pasture is 44% of Simpson's whole footprint (2.61 of 5.96, B050), not of the food row; animal products, particularly beef, drive HALF for New Zealand, Argentina and Australia together, with no Australia-only beef split (B070).
3. **How waste is treated**: production counted as eaten, waste inside the diet, US loss factors; the model's Australian loss factors and the recycling credit. In decision 72's words (X-1): the model's 6% setting halves the model's retail-and-consumer loss share, mirroring UN Target 12.3; Australia's own goal (National Food Waste Strategy 2017, p. 8 printed) is whole-chain halving by 2030; the 2016-17 Baseline is 7.3 Mt (L231) and the later 7.6 Mt estimate is the 2021 Feasibility Study (L242), each named with year and source.
4. **Which land counts** (the land base): Nix's 70 Mha of intensive land, New York State's three land classes, doubled cropland (Gifford scaled intensive land from 40.5 to 70 Mha, B232), suitability; the model's reserve rule.
5. Diet: guideline diets by meat share and the nutrition-optimised diets. On the improved release capacity is not monotone in meat share: a dip at 2.5% and a cliff between 5% (103.3, B208) and 7.5% (66.9, B209) (decision 31); "a little meat beats none" on the corrected release only (X-5); "5% meat and eggs" named with its release and setting (X-6). EAT-Lancet supports diet as a lever for emissions, not for cropland.
6. The drought allowance: the failure-probability view as a design choice; the model supplies the allowance as a quantity (23 to 30 million at 50 years and 19 to 25 at 100, B199). The Jones figures the allowance is set beside are quoted as summarised in the thesis until the report is read (decision 89).
7. **The unit of self-sufficiency** (scale), shown with three points: nation, states, SA2 sum (decision 59); the full curve is Paper A's. The text says the three points sit on two land bases (national and state rows on the release land, SA2 on "2020-21 land", B173 to B175 notes) and on the state yield basis; on the local yield basis the SA2 sum is 54% (A098, A108). The 15.5 million is named by its meaning (X-8).
8. The time frame: short-term and long-term settings.
9. **How sure the answer is, as a method**: the Monte Carlo (Latin hypercube; 13 sampled, 12 vary in the 2025 corrected and published releases; in 2025-improved the benchmark is drawn but has almost no effect; 1,000 draws) and its test, the additive shortcut checked against full runs (B116). The ranges are a spread across the settings the author judges defensible, not confidence intervals; one judged choice (the herd and meat data window) explains 81% of the short-term variance (B117). Five range ends are the author's judgement: the meat-window three-way choice, the meat-and-egg share of diet low end 0.115, the red-meat share of meat low end 0.528 (X-4), the 50/50 weight on the leave-one-out resilience table, and the long-term benchmark low end 0.30. Method references L235 to L237 (decision 67), record only.
10. The spread across defensible settings against the definitions, and the ladder: where the published spread sits, read as a reading, not a decomposition (B192: a telescoping identity). The span by definition is quoted in the one reading Q8 sets for the whole paper; the ladder mixes tiers (corrected low steps, improved high steps), and the factor from 9.4 to 15.6 mixes a data change with the correction (X-10).
11. The ordering of the design choices as `design_choices.csv` gives it: land matters least (1.09), then waste (1.17 to 1.33) and the Australian settings (1.29); then guideline diets (2.14), the drought allowance (2.19), exports counted proportionally (2.41), the time frame (2.66) and the unit (2.67); then exports by energy (4.4 to 6.4) and the optimised diet (7.88). Diet is named with both readings.

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | B162, B185, B186, B191; B161, B163, B164, B165, B166; register L229 (p. 24) | B162, B165, B185, B186, B191: A, yes (B185, B191 on 100; Q9). B164: B, yes. B161: B, yes with notes. B163: B, unverified (no NFF or industry source found). B166: C, yes after correction |
| 2 | B050 (44% of the whole footprint), B051 (8.1 of 13.6), B070, B231, B233; B069; B183 (corrected to improved); B234 | B183: A, yes. B050, B051: B, yes. B069: B, yes with notes. B070, B234: C, yes with notes (B070: three countries together, no Australia-only split). B231, B233: C, yes |
| 3 | B168, B169 (waste factors); B108 (no avoidable waste); decision 72 wording; `analysis/waste_2025/README.md` lines 65 to 70; register L230 (p. 8 printed), L231, L242, L163 (pp. 118 to 119), L160 (p. 162) | B108, B168, B169: A, yes. Waste source rows: single reading (B83, B82, B66b) |
| 4 | B170 (land 1.09); B106, B107, B109; B200, B225; B232 | B170: A, yes. B106, B107, B200: B, yes. B109: B, yes with notes. B225: B, yes after correction (58.3). B232: C, yes after correction (40.5 to 70 Mha) |
| 5 | B178, B179, B180, B181, B182; B205 to B216; B201; B202 to B204, B228; B218; A258 (X-6) | B178 to B182: A, yes. B201, B202, B205 to B216: B, yes (B216's note carries superseded values; register note listed). B204, B218, B228: B, yes with notes. B203: B, unverified. A258: A, yes |
| 6 | B167 (2.19); B095 to B103; B196 to B199, B226; B138 | B096, B167: A, yes. B095, B097, B103, B226: B, yes. B098 to B102, B138: B, self-checked. B198: B, yes with notes. B199: B, yes after correction. B196, B197: B, unverified (L006 not on disk; decision 89) |
| 7 | B171 to B177; A098, A108 (local basis) | B175 to B177: A, yes. B171, B174: B, yes. B172, B173: B, self-checked. A098, A108: B (Paper A rows) |
| 8 | B184 (2.66); B160 | A, yes |
| 9 | B187; B116; B117 to B120; B250 to B253; `results/ranges_2025-*.csv`; register L235 to L237 | B187: A, yes. B116: C, yes. B117, B120, B250: B, yes. B253: B, yes with notes (improved release). B118, B119, B251, B252: B, self-checked (A341 and A342, the same ends in Paper A, are yes with notes; register edit listed) |
| 10 | B188, B189, B190, B192, B193, B195; B005; B003 (Q8) | A, yes. B190 and B193: the ladder mixes tiers; "a factor of 4" holds only from 15.6. B189 mixes a data change with the correction |
| 11 | B194; B170, B167, B177, B181, B182, B184, B185, B186 | A, yes. No single row holds the full ordering (gap 6) |

**4. Tables and figures.**
* Table 6, the design choices and their factors: `analysis/method_tests_2025/design_choices.csv`; script `design_choices.py` (exists). Rows in the order of point 11.
* Figure 3, the effect of each design choice, with the ladder: `design_choices.csv` and `ladder.csv`; table script exists (`make_readme_tables.py`), no plotting script.
* Table 7, diets on the improved release: `analysis/comparators_2025/diet_land.csv` (`diet_land.py`, exists) and `analysis/nutrition_lp_2025/variants.csv` (`optimise.py`, `run_variants.sh`, exist).
* Table 8, the Monte Carlo ranges and variance shares: `results/ranges_2025-mirror.csv`, `ranges_2025-fixed.csv`, `ranges_2025-improved.csv`; scripts `monte_carlo.mjs`, `summarise_mc.py`, `rss_check.py` (exist).
* Scale, three points: `results/scale_curve.csv`; `analysis/scale_curve_2025/plot_scale_curve.py` draws Paper A's full curve; no script for the three-point table.

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L023 | Simpson, Petroeschevsky and Lowe 2000 | read (B85 page level); self-checked (B85) | pasture is 44% of the whole footprint (2.61 of 5.96) | before 2016 |
| L022 | Lenzen and Murray 2001 | read (B85 page level); self-checked (B85) | footprint mostly pasture (8.1 of 13.6 ha) | before 2016 |
| L017 | Alexander et al. 2016 | read (B85 page level); self-checked (B85) | animal products, particularly beef, drive HALF for three countries together; grassland intensities, global averages | 2016 to 2019 |
| L040 | Peters, Wilkins and Fick 2007 | read; self-checked (B62 full text) | land base: 2.03 Mha in three classes; diet moves capacity threefold | before 2016 |
| L015 | Peters et al. 2016 | read (B85 page level); self-checked (B85) | US diets turn on grazing land | 2016 to 2019 |
| L016 | Cassidy et al. 2013 | read (B85 page level); self-checked (B85) | grazing left out; production counted as eaten | before 2016 |
| L003 | Henry and Godden 1995 | read (B85 page level); self-checked (B85) | land base rests on Nix; production counted as eaten | before 2016 |
| L035 | Nix (70 Mha) | reported; self-checked (B85) | the 70 Mha of intensive land, second-hand | before 2016 (undated; by context) |
| L002 | Gifford et al. 1975 | reported; self-checked (B85) | intensive land scaled from 40.5 to 70 Mha, second-hand (decision 39) | before 2016 |
| L029 | Fischer et al. 2002 | read (B85 page level); self-checked (B85) | land base resting on suitability | before 2016 |
| L042 | Fearnside 1985 | read (B85 page level); self-checked (B85) | the failure-probability view of the drought allowance | before 2016 |
| L068 | Buzby 2010 | read; unverified | US loss factors used by the thesis model | before 2016 |
| L069 | Muth 2011 | read; unverified | US loss factors used by the thesis model | before 2016 |
| L160 | Reutter et al. 2017 | read (B66b targeted); self-checked (B66b) | caution: household waste totals differ about 3.4 times by method | 2016 to 2019 |
| L163 | Spang et al. 2019 | read (B66b targeted); self-checked (B66b) | UN Target 12.3 scope, which the model's 6% setting mirrors (decision 72) | 2016 to 2019 |
| L230 | National Food Waste Strategy 2017 | read (B83 targeted); self-checked (B83) | Australia's goal: whole-chain halving by 2030 (p. 8 printed) (decision 72) | 2016 to 2019 |
| L231 | National Food Waste Baseline 2019 | read (B83 targeted); self-checked (B83) | 7.3 Mt in 2016-17 (decision 72) | 2016 to 2019 |
| L242 | DCCEEW, "Reducing Australia's food waste" (web page) | read (B82 targeted); self-checked (B82) | about 7.6 Mt, from the 2021 Feasibility Study (decision 72) | 2020 to 2026 |
| L081 | Willett et al. 2019 | read; self-checked (B50b full text) | diet change alone moves global cropland 0 to 2% (p. 472) | 2016 to 2019 |
| L080 | Kastner et al. 2012 | read (B85 targeted); self-checked (B85) | diet as a lever on land | before 2016 |
| L120 | Tilman and Clark 2014 | read; self-checked (B50b full text) | diet as a lever (context, base year named) | before 2016 |
| L115 | Poore and Nemecek 2018 | read; self-checked (B50b full text) | grass on land unsuited to crops | 2016 to 2019 |
| L116 | Roos et al. 2017 | read; unverified | grazing and land per diet | 2016 to 2019 |
| L117 | van Zanten et al. 2016 | read; self-checked (B54b full text) | livestock on leftovers (protein only) | 2016 to 2019 |
| L096 | Ridoutt et al. 2020 | read; unverified | Australian diet choices and cropland | 2020 to 2026 |
| L084 | Erb et al. 2016 | read; unverified | reporting a range of options | 2016 to 2019 |
| L106 | Cohen 2017 | read; unverified | reporting a range, not a single number (cite only if read) | 2016 to 2019 |
| L235 | McKay, Beckman and Conover 1979 | record only; record only | Latin hypercube sampling (decision 67) | before 2016 |
| L236 | Helton and Davis 2003 | record only; record only | Latin hypercube sampling and uncertainty propagation (decision 67) | before 2016 |
| L237 | Saltelli et al. 2008 | record only; record only | variance shares (decision 67) | before 2016 |
| L009 | Bellotti 2017 | read; unverified | exports counted: 61 million | 2016 to 2019 |
| L010 | CSIRO and UQ 2025 | read (B85 page level); self-checked (B85) | exports counted: 27 at home plus 63 abroad, "around 100 million" (Q9) | 2020 to 2026 |
| L011 | National Farmers' Federation | reported; unverified | "feeds 75 million": untraced; drop, or cite only through L229 as a submitter's claim | before 2016 (undated; by context) |
| L229 | House of Representatives Standing Committee on Agriculture 2023 | read (B82 targeted); self-checked (B82) | NFF's "feed 75 million" as a submitter's claim (p. 24), if kept | 2020 to 2026 |
| L006 | Jones committee 1994 | read; unverified | the two figures set beside the model's average year and 1-in-10 point, as summarised in the thesis until read (decision 89) | before 2016 |
| L007 | Foran and Poldy 2002 | read (B85 page level); self-checked (B85) | the meat-limited count | before 2016 |
| L041 | Fairlie 2007 | read; self-checked (B62 full text) | unit of self-sufficiency: a country | before 2016 |
| L034 | Gutteridge 2005 | read (B85 page level); self-checked (B85) | unit of self-sufficiency: a region | before 2016 |
| L073 | Khorsandi et al. 2022 | read (B85 page level); self-checked (B85) | capacity falls as the unit shrinks | 2020 to 2026 |
| L074 | Khorsandi et al. 2023 | read; unverified | scale in a meta-model | 2020 to 2026 |
| L077 | Peters et al. 2009 | read (B85 page level); self-checked (B85) | scale: foodshed | before 2016 |
| L014 | Lane 2017 | read; unverified | the time frame as a design choice | 2016 to 2019 |

Year mix (42 rows): before 2016: 22; 2016 to 2019: 14; 2020 to 2026: 6. Mirosa et al. 2020 (L161) is no longer cited for the 7.3 Mt: it reports the Baseline second-hand, and decision 72 names L231. Lawrence, Richards and Lyons 2013 (L224) is not cited here: decision 46 places its 22 plus 40 million in Paper A section 8 only (X-2).

**6. Gaps.**
1. Closed by decision 67: the Monte Carlo method references are L235 to L237 (record only, not opened; a page read is needed only if a passage is quoted).
2. Closed by decision 72: the waste documents are L230, L231 and L242. The Feasibility Study itself (L232) is not reached and stays optional (decision 72).
3. The Australian loss factors rest on data sources (D40: a bin audit and FAO's regional loss shares) that have no literature-register row to cite in the text. Job: register rows for the cited loss-factor sources.
4. Figure 3 and the three-point scale table have no script. Job: two small scripts over `design_choices.csv`, `ladder.csv` and `results/scale_curve.csv`.
5. Statements the section leans on that are still unverified or self-checked: B203; B196, B197 (Jones, decision 89); B163 (NFF); B098 to B102, B138, B172, B173, B118, B119, B251, B252. Job: a one-route check of each against its source page or output file, and the register edits to B251 (unit "share of meat") and B252 (the improved-release note) so they match A341 and A342.
6. No register row holds the full ordering of design choices that point 11 quotes. Job: one claim row over `design_choices.csv` if the paper prints the ordering.
7. The NFF figure (L011, B163) cannot be traced to an NFF work; the nearest trace is the 2023 House committee's record of it as a submitter's claim (L229, p. 24). Job: decide at drafting (drop, or cite through L229).

**7. Open decisions.**
* Binding: 27 (Monte Carlo rerun), 30 and 31 (diets re-optimised; diet route; "a little meat beats none" kept for the corrected release only), 33, 35, 46 (Lawrence only in Paper A), 54 (thirteen choices wording kept in rerun scripts), 59 (scale points: nation, states, SA2 sum), 63 (any Tier A value change goes to Murray first), 67 (Monte Carlo references), 72 (waste wording; replaces 44), 87 (cross-paper resolutions), 89 (Jones report). Standing: scale as a design choice with three points (CARD).
* Open: outline "Decisions still open" item 2 (where the rest of the model material goes; the improvements as settings in section 6 are proposed and await Murray), Q8 and Q9.

| # | Question | Options | Recommended | Confidence | Reason |
|---|---|---|---|---|---|
| Q5 | Which three points show scale | Settled by decision 59: nation, states, SA2 sum. The outline's source line still names "national, state and NRM rows" (outline edit) | settled (59) | n/a | n/a |
| Q8 | One reading of "the span by definition" for the whole paper (V32b problem 4): section 6 point 10, section 7 purpose 2 (B246) and section 9 point 1 use "a factor of 4" (15.6 to 62.9, B190, B193), which joins a corrected long-term figure to an improved figure; the outline headline and B003 say "about 19 to 55 million by definition alone", with 63 only with the improved settings | (a) use B003's span throughout: 18.9 to 55.3 million by definition alone on the corrected method, 62.9 with the improved settings; B190, B193 and B246 reworded to match / (b) keep "a factor of 4" and call it "definitions and settings" | (a) | Medium | (a) uses a Tier A row already verified, keeps one tier per span and matches the headline; (b) keeps a rounder factor but needs every use to carry the qualifier. Either is a register edit to three rows, and neither needs a new run. Medium because the ladder reading (B192) uses the 4.03 step, which (a) would leave as a ladder step only |
| Q9 | The upper end of the published span (V32b problem 5): the CSIRO and UQ report gives 27 + 63 = 90 and calls it "around 100"; B005, B185, B191 and B192 use 100 | (a) keep 100, the report's own figure ("approximately 100 million" in its foreword, B006 note), and state at first use that its parts sum to 90 / (b) adopt 90 and restate B185, B191 and B192 on 90 (new values computed and registered first), a Tier A change that goes to Murray first (decision 63) | (a) | Medium | (a) quotes the source as it states itself and changes no Tier A value; (b) is arithmetically tighter but replaces the report's headline with the project's sum. Medium because a reader who adds 27 and 63 may prefer (b) |

**8. Word budget and dependencies.** About **1,700 words**: eleven points; the three settings paragraphs (grazing, waste, land base) at about 200 words each because each must say what the other methods assume; the Monte Carlo at about 250; the ladder and the reading at about 250; the factors themselves sit in Table 6 and Figure 3. Dependencies: Q8; Q9; outline item 2; the Jones report (decision 89); Figure 3 script; the register edits in gap 5.

---

## Section 7. Which method for which purpose

**1. Purpose and argument.** The section turns the tests into a guide: a matrix of four purposes against seven methods, a recommendation per purpose, and a minimum reporting checklist. The purposes run in order of how strongly the paper's evidence supports them (food security and drought risk; why national estimates range from 9 to 100 million; regional and local land-use planning; diet change and land use). Its argument is that no single method serves every purpose, that the aggregate methods answer a different question, and that a security claim needs a level and a failure probability from the balance run through the failure view, plus a commodity balance for the item that fails first. The draft (`SECTION7_DRAFT.md`) holds the matrix, ratings and checklist for Murray's edits; the ratings are the author's judgement, re-derived blind (V28, decisions 61 and 69), and are labelled so.

**2. Content list.**
1. The rating key and the seven methods; the four planning-oriented studies of the earlier work treated as the balance family at other scales (B242).
2. Purpose 1, food security and drought risk: the land-and-diet balance and its failure view suited (one model read two ways, B275); commodity balance partly; aggregate methods not suited. The Jones figures enter as summarised in the thesis until the report is read (decision 89), and the text does not say the balance "reproduces" them.
3. Purpose 2, why estimates range from 9 to 100 million: the balance suited; the others partly, each reproducing one family of published estimates (decision 69 for HALF and people per hectare). The span by definition is quoted in Q8's reading.
4. Purpose 3, regional and local planning: only the balance carries a unit of land, a diet and the pasture-crop pairing; scale decides the answer; the scale shares are on the state yield basis and say so (section 6 point 7); the footprint partly (decision 69).
5. Purpose 4, diet change and land use: HALF for comparison across countries; the balance for what Australia's land can feed; the meat-share cliff between 5% and 7.5% on the improved release, and "a little meat beats none" on the corrected release only (X-5).
6. The short reading: no single method serves all purposes; aggregate methods read about three to eight times the balance (146 to 343 million on current yields, 103 at 1990 world yields; B94), consistent with none of them carrying the pairing of pasture-fed food with crops (an interpretation, not tested by removing the pairing, B247); for a security claim, report a level and a failure probability from the balance run through the failure view, plus a commodity balance for the item that fails first.
7. The minimum reporting checklist (twelve items: items 2 to 8 are the design choices measured in section 6, items 1 and 9 to 12 what a reader needs to use the number; decision 60).
8. Cautions: a figure of people fed is not a target; the ratings may differ where grazing is a small share of food land; the ratings are the author's judgement on seven methods; the failure view is the model's own runs.

The draft's 2011 sentences (purpose 1 "7% in 2011", B131; purpose 4 "fell 28% between 2011 and 2021-23", B067) leave the section or point to Paper A (X-11).

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | B242 | C, yes after correction (four planning-oriented studies) |
| 2 | B238; B137, B130 (failure); B245 (30.8 at 1 in 10); B138, B196 (Jones); B248 (commodity balance); B275 | B238, B245, B248, B275: B, yes. B137, B130: A, yes. B138: B, self-checked. B196: B, unverified (decision 89) |
| 3 | B239; B246; B192 | B239: B, yes after correction (decision 69). B246: B, yes (Q8). B192: A, yes |
| 4 | B240; B171 to B177; B244 | B240: B, yes after correction (decision 69). B175 to B177: A, yes. B171, B174: B, yes. B172, B173: B, self-checked. B244: C, yes with notes (both facts are in Fearnside 1990) |
| 5 | B241; B249; B063, B067; B217; B216; B208, B209 | B241, B063, B216, B217, B208, B209: B, yes. B249, B067: B, yes with notes |
| 6 | B247; B156; B268; B275 | B247: B, yes (reworded by B94). B156: A, yes (reworded by B94). B268, B275: B, yes |
| 7 | B243 (reworded per decision 60) | B, yes with notes (waste 1.33 is covered in the statement's second clause) |
| 8 | none needed | none needed |

**4. Tables and figures.**
* Figure 4 or Table 9, the purpose-to-method matrix: typed in `SECTION7_DRAFT.md`; no csv, no script.
* Table 10, the reporting checklist: typed in the draft; no csv, no script (text table; a csv is optional).

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L042 | Fearnside 1985 | read (B85 page level); self-checked (B85) | failure probability as the security frame; data needs | before 2016 |
| L043 | Fearnside 1990 | read (B85 page level); self-checked (B85) | site scale of the original application; KPROG2 data needs (B244) | before 2016 |
| L017 | Alexander et al. 2016 | read (B85 page level); self-checked (B85) | HALF built for diet comparison; not predictive | 2016 to 2019 |
| L016 | Cassidy et al. 2013 | read (B85 page level); self-checked (B85) | cropland only | before 2016 |
| L006 | Jones committee 1994 | read; unverified | the committee's figures, as summarised in the thesis until read (decision 89) | before 2016 |
| L040 | Peters, Wilkins and Fick 2007 | read; self-checked (B62 full text) | the balance family at state scale | before 2016 |
| L041 | Fairlie 2007 | read; self-checked (B62 full text) | the balance family at country scale | before 2016 |
| L034 | Gutteridge 2005 | read (B85 page level); self-checked (B85) | the balance family at regional scale | before 2016 |
| L229 | House of Representatives Standing Committee on Agriculture 2023 | read (B82 targeted); self-checked (B82) | food security as a planning and policy purpose in Australia (a National Food Plan recommended) | 2020 to 2026 |

Year mix (9 rows): before 2016: 7; 2016 to 2019: 1; 2020 to 2026: 1. The section rests on the paper's own tests; Paper A section 1 carries the Australian food-security policy literature (L148 to L151, L224), and section 7 points to it rather than repeating it.

**6. Gaps.**
1. The matrix and checklist are typed, not generated, against the CARD rule that tables are scripts over files. Job: a csv of ratings, each cell with the claim ids that justify it, and a script.
2. Closed by decision 60: B243 is reworded to the checklist items that moved the answer more than 1.2 times.
3. No precedent is cited for a minimum reporting checklist. Kind of source: a modelling reporting standard (for example the ODD protocol, Grimm and others). Job: acquisition and a register row.
4. Closed: the 2023 inquiry is L229 (B82).

**7. Open decisions.**
* Binding: 5 (outside readers before submission, including a land-use planning colleague for this paper), 31 (the "little meat beats none" line kept for the corrected release only), 33, 60 (B243 wording), 61 and 69 (ratings re-derived blind; "partly" for HALF and Cassidy on purpose 2 and the footprint on purpose 3), 70 (reasons corrected to 103 to 343, since reworded by decision 85), 85 (footprint low end and "about three to eight times"), 89 (Jones report).
* Open: none here; Q8 (section 6) sets the span quoted in purpose 2.

| # | Question | Options | Recommended | Confidence | Reason |
|---|---|---|---|---|---|
| Q6 | Wording of the checklist claim (B243) | Settled by decision 60 | settled (60) | n/a | n/a |
| Q7 | How the 28 ratings are checked before drafting | Settled by decisions 61 and 69: blind re-derivation (V28); its differences taken | settled (61, 69) | n/a | n/a |

**8. Word budget and dependencies.** About **900 words**: four purpose paragraphs of about 150 words, a short reading and the cautions; the matrix and the checklist carry the detail as tables. Dependencies: sections 5 and 6 settled; Q8; the ratings csv; the Jones report (decision 89).

---

## Section 8. Limitations and what no method yet does

**1. Purpose and argument.** The section says what no method reviewed can do, and what the author's own method lacks in the light of the others, in the same terms used for every method. Its four labelled points are variability between years, trade, energy and a fixed diet, plus the constants borrowed from abroad and declared as assumptions. It also says where an implementation could not be checked against its authors' figure and rests on their description alone, and where another method does better for a stated purpose. It is the counterpart of section 7: the guide holds only within these limits.

**2. Content list.**
1. **B8.1 Variability.** Every method but the failure view works in an average year; production shocks are rising and national totals smooth them in a large country; bad wheat years across the southern states are partly correlated (decision 51 wording); Australian wheat "yield potential since 1990" (decision 52 wording; L153 reports a fall in simulated water-limited yield potential, not in actual yields).
2. **B8.2 Trade.** Most methods treat the region as closed or count exports at full value; the footprint and HALF are consumption-based, so imports and exports drop out (B049); trade and reserves together set exposure; self-sufficiency as a continuum; local production meets crop demand for a minority of people (a range across crops, not an uncertainty).
3. **B8.3 Energy.** Simpson's footprint counts fossil energy land (about a sixth, 16%, of the food row, B047) and the model does not; post-farm energy is documented, farm fuel in Australia is not; the farm diesel share is a model statement with the NFF figure as quoted (decision 53).
4. **B8.4 Diet dynamics.** Each method fixes one diet; diets are moving (nutrition transition; meat near a peak in some countries).
5. Borrowed constants and data limits: the US-sourced constants of the thesis model (loss factors, carcase-to-retail) declared as assumptions; what the model cannot carry (`DISCUSSION.md`).
6. Implementations resting on description alone, and the figures not reproduced (plant-food crop and clothing wool in the footprint; New Zealand in HALF).
7. Where another method does better for a stated purpose (HALF for comparisons across countries; for risk, a failure probability, which here is the model's own runs read through Fearnside's frame).

**3. Evidence.** Paper B has no claims-register rows for the section's own statements of limits (gap 2). The points rest on the limits recorded for each test, on the rows below and on `DISCUSSION.md`.

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | B139 (failure view: one criterion, weather as one factor); `cross_method.csv` column "What it leaves out"; register L216 (pp. 132, 135), L217, L218, L153 | B139: C, yes. Register cells single reading; L217 page-read (B78) |
| 2 | B049 (consumption-based footprint); `cross_method.csv` "What it leaves out"; register L165 (p. 4), L175 (pp. 4, 6, 9), L179, L180 | B049: C, yes; register cells single reading |
| 3 | B047 (Simpson's energy land); register L191 (p. 486), L192, L176 | B047: B, yes after correction (about a sixth, 16%) |
| 4 | register L219, L220, L221, L120, L084 | none in claims register; L219, L220 page-read (B78) |
| 5 | `ERRATA.md`; `DISCUSSION.md`; `analysis/constants_audit/` | none in claims register |
| 6 | B035, B261 (not reproduced); B057 (New Zealand); B028, B048, B061, B086 (reconstruction limits) | B035, B057, B261: B, yes (each records not reproduced). B028, B048, B086: C, yes. B061: C, yes after correction |
| 7 | B249; B137; B275 | B249: B, yes with notes. B137: A, yes. B275: B, yes |

**4. Tables and figures.** None required. An optional table of constants declared as assumptions could be built from `analysis/constants_audit/` (scripts exist there for the flags and leverage files); no script makes a paper table.

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L216 | Cottrell et al. 2019 | read (B66f targeted); self-checked (B66f) | B8.1: shocks; national totals smooth shocks in large countries (p. 135) | 2016 to 2019 |
| L217 | Gaupp et al. 2019 | read (B78 page level); self-checked (B78) | B8.1: rising risk of simultaneous breadbasket failure | 2016 to 2019 |
| L218 | Anderson et al. 2019 | read (B67b full); self-checked (B67b) | B8.1: ENSO and IOD tie bad years together (decision 51 wording) | 2016 to 2019 |
| L153 | Hochman et al. 2017 | read (B67a full); self-checked (B67a) | B8.1: "yield potential since 1990", not harvested yield (decision 52) | 2016 to 2019 |
| L042 | Fearnside 1985 | read (B85 page level); self-checked (B85) | B8.1: variability as the failure view handles it | before 2016 |
| L080 | Kastner et al. 2012 | read (B85 targeted); self-checked (B85) | B8.1: Oceania annual variability | before 2016 |
| L165 | Marchand et al. 2016 | read (B73 page level); self-checked (B73) | B8.2: reserves and trade set exposure | 2016 to 2019 |
| L175 | Kummu et al. 2020 | read (B66c targeted); self-checked (B66c) | B8.2: diversity through trade (global pattern only) | 2020 to 2026 |
| L179 | Clapp 2017 | read (B66d targeted); self-checked (B66d) | B8.2: self-sufficiency as a continuum | 2016 to 2019 |
| L180 | Kinnunen et al. 2020 | read (B67a full); self-checked (B67a) | B8.2: local crop production (range across crops, not uncertainty) | 2020 to 2026 |
| L105 | Fader et al. 2013 | read; unverified | B8.2: spatial decoupling of production and consumption | before 2016 |
| L087 | Blomqvist et al. 2013 | read; unverified | B8.2: national footprint read as self-sufficiency | before 2016 |
| L131 | Wiedmann and Lenzen 2018 | read; unverified | B8.2: footprints across borders | 2016 to 2019 |
| L023 | Simpson, Petroeschevsky and Lowe 2000 | read (B85 page level); self-checked (B85) | B8.3: energy land the model does not count | before 2016 |
| L022 | Lenzen and Murray 2001 | read (B85 page level); self-checked (B85) | B8.3: energy in a modified footprint | before 2016 |
| L191 | D'Odorico et al. 2018 | read (B73 page level); self-checked (B73) | B8.3: food-energy-water nexus | 2016 to 2019 |
| L192 | Ladha-Sabur et al. 2019 | read (B67b full); self-checked (B67b) | B8.3: post-farm energy only | 2016 to 2019 |
| L176 | Soliman Hunter and Taylor 2021 | read (B66c targeted); self-checked (B66c) | B8.3: liquid fuel security; NFF 84% quoted as cited there (decision 53) | 2020 to 2026 |
| L060 | Geoscience Australia and ABARE 2010 | read (B85 page level); self-checked (B85) | B8.3: bioenergy (AERA) | before 2016 |
| L219 | Bodirsky et al. 2020 | read (B78 page level); self-checked (B78) | B8.4: the nutrition transition | 2020 to 2026 |
| L220 | Whitton et al. 2021 | read (B78 page level); self-checked (B78) | B8.4: meat consumption near a peak in some countries | 2020 to 2026 |
| L221 | Bentham et al. 2020 | read (B66f targeted); self-checked (B66f) | B8.4: food supply patterns 1961 to 2013 (check against the typeset article) | 2020 to 2026 |
| L120 | Tilman and Clark 2014 | read; self-checked (B50b full text) | B8.4: diet trajectories | before 2016 |
| L084 | Erb et al. 2016 | read; unverified | B8.4: option space under diet change | 2016 to 2019 |
| L142 | Gilland 2006 | read; self-checked (B62 full text) | B8.4: capacity tied to a period and standard | before 2016 |
| L062 | USDA Handbook 697 | read; unverified | B8.5: a US constant in the thesis model | before 2016 (undated; by context) |
| L068 | Buzby 2010 | read; unverified | B8.5: US loss factors | before 2016 |
| L069 | Muth 2011 | read; unverified | B8.5: US loss factors | before 2016 |
| L067 | AUSNUT 2007 | read; unverified | B8.5: nutrient table | before 2016 |

Year mix (29 rows): before 2016: 13; 2016 to 2019: 10; 2020 to 2026: 6.

**6. Gaps.**
1. Narrowed by decision 64: L217, L219 and L220 have page-level reads (B78). Open: L221 is an accepted manuscript to check against the typeset article.
2. No claims-register rows exist for the section's statements about what each method and the model lack. Job: register rows for each limit stated, tied to the README limits and `DISCUSSION.md`.
3. No Australian figure for energy used in farming and food production (B63 found none since 2016). Kind of source: Australian energy statistics by industry (a government data source). Job: register and read; B74's list does not include it.
4. USDA Handbook 697 (L062) has no year in the register, and L062, L068, L069 are unverified with no claim rows. Job: register fix and a one-route read of each constant against its source.

**7. Open decisions.**
* Binding: 33, 51 (Anderson wording on correlated bad years), 52 (Hochman "yield potential since 1990"), 53 (farm diesel share a model statement), 49 and 64 (page-level reads).
* Open: none.

**8. Word budget and dependencies.** About **800 words**: four labelled limits at about 130 words each, constants and unchecked implementations at about 200, and a closing line on where another method does better. Dependencies: the L221 check (gap 1); claims rows (gap 2); sections 5 and 7 settled so the limits match the tests and the guide.

---

## Section 9. Conclusions, data and code availability

**1. Purpose and argument.** The section answers the question set in section 1 in a few sentences: the spread of published estimates is mostly a spread of questions, so the method should follow the purpose, and a capacity figure is only as good as its stated question and the spread across its settings. Every figure quoted for the answer keeps its basis: which tier, which yields, and that the model's range is a spread across judged settings. It gives planners and analysts the two or three things to do with that (choose the method by purpose, report the checklist, distrust a number without its definition). It then states where the data, code, releases and registers are, and the competing-interests statement.

**2. Content list.**
1. The answer: one model on one data set spans the definitional range Q8 sets (by definition alone on the corrected method, with the improved settings named separately), exports stretch it further, and the spread across the settings the author judges defensible (factor 1.26) is small beside the definitions.
2. The equalised-input result: the gap between methods is the method; equalising inputs narrows the spread within the energy balance and people per hectare, the footprint keeps its definitional spread, and the 10% share of inputs depends on the row set (10 to 18%).
3. What to do: method by purpose (section 7); report the checklist.
4. Data and code availability: the archive with its DOI, the frozen releases, the scripts, and the claims and sources registers (decision 6).
5. Competing interests: the model is the author's.

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | B003 or B190 and B193 (Q8); B191, B188, B192, B005; B187, B117 (the judged spread) | B003, B005, B187, B188, B190 to B193: A, yes. B117: B, yes |
| 2 | B277, B276; B264, B267, B268, B273 | B276, B277, B264, B273: A, yes (B276: 10 to 18% by row set). B267, B268: B, yes |
| 3 | B238 to B243 | B238, B241: B, yes. B239, B240: B, yes after correction. B242: C, yes after correction. B243: B, yes with notes |
| 4 | `CITATION.cff`; `results/releases.json`; `LICENSE`, `LICENSE-DATA.md` | none needed |
| 5 | none needed | none needed |

**4. Tables and figures.** None.

**5. Sources to cite.** None from the literature register. The archive is cited by its DOI once minted.

Year mix: no rows.

**6. Gaps.**
1. The archive DOI does not exist: the Zenodo release is on hold until Murray releases it (CARD; HANDOFF). Job: Murray's release, then the DOI in the data statement.

**7. Open decisions.**
* Binding: 6 (registers published with the archive), 8 (releases frozen), 23 (correction notes sent before submission), 55 (journal: Land Use Policy); standing: Zenodo on hold.
* Open: outline "Decisions still open" item 4 (authors and order). Q8 sets point 1's span.

**8. Word budget and dependencies.** About **350 words**: three points of conclusion and a short availability and interests statement. Dependencies: every other section; Q8; the DOI; Land Use Policy's required statements; authors.

---

## Closing part

### Whole-paper table

| Section | Word budget | Sources (register rows) | Year mix (before 2016 / 2016 to 2019 / 2020 to 2026) | Gaps open | Open decisions | Pending jobs |
|---|---|---|---|---|---|---|
| 1. Introduction | 800 | 25 | 13 / 5 / 7 | 4 | 1 (outline item 4) | decision 89 (Jones) |
| 2. Concept and critics | 1,000 | 26 | 17 / 4 / 5 | 2 | 1 (Q2) | none |
| 3. How the review was done | 450 | 7 | 3 / 2 / 2 | 1 | 0 | none |
| 4. Catalogue of methods | 1,800 | 63 | 32 / 20 / 11 | 3 | 0 (Q3 settled, 57) | none |
| 5. Testing the methods | 2,300 | 19 | 16 / 2 / 1 | 5 | 0 (Q4 settled, 58) | B93 (points 3, 6, 12) |
| 6. What moves the number | 1,700 | 42 | 22 / 14 / 6 | 5 | 3 (outline item 2, Q8, Q9; Q5 settled, 59) | decision 89 (Jones) |
| 7. Which method for which purpose | 900 | 9 | 7 / 1 / 1 | 2 | 0 (Q6 settled, 60; Q7 settled, 61 and 69) | decision 89 (Jones) |
| 8. Limitations | 800 | 29 | 13 / 10 / 6 | 4 | 0 | none |
| 9. Conclusions and availability | 350 | 0 | none | 1 | 1 (outline item 4; item 1 settled, 55) | none |
| **Total** | **10,100** | **137 distinct rows** (220 section citations) | **distinct: 64 / 43 / 30** (53% from 2016 on) | **27** | **6 by section; 5 distinct** (outline item 4 counts in sections 1 and 9); 7 questions settled by decisions 55 to 61 and 69 | **B93; decision 89** |

The word budgets are main text only; tables, figure captions, references and the supplement are extra. Land Use Policy's word limit and reference cap are for Murray to check (decision 55); the drafter can trim context-only rows (marked "context" in the tables) first if the journal sets a cap.

### Target journal (outline "Decisions still open" item 1)

Settled by decision 55: Paper B goes to Land Use Policy (word limits to be checked by Murray). The scoping recommendation is kept below for its reasons.

| # | Question | Options | Recommended | Confidence | Reason |
|---|---|---|---|---|---|
| J1 | Target journal for Paper B | Settled by decision 55: (a) Land Use Policy | settled (55) | n/a | (a) is where the 2010 review this paper follows was published (L055), and its readers are the planners the outline names; it has carried Australian capacity-related work (Mcdougall et al. 2020, L183). Check its guide for authors for article types, word limit and reference cap: https://www.sciencedirect.com/journal/land-use-policy/publish/guide-for-authors |

If the guide sets a main-text limit below about 10,000 words, the cut falls first on section 4 (move the family details into Table 2) and section 5 (move fidelity detail into the supplement), not on sections 6 and 7, which carry the paper's argument.

### Register rows touched

None. S01 wrote only `papers/B_methods/SECTION_SCOPE.md`; B92b wrote only this file and `qa/reports/B92b_scope_rewrite.md`. Register edits the rewrite depends on are listed in the B92b report for the next register job.

### Wrong-value check

Wrong-value check: EXAMPLE ONLY, not a finding. Suppose claim B175 (the sum of SA2 capacities is 37% of the national figure, built from `results/scale_curve.csv`) were listed in the section 5 evidence table against point 8 (failure probability). A reader following the id would land on the scale curve, not on `fearnside_failure_curve.csv`, and point 8 would appear to rest on a verified tier A figure it does not use. The check that catches it: each claim id's `output_file` must match the csv named for that point in the Tables and figures list.
