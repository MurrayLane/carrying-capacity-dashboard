# B95: the audit's register changes applied (B90, B91, B92a, B92b, B93; V33); Tier A values stay pending gate 4

Brief: `qa/briefs/B95_apply_audit_changes.md`. No git, no subagents, no network. V33 passed every B90 item it could check; its one undetermined item is the second ABS source (the 3218.0 cube, 98,642), which blocks no row, so every change B90 lists was applied under the Tier rule.

Files written: `qa/claims_register.csv`, `qa/defects.csv`, `analysis/method_tests_2025/make_readme_tables.py`, `analysis/method_tests_2025/README.md`, `papers/A_results/DISCUSSION_MEASURES.md` and this report.

## 1. Tier A rows marked pending (value and statement not changed)

Each row has "; pending gate 4 (2026-11-13): new value ..." added to `notes`, and `status` set to "independently verified; new value pending gate 4 (job)".

| Id | Current value | Pending value | Job |
|---|---|---|---|
| A029 | 23 | 22 (release 2011-fixed-2) | B90 |
| A033 | 23 to 16; 36 to 32 | 22 to 16; 36 to 32 | B90 |
| A034 | 9 (8 over to under, 1 under to over) | 8 (7 over to under, 1 under to over) | B90 |
| A036 | 3: Mackay Whitsunday; North Tasmania; North East Vic | 2: Mackay Whitsunday; North Tasmania | B90 |
| A164 | 23 | 22 | B90 |
| A165 | 82 | 81 | B90 |
| A199 | 5 (2025); 1 (2011) | 5 (2025); 2 (2011): Corangamite and North East Vic | B90 |
| A205 | -0.26% | -0.2% | B91 |
| A206 | -5.34%, 36 regions | -0.65%, 34 regions | B91 |
| A219 | 0%, release 2025-store-1 | 0%, release 2025-fixed (resilience table of 2025-store-1) | B91 |
| A220 | 48.27%, 27 regions | +48.45%, 25 regions | B91 |
| A223 | -0.3; -26 | -0.2; -26 (both 2025-fixed) | B91 |
| A264 | +48%; +64% | +48%; +64% (48.45 and 64.47 on 2025-fixed with the store tables) | B91 |
| A265 | 27.4 million, about 16 years | 23.2 million, about 16 years (16.1) | B91 |
| A266 | 30.4 million, about 10 years | 25.7 million, about 10 years (9.8) | B91 |
| B084 | about 190 million | about 183 million (harvest-matched) | B93 |
| B273 | 190 falls to 112.9 (factor 0.594) | 183 falls to 112.9 (factor 0.618); 112.9, 110.9, 0.766 unchanged | B93 |

Four more Tier A rows are marked pending because the scope rewrites need a change to their value or statement, and the rule bars changing either:

| Id | Current | Pending | Job |
|---|---|---|---|
| A196 | 0.89; 0.95 (capacity over population) | 1.12; 1.05 (people over capacity, the paper's ratio convention) | B92a |
| B156 | statement ends "read 12 to 41 million, the model's range" | statement ends "read 12 to 41 million." | B92b |
| B277 | "17 to 343 million as run, 12 to 343 harmonised" | "12 to 343 million as run, 12 to 343 harmonised" (the as-run low is fish on actual use, B151) | B92b |
| B083 | "Australia's 21 crops" | "Australia's 22 crop items" (B079, V31a) | B92b |

## 2. Tier B and C rows changed

Status is "self-checked (job, 2026-11-13)" unless noted. A note beginning "B95 2026-11-13 (from job)" records each change.

| Id | Tier | Before | After |
|---|---|---|---|
| A043 | B | 7 against 3; 4 against 1 | 6 against 2; 4 against 1 (V33 agrees) |
| A197 | B | 81-82; 85; 91 | 81; 85; 91 |
| A308 | B | 22; 23; 22 | 22; 22; 21 (V33 agrees; `method_status.csv` is not rerun, so its cells read 22, 23, 22 and the status says so) |
| A202 | B | 53.6; 18.5; 15; 36 (improved) | 41.5; 15.6; 16; 32 (2025-fixed) |
| A203 | B | -0.11% | -0.09% |
| A204 | B | -0.35%, 36 regions | -0.28%, 34 regions |
| A207 | B | 8.67% | 16.4% |
| A208 | B | -4.14%, 36 | -8.15%, 36 |
| A209 | B | 17.29% | 33.21% |
| A210 | B | 0%, 36 | 0%, 32 |
| A211 | B | -0.11% | 0% (not the same recycling measure) |
| A212 | B | -0.23%, 36 | -1.21%, 35 (not the same measure) |
| A213 | B | -0.06% | 1.7% (not the same measure) |
| A214 | B | -0.12%, 36 | -0.28%, 33 (not the same measure) |
| A216 | B | 0.98%, 35 | 0.78%, 31 |
| A218 | B | -18.75%, 37 | -1.83%, 37 |
| A222 | B | 64.21%, 25 | 64.47%, 25 |
| A224 | B | 36 to 27; 36 to 25 | 32 to 25; 32 to 25 (seven regions each) |
| A225 | B | locator "every other scenario under 20%"; note "+57%" | grain store +48.45% and +64.47% against every other scenario under 10% (largest waste-target-6, -8.15%); note "+60%" |
| A226 | B | 19 (fuel 340 takes 19% off) | "on the corrected release the CSIRO fuel scenario takes 1.8% off; on the improved release 18.8%, a method effect not yet explained" (value 1.8; 18.8) |
| A227 | B | -0.1; -0.1 to -0.2 | 0 to +1.7 short; -0.3 to -1.2 long (not the same measure) |
| A277 | C | table A restates measures.csv and the stores (improved) | table A has a Release column, stores on 2025-fixed, improved figures in brackets |
| A106 | B | "2015 finding (national 40, states 28, regions 23) survives" | corrected values 33.3; 25.7; 21.0 with the basis (regions on each zone's own yields); states are 25,677,412 in `scale_curve.csv`, so 25.7 (L013's row prints 25.6, not edited) |
| A200 | C | "so regions of one state tip together" | "so regions of one state share that state's yield factor" |
| A149 | B | 8.1; 7.3; 7.1; 6.1; 4.6; 3.9 (capacity over people) | 0.12; 0.14; 0.14; 0.16; 0.22; 0.26 (people over capacity) |
| A343 | B | 1.000; 0.798 | 1.000; 1.253 (people over capacity) |
| A344 | B | 2.076; 0.411; 0.623 | 0.482; 2.431; 1.604 (people over capacity) |
| B081 | B | 5.8 to 6.0 delivered, 10.0 to 10.5 produced; "21 crops" | 5.8 delivered, 10.1 produced (harvest-matched); 6.0 and 10.5 (same-year pairing); 22 crop items; output `cassidy_matched.csv` |
| B085 | B | 6.1 to 5.8 | 5.9 to 5.6 (harvest-matched); 6.1 to 5.8 (same-year) |
| B258 | B | wording | states that both of its figures use the same-year pairing, and that harvest-matched the project's figure is 5.78 (label only, status kept) |
| B301 | B | 108.89; -24 | 108.89; within rounding |
| B302 | B | 109.55; +731 | 109.55; within rounding |
| B303 | B | 95.65; -3 | 95.65; within rounding |
| B304 | B | 96.45; +234 | 96.45; within rounding |
| B322 | B | four figures with -779%, +731%, -239%, +234% | the same four figures, shares dropped, "within rounding" |
| B157 | B | contains Fearnside's average-year point (41.5), "sits on" 18.9 | containment sentence deleted: 1-in-10 point outside the corrected range, improved range holds none, improved long term near 18.9, corrected 17% below (value 30.8; 18.9) |
| B216 | B | "a cliff after 5.5%"; note carries 96.7 and 88.0 | "a cliff between 5% and 7.5%"; note says 96.7 and 88.0 are superseded (decision 31 set 100.4 and 103.6) |
| B230 | C | Ridoutt 2017 "citation that does not contain it" | remark dropped (decision 33); PMSEIC worded as decision 46 sets it |
| B251 | B | unit "share of diet"; status "self-checked" | unit "share of meat" (as A341), status "self-checked (B92b, 2026-11-13)" |
| B252 | B | status "self-checked" | status adds the improved-release note of A342 |
| B278 to B332 | B | status "unverified" | "self-checked (B93, 2026-11-13)" for the 34 passes; the same with the B93 note for the 21 passes with a note (B278 to B288, B293, B294, B295, B301 to B304, B306, B320, B322) |

B93 proposed the status label "one-route checked (B93)". The register's tools read "self-checked" as the one-route label and this brief names that label, so "self-checked (B93, 2026-11-13)" was used.

Label-only changes (value unchanged; note added):
* Release label `2011-fixed` to `2011-fixed-2` in `release_or_data` and the locator, because `shocks_summary.csv` and the flips carry that id: A031, A035, A039, A112, A163, A166 to A178, A196. The `output_file` path of each is the same csv, so it did not change. B129 (national row, `results/2011-fixed.csv`) was left, as the national row is unchanged. A037, A038, A040, A042, A044 and the `movers.csv` rows hold on every other zone and were left. A029, A033, A034, A036, A164, A165, A199 keep their old release label because their old value belongs to it.
* A215, A217, A221: moved to the corrected release, value 0% unchanged.
* A228 to A263 (36 rows): locator adds "column release = 2025-fixed (new first column of measures.csv)".
* A003 and A008 notes: the superseded ranges (35.9 to 45.1; 14.3 to 17.8) are marked superseded by decision 27 (36.3 to 45.8; 13.4 to 16.5). A072 note: the decomposition on the corrected releases is `capacity_by_cause_corrected.csv`, whose layers sum to +8,195,723 and +273,063 (checked here against zone 1).
* B318 to B332 layout: `unit`, `output_locator`, `depends_on` and `notes` were shifted by one column; each is realigned, contents unchanged (defect X126).

The recycling rows A211 to A214 and A227 each say the two releases' recycling settings are not the same measure.

## 3. Rows added (700 data rows: 697 plus 3)

* A366 (Tier B, unverified): the Monte Carlo draws the herd and meat window as three choices with equal chances; the equal chances are the author's judgement (B92a gap 2).
* A367 (Tier B, unverified): the long-term resilience table is drawn 50/50 between the release's own table and the leave-one-out table; the weight is the author's judgement (B92a gap 2).
* B333 (Tier B, unverified): the ordering of the design choices by high over low in `design_choices.csv` (1.09 land; 1.17 to 1.33 waste; 1.29 Australian settings; 2.14 guideline diets; 2.19 drought allowance; 2.41 exports proportional; 2.66 time frame; 2.67 unit; 4.43 to 6.36 exports by energy; 7.88 optimised diet) (B92b section 6 gap 6).

B92a names two missing rows (A366, A367). B92b names one row that is definitely missing (B333). It names three more only as conditional jobs (a Cohen range if quoted, the model limits, the L062 constants), so those were not added. B90 asks for no claim row, only sources-register and defect rows. B93 and B91 ask for none.

## 4. README and DISCUSSION_MEASURES lines changed

`analysis/method_tests_2025/make_readme_tables.py` (`t_gap_attribution`): prints "within rounding" when the residual is within half a unit of the published figure's last digit; two cells are printed from unrounded values (Simpson -12.48, Foran and Poldy 32.8546). The generated table differs from the hand-typed one in exactly the seven lines below (checked by diffing the generator's output with and without the change).

`analysis/method_tests_2025/README.md` (hand-typed table, so edited in the text):
* Simpson (a) sheep-meat rate 34.1: -13% to -12%.
* Henry and Godden energy (b) 82/466: -24% to within rounding; (b) 82.5: +731% to within rounding.
* Henry and Godden protein (b) 60/294: -3% to within rounding; (b) 60.5: +234% to within rounding.
* Foran and Poldy (b) three-year mean 1996 to 1998: 32.86 to 32.85.
* The Henry and Godden sentence "moves the result by several times the residual" to "moves the result by 0.6 to 0.8 million; the residuals themselves are within the rounding of the published whole numbers".

The Simpson prose in the same section (widens the residual by 13%) has the same double rounding and is not in B93's list; it was not changed (recorded in defect X127).

`papers/A_results/DISCUSSION_MEASURES.md` item 5 (D5): South Australia 0.36 to 0.35; Western Australia 0.49 to 0.47; "because the states do not fail together" to "because bad wheat years are only partly correlated across the southern states (Anderson 2019)" (decision 51).

## 5. Defects (`defects.csv`, 121 rows plus 5 appended)

| Id | Result |
|---|---|
| X108 | `fixed_in` set to open: neither B90 nor V33 traces the 304 people |
| X109 | fixed in B89 (claim A321 corrected to 0.35 and 0.47; read in the register) |
| X110 | fixed in B89 (claim B045 label corrected to 1991, V31e; read in the register) |
| X116 | NOT marked fixed. The brief says B90 fixed `movers.csv`, but B90 changed only the zone 22 rows (population, ratios, flag). The `land_only_ratio` column carries the published-method values (Goulburn Broken 1.21, corrected tier 1.03), so `fixed_in` says open and why |
| X117 | fixed in B93 (QCL 2020 extracted; harvest-matched run; Australia 5.78 against 6.01; canola and winter pulses lagged as well) |
| X122 | has `fixed_in` "B89 (claims B239 and B240 corrected)"; B239 and B240 read as corrected; left unchanged |
| X123 (new) | the North East Vic copy of Goulburn Broken's population, layer 1, found by V32a, fixed in B90 (2011-fixed-2 and 2011-improved-2); V33 agrees on 98,604 |
| X124 (new) | Fitzroy and Wet Tropics share a population (ERRATA error 9), found by B90, `fixed_in` empty |
| X125 (new) | CSIRO fuel scenario: 18.75% off on improved, 1.83% on corrected, same settings, found by B91, `fixed_in` empty |
| X126 (new) | B318 to B332 column shift, found by B93, fixed in B95 |
| X127 (new) | gap-attribution table printed within-rounding shares and double-rounded cells, found by B93, fixed in B95 |

## 6. Checks

* Register parses with 18 columns on every row (700 data rows plus the header); 697 plus 3 added.
* 171 rows differ from the old file; every one is a row this job touched (174 touched counting the 3 added). Every other row is byte-identical.
* No em dashes or en dashes in the register, the defects file, the README, the generator or DISCUSSION_MEASURES.md. The only time-word hit among added text is "not yet explained", which the brief requires in A226.
* Line endings unchanged: the register and `defects.csv` are CRLF throughout with a final CRLF; the README, generator and DISCUSSION_MEASURES.md are LF as they were.
* Every Tier A row touched keeps its old `value` and `statement` (the pending rows) or has only its label, locator or notes changed (A003, A008, A031, A035, A039, A072, A163, A167, A171, A196 locator, A228 to A263 locators). Tier A pending count: 21.
* The generator output was diffed with and without the change: seven lines differ, all in the gap-attribution table.

## 7. Open items for Murray or a builder

* The national 2011 population row (B90 decision 2) was not touched. A002 (22.3), A005 (1.49 to 1.50) and A328 move if it is reset.
* A163, A167, A171 and A005 are capacity over population ratios; only A196 was restated, as the brief names it. The other four need the same decision.
* A144 (94%) depends on the denominator (V33 finding 2).
* Goulburn Broken's own 2011 population is 15% above its ERP (V33 finding 1); no status moves.
* `method_status.csv`, `long_term_regions.csv`, `regions_in_depth.py` and `make_readme_tables.py` in `analysis/paper_a` need the one-word release switch B90 lists; A308's output cell depends on it.
* The sources register rows B90 lists (the ABS 3218.0 cube, D31 `used_by`, D44 notes) were not written, since this job may not write that file.
* L050 and L062 (literature rows) were skipped, as the brief says.

## Wrong-value check

Wrong-value check: example only, marked as what was NOT done. A029's `value` cell changed outright from 23 to 22 and its statement to "22 of the 53 regions". A029 is Tier A, so that edit is barred; the row keeps 23 and carries "pending gate 4 (2026-11-13): new value 22 (release 2011-fixed-2) per B90". The register shows this: A029 `value` reads 23 and `status` reads "independently verified; new value pending gate 4 (B90)". The same holds for the other 20 pending rows.
