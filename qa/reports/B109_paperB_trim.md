# B109: Paper B back under 8,000 words by the fixed counter (decision 92)

Brief: `qa/briefs/B109_paperB_trim.md`. Files written: `papers/B_methods/draft/B_s01-03.md`, `B_s04-05.md`, `B_s06-09.md`, their three `_claims.csv` files, `supplementary.md`, `supplementary_claims.csv`, and this report. Nothing else was written: `references.md` was not regenerated (a copy of the reference tool was run to a scratch file to check it, see section 5), and no register row was touched. No number was changed.

## 1. Word counts (`python3 qa/tools/wordcount.py B`, the only counter used)

| Section | Scope budget | 70% floor | Before | After | Change |
|---|---|---|---|---|---|
| 1 | 800 | 560 | 978 | 968 | -10 |
| 2 | 1,000 | 700 | 795 | 788 | -7 |
| 3 | 450 | 315 | 340 | 340 | 0 |
| 4 | 1,800 | 1,260 | 1,371 | 1,297 | -74 |
| 5 | 2,300 | 1,610 | 1,874 | 1,682 | -192 |
| 6 | 1,700 | 1,190 | 1,506 | 1,458 | -48 |
| 7 | 900 | 630 | 469 | 469 | 0 |
| 8 | 800 | 560 | 625 | 623 | -2 |
| 9 | 350 | 245 | 332 | 324 | -8 |
| **Total** | 10,100 | 7,070 | **8,290** | **7,949** | **-341** |

Counter output before: `1 978, 2 795, 3 340, 4 1371, 5 1874, 6 1506, 7 469, 8 625, 9 332, TOTAL 8290`. After: `1 968, 2 788, 3 340, 4 1297, 5 1682, 6 1458, 7 469, 8 623, 9 324, TOTAL 7949`.

The target (at most 7,950) is met with one word to spare. Every section I edited stays at or above its 70% floor. **Section 7 was already below its floor before this job (469 against 630) and was not touched**; it cannot be brought up by cutting, so it is a point for Murray (section 6 below). Section 1 is still 168 words over its budget of 800: every sentence left there is required by the scope's content list, a flagged value, a Jones committee sentence or decision 93's wording.

The supplement's prose rose from 1,944 to 2,143 words (by a plain count of its prose lines, not the paper counter, which does not read the supplement).

## 2. Sentences moved or cut (one line each)

Order of the brief: (1) repeats, (2) section 5 detail to S3, (3) section 4 detail to S2, (4) tightening.

**(1) Repeats cut**
* 4 opening: "The planning-oriented studies of the earlier review (Lane 2010) get one line each." Cut; 4.11 gives them one line each, and Lane 2010 stays cited in sections 1 and 4.11.
* 4.1: clause ", with land in three classes" cut from the Peters, Wilkins and Fick 2007 sentence; 6.4 carries the three classes (2.03 Mha, p. 148).
* 5.4 Test: "The readings are high chiefly because all of Australia's pasture, most of it rangeland, counts at world-average productivity, with no pairing of pasture-fed food with crops." Cut; 4.5 states what the footprint sees, and 5.11 (local-productivity adjustment) and 7.6 carry the pairing reading. No number.
* 5.9: "On 2025 data the corrected tier, the baseline entry, reads 41.5 million in the short term (36.3 to 45.8) and 15.6 million in the long term (13.4 to 16.5)." Cut; Table 4 (same section) carries every value with its row label "the baseline entry", 6.8 states the 15.6 and 6.9 the 36.3 to 45.8 (citing Table 4).
* 5.12: "Simpson's pasture residual of 2.3% would be closed by a dairy share of about 57% of milk, but the paper prints no share." Cut; S3.7 already carries the same statement with the 2.3% and 57% and its claims rows.
* 6.2: clause "; on the improved release the default diet used 5.93 ha of pasture and 0.3 ha of cropland a person" cut; Table S2 row 1 (section S4) carries both values, and 6.5 points to Table S2.
* 6.2: clause ", counting the land Australia actually uses," cut from the Lenzen and Murray sentence; 4.5 and section 2 say what their modified footprint counts.
* 6.10: ", a factor of 1.26," cut from "The spread across defensible settings ... is small beside these definitions"; 6.9, the sentence group just before, states 1.26 (and 9.2 keeps it, as section 9's content list requires).

**(2) Section 5 implementation detail moved to S3** (whole sentences, or a sentence split at a clause and the clause moved as its own sentence)
* 5.1: "with the model's 2025 data taken as the same vintage" moved to the new lead paragraph of S3 (sentence 1: "For the common data set of section 5.1, the model's 2025 data were taken as the same vintage as FAOSTAT's data for 2021 to 2023.").
* 5.1: "which equals the model's ABS holdings to within 0.01 Mha" moved to S3, sentence 2 ("The land base of 363.5 Mha equals the model's ABS holdings to within 0.01 Mha.").
* 5.1: "which rests on FAO's head count of 26.20 million, not the model's population" moved to S3, sentence 3.
* 5.4 Access: "the rebuild also drew on ABS 4306.0 for consumption in 1991-92, Wackernagel and Rees 1996, and the rates in Wackernagel 1994" moved to the start of S3.2 ("Besides Simpson, Petroeschevsky and Lowe 2000, the rebuild drew on ..."). The main text keeps the source, its figures and page.
* 5.5 Access: "the rebuild used FAOSTAT's food balance series that starts in 2010, not the authors' download" moved to the start of S3.3.
* 5.5 Fidelity: "A second, independent build agrees within 2%" moved to the end of S3.3; the main sentence keeps "Table 3 gives the other countries."
* 5.6 Fidelity: "A second, independent build agrees within 5% for Australia and 8% for the world on delivered calories." moved to S3.4 (after the crop-count sentence). The main text keeps "two builds" through 5.6's "145 million in the second build" and Table 3.
* 5.12: "Australia's residual of 0.8% is partly explained by the supplement's cropland adjustment (42%) and is not closed by any cause tested." moved to S3.7, worded "Australia's HALF residual of 0.8% is partly explained by the cropland adjustment in the authors' supplement (42%) ..." so that "supplement" is not read as this paper's. Section 5.12 keeps the method sentence, the HALF revisions sentence and the pointer to Table S1 and S3.7.

**(3) Section 4 family detail moved to S2**
* 4.6: "Livestock are charged for their feed and ruminants take all pasture" cut from the HALF sentence; S2.6 already says livestock are charged for their feed, and "Ruminants take all pasture." is added there. The main text keeps "the authors state that the index is not predictive (Alexander et al. 2016, p. 89)".
* 4.6: Cassidy's recipe detail ("with feed calories returned as meat, eggs and dairy at fixed efficiencies, exports following the average use of the importing countries") moved to S2.6 as "Feed calories return as meat, eggs and dairy at fixed efficiencies, and exports follow the average use of the importing countries (Cassidy et al. 2013, p. 4)." The main sentence keeps people per hectare of cropland and the 2,700 kcal a day (p. 4); Table 3 carries the same recipe in its "What it counts" cell.
* 4.10: "Yields and weather are drawn from fitted distributions over runs of years at fixed densities." moved to the start of S2.10 as "In Fearnside's simulation (Fearnside 1985), yields and weather are drawn ...".

**(4) Tightened, meaning unchanged**
* 1: "Each was offered as a count of how many people Australia can feed." to "Each was offered as such a count."
* 1: "27 million fed at home and another 63 million fed abroad" to "27 million fed at home and 63 million abroad".
* 1: "extrapolated from the share of production that is exported" to "extrapolated from the exported share of production".
* 2: "a sound idea when applied to people" to "a sound idea for people".
* 2: "a stated question, a stated standard of living and diet, and a stated time frame" to "a stated question, standard of living and diet, and time frame".
* 2: "That point bears directly on Australia" to "That bears directly on Australia".
* 4 opening: "before section 5 compares any number" to "before section 5 compares numbers"; "Table 2 carries inputs, outputs and scale, and supplementary section S2 gives the fuller account of each family" to "Table 2 carries inputs, outputs and scale; supplementary section S2 gives the fuller account".
* 4.3: "for each commodity, item by item" to "for each commodity".
* 4.4: "and assume that exports would be eaten" to "and assume exports would be eaten".
* 6.1: "CSIRO and the University of Queensland (section 4.4)" to "CSIRO and UQ (section 4.4)" (the abbreviation the section already uses); "and the energy count by a factor of 4.4 to 6.4" to "and the energy count by 4.4 to 6.4".
* 6.2: "from 41.5 million on the corrected method to 53.6 million on the improved method" to "from 41.5 million (corrected method) to 53.6 million (improved)".
* 6.4: "moved the model's answer" to "moved the answer".
* 6.5: "on the improved release: there was a dip at 2.5% meat and eggs, and a cliff between" to "on the improved release, with a dip at 2.5% meat and eggs and a cliff between" (dip and cliff wording kept, decision 31).
* 6.6: "for the worst year in 100 they fed 19 to 25 million" to "for the worst year in 100, 19 to 25 million".
* 6.7: "Three points from the model show" to "Three points show".
* 6.9: "Australia's short-term capacity" to "short-term capacity".
* 8.3: "no Australian figure for the energy used in farming" to "no Australian figure for farm energy use".
* 9.3: "The implication for practice is to choose the method by purpose" to "Choose the method by purpose"; "Distrust a capacity figure given without its definition." to "Distrust one given without its definition." (the sentence before ends "with every capacity figure").

**Left alone on purpose:** every [gate 4] and [open] flagged value; the Jones committee sentences in 1, 5.8 and 6.6 (B100), although 6.6 repeats section 1; the van den Bergh and Rietveld and Wackernagel et al. 1999 sentences (B108); decision 33, 42, 46, 57, 58, 59, 69, 72, 85 and 93 wordings (in particular 5.10 and 7.6's "134 to 343 ... about three to eight times", 6.3's waste paragraph, section 1's relationship to the 2010 review, section 2's footprint lineage from B101); every "as reported in" and "not seen" label; the access and assumption statements of section 5 (decision 33), apart from the secondary sources and series named above; section 7 in full.

## 3. Claims rows

Row counts: `B_s01-03_claims.csv` 89 data rows (unchanged), `B_s04-05_claims.csv` 195 to 179, `B_s06-09_claims.csv` 132 to 131, `supplementary_claims.csv` 187 to 200. Line endings were kept as they were, line by line (the supplement csv's new rows use its CRLF).

**Moved to `supplementary_claims.csv`** (each new row's `moved_from` reads "B_s04-05, section 5, sentence n (B109)"):
* 5,2 "model's 2025 data" (B094, release 2025-fixed) to S3,1, fragment "the model's 2025 data were taken as the same vintage".
* 5,3 "within 0.01 Mha" (B262) to S3,2.
* 5,4 "26.20 million" (`harmonised_comparison.csv` summary note) to S3,3.
* 5,13 "ABS 4306.0" (publication number; L051) and "1991-92" (B048; B032; L051) to S3,13.
* 5,21 "starts in 2010" (B061) to S3,22.
* 5,24 "within 2%" (B058) to S3,26.
* 5,32 "within 5% for Australia and 8% for the world" (B258) to S3,31.
* 5,66 "0.8%" (B056) and "the supplement's cropland adjustment (42%)" (B278; L017) to S3,44, fragment reworded to the new text.

**New supplement rows (copies, no new number):** S3,1 "FAOSTAT's data for 2021 to 2023" (B263); S3,2 "The land base of 363.5 Mha" (B262); S2,25 "(Cassidy et al. 2013, p. 4)" (page as printed, L016; the page also stays in section 4).

**Deleted, the value staying in a row where it remains in the text:**
* 4,5 "with land in three classes" (L040; 6.4's row 6,23 keeps it).
* 5,47 "2025 data", "41.5 million in the short term (36.3 to 45.8)", "15.6 million in the long term (13.4 to 16.5)" (B090; B112; B091; B113): Table 4 row 3 keeps them.
* 5,67 "residual of 2.3%" (B260) and "a dairy share of about 57% of milk" (B325): S3,45 already holds both; its "(copy; also in main text)" note now says the main-text copy was cut by B109.
* 6,12 "5.93 ha of pasture and 0.3 ha of cropland" (B069; B205): Table S2 row 1 keeps them.

**Fragments updated to the tightened text:** 1,6; 6,6 (now "the energy count by 4.4 to 6.4"); 6,13; 6,25; 6,35; 6,56 (now "The spread across defensible settings is small beside these definitions", claim B188, with a note that 1.26 is stated in sentence 50, B187).

**Renumbered:** section 4 rows from sentence 3 down by 1, and from 54 down by 2; section 5 rows 21 to 31 down by 1, 33 to 46 down by 2 (44a to 42a, and its "as sentence 44" to "as sentence 42"), 48 to 65 down by 3, 68 on down by 5; supplement S3 rows renumbered for the three-sentence lead paragraph and the inserted sentences (old 1 to 9 up 3, 10 to 17 up 4, 18 to 20 up 5, 21 to 24 up 6, 25 to 35 up 7, 36 to 43, 37 to 45); S2 row 33 to 35.

## 4. Drafter notes

A short "B109 trim" note was added at the end of each section file's drafter notes, pointing here. The counter stops at the drafter-notes heading, so these add nothing to the count.

## 5. Checks

* Counter: 8,290 before, 7,949 after (section 1 of this report).
* Numbers: a script listed every number in the prose of the three section files and the supplement and looked for it in the four claims csvs. Before and after, the only misses are the same three parsing artefacts (a page in a page list followed by a comma: "199," in section 2, "380," in 4.5, "697," for USDA Handbook 697 in 8.5). Every fragment of every claims row was also checked to occur in its file: the mismatches after (12, 2, 3 and 80 descriptive table-row fragments) are identical to those before.
* Sentence numbers: section 4 and 5 rows were checked against a sentence split of the edited text; every row lands on the sentence that holds its fragment (with the split's constant offsets for the italic labels).
* References: a copy of `qa/tools/make_references.py` was run with its output sent to a scratch file. It gives 130 entries, no id without a register row, and a reference list identical to the current `references.md`: every work cited before is still cited in the main text or the supplement (ABS 4306.0 now in S3.2 and Table S1a, Lane 2010 in sections 1 and 4.11).
* Cross-references: every "section n.n", "section Sn.n", "Table n" and "Figure n" in the prose resolves to an existing heading, table or figure placeholder; no section or table was renumbered.
* No em or en dashes in any file written. No time words added.

## 6. Points for Murray and the coordinator

1. **Section 7 is below its 70% floor** (469 against 630) before and after this job. Cutting cannot fix it; restoring material (for example the 7.2 to 7.5 figures B98b and B101 cut as repeats) or lowering the section's budget is a decision.
2. **Section 1 is 168 words over its budget** of 800 although every sentence in it is required; the total is under 8,000 because sections 2, 3, 7, 8 and 9 sit under theirs.
3. The margin is one word (7,949 against 7,950). Any later addition needs a matching cut.
4. Found, not changed: the Jones row in 5.8 carries sentence number 42a (was 44a) though the Jones sentence follows sentence 43 in the text; and section 1 labels Khorsandi et al. 2022 "not seen; cited from its abstract" while 4.9 describes the 2022 paper without that label and gives it only to the 2023 paper. Both are for a register or claims job.

## 7. Wrong-value check

Wrong-value check: EXAMPLE ONLY, not a cut that was made. In 6.10, "the published estimates, which run from 9.4 million to 100 million, a factor of 10.6 (section 1)" looks like a plain repeat of section 1 and cutting it would save 11 words. It would break the brief three ways: the row (6,57) carries the [open: Q9] flag, so the value cannot be cut; the scope's section 6 content list (point 10) requires the ladder to be read against the published span; and Figure 3's placeholder says its steps multiply to the 10.6, which the text would then no longer state. The check that catches it: the flag column of `B_s06-09_claims.csv` for the sentence, read before any cut.
