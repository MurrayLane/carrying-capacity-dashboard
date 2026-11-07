## How to read the matching

* `matched` means a register `value` or `statement` holds the number after rounding or scaling. It does not mean the row is the claim. Small and common numbers (5%, 10, 12, 100, 30.8) land on many rows; the `n_candidates` and `strength` columns in the .csv show this. `weak` is 49 numbers: a rounded or scaled match among more than three rows, or a low word overlap. Treat weak matches as unchecked until a person confirms the row.
* The thousands and millions scaling (41.5 against 41,503,537) is in the tool and tested on its own, but no document number needed it: the register already stores figures in millions.
* Bare years past 2030 (2050) and written zeros ("0%") are not listed. ABS catalogue numbers (4306.0, 7503.0) are read as numbers, so they show as orphans; they are identifiers, not claims.
* Nothing here is a new finding about the science. Orphans are claims the register lacks and the matched-but-not-verified list is what the register has not yet had independently checked.

## Spot checks: ten matches that are right

| # | Document line | Number | Row | Why it is right |
|---|---|---|---|---|
| 1 | B OUTLINE:70 | 113.1 | B056 | Row says rebuilt HALF index for Australia 2011 is 113.1% of world land; the sentence is the same HALF rebuild result. |
| 2 | B OUTLINE:71 | 5.4 | B077 | Cassidy US 5.4 people a hectare on delivered calories; sentence and row are the same sentence. |
| 3 | B OUTLINE:72 | 1.737 | B033 | Rebuilt 1991-92 pasture 1.737 ha a person against Simpson's 1.758; sentence repeats it. |
| 4 | B OUTLINE:68 | 138 | B016 | Doc "138 to 211 million (energy)"; row value 137.6 rounds to 138 at 0 decimals (rounded match). |
| 5 | B OUTLINE:68 | 211 | B018 | Row value 210.7 rounds to 211; row is Henry and Godden with in-use land unchanged, the same quantity. |
| 6 | DISCUSSION:17 | 8.2% | A247 | Row: waste at the national target gives -8.2% on 15.6 (14.3); the table cell is that measure. |
| 7 | DISCUSSION:37 | 593 | A319 | Fish imports 593 thousand tonnes; sentence and row say the same. |
| 8 | DISCUSSION:28 | 55.4 | A317 | Single-year capacity 43.5 to 55.4 million across 2016 to 2025 with the herd cycle; same claim. |
| 9 | A OUTLINE:8 | 1.12 | A183 | National short-term capacity is 1.12 times the population in a 1-in-10 year (30.8 against 27.6 million). |
| 10 | B OUTLINE:68 | 0.1760 | B014 | Four-decimal figure matches the 0.1760 million people per 10^15 J consumption factor exactly; the four decimals make a chance hit very unlikely. |

## Spot checks: ten where the matching is doubtful

| # | Document line | Number | Row chosen | Problem |
|---|---|---|---|---|
| 1 | SECTION7:21 | 6% | B217 | Doc is the failure risk "about 6% a year"; B217 is 6.2 ha a person (rounded to 6). The right row is B130 (5.8 to 6.1% a year), a lower-ranked candidate. |
| 2 | SECTION7:21 | 7% | B249 | Doc is the 2011 failure risk "7%"; B249 is HALF "India 7% low". The right row is B131 (6.7 to 7.1% at the 2011 population). |
| 3 | SECTION7:21 | 10 | B245 | "1-in-10 failure level": B245 does state the 1-in-10 allowance, so the row is plausible, but 59 rows hold a 10 and the match carries no weight on its own. |
| 4 | B OUTLINE:72 | 36% | B159 | Doc: "36% high in the other build" (pasture); B159 holds 36.3 (the lower end of 36.3 to 45.8, a capacity). The number is a coincidence; the claim is probably an orphan. |
| 5 | B OUTLINE:71 | 5% | B077 | Doc: "within 5% to 8% between the two builds"; B077 holds Cassidy's 5.4. A rounding coincidence. |
| 6 | DISCUSSION:14 | 18.8% | A218 | Table cell is livestock output +20% on the improved release; A218 is liquid fuel -18.75%. A different measure and the opposite sign: wrong row, and the claim is not in the register. |
| 7 | B OUTLINE:11 | 100 | B001 | The "9 to 100 million" range ends in 100; B001 is the worst of 100 years. The same digits, a different quantity. |
| 8 | B OUTLINE:44 | 12 | B169 | Doc: "12 [of the 13 sampled choices] vary"; B169 is avoidable waste of 12%. Different quantity. |
| 9 | DISCUSSION:27 | 1.5 | A315 | Doc "margin of 1.5 times" and A315 "the model's 1.5 times" agree in sense, but 12 rows hold 1.5 and the overlap is 0.14; plausible, unconfirmed. |
| 10 | B OUTLINE:41 | 0.30 | A261 | Doc is the red-meat 30% share written 0.30; A261 (red meat 30% of meat) is the right row, reached by the decimal-against-percentage rule, but 17 rows hold 30, so the pick rests on word overlap alone. |

Pattern behind the doubtful list: the ranking prefers the same paper and section and then word overlap, so when a long sentence carries several numbers each number picks the row that fits the whole sentence, not the number's own role. The fix belongs to a person (confirm or reassign the row id for every weak match); the tool cannot read meaning.

## Resolution of orphans and weak matches

Written 2026-11-07 (brief B33). The "How to read the matching" and the two spot-check tables above are the hand-made notes of the first run and describe it as it was then (17 orphans, 49 weak). The summary table at the top is the rerun after the register changes below.

### Orphans (17 numbers): what was done

New register rows are A340 to A346 and B250 to B259 (17 rows). Rows A340 to A342 and B250 to B252 are of kind "setting" (stated in the notes column; the register has no kind column).

| document and line | number | resolution |
|---|---|---|
| A OUTLINE 41 | 0.115 | A340 (setting, judgement; source `analysis/sensitivity_2025/README.md`), self-checked |
| A OUTLINE 41 | 0.528 | A341 (setting, judgement; same source), self-checked |
| A OUTLINE 43 | 0.798 | A343 (North Tasmania; `analysis/paper_a/regions_in_depth.csv`, 1-in-100 column 0.7981), self-checked |
| A OUTLINE 43 | 2.076 | A344 (Murrumbidgee-ACT, average year 2025), self-checked |
| A OUTLINE 43 | 0.411 | A344 (long term 0.4114), self-checked |
| A OUTLINE 43 | 0.623 | A344 (1 in 100, 0.6234), self-checked |
| A DISCUSSION 22 | 99% | A346 (capacity flat for cropland share 10% to 99%), unverified: the document says it is read from an evaluator test and no saved script or output holds the 10% and 99% ends |
| A DISCUSSION 22 | 3.49 | A345 (pasture need, `analysis/scale_curve_2025/README.md`), self-checked |
| A DISCUSSION 22 | 3.32 | A345 (pasture held, same row), self-checked |
| B OUTLINE 44 | 0.115 | B250 (setting), self-checked |
| B OUTLINE 44 | 0.528 | B251 (setting), self-checked |
| B OUTLINE 68 | 7503.0 | identifier (ABS catalogue number), no row |
| B OUTLINE 68 | 322.5 | B254 (ABS eggs $322.5m, from the scan), unverified: not in a generated output |
| B OUTLINE 68 | 1.54 | B254 (eggs at $1.54 a dozen), unverified |
| B OUTLINE 70 | 378 | B255 (the "1,556/1,378" cropland-to-harvested ratio in the Alexander supplement; the tool reads 1,378 as 1 and 378), unverified: a published constant, not found in `half_index.py` |
| B OUTLINE 71 | 145 | B259 (independent rebuild, 5.77 x 25.1 Mha, `qa/reports/V05_cassidy.md`), unverified. B083 already holds "145 to 147" in its value, but the tool drops the leading number of an "N to M" value, so the lower end showed as an orphan |
| B OUTLINE 72 | 4306.0 | identifier (ABS catalogue number), no row |

Two identifiers remain as orphans in the rerun, as intended. The statement of B254 avoids the catalogue number so that 7503.0 stays an identifier.

### Weak matches (49 numbers): decisions

"new" marks a row added in this step. Where the chosen row differs from the audit's first pick the reason says why. The tool's ranking is unchanged, so the .csv still shows its own pick; this table is the decision.

| document | line | number | row | reason |
|---|---|---|---|---|
| A OUTLINE | 8 | -0.3% | A223 | its statement is this sentence; A205 holds the unrounded -0.26% |
| A OUTLINE | 8 | 48% | A264 | one-year grain store +48%; A220 is the same figure unrounded |
| A OUTLINE | 39 | 50 | B098 | list of return periods run, no figure claimed; the 50-year result is B098 (22.9) |
| A OUTLINE | 41 | 27% | A285 | dairy on good land, regional range -27.3 to +22.1 |
| A OUTLINE | 41 | 0.30 | A342 (new) | long-term benchmark low end, setting |
| A OUTLINE | 45 | 16% | A246 | waste at the national target, short term +16.4% |
| A OUTLINE | 45 | 16 | A265 | grain store equals a drought of about 16 years |
| A OUTLINE | 45 | 2% | A275 | field crops, irrigation, cropland move the short term 0 to 2.4% |
| A OUTLINE | 45 | 1.8 | A273 | national capacity 1.60 to 1.82 times the sum of regions |
| A DISCUSSION | 14 | 9.4% | A235 | livestock output +10%, long term 9.4% |
| A DISCUSSION | 14 | 18.8% | A237 | right row, but its figure is stale: see the finding below |
| A DISCUSSION | 15 | 85% | A258 | meat and eggs 5%, short term +85.0% |
| A DISCUSSION | 15 | 26% | A259 | same measure, long term +25.7% |
| A DISCUSSION | 16 | 56% | A260 | red meat 30% of meat, short term +55.6% |
| A DISCUSSION | 16 | 19% | A261 | same measure, long term +18.6% |
| A DISCUSSION | 17 | 16% | A246 | waste at the national target, short term |
| A DISCUSSION | 17 | 33% | A248 | no avoidable waste, short term +33.2% |
| A DISCUSSION | 20 | 2% | A242 | irrigated share 0.02 (A243 is its long term) |
| A DISCUSSION | 20 | 5% | A244 | irrigated share 0.05 (A245 is its long term) |
| A DISCUSSION | 21 | 0.1% | A228 | field-crop yields +10%, short term 0.1% |
| A DISCUSSION | 27 | 1.5 | A179 | margin of 1.5 times in an average year |
| A DISCUSSION | 51 | 5% | A258 | the 5% meat share measure |
| B OUTLINE | 11 | 100 | B005 | the 9 to 100 million spread |
| B OUTLINE | 12 | 16 | B091 | long-term settings, 15.6 |
| B OUTLINE | 12 | 55 | B003 | kept: the span 19 to 55 (B002 holds 55.3 alone) |
| B OUTLINE | 12 | 63 | B108 | improved, no avoidable waste, 62.9 |
| B OUTLINE | 35 | 100 | B005 | the 9 to 100 million spread |
| B OUTLINE | 44 | 12 | B253 (new) | 12 of the 13 sampled choices vary |
| B OUTLINE | 44 | 100 | B005 | the 9 to 100 million spread |
| B OUTLINE | 44 | 0.30 | B252 (new) | long-term benchmark low end, setting |
| B OUTLINE | 68 | 60 | B010 | Gifford et al. 82 and 60 |
| B OUTLINE | 68 | 109 | B015 | kept: "recipe reproduces their 109 and 96 (108.9 and 95.7)"; B008 holds the published pair |
| B OUTLINE | 68 | 96 | B015 | as above |
| B OUTLINE | 70 | 2% | B058 | "an independent rebuild agrees within 2%" is in its statement |
| B OUTLINE | 71 | 59% | B257 (new) | Cassidy's published delivered fraction; B072 holds the rebuilt 61% and the paper values only in its notes |
| B OUTLINE | 71 | 5% | B258 (new) | V05 verdict, within 5% for Australia |
| B OUTLINE | 71 | 8% | B258 (new) | V05 verdict, within 8% for the world |
| B OUTLINE | 72 | 36% | B256 (new) | second build of the Simpson footprint puts pasture 36% high (2.385 against 1.758); B033 carries it only in its notes |
| B OUTLINE | 73 | 6% | B130 | failure probability 5.8 to 6.1% at the 2025 population |
| B OUTLINE | 73 | 7% | B131 | failure probability 6.7 to 7.1% at the 2011 population |
| B SECTION7 | 21 | 30.8 | B096 | worst year of 10, 2025-fixed (B134 states the same sentence) |
| B SECTION7 | 21 | 10 | B096 | the 1-in-10 level |
| B SECTION7 | 21 | 100 | B001 | worst of 100 years, 18.9 |
| B SECTION7 | 21 | 6% | B130 | failure risk a year, not B217 (6.2 ha) |
| B SECTION7 | 21 | 7% | B131 | failure risk in 2011, not B249 (HALF, India 7% low) |
| B SECTION7 | 28 | 30 | B222 | the 30 to 32 million meat count |
| B SECTION7 | 37 | 2% | B058 | independent HALF rebuild agrees within 2% |
| B SECTION7 | 38 | 6.2 | B217 | kept: 6.2 ha a person on the default diet |
| B SECTION7 | 47 | 12 | none | item numbers of the reporting checklist ("items 1 and 9 to 12"), not a claim; no row |

Of the 49 numbers, 13 keep the audit's first pick, 28 are reassigned to another existing row (one of them, the list of return periods, points to the row for the 50-year run), 7 are tied to 6 new rows (A342, B252, B253, B256, B257, B258; B258 serves both 5% and 8%) and 1 needs no row (checklist numbering).

### Findings to decide (not changed, outside this brief)

* **Stale measures rows.** `analysis/paper_a/measures.csv` was regenerated at 11:26 on 2026-11-07, after the livestock row set was widened in `long_term_and_measures.mjs`. It now reads livestock output +10% 45.5 (+9.7%) short and 17.1 (+9.4%) long; +20% 49.6 (+19.4%) short and 18.6 (+18.8%) long; all yields +10% 45.7 (+10.0%) short and 17.2 (+10.0%) long. The register still holds the earlier figures: A234 (9.6%, status independently verified), A236 (49.5, 19.2%), A237 (18.7%), A238 (45.6, 9.8%), A239 (9.8%), and the text of A275 ("+9.6%"). DISCUSSION_MEASURES.md line 14 agrees with the csv, so the register is the stale side. I did not add a duplicate row for 18.8%; the rows should be corrected in place and the verified status of A234 reconsidered. The first-run audit also tied 9.7% to A323 (9.7 million, biofuel) and 19.4% to B115 (19.4 million) as strong matches; both are wrong rows.
* **Lower-end orphan cause.** The tool drops the leading number in a value written "N to M" (found with 145 to 147). Any other register value of that form hides its lower end from the audit.
* **Long-term benchmark influence.** The sensitivity README says the influence of the long-term benchmark is 0 in every zone. That holds for 2025-fixed and 2025-mirror, but 2025-improved shows up to 0.012 in 101 of 120 rows (see B253 notes).
* **Alexander recipe constant.** 1,556/1,378 (B255) is not found in `half_index.py`; whether the rebuild applies it is not checked here.

### Follow-ups from B32 (step 4)

* (a) B117, B119, B120 set to the current Monte Carlo figures, confirmed in `analysis/sensitivity_2025/monte_carlo_2025-fixed_all_summary.csv` (zone 1): short term herd and meat window 0.806 gives 81; long term resilience table 0.521 gives 52; long term herd and meat window 0.363 gives 36. Status `self-checked (rerun 2026-11-07)`.
* (b) B046 statement now reads "140 to 343 million", agreeing with its value, `cross_method.csv` (140 and 343) and V04.
* (c) B112 and B113 are `independently verified` (verifier report `qa/reports/V14_ranges_recheck.md`, commit 1a51ffe). B110, B111, B114, B115 are `self-checked (rerun 2026-11-07)`; their figures agree with the _all summary csv of each release (43.4 to 54.3 and 11.8 to 16.0 mirror; 46.2 to 60.1 and 15.9 to 19.4 improved).
* (d) B088 to B093 are `self-checked (evaluator route; a second implementation against the original workbook is pending, V15)`.
* (e) B159 and B187 confirmed current (41.5 with 36.3 to 45.8; 53.6 with 46.2 to 60.1; 45.764 / 36.333 = 1.26) and set to `self-checked (rerun 2026-11-07)`.
