# Builder brief B126b: patch Paper B to the blind read V45b

Rules: plain language; no em dashes anywhere; no time words. No git; no subagents; no network. Write only under `papers/B_methods/` (section files, claims csvs, `supplementary.md`, `highlights.md`, `SECTION_SCOPE.md`, `OUTLINE.md`) and `qa/reports/B126b_patch_paper_B.md`. Do not touch `paper_B_draft1.md`, `references.md`, any register, or any file under `analysis/` (list what each needs).

Input: `qa/reports/V45b_read_paper_B.md`. Work every fail it lists, in its order, except the one below that is Murray's. For each: the fix, or why it stands (with the file and line that supports the current text). Where the read says a table was typed from a builder report instead of the file (Table S6 Simpson +21.6 against `fidelity.csv`; Table S8's 6.40, 2.48, 1.92 against `cross_method_local.csv`), take every cell of that table from the file as it now stands and say so in the caption's claims row. Where a caption names a file that still prints the 13-setting range (Table 3 `cross_method.csv`; Table 8 `design_choices.csv`), make the caption name the widened file (`results/ranges_2025-fixed_wide.csv` or the B115 file) for the range cells and list the two analysis files as needing regeneration.

Specific items:
- **Decision 118 (18.9 to 55.3 "by definition alone")** is Murray's: leave the figures as decided, but make the sentence in 6.9 and 6.10 state the paper's own rule and that under it the waste row is a setting, in one clause, so the text does not contradict itself; the digest asks Murray whether the span changes. Report the exact sentences.
- **Overclaims:** 9.1 (relaxing the pairing reaches 93% of footprint build 3 and stays below 117.0); 7.3 ("spans most of": under half on a log scale); 7.5 (HALF "reproduced closely" is "partly reproduced"); the Cassidy crop count (22 against 21) and all-cropland reading (183 against 190) made one figure from the file.
- **B276:** the register's pending value for the input factors is 0.59 and Table 5 prints 0.62: find which the file supports (`analysis/method_tests_2025/harmonised_comparison_lines.csv` or the README) and use it; report which, for the register job.
- **"54% lower"** in 5.8: derive it in the claims row from the two printed figures, or cut it.
- **Citations:** every work cited in prose is in the claims csv citation list (Centre for Population 2026; Schön and Böhringer 2023; the others the read lists); the 7 uncited entries drop from the lists; "Li et al. 2018" cited under the right first author (check `qa/references.csv`; if the register has it under Yi, say which is right from the file in the archive and report it for the register job).
- **Prose labels:** "reported in" out of prose (9 places; the claims csv carries it); internal labels "decision 57", "V05", "V42" out of the supplement (say what was done in plain words: "a blind check" and the like); time words "still", "yet", "on hold", "earlier" removed or tied to a date.
- **The declaration:** insert the short generative-AI declaration from `papers/DECLARATIONS.md` as the journal's section after the conclusions, with Murray's unfilled points (model versions) left as bracketed placeholders, and competing interests, funding and CRediT after it.
- **Highlight 5** at 85 characters: shorten to at most 80.
- **references.md em dash** (Reutter 2017 title): that is `qa/references.csv`; report it for the register job.
- **B119 labels:** take the "not seen" label off the 20 claims rows B119 section 9 lists for Paper B (file and row given there); leave the 4 that stay.
- **"Burnside bin audit 2022"** in prose: the author is Rawtec (B119); fix the citation.

Then `python3 qa/tools/assemble_draft.py B` on a scratch copy and `python3 qa/tools/wordcount.py B`: at most 7,950; abstract at most 250. Report both.

Report: every V45b fail with its fix or its stand; the sentences changed (before; after); the analysis files needing regeneration; the register rows for the register job (B276 value; Li/Yi; Reutter title); the word counts; "Wrong-value check:" with one cell deliberately copied from a builder report and caught against the file, marked as an example.
