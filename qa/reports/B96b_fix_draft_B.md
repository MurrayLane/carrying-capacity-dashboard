# B96b: the V34b check applied to the Paper B first draft

Brief: `qa/briefs/B96b_fix_draft_B.md`. Check applied: `qa/reports/V34b_draft_check_B.md` (read in full first).
Files written: `papers/B_methods/draft/B_s01-03.md`, `B_s04-05.md`, `B_s06-09.md`, their three `_claims.csv` files, and this report. Nothing else was edited. Register rows touched: none. `paper_B_draft1.md` was not touched.

## 1. Fixes applied

Line numbers are for the files as they stand after this job.

| Fix | What changed | File:line |
|---|---|---|
| F1 | 4.4: the sentence "The statistics they draw on are the national food trade accounts (Department of Agriculture 2014)" deleted (the check's first option). | B_s04-05.md:25 |
| F2 | 4.11: "reviewed in the earlier work"; "the Noosa study is cited through Lane 2010 and the Douglas Shire study through the thesis (Lane 2014, chapter 6) only". | B_s04-05.md:57 |
| F3 | 5.10 and 7.6: "134 to 343 million (the footprint 146 to 343 on current yields, 103 at 1990 yields), about three to eight times the model" (7.6: "the balance"). 134/41.5 = 3.2 and 343/41.5 = 8.3, so "three to eight" holds. | B_s04-05.md:145; B_s06-09.md:136 |
| F4 | 5.12: "a calendar-year reading of consumption and putting all milk on pasture each overshoot the residual of 2.3% (149% and 175% of it); a dairy share of about 57% of milk would close it, but the paper prints no share." | B_s04-05.md:191 |
| F6, section 3 | "Where no file of a work is held, the work is cited as reported in a held work that reports it; where no such work is held, the text says once that the work was not seen and is cited from its abstract." | B_s01-03.md:59 |
| F6, as reported | Blomqvist et al. 2013 as reported in Giampietro and Saltelli 2014, p. 619 (sentence reworded to what that page reports; the self-sufficiency clause dropped) | B_s04-05.md:31 |
| | Fader et al. 2013 as reported in Clapp 2017, p. 90 (4.4) and p. 91 (8.2, which now carries Clapp's 16% reading of Fader) | B_s04-05.md:25; B_s06-09.md:173 |
| | Gerten et al. 2020 as reported in Beltran-Peña, Rosa and D'Odorico 2020, p. 5 (10.2 billion on existing cropland) | B_s04-05.md:49 |
| | Buzby 2010 and Muth 2011 as reported in Lane 2014, pp. 201 to 202; AUSNUT 2007 as reported in Lane 2014, p. 202; USDA Handbook 697 as reported in the archive's errata (8.5). 6.3 now points to 8.5 for the loss factors. | B_s06-09.md:185, 19 |
| | Gifford et al. 1975 in 7.3: "the method of Henry and Godden (1995) and of the 1975 estimate they report"; in 4.2 "cited as reported in Henry and Godden 1995 (p. 98)". | B_s06-09.md:124; B_s04-05.md:17 |
| | Table 1 route cell: "the author's own (thesis method); read in Lane 2014, p. 280" (V34b section 1 issue 1). | B_s01-03.md:29 |
| F6, not seen | "(not seen; cited from its abstract)" once, at first citation: Khorsandi et al. 2022 (s1); Lane, Dawes and Grace 2014, 2015 and Lane 2017 ("each not seen; cited from its abstract", s1); Shepon 2016, Goldfinger 2014, Wiedmann and Lenzen 2018, Kastner 2012, Röös 2017, Ridoutt 2020, Khorsandi 2023 (s4); McKay, Beckman and Conover 1979 and Helton and Davis 2003 ("each not seen ..."), Saltelli et al. 2008 (6.9); Erb et al. 2016 (8.4). | B_s01-03.md:17, 19; B_s04-05.md:17, 31, 35, 49; B_s06-09.md:62, 181 |
| F7 | 9.4: "the model workbook, default inputs, 2011 baseline and analysis outputs are under CC BY 4.0, and source data keep their publishers' licences (`LICENSE-DATA.md`)". | B_s06-09.md:211 |
| F8 | Section 5: harvest matching cut to two sentences with a Supplementary Table S1 pointer; 5.12 detail (H&G half unit, India, population year, Foran and Poldy, Cassidy) left to Supplementary Table S1; 5.11 restatement of Table 5 cut. Sections 4 and 6 trimmed by merging sentences. Counts in section 2 below. | B_s04-05.md:111, 168, 189 to 191 |
| Item 1 (S1) | Kept "about 9 to 100 million" and added "although one figure in Table 1, Henry and Godden's energy count of 109 million (1995, p. 100), sits above that span". Flagged "[open: span]" in the csv for Murray. | B_s01-03.md:5 |
| Item 2 (S2) | "Each was offered as a count of how many people Australia can feed." | B_s01-03.md:5 |
| Item 3 (S3) | 5.11: "is consistent with the pairing ...; the pairing was not removed from the model to test it." | B_s04-05.md:172 |
| Item 4 (S4) | 5.8: "so the failure risk at the 2025 population depends strongly on the method." | B_s04-05.md:129 |
| Item 5 (S5) | 5.12: "Australia's residual of 0.8% is partly explained by the supplement's cropland adjustment (42%) and is not closed by any cause tested." | B_s04-05.md:191 |
| Item 6 (S6) | Table 3, people per hectare fidelity cell: the check's wording; caption now says four cells differ, and the table note says why. | B_s04-05.md:154, 160 |
| Item 7 (S7) | Table 3, commodity balance fidelity cell: "production within 1.2%; their balance reproduced; the 30 and 77 readings are derived here". | B_s04-05.md:155 |
| Item 8 (S8) | 7.3: "because each shows what one family of published estimates counts". | B_s06-09.md:124 |
| Item 9 (S9) | 6.5: the emissions sentence cut; the cropland result (Willett p. 472) kept. | B_s06-09.md:29 |
| Item 10 (S10) | 5.4: "chiefly because". | B_s04-05.md:89 |
| Claims csvs | B297 moved to "putting all milk on pasture ... 175%"; the dairy share now cites B325; 149% cites B298. (6,90) 50/50 weight now A367. [gate 4] on every row of every sentence or table row that cites a pending row (B083, B084, B156, B273, B277): 32 rows in B_s04-05, 7 in B_s06-09, none needed in B_s01-03. Missing numbers added: ten diets, six farming regimes, three classes (4.1), about three to eight times (5.10, and 7.6), 223.9 (Figure 3). Two of the seven, "within half a unit" and "two to three times its residual", left the prose under F8, so they have no row. Rows also added for every new figure (109, 42%, 57%, 10.2 billion, 16%, 2025 population in 5.8, 2011 data in 7.5) and rows for cut fragments removed. Sentence numbers recomputed by one rule: prose sentences and table-note sentences in order, split at ". " or ": " before a capital; tables, captions and placeholders excluded. | the three csvs |
| Headings | Blocks reordered whole: 4.7 Optimisation (B4.7), 4.8 Integrated (B4.8), 4.9 Water-bounded (B4.9), 4.10 Failure probability. The one in-text reference updated ("Limits to Growth is placed in section 4.8"). Drafter note conflict 1 marked resolved. | B_s04-05.md:39 to 57 |
| Also, small | 5.4: "the rate Wackernagel's thesis prints", "Wackernagel's printed rate" (V34b section 5 issue 1). 4.6: Kastner "cropland needed" (section 4 issue 3). Figure 3 placeholder states the 10.6 product and the 223.9 top step beyond the span (section 6 issue 1). | B_s04-05.md:85, 87, 35; B_s06-09.md:79 |

## 2. Sentences cut, and word counts

Sentences cut whole (words): 4.4 F1 sentence (15); 5.6 "The 147 million do not change ..." (11), "The world figure stays at 7.9." (6), "The pairing moves Australia's figure ..." (26); 5.11 footprint, HALF and meat restatement (40); 5.12 Henry and Godden half-unit sentence (30), India clause (7), population-year sentence (27), Foran and Poldy sentence (34), Cassidy sentence (34); 6.1 "The report itself called the measure misleading ..." (19, already in section 1); 6.5 S9 emissions sentence (13); 6.11 "Table 6 orders the design choices ..." (15); 8.6 "The HALF rebuild covered 66 of the paper's 90 commodities." (10, already in 5.5). Others were merged or shortened.

Prose words (headings, tables, table captions, table notes and placeholders excluded). The V34b counts ran up to 40 words above this counter (section 4), so the margin below 15% is kept for that.

| Section | Budget | Before | After | Difference | Within 15% |
|---|---|---|---|---|---|
| 1 | 800 | 846 | 883 | +10% | yes |
| 2 | 1,000 | 898 | 898 | -10% | yes |
| 3 | 450 | 437 | 456 | +1% | yes |
| 4 | 1,800 | 2,016 | 1,992 | +11% | yes |
| 5 | 2,300 | 2,627 (2,823 with table notes) | 2,365 (2,580 with table notes) | +3% (+12%) | yes |
| 6 | 1,700 | 1,923 | 1,870 | +10% | yes |
| 7 | 900 | 991 | 991 | +10% | yes |
| 8 | 800 | 876 | 907 | +13% | yes |
| 9 | 350 | 317 | 329 | -6% | yes |

## 3. Register rows that need an edit (for Murray and the register job; none edited here)

* **B156** and **B247**: statements to carry "134 to 343 million (the footprint 146 to 343 on current yields, 103 at 1990 yields)" as the draft does (F3; decision 85 is Murray's).
* **B005**: the span. Henry and Godden's 109 (B008) and, in `harmonisation.csv`, their 172 and 206 (B009, unverified) sit above 100. The draft keeps "about 9 to 100" and names only the 109 that Table 1 prints; flagged [open: span].
* **B215**: Optimised C land 0.09 and 0.0 against `diet_land.csv` 0.06, 0.13, 0.19 (from V34b).
* **B060** against **B318**: 3,203 against 3,364 Mha (from V34b).
* **A367**: now the cited row for the 50/50 weight, and still "unverified".
* **L087** (Blomqvist): `what_taken` includes "at national scale the footprint measures self-sufficiency", which no held work reports; the draft dropped it.
* **L117** (van Zanten 2016): `local_path` names `..._FIRST_PAGE_ONLY.pdf`; the file on disk is `vanZanten2016_IJLCA_Global_food_supply_land_use_efficiency_of_livestock_systems.pdf`, so the work does have a file.
* **L182**: the title gives "Beltran-Peña 2020"; the paper has three authors (Beltran-Peña, Rosa and D'Odorico), as the draft cites it.
* Figures resting on a literature page, with no claims row: 10.2 billion (L182 p. 5), 16% (L179 p. 91), the Blomqvist reading (L085 p. 619), the loss-factor and AUSNUT sources (L020 pp. 201 to 202). A register job may want rows for them.
* Not register rows, but csv cells: `analysis/method_tests_2025/cross_method.csv`, people per hectare and commodity balance fidelity cells, need the S6 and S7 wording.

## 4. Points for Murray

1. The label "(not seen; cited from its abstract)" is the brief's wording. For several works the literature register records a full-text read of an open copy that is not on disk (Khorsandi 2022 and 2023, Kastner, Goldfinger, Röös, Ridoutt 2020, Wiedmann and Lenzen, Shepon, Erb), and for the author's own 2014, 2015 and 2017 papers. Some of those sentences say more than an abstract would (for example "cites the thesis" for Khorsandi 2022). Fetching these files (decision 82) would let the labels go. McKay, Helton and Saltelli are "record only", so even an abstract was not read.
2. 8.5 says the thesis model borrowed a carcase-to-retail factor for beef from USDA Handbook 697. ERRATA row 2 says the shipped model had 1.0 and that 0.705 (from Handbook 697) was in earlier workbook versions. The sentence is cited as the errata report it but may need rewording.
3. 7.1 still says "the four planning-oriented studies" and names five (V34b section 7 issue 1); not in this brief, so unchanged.

## 5. Checks before finishing

* Em dashes and en dashes: none in the three drafts or the three csvs.
* Every number in the claims csvs: a script matched every number in every prose sentence and changed table cell to a csv row for that sentence. Left out by the drafters' rule: citation years, pages, and section, table and figure numbers ("the 2010 review", "a 1975 submission").
* References resolve: every author-year citation maps to a `qa/literature_register.csv` row; every B, A and L id and every csv path in the claims csvs exists.
* No time words in new text ("now growing" and "current extent" were reworded; "on current yields" is the brief's wording).

## 6. Wrong-value check

**Example (deliberate wrong fix, not applied).** For F4, a wrong fix would read "a dairy share of about 75% of milk would close it". Against B325 (106 kg of 186 kg, 57%), 75 FAILS and 57 PASSES. Likewise for F3, writing "two to eight times" fails against B247 (3 to 8), because 134/41.5 = 3.2.
