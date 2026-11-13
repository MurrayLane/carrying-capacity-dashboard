# B98b: Paper B cut to under 8,000 words, with an abstract (decision 92)

Brief: `qa/briefs/B98b_cut_paper_B.md`. Files written: `papers/B_methods/draft/B_s01-03.md`, `B_s04-05.md`, `B_s06-09.md`, their three `_claims.csv` files, `supplementary.md`, `supplementary_claims.csv`, and this report. `paper_B_draft1.md` was not touched. No register rows were touched.

## 1. Word counts (prose only)

Counting rule: prose only, as V34b states it. Headings, table rows, table captions, figure and table placeholders, drafter notes and the abstract are left out. Table notes are left out of the main count and reported separately, because V34b's section 5 count appears to include them. The counter splits on white space, and it ran 1 to 7 words per section below the B96b counter on the uncut draft.

| Section | Scope budget | 70% floor | Before | After | After as share of budget |
|---|---|---|---|---|---|
| 1 | 800 | 560 | 882 | 689 | 86% |
| 2 | 1,000 | 700 | 891 | 737 | 74% |
| 3 | 450 | 315 | 451 | 356 | 79% |
| 4 | 1,800 | 1,260 | 1,988 | 1,291 | 72% |
| 5 | 2,300 | 1,610 | 2,358 | 1,769 | 77% |
| 6 | 1,700 | 1,190 | 1,866 | 1,397 | 82% |
| 7 | 900 | 630 | 986 | 653 | 73% |
| 8 | 800 | 560 | 900 | 651 | 81% |
| 9 | 350 | 245 | 324 | 298 | 85% |
| **Total** | 10,100 | 7,070 | **10,646** | **7,841** | 78% |

Table notes (Tables 3 and 5): 122 words before, 102 after. With them the total is **7,943**, still under 8,000. Every section is above its 70% floor. Sections 4 (31 words over the floor) and 7 (23 over) have the least margin, so later edits should not cut those two further.

**Abstract: 208 words** (allowed range 150 to 250). It sits under "## Abstract" at the top of `B_s01-03.md`. Every figure in it (about 9 to 100 million; factor 10.6; 2025 and FAOSTAT 2021-23; seven methods; 134 to 343 million; about three to eight times; 12 to 343 million; 18.9 to 55.3 million; 1.26) is in the main text, and each has a row in `B_s01-03_claims.csv` (section "abstract"), with the [gate 4], [open: Q8] and [open: Q9] flags of the rows it draws on.

Supplement: 2,001 words of prose, plus Tables S1, S1a, S2, S3 and S4.

## 2. What moved to the supplement

| Block (main-text origin) | Goes to | Words |
|---|---|---|
| Section 2: second-tier positions in fuller form (Sayre's rangeland history and the Australia and Africa critiques, p. 126; ecology's many senses; Meyer and Ausubel's growing capacity; Hopfenberg in full; Gilland's nutrition standard; Rees 1996's definition; Giampietro and Saltelli's "narrative" consequence; Biermann and Kim's three fields). The main text keeps one sentence for each critic. | S1 | 156 |
| Section 4: family detail beyond one paragraph each (foodshed studies, Peters 2007 and 2016 detail, Gifford's inquiry and Nix's 70 Mha, Shepon in full, Ridoutt 2017, Fader, the footprint's national accounts, critique and defence (Blomqvist as reported, Giampietro and Saltelli, Goldfinger, Wiedmann and Lenzen), HALF recipe detail, Kastner, Röös, van Zanten, Schön and Böhringer, Ridoutt 2020 and 2021, EAT-Lancet, FABLE detail, Rosa, Kummu 2016, Li, Gerten's 10.2 billion as reported, Fearnside 1990 overview). Each family keeps one paragraph in the main text, and Table 2 carries inputs, outputs and scale. | S2.1 to S2.10 | 754 |
| Section 5: per-method implementation detail. Fidelity-check arithmetic for Henry and Godden (totals, factors, land-base cases, 31%, 15.6 and 8.8 MJ, 243 million); the Simpson three-build detail (build definitions, 1.737, 2.385, 0.098, 0.094, 0.074 to 0.142); HALF's 66 of 90 commodities, the animal-fat rule, US, Argentina and India; Cassidy's 61% against 59%, the US feed share, 1,061 against 947 Mha, the harvest-matching detail and the 0.766 factor; Foran and Poldy tonnages; Fearnside's 0.24 persons a hectare; the 1.5% and 2% failure probabilities; Simpson gap shares (149%, 175%). | S3.1 to S3.7 | 751 |
| Section 5.12: the gap-attribution table with its shares. It is new here, built cell by cell from `gap_attribution.csv`: 22 figure rows, every non-input cause, and a key of 58 causes quoted as the csv states them. | Tables S1 and S1a | tables |
| Section 6.5: diet table variants (old Table 7), with the 103.6 no-meat point and the 118.0 against 112.4 corrected-release figures | S4, Table S2 | 51 + table |
| Section 6.9: Monte Carlo method detail (Latin hypercube and its citations, 12 of 13 varied, the improved-release benchmark, the additive shortcut, Saltelli), the five range-end values, and the variance-share table (old Table 8). The main text keeps the 1,000 draws over 13 choices, the 36.3 to 45.8 range, the factor 1.26, "not confidence intervals", the 81% meat window, and a pointer to the five judged range ends. Table 4 carries the ranges for every release. | S5, Table S3 | 155 + table |
| Section 7.7: the reporting checklist (old Table 10) and its factor sentences. The main text keeps the twelve items, which items are design choices, and the land-base reason. The matrix stays as Table 7. | S6, Table S4 | 79 + table |

Renumbering: old Tables 7, 8 and 10 became Tables S2, S3 and S4, and old Table 9 (the matrix) became Table 7. Every table, figure and section reference was checked: Tables 1 to 7, S1, S1a and S2 to S4; Figures 1 to 3; sections 1 to 9.5 and S1 to S6.

## 3. What was merged or cut (one line each)

Merged (a figure stays where it is a finding; the other place cites the section):
* Section 1: corrected 15.6 million cut. It stays in 5.9 and 6.8.
* Section 1: PMSEIC 60 and 40 million cut. They stay in 4.4 and Table 1.
* Section 1: Henry and Godden's 1990-91 sentence (109 and 96) cut. 109 stays in the opening sentence, 96 in 5.3 and Table 1.
* Section 1: the thesis's 40, 9 to 40 and 23 million cut from the prose. They stay in Table 1.
* Section 3: "the 2010 review covered all except Douglas Shire and Peters" cut. It stays in section 1.
* Section 4.4: "the report itself calls the measure misleading" cut. It stays in section 1.
* Section 4.4: Bellotti's one-line description cut. It stays in section 1.
* Section 4.5: the Giampietro and Saltelli critique now points to section 2 and S2.
* Section 4.2: Nix's "about 70 Mha" cut. It stays in 6.4 and S2.2.
* Section 5.3: "Gifford enters only through them" moved to S3.1.
* Section 5.5: "its authors say it is not predictive" cut. It stays in 4.6 and 7.3.
* Section 5.8: one criterion and six run points cut. They stay in 8.1 and S3.6.
* Section 5.9: "1,000 draws over 13 choices" cut and replaced by a pointer to 6.9. "Raises these by about 12 million and 3 million" cut, because Table 4 carries both tiers.
* Section 5.12: "Henry and Godden reproduced within rounding" cut. It stays in 5.3.
* Section 6.1: the 90-million sum, "keeps the report's own figure of 100", and Bellotti's 61 and 36.6 cut. All stay in section 1, where the [open: Q9] flag is carried.
* Section 6.1: the description of export counts replaced by a pointer to 4.4.
* Section 6.6: Fearnside's definition cut. It stays in 4.10.
* Section 6.7: Fairlie, Gutteridge, Peters and Khorsandi on the unit cut. They stay in section 4.
* Section 6.10: "counting exports takes the figures to 100" cut. It stays in 6.1 and 9.1.
* Section 6.10: the definition of 9.4 cut. It stays in section 1.
* Section 6.11: the ordering reduced to the ends (1.09; 4.4 to 6.4 and 7.88). The full order is in Table 6.
* Section 7.1: the list of seven methods cut. Table 7's columns carry it.
* Section 7.1: the planning studies are kept as a citation list.
* Section 7.2: the failure figures (41.5, 30.8, 18.9; 5.8 to 6.1%) and the commodity figures cut, citing 5.8. The Jones sentence cut. It stays in 6.6.
* Section 7.3: 276 and 145 to 183 cut, citing 5.10. Both stay in Tables 3 and 5 with their [gate 4] flags.
* Section 7.4: 75% and 37% cut, citing 6.7. 64.8 to 84.6 cut, citing 5.11.
* Section 7.5: HALF's 0.8%, 2.1% and 2% cut, citing 5.5. 6.2 ha and 0.27 ha cut, because Table S2 carries them.
* Section 7.6: "the pairing was not removed to test it" now cites 5.11.
* Section 7.7: the factor sentences moved to S6. Table 6 carries the factors.
* Section 8.1: Fearnside's four criteria now cite 4.10.
* Section 8.6: the New Zealand figures cut, citing 5.5.
* Section 8.7: "reproduced closely on 2011 data" and "the model's own runs" cut. They stay in 5.5 and 7.8.
* Section 9.2: "12 to 343 million as run and harmonised" cut, citing 5.11. The [gate 4] flag is carried there and in the abstract.

Cut. These works carry no figure, and nothing else in the paper cites them, so the reference list needs pruning:
* Section 6.3: the household-waste sentence (Reutter et al. 2017).
* Section 8.1: the breadbasket sentence (Gaupp et al. 2019).
* Section 8.2: the trade-diversity clause (Kummu et al. 2020).
* Section 8.3: the food, energy and water clause (D'Odorico et al. 2018).
* Section 8.4: the meat-peak clause (Whitton et al. 2021).
* Section 6.2: Peters 2016's sentence, Cassidy's clause and Alexander's p. 89 grassland clause cut. These authors are still cited in sections 4 and 5.
* Section 6.4: Fischer in 6.4 cut. Fischer is still cited in 4.9.
* Section 8.3: Lenzen and Murray's energy land cut. They are still cited in 4.5 and 6.2.

Tightened without a change of number or claim: every section. Examples: one-idea sentences in sections 1 to 3; the 5.1 and 5.2 merges; a shorter Table 3 note; "supplementary section S…" shortened to "section S…" after first use.

## 4. Claims csvs

* Main csvs were rebuilt on the cut text with sentences renumbered: 63, 185 and 125 rows (from 61, 233 and 186).
* 65 sentence rows moved to `supplementary_claims.csv`. Its extra `moved_from` column gives the old file, section and sentence. 25 rows from the moved tables (old 7, 8 and 10) went with them.
* Supplementary rows added: Table S1 (22 rows) and Table S1a (58 rows), each citing its `gap_attribution.csv` rows. 17 further rows cover numbers that now appear in both places or are new in the supplement. `supplementary_claims.csv` has 187 rows in all.
* 32 rows were dropped, one for each figure cut or merged in section 3. Each dropped figure is still in a csv where it remains in the text.
* 15 main-text rows were added: the abstract figures, "1.718 ha against 1.758", "22 crop items against 41 crops", "1990-91 in-use land carried forward", "within 1.2% each way" with 1997-98, "On production in 2021-23", and "a dairy share of about 57%".
* A script check finds every number in the main text and the supplement in a csv row for its sentence. Exceptions are labels and citation years: SA2, World3, build 1 and 3, decision 57, and citation years.
* Flags survive. [gate 4] covers 22 crop items, 147, 145, 183, 190, 134 to 343, three to eight times, 12 to 41, 12 to 343, 145.2 to 148.8, 110.9 to 112.9, 0.766 (in S3.4) and 5.8 a hectare. [open: Q8] covers 18.9 to 55.3 and 62.9. [open: Q9] covers 100, 90, 10.6, 2.41 and 1.59. [open: span] covers 109.

## 5. Points for the coordinator and Murray

1. Scope section 6 point 9 lists the five range-end values (0.115, 0.528, 50/50, 0.30). The brief's Monte Carlo instruction keeps only the ranges and the 81% choice, so the values moved to S5 and 6.9 points to them. Restoring them costs about 40 words, and the total stays under 8,000.
2. Scope section 7 point 6 requires 7.6's "134 to 343 ... about three to eight times", which decision 85 binds. So 7.6 keeps it although 5.10 states it too. Section 9 points 1 and 2 require 9.1's span and 1.26 and 9.2's 10% and 10 to 18%, so these are kept as well.
3. Table S1 was generated from `gap_attribution.csv` with a one-off script, which was not saved because the brief allows no other files. A table script in `analysis/method_tests_2025/` would make it reproducible.
4. "Table S5, p. SI-6" in 5.5 now reads "their Table S5", so it is not confused with this paper's supplement. Table S1a's caption says that "SI" in the quoted causes means the authors' supplement.
5. `paper_B_draft1.md` needs reassembling from the three section files and `supplementary.md`.
6. Time words: "still" in sections 2 and 8 and "today's" in Table S4 come from the first draft and the scope wording. No new ones were added. No em or en dashes.

## 6. Wrong-value check

Wrong-value check: EXAMPLE ONLY, not something done. Under the merge rule, 7.6's "134 to 343 million (the footprint 146 to 343 on current yields, 103 at 1990 yields), about three to eight times the balance" looks like a repeat of 5.10, and cutting it would save 25 words. It would break rule 4 three ways. The scope's section 7 content list (point 6) requires those figures. Decision 85 binds the wording. The sentence carries [gate 4] values in its csv row (7,42 in the first draft). So it was kept. The check that catches such a cut: every number named in a section's scope content list must still appear in that section's prose or tables after the cut.
