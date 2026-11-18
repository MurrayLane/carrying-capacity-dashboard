# B122: the checked changes of B110 to B116 applied to the registers; the loose ends of V36 to V42 fixed

Brief: `qa/briefs/B122_apply_checks.md`. No git, no subagents, no network. Written: `qa/claims_register.csv`, `qa/defects.csv`, the analysis READMEs and csv files named in the brief, `analysis/method_tests_2025/bases_fidelity.py` and `make_readme_tables.py` (V42 asks for both), and this report. No frozen release, nothing under `results/` or `releases/`, no paper draft was touched. A scratch copy of `analysis/paper_a/regional_flips.py` was run for A038 (nothing filed).

## 0. Summary

* **Register:** 707 rows became 788 (81 added); 87 existing rows changed (27 Tier A rows marked pending gate 5 with value and statement untouched, 56 Tier B or C rows changed, 4 note only); the other 620 rows are byte-identical (checked by serialising old and new rows). 18 columns on every row, CRLF line endings as before, no em dashes.
* **Defects:** `defects.csv` 127 to 137 rows (X128 to X138 added, X124 closed). Fixed here: X130 (README only), X132, X133, X134, X135, X136; open: X129, X131, X137, X138 (X128 fixed in B110).
* **Decision 115 changes what the B115 rows mean.** `qa/DECISIONS.md` 115 (Murray, 2026-11-18) adopts the widened Monte Carlo range in both papers, so the Tier B and C rows that B115 marked "only if adopted" (B113, B116, B117, B120, B157, B253) were applied, and the Tier A rows (A027, A028, A009, B112, B159, B187, B188) are pending with the widened figures. The herd-cycle range of B112 (39.4 to 43.8) is carried as a separate result, not as A027's pending value.
* **Open for the coordinator (section 8):** the shocked 1-in-10 and 1-in-20 ranges exist only on the 13-choice and herd-cycle draws, not on the widened draws that decision 115 makes the headline range; `cross_method_local.csv` and the README writer of `decompose_corrected.mjs` are not regenerated.

## 1. Tier A rows marked pending (value and statement unchanged)

Each row has `; pending gate 5 (2026-11-18): new value <x> per <job>, checked <V job> (<reason>)` added to `notes`; `status` reads `independently verified; new value pending gate 5 (<job>, <V job>)` (where the row already carried a gate 4 pending value that text is kept in front of it); the checker's report is added to `verifier_report`.

| Id | Current value | Pending value | Job | Checker |
|---|---|---|---|---|
| A031 | 36 | 35 (release 2011-fixed-3) | B110 | V36 |
| A033 | 23 to 16; 36 to 32 | 22 to 16; 35 to 32 | B110 | V36 |
| A035 | 4 | 3 (Desert Channels, South West Qld, SA Arid Lands) | B110 | V36 |
| A039 | 1: South West Qld | 1: South West Qld (value holds); statement "One of the three long-term flips is clean and robust: South West Queensland (over to under)." | B110 | V36 |
| A165 | 82 | 82 (81.55%, about 82%) | B110 | V36 |
| A199 | 5 (2025); 1 (2011) | 5 (2025); 3 (2011): Corangamite, North East Vic, Burnett Mary | B110 | V36 |
| A014 | 30.8 | 30.8 with a range of 27.0 to 34.0 million (5th to 95th percentile of the 13-choice draws; 29.2 to 32.5 on the herd-cycle draws) | B112 | V38 |
| A183 | 1.12 | 1.12 with a range of 0.98 to 1.23 (13-choice draws) or 1.06 to 1.18 (herd-cycle draws) | B112 | V38 |
| A187 | 0.95 | 0.95 with a range of 0.83 to 1.05 (13-choice draws) or 0.90 to 1.01 (herd-cycle draws) | B112 | V38 |
| A196 | 0.89; 0.95 | base values hold (gate 4 value 1.12; 1.05 in people over capacity); at 1 in 10 the national range is 0.98 to 1.23 (13-choice draws) or 1.06 to 1.18 (herd-cycle draws) and at 1 in 20 0.83 to 1.05 or 0.90 to 1.01; on the herd-cycle draws national capacity at 1 in 20 is below 27.6 million in about 92% of draws (75 of 1,000 above) | B112 | V38 |
| A027 | 36.3 to 45.8 | 31.1 to 49.2 (19 choices, 2,000 draws; 18 of the 19 vary) | B115 | V41 |
| A028 | 13.4 to 16.5 | 13.3 to 18.8 (19 choices, 2,000 draws) | B115 | V41 |
| A009 | 15.35 and 15.6 within 13.4 to 16.5 | 15.35 and 15.6 within 13.3 to 18.8 (both inside); the 2011 short-term figure 33.3 lies inside the widened short-term range 31.1 to 49.2 | B115 | V41 |
| A184 | 21 | 21 of 53 at the central figure, 21 to 22 across the 5th to 95th range (North Tasmania at balance) | B112 | V38 |
| A038 | 3: Wet Tropics; Rangelands; Corangamite | 2: Rangelands; Corangamite (on the herd-cycle ranges; on the 13-choice ranges the value stays 3) | B112 | V38 |
| A223 | -0.3; -26 | -0.3; -26 unchanged in value (gate 4 value -0.2; -26); the crop-only bound -0.8% at 1 in 10 (41.2 against 41.5 million) can be cited beside it | B112 | V38 |
| B276 | 10% and 90%; 0.14 and 1.35; 0.59 to 1.42 | line (a): 4% of the distance to the corrected model closed (factor split 9.6%; about 20% to the centre of the methods); line (b): 39% (38.5%; factor split 41%); input factors 0.59 to 1.42 unchanged | B113 | V39 |
| B277 | 17 to 343; 12 to 343 | line (a): the spread of method centres does not narrow (SD of log centres 0.65 to 0.70; highest over lowest 6.2 to 7.0); line (b): it narrows by about a third (0.65 to 0.44; 6.2 to 3.7) | B113 | V39 |
| B156 | 103 to 343; 12 to 41 | about 65 to 211 million, about 1.6 to 5 times the model (footprint and HALF at Australian productivity); at world-average productivity on 2021-23 yields 134 to 343 million, about 3.2 to 8.3 times (103 at 1990 world yields); 12 to 41 (commodity balance and Fearnside) | B113 | V39 |
| B046 | 103 to 343 | primary 64.8 to 117.0 million at Australian productivity (crop and pasture together 64.8 to 84.6); secondary 146.2 to 343.4 on current world-average yields (103 at 1990 world yields) | B113 | V39 |
| B068 | 276 | HALF at Australian productivity (Wackernagel and Rees 1996, p. 78): 76.0 million, 1.83 times the corrected model and 1.42 times the improved; 276 million at world-average productivity | B113 | V39 |
| B272 | 275.8; 6.65; 5.15; 76.0 | primary 76.0 million (1.83 and 1.42 times); secondary 275.8 million (6.65 and 5.15 times) | B113 | V39 |
| B112 | 36.3 to 45.8 | 31.1 to 49.2 (19 choices, 2,000 draws; 18 of the 19 vary) | B115 | V41 |
| B159 | 41.5 (36.3 to 45.8); 53.6 (46.2 to 60.1) | 41.5 (31.1 to 49.2); 53.6 (46.2 to 60.1) | B115 | V41 |
| B187 | 1.26 | 1.58 over 19 choices (18 of the 19 vary; lbench is fixed at 0.4); 2.22 min to max | B115 | V41 |
| B188 | 1.26 vs 2.2 to 6.4 | 1.58 (2.22 min to max) against 2.14 (guideline diets), 2.19 (drought allowance), 2.41 to 6.36 (exports), 2.66 (time frame), 2.67 (unit) | B115 | V41 |
| B058 | within 0.8%; within 2.1%; within 5%; -7.4%; -30.2% | HALF rebuilt from FAOSTAT 2011 on the current revision: Australia +0.8%, world -2.2% (-2.16% unrounded), United States -3.3%, Argentina -4.6%, India -7.2% (the row says -7.4%), New Zealand -30.2%; on the inputs the authors printed Australia +8.4% and world +2.8%; verdict partly for both under decision 109 | B116 | V42 |

A223 is Tier A (V38): listed above with no value change. A184, A014, A183, A187 gain a range, not a new point value. A038 was rerun here (section 8, item 3).

Held without an edit, as B110 says their value holds on `-3` and only the release label in the locator moves: A002, A005, A029, A034, A036, A037, A163, A164, A167, A171 (A029, A034, A036 and A164 keep their gate 4 pending values, 22, 8 flips, 2 clean flips and 22, which are right on `-3`).

## 2. Tier B and C rows changed (id; before; after)

Each row has ` | B122 2026-11-18 (from <job>, checked <V job>): ...` added to `notes` with the before and after; `status` is `independently verified (<job>, <V job>, 2026-11-18)` where the checker reproduced the figure by its own route, with the limit stated where it did not.

| Id | Tier | Before (value) | After (value) | Job, checker |
|---|---|---|---|---|
| A040 | B | 3: Desert Channels; SA Arid Lands; Northern and Yorke | 2: Desert Channels; SA Arid Lands | B110, V36 |
| A041 | B | 2: SA Arid Lands; Northern and Yorke | 1: SA Arid Lands | B110, V36 |
| A042 | B | short 3 and 3; long 3 and 2 | short 3 and 3; long 2 and 1 | B110, V36 |
| A043 | B | 6 against 2; 4 against 1 | 6 against 2; 3 against 1 | B110, V36 |
| A057 | B | value unchanged. Statement before: SA Arid Lands: capacity 2 to 28 thousand people (population 31 to 8 thousand), over to under, with the land layer alone raising capacity 6.5 times. ... | value unchanged. Statement after: SA Arid Lands: capacity 2 to 28 thousand people (population 11 to 8 thousand), over to under, with the land layer alone raising capacity 6.5 times. ... | B110, V36 |
| A067 | B | 31,361; 8,049 | 31,361; 10,613; 8,049 | B110, V36 |
| A143 | B | 17 | 18 | B110, V36 |
| A144 | B | 94 | 93 | B110, V36 |
| A151 | B | 13 published; 17; 21 | 13 published; 18; 21 | B110, V36 |
| A168 | B | 24 | 25 | B110, V36 |
| A169 | B | 84 | 85 | B110, V36 |
| A172 | B | 27 | 26 | B110, V36 |
| A173 | B | 87 | 88 | B110, V36 |
| A176 | B | 33 | 32 | B110, V36 |
| A177 | B | 92 | 91 | B110, V36 |
| A197 | B | 81; 85; 91 | 81-82; 85; 91 | B110, V36 |
| A308 | B | 22; 22; 21 | 22; 22; 20 | B110, V36 |
| A309 | B | Mackay Whitsunday | Desert Channels; Mackay Whitsunday | B110, V36 |
| A310 | B | 39; 36; 38 | 39; 35; 36 | B110, V36 |
| A311 | B | Western NSW; South East SA | South East SA | B110, V36 |
| A195 | B | value unchanged. Statement before: The national short-term capacity falls to 26.3 million in a 1-in-20 year (2025) and 18.9 million in a 1-in-100 year. ... | value unchanged. Statement after: The national short-term capacity falls to 26.3 million in a 1-in-20 year (2025; 23.0 to 29.0 across the 13-choice Monte Carlo range, 25.0 to 27.8 on t ... | B112, V38 |
| A188 | B | value unchanged. Statement before: In a 1-in-20 year in 2025 24 of 53 regions are over capacity. ... | value unchanged. Statement after: In a 1-in-20 year in 2025 24 of 53 regions are over capacity, and 24 at every point of the 5th to 95th percentile range. ... | B112, V38 |
| B113 | B | 13.4 to 16.5 | 13.3 to 18.8 | B115, V41 |
| B116 | C | 13; 1,000 | 19; 2,000 | B115, V41 |
| B117 | B | 81 | 24 | B115, V41 |
| B120 | B | 36 | 14 | B115, V41 |
| B157 | B | value unchanged. Statement before: Fearnside's 1-in-10 point (30.8) lies outside the corrected range (36.3 to 45.8) and the improved range contains none of his points; the improved long ... | value unchanged. Statement after: Fearnside's 1-in-10 point (30.8) lies just below the widened corrected range (31.1 to 49.2; it was outside the earlier 36.3 to 45.8) and the improved  ... | B115, V41 |
| B253 | B | 12 of 13 | 18 of 19 | B115, V41 |
| B249 | B | within 2.1%; within 0.8% | 2.2%; 0.8%; 2.8%; 8.4% | B116, V42 |
| B260 | B | value unchanged. Statement before: Simpson's food pasture of 1.758 ha a person (1991-92) is reproduced within 3% (1.718 ha) by charging all red meat (58.4 kg carcase weight) at the shee ... | value unchanged. Statement after: Simpson's food pasture of 1.758 ha a person (1991-92) is partly reproduced (2.3% low) at 1.718 ha by charging all red meat (58.4 kg carcase weight) at ... | B116, V42 |
| B278 | B | 112.74; +42 | 112.74; -0.38 points, +0.6 million people | B116, V42 |
| B279 | B | 118.88; -622 | 118.88; +5.76 points, -9.2 million people | B116, V42 |
| B280 | B | 113.15; -3 | 113.15; +0.03 points, -0.1 million people | B116, V42 |
| B281 | B | 113.11; +2 | 113.11; -0.01 points, 0 million people | B116, V42 |
| B282 | B | 113.20; -8 | 113.20; +0.08 points, -0.1 million people | B116, V42 |
| B283 | B | 115.88; -298 | 115.88; +2.76 points, -4.5 million people | B116, V42 |
| B284 | B | 113.15; -3 | 113.15; +0.03 points, -0.1 million people | B116, V42 |
| B285 | B | 34.06; -40 | 34.06; -0.31 points | B116, V42 |
| B286 | B | 35.76; +183 | 35.76; +1.39 points | B116, V42 |
| B287 | B | 34.88; +67 | 34.88; +0.51 points | B116, V42 |
| B288 | B | 34.38; +2 | 34.38; +0.01 points | B116, V42 |
| B289 | B | 94.10; -14 | 94.10; -0.45 points | B116, V42 |
| B290 | B | 99.13; +144 | 99.13; +4.58 points | B116, V42 |
| B291 | B | 109.34; -6 | 109.34; -0.29 points | B116, V42 |
| B292 | B | 115.36; +109 | 115.36; +5.73 points | B116, V42 |
| B295 | B | 1.713; -12 | 1.713; -0.005 ha a person | B116, V42 |
| B296 | B | 1.291; -1057 | 1.291; -0.426 ha a person | B116, V42 |
| B297 | B | 1.788; +175 | 1.788; +0.071 ha a person | B116, V42 |
| B298 | B | 1.778; +149 | 1.778; +0.060 ha a person | B116, V42 |
| B299 | B | 1.740; +56 | 1.740; +0.023 ha a person | B116, V42 |
| B300 | B | 1.730; +30 | 1.730; +0.012 ha a person | B116, V42 |
| B305 | B | 31.28; +180 | 31.28; -0.67 Mt | B116, V42 |
| B306 | B | 32.85; -243 | 32.85; +0.91 Mt | B116, V42 |
| B307 | B | 30.59; +365 | 30.59; -1.36 Mt | B116, V42 |
| B308 | B | 3.60; +303 | 3.60; +0.13 Mt | B116, V42 |
| B309 | B | 3.53; +129 | 3.53; +0.06 Mt | B116, V42 |

Note only (value, statement and status unchanged; a `B122` line added to `notes` and the checker's report to `verifier_report`):

* A343 (Tier B, B112 checked V38): value unchanged; North Tasmania is the one region whose population lies inside its 1-in-10 range (5th to 95th percentile) on the 13-choice and the herd-cycle draws (shocks_ranges.csv, zone 57)
* A366 (Tier B, B112 checked V38): value unchanged; the B112 herd-cycle run draws the window from the four full-cycle windows (8, 10, 15 and 20 years, 250 draws each) with equal chances: a separate result, not the headline basis (decision 115 keeps the three windows in the widened run)
* B247 (Tier B, B113, B114 checked V39, V40): value "3 to 8" unchanged and the statement unchanged, including its cause clause (V40: the builder's reworded cause clause is not taken). The primary local-productivity reading of the aggregate methods is 64.8 to 210.7 million, about 1.6 to 5 times (decision 106; rows B3xx added in B122); this row keeps the world-average readings, secondary on 2021-23 yields 133.8 to 343.4 million, 3.2 to 8.3 times (103 at 1990 world yields)
* B270 (Tier B, B113 checked V39): values unchanged (64.8; 84.6 etc.); the role moves from sensitivity to primary reading (decision 106)

Conflict resolved: B113 listed B247 as moving to "about 1.6 to 5 times" and B114 listed it as unchanged at "3 to 8". V40 and the brief keep "3 to 8" and the existing cause clause; the primary 1.6 to 5 reading is carried by new row B349 and named in B247's note.

## 3. Rows added (81)

Tier B, `last_verified_commit` empty. Status is `independently verified (<job>, <V job>, 2026-11-18)` where the checker reproduced the figure; the ones that are not are listed after the table.

| Ids | Job | What |
|---|---|---|
| A368 to A371 | B110, V36 | the 23 and 12 against the ABS figures; the 53-region sums; four regions tipping at 1 in 20; capacities equal on the corrected method and 75 of 120 cells moving on the improved |
| A372 to A380 | B111, V37 | the Shapley (all-orderings) average of each of the nine layers, short and long term |
| A381 to A389 | B111, V37 | land and livestock together (sum) and as one layer; the other eight-layer figures; the driver figures ("the consumption and red-meat-mix layers"); the eight-layer ranking; regions by largest layer (short, long, with the minor categories); Swan; the land-livestock overlap (Avon, Australia) |
| A390 to A403 | B112, V38 | shocked ranges 1 in 10 and 1 in 20; capacity over population ranges; herd-cycle range short and long; herd-cycle variance shares; shocked herd-cycle ranges (about 92% of draws); window means from the four-window run; crop-only bounds short and long; the 97% attribution; the drought factor construction (0.742 = 15th-worst of 153); regions over capacity across the range; herd-cycle limits |
| B341 to B350 | B113, V39 | line (a) and line (b) distance to 41.5 (4.1%, 38.5%) with the definition of the share written into the notes; centre references; dispersion of centres and readings; per-method shares; local-productivity ratios (footprint, HALF, aggregate); secondary on 2021-23 yields |
| B351 to B356 | B114, V40 | base binding land; variants 1, 1p, 2 (figures only, no cause sentence); variant 3 and 3u; gap closed shares |
| B357 to B371 | B115, V41 | widened short and long ranges, factor 1.58, 2.22, 1.41, 1.60; first-order and total-order indices short and long; sum of first-order shares (97%) and interactions (about 3%); conditional ranges; 2011 inside; against the definitions; the six new ranges (one row each); the judgement count |
| B372 to B385 | B116, V42 | bases (population, energy, land, waste); fidelity (HALF Australia and its people equivalents, HALF others, Simpson, Cassidy ten rows, Cassidy shares, reproduced rows); intake on FAO's factor, commodity balance, the model's factors |

Not independently verified: B355 (variants 3 and 3u, `unverified`: V40 did not reach them, as the brief says), A403 (herd-cycle limits, `unverified`). With limits stated in `status`: A400 (the 97% is the checker's own test, no repository output), B350 (the 2021-23-yield secondary is the checker's counterfactual), B368 (meat-calibration yearly gaps not recomputed), B375 (model rows not on the checker's route), B385 (model loss factors spot-checked only). The B116 report's intake tops 11.0 and 13.0 read 10.9 and 12.9 (B383, B385). The driver sentence is carried by A384; the register has no abstract or highlights row, so it is not attached to A357, A358 or A362.

## 4. README, script and csv changes

**`analysis/method_tests_2025/`**
* `bases_fidelity.py`: Henry and Godden energy computed from the printed factor 0.1760 (3,718 kcal, was 3728); `fidelity.csv` gains two columns (`rebuild on current FAOSTAT yields, paper years`, `gap on those yields (%)`); the Cassidy rows take their 1997-2003 rebuild into them, the verdict rests on the rebuild as run (decision 109); four Cassidy delivered rows (US, India, China, Brazil) added; the Fearnside row padded for the new columns. `--check`: 0 mismatches.
* `bases.csv`: one cell changed: row "Energy and protein balance ... as run", column "energy a person a day": `15.6 MJ (3728 kcal), implied by the factor 82/466` to `15.6 MJ (3718 kcal), implied by the factor 82/466 (printed 0.1760 a 10^15 J)`.
* `fidelity.csv`: header 15 to 17 columns, 30 to 34 rows. Cells that changed: Cassidy world produced, world delivered, United States produced, India produced, China produced, Brazil produced: the printed-input rebuild, its basis and gap move to the new yields columns (values 10.7268, 6.5426 on the yields alone, 19.2771, 7.3436, 15.9537, 11.2266), `verdict basis` printed inputs to as run, and `verdict` partly to not reproduced for world produced, world delivered and Brazil produced. World delivered now takes the yields alone (6.5426, +9.0%) in place of yields plus the paper's feed efficiency (6.3911, +6.5%, kept in the note). Four rows added: United States delivered (6.908, +27.9%), India (7.8643, +33.3%), China (11.9495, +42.3%), Brazil (6.8265, +31.3%), all not reproduced; on current yields +18.9%, +11.8%, +25.1%, +5.2%. `intake_variant.csv` and `gap_attribution_readable.csv` are byte-identical after the rerun.
* `make_readme_tables.py`: the units of Table S1 come from the method (points for HALF, ha a person for Simpson, Mt for Foran and Poldy; Simpson at three decimals); the Fidelity table gains the yields column.
* `README.md`: Convention paragraph ("under 1%" to "under 5% (decision 119)", the cases that print a change listed: HALF Australia, world, United States, Argentina, Simpson, Foran and Poldy; shares kept for HALF India, Cassidy; Henry and Godden read "within rounding"); Table S1, bases, fidelity and intake tables regenerated (`--write --only gap_attribution,bases,fidelity,intake_variant`; a second run leaves the file unchanged); Fidelity prose (introductory sentence, Partly and Not reproduced bullets, the wording for the papers: Cassidy not reproduced, Simpson feed cropland and total named, "partly reproduced or not reproduced"); intake range tops 10.9 and 12.9; in the B113 subsection "the spread of method centres narrows by about a third" and the secondary readings on 2021-23 yields beside the 103 at 1990 yields.
**`analysis/comparison_2025/README.md`** (B111 section): "the consumption and red-meat-mix layers" in place of "the two diet layers" (with the note that the consumption layer carries fuel, biofuel and timber presets); "-7 people" for "-0.00 million" in both places; "land and livestock as one layer" for the second use of "together" in the long-term sentence. The regions where a minor layer is largest (consumption 1 and crop yields 1 short term; fuel 1 long term) were already in the README bullet.
**`analysis/paper_a/README.md`** (B112 section): a paragraph appended with the V38 readings (about 92% of draws, 75 of 1,000 above 27.6; R03a confirmed to within 0.15 million; window means from the four-window run 41.7, 41.7, 41.7, 41.3 and the five-window file separately; "almost all (about 97%)"; the flips not robust: three on the published ranges, two on the herd-cycle ranges). The README did not hold the window means; they were in the B112 report only.
**`analysis/pasture_2025/README.md`**: the pointer now reads `qa/reports/B114_pairing_relaxed.md`.
**`analysis/sensitivity_2025/README.md`** (B115 section): heading and `lbench` row (18 of 19 vary); judgement marks for the loss-factor weight, the meat-calibration weight and the energy range (a part of the NHMRC PAL 1.2 to 2.2); first-order shares add to 97% in both settings (96% is the total order), interactions about 3%; five of the six new choices have the release at one end (waste too); a bullet naming the six judged choices and the two weights.

## 5. Defects added or closed

| Id | Kind | Found by | Fixed in |
|---|---|---|---|
| X128 | data provenance (2011 regional populations) | R02a, R02b, B110 | B110 (ERRATA error 10; `-3` releases) |
| X124 (closed) | data copy (Fitzroy, Wet Tropics) | B90 builder | B110 (error 9 closed by error 10; V36 confirms the figures) |
| X129 | code fault: default rerun of `decompose_corrected.mjs` drops the V29 paragraph | B111 builder | open |
| X130 | generated wording: -0.00 million, "diet layers" | V37 | README corrected by hand; generator not edited (open there) |
| X131 | mixed bases in `cross_method_local.csv` (103 at 1990 yields; 6.40) | V39 | open |
| X132 | pointer to a report that does not exist | V40 | B122 |
| X133 | wrong counts in the B115 README section | V41 | B122 |
| X134 | Table S1 threshold and units against the Convention paragraph | V42 | B122 |
| X135 | Cassidy delivered rows missing; "printed inputs" mislabel | V42 | B122 |
| X136 | double rounding: 3728 kcal; intake tops 11.0 and 13.0 | V42 | B122 |
| X137 | `foran_poldy_balance.py` head-count year mismatch (0.48%) | V42 | open |
| X138 | Kitagawa and Das Gupta not in the literature register | B111 builder | open |

The V36 note that the `-3` release files read frozen while the B110 report says current is not a defect: B120 froze them and ERRATA error 10 already says so. The B110 report text is a builder report and was not edited.

## 6. Checks

* Register parses with 18 columns on every row; 707 + 81 = 788; the 620 untouched rows are byte-identical when serialised; the Tier A rows have the same `value` and `statement` as before (asserted for all 163 Tier A rows); `depends_on` ids all exist; CRLF as before; no em dashes in the register, defects or any file written.
* `defects.csv` parses with 8 columns; only the X124 line changed among the old lines; 137 data rows. It does not round-trip through the csv writer (as before), so the file was edited as text.
* `python3 -I analysis/method_tests_2025/bases_fidelity.py --check`: 0 mismatches. `make_readme_tables.py --write --only ...` run twice: the second run leaves the README byte-identical.
* `qa/tools/numbers_lint.py` does not take the register (it scans documents against output csvs and writes a shared dated report), so it was not run.
* Regenerated csvs and the cells that changed: `bases.csv` (1 cell), `fidelity.csv` (2 columns added; 6 Cassidy rows changed; 4 rows added); `intake_variant.csv` and `gap_attribution_readable.csv` unchanged (same md5).

## 7. What was not applied, and why

* **B110 follow-ups outside the write list:** the sources register rows (D31 `used_by`, D44 notes), the ERRATA wording and the B110 report text are not edited.
* **V36 paper cautions** ("about 82%" and "about 91%" in the text; one line that the share is of the 53 regions' population): carried in the notes of A165, A177 and A369; paper text not edited.
* **V37:** the driver sentence of the abstract and highlights is paper text, not a register row (the register has none); not attached to A357, A358 or A362. The generator of the README, `decompose_corrected.mjs`, is not on the write list (X129, X130).
* **V38 paper sentences** ("at or below it", the shocked range sentences): paper text; the corrected readings are in A396 and in the A196 pending note.
* **V39:** `cross_method_local.csv` secondary rows are not regenerated (X131); the register carries the 2021-23-yield secondary figures (B156, B046 pending; B350).
* **V40:** the builder's reworded cause clause for B247 and the proposed 7.6 sentence are not taken; "Relaxed in the model, the residual closes" is paper wording.
* **V41 paper sentences** (judgement "four", "every definition moves it further", the 18.9 to 55.3 span, the 2011 change sentence, the 4% interactions): paper text; the supported readings are in B361, B363, B364, B371.
* **V42 notes not acted on:** the Henry and Godden waste cell should say FAO pre-retail losses are deducted from production; HALF New Zealand on the printed inputs (101.88, -25.0%) was not added; the consumption-only intake lower bound is in the note of B383 only.
* **Held rows of B110** (section 1) and the unchanged rows B015, B019, B083, B094, B141, B263, B266 to B269, B301 to B304, B310 to B317, B326: no value moves.

## 8. Open items for the coordinator

* **Shocked ranges on the widened draws.** B112's 1-in-10 and 1-in-20 ranges (27.0 to 34.0, 23.0 to 29.0) and its herd-cycle ranges are on the 13-choice and four-window draws. Decision 115 makes the widened draws (31.1 to 49.2 short term) the headline range, and the widened draws have only a national zone, so the shocked range on them (national, times the factor 0.742 and 0.634) was not computed or checked by anyone. A014, A183, A187, A196 carry the existing ranges in their pending notes and say so.
* **A027 against the herd-cycle range.** A027, A028 and A009 are pending with the widened figures (decision 115); the herd-cycle figures (39.4 to 43.8, 13.9 to 16.2) are rows A393 and A394. If Murray also wants the herd-cycle range in the paper, that is a second choice at gate 5.
* **A038 rerun, as the brief asks.** `regional_flips.py` hard-codes `results/ranges_2025-fixed.csv`; a scratch copy with `results/ranges_2025-fixed_herdcycle.csv` was run on `analysis/paper_a/movers-3.csv` (the frozen `2011-fixed-3`). Published ranges: short-term flips not robust are three (Wet Tropics, Rangelands, Corangamite). Herd-cycle ranges (and the five-window variant): two (Rangelands, Corangamite); Wet Tropics becomes robust. Long term: one (SA Arid Lands) on all three. So A038 is pending as "2" on the herd-cycle ranges only, and stays 3 on the published ranges. The widened run has no zone ranges, so A038 on the widened basis cannot be computed.
* **Not rerun on `-3`:** `long_term_and_measures.mjs` (A143, A144, A151 are counted from `results/2011-fixed-3.csv`) and `method_effects_by_region.py` (A308 to A311; the cells in `method_status.csv` still read the `-2` values). V36 reproduced the corrected and improved counts by its own route; the published counts (22, 39) were not rechecked.
* **Writer of `decompose_corrected.mjs` (X129, X130)** and **`cross_method_local.csv` (X131)** need an edit outside the brief's write list.
* **X137** (the 0.48% head-count year in `foran_poldy_balance.py`): the script is outside the write list.

## 9. Wrong-value check

Wrong-value check: example of what was NOT done. A031 (Tier A, 36 regions over capacity in 2011, long term) has a new value of 35 on `2011-fixed-3`. Writing `value` = 35 into the row would be the wrong move: the tier rule keeps `value` at 36 and `statement` as written, and puts the 35 in `notes` (`; pending gate 5 (2026-11-18): new value 35 (release 2011-fixed-3) per B110, checked V36 (...)`) and in `status` (`independently verified; new value pending gate 5 (B110, V36)`). In the written register A031's `value` is `36`. The same holds for all 27 Tier A rows: the assertion `value and statement equal the old row` passed for every Tier A row. The 35 is an example of a changed value, not an edit.
