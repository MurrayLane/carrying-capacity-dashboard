# Builder brief B147a: Figures 1 to 8 and S6 placed in Paper A

Rules: plain language; no em dashes anywhere; no time words. No git; no subagents; no network. Write only under `papers/A_results/` (section files, claims csvs, `supplementary.md`, `SECTION_SCOPE.md`, `OUTLINE.md`) and `qa/reports/B147a_figures_into_paper_A.md`. Do not touch `paper_A_draft1.md`, `references.md`, any register, or `analysis/`.

Inputs: `analysis/figures_2025/paper_A/figures.csv` (as fixed by the B144a follow-up), `qa/reports/B144a_figures_paper_A.md` (with its appendix) and `V56a_check_figures_A.md`; the paper's placeholders ("[Figure 1" to "[Figure 8") in the section files and the supplement.

1. Replace each figure placeholder with a figure reference and the caption from `figures.csv` (as amended after V56a), in the journal's form ("Figure 1. ..."), the figure file named in the claims csv row (not in the prose); Figure S6 goes to the supplement with the named scenarios defined; the Figure 3 placeholder and the sentence that says "forward walk" change to the all-orderings average; the Figure 6 placeholder drops "with the named scenarios" and points to S6; the Figure 4 caption states the partition rule dependence or names the national-yield reference range as drawn.
2. Every number in a caption has a claims row citing `figures.csv` and the source csv; the supplement's figure list names the nine files.
3. Word count: `python3 qa/tools/wordcount.py A` after `python3 qa/tools/assemble_draft.py A` on a scratch copy: captions do not count, but any sentence changed does; stay at or under 7,950; abstract unchanged.

Report: the captions as placed; the sentences changed (before; after); word counts; "Wrong-value check:" with one caption number deliberately taken from the pre-fix figures.csv and caught against the fixed one, marked as an example.
