# V57b: final blind read of Paper B before deposit

Reader: a blind checker session. Read: `papers/B_methods/draft/paper_B_draft1.md` (sections 1 to 9 and declarations; drafter notes appendix skipped except to confirm it is marked not for the paper), `supplementary.md`, `highlights.md`, `references.md`, `B_s10_declarations.md`, `papers/B_methods/response_letter_round2.md`, the three 190 mm PNGs and `figures.csv` under `analysis/figures_2025/paper_B/`. This is a submission check, not a tracing audit: numbers were not re-traced (V54b did that). No git, no subagents, no network. Only this file was written.

## Fails first

Ranked by seriousness. Each gives file, section and the sentence.

**F1. The model's purpose 1 rating: Figure 1 caption contradicts Table 9 and section 7.6.** `paper_B_draft1.md`, section 4, Figure 1 caption: "the author's model, rated well suited to all four (for crops at purpose 1, not tested on pasture-fed output), sits at the first." Table 9 rates the model "partly suited" for purpose 1, and section 7.6 says "In the author's ratings no method is well suited to all four purposes, the model being partly suited to the first." The caption was not updated after the round-three lowering. Also, by the caption's own placement rule (highest rating, fewest others sharing it), the model would sit at purpose 2 or 3, not 1. It sits at purpose 1 in the figure and in Table 2. Fix: "the author's model, rated partly suited to purpose 1 and well suited to the other three, is placed at purpose 1, the purpose it was built for." Or move the mark and state the rule as applied. `figures.csv` carries the same stale caption.

**F2. The pairing sentence says more than its numbers (abstract, highlight 4, sections 7.6 and 9.1), and the letter misquotes it.**
- Abstract: "relaxing the pasture-crop pairing closes the gap only if pasture-fed food is replaced at equal energy or protein (81.7 and 85.4 million...)". Section 7.6 and section 9.1 say the same. Highlight 4: "The pairing reaches HALF only at equal energy or protein; pooling is 18% of the gap".
- (i) The 85.4 million variant holds energy *and* protein (section S3.12: "energy and protein at least the diet's"; section 5.14: "holding the diet's protein as well"), so "or protein" misdescribes it.
- (ii) "Only" claims more than was tested. Two substitution rules were run, and Table 7 variant 2 (107.7 million, 192% of the gap to HALF) also passes HALF, though it changes the diet. Section S3.12 also gives 92.4 million with dairy allowed to rise.
- (iii) Highlight 4 drops the condition on the 18%. Section 5.14 says the pooling rule is 18% "at HALF's own exchange rate" and 60% of a larger gap at the variant 1 rate.
- (iv) The letter ("Third round, Both referees") says these places read "at equal energy (variant 1 ...) or at equal energy and protein (85.4 million)". They do not: the paper says "equal energy or protein".
- Fix (abstract and 7.6 and 9.1): "of the substitutions tested, the relaxed pairing reaches HALF's reading when pasture-fed food is replaced at equal energy (81.7 million) or at equal energy and protein (85.4 million)". Highlight 4, fixed and checked against the 85-character limit (80 characters): "Relaxing the pairing reaches HALF at equal energy; pooling is 18% at HALF's rate".

**F3. Internal labels left in the paper and the supplement** (brief: no job ids, register ids, release codes, file paths).
- Title: "Paper B, methods: ..." The heading lines "First draft, assembled 2026-11-18 ... Not for circulation.", "# Paper B, sections 1 to 3" and "# Paper B, sections 6 to 9", and the "Appendix: drafter notes" all sit in the assembled file. The title in the letter is "Well-known carrying-capacity methods tested on common Australian data".
- Register ids: Table 2 has a "Register ids" column (L020, L012, ... 32 ids), and its caption says "the literature register ids".
- File paths in captions and text (36 backticked paths in the main text, 47 in the supplement):
  - Tables 1 to 9 captions and Figures 1 to 3 captions ("Built from `analysis/...csv`")
  - Table 9: "Typed from `papers/B_methods/SECTION7_DRAFT.md`"
  - Table 1: "ladder row"
  - section 5.9 and section 8.5: "the repository's ERRATA.md"
  - section 9.4: `results/releases.json`, `LICENSE-DATA.md`
  - supplement: every table caption, plus `monte_carlo.mjs`, `data/abs-2022-25/group_trend.json` (Table S14), the sha256 hash and "the project's data register" (S3.14), `results/2025-fixed.csv` and "the evaluator" (S3.12), and "supplementary_claims.csv" (supplement opening).
- Release codes: Table 4 "Release" column (2025-mirror, 2025-fixed, 2025-improved), section 9.4, and Table S4.
- Note: the letter (modeller M8) says "Captions name each table's source file, as section 9.4's reproducibility claim requires (the author's choice)". The brief and that decision conflict. This is a decision row for the author: keep source names in the data statement only, or keep them in captions. The register ids, "ladder row", SECTION7_DRAFT.md, the draft heading lines and the drafter appendix have no such reason and must go.

**F4. The letter states things the paper does not carry.** All in `response_letter_round2.md`.
- (a) "Presentation (M8), third round": "Internal file paths are out of S3.14 and Table S15." Section S3.14 still has `bases.csv` in its text and two paths in the Table S12 caption, plus the sha256 hash.
- (b) Modeller minor 3 quotes section S4 as "The records do not trace why pasture a person doubles between 5% and 7.5%". The supplement reads "The records do not show why ...". Quote mismatch.
- (c) Ecological economist minor issues: "Section 5.10 notes that 211 is the energy balance on 1990-91 land (2); the abstract does not." The abstract now does ("the top, the 1990-91 energy balance"), as the third-round section itself says.
- (d) Ecological economist M9: "the tie to van den Bergh and Rietveld (2004) is not drawn in the introduction". Section 1 now draws it, and the third round says so. Mark the earlier text as superseded.
- (e) Modeller M8 and third round: "Table 2 and Figures 1 to 3 are placeholders in the manuscript file and are not supplied". The manuscript carries Table 2 in full, and the three figures exist as PNG and SVG. Reword to "are supplied with this revision".
- (f) Works added and not cited: "Muth et al. 2011 and Lane 2014 replace Buzby 2010". But Buzby 2010 is still in the reference list, uncited (see F5).

**F5. Reference list against prose.**
- In the list, cited nowhere in the paper or supplement:
  - Buzby, 2010 (the letter says it is replaced)
  - Mottet et al., 2017 (the letter says it is not cited)
  Delete both.
- Cited, not in the list: "Paper A, section 2" (section 5.9), a companion paper with no entry and no identification. "ERRATA.md" (sections 5.9, 8.5) is a repository file, not a reference. Fix: cite Paper A as a submitted or in-press work, or drop the cross-reference and point to the archive.
- Elsevier Harvard form:
  - Malformed entries: "Buzby, 2010. (cited in Lane, 2014)", "Mottet, et al., 2017.", "Nix, n.d. (cited in ...)", "Migration Committee, 1986. (cited in ...)". AUSNUT 2007 has no URL.
  - Every entry carries an HTML comment with a register id (`<!-- L017 -->`), and the file header names `qa/tools/make_references.py`. These must be stripped from the submitted list.
  - In text, works with three authors are spelled out (Simpson, Petroeschevsky and Lowe; Peters, Wilkins and Fick; Graymore, Sipe and Rickson; Lane, Dawes and Grace; McKay, Beckman and Conover). Elsevier Harvard uses "et al." for three or more.
  - Parenthetical citations have no comma between name and year ("(Lane 2014, p. 280)"; the style is "(Lane, 2014, p. 280)").
  - Confirm both points against the journal guide; they are form, not substance.

**F6. The drought comparison in sections 6.10 and 9.2 picks the variant the paper calls untested.** "The spread across the settings varied together (a factor of 1.58) is smaller than the drought allowance alone (2.19) and larger than waste alone (1.33)." The 2.19 puts the cereal weather factor on pasture-fed output, which the paper says no livestock series has tested. On crops only, the same allowance is 1.03, below 1.58. Fix: "smaller than the drought allowance with the factor on every yield (2.19), larger than the same allowance on crops only (1.03), and larger than waste alone (1.33)."

**F7. Figure captions in `figures.csv` and in the PNGs differ from the paper.**
- Figure 1, paper: "they are the author's reading of section 4, not ratings". Figure 1, `figures.csv` and the legend drawn in the PNG: "placed by the builder's reading of section 4". "Builder" is an internal word, and the two versions disagree.
- Figure 3, `figures.csv`: "a note beside the 1.03 row linking them". Paper: "reading 'same allowance as the 2.19 row'". The PNG matches the paper.
- Fix: regenerate `figures.csv` from the paper captions, and redraw the Figure 1 legend line as "Italic: not rated in Table 9; placed by the author's reading of section 4".

**F8. Time words.**
- Section 5.2: "The authors had not been consulted at the time of writing."
- Section 9.4: "On 18 November 2026 the archive has no DOI and the author has not deposited it on Zenodo." This becomes the DOI sentence at deposit; it is an author placeholder.
- Supplement opening: "the detail moved out of the main text when it was cut to the journal's length ... and the tables and rubric the revision adds".
- S3.12: "Of the three further tests proposed after it, two have been run".
- S5: "run before six settings were added, which was not rerun".
- Letter, to the editor: "no longer a range". This is acceptable in a response letter, but noted.
- Fix for 5.2: "The authors were not consulted."

**F9. Internal working register in the supplement** (tone, not substance).
- S3.13 and S3.14: "the ABS tables are not on disk". Fix: "were not available to this study".
- S3.14: "this is a compute job ..., not done here".
- S3.12: "the evaluator". Fix: "the model's program".
- These read as project notes, not as a paper.

Minor, not fails:
- Figure 2 caption: "Every reading is one dot: 19 readings ... on each line". On the harmonised lines several readings coincide: the energy balance's six readings fall on two values, and people per hectare's three on two. So about 14 dots are visible per line against 19 as run. Add "coinciding readings overplot".
- Supplementary tables are not numbered in order of first citation. Table S7 is first cited in the Figure 2 caption, before Tables S5 and S6.
- Highlight 5, "One at a time, weather gives 18.9 million", omits "the worst year in 100".

## Overclaim (step 2), item by item

- Pairing and bridge sentences: fail, F2. The bridge sentence in section 9.1 ("spreads the gap of 34.5 million over seven features") is supported by Table 7 panel B. It should keep section 5.14's caveat that requirement and waste cannot be separated, which it drops.
- "Partly suited" rating: Table 9, sections 7.1, 7.2, 7.6 and S7 are consistent with each other. Figure 1 caption fails (F1).
- Line (b) against line (a): consistent across the abstract, sections 1, 5.11 and 9.1, Table 6 and the letter (28% to 46%; -1% to 7%; 10% to 16% on line (c)). No overclaim found. Lost-reader risk: Table 5's column "(b) Harmonised" is not line (b) (see below).
- Drought-bound sentences: sections 5.8, 6.6, S3.6, Table 4 and Table 8 are careful ("a bound set by the last run point", "does not cover the binding constraint"). Sections 6.10 and 9.2 fail (F6).
- Ten-year window sentence (section 5.1): supported by S3.14. "An upper indication and not a measured effect" is right. "Would fall" for the crop-scaled readings matches S3.14 ("The direction is known"). Not a fail. A reader may assume the +6% comes from crops when it comes from beef and milk; adding "(from beef and milk, which were below their ten-year means)" would prevent that.
- Abstract and highlights 1 to 3: consistent with sections 5.10 and S3.11 (1.6 to 5; 1.56 to 2.82; 2.4 to 4.3; 53.9 to 77.9). Highlight 2's "most of their gap" is supported: 61% and 68% (S3.11).

## Consistency (step 1), other checks that passed

- Every figure, table, section and supplementary-table number cited in the prose exists (Tables 1 to 9, S1 to S15, Figures 1 to 3, sections S1 to S8). "Table 16" is the thesis's own table.
- Letter quotations found verbatim: 5.11 (M1 and M3), section 7.1 "No outside person has rated the table.", the abstract weather sentence (M7), highlight 2 (M3), S5 "an illustration at 20% either way, not a bound" (prefix of the sentence), section 9.1 "not Simpson's other components or people per hectare", and section 5.2 "The authors had not been consulted at the time of writing". The two exceptions are F2 and F4(b).
- "A sufficient cause" and "Which line holds is a classification" are gone from the paper, as the letter says.
- The Monte Carlo (31.1 to 49.2, 1.58, median 39.0, 19 settings with 18 varying) agrees across the abstract, sections 6.9 and 6.10, Tables 3, 4 and 8, Figure 2, S5 and Table S4.
- The Table 2 catalogue matches the Figure 1 marks for all 13 methods (purpose column and people-count shape). The exception is the model's placement rule (F1).

## Journal counts (step 3)

| Check | Limit | Count | Result |
|---|---|---|---|
| `python3 qa/tools/wordcount.py B` | at most 7,950 | 7,934 (s1 714, s2 519, s3 295, s4 858, s5 2,723, s6 1,324, s7 656, s8 468, s9 377) | pass, 16 words spare |
| Abstract | at most 250 words | 250 | pass, at the limit |
| Highlights | 3 to 5, at most 85 characters each | 5: 76, 84, 84, 83, 77 | pass (highlight 4 fails on content, F2) |
| Keywords | 1 to 7 | 7 | pass |
| Em dashes | none | 0 in the paper, supplement, highlights, references, declarations, letter and SVGs | pass (en dashes appear only in reference page ranges, which is correct) |
| Time words | none | see F8 | fail |
| Internal labels | none | see F3 | fail |
| References | every citation listed and every entry cited | 129 entries; 2 uncited, 1 cited work unlisted (Paper A); see F5 | fail |
| Decision 33 tone | no sentence about other authors' shortcomings | neutral throughout; "stated without a source" (Table 1, S2.4, PMSEIC) is factual | pass |
| Declarations | complete except the bracketed author placeholders | AI, competing interests, funding, CRediT and data availability present; placeholders below | pass |

### [CHECK] markers in `references.md`: 30 entries, with what each needs

The author can fill these from the source or a library catalogue:

- Place of publication only:
  - ABS 1994
  - Centre for Population 2026
  - CSIRO and University of Queensland 2025
  - DCCEEW 2017
  - Food Innovation Australia Limited 2021
  - Lane 2014
  - Treasury 2021
  - Treasury 2023
  - USDA 1992
  - Wackernagel 1994
- AUSNUT 2007: URL, access date, version.
- Australian Bureau of Statistics 2011: confirm that the meat calibration reads the December 2010 issue.
- Chisholm 2000: volume, and the surname spelling (Chisolm on the page).
- DCCEEW 2019: publisher, place, and whether to name Arcadis as author.
- DCCEEW n.d.: year.
- Fairlie 2008: volume and pages, DOI if any. The file held is a later chapter version, not the issue 4 article.
- Geoscience Australia and ABARE 2010: publisher and place.
- Gifford et al. 1975: DOI if any.
- Gutteridge 2005: publisher and place.
- Jansen 1999: not seen, needs fetching.
- Saltelli et al. 2010: not seen, needs fetching.
- National Health and Medical Research Council 2006: not seen; confirm year, version and table numbers.
- Wackernagel and Rees 1996: place, edition, and the year from the imprint.
- Taylor 1922: end page and initials from the article itself.
- National Population Council 1992: the report itself (second-hand).
- National Population Inquiry 1975: the identity of the work cited as Borrie (second-hand).

The author cannot fill these from what is held:
- Nix n.d.: the work is unidentified. Recast it in the text as "Nix, as cited in Henry and Godden (1995)" and drop the entry, or identify the work.
- Migration Committee 1986: the work is unidentified. Same remedy.
- Buzby 2010: delete (uncited).
- Mottet et al. 2017: delete (uncited).

The CHECK notes also name the author by first name ("Murray fetches", in three entries). They must not survive into the submitted list.

## Placeholders left for the author

1. AI declaration (in the paper and in `B_s10_declarations.md`): "Opus [model name and version: author to enter from the account's usage history]".
2. AI declaration: "Sonnet [model name and version: author to enter]".
3. CRediT: "**[Author name]:**", plus confirmation of the roles.
4. Section 9.4: the archive DOI. The sentence "On 18 November 2026 the archive has no DOI ..." becomes the DOI statement at deposit.
5. Title page: author name and affiliation, blank by design. Also confirm the declaration heading against the journal guide, the "doctoral thesis" wording and the funding statement (drafter note to `B_s10_declarations.md`).
6. Letter, ecological economist M2: the edition and date of the national-accounts release checked, left to the author.
7. The 26 fillable [CHECK] reference fields above.

## Figures (step 4)

All three PNGs are 2,244 px wide at 300 dpi, which is 190 mm. All have legends and are legible at that width.

- **Figure 1:** the marks match Table 2 (purpose and people-count shape for all 13 methods). Failures are F1 (caption and placement rule) and F7 ("builder" in the legend). There is no label collision; the purpose 2 column header wraps to three lines but is clear.
- **Figure 2:** the bands (31.1 to 49.2 grey; 37.9 to 60.0 hatched) and base lines (41.5, 53.6) match the caption, and the footprint line (b) dots sit at 53.9, 64.8, 77.9, 84.6, 112.5 and 117. Overplotting (minor, above). The vertical base lines have no legend entry, but the caption covers them.
- **Figure 3:** the values and order match Table 8 panel A, and the "same allowance as the 2.19 row" note is present. Minor: the 1.03 bar's start mark overlaps the axis at 1, and the label "(PAL 1.4 to 1.8)" wraps with "1.8)" alone on its line. The pasture-output row does not say "an illustration", which Table 8 does.

## The reader's test (step 5)

1. **Table 5's columns against the lines.** Column "(b) Harmonised" holds the line (a) harmonised readings (the footprint 139 to 343, HALF 275.8), and the line (b) readings sit in column (e). A referee will read column (b) as line (b). One sentence to fix it, in the Table 5 caption: "Column (b) is the harmonised reading with the productivity basis kept (line (a)); the line (b) readings of the footprint and HALF, at Australia's own productivity, are column (e)." Better still, relabel the columns with words, not letters.
2. **The pairing and the pooling rule.** The abstract, highlight 4 and section 5.14 lean on "the pasture-crop pairing", "the pooling rule" and "HALF's land exchange rate" before any plain statement of what they are. One sentence to fix it, early in section 5.14 (or section 4.1): "The model holds cropland and pasture as separate limits, each feeding its own part of a fixed diet, so the scarcer land sets the total; the footprint and HALF instead pool all land into one sum of world-average hectares."
3. **Which model, and what Paper A is.** "The thesis method as built", "corrected", "improved", "the published method", "2025-mirror/fixed/improved", "the reference", "Paper A, section 2" and "the failure view" all name versions or uses of one model. One sentence to fix it, in section 5.9: "The model is used in three versions: as published in the thesis (two errors kept, 49.4 million), corrected (41.5 million, the reference everywhere unless stated) and improved with Australian settings (53.6 million); the failure view is the corrected version read through Fearnside's frame." Cite Paper A properly or drop it.

**The sentence I would put first in the abstract:** "Published estimates of how many people Australia can feed differ tenfold mainly because they answer different questions, so a capacity figure means little unless it states its question, diet, waste, weather allowance, land base, unit and time frame."

## Register rows touched

None.
