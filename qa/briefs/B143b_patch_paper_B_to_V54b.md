# Builder brief B143b: patch Paper B to the blind read V54b

Rules: plain language; no em dashes anywhere; no time words. No git; no subagents; no network. Write only under `papers/B_methods/` (section files, claims csvs, a new `highlights_claims.csv`, `supplementary.md`, `highlights.md`, `SECTION_SCOPE.md`, `OUTLINE.md`) and `qa/reports/B143b_patch_paper_B_to_V54b.md`. Do not touch `paper_B_draft1.md`, `references.md`, any register, or `analysis/` (list what each needs).

Input: `qa/reports/V54b_read_paper_B.md`. Work every fail it lists, in its order; for each, the fix or why it stands (with the file and line that supports the current text). In particular:
- **Table S7 and the Table 5 note:** every commodity-balance cell from `analysis/method_tests_2025/intake_variant.csv` as it now stands (meat 41.3/48.3/58.4; fish 12.1/19.8/18.0; grain 126.8/137.3/138.2); Table S5 and S3.8 say the 2021-23 mean head count 26.2 million (`bases.csv`).
- **Ranges on one basis:** the abstract, section 1 and 9.1 give line (a) and line (b) on the same basis (to the model 41.5 across variants: about -1% to 7% and 28% to 46%; across model references: -1% to 8% and 23% to 53%), saying which once; the V54b rewrite is acceptable.
- **5.10:** 41.2 on crops only is not "below the range"; rewrite. **7.3:** "spans 15.5 to 62.9 million" names the definitions only, with the diet runs (202.1, 422.3) named as diets.
- **Highlights:** a `highlights_claims.csv` with one row per highlight number, as Paper A has.
- **The 88 numbers with no claims row and the 25 with a wrong or missing file:** a row for each (the report lists them), citing the file that prints the number; where no file prints it, the row says "derived" with the arithmetic or the sentence is cut.
- **Flagged rows:** the 199 rows carrying "restate or retire", "open", "gate 4" or "register-change" flags: resolve each (retire the superseded fragment, or update the flag to the current state), so the csvs carry only live rows.
- **Internal labels:** "B139, checked V53", "decision 113" and the like out of captions and prose (the claims csv carries them); undated "current" and "today's" tied to a year or removed.
- **Citations:** Beltran-Peña 2020 out of the lists if uncited; the Borrie 1975 inquiry gets a citation that the register can carry (list it for the register job); "Saltelli et al. (2010)", "Muth et al. 2011"; corporate authors cited as the entries print them (check `references.md`); "Name Year" as a sentence subject becomes "Name (Year)"; the Schön and Böhringer entry is the register job's (list it).
- **Lost-reader places:** one sentence each: what the thesis method's errors were (ERRATA errors 1 to 10 in one clause, pointing to Paper A); define evaluator, SA2, PAL and DSE at first use; define "share closed" where it first appears or move the abstract's use after a short gloss.
- **Supplementary table order:** renumber in order of first citation only if it can be done by a script over the four files and the claims csvs in one pass with a check that every reference still resolves; else leave and say so.

Then `python3 qa/tools/assemble_draft.py B` on a scratch copy and `python3 qa/tools/wordcount.py B`: at most 7,950; abstract at most 250. Report both.

Report: every V54b fail with its fix or its stand; the sentences changed; the register job's list (the 9 Tier A rows V54b names, with the supporting report and checker for each; Borrie; Schön); word counts; "Wrong-value check:" with one Table S7 cell deliberately left stale and caught against the csv, marked as an example.
