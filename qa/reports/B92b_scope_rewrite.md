# B92b: Paper B section scope rewritten to the logic check (decision 87)

Wrote `papers/B_methods/SECTION_SCOPE.md` (rewritten in place, headings kept) and this report. Read: `qa/reports/V32b_logic_B.md` in full, the cross-paper table of `qa/reports/V32a_logic_A.md`, `qa/DECISIONS.md` rows 55 to 90, `qa/reports/B94_footprint_wording.md`, and both registers as they stand (claims 697 rows, 332 Paper B; literature L001 to L242). Every read status in the scope's source tables is filled by script from the register's `read_or_reported` and `status` fields; every evidence-table status was set by hand from a dump of the register's `tier` and `status`.

**One departure from the brief, stated plainly.** The brief lists B94 (footprint wording) as running. B94's report appeared on disk while this job ran, and the register already carries its reworded statements for B046, B156 and B247 (decision 85). Applying it is not a guess, so the scope uses "146 to 343 million on current yields (103 million at 1990 world yields)" and "about three to eight times", marked "B94". If the coordinator prefers the brief's literal instruction, the five places are section 5 points 4 and 10, section 7 points 5 and 6, and the evidence rows for B046, B156, B247.

## Section table

| Section | Fixes applied (V32b) | Cross-paper items resolved | Items left pending |
|---|---|---|---|
| Header | Basis and jobs paragraph updated; table key reads both register fields; new cross-paper resolutions table (X-1 to X-13) | all 13, listed below | B93 named as running |
| 1. Introduction | "all called carrying capacity" to "offered as how many Australia can feed"; both soft ends declared at first use (9.4 the author's pre-correction figure; 100 the report's "around 100" for 27 + 63); 1986 range third-hand (L036); 1975 CSIRO via two routes (B010, L143), "only through" dropped; Jones figures "as summarised in" the thesis and no "reproduces"; L099 and L106 cited only if fetched or read; B236's chapter 6 qualifier and Fearnside's double listing; B74 rows L226 to L228 replace "pending B74"; statuses refreshed (B006, B010, B161, B236, B229 now verified) | X-2 (PMSEIC), X-9 (cause of scatter), X-10 ("9 to 14" as published method), X-13 (L003, L010, L013 statuses) | Jones report (decision 89; gap 5); Q9 (100 or 90) |
| 2. Concept and critics | Herrington: closest fit CT (7) with BAU2 one count behind; L240 (Rockström 2009) added; L106, L107 "not reached: no file" and cited only if read | none needed | Q2 (outline tag) open |
| 3. How the review was done | Point 4 reworded to the register's own reading labels (read in full, page level, targeted, reported, record only; inherited "read" labels cited as reported or fetched); purpose no longer claims the coverage can be judged before the selection record exists; decision 42 wording noted | none needed | gap 1 (selection record) |
| 4. Catalogue | B4.7 renamed "optimisation models (diet and land use)" (decision 57); foodshed as spatial form; PMSEIC worded per decision 46 (sourced export part on p. 15); Ridoutt 2017 remark dropped (decision 33, B230 not cited); 2,550 kcal in the English original (B122); L042 is the English original; page-read rows (B78) closed gap 3; statuses refreshed (B029, B049, B071, B087, B155 verified; B122, B166 after correction) | X-2 | outline edit (2,500 kcal line) outside this file |
| 5. Testing the methods | Purpose: equalising narrows spread within energy balance and people per hectare, footprint keeps its spread; point 3 "arithmetic reproduces 109 and 96 from printed totals; totals not rebuilt", 134 to 211 a spread across cases, not uncertainty, land carried forward (B027); point 4 builds named for each verdict, 1.718 quoted; point 6 United States excluded, 22 crop items, 190 typed and build 1 only; point 7 meat 1.22%; point 8 "the model read through Fearnside's failure frame"; point 10 "the model's range" and the containment sentence removed; point 11 footprint factor about 2 kept, both lows single-commodity fish, 10 to 18% by row set, "the adjustment the book describes" for p. 78; Q4 settled (58); L050 read from the filed scan (65); gap 2 recast as register edit; gap 3 narrowed to B009, B011 to B013, B031 | X-11 (2011 rows to Paper A) | B93: gap-attribution shares (point 12, B278 to B332, B295, B321), point 3 "within rounding" wording, Cassidy figures (point 6, B081 to B084, B258, B259), crop count 21 or 22 |
| 6. What moves the number | Purpose and point 9: "the spread across the settings the author judges defensible (1.26) is small beside the definitions", 81% from one judged choice, not confidence intervals; point 1: 27 + 63 and "around 100", NFF untraced (drop or cite via L229 p. 24); point 2: 44% of the whole footprint, beef for three countries together; point 3: decision 72 wording, L230, L231, L242 replace L161 and "pending B74", "2018-19" removed; point 5: cliff between 5% and 7.5%; point 6: Jones as summarised, B199 corrected values; point 7: nation, states, SA2 sum (59), two land bases, state yield basis, 54% on local basis (A098, A108); point 9: test stated (B116), L235 to L237 (67); point 10: ladder mixes tiers, B189 mixes data and correction; point 11: full ordering from design_choices.csv (diet with both readings); Q5 settled (59); gaps 1 and 2 closed | X-1 (waste), X-3 (Monte Carlo 13/12 and the test), X-4 (0.528 share of meat), X-5 (little meat, corrected only), X-6 (5% meat and eggs with release), X-7 (ratio convention), X-8 (15.5 million), X-10 (B189) | Q8 (one reading of the definitional span: B003 or factor 4); Q9 (100 or 90); Jones (decision 89) |
| 7. Which method for which purpose | Security recommendation reworded to "a level and a failure probability from the balance run through the failure view, plus a commodity balance for the item that fails first"; FAIL and LDB named as one model (B275); "about three to eight times" (B94); "because none carries the pairing" to "consistent with"; scale shares on the state yield basis; Jones not "reproduced"; checklist per decision 60; Q6 and Q7 settled (60; 61 and 69); L229 replaces the B74 inquiry placeholder; draft's 2011 sentences flagged out | X-5, X-11 (2011 sentences) | Q8 for purpose 2; Jones (decision 89) |
| 8. Limitations | Point 2: footprint and HALF are consumption-based (B049), not closed; point 3: 16% (B047 corrected); point 1: L153 is simulated yield potential; point 7: failure probability is the model's own runs; L217, L219, L220 page-read (B78) | none needed | L221 typeset check |
| 9. Conclusions | Point 1: definitional span per Q8, "spread across defensible settings" for uncertainty; point 2: qualifiers (within-method narrowing, footprint spread, 10 to 18%); journal settled (55) | X-9 | Q8; DOI; authors (outline item 4) |
| Closing part | Whole-paper table recomputed: 137 distinct rows, 220 section citations, distinct year mix 64 / 43 / 30 (53% from 2016 on), 27 open gaps, 6 open decisions by section (5 distinct), 7 questions settled (decisions 55 to 61, 69); new column for pending jobs; J1 settled by decision 55 | n/a | n/a |

## Cross-paper items and how each was resolved

All are written into the scope's header table (X-1 to X-13) and cited from the section points.

1. **Waste (X-1).** Decision 72's wording verbatim; L230 (whole-chain goal, p. 8 printed), L231 (7.3 Mt, 2016-17), L242 (7.6 Mt, 2021 Feasibility Study); L161 dropped as a second-hand route; decision 44 marked replaced.
2. **PMSEIC and Lawrence (X-2).** Decision 46: PMSEIC's 60 million on p. 1 without source and some 40 million abroad on p. 15 (citing DAFF 2009), not added by the report; Lawrence, Richards and Lyons's 22 plus 40 only in Paper A section 8.
3. **Monte Carlo (X-3).** "13 sampled, 12 vary in the 2025 corrected and published releases", with the 2025-improved note (B253); the test of the method stated in section 6 point 9 with B116, so A336's "tested in Paper B" holds.
4. **Red-meat 0.528 (X-4).** Unit "share of meat" in both papers; B251's unit field needs the register edit.
5. **Little meat beats none (X-5).** Corrected release only (118.0 against 112.4; improved release peaks at no meat, 103.6).
6. **5% meat and eggs (X-6).** 103.3 million improved, guideline diet, direct route (B179); 76.8 million corrected, measure applied alone (A258).
7. **Ratio convention (X-7).** People over capacity, above 1 is over, in both papers; factors between capacities are called factors. Paper B's scope contains no people-over-capacity ratio.
8. **15.5 million (X-8).** Paper B: SA2 sum against 41.5 (B176); Paper A: what trade between regions recovers (A274); never bare.
9. **Cause of the scatter (X-9).** Decision 35: "by definition and by method"; within one model about 4 (Q8 sets the reading), between methods the gap is the method.
10. **"9 to 14" (X-10).** Published method (9.4 on 2011 data, 14.1 on 2025 data, as built); corrected 15.35 (A007) and 15.6 (A008); B189's step worded as mixing data and correction.
11. **2011 to 2025 material (X-11).** Paper A alone; the section 7 draft's "7% in 2011" and "fell 28%" leave Paper B or point to Paper A.
12. **National margin (X-12).** Failure probability 5.8 to 6.1% a year, about 1 in 16 to 17 (B130), where a threshold is meant.
13. **Statuses (X-13).** L003, L010, L013 as the register gives them.

## Left pending

* **B93** (decision 88): gap-attribution shares (B278 to B332, including B295, B296, B302, B321) and the "within rounding" wording; Cassidy figures with harvests matched (B081 to B084, B258, B259) and the crop count. Marked "pending B93" in section 5 evidence rows 3, 4, 6, 12 and gaps 1 and 5.
* **Jones report** (decision 89): B196, B197, B138, B245 and L006; until read, quoted "as summarised in" the thesis.
* **Q8** (one reading of the definitional span) and **Q9** (100 or 90) are new questions for Murray in section 6; V32b problems 4 and 5 call for a choice, and Q9 option (b) is a Tier A change (decision 63).
* **Q2** (outline tag) and outline item 4 (authors) stay open.

## Register and outline edits the rewrite depends on (not made; for the next register job)

B156 (delete "the model's range"); B157 (delete the containment sentence); B277 (as-run low is 12, B151); B081 and B083 ("21 crops" against B079's 22, after B93); B251 (unit "share of meat"); B251 and B252 statuses and the improved-release note to match A341 and A342; B216 note (superseded 96.7 and 88.0); B190, B193, B246 or B003 (per Q8); B185, B191, B192 (only if Q9 option b); L050 (`what_taken` to lead with p. 78); L062 (year); B230 (Ridoutt remark, decision 33). Outline: the 2,500 kcal line (B122); the B1-2.a decision tag (Q2); the scale source line ("national, state and NRM rows", decision 59).

## Register rows touched

None.

## Wrong-value check

Wrong-value check: EXAMPLE ONLY, a fix that would itself be wrong, not made. V32b problem 5 suggests restating the export factor on 90 million. A tempting fix would write "exports counted proportionally change the answer by a factor of 2.17" into section 6 point 1, taking 90 / 41.5. That number is not in the register, it changes a Tier A row (B185) without Murray's word (decision 63), and it would replace the report's own stated figure ("approximately 100 million") with the project's sum. The scope instead keeps B185's 2.41 on 100 and puts the choice to Murray as Q9.
