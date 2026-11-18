# B147b: Table 2 and Figures 1 to 3 placed in Paper B

Changed files (all under papers/B_methods/ except this report): draft/B_s04-05.md, draft/B_s04-05_claims.csv, draft/B_s06-09.md, draft/B_s06-09_claims.csv, OUTLINE.md, SECTION_SCOPE.md. Not touched: paper_B_draft1.md, references.md, supplementary.md (it has no figure list, so there was nothing to name the three files in), registers, analysis/. The assembly check ran on a scratch copy.

## Captions as placed

Table 2 (section 4, above the 13-row table of table_2.md with its scale column). Figure 1 (section 4), Figure 2 (section 5.10), Figure 3 (section 6.10). Figure files are named in the claims csv rows, not in the prose. Two caption edits from figures.csv: Figure 1 now says "they are the author's reading of section 4, not ratings" (was "the builder placed them by reading section 4"); Figure 3 now says the note beside the 1.03 row reads "same allowance as the 2.19 row" (the text drawn by fig3_design_choices.py). Figure 2 is as in figures.csv and carries the 12 to 128 explanation.

> Table 2. The catalogue of methods: family, what it measures, the question it answers, data it needs, whether it gives a people count directly, scale, the Australian reading, and the literature register ids. Built from `analysis/method_tests_2025/method_catalogue.csv`.

> Figure 1. The methods of section 4 mapped by the question each answers, in the four purposes of section 7 (columns). Each method has one mark. A method rated in Table 9 sits at the purpose where Table 9 rates it highest and the fewest other rated methods share that rating; the author's model, rated well suited to all four (for crops at purpose 1, not tested on pasture-fed output), sits at the first. Names in italic are not rated in Table 9 (the Peters land and diet balance, failure probability, the export-inclusive count, optimisation, integrated resource-flow, water-bounded capacity, and index and planning studies); they are the author's reading of section 4, not ratings. Mark shape shows whether the method gives a people count directly, only by a further step, not at all, or is mixed (the planning studies); orange is the author's model. Built from `analysis/method_tests_2025/method_catalogue.csv` (Table 2).

> Figure 2. Each method's reading of Australia on the common 2021 to 2023 data, as run and under lines (a), (b) and (c) of section 5.11, beside the model's widened ranges (million people, log scale). Every reading is one dot: 19 readings of five methods on each line, including the footprint's pasture-only readings (Table 5 column (e) prints those at Australia's own productivity, 53.9 to 77.9; as run they are 316.9 and 385.7). The commodity-balance row runs 12 to 128 because grain with feed grain (127 to 128) is plotted but never binds, so the commodity balance's capacity range is 12 to 41. Line (a) keeps the productivity basis as part of the method, line (b) treats it as an input, and line (c) adds one per-person requirement and waste treatment to line (b) (cell c1 of Table S7). The grey band is the corrected release's 5th to 95th percentile (31.1 to 49.2) and the hatched band the improved release's (37.9 to 60.0); the vertical lines mark each release's base value. Built from `harmonised_comparison_lines.csv`, `harmonised_line_c.csv`, `results/ranges_2025-fixed_wide.csv` and `results/ranges_2025-improved_wide.csv`.

> Figure 3. The factor by which each single choice moved the answer of the author's model, one at a time (Table 8, panel A; higher capacity over lower, log scale). Single choices are ranked by factor; the drought allowance appears twice, with the weather factor on every yield (2.19) and on crop output alone (1.03), a note beside the 1.03 row reading "same allowance as the 2.19 row". Below the line, not ranked: the diet C upper bound (triangle), two bundles of settings (squares) and the spread across the settings drawn together (diamonds). Built from `analysis/method_tests_2025/design_choices_panels.csv`.

## Two reconciled sentences

5.10 ("12 to 41").
Before: "The second, the commodity balance, reads 12 to 41 million, its low end the single-commodity fish reading."
After: "The second, the commodity balance, reads 12 to 41 million, its low end the fish reading; grain with feed grain (127 to 128) never binds."

7.6 ("no method serves all four purposes").
Before: "In the author's ratings no single method serves all four purposes."
After: "In the author's ratings no method is well suited to all four purposes, the model being partly suited to the first." Table 9 prints the model as partly suited, well suited, well suited, well suited, and no other column has a well suited cell in more than one row. To stay in budget the same paragraph's "say that the factor is untested on pasture-fed output" became "(untested on pasture-fed output)", same meaning.

## Word counts

`qa/tools/wordcount.py B` before: 7,948. After: 7,934 (cap 7,950). The fall is because the old Table 2 placeholder line was counted as prose; the two sentences add 8 (section 5) and 5 (section 7). Per section after: 1 714, 2 519, 3 295, 4 858, 5 2723, 6 1324, 7 656, 8 468, 9 377. Abstract unchanged at 250 words. `assemble_draft.py B` on the scratch copy ran clean (4 section files); the repository's paper_B_draft1.md was not regenerated.

## Claims

Rows added: B_s04-05_claims.csv, 13 (Table 2 whole and by row group, Figure 1, five for Figure 2, one for the 5.10 sentence); B_s06-09_claims.csv, 3 (Figure 3 file, 2.19 and 1.03, and the 7.6 sentence). Every caption number (19; 53.9 to 77.9; 316.9; 385.7; 12 to 128; 127 to 128; 12 to 41; 31.1 to 49.2; 37.9 to 60.0; 2.19; 1.03) has a row citing figures.csv and its source csv. Flag: B153's value field (12 to 41) is narrower than the 12 to 128 drawn; the row says so. All csvs parse with constant column counts.

Wrong-value check: (example) the footprint reading "103 to 343" is the pre-fix figures.csv/Table 5 value for the as-run range. Checked against the fixed table_2.md, "103 to 343" is absent and the row reads "146 to 343 million people as run ... (103 at 1990 world yields)": caught. The 103 survives only as the 1990-yield reading, so a search for the number alone would have passed; the check has to be on the phrase.

No em dashes in any changed file (grep count 0).
