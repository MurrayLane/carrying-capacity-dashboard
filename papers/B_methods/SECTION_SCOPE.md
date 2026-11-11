# Paper B (methods): section-by-section scope

Scoping job S01, 2026-11-11, on Murray's instruction: scope each section, draft nothing. This file holds no paper prose beyond the purpose sentences. Every number it repeats carries a claim id from `qa/claims_register.csv` or a named csv, and is there to show what a point rests on, not as text for the paper.

**Basis.** Read: `papers/B_methods/OUTLINE.md` (labels as placed by B72), `papers/B_methods/SECTION7_DRAFT.md`, `qa/DECISIONS.md` (rows 1 to 54), `qa/CARD.md`, `qa/reports/B61_lit_review_scope.md`, `B63_recency_sweep.md`, `B68_reader_flags.md`, `B70_paperA_thin_points.md`, `B72_outline_numbering.md`, `qa/literature_register.csv` (L001 to L225 as it stands), `qa/claims_register.csv` (277 Paper B rows), `qa/sources_register.csv` (data ids only), the READMEs of `analysis/method_tests_2025/`, `analysis/comparators_2025/`, `analysis/sensitivity_2025/`, `analysis/nutrition_lp_2025/` and `results/`, and `HANDOFF.md`.

**Jobs running while this was written.** B73 (page-level reads, decision 49): its report is on disk and the register already shows three of its Paper B rows as `self-checked (B73)` (L146, L165, L191); they are marked "pages checked by B73, job still running" below. B74 (government documents, decision 50): no rows yet (the register ends at L225), so every place a government document would serve says "pending B74".

**How to read the tables.**
* *Evidence*: tier is the claims register's tier (A headline, B supporting, C context). "Two routes agree" is yes only where the row's status is `independently verified`; otherwise it says self-checked (one route) or unverified. Where no claim row exists, the cell names the register or csv cell the point rests on, or says "none needed".
* *Read status* is the register's `read_or_reported` field. "Read from open copy, no page in register" marks the rows read from B63 open copies whose `what_taken` holds no page.
* *Year band* is by publication year (decision 42). Undated register rows are counted before 2016, as B63 did.
* *Open decisions* lists the settled rows that bind the section and, separately, the questions still open. New questions are numbered Q1 to Q7 across the file.

---

## Section 1. Introduction

**1. Purpose and argument.** The section sets out the puzzle the paper answers: published estimates of how many people Australia can feed run from about 9 to 100 million, and all of them are called carrying capacity. It says why the spread matters to land-use planners and sustainability analysts, who use capacity figures to argue about population, food security and land. It states the question (how much of the spread is the definition, the diet or the method, and which method suits which purpose) and that the paper follows the 2010 review and thesis chapter 6. It discloses at the outset that the model tested beside the others is the author's own, held to the same tests.

**2. Content list.**
1. Four figures that are all called carrying capacity (100, 61, 30 to 35, 9 to 14 million) and the full published span of 9.4 to 100 million.
2. The spread is old: a 1986 committee gave 10 to 480 million, and the 1975 CSIRO work is known only through Henry and Godden (decision 39).
3. At world scale the scatter of capacity estimates is a known feature, and depends on the choices made (Cohen).
4. **B1-2.b Use of capacity in planning.** Why the spread matters: capacity figures enter Australian population debate and planning (Productivity Commission roundtable; a northern Australia settlement study that uses Lane 2017) and city and regional planning abroad. Government population planning documents: pending B74.
5. The question: which method suits which purpose, and how much of the spread is definition, diet or method.
6. What this paper adds to the 2010 review and thesis chapter 6: method families not covered there, a test of each on the same 2025 Australian data, measured design choices, and a guide.
7. Disclosure: the model is the author's (thesis 2014, papers to 2017), one of the methods reviewed, entered as published and as built on, and named again in the competing-interests statement.

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | B005 (9 to 100, factor 10.6); B160 (9.4); B162 (100); B161 (61); B196 (30 to 35); B006 (the four figures named together) | B005, B160, B162: A, yes. B161, B196: B, unverified. B006: C, unverified |
| 2 | B010 (Gifford 82 and 60); `analysis/comparators_2025/harmonisation.csv` rows for the 1986 committee and Gifford; register L036 `what_taken` | B010: B, unverified; csv and register cells are typed from sources (no second route) |
| 3 | register L049 and L106 `what_taken` | none needed (context, read sources) |
| 4 | register L099, L146, L197, L198, L199 `what_taken` | none needed; government framing pending B74 |
| 5 | none needed | none needed |
| 6 | B236 (what the earlier work covered) | C, unverified |
| 7 | B229 (the author's published 40, 9 to 40, 23 million) | B, unverified |

**4. Tables and figures.**
* Table 1, published Australian estimates with their definitions (exports, diet, drought allowance): from `analysis/comparators_2025/harmonisation.csv` and `analysis/method_tests_2025/published_values.csv`. No script makes a paper table from them; `harmonisation.csv` itself is typed from the sources, not generated. A script is needed.

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L006 | Jones committee 1994 | read | 30 to 35 million and 50 plus; the committee figures as published estimates | before 2016 |
| L036 | Migration Committee 1986 | reported | the 10 to 480 million range, cited second-hand through Henry and Godden | before 2016 |
| L002 | Gifford et al. 1975 | reported | the 1975 CSIRO figures, second-hand through Henry and Godden (decision 39) | before 2016 |
| L003 | Henry and Godden 1995 | read | 109 and 96 million; route to Gifford and the Migration Committee | before 2016 |
| L007 | Foran and Poldy 2002 | read | a commodity-balance estimate among the published figures | before 2016 |
| L136 | PMSEIC 2010 | read | 60 million, cited only as "PMSEIC states, without source" (B61 section d) | before 2016 |
| L009 | Bellotti 2017 | read | 61 million, the population plus those fed by exports | 2016 to 2019 |
| L010 | CSIRO and UQ 2025 | read | about 100 million, export-inclusive | 2020 to 2026 |
| L020 | Lane 2014 (thesis) | read | the 9 to 14 million long-term figures; chapter 6 as the earlier review | before 2016 |
| L012 | Lane, Dawes and Grace 2014 | read | the author's published estimates (disclosure) | before 2016 |
| L013 | Lane, Dawes and Grace 2015 | read | the author's published estimates and scale (disclosure) | before 2016 |
| L014 | Lane 2017 | read | short-term and long-term time frames (disclosure) | 2016 to 2019 |
| L055 | Lane 2010 | read | the 2010 methodology review this paper follows | before 2016 |
| L049 | Cohen 1995 | read | world estimates scatter from under 1 to over 1,000 billion | before 2016 |
| L106 | Cohen 2017 | read | about ninety world estimates; capacity depends on choices | 2016 to 2019 |
| L099 | Productivity Commission 2011 | read | capacity in Australian population policy debate | before 2016 |
| L146 | Bolleter 2018 | read (pages checked by B73, job still running) | an Australian planning use of Lane 2017 (northern Australia) | 2016 to 2019 |
| L197 | Świąder et al. 2020 | read (B66e targeted) | footprint-based capacity in European city planning | 2020 to 2026 |
| L198 | Zhang et al. 2018 | read (B66e targeted) | an urban capacity index in Chinese planning (no claim that it builds on Lane 2010; B68) | 2016 to 2019 |
| L199 | Qiu 2024 | read (B66e targeted) | capacity in China's regional functional planning (publication year rule, decision 42) | 2020 to 2026 |
| L073 | Khorsandi et al. 2022 | read | a recent method that cites the thesis and the 2014 paper | 2020 to 2026 |
| pending B74 | Intergenerational Reports; Centre for Population statements | pending B74 | government framing of population planning, 2011 to 2025 | pending B74 |

Year mix (21 rows, B74 rows not counted): before 2016: 12; 2016 to 2019: 5; 2020 to 2026: 4.

**6. Gaps.**
1. Government framing of population planning since 2011 (Intergenerational Reports, Centre for Population): pending B74.
2. A synthesis of how methods spread capacity estimates, beyond Cohen: kind of source, a review such as van den Bergh and Rietveld 2004 (B61 candidate, not acquired). Job: acquisition, optional if Cohen 1995 and 2017 carry the point.
3. Australian planning uses of capacity since 2011 beyond one paper (B63 found only Bolleter 2018): job, a targeted sweep of Australian planning and urban policy journals.
4. How others have taken up the model: about 60 citing works on the OpenAlex list, two read (B61 point B1.5), and the "among the most cited" line for L198 has no count source (B68). Job: a reading pass over the citing list with a named count source.

**7. Open decisions.**
* Binding: 33 (tone), 36 (acquisitions), 39 (Gifford cited second-hand, saying so), 42 (selection rule), 23 (correction notes go out before submission, so the introduction can name corrected figures).
* Open: outline "Decisions still open" item 4 (authors and order), which the competing-interests statement needs.

**8. Word budget and dependencies.** About **800 words**: seven points, most of one or two sentences, with Table 1 carrying the figures; long enough for one paragraph on planning use and one on disclosure. Dependencies: written after sections 5 and 6 so the framing quotes only verified figures; Table 1 script; B74 rows; outline item 4 for the disclosure wording.

---

## Section 2. The concept, its refinements and its critics

**1. Purpose and argument.** The section asks whether carrying capacity is a sound idea for people at all, and why planners still need it. It sets the defenders who extend the concept (cultural capacity below the biological limit; a limit that moves) beside the critics (capacity is social and normative; a static capacity is empty and a variable one begs the question; the idea may validate itself; it depends on choices). It then takes in the debate since 2016 on planetary limits and overshoot in one paragraph (decision 43). Its argument for the rest of the paper is that a capacity figure is usable only with a stated question, standard and time frame, which is what the tests in sections 5 and 6 make explicit. It stays short (decision 37) and points back to thesis chapter 6 and the 2010 review.

**2. Content list.**
1. Where K comes from: range management and shipping to the logistic; the static and the variable reading (Sayre), with the ecological lineage only from Chapman and Byron.
2. Defenders who extend it: cultural capacity below the biological limit, so stay well below the best estimate (Hardin); a limit that itself rises (Meyer and Ausubel; Hopfenberg); capacity tied to a period and a nutrition standard (Gilland).
3. Critics: capacity as social and normative with no single objective level (Seidl and Tisdell); static capacity empirically vacuous, variable capacity question-begging (Sayre); the concept flawed and possibly self-validating (Price); capacity dynamic and choice-dependent, undefined for a trading nation (Cohen).
4. The footprint inversion: capacity turned into the land a population needs, at world-average productivity (Rees 1992, 1996); the open-economy counter-view from Australia (Chisholm); the critique that the footprint protocol lacks an external referent (Giampietro and Saltelli).
5. **B1-2.a Post-2016 debate on human carrying capacity and planetary limits.** Overshoot and limits (Rees 2023; overshoot accounts from Wackernagel 2002; O'Neill and others nation by nation); critics of planetary boundaries (Biermann and Kim, in their words "planetary limits"; Montoya and others); World3 against data, where the closest fit is not business as usual (Herrington); single world figures (Tucker; Cohen 2017).
6. Why planners still need the concept, and the thesis typology (inputs and outputs, scale) that organises section 4; pointer to thesis chapter 6 and the 2010 review.

**3. Evidence.** Paper B has no claims-register rows for section 2; the positions rest on the register's `what_taken` cells as the rows L044 to L049 and L139 to L143 record them (B62 full-text reads) and on L193 to L196 and L210 (B66e, B66f).

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | register L046 `what_taken` (pp. 120, 124, 126, 131); L088 | none needed (concept); single reading |
| 2 | register L044 (pp. 600 to 603), L047 (pp. 210 to 213), L141, L142 (pp. 1 to 2, 8, 11) | none needed |
| 3 | register L045 (pp. 399, 403 to 407), L048 (pp. 9 to 10, 17, 23), L049 (pp. 341 to 343) | none needed; a quoted range (Cohen's under 1 to over 1,000 billion) would need a claim row |
| 4 | register L139 (pp. 125 to 126), L140 (p. 207), L143, L085 | none needed |
| 5 | register L193 (pp. 498, 501 onward), L194, L195, L196, L210 (pp. 622 to 623), L024, L106, L107, L109 | none needed; L106 and L107 have no page in the register |
| 6 | register L020 (chapter 6), L055 | none needed |

**4. Tables and figures.** None.

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L046 | Sayre 2008 | read | the history of K; static capacity empirically vacuous, variable capacity question-begging | before 2016 |
| L088 | Chapman and Byron 2018 | read | the ecological lineage only (it excludes human capacity) | 2016 to 2019 |
| L044 | Hardin 1986 | read | cultural capacity below the biological limit; stay well below the best estimate | before 2016 |
| L047 | Meyer and Ausubel 1999 | read | a limit that itself rises (logistic with varying K) | before 2016 |
| L141 | Hopfenberg 2003 | read | capacity fitted to food availability (moving capacity) | before 2016 |
| L142 | Gilland 2006 | read | capacity tied to a period and a nutrition standard | before 2016 |
| L045 | Seidl and Tisdell 1999 | read | capacity is social and normative, no single objective level | before 2016 |
| L048 | Price 1999 | read | the concept flawed and possibly self-validating | before 2016 |
| L049 | Cohen 1995 | read | capacity is dynamic and choice-dependent; undefined for a trading nation | before 2016 |
| L139 | Rees 1992 | read | capacity inverted into the land a population needs; trade and the unit of analysis | before 2016 |
| L140 | Rees 1996 | read | area-based indicators; world-average productivities | before 2016 |
| L143 | Chisholm 2000 | read | the open-economy counter-view, Australian | before 2016 |
| L024 | Wackernagel et al. 2002 | read | overshoot accounting at world scale | before 2016 |
| L085 | Giampietro and Saltelli 2014 | read | the critique of footprint-based capacity (also section 4) | before 2016 |
| L099 | Productivity Commission 2011 | read | absorption capacity and rate of change in the Australian debate | before 2016 |
| L106 | Cohen 2017 | read | single-number claims and choices | 2016 to 2019 |
| L107 | Tucker 2020 | read | a single long-term world figure, as an example of the claim type | 2020 to 2026 |
| L109 | Wang 2022 | read | land capacity framed for food security (single author; its range is second-hand) | 2020 to 2026 |
| L194 | Rees 2023 | read (B66e targeted) | overshoot: a defender of limits | 2020 to 2026 |
| L195 | O'Neill et al. 2018 | read (B66e targeted) | social thresholds against biophysical boundaries, nation by nation | 2016 to 2019 |
| L193 | Biermann and Kim 2020 | read (B66e targeted) | critiques of planetary boundaries; say "planetary limits" (decision 43) | 2020 to 2026 |
| L196 | Montoya et al. 2018 | read (B66e targeted) | a critique of a biodiversity boundary | 2016 to 2019 |
| L210 | Herrington 2020 | read (B66f targeted) | World3 against data; the closest fit is not business as usual (B68 flag) | 2020 to 2026 |
| L020 | Lane 2014 (thesis) | read | the typology by inputs and outputs and by scale | before 2016 |
| L055 | Lane 2010 | read | pointer to the earlier review of the concept | before 2016 |

Year mix (25 rows): before 2016: 16; 2016 to 2019: 4; 2020 to 2026: 5. The concept's founding works are old by nature (B63 found the same); decision 42 keeps works before 2011 for lineage only, so the drafter can cut points 2 and 3 to the fewest classics that carry them.

**6. Gaps.**
1. The founding planetary boundaries paper is not in the register (Rockström et al. 2009 or Steffen et al. 2015), yet point 5 names the framework. Kind of source: the founding paper. Job: acquisition (Q1).
2. Cohen 2017 (L106) and Tucker 2020 (L107) were read from copies that were not kept and have no page in the register. Job: save the copies and record pages (a B73-style read) if either is quoted.
3. No claim rows exist for section 2. Any figure quoted from a concept source (for example Cohen's range of estimates) needs a claims-register row first. Job: register builder.

**7. Open decisions.**
* Binding: 33, 37 (reading pass, kept short), 42 (lineage only before 2011), 43 (one paragraph, "planetary limits" where the authors say so), and the standing recency rule (CARD). B68 decision 4 is settled by 43.
* Open: Q1 and Q2.

| # | Question | Options | Recommended | Confidence | Reason |
|---|---|---|---|---|---|
| Q1 | Acquire the founding planetary boundaries paper for the decision-43 paragraph | (a) acquire Rockström et al. 2009, "A safe operating space for humanity", Nature 461: 472-475 (QUT search: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,A%20safe%20operating%20space%20for%20humanity&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT ; sign-in form https://go.openathens.net/redirector/qut.edu.au?url=https://doi.org/10.1038/461472a ; DOI https://doi.org/10.1038/461472a) / (b) cite the framework only through Biermann and Kim, who review it | (a) | Medium | A paragraph on planetary limits that cites only a review of the framework will draw a reviewer's comment; one founding paper is a small acquisition. Medium because Biermann and Kim may carry it for a review whose subject is capacity, not boundaries |
| Q2 | The outline tags the B1-2.a bullet "(added 2026-11-11, decision 52)"; row 52 is Paper A's drought wording. The bullet comes from decision 45 (numbering, B72) and its content from decision 43 | (a) correct the tag to decisions 43 and 45 at the next outline edit / (b) leave it | (a) | High | A wrong decision number sends a reader of the outline to the wrong row; the fix is one line in a file the coordinator may edit |

**8. Word budget and dependencies.** About **1,000 words**: six points over about 25 sources, one paragraph for the post-2016 debate (decision 43) and a closing paragraph on why planners still need the concept; decision 37 asks for a short section. Dependencies: Q1; Q2 is housekeeping only. Reading is done (B62, B66e, B66f).

---

## Section 3. How the review was done

**1. Purpose and argument.** The section states the review type and how works were chosen, briefly and transparently. It names the type as a critical review with a narrative synthesis, citing Grant and Booth for the type and Greenhalgh and others for the narrative style (decision 42). It states the selection rule (works from 2011 by publication year, earlier works for lineage only, exclusions named) and where the works came from, so a reader can judge the coverage. It says what the earlier work already covered and is not repeated.

**2. Content list.**
1. **B3.1 Review method (narrative and critical reviews).** The type: a critical review in Grant and Booth's sense, written as a narrative synthesis in Greenhalgh's sense; why that suits a question of method fit.
2. The selection rule (decision 42): publication year from 2011; earlier works for the lineage of a method or concept only; the well-known methods across the main approaches; exclusions named (for example index methods with no food or land basis).
3. Where the works came from: Murray's citation exports and the OpenAlex citing list; the B14 sweep; the B61 scoping; the B63 recency sweep (Crossref, 2016 to 2026); government documents as grey literature (pending B74).
4. How sources were used: content taken only from works read in full; works held second-hand cited as reported (Gifford, decision 39); the reading labels.
5. What thesis chapter 6 and the 2010 review covered, which this paper points to and does not repeat.
6. A pointer to section 5 for the test design (the common data set and the fidelity check).

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | register L223 (Table 1, p. 94), L201 | none needed |
| 2 | `qa/DECISIONS.md` row 42 | none needed |
| 3 | no csv holds the counts (see gap 1) | needs a count before drafting |
| 4 | `qa/literature_register.csv` column `read_or_reported` | none needed |
| 5 | B236 | C, unverified |
| 6 | none needed | none needed |

**4. Tables and figures.** Optionally a small table or flow note of works by route and status (found, read, cited, excluded). No csv and no script exist; see gap 1.

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L223 | Grant and Booth 2009 | read (B66e targeted) | "critical review" as a type (Table 1, p. 94) | before 2016 |
| L201 | Greenhalgh et al. 2018 | read (B66e targeted) | narrative as a style of synthesis; no ranking below systematic reviews | 2016 to 2019 |
| L202 | Sukhera 2022 | read from open copy, no page in register | narrative reviews can be rigorous | 2020 to 2026 |
| L203 | Snyder 2019 | read (B66e targeted) | reasoned, transparent inclusion criteria (p. 337) | 2016 to 2019 |
| L200 | Haddaway et al. 2020 | read (B66e targeted) | state the selection rule and exclusions plainly (pp. 1583 to 1585) | 2020 to 2026 |
| L020 | Lane 2014 (thesis) | read | what chapter 6 already covered | before 2016 |
| L055 | Lane 2010 | read | what the 2010 review already covered | before 2016 |

Year mix (7 rows): before 2016: 3; 2016 to 2019: 2; 2020 to 2026: 2.

**6. Gaps.**
1. The selection record: how many works each route found, how many were read, cited and excluded, and why. No csv holds this. Job: a counting pass over the register, B14, B15, B61, B63 and the B74 output, written to a csv with a script.
2. Sukhera 2022 (L202) has no page in the register. Job: a B73-style page read if it is quoted.

**7. Open decisions.**
* Binding: 42 (rule, citations for the type and style), 36 (acquisitions), 50 (government documents as grey literature). B68 decision 3 is settled by 42.
* Open: none.

**8. Word budget and dependencies.** About **450 words**: six short points; reviewers of a narrative review want the rule and the routes stated, not a protocol. Dependencies: the selection record (gap 1), which needs B74 finished.

---

## Section 4. A catalogue of methods

**1. Purpose and argument.** The section sorts the methods into families, each by the question it answers, its inputs and outputs, and its scale, so a reader can see that the published figures answer different questions before any number is compared. Families new to the author's earlier work are treated in full; the planning-oriented studies of the 2010 review get one line each and a pointer. The catalogue sets up the tests: each family tested in section 5 is described here with what it counts and what it leaves out, stated as what the method can and cannot see (decision 33).

**2. Content list.**
1. Resource-based land and diet (the thesis method; Peters for New York State and the United States; Fairlie for Britain), with its spatial form, the foodshed (Peters 2009; Zumkehr and Campbell; Kurtz).
2. Energy and protein balance (Gifford, second-hand; Henry and Godden), scaled to Nix's land base; Shepon as a gain, not a capacity.
3. Commodity balance (Foran and Poldy) and the nutritional food balance (Ridoutt 2017, an index with no people count).
4. Export-inclusive counts (Bellotti; CSIRO and UQ; PMSEIC stated without source), with the statistics they draw on.
5. Ecological footprint: origin (Rees; Wackernagel 1994), Australian applications (Simpson; Lenzen and Murray), the accounts (Lin; Wackernagel 2019), and the critique and defence (Blomqvist; Giampietro and Saltelli; Goldfinger).
6. Land per diet indices (Alexander's HALF; Kastner; Röös; van Zanten; Schon and Bohringer; Ridoutt 2020) and people per hectare (Cassidy).
7. **B4.8 Integrated resource-flow models.** Stocks and flows (Foran and Poldy), Australian scenario models (Hatfield-Dodds; Bryan 2016), the FABLE Calculator (Navarro Garcia; Jones 2023) and the World3 line (Herrington); Limits to Growth by one line through the 2010 review.
8. **B4.7 Nutrition optimisation.** Diet optimisation at national scale (Chaudhary and Krishna; Gazan; van Dooren), Ridoutt 2021 as a scored, not optimised, comparison, and LUTO as a land-use optimisation model (decision 41); EAT-Lancet as a judged diet, context only.
9. Failure probability (Fearnside 1985 and 1990): failure as the share of settler-years below a standard, capacity read from a density-by-failure curve.
10. **B4.9 Water-bounded capacity.** Land-suitability, water and realistic-yield bounds (Khorsandi 2022 and 2023, catalogue only, decision 26; Fischer; Mesgaran; Rosa 2018; Kummu 2016; Li et al. 2018; Gerten 2020).
11. Index methods in regional assessment (Graymore) and the planning-oriented studies (South East Queensland, Noosa, Douglas Shire), one line each with a pointer to the 2010 review.

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | register L040 (pp. 148 to 152), L015, L041, L077, L103, L104 | none needed (descriptions) |
| 2 | B029 (what the balance counts) | C, unverified |
| 3 | B155 (what the commodity balance asks) | C, unverified |
| 4 | B166 (published export counts are neither energy- nor land-based) | C, unverified |
| 5 | B049 (food-row footprint recipe) | C, unverified |
| 6 | B071 (HALF allocation); B087 (people per hectare allocation) | C, unverified |
| 7 | register L007, L075, L076, L208 to L211 | none needed |
| 8 | register L204 to L207, L208 (p. 217, linear programming), L081 | none needed |
| 9 | B122 (Fearnside's four criteria) | C, unverified |
| 10 | register L073, L074, L029, L212 to L215, L083 | none needed |
| 11 | register L091, L034, L055 | none needed |

**4. Tables and figures.**
* Table 2, the catalogue (family, question answered, inputs, outputs, scale, register ids): no csv and no script. A csv and a script are needed (gap 4).
* Figure 1, the methods mapped by the question each answers: from the same csv; no script.

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L020 | Lane 2014 (thesis) | read | resource-based land and diet: the thesis method | before 2016 |
| L012 | Lane, Dawes and Grace 2014 | read | resource-based land and diet: essential parameters | before 2016 |
| L040 | Peters, Wilkins and Fick 2007 | read | complete-diet land model, New York State | before 2016 |
| L015 | Peters et al. 2016 | read | US agricultural land under ten diets | 2016 to 2019 |
| L041 | Fairlie 2007 | read | UK land budget under six farming regimes (one line, planning-oriented) | before 2016 |
| L034 | Gutteridge 2005 | read | South East Queensland (one line, planning-oriented) | before 2016 |
| L037 | Limits to Growth | not reached | one line, through the 2010 review only (not reached) | before 2016 (undated; by context) |
| L038 | Noosa study | not reached | one line, through the 2010 review only (not reached) | before 2016 (undated; by context) |
| L039 | Douglas Shire study | not reached | one line, through the 2010 review only (not reached) | before 2016 (undated; by context) |
| L077 | Peters et al. 2009 | read | foodshed: spatial land and diet | before 2016 |
| L103 | Zumkehr and Campbell 2015 | read | foodshed: result turns on radius | before 2016 |
| L104 | Kurtz et al. 2020 | read | foodshed: US metropolitan shares | 2020 to 2026 |
| L003 | Henry and Godden 1995 | read | energy and protein balance: the recipe | before 2016 |
| L002 | Gifford et al. 1975 | reported | energy and protein balance: founding work, second-hand (decision 39) | before 2016 |
| L035 | Nix (70 Mha) | reported | the land base the balance scales to, second-hand | before 2016 (undated; by context) |
| L124 | Shepon et al. 2016 | read | energy and protein: a gain from reallocation, not a capacity | 2016 to 2019 |
| L007 | Foran and Poldy 2002 | read | commodity balance; also integrated resource flow (stocks and flows) | before 2016 |
| L079 | Ridoutt et al. 2017 | read | nutritional food balance (an index, no people count) | 2016 to 2019 |
| L105 | Fader et al. 2013 | read | export-inclusive and land-boundary reading | before 2016 |
| L137 | Department of Agriculture 2014 | read | export-inclusive counts: source statistics | before 2016 |
| L139 | Rees 1992 | read | footprint: origin | before 2016 |
| L140 | Rees 1996 | read | footprint: world-average productivities | before 2016 |
| L134 | Wackernagel 1994 | read (B45, two passes on the tables) | footprint: rates (thesis, pp. 279 to 298) | before 2016 |
| L023 | Simpson, Petroeschevsky and Lowe 2000 | read | footprint applied to Australia | before 2016 |
| L022 | Lenzen and Murray 2001 | read | modified footprint for Australia | before 2016 |
| L025 | Lin et al. 2018 | read | National Footprint Accounts method | 2016 to 2019 |
| L129 | Wackernagel et al. 2019 | read | footprint accounts, rationale and use | 2016 to 2019 |
| L085 | Giampietro and Saltelli 2014 | read | footprint: the critique | before 2016 |
| L086 | Goldfinger et al. 2014 | read | footprint: the defence | before 2016 |
| L087 | Blomqvist et al. 2013 | read | footprint: the critique | before 2016 |
| L131 | Wiedmann and Lenzen 2018 | read | footprints in general, context | 2016 to 2019 |
| L017 | Alexander et al. 2016 | read | land per diet: the HALF index | 2016 to 2019 |
| L016 | Cassidy et al. 2013 | read | people nourished per hectare | before 2016 |
| L080 | Kastner et al. 2012 | read | land per diet, global change | before 2016 |
| L114 | Schon and Bohringer 2023 | read | land per diet, German state and regions | 2020 to 2026 |
| L096 | Ridoutt et al. 2020 | read | cropland footprints of Australian diets | 2020 to 2026 |
| L116 | Roos et al. 2017 | read | land per diet, grazing | 2016 to 2019 |
| L117 | van Zanten et al. 2016 | read | land per diet, livestock on leftovers (protein only) | 2016 to 2019 |
| L075 | Hatfield-Dodds et al. 2015 | read | integrated scenario model, Australia (context) | before 2016 |
| L076 | Bryan et al. 2016 | read | integrated land-use scenarios, Australia (no people count) | 2016 to 2019 |
| L209 | Navarro Garcia et al. 2022 | read (B66f targeted) | FABLE Calculator, Australia (no optimisation) | 2020 to 2026 |
| L211 | Jones et al. 2023 | read from open copy, no page in register | the FABLE initiative | 2020 to 2026 |
| L210 | Herrington 2020 | read (B66f targeted) | World3, the Limits to Growth line | 2020 to 2026 |
| L208 | Gao and Bryan 2017 | read (B66f targeted) | LUTO: optimisation family (decision 41) | 2016 to 2019 |
| L204 | Chaudhary and Krishna 2019 | read (B66f targeted) | nutrition optimisation at national scale | 2016 to 2019 |
| L205 | Gazan et al. 2018 | read (B66f targeted) | review of diet optimisation | 2016 to 2019 |
| L207 | van Dooren 2018 | read from open copy, no page in register | linear programming for diets | 2016 to 2019 |
| L206 | Ridoutt et al. 2021 | read (B66f targeted) | Australian diets against planetary limits (scored, not optimised) | 2020 to 2026 |
| L083 | Gerten et al. 2020 | read | land-boundary capacity, global | 2020 to 2026 |
| L081 | Willett et al. 2019 | read | a judged reference diet, not an optimisation (context only) | 2016 to 2019 |
| L042 | Fearnside 1985 | read | failure probability: method detail (Spanish translation on hand) | before 2016 |
| L043 | Fearnside 1990 | read | failure probability: overview and one result | before 2016 |
| L073 | Khorsandi et al. 2022 | read | water-bounded capacity (catalogue only, decision 26) | 2020 to 2026 |
| L074 | Khorsandi et al. 2023 | read | water-bounded meta-model | 2020 to 2026 |
| L029 | Fischer et al. 2002 | read | land suitability (GAEZ) | before 2016 |
| L212 | Mesgaran et al. 2017 | read from open copy, no page in register | land suitability, Iran | 2016 to 2019 |
| L213 | Rosa et al. 2018 | read from open copy, no page in register | water bound on irrigation expansion | 2016 to 2019 |
| L214 | Kummu et al. 2016 | read from open copy, no page in register | water scarcity over the 20th century | 2016 to 2019 |
| L215 | Li et al. 2018 | read (B66f targeted) | water resources carrying capacity methods (cite as Li et al.) | 2016 to 2019 |
| L091 | Graymore et al. 2010 | read | a regional capacity index (pressure index, not food) | before 2016 |
| L010 | CSIRO and UQ 2025 | read | export-inclusive count by proportion | 2020 to 2026 |
| L009 | Bellotti 2017 | read | export-inclusive count | 2016 to 2019 |
| L136 | PMSEIC 2010 | read | export-inclusive figure, stated without source | before 2016 |

Year mix (63 rows): before 2016: 32; 2016 to 2019: 20; 2020 to 2026: 11. Three of the 32 are not reached (L037 to L039) and are cited only through the 2010 review.

**6. Gaps.**
1. Fearnside 1985 is held only as a Spanish translation (L042); the English original is item 9 of the decision-36 acquisitions. Kind of source: the original article. Job: Murray's acquisition under decision 36.
2. No method paper for the stocks-and-flows framework (B61 point B4.8; B63 found none after 2016). Kind of source: a framework paper such as Turner et al. 2011 (B61 candidate). Job: acquisition, or describe the framework from Foran and Poldy 2002 alone and say so.
3. Five catalogue rows were read from open copies with no page in the register (L207, L211, L212, L213, L214). Job: a B73-style page read for the Paper B rows; decision 49 covered only the seven Paper A rows.
4. Table 2 and Figure 1 have no data file. Job: a catalogue csv with a script, each cell traced to a register row.
5. The family descriptions in the claims register are tier C and unverified (B029, B049, B071, B087, B122, B155, B166), and there are none for the foodshed, footprint critique, integrated, optimisation and water-bounded families. Job: register rows and a one-route check of each description against its source page.

**7. Open decisions.**
* Binding: 24 and 26 (Khorsandi in the catalogue, not tested), 39 (Gifford second-hand), 41 (LUTO with optimisation models), 33 (tone), 36 (acquisitions). B68 decision 2 is settled by 41.
* Open: Q3.

| # | Question | Options | Recommended | Confidence | Reason |
|---|---|---|---|---|---|
| Q3 | Family headings in section 4. Decision 41 puts LUTO under "optimisation models" but the outline's B4.7 heading is "nutrition optimisation"; the foodshed literature (B61 point B4.2) has no family in the outline | (a) rename B4.7 "optimisation models (diet and land use)" and treat the foodshed as the spatial form of resource-based land and diet / (b) keep B4.7 for diets only and add a land-use optimisation family and a foodshed family / (c) leave the outline as it is | (a) | Medium | (a) honours decision 41 without adding families, keeps the register label B4.7, and the foodshed studies answer the land-and-diet question on a radius; (b) lengthens the catalogue for two or three works each. Medium because a reviewer from the foodshed field may want it named as a family |

**8. Word budget and dependencies.** About **1,800 words**: eleven families at 120 to 250 words each, the planning studies in one line each, with Table 2 carrying inputs, outputs and scale so the prose can stay short. Dependencies: Q3; the catalogue csv; page reads (gap 3); the Fearnside original if decision 36 delivers it.

---

## Section 5. Testing the methods on common Australian data (the core)

**1. Purpose and argument.** This is the core of the paper: each method is applied to the same 2025 Australian data, wherever its author first used it, and checked against its author's own figure where that can be reached (a fidelity check, not the test). For each method the section states the access the project had (sources and pages), the assumptions made, and whether the authors' figure was reproduced or not reproduced on that basis (decision 33). The author's model is entered the same way, as published and as built on. The result is the methods side by side on one data set, and the harmonised comparison shows that equalising inputs removes the spread within each method but not the gap between methods, so the gap is the method (decision 35).

**2. Content list.**
1. The common data set: one population, data year, land base and consumption basis for every method (2025 only; decision of 2026-11-06).
2. Fidelity check against test: what each is, and how each method is reported (fidelity-checked implementation, or implementation from the published description alone).
3. Energy and protein balance: the recipe reproduces Henry and Godden's own figures; on current data it reads 134 to 211 million; what it hides (land base, exports eaten at home, the consumption factor).
4. Ecological footprint, food row: three builds (decisions 12 and 32); pasture reproduced within 3% at a sourced rate, feed crop reproduced, plant-food crop and clothing wool not reproduced from the published sources; read as a capacity, 103 to 343 million.
5. HALF: reproduced for Australia and the world on 2011 data, not for New Zealand; 2021-23 value and its capacity reading.
6. People per hectare: shares and delivered fraction reproduced within a few points; two builds; 145 to 147 million delivered, about 190 on all cropland.
7. Commodity balance: 1997-98 production and the published balance reproduced; meat, fish and grain readings on current data.
8. Failure probability: applied as a method (no check against Fearnside's Brazilian figure); capacity by return period and today's failure probability.
9. The author's model as an exemplar: as published (thesis method as built), corrected, and improved, each with its Monte Carlo range.
10. The methods side by side: three groups (aggregate methods, binding-commodity and weather methods, the model).
11. The harmonised comparison (decision 35): inputs equalised; the spread among methods does not narrow; the footprint at Australian productivity as the one sanctioned sensitivity (Wackernagel and Rees 1996, p. 78).
12. Gap attribution (decision 34): how much each candidate cause explains of each residual against the authors' figures.

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | B094 (population 27.6); B262 (one land base, 363.5 Mha); B263 (common consumption basis) | B094: B, self-checked. B262, B263: B, yes |
| 2 | none needed (rule: CARD, "Methods paper (B)") | none needed |
| 3 | B015 (fidelity); B016 to B018, B019 (134 to 211); B020, B021; B022, B023, B024, B025; B026 to B028 (limits); authors' figures B008 to B014 | B019: A, yes. B015 to B018, B020, B021, B023, B026: B, yes. B024: B, self-checked. B022, B025, B027: B, unverified. B008 to B014: B, unverified. B028: C, unverified |
| 4 | B033, B034, B260 (reproduced); B035, B261 (not reproduced); B036; B038 to B041, B044, B046 (103 to 343); B042, B043, B045 (consumption and land behind the reading); B256 (second build); B047; B048 (limits); authors' figures B030 to B032; B037 withdrawn | B040, B046: A, yes. B033, B034, B036, B038, B039, B041, B044, B260, B261: B, yes. B043, B045: B, self-checked. B035: not reproduced (status records it). B042, B256, B047, B030 to B032: B, unverified. B048: C, unverified |
| 5 | B058 (fidelity summary); B052 to B057; B059, B060; B062 to B067; B068 (276); B061 (limits) | B058, B068: A, yes. B056, B062, B063: B, yes. B053 to B055, B057, B064 to B066: B, self-checked. B052, B059, B060, B067: B, unverified. B061: C, unverified |
| 6 | B078 (fidelity); B072 to B077, B079, B080, B257; B081, B082, B083 (145 to 147), B084 (190); B085; B258, B259 (second build); B086 (limits) | B078, B083, B084: A, yes. B081: B, yes. B072 to B076, B082: B, self-checked. B077, B079, B085, B257 to B259: B, unverified. B080, B086: C, unverified |
| 7 | B141 (fidelity); B142, B143; B140, B144; B145 to B152; B153 (summary); B154; B222 (register readings) | B153: A, yes. B141, B146, B148, B150, B152: B, yes. B142 to B145, B147, B149, B151: B, self-checked. B140, B154, B222: B, unverified |
| 8 | B137 (41.5 to 18.9); B130 (failure probability today); B131 to B134; B121 (Fearnside's own result, context); B139 (limits); `fearnside_failure_curve.csv` | B130, B137: A, yes. B131 to B134: B, self-checked. B121, B139: C, unverified |
| 9 | B088, B089, B104, B105, B110, B111 (as built); B090, B091, B112, B113 (corrected); B092, B093, B114, B115 (improved) | B090 to B093, B112, B114: A, yes. B088, B089, B110, B111, B113, B115: B, yes. B104, B105: B, self-checked |
| 10 | B156 (three groups); B157; B159; B158; B247 | B156, B159: A, yes. B157, B247: B, yes. B158: B, unverified |
| 11 | B264, B266, B272, B273, B274, B276, B277; B265, B267 to B271; B275 | B264, B266, B272 to B274, B276, B277: A, yes. B265, B267 to B271, B275: B, yes |
| 12 | `analysis/method_tests_2025/gap_attribution.csv` (checked by V25); no claim rows | no claim row; see gap 1 |

The 2011 rows of the model (B123 to B129, B131, B135) exist but belong in Paper A unless Q4 keeps one check column.

**4. Tables and figures.**
* Table 3, each method's reading of Australia on current data: `analysis/method_tests_2025/cross_method.csv`; script `cross_method.py`, table writer `make_readme_tables.py` (exists).
* Table 4, the model's entry by tier with ranges: `analysis/method_tests_2025/model_entry.csv`; script `cross_method.py` (exists); ranges from `results/ranges_2025-*.csv`.
* Table 5, the harmonised comparison: `analysis/method_tests_2025/harmonised_comparison.csv`; script `harmonised_comparison.py` (exists).
* Supplementary table, fidelity checks and gap attribution: `published_values.csv`, `second_build_values.csv`, `simpson_food.csv`, `half_index.csv`, `cassidy.csv`, `foran_poldy_balance.csv`, `henry_godden_summary.csv`, `gap_attribution.csv`; scripts exist for each output; no script assembles the supplementary table.
* Figure 2, the same data through each method: `cross_method.csv` and `harmonised_comparison.csv`; no plotting script.

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L003 | Henry and Godden 1995 | read | the energy and protein recipe and Table 5 (fidelity check) | before 2016 |
| L035 | Nix (70 Mha) | reported | the land base of the recipe, second-hand | before 2016 (undated; by context) |
| L023 | Simpson, Petroeschevsky and Lowe 2000 | read | the food row and recipe (fidelity check) | before 2016 |
| L134 | Wackernagel 1994 | read (B45, two passes on the tables) | pasture and wool rates for the third build (decision 32) | before 2016 |
| L050 | Wackernagel and Rees 1996 | not reached | p. 78, the one sanctioned sensitivity (decision 35); register row still "not reached" | before 2016 |
| L051 | ABS 4306.0 (1991-92 data) | read | 1991-92 consumption for the footprint fidelity check | before 2016 (undated; by context) |
| L052 | ABS 7503.0 (1990-91 data) | read | 1990-91 unit values for the energy balance check | before 2016 (undated; by context) |
| L053 | ABARE 2010 | read | commodity statistics for the energy balance check | before 2016 |
| L017 | Alexander et al. 2016 | read | HALF recipe and supplement (fidelity check) | 2016 to 2019 |
| L016 | Cassidy et al. 2013 | read | people per hectare recipe (fidelity check) | before 2016 |
| L007 | Foran and Poldy 2002 | read | Table 2.5 requirements and 1997-98 production (fidelity check) | before 2016 |
| L042 | Fearnside 1985 | read | failure-probability recipe | before 2016 |
| L043 | Fearnside 1990 | read | the one published result, context only | before 2016 |
| L030 | FAO, IIASA and UNFPA 1982 | reported | the comparison figure in Fearnside 1990, second-hand | before 2016 |
| L006 | Jones committee 1994 | read | 30 to 35 million matched at the 1-in-10 point | before 2016 |
| L020 | Lane 2014 (thesis) | read | the thesis method as published | before 2016 |
| L014 | Lane 2017 | read | short-term and long-term settings | 2016 to 2019 |
| L083 | Gerten et al. 2020 | read | a comparator for a range (register use) | 2020 to 2026 |
| L105 | Fader et al. 2013 | read | a comparator for a range (register use) | before 2016 |

Data sources are in `qa/sources_register.csv`, not the literature register: FAOSTAT food balances, production and land use (D17 to D19) and the test extracts (D22 to D28), and the model's 2025 data (D47 to D49). They are cited in the data statement and the table notes.

Year mix (19 rows): before 2016: 16; 2016 to 2019: 2; 2020 to 2026: 1. The section cites the methods' own papers and their input statistics, which are old by nature; recent works enter in sections 4, 6 and 8.

**6. Gaps.**
1. Gap attribution (decision 34) has a checked output (V25) but no claims-register rows, so its shares cannot be quoted. Job: register rows for each residual and share used.
2. Wackernagel and Rees 1996 (L050) is still "not reached" in the register, yet decision 35 and B270 rest on its p. 78. Job: record the reading of p. 78 in the register row.
3. The authors' own figures used for the fidelity checks are mostly tier B and unverified (B008 to B014, B030 to B032, B059, B077, B140). Job: a one-route recheck of each against the page it is read from.
4. Figure 2 has no plotting script. Job: a script over `cross_method.csv` and `harmonised_comparison.csv`.

**7. Open decisions.**
* Binding: 8 (frozen releases), 12 (Simpson and Cassidy as ranges), 27 (Monte Carlo rerun), 32 (third Simpson build), 33 (tone), 34 (gap attribution), 35 (harmonised comparison; figures quoted only after V26, which is done), 39 (Gifford second-hand); the 2026-11-06 decisions (no reproduction gate; 2025 data only; the model as one exemplar).
* Open: Q4.

| # | Question | Options | Recommended | Confidence | Reason |
|---|---|---|---|---|---|
| Q4 | The outline allows at most one 2011 column in one table, as a check that method differences are not an artefact of the data. Keep it? | (a) no 2011 column: the harmonised comparison (B276, B277) is the check / (b) one 2011 column for the model's corrected row (B123) beside the methods' 2011 fidelity figures | (a) | Medium | The harmonised comparison tests the same worry directly (equalising inputs leaves the spread among methods), and leaving 2011 out keeps the line between the papers clean. Medium because a reviewer may still ask whether the 2025 data drive the gap, and (b) answers that in one column |

**8. Word budget and dependencies.** About **2,300 words**, the largest section: seven tests at about 220 words each (access, assumptions, fidelity result, reading on current data), about 250 for the common data and the fidelity rule, and about 500 for the side-by-side and the harmonised comparison. The numbers sit in Tables 3 to 5 and the supplementary table, so the prose carries access, assumptions and verdicts. Dependencies: gap attribution rows (gap 1); the L050 row (gap 2); Q4; Figure 2 script.

---

## Section 6. What moves the number

**1. Purpose and argument.** The section measures, with the model on the same data, what each design choice does to the answer: exports, diet, waste, a drought allowance, the land base, the unit of self-sufficiency, the yield basis, the time frame and uncertainty. It shows that the model's own uncertainty is small beside the definitions, and reads the published spread along a ladder of definitions without calling it a decomposition. Three choices are where the model's Australian settings enter (grazing and pasture-fed food, waste, the land base), each introduced by what the other methods show; the paper says the comparison shows where each choice matters, not that it produced the improvements (outline caution). Uncertainty is treated as a design dimension through the Monte Carlo.

**2. Content list.**
1. Exports counted or not: the published export-inclusive counts and an energy count of exports, against the model.
2. **Grazing and pasture-fed meat and dairy** (the yield basis): how each method treats it, and the model's Australian setting (beef output by state, dairy on land that can carry it, the organic ruminant factor).
3. **How waste is treated**: production counted as eaten, waste inside the diet, US loss factors; the model's Australian loss factors and the recycling credit; the 6% setting described as halving the retail-and-consumer share, every tonnage with its year (decision 44).
4. **Which land counts** (the land base): Nix's 70 Mha, New York State's three land classes, doubled cropland, suitability; the model's reserve rule.
5. Diet: guideline diets by meat share and the nutrition-optimised diets; capacity is not monotone in meat share on the improved release (decision 31); EAT-Lancet supports diet as a lever for emissions, not for cropland.
6. The drought allowance: the failure-probability view as a design choice.
7. **The unit of self-sufficiency** (scale), shown with three points (Q5); the full curve is Paper A's.
8. The time frame: short-term and long-term settings.
9. **How sure the answer is, as a method**: the Monte Carlo (13 sampled choices, 12 varying in 2025, 1,000 draws), the drivers of its width, the five range ends that are the author's judgement.
10. The model's own uncertainty against the definitions, and the ladder: where the published spread sits, read as a reading, not a decomposition.
11. Land matters least, then waste and the Australian settings; diet and weather most.

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | B162, B185, B186, B191; B161, B163, B164, B165, B166 | B162, B185, B186, B191, B165: A, yes. B164: B, yes. B161, B163: B, unverified. B166: C, unverified |
| 2 | B050 (44%), B051 (8.1 of 13.6), B070, B231, B233; B069; B183 (corrected to improved); B234 | B183: A, yes. B050, B051, B069: B, unverified. B070, B231, B233, B234: C, unverified |
| 3 | B168, B169 (waste factors); B108 (no avoidable waste); decision 44 wording; `analysis/waste_2025/README.md`; register L161 (p. 229), L163 (pp. 118 to 119), L160 (p. 162) | B108, B168, B169: A, yes. Waste source rows: single reading |
| 4 | B170 (land 1.09); B106, B107, B109; B200, B225; B232 | B170: A, yes. B106, B107, B200: B, self-checked. B109, B225: B, unverified. B232: C, unverified |
| 5 | B178, B179, B180, B181, B182; B205 to B216; B201; B202 to B204, B228; B218 | B178 to B182: A, yes. B205 to B216: B, yes. B201, B218, B228: B, self-checked. B202 to B204: B, unverified |
| 6 | B167 (2.19); B095 to B103; B196 to B199, B226 | B167: A, yes. B095, B097 to B103, B198, B226: B, self-checked. B096: A, yes. B196, B197, B199: B, unverified |
| 7 | B171 to B177 | B175 to B177: A, yes. B171 to B174: B, self-checked |
| 8 | B184 (2.66); B160 | A, yes |
| 9 | B187; B116; B117 to B120; B250 to B253; `results/ranges_2025-*.csv` | B187: A, yes. B117 to B120, B250 to B253: B, self-checked. B116: C, unverified |
| 10 | B188, B189, B190, B192, B193, B195; B005 | A, yes |
| 11 | B194 | A, yes |

**4. Tables and figures.**
* Table 6, the design choices and their factors: `analysis/method_tests_2025/design_choices.csv`; script `design_choices.py` (exists).
* Figure 3, the effect of each design choice, with the ladder: `design_choices.csv` and `ladder.csv`; table script exists (`make_readme_tables.py`), no plotting script.
* Table 7, diets on the improved release: `analysis/comparators_2025/diet_land.csv` (`diet_land.py`, exists) and `analysis/nutrition_lp_2025/variants.csv` (`optimise.py`, `run_variants.sh`, exist).
* Table 8, the Monte Carlo ranges and variance shares: `results/ranges_2025-mirror.csv`, `ranges_2025-fixed.csv`, `ranges_2025-improved.csv`; scripts `monte_carlo.mjs`, `summarise_mc.py`, `rss_check.py` (exist).
* Scale, three points: `results/scale_curve.csv`; `analysis/scale_curve_2025/plot_scale_curve.py` draws Paper A's full curve; no script for the three-point table.

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L023 | Simpson, Petroeschevsky and Lowe 2000 | read | pasture is 44% of the footprint | before 2016 |
| L022 | Lenzen and Murray 2001 | read | footprint mostly pasture (8.1 of 13.6 ha) | before 2016 |
| L017 | Alexander et al. 2016 | read | beef drives HALF; grassland intensities, global averages | 2016 to 2019 |
| L040 | Peters, Wilkins and Fick 2007 | read | land base: 2.03 Mha in three classes; diet moves capacity threefold | before 2016 |
| L015 | Peters et al. 2016 | read | US diets turn on grazing land | 2016 to 2019 |
| L016 | Cassidy et al. 2013 | read | grazing left out; production counted as eaten | before 2016 |
| L003 | Henry and Godden 1995 | read | land base rests on Nix; production counted as eaten | before 2016 |
| L035 | Nix (70 Mha) | reported | the 70 Mha of intensive land, second-hand | before 2016 (undated; by context) |
| L002 | Gifford et al. 1975 | reported | cropland doubled, second-hand (decision 39) | before 2016 |
| L029 | Fischer et al. 2002 | read | land base resting on suitability | before 2016 |
| L042 | Fearnside 1985 | read | the failure-probability view of the drought allowance | before 2016 |
| L068 | Buzby 2010 | read | US loss factors used by the thesis model | before 2016 |
| L069 | Muth 2011 | read | US loss factors used by the thesis model | before 2016 |
| L160 | Reutter et al. 2017 | read (B66b targeted) | caution: household waste totals differ about 3.4 times by method | 2016 to 2019 |
| L161 | Mirosa et al. 2020 | read (B66b targeted) | the 7.3 Mt 2016-17 baseline, named with its year (decision 44) | 2020 to 2026 |
| L163 | Spang et al. 2019 | read (B66b targeted) | SDG 12.3 scope: the 6% halves the retail and consumer share (decision 44) | 2016 to 2019 |
| L081 | Willett et al. 2019 | read | diet change alone moves global cropland 0 to 2% (p. 472) | 2016 to 2019 |
| L080 | Kastner et al. 2012 | read | diet as a lever on land | before 2016 |
| L120 | Tilman and Clark 2014 | read | diet as a lever (context, base year named) | before 2016 |
| L115 | Poore and Nemecek 2018 | read | grass on land unsuited to crops | 2016 to 2019 |
| L116 | Roos et al. 2017 | read | grazing and land per diet | 2016 to 2019 |
| L117 | van Zanten et al. 2016 | read | livestock on leftovers (protein only) | 2016 to 2019 |
| L096 | Ridoutt et al. 2020 | read | Australian diet choices and cropland | 2020 to 2026 |
| L084 | Erb et al. 2016 | read | reporting a range of options | 2016 to 2019 |
| L106 | Cohen 2017 | read | reporting a range, not a single number | 2016 to 2019 |
| L009 | Bellotti 2017 | read | exports counted: 61 million | 2016 to 2019 |
| L010 | CSIRO and UQ 2025 | read | exports counted: proportional count, 100 million | 2020 to 2026 |
| L011 | National Farmers' Federation | reported | exports counted: "feeds 75 million" (reported) | before 2016 (undated; by context) |
| L006 | Jones committee 1994 | read | the two figures matched to the model's average year and 1-in-10 point | before 2016 |
| L007 | Foran and Poldy 2002 | read | the meat-limited count | before 2016 |
| L041 | Fairlie 2007 | read | unit of self-sufficiency: a country | before 2016 |
| L034 | Gutteridge 2005 | read | unit of self-sufficiency: a region | before 2016 |
| L073 | Khorsandi et al. 2022 | read | capacity falls as the unit shrinks | 2020 to 2026 |
| L074 | Khorsandi et al. 2023 | read | scale in a meta-model | 2020 to 2026 |
| L077 | Peters et al. 2009 | read | scale: foodshed | before 2016 |
| L014 | Lane 2017 | read | the time frame as a design choice | 2016 to 2019 |
| pending B74 | National Food Waste Strategy (2017) and National Food Waste Baseline (2019) | pending B74 | the waste baseline and target named with their years (decision 44) | pending B74 |

Year mix (36 rows, B74 rows not counted): before 2016: 19; 2016 to 2019: 12; 2020 to 2026: 5. Lawrence, Richards and Lyons 2013 (L224) is not cited here: decision 46 places its 22 plus 40 million in Paper A section 8 only (settles B68 decision 7 for this paper).

**6. Gaps.**
1. No method source for the Monte Carlo is in the register: Latin hypercube sampling and variance shares. Kind of source: the standard method papers or a sensitivity-analysis text (for example McKay, Beckman and Conover 1979; Saltelli and others). Job: acquisition and a register row.
2. The waste baseline and target documents: pending B74. The 2018-19 feasibility study is in the sources register (D39) but not the literature register.
3. The Australian loss factors rest on data sources (D40: a bin audit and FAO's regional loss shares) that have no literature-register row to cite in the text. Job: register rows for the cited loss-factor sources.
4. Figure 3 and the three-point scale table have no script. Job: two small scripts over `design_choices.csv`, `ladder.csv` and `results/scale_curve.csv`.
5. Several statements the section leans on are unverified (B050, B051, B069, B109, B202 to B204, B225, and the C rows B070, B231 to B234). Job: a one-route check of each against its source page or output file.

**7. Open decisions.**
* Binding: 27 (Monte Carlo rerun), 30 and 31 (diets re-optimised; diet route; "a little meat beats none" kept for the corrected release only), 33, 35, 44 (waste wording), 46 (Lawrence only in Paper A), 54 (thirteen choices wording kept in rerun scripts). Standing: scale as a design choice with three points (CARD).
* Open: outline "Decisions still open" item 2 (where the rest of the model material goes; the improvements as settings in section 6 are proposed and await Murray), and Q5.

| # | Question | Options | Recommended | Confidence | Reason |
|---|---|---|---|---|---|
| Q5 | Which three points show scale. The CARD and the outline say three points, and the outline's source line names the national, state and NRM rows; the design-choice factor (B177, nation against the SA2 sum) and SECTION7_DRAFT also use SA2 | (a) nation, states, SA2 sum / (b) nation, states, NRM regions / (c) all six levels in the table row text, three in the figure | (a) | Medium | (a) is the only set that matches the tier A factor already in the design-choice table and the matrix text, and SA2 is the extreme the reader needs; (b) matches the outline's source line but leaves B175 to B177 without a point in the text. Medium because NRM regions are the planning unit some readers know best |

**8. Word budget and dependencies.** About **1,700 words**: eleven points; the three settings paragraphs (grazing, waste, land base) at about 200 words each because each must say what the other methods assume; the Monte Carlo at about 250; the ladder and the reading at about 250; the factors themselves sit in Table 6 and Figure 3. Dependencies: Q5; outline item 2; B74 waste documents; the Monte Carlo method citation; Figure 3 script.

---

## Section 7. Which method for which purpose

**1. Purpose and argument.** The section turns the tests into a guide: a matrix of four purposes against seven methods, a recommendation per purpose, and a minimum reporting checklist. The purposes run in order of how strongly the paper's evidence supports them (food security and drought risk; why national estimates range from 9 to 100 million; regional and local land-use planning; diet change and land use). Its argument is that no single method serves every purpose, that the aggregate methods answer a different question, and that a security claim needs two methods reported together. The draft (`SECTION7_DRAFT.md`) holds the matrix, ratings and checklist for Murray's edits; the ratings are the author's judgement and are labelled so.

**2. Content list.**
1. The rating key and the seven methods.
2. Purpose 1, food security and drought risk: failure probability and the land-and-diet balance suited; commodity balance partly; aggregate methods not suited.
3. Purpose 2, why estimates range from 9 to 100 million: the balance suited; four methods partly, each reproducing one family of published estimates.
4. Purpose 3, regional and local planning: only the balance carries a unit of land, a diet and the pasture-crop pairing; scale decides the answer.
5. Purpose 4, diet change and land use: HALF for comparison across countries; the balance for what Australia's land can feed.
6. The short reading: no single method serves all purposes; aggregate methods read two to eight times the balance; use two methods for a security claim.
7. The minimum reporting checklist (twelve items: seven design choices from section 6 and five things a reader needs).
8. Cautions: a figure of people fed is not a target; the ratings may differ where grazing is a small share of food land; the ratings are the author's judgement on seven methods.

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | B242 | C, unverified |
| 2 | B238; B137, B130 (failure); B245 (Jones at 1 in 10); B248 (commodity balance) | B238: B, unverified. B137, B130: A, yes. B245, B248: B, self-checked |
| 3 | B239; B246; B192 | B239: B, unverified. B246: B, self-checked. B192: A, yes |
| 4 | B240; B171 to B177; B244 | B240: B, unverified. B175 to B177: A, yes. B171 to B174: B, self-checked. B244: C, unverified |
| 5 | B241; B249; B063, B067; B217; B216 | B241, B249, B067: B, unverified. B063, B216, B217: B, yes |
| 6 | B247; B156 | B247: B, yes. B156: A, yes |
| 7 | B243 (conflicts with B170, see Q6) | B, unverified |
| 8 | none needed | none needed |

**4. Tables and figures.**
* Figure 4 or Table 9, the purpose-to-method matrix: typed in `SECTION7_DRAFT.md`; no csv, no script.
* Table 10, the reporting checklist: typed in the draft; no csv, no script (text table; a csv is optional).

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L042 | Fearnside 1985 | read | failure probability as the security method; data needs | before 2016 |
| L043 | Fearnside 1990 | read | site scale of the original application | before 2016 |
| L017 | Alexander et al. 2016 | read | HALF built for diet comparison; not predictive | 2016 to 2019 |
| L016 | Cassidy et al. 2013 | read | cropland only | before 2016 |
| L006 | Jones committee 1994 | read | the 1-in-10 point as the committee's figure | before 2016 |
| L040 | Peters, Wilkins and Fick 2007 | read | the balance family at state scale | before 2016 |
| L041 | Fairlie 2007 | read | the balance family at country scale | before 2016 |
| L034 | Gutteridge 2005 | read | the balance family at regional scale | before 2016 |
| pending B74 | 2023 parliamentary inquiry into food security | pending B74 | food security as a planning and policy purpose in Australia | pending B74 |

Year mix (8 rows, B74 rows not counted): before 2016: 7; 2016 to 2019: 1; 2020 to 2026: 0. The section rests on the paper's own tests; Paper A section 1 carries the Australian food-security policy literature (L148 to L151, L224), and section 7 points to it rather than repeating it.

**6. Gaps.**
1. The matrix and checklist are typed, not generated, against the CARD rule that tables are scripts over files. Job: a csv of ratings, each cell with the claim ids that justify it, and a script.
2. B243 says each checklist item is a design choice that moved the answer by more than 1.2 times; the land base moved it 1.09 times (B170) and the draft itself says items 1 and 9 to 12 are not design choices. Job: rewording (Q6).
3. No precedent is cited for a minimum reporting checklist. Kind of source: a modelling reporting standard (for example the ODD protocol, Grimm and others). Job: acquisition and a register row.
4. Food security as an Australian planning purpose: pending B74 (the 2023 inquiry).

**7. Open decisions.**
* Binding: 5 (outside readers before submission, including a land-use planning colleague for this paper), 31 (the "little meat beats none" line kept for the corrected release only, already reflected in the draft), 33.
* Open: Q6 and Q7.

| # | Question | Options | Recommended | Confidence | Reason |
|---|---|---|---|---|---|
| Q6 | Wording of the checklist claim (B243) | (a) "items 2 to 8 are the design choices measured in section 6; items 1 and 9 to 12 are what a reader needs to use the number", with no threshold / (b) keep "more than 1.2 times" and drop the land base from the checklist | (a) | High | The draft's own heading already says (a); the land base belongs in the checklist even though it moves the answer least, because readers argue about it most |
| Q7 | How the 28 ratings are checked before drafting | (a) a blind checker re-derives each rating from the method-test README and the claim rows, without seeing the draft's ratings, and differences come to Murray / (b) Murray edits the draft directly / (c) both | (c) | Medium | The ratings are judgement, so a blind re-derivation is the only test that can fail; Murray's edits set the direction (decision 5's outside reader comes after). Medium because a second judgement may disagree for reasons of taste, not evidence |

**8. Word budget and dependencies.** About **900 words**: four purpose paragraphs of about 150 words, a short reading and the cautions; the matrix and the checklist carry the detail as tables. Dependencies: sections 5 and 6 settled; Q6 and Q7; the ratings csv; B74 for the inquiry.

---

## Section 8. Limitations and what no method yet does

**1. Purpose and argument.** The section says what no method reviewed can do, and what the author's own method lacks in the light of the others, in the same terms used for every method. Its four labelled points are variability between years, trade, energy and a fixed diet, plus the constants borrowed from abroad and declared as assumptions. It also says where an implementation could not be checked against its authors' figure and rests on their description alone, and where another method does better for a stated purpose. It is the counterpart of section 7: the guide holds only within these limits.

**2. Content list.**
1. **B8.1 Variability.** Every method but the failure view works in an average year; production shocks are rising and national totals smooth them in a large country; bad wheat years across the southern states are partly correlated (decision 51 wording); Australian wheat "yield potential since 1990" (decision 52 wording).
2. **B8.2 Trade.** Every method treats the region as closed or counts exports at full value; trade and reserves together set exposure; self-sufficiency as a continuum; local production meets crop demand for a minority of people (a range across crops, not an uncertainty).
3. **B8.3 Energy.** Simpson's footprint counts fossil energy land and the model does not; post-farm energy is documented, farm fuel in Australia is not; the farm diesel share is a model statement with the NFF figure as quoted (decision 53).
4. **B8.4 Diet dynamics.** Each method fixes one diet; diets are moving (nutrition transition; meat near a peak in some countries).
5. Borrowed constants and data limits: the US-sourced constants of the thesis model (loss factors, carcase-to-retail) declared as assumptions; what the model cannot carry (`DISCUSSION.md`).
6. Implementations resting on description alone, and the figures not reproduced (plant-food crop and clothing wool in the footprint; New Zealand in HALF).
7. Where another method does better for a stated purpose (HALF for comparisons across countries; failure probability for risk).

**3. Evidence.** Paper B has no claims-register rows for section 8. The points rest on the limits recorded for each test and on `DISCUSSION.md`.

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | B139 (failure view: one criterion, weather as one factor); `cross_method.csv` column "What it leaves out"; register L216 (pp. 132, 135), L218, L153 | B139: C, unverified; register cells single reading |
| 2 | `cross_method.csv` "What it leaves out"; register L165 (p. 4), L175 (pp. 4, 6, 9), L179, L180 | none in claims register |
| 3 | B047 (Simpson's energy land); register L191 (p. 486), L192, L176 | B047: B, unverified |
| 4 | register L219, L220, L221, L120, L084 | none in claims register |
| 5 | `ERRATA.md`; `DISCUSSION.md`; `analysis/constants_audit/` | none in claims register |
| 6 | B035, B261 (not reproduced); B057 (New Zealand); B028, B048, B061, B086 (reconstruction limits) | B035: not reproduced. B261: B, yes. B057: B, self-checked. B028, B048, B061, B086: C, unverified |
| 7 | B249; B137 | B249: B, unverified. B137: A, yes |

**4. Tables and figures.** None required. An optional table of constants declared as assumptions could be built from `analysis/constants_audit/` (scripts exist there for the flags and leverage files); no script makes a paper table.

**5. Sources to cite.**

| Register id | Author Year | Read status | Cited for | Year band |
|---|---|---|---|---|
| L216 | Cottrell et al. 2019 | read (B66f targeted) | B8.1: shocks; national totals smooth shocks in large countries (p. 135) | 2016 to 2019 |
| L217 | Gaupp et al. 2019 | read from open copy, no page in register | B8.1: rising risk of simultaneous breadbasket failure | 2016 to 2019 |
| L218 | Anderson et al. 2019 | read (B67b full) | B8.1: ENSO and IOD tie bad years together (decision 51 wording) | 2016 to 2019 |
| L153 | Hochman et al. 2017 | read (B67a full) | B8.1: "yield potential since 1990", not harvested yield (decision 52) | 2016 to 2019 |
| L042 | Fearnside 1985 | read | B8.1: variability as the failure view handles it | before 2016 |
| L080 | Kastner et al. 2012 | read | B8.1: Oceania annual variability | before 2016 |
| L165 | Marchand et al. 2016 | read (pages checked by B73, job still running) | B8.2: reserves and trade set exposure | 2016 to 2019 |
| L175 | Kummu et al. 2020 | read (B66c targeted) | B8.2: diversity through trade (global pattern only) | 2020 to 2026 |
| L179 | Clapp 2017 | read (B66d targeted) | B8.2: self-sufficiency as a continuum | 2016 to 2019 |
| L180 | Kinnunen et al. 2020 | read (B67a full) | B8.2: local crop production (range across crops, not uncertainty) | 2020 to 2026 |
| L105 | Fader et al. 2013 | read | B8.2: spatial decoupling of production and consumption | before 2016 |
| L087 | Blomqvist et al. 2013 | read | B8.2: national footprint read as self-sufficiency | before 2016 |
| L131 | Wiedmann and Lenzen 2018 | read | B8.2: footprints across borders | 2016 to 2019 |
| L023 | Simpson, Petroeschevsky and Lowe 2000 | read | B8.3: energy land the model does not count | before 2016 |
| L022 | Lenzen and Murray 2001 | read | B8.3: energy in a modified footprint | before 2016 |
| L191 | D'Odorico et al. 2018 | read (pages checked by B73, job still running) | B8.3: food-energy-water nexus | 2016 to 2019 |
| L192 | Ladha-Sabur et al. 2019 | read (B67b full) | B8.3: post-farm energy only | 2016 to 2019 |
| L176 | Soliman Hunter and Taylor 2021 | read (B66c targeted) | B8.3: liquid fuel security; NFF 84% quoted as cited there (decision 53) | 2020 to 2026 |
| L060 | Geoscience Australia and ABARE 2010 | read | B8.3: bioenergy (AERA) | before 2016 |
| L219 | Bodirsky et al. 2020 | read from open copy, no page in register | B8.4: the nutrition transition | 2020 to 2026 |
| L220 | Whitton et al. 2021 | read from open copy, no page in register | B8.4: meat consumption near a peak in some countries | 2020 to 2026 |
| L221 | Bentham et al. 2020 | read (B66f targeted) | B8.4: food supply patterns 1961 to 2013 (check against the typeset article) | 2020 to 2026 |
| L120 | Tilman and Clark 2014 | read | B8.4: diet trajectories | before 2016 |
| L084 | Erb et al. 2016 | read | B8.4: option space under diet change | 2016 to 2019 |
| L142 | Gilland 2006 | read | B8.4: capacity tied to a period and standard | before 2016 |
| L062 | USDA Handbook 697 | read | B8.5: a US constant in the thesis model | before 2016 (undated; by context) |
| L068 | Buzby 2010 | read | B8.5: US loss factors | before 2016 |
| L069 | Muth 2011 | read | B8.5: US loss factors | before 2016 |
| L067 | AUSNUT 2007 | read | B8.5: nutrient table | before 2016 |

Year mix (29 rows): before 2016: 13 (one undated, L062); 2016 to 2019: 10; 2020 to 2026: 6.

**6. Gaps.**
1. Three section 8 rows were read from open copies with no page in the register (L217, L219, L220), and L221 is an accepted manuscript to check against the typeset article. Job: a B73-style page read for the Paper B rows.
2. No claims-register rows exist for the section's statements about what each method and the model lack. Job: register rows for each limit stated, tied to the README limits and `DISCUSSION.md`.
3. No Australian figure for energy used in farming and food production (B63 found none since 2016). Kind of source: Australian energy statistics by industry (a government data source). Job: register and read; B74's list does not include it.
4. USDA Handbook 697 (L062) has no year in the register. Job: register fix.

**7. Open decisions.**
* Binding: 33, 51 (Anderson wording on correlated bad years), 52 (Hochman "yield potential since 1990"), 53 (farm diesel share a model statement), 49 (page-level reads, Paper A rows only).
* Open: none.

**8. Word budget and dependencies.** About **800 words**: four labelled limits at about 130 words each, constants and unchecked implementations at about 200, and a closing line on where another method does better. Dependencies: page reads (gap 1); claims rows (gap 2); sections 5 and 7 settled so the limits match the tests and the guide.

---

## Section 9. Conclusions, data and code availability

**1. Purpose and argument.** The section answers the question set in section 1 in a few sentences: the spread of published estimates is mostly a spread of questions, so the method should follow the purpose, and a capacity figure is only as good as its stated question and uncertainty. It gives planners and analysts the two or three things to do with that (choose the method by purpose, report the checklist, distrust a number without its definition). It then states where the data, code, releases and registers are, and the competing-interests statement.

**2. Content list.**
1. The answer: one model on one data set spans a factor of 4 by definition alone, exports stretch it further, and the model's own uncertainty is small beside the definitions.
2. The equalised-input result: the gap between methods is the method.
3. What to do: method by purpose (section 7); report the checklist.
4. Data and code availability: the archive with its DOI, the frozen releases, the scripts, and the claims and sources registers (decision 6).
5. Competing interests: the model is the author's.

**3. Evidence.**

| Point | Claim id or csv cell | Tier; two routes agree |
|---|---|---|
| 1 | B193, B190, B191, B188, B192, B005 | A, yes |
| 2 | B277, B276 | A, yes |
| 3 | B238 to B243 | B and C, unverified |
| 4 | `CITATION.cff`; `results/releases.json`; `LICENSE`, `LICENSE-DATA.md` | none needed |
| 5 | none needed | none needed |

**4. Tables and figures.** None.

**5. Sources to cite.** None from the literature register. The archive is cited by its DOI once minted.

Year mix: no rows.

**6. Gaps.**
1. The archive DOI does not exist: the Zenodo release is on hold until Murray releases it (CARD; HANDOFF). Job: Murray's release, then the DOI in the data statement.

**7. Open decisions.**
* Binding: 6 (registers published with the archive), 8 (releases frozen), 23 (correction notes sent before submission); standing: Zenodo on hold; journal and authors decided by Murray.
* Open: outline "Decisions still open" item 1 (journal; see the closing part) and item 4 (authors and order).

**8. Word budget and dependencies.** About **350 words**: three points of conclusion and a short availability and interests statement. Dependencies: every other section; the DOI; the journal (its required statements); authors.

---

## Closing part

### Whole-paper table

| Section | Word budget | Sources (register rows) | Year mix (before 2016 / 2016 to 2019 / 2020 to 2026) | Gaps | Open decisions |
|---|---|---|---|---|---|
| 1. Introduction | 800 | 21 (+ pending B74) | 12 / 5 / 4 | 4 | 1 (outline item 4) |
| 2. Concept and critics | 1,000 | 25 | 16 / 4 / 5 | 3 | 2 (Q1, Q2) |
| 3. How the review was done | 450 | 7 | 3 / 2 / 2 | 2 | 0 |
| 4. Catalogue of methods | 1,800 | 63 | 32 / 20 / 11 | 5 | 1 (Q3) |
| 5. Testing the methods | 2,300 | 19 | 16 / 2 / 1 | 4 | 1 (Q4) |
| 6. What moves the number | 1,700 | 36 (+ pending B74) | 19 / 12 / 5 | 5 | 2 (outline item 2, Q5) |
| 7. Which method for which purpose | 900 | 8 (+ pending B74) | 7 / 1 / 0 | 4 | 2 (Q6, Q7) |
| 8. Limitations | 800 | 29 | 13 / 10 / 6 | 4 | 0 |
| 9. Conclusions and availability | 350 | 0 | none | 1 | 2 (outline items 1 and 4) |
| **Total** | **10,100** | **127 distinct rows** (208 section citations) | **distinct: 60 / 41 / 26** (53% from 2016 on) | **32** | **11 by section; 10 distinct** (outline item 4 counts in sections 1 and 9) |

The word budgets are main text only; tables, figure captions, references and the supplement are extra. About 127 distinct references is within the usual range for a review of this kind, and sections 4 and 6 hold most of them; the drafter can trim context-only rows (marked "context" in the tables) first if the journal sets a cap.

### Target journal (outline "Decisions still open" item 1)

The CARD reserves the journal to Murray; this is a recommendation only. The three suggested journals were weighed on the outline's readers (land-use planners and sustainability analysts), on where the paper's own lineage sits, and on the decision-33 tone.

| # | Question | Options | Recommended | Confidence | Reason |
|---|---|---|---|---|---|
| J1 | Target journal for Paper B | (a) Land Use Policy / (b) Environmental Science and Policy / (c) Ecological Indicators | (a) Land Use Policy, with (b) as the second choice | Medium | (a) is where the 2010 review this paper follows was published (L055), and its readers are the planners the outline names; it has carried Australian capacity-related work (Mcdougall et al. 2020, L183). (b) suits the policy readers and has carried Australian food-waste and city capacity work (Reutter 2017, L160; Świąder 2020, L197). (c) is the home of the footprint debate (L085, L086, L125, L127), which would pull the paper toward a method critique, against decision 33. Medium because this job had no network and did not check each journal's article types, word limit or reference cap; check Land Use Policy's guide for authors before deciding: https://www.sciencedirect.com/journal/land-use-policy/publish/guide-for-authors |

If the guide sets a main-text limit below about 10,000 words, the cut falls first on section 4 (move the family details into Table 2) and section 5 (move fidelity detail into the supplement), not on sections 6 and 7, which carry the paper's argument.

### Register rows touched

None. This job wrote only `papers/B_methods/SECTION_SCOPE.md`.

### Wrong-value check

Wrong-value check: EXAMPLE ONLY, not a finding. Suppose claim B175 (the sum of SA2 capacities is 37% of the national figure, built from `results/scale_curve.csv`) were listed in the section 5 evidence table against point 8 (failure probability). A reader following the id would land on the scale curve, not on `fearnside_failure_curve.csv`, and point 8 would appear to rest on a verified tier A figure it does not use. The check that catches it: each claim id's `output_file` must match the csv named for that point in the Tables and figures list.
