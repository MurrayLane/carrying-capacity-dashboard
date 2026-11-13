# B89: merge of the claim checks V31a to V31e into the claims register (decision 83)

Files written: `qa/claims_register.csv`, `qa/defects.csv`, this report. No git, no network, no subagents. Inputs: `qa/reports/V31a_claims.md` to `V31e_claims.md`.

## Tally (209 claim ids, all tier B or C)

| Result | Rows |
|---|---|
| Pass (plain: "independently verified (V31x, 2026-11-13)") | 128 |
| Pass with a note ("independently verified with notes ...") | 57 |
| Corrected after a fail ("independently verified after correction ...") | 18 |
| Unverified (cannot determine) | 5 |
| Withdrawn, left withdrawn (B037) | 1 |

Total 209. The 57 with notes are the 55 checker "pass with a note" rows (56 less B045, which V31e fails), plus B052 (V31a "pass", but its register note held a stale rebuild figure, so the correction is recorded), plus B161 (read in this task, see below).

Counts by report: V31a 53, V31b 44, V31c 40, V31d 54, V31e 18. A321 and B045 appear in two reports (A321 in V31d and V31e, B045 in V31a and V31e); each is counted once. A321 is filed under V31d and B045 under V31e.

## Corrected rows (id: before; after)

* A064: "193,162 to 2,413; 9 to 356 times" (published method); "170,101 to 2,125; 10 to 349 times" (corrected method). Output file and locator set to `capacity_by_cause_corrected.csv`, Swan, short term.
* A276: "Nothing but diet and waste moves the short term by more than 10%"; "Nothing but diet, waste and a 20% rise in livestock output moves the short term by more than 10%". Locator and note figures +19.2% to +19.4%, +9.6% to +9.7%, all yields +10.0%.
* A321: South Australia 0.36 and Western Australia 0.49; 0.35 and 0.47. Locator moved to the "data: ABS to 2024-25" rows of tables.csv (0.36 and 0.49 were the thesis archive rows).
* A323: "cuts the 2025 long-term figure to 9.7 million"; "(0.0023 to 1, other settings short term) cuts the 2025 short-term figure from 41.5 to 9.7 million".
* A324 (not named in the brief; a fail in the V31d table, so corrected to the checker's wording): "unused pasture (1.8 million km2 excess)"; "Pasture is fully used (need 3.49 million km2 against 3.32 held, short term); the unused land is 1.96 million km2 of non-agricultural land; cropland +25% at the pasture's expense leaves capacity unchanged". Value 1.8 to 1.96.
* A327: livestock output (+20%) added to the long-term list with the weather allowance, grain store and diet changes; the short-term list now marks livestock output as the +20% step.
* B045: "17.38 and 445.4 Mha in 1991-92"; "... in 1991". Values unchanged (they are the FAOSTAT 1991 rows; the 1991-92 means 16.89 and 447.5 are in the note). I used the 1991 label because the script reads 1991 only.
* B047: "a fifth to a third of the food row"; "about a sixth of the food row (16%)".
* B061: "70 of 90 commodities"; "66 of 90" with the left-out list (24 items: alcoholic and fermented beverages and wine; cocoa, coffee, tea; pimento and other spices; fish; animal fats; nine oilseed cakes; cotton lint, seed cotton, molasses, ricebran oil, oil palm fruit). Beer is included; offals are not among the 90.
* B079: "21 crops"; "22 crop items" (value "22; 1,061").
* B122: "2,500 kcal in the text, 2,550 in a figure caption"; "2,550 kcal a person a day" (English original, L042, p. 352 and p. 353; the 2,500 is in the Spanish translation only).
* B166: "41 to 49 million" and "fruit, vegetables and dairy are not exported"; "41 to 54 million (corrected and improved)" and "exported far less (11% to 26% of production) than wheat and beef (67% to 78%)".
* B199: "22 to 25 at 50 years and 19 to 21 at 100"; "23 to 30 at 50 years and 19 to 25 at 100".
* B225: "49.7 improved"; "58.3 improved".
* B232: "Gifford doubled cropland"; "Gifford scaled intensive land from 40.5 to 70 Mha, a factor of 1.73, as Henry and Godden report".
* B239: "HALF o, PPH o"; "HALF partly, PPH partly".
* B240: "FP o"; "FP partly".
* B242: "three planning-oriented studies" (value "7; 3"); "four" (value "7; 4").

B037 is not corrected: its status stays "withdrawn (X044 ...)" and a note records that the arithmetic gives 0.300 (0.299 unrounded), not 0.298, and that no equivalence factor is supported.

## Pass with a note: register edits made beyond the status

A315 (4.65 to 4.66 in statement and value); B052 (note's rebuild 34.07 (+1.0%) to 34.37 (-2.2%)); A303 (release_or_data to "2025-mirror (published-method base)"); A316 (locator and note: exact factor 0.7424 gives 3.45); A051 and A052 (unit to "ratio"); B204 (unit to "million people; Mha", locator 53.5 to 53.6); A341 (unit to "share of meat"); A273 (locator to the exact ratios); A062 (locator and note: median 0.91 on the corrected tier); A071 (note records the chosen set); A277 (note: the waste-at-target cell agrees); A320 (locator and sources set to the food balance, D17 only); B143 (release_or_data to the ABS 1997-98 production); B158 (statement reworded to "On 2025 data the improved tier raises the model's own national readings by about 12 million ... and 3"). All other pass-with-note rows carry the checker's note in the status and the notes column only.

Left as suggestions in the notes, statement and value unchanged, because the checker offered alternatives or a rounding preference and the statement quotes a document: B144 (fish 25 against 24), B198 ("41" against "41.5"), B249 ("within 2.1%" against 2.2%), B253 (wording for 2025-improved), A134 ("about half" against +62%), B080 (US maize). A275 is a plain pass: its row already reads +9.7%; the +9.6% and +19.2% figures were in A276's note and are corrected there.

## Unverified

* A317: build_years.py fails at 2016-17 on the current livestock series (V31d).
* A113: rejected method not committed; 33 confirmed, 77 not reproduced, nearest reconstruction 73.0 (V31d).
* B163: no NFF or industry source found; nearest is PMSEIC 2010 (V31b).
* B196, B197: Jones committee report (L006) not on disk (V31b).

B161 was read in this task. The L009 file is now the right article (sha256 f8004487..., title "How many people can Australia feed?"). It prints "our exports feed (at least in part) 36.6 million people outside Australia. If we add that to our domestic population, 61 million people will eat Australian food in 2017". The row is set to pass with notes (V31a): 61 and 36.6 confirmed; it is a web article with no page numbers; the 24.4 million domestic population is not printed (61 - 36.6 = 24.4).

## Tier A

No tier A row is in the 209. A019 (tier A, status "independently verified") is named in the brief's fail bullet ("A019 cites L012 for 40,450,144"). Because the instruction to me says no tier A row is in scope, I left A019 untouched. The finding, from V31e: A019 carries 40.45 million (correct for 2011-corrected and the 2014 article, L012), but names L020 (the thesis) as method source, and the thesis prints 40,439,187. The change, for the caller to decide: cite L012 for 40,450,144. B229 holds at whole millions either way.

## Defects added (defects.csv, ids X116 to X122, dated 2026-11-13)

* X116: movers.csv mixes corrected-method and published-method values in one table (V31c; claims A062, A064).
* X117: Cassidy test pairs food-balance production with crops-file area across the one-year winter-crop lag, about 6% on the Australian figure; rerun needed, decision for Murray (V31a; B085, B258).
* X118: build_years.py and livestock_zone.py cannot rebuild years.csv (V31d; A317).
* X119: rejected 77 million method not in the repository (V31d; A113).
* X120: Jones committee report not on disk (V31b; B196, B197).
* X121: NFF figure untraced (V31b; B163).
* X122: Section 7 matrix rows 2 and 3: the register claims were out of date. SECTION7_DRAFT.md rows 2 and 3 read partly for HALF, PPH (row 2) and FP (row 3), which is what B79 (decision 69) set. The draft is current; the claims were stale; fixed in B89 by correcting B239 and B240.

Existing defects X109 (A321) and X110 (B045) are now resolved by the corrections above; I did not edit those rows.

## Parse and count checks

* claims_register.csv: parses with the csv module, 698 lines (header and 697 rows), every row 18 columns, same as before. Every line ends CRLF (698 CRLF, no bare LF), as before. No em dash or en dash. The count of non-ASCII characters is unchanged (12).
* Untouched rows: the 488 rows outside the 209 ids are byte-identical (checked line by line against the original; only the 209 target lines differ). A019 is among the untouched.
* defects.csv: 115 lines before, 122 after (7 appended, ids X116 to X122), every row 8 columns, CRLF, no em dash. The first 115 lines are unchanged.
* Every replacement in the register was made by exact-text match and asserted to occur once; every id in the five summary tables was matched to a register row (209 of 209).

## Register rows touched

All 209 ids (each gets a new status and verifier_report): the 128 plain passes by status and verifier_report only; the other 81 also in notes, and in the fields named above. `last_verified_commit` is unchanged on every row (no git).

Wrong-value check: example of a correction that would itself be wrong (EXAMPLE ONLY, not applied): setting B225's improved figure to 53.6 instead of 58.3. 53.6 is the improved release at its default cropland; the doubled-cropland run, which B225 names, gives 58.3 (V31e own run 58.314; rerun.csv R2 58.31).

## Other observations (not edited)

* `analysis/method_tests_2025/README.md` line 199 repeats "Australia's 21 crops" (B079; Australia has 19 with production).
* V31a: `foran_poldy_balance.py` divides 2021-23 use by the 2021-22 mean population (this is why fish reads 25, not 24); X102 already records it.
* V31a notes the FAOSTAT year lag (food balance winter crops one year late); X111 already records the question, X117 records the Cassidy consequence.
