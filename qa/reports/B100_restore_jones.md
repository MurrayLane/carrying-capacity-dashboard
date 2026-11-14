# B100: the Jones committee figures restored in the Paper B draft

Brief: `qa/briefs/B100_restore_jones.md`. Source: `qa/reports/B99_jones_report_read.md`. Pages confirmed on the PDF (printed page = sheet minus 14): para 2.13 pp. 39 to 40 (sheets 53 to 54); paras 2.15 and 2.16 p. 40 (sheet 54); para 1.28 and note 13 p. 8 (sheet 22); para 8.4 p. 143 (sheet 157, unnumbered, by sequence); para 8.10 p. 144 (sheet 158). Para 1.61 p. 17 and para 2.17 pp. 40 to 41 are from B99 and were not re-opened.

## 1. Insertions

- `B_s01-03.md` line 13 (section 1, "The spread is old"), three sentences after the CSIRO 1975 sentence: the Jones committee accepted "in subsistence terms Australia has the arable land to produce food for 50 plus million people", but "allowing a safety margin for the possibility of a run of bad seasons" put the population "carrying capacity" at 30 to 35 million "in terms of the food constraint" (para 2.16, p. 40); it called even serious estimates "little more than 'guesstimates'" (para 2.13, pp. 39 to 40) and proposed no target (para 8.10, p. 144); its report also gives 50-60 million for Gifford and others, with no basis (para 2.17, pp. 40 to 41).
- `B_s01-03.md` lines 25 to 39: Table 1 rows and a note line (section 2 below). Caption changed from "all rows except PMSEIC 2010" to "all rows except PMSEIC 2010 and the four marked 'from the report'".
- `B_s04-05.md` line 113 (5.8, Test), one sentence: the Jones committee's 30 to 35 million "in terms of the food constraint", after a safety margin for a run of bad seasons (para 2.16, p. 40), brackets the model's 30.8 million at 1 in 10; the committee states no failure probability, so the two agree in scale, not in method.
- `B_s06-09.md` line 31 (6.6), replacing the sentence that said the figures were not quoted: the two figures with the 2.16 framing and page, the margin being a stated allowance and not a return period, and the 2.13 caution and 8.10 no-target point with pages.
- Omission notes removed: `B_s01-03.md` drafter note "What could not be sourced" item 1 (list renumbered 1 to 7); `B_s04-05.md` drafter note item 4 (list renumbered); `B_s06-09.md` the Jones bullet of the drafter notes. Edited, not removed: `B_s01-03.md` note 4 (Taylor, Borrie and the Council now in Table 1) and conflict 2 (now says the draft quotes the report, not the thesis summary). No Jones sentence was found in section 7.2, as B99 said.

## 2. Table 1 rows added (the caption names csv sources, so the rows carry "from the report, p. n" in the route column, and a note line under the table says so)

| Row | People (million) | Route |
|---|---|---|
| Taylor 1922; 1937 | 65 (1922); 20 (1937); the 1937 figure assumes a much higher standard of living | from the report, p. 8 |
| Borrie 1975 | 50 to 60 | from the report, p. 17 and p. 143 |
| National Population Council 1991 | 50 (a maximum) | from the report, p. 40 |
| Jones committee 1994 (restored row) | 50 plus (subsistence terms); 30 to 35 (food constraint, bad-seasons margin) | from the report, p. 40 |

Other columns read "not given" where the report states nothing. The note says Taylor, Borrie and the Council are second-hand.

## 3. Register rows changed

- `qa/claims_register.csv`: B196 and B197 statements now carry p. 40, para 2.16 and the food-constraint framing; status "self-checked (B99, from the report)"; notes appended. B006 note appended: the 30 to 35 element is confirmed at p. 40 and its other figures are unchanged (statement and status left as they were).
- `qa/literature_register.csv`: L002 notes only, appended: the Jones report (para 2.17, pp. 40 to 41) attributes 50-60 million to Gifford and others, against the 82, 60 and 30 million of Henry and Godden 1995, with no basis given.
- `qa/defects.csv`: X120 fixed_in set to "B99; B100".
- Parse checks: claims register 701 rows, 18 columns each; literature register 244 rows, 12 columns; defects 127 rows, 8 columns. Row counts unchanged. CRLF endings kept.

## 4. Claims csvs

`B_s01-03_claims.csv` +14 rows (64 to 78: six body rows at sentences 15a to 15c, eight Table 1 rows), `B_s04-05_claims.csv` +3 (186 to 189, sentence 46a), `B_s06-09_claims.csv` +4 net (126 to 130; the one "not quoted" row at 6.6 sentence 37 removed and five rows added). All new rows carry register id L006 (L002 also on the Gifford row) and the page.

## 5. Word counts (prose only: not headings, tables, captions, notes or drafter notes)

| Section | Before | After | Budget room asked for |
|---|---|---|---|
| 1 | 689 | 787 | about 110 (800 cap); used 98 |
| 5 | 1,794 | 1,845 | about 180; used 51 |
| 6 | 1,445 | 1,527 | about 300; used 82 |

The counter reproduces B98b's figures for sections 1 to 3 exactly; for sections 4 to 7 it runs higher than B98b's report (for example section 5: 1,794 here against 1,769), so the changes are the figure to rely on. Nothing was cut to make room; no number was removed. Sections 2, 3, 4, 7, 8 and 9 are unchanged.

## 6. Checks

No em dashes in any file written. No time words in the new text. Every new number (50 plus, 30 to 35, 50-60, 65, 20, 50, pages, paragraph numbers, 30.8) has a row in a claims csv. `paper_B_draft1.md` and `supplementary.md` were not touched.

Open points for Murray: (a) scope section 1 point 1 said to quote the figure "as summarised in the thesis"; the draft quotes the report instead, because the thesis has no 30 to 35 (X120). (b) The Jones committee's full title appears only in the Table 1 note; the body uses "the Jones committee (1994)". The reference list entry is not in these files. (c) B198 and B138 were not read (not in B99).

Wrong-value check: example only, not a finding. A draft that said "the Jones committee put the food-constraint capacity at 30 to 35 million (p. 44)" would carry a wrong page: the figure is at p. 40, para 2.16 (sheet 54), and p. 44 is in a different part of chapter 2.
