# B129: Paper B patched for decisions 122 to 129 and the widened improved range (B130)

Brief: `qa/briefs/B129_patch_paper_B_gate5.md`. No git, no subagents, no network. Written under `papers/B_methods/` and this report only. `paper_B_draft1.md`, `references.md`, registers and `analysis/` untouched. Every B130 figure is labelled "checker pending V46" in the claims rows.

## 1. Outcome

* Word counts (`assemble_draft.py B` then `wordcount.py B` on a scratch copy): 1: 709, 2: 574, 3: 320, 4: 1120, 5: 2231, 6: 1316, 7: 682, 8: 538, 9: 426. **TOTAL 7916** (limit 7,950; it was 7,945). Abstract **249** (limit 250). Highlights 74, 82, 82, 76 and 79 characters (limit 85).
* No em dash in any file I wrote or changed.

## 2. Sentences changed (before; after)

**Decision 125, improved range**
* Table 3 caption. Before: "The corrected model's range (31.1 to 49.2; 19 settings, 2,000 draws) is from `results/ranges_2025-fixed_wide.csv`; `cross_method.csv` prints the 13-setting range, 36.3 to 45.8, and needs regenerating. ... The model's improved range (46.2 to 60.1) is from the 13-setting Monte Carlo, not rerun." After: "Both model ranges are the widened ones, 2,000 draws each: corrected 31.1 to 49.2 (19 settings, ...) and improved 37.9 to 60.0 (18 settings, `results/ranges_2025-improved_wide.csv`), as `cross_method.csv` prints them." and "`cross_method_local.csv` still prints the earlier 13-setting improved range and needs regenerating." (The first sentence was stale: `cross_method.csv`, `model_entry.csv` and `design_choices.csv` were regenerated and now print 31.1 to 49.2.)
* Table 3 row "The model, improved": 53.6 (46.2 to 60.1) becomes 53.6 (37.9 to 60.0).
* Table 4 caption. Before: "...prints the 13-setting range for the corrected row ... and needs regenerating. The corrected row carries the widened range ...; the mirror and improved rows keep a 13-setting range of 1,000 draws ..." After: the corrected and improved rows carry the widened range (2,000 draws; 19 and 18 settings, section S5); the mirror row keeps its 13-setting range of 1,000 draws.
* Table 4 improved row: 53.6 (46.2 to 60.1) and 18.5 (15.9 to 19.4) become 53.6 (37.9 to 60.0) and 18.5 (15.7 to 22.1).
* S5, paragraph 2. Before: "The mirror and improved releases keep an analysis of 1,000 draws of 13 settings, run before six settings were added, which was not rerun." After: the improved release "was drawn the same way, 2,000 times over 18 settings, 40,000 runs in all with the runs for the indices: the Australian loss-factor weight has no meaning there, because the release already applies the Australian factors, and the other 18 all vary. The mirror release keeps an analysis of 1,000 draws of 13 settings ..." This is the one place the "18 choices (loss-factor weight has no meaning)" statement is made.
* S5, after the Table S3a paragraph, added: "On the improved release the median of the draws, 48.1 million, also lies below the release's 53.6, which sits near the top of the meat-window and meat-calibration choices."
* Table S3 caption: now built from `ranges_2025-improved_wide.csv` and `sobol_2025-improved.csv`. Rows 7 and 8: "2025-improved, 13 settings: 46.2 to 60.1 / 15.9 to 19.4 (shares 0.786 ...)" become "18 settings, 2,000 draws: 37.9 to 60.0 (32.0 to 69.5), base 53.6, land source 0.33 (0.35); meat window 0.30 (0.30); energy requirement 0.22 (0.25); red-meat share 0.06 (0.06)" and "15.7 to 22.1 (15.1 to 23.0), base 18.5, land source 0.63 (0.66); resilience table 0.20 (0.20); meat window 0.14 (0.15)". Shares from `sobol_2025-improved.csv`, rounded to two places as the corrected rows are.
* B157's sentence ("the improved range contains none of the reference points") is **not in Paper B** (it is in the sensitivity README "What the comparison shows"). Nothing to rewrite in the paper. Replacement text for the README and register: "The improved widened range (37.9 to 60.0) contains the 41.5 average-year point and the meat readings of 40 to 41, and excludes the 1-in-10 point (30.8); the long-term 18.9 lies inside 15.7 to 22.1."
* "Every range is the widened one": true for Tables 3, 4 (corrected, improved) and S3 headline rows, but **not for the mirror row**: no widened mirror run exists, so Table 4's caption says the mirror row keeps its 13-setting range. Table S3 keeps the mirror and corrected 13-setting rows as labelled comparison rows.

**Decision 124, variant 3 out**
* 5.14 para 1. Before: "relaxed ... in three ways (Table 7)." After: "in two ways (Table 7); a third, stronger relaxation is reported in the repository." (the one clause). The sentence defining variant 3 is cut.
* 5.14 para 2. "Variants 2 and 3 pass all three readings but also change the diet" becomes "Variant 2 passes all three readings but also changes the diet"; "Variant 3 reads 172.3." cut; "and variants 2 and 3 test the fixed diet" becomes "and variant 2 tests the fixed diet".
* Table 7 row 4 (172.31) deleted. S3.12: the variant 3 sentence cut. OUTLINE and SECTION_SCOPE lines that gave 172.31 or "three ways" updated.

**Decision 127.** Table S3a row 4 source: "ABS 7215.0 against the archive" becomes "ABS 7215.0, December 2010 issue (ABS 2011), against the archive" (L253).

**Decision 128.** Checked every statement of fidelity (5.2, 5.4 to 5.6, Table 3, S3.9, Table S6, 9.1): Cassidy people per hectare "not reproduced", delivered shares "partly". B126b had done it; no remnant.

**Decisions 122, 123, 129.** Checked: abstract, 6.9, 6.10, 9.2 and highlight 5 read "weather and waste ... 18.9 to 55.3"; keywords read "ecological footprint; sensitivity analysis". No remnant of "by definition alone" or the old keywords in the paper (the phrase survives only in a drafter flag, line 200 of `B_s06-09.md`, not for the paper).

**Table S7 (item 6).** Cells 182.2 and 324.8 become 182.3 and 324.3 (`intake_variant.csv`); the multiple for HALF 7.83 becomes 7.82 (the csv's 7.82); the caption sentence about the blind check's figures replaced by "as the csv prints them". The 5.13 prose "182.2 (protein)" and "HALF 324.8" become 182.3 and 324.3.

**Citations (item 7).** S8 prose (supplementary line 372): "Department of Climate Change, Energy, the Environment and Water 2017 / 2019 / n.d." becomes "DCCEEW 2017 / 2019 / n.d.", with the first mention "The Department of Climate Change, Energy, the Environment and Water (DCCEEW) sets Australia's own goal as ...". These match the renamed L230, L231, L242. "CSIRO and University of Queensland 2025" in the prose already matches L010 ("CSIRO and University of Queensland, 2025"): confirmed, no change. **Higgins: Paper B does not cite Higgins anywhere** (no L172 or L173 in any Paper B claims csv or prose); nothing to drop. The `make_references.py` and A-side edits in B127's list stay for the reference job.

## 3. Claims rows changed or removed

`B_s04-05_claims.csv`
* Changed: line 94 (Table 4 row 4, short), line 95 (long), line 225 (Table 3 row 9), line 217 (Table 4 caption), lines 182 and 184 (Table S7 values cited to the csv). Rows 94, 95, 225 cite `results/ranges_2025-improved_wide.csv`, `model_entry.csv` or `cross_method.csv`, and carry "checker pending V46".
* Removed (variant 3): lines 197 ("Variant 3 reads 172.3"), 200 ("eleven food groups"), 201 ("at most three times"), 214 (Table 7 row 4).
* Added: Table 3 note (both ranges widened, pending V46); Table 3 note (`cross_method_local.csv` stale); 5.14 clause (README pointer, no figure).

`supplementary_claims.csv`
* Changed: lines 276 and 283 (Table S7, csv values), 309 and 310 (Table S3 rows 7 and 8, with the sobol shares; pending V46), 314 (S3a row 4 names the December 2010 issue, L253), 118 to 120 (flag: cited as DCCEEW).
* Added: S5 rows for "2,000 times over 18 settings, 40,000 runs", "loss-factor weight has no meaning", and "median 48.1 below 53.6" (all pending V46).

## 4. Register rows to change

* **B157** (text of the containment sentence): as in section 2 above; the old sentence is in the README only.
* **B114** (improved short-term range 46.2 to 60.1): 37.9 to 60.0, pending V46.
* **B115** (improved long term 15.9 to 19.4): 15.7 to 22.1, pending V46.
* **B159** (cross-method improved entry "53.6 (46.2 to 60.1)"): 53.6 (37.9 to 60.0); `cross_method.csv` already prints it. Pending V46.
* Also: `cross_method_local.csv` row "The model, improved" (and `harmonised_lines.py` line 152, which hard-codes "13-choice") still print 46.2 to 60.1; regenerate. The README sentence for "What the comparison shows" needs the rewrite above.

## 5. Decisions or flags for the coordinator

* Mirror row stays 13-setting (no widened mirror run). If Murray wants "every range widened" literally, a mirror rerun is needed.
* The Table S3 rows keep the mirror and corrected 13-setting comparison rows; drop them if "one kind of range" is meant for the whole table.
* I added 40,000 runs and "all 18 vary" from B130 in S5; both are pending V46.

## Wrong-value check:

Check script (scratchpad `chk.py`) reads `results/ranges_2025-improved_wide.csv` (rows `variant=wide`: p5 and p95 give 37.9 to 60.0 short and 15.7 to 22.1 long) and compares every range on an "improved" table row in `B_s04-05.md` and `supplementary.md`.

* On the real files: 0 mismatches.
* **Example of a deliberate wrong value** (a scratch copy, not the paper): the 13-choice range left in the Table 4 improved cell, "53.6 (46.2 to 60.1)". Result: `MISMATCH B_s04-05.md 140 46.2 to 60.1`, 1 mismatch, caught.

## Changed files

* `papers/B_methods/draft/B_s04-05.md`
* `papers/B_methods/draft/B_s04-05_claims.csv`
* `papers/B_methods/draft/supplementary.md`
* `papers/B_methods/draft/supplementary_claims.csv`
* `papers/B_methods/OUTLINE.md`
* `papers/B_methods/SECTION_SCOPE.md`
* `qa/reports/B129_patch_paper_B_gate5.md`
