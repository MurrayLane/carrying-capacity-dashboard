# B143b: patch of Paper B to the blind read V54b

Brief: `qa/briefs/B143b_patch_paper_B_to_V54b.md`, with the coordinator's addition (six sentences from the response letter). No git, no subagents, no network. Written under `papers/B_methods/` and this report only. Not touched: `paper_B_draft1.md` (stale, needs `python3 qa/tools/assemble_draft.py B`), `references.md`, registers, `analysis/`.

## Counts

* `python3 qa/tools/wordcount.py B` on a scratch copy: sections 730, 519, 295, 885, 2705, 1329, 594, 478, 404; TOTAL 7,939 (cap 7,950).
* Abstract: 249 words (cap 250).
* Highlights: 76, 84, 82, 85, 77 characters (cap 85).
* My re-run of the V54b trace over the assembled scratch draft (2,509 numbers): all 2,509 have a claims row whose named file, register row, literature row or "derived:" arithmetic carries the number. Table-cell check against the csv each caption names: every cell matches except three documented derived cells (Table S11 binding-land multiples 1.30, 1.88, 1.01; the "about 183" in Tables S3 and S10, which is 5.78 x 31.65).
* Highlights: 10 rows in `highlights_claims.csv`, every number matched to its file.
* Claims rows now: 88, 241, 106, 373. Rows carrying "derived:" arithmetic: 1, 1, 1, 4 (the arithmetic is evaluated by my trace).

## Wrong-value check (EXAMPLE only, not in any repository file)

On a scratch copy of the supplement I left one Table S6 cell stale (grain with embodied feed grain, supply basis 126.6 in place of 126.8; Table S6 is the old Table S7). Checked against `analysis/method_tests_2025/intake_variant.csv` the cell returned `(257, '126.6')` unmatched; the published file returned no unmatched cell.

## V54b fails, in order, with the fix or the stand

Values the file contradicts (15)
1. Table S7 (now S6): meat 41.3 (0.99), 48.3 (1.16), 58.4 (1.41); fish 12.1 (0.29), 19.8 (0.48), 18.0 (0.43); grain 126.8 (3.05), 137.3 (3.31), 138.2 (3.33), each retyped from `intake_variant.csv`. Table 5 note now says 126.8. The claims rows for these cells and S3/54, S3/67 carry "pending: check of the rerun": V42 checked the old values, so the rerun needs a check (checker job).
2. Table S5 (now S10) and S3.8: 2021-23 mean head count, 26.2 million (`bases.csv`); the 26.08 clause is gone.
3. Table S8 (now S11) binding-land-type row: caption says its multiples are `harmonised_robustness_footprint.csv` 53.9 and 77.9 over 41.5 and 53.6; the claims row gives the arithmetic as "derived". Stands as derived, not a csv cell.

Row whose file does not print the number (10): 14.75 (row now cites `README_round2_B139.md` and 3,525 x 4.184 / 1000); 34.5 (`bridge_half_to_model.csv`, -34.46); 28, 46, 87, 10, 16 (`harmonised_robustness.csv`, `harmonised_line_c.csv`); 40.4 (`drought_bounds_paper_B.csv`); 331.87 (`bases.csv`).

No claims row (88): every number has a row. Highlights: new `highlights_claims.csv`. Unit conversions: 11.3 MJ cites `bases.csv`; 10.7 MJ is "derived: 2,550 x 4.184 / 1000"; 1,912 kcal likewise. S2.4, S2.9 (register rows L136, L083), S3.6, S3.7, S3.11, S3.12, S3.14, S4, S7, S8: rows added citing the file that prints them (`drought_bounds_paper_B.csv`, `gap_attribution_readable.csv`, `harmonised_robustness.csv`, `harmonised_line_c.csv`, `README_round2_B139.md`, `bridge_half_to_model.csv`, `production_window_10y.csv`, `diet_land.csv`, `energy_exports.csv`). "UN Target 12.3" is a name, with a row saying so. Jones's 30 to 35 in 6.6 has its own row.

Checker-wording: item 1 is fail 1 above. Item 3 (diet A 1.60 against Monte Carlo 1.58, a hundredth) stands: unrounded 1.593 against 1.583, as V53 states.

Logic fails
1. Ranges on one basis: abstract, section 1, 5.11 and 9.1 give line (a) and line (b) to the model at 41.5 across variants (-1% to 7%, 28% to 46%) and across the four model values 31.1, 41.5, 49.2, 53.6 (-1% to 8%, 23% to 53%). I recomputed all four from `harmonised_robustness.csv` (core variants).
2. 5.10: "its 1-in-10 point with the factor on every yield, 30.8 million, lies just below the corrected range of 31.1 to 49.2 million; with the factor on crops only it is 41.2, inside it."
3. 7.3: "one model run under the choices of section 6 other than diet spans 15.5 to 62.9 million, the optimised diets reach 202.1 and 422.3, and a proportional count of exports reaches the published 100 million". Checked: 15.5 and 62.9 are the lowest and highest single-choice rows of Table 8 panel A outside diet.
4. Abstract and highlight 4: "relaxing the pasture-crop pairing alone closes it (not shown to be the only cause)"; highlight 4 is "The pasture-crop pairing is enough to close the gap to HALF, not shown the only cause" (85 characters).
5. 6.10 and 9.2: the spread across settings (1.58) is compared with the drought allowance alone (2.19) and waste alone (1.33).
6. 5.4: "not reproduced, graded on the printed rates".

Consistency fails
1. As fail 1. 2. Table 3 commodity cell: "the 30 to 32 and 76 to 80 readings of Table 1 are derived here".
3. **Stands: Table 2 and Figures 1 to 3 are placeholders.** Table 2 needs a catalogue csv; Figures 1 to 3 need plotting scripts and data (`cross_method.csv`, `harmonised_comparison.csv`, `design_choices_panels.csv`). Both are `analysis/` work outside this job's write scope.
4. Supplementary tables renumbered by one script over the four section files, the claims csvs and the intro line, in order of first citation (main text first, then supplement), with a check that all 15 captions are defined once and every citation resolves. Map, old to new: S11 to S1, S6 to S2, S10 to S3, S3 to S4, S13 to S5, S7 to S6, S14 to S7, S1 to S8, S4 to S9, S5 to S10, S8 to S11, S12 to S12, S2 to S13, S3a to S14, S9 to S15. Alexander et al.'s own "Table S5" in 5.5 is not ours and is unchanged. The tables now sit in the file in non-monotonic order (the price of numbering by citation). Drafter notes keep their old numbers on purpose.
5. S3.7: "Cassidy's rows in Table S8 (22% to 37%)". 6. Table 5 caption names `drought_bounds_paper_B.csv`.
7. Internal labels out of captions and prose (Tables 6, 7, 8, S4, S5, S7, S11, S12 and S3.6, S3.11, S3.12, S3.14, S4, S7, S8): "B139, checked V53", "decision 113", "V19", "builder" and the like; the claims csvs carry them. Table 8 panel C's "Register" column (L-numbers) became "How the source was read".

Citations and references
* Beltran-Peña 2020: its only claims row (supplementary S2/37) was a superseded row and is retired, so the list drops it. A scratch rebuild with `make_references.py B` from my final csvs equals the `references.md` now in the folder (which I did not write): 128 entries, Beltran-Peña out.
* Borrie: Table 1 rows carry L004 and L006; the entry "National Population Inquiry, 1975" is in the list.
* "Saltelli et al. (2010)", "Muth et al. 2011", "Australian Bureau of Statistics 2011", "Food Innovation Australia Limited 2021", "National Health and Medical Research Council (2006)" (NHMRC defined), "USDA 1992, Handbook 697", "Nix's estimate (n.d.)", "AUSNUT (2007)" as the entries print them.
* "Name Year" as sentence subject became "Name (Year)" in sections 4, 5, S2, S3 (about 60 places); bare forms inside parentheses and in table cells stand (house form for those).
* Stands, register job: the 29 [CHECK] notes in `references.md`; the Schön and Böhringer entry (see list below).

Journal checks: counts above; no em dash in any file I wrote (scan of the folder); the undated "current" and "today's" are tied to 2021-23, the 2025 FAOSTAT revision, or "the observed diet".

Lost-reader places: 5.9 gives the ten ERRATA errors in one clause (Paper A section 2, `ERRATA.md`), the two that reach 2025 (beef carcase-to-retail 1.0; doubled oil content in the biodiesel yield) and their effect (49.4 to 41.5 short term, 14.1 to 15.6 long term). Defined at first use: SA2 (6.7), PAL (Table 8, S5), DSE (S5), evaluator (S3.11), zone 1 (Tables S4, S13), mirror release (Table 4 caption). The share closed is glossed in the abstract and section 1.

## Coordinator's six additions (response letter, R07b)

1. 5.11: "A method's centre is the geometric mean of its paired readings."
2. S3.11: fish dropped gives 5.9% (line a) and 40.9% (line b) to 41.5 (`harmonised_robustness.csv`, checked).
3. S2.5: the accounts' own Australian reading is not used because the public release has no Australian row and the licensed data were not sought.
4. S3.14: only the model was rescaled; the other methods' output-scaled readings were not rerun on the ten-year window.
5. 3.1: "The selection record holds no counts by route."
6. 5.2: "The authors had not been consulted at the time of writing." Its claims row (5/B143b-12) is an open decision row: Murray resolves it, with the bracketed note in the letter (Mod M6), when the requests go out.
Table numbers the letter cites (2 to 4, 6 to 9; the letter has no Table 5 or 1 beyond "Tables 3 and 5") match the final text: 3 readings and fidelity, 4 model entry, 6 three-line comparison, 7 pairing and bridge, 8 design choices (panel B holds 4.29, 2.06, 2.47), 9 ratings, Table 2 placeholder. The letter cites the supplement by section, so the renumbering does not touch it. Word cost: added about 40 words, offset by cuts (the 5.11 clause on spread within methods, 6.8's first sentence, earlier trims).

## Sentences changed (main text)

Abstract (rewritten); 1 (first paragraph pointer; closing paragraph); 3.1 (selection record); 4.5 (Wackernagel 1999 sentence cut); 4 and 5 ("Name (Year)"); 5.1 (ABS parenthesis cut; signpost cut); 5.2 (consulted); 5.4, 5.5 ("2021-23 yields", "2025 FAOSTAT revision", printed rates, NZ numbers cut); 5.9 (errors); 5.10 (last sentence); 5.11 (ranges; centre; export-ratio sentence shortened; per-method clause cut); 5.12, 5.13 (shortened); 5.14 (binding-type sentence shortened); 6.4 (Nix n.d.); 6.7 (SA2); 6.8 (first sentence cut); 6.9 (pasture swing cut); 6.10, 9.2 (comparison); 6.11 ("an illustration, not a bound"); 7.1, 7.3, 7.6; 8.2, 8.5, 8.6; 9.1. Captions of Tables 3 to 8; supplementary S3.1, S3.3, S3.4, S3.6, S3.7, S3.8, S3.9, S3.10, S3.11, S3.12, S3.13, S3.14, S4, S5, S7 (labels, citations, "current"), Tables S3, S6, S8, S10, S11, S13 and S14 (old S10, S7, S1, S5, S8, S2, S3a).

## Register job (not done here)

Tier A rows whose register value or statement differs from the paper (supporting report and checker):
| Row | Paper prints | Support |
|---|---|---|
| B276 | line (a) -1% to 7% / -1% to 8%; line (b) 28% to 46% / 23% to 53%; base 4.1% and 38.5%; line (c) 14.7%, band 10% to 16% | B135, V50; B139, V53 |
| B277 | narrowing about a third with the commodity-balance caveat; line (c) 0.65 to 0.48 | B135, V50; B139, V53 |
| B156 | counterfactual 146 to 343 and HALF 276, about 3.5 to 8 times | B046; B123, V44; B141b |
| B003 | two one-at-a-time changes, 40.4 on crops only, 62.9 improved, "not a joint range" | B134, V49 (decision 146) |
| B194 | crop-only bound (1.03) and land base (1.09) move it least | B134, V49; B139, V53 |
| B187 | 1.58 with the 2.22 dropped (B188 carries the same 2.22) | B141b |
| B005 | 9.4 to 100 without the factor 10.6 | B141b |
| B130 | 5.8 to 6.1%, "short-term", "below 1% on crops alone" | B134, V49 |
| B137 | 18.92 to 41.5 plus 41.2 and 40.4 on crops only | B134, V49 |
Also: B242 (Tier C, counts seven methods; the paper says five plus the model read two ways); Borrie (L004: identity of the work rests on footnote 12 of the Jones report, no copy of the inquiry report; entry reads "National Population Inquiry, 1975"); Schön and Böhringer 2023 (entry "Schon, Bohringer, 2023" lacks umlauts and initials; prose has "Schön and Böhringer (2023)").

## What each protected file needs

* `paper_B_draft1.md`: reassemble. The assemble tool's header still says sentences marked [gate 4] use unapproved values; no csv carries that flag now (tool text, `qa/tools/`).
* `references.md`: already matches my csvs; [CHECK] notes and the two entries above remain.
* `analysis/method_tests_2025/cross_method.csv` and `cross_method_local.csv`: column header "on current data"; the commodity-balance fidelity cell ("30 and 77 readings reproduced") and the Cassidy fidelity cell are worded differently from Table 3; `bases.csv` prints "Muth 2011" where the paper has "Muth et al. 2011".
* Checker job: the rerun commodity-balance values (Tables S6, S10 rows) against V42.
* Open decision row for Murray: sections 6.2 and 6.3 headed as definitions while 6.9 calls waste and the Australian settings settings (claims row 6.9 sentence 3); the 5.2 consultation sentence.

## Changed files

`papers/B_methods/draft/`: `B_s01-03.md`, `B_s04-05.md`, `B_s06-09.md`, `supplementary.md`, `highlights.md`, `B_s01-03_claims.csv`, `B_s04-05_claims.csv`, `B_s06-09_claims.csv`, `supplementary_claims.csv`, new `highlights_claims.csv`; `papers/B_methods/OUTLINE.md` (item 7 added, one table number corrected); this report. Drafter notes in the three section files carry a B143b paragraph.

Register rows touched: none.
