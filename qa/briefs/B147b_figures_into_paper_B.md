# Builder brief B147b: Table 2 and Figures 1 to 3 placed in Paper B

Rules: plain language; no em dashes anywhere; no time words. No git; no subagents; no network. Write only under `papers/B_methods/` (section files, claims csvs, `supplementary.md`, `SECTION_SCOPE.md`, `OUTLINE.md`) and `qa/reports/B147b_figures_into_paper_B.md`. Do not touch `paper_B_draft1.md`, `references.md`, any register, or `analysis/`.

Inputs: `analysis/figures_2025/paper_B/figures.csv` and `table_2.md` (as fixed by the B144b follow-up), `qa/reports/B144b_figures_paper_B.md` (with its appendix) and `V56b_check_figures_B.md`; the paper's placeholders ("[Figure 1", "[Figure 2", "[Figure 3", "Table 2") in the section files; `analysis/method_tests_2025/method_catalogue.csv`.

1. Replace each figure placeholder with a figure reference and the caption from `figures.csv` (the caption text as the builder amended it after V56b), in the form the journal takes ("Figure 1. ..."), the figure file named in the claims csv row (not in the prose); Table 2 takes the rows of `table_2.md` with the scale column; the Figure 1 caption says the italic placements are the author's reading of section 4, not ratings; the caption of Figure 2 says the commodity-balance row runs 12 to 128 because grain never binds; Figure 3's note on the 1.03 row as drawn.
2. Reconcile the two sentences the figures builder flagged: 5.10's "12 to 41" (add that grain with feed grain reads 127 to 128 and never binds); 7.6's "no method serves all four purposes" against Table 9's model row (after B146b the model is partly suited on purpose 1: make 7.6 say what Table 9 now says).
3. Every number in a caption has a claims row citing `figures.csv` and the source csv; the figure list in the supplement (if one exists) names the three files.
4. Word count: `python3 qa/tools/assemble_draft.py B` on a scratch copy, then `python3 qa/tools/wordcount.py B`: captions do not count, but the 5.10 and 7.6 sentences do; stay at or under 7,950; abstract unchanged.

Report: the captions as placed; the two reconciled sentences (before; after); word counts; "Wrong-value check:" with one caption number deliberately taken from the pre-fix figures.csv and caught against the fixed one, marked as an example.
