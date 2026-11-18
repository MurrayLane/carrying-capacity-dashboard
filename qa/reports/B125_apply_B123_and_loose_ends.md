# B125: B123 (checked V44) and B119 applied to the registers; loose ends

Brief: `qa/briefs/B125_apply_B123_and_loose_ends.md`. No git, no subagents, no network. Written: `qa/claims_register.csv`, `qa/references.csv`, `qa/defects.csv`, `analysis/method_tests_2025/bases_fidelity.py` and what it regenerates, `analysis/method_tests_2025/harmonised_lines.py` (the script that writes `cross_method_local.csv`), `analysis/method_tests_2025/README.md`, `analysis/paper_a/README.md`, the two `papers/*/draft/references.md` (written by `make_references.py`, as the brief allows), and this report. No paper file otherwise, no frozen release, nothing under `results/`.

Checks: register 789 to 805 lines (788 to 804 rows), 18 columns on every row, CRLF kept, the 773 untouched rows byte-identical when serialised (only the 15 listed rows differ), all `depends_on` ids exist, no em dash in anything I wrote (four em dashes in `references.csv` were already there, in source titles). `defects.csv` 138 to 139 lines, 8 columns, CRLF kept, only X130, X131, X137 changed and X139 added. `references.csv` 190 rows, only the seven second-hand rows changed. `bases_fidelity.py --check`: 0 mismatches. `make_readme_tables.py --write --only bases,intake_variant,gap_attribution,fidelity` run twice: the second run leaves the README byte-identical. Tier A: `value` and `statement` of every Tier A row equal the old row (asserted).

## 1. Tier A rows marked pending (value and statement NOT changed)

Each has `; pending gate 5 (2026-11-18): new value <x> per B123, checked V44 (...)` added to `notes`, `status` as shown, V44 added to `verifier_report`.

| Id | Value kept | Pending value (B123, V44) | Status now |
|---|---|---|---|
| A014 | 30.8 | 30.8, widened range 23.1 to 36.5 million (23.0989 to 36.5018; median 28.9); 27.6 inside; replaces the 13-choice pending range of B112 | independently verified; new value pending gate 5 (B123, V44) |
| A183 | 1.12 | 1.12, widened range 0.84 to 1.32 (0.837 to 1.322) | same |
| A187 | 0.95 | 0.95, widened range 0.72 to 1.13 (0.715 to 1.130) | same |
| A196 | 0.89; 0.95 | base holds; 37.0% of widened draws under 27.6 million at 1 in 10, 77.65% at 1 in 20 (0.45% average year): neither "feeds itself at 1 in 10" nor "not at 1 in 20" holds across the range | independently verified; new value pending gate 4 (B92a); new value pending gate 5 (B123, V44) |
| B046 | 103 to 343 | 146.2 to 343.4 on 2021-23 yields, 103 at 1990 world yields as qualifier | independently verified; new value pending gate 5 (B113, V39); new value pending gate 5 (B123, V44) |
| B156 | 103 to 343; 12 to 41 | secondary 133.8 to 343.4 aggregate, footprint 146.2 to 343.4; **new statement: "134 to 343 million on current yields" in place of "146 to 343"** (V44 amendment: the group's low is the energy and protein balance, 133.8) | independently verified; new statement pending gate 4 (B92b); new value pending gate 5 (B113, V39); new value and statement pending gate 5 (B123, V44) |

Where the row already carried a pending text for a different quantity (gate 4, or B113 on B046 and B156) it is kept in front, as B122 did. For A014, A183, A187 the B112 pending range is superseded by the B123 one (both stay in `notes`), so `status` is the form the brief gives.

## 2. Tier B and C rows changed (id; before; after)

Status is `independently verified (B123, V44, 2026-11-18)` unless stated; each row has a `B125 2026-11-18 (from B123, checked V44): before; after` note.

| Id | Before | After |
|---|---|---|
| A195 | statement: "23.0 to 29.0 across the 13-choice Monte Carlo range, 25.0 to 27.8 on the herd-cycle draws" | "19.7 to 31.2 across the widened 19-choice Monte Carlo range; 23.0 to 29.0 on the 13-choice draws, 25.0 to 27.8 on the herd-cycle draws"; value 26.3; 18.9 kept; locator gains `shocks_ranges_wide.csv` |
| A390 | note: widened shocked range "not computed" | note points to row A404; value and statement unchanged (A391, A392 untouched; their widened companions are new rows A404 to A412) |
| A308 | 22; 22; 20 | "21; 22; 20 (one population for all three); 22; 22; 20 (published on its own release's population)"; statement carries both; file `method_status-3.csv` |
| A310 | 39; 35; 36 | "37; 35; 36 (one population for all three); 39; 35; 36 (published on its own release's population)" |
| B144 | fish 25 kg (value `...; 25`) | fish 24 kg (`...; 24`); 24.46 on the 2021-23 head count |
| B247 | value "3 to 8; 103 to 343" | "3 to 8; 146.2 to 343.4" (103 is the 1990-yield qualifier); statement already said 146 to 343 |
| B350 | locator "csv prints 103 to 343 and 2.48 to 8.27"; status "with notes" | locator names the regenerated cells (146.2 to 343.4; 133.8 to 343.4; 3.52 to 8.27 and 3.22 to 8.27 times); note: aggregate low over improved is 2.50 on rounded 53.6, 2.49 on the unrounded improved capacity (V44) |
| B372 | "26.20 million; Foran and Poldy's script uses the 2021-22 mean, 26.08"; value `26.20; 26.08` | "26.20 million, ... which Foran and Poldy's script now uses too"; value `26.20`; locator 26.2 |
| B384 | meat 41.1 (0.99), 48.1 (1.16), 58.1 (1.40); fish 12.0, 19.7 (0.47), 17.9 (0.43); value `48.1; 58.1; 19.7; 17.9` | meat 41.3, 48.3 (1.16), 58.4 (1.41); fish 12.1, 19.8 (0.48), 18.0; value `48.3; 58.4; 19.8; 18.0`. Status says the head count and supply readings are V44's and the intake figures are the builder's (same eaten shares applied; no checker reran them) |

B372 and B384 are the claim rows that carried the old head-count figure (item 2). **B274 (Tier A) is not changed**: its value (41; 12; 127; 0.99) holds in whole millions; its note still says "the script divides by the 2021-22 mean population", now out of date. The coordinator can add a note at gate 5.

Held with no edit, as B123 says they hold: A143, A144, A151, A309, A311. A143's and A144's `script` and `note` text still says "not rerun on 2011-fixed-3"; `long_term_regions-3.csv` now exists (new row A417).

## 3. Rows added (A404 to A419; 16 rows, Tier B)

| Ids | What | Status |
|---|---|---|
| A404, A405, A406 | widened shocked percentiles and medians, Australia: 1 in 10 23.1 to 36.5 (median 28.9; central 30.8); 1 in 20 19.7 to 31.2 (24.7; 26.3); average year 31.1 to 49.2 (39.0; 41.5). The own-table variant is described in notes as "an extra fifty-fifty choice of resilience table added at the shock" (V44) | independently verified (B123, V44) |
| A407, A408, A409 | shares of draws below 27.6 million: 1 in 10 37.0% (740 of 2,000); 1 in 20 77.65% (1,553); average year 0.45% (9) | same |
| A410, A411, A412 | capacity over population ranges and people over capacity at p95, central, p5: 0.84 to 1.32 (0.756; 0.896; 1.195); 0.72 to 1.13 (0.885; 1.049; 1.399); 1.13 to 1.78 (0.561; 0.665; 0.887) | same |
| A413 | 27.6 million inside both shocked ranges; the herd-cycle result does not carry | same |
| A414, A415, A416 | `-3` method-status counts on both footings: one population 21, 22, 20 short and 37, 35, 36 long; published on its own population 22 and 39; status changes 1; 2; 2; 1 with names | same |
| A417 | 2011-fixed-3 long term: 18 under, 35 over, 93.4% of people in over-capacity regions (17, 36, 93.8% on 2011-fixed) | same |
| A418 | failure probability: linear in T 17.1 years 5.84%, linear in log T 16.4 years 6.10% (Paper A S8 sentence reconciled with Paper B 5.8 to 6.1%) | **unverified: no checker yet**. I recomputed it from `fearnside_failure_curve.csv` capacities (5.835% and 6.097% unrounded) |
| A419 | scope: regional tipping counts stand on 13-choice zone ranges; widened draws are national and state only | independently verified with the limit stated (V44 checked the state columns only) |

Not added: the state rows of `shocks_ranges_wide.csv` (Queensland inside its 1-in-10 range at 46.7%, no state inside at 1 in 20); V44 checked NSW-ACT and Queensland on 200 draws only, and the brief did not list them.

## 4. Defects

* Closed: X130 (generator wording; `fixed_in` B123, V44 shows a rerun leaves README and csv files byte-identical), X131 (`cross_method_local.csv`; B123 and B125), X137 (`foran_poldy_balance.py`, B123; plus the second script, B125).
* Added and closed: **X139**, `bases_fidelity.py` line 68 head count, with the cells changed (section 5).
* Still open: X129 (default rerun of `decompose_corrected.mjs` drops the V29 paragraph), X138.

## 5. `bases_fidelity.py` head-count fix: cells changed

Line 68 now divides by the 2021 to 2023 mean (26.203 million), as `foran_poldy_balance.py` does. The two texts that said "2021-22" now say "2021-23".

* `bases.csv` (rows 10 and 11, Foran and Poldy): population 26.08 to 26.2 (both rows); row 10 basis "...2021-22 mean head count" to "...2021-23 mean head count"; row 11 basis "FAO food use per person on the 2021-22 mean head count (the method script; under 0.5% from the three-year 26.20)" to "...2021-23 mean head count (the method script)".
* `intake_variant.csv`: meat supply 41.1 to 41.3, FAO factor 48.1 to 48.3, model factors 58.1 to 58.4, ratio on model factors 1.4 to 1.41; fish supply 12.0 to 12.1, FAO factor 19.7 to 19.8, ratio on FAO factor 0.47 to 0.48, model factors 17.9 to 18.0; grain supply 126.6 to 126.8, intake share on FAO 0.9229 to 0.9232, FAO factor 137.2 to 137.3, share on model factors 0.9166 to 0.9169, model factors 138.1 to 138.2.
* `gap_attribution_readable.csv` and `fidelity.csv`: **byte-identical** (B123 expected the first to change; its Foran and Poldy rows are 1997-98 production, not the head count).
* `README.md`: the generated bases table (rows 373 and 374) and intake table (meat and fish rows), the source-commit stamps of the four generated blocks (the tool's own output), the Population bullet (line 383, now says the script uses the 2021-23 mean and took 2021-22 until B125), and the "commodity balance changes side" bullet (41.3, 48.3, 58.4; 12.1, 19.8, 18.0).
* Not changed: `harmonised_comparison.csv` prints Foran and Poldy meat 41.0, fish 12.0, grain 127.0 (whole millions, written by `harmonised_comparison.py`, outside my write list); `bases_fidelity.py`'s own cross-check accepts it (41.28 against 41.0). README lines 288 and 562 print integers and do not move.

## 6. `cross_method_local.csv`

`harmonised_lines.py` now reads the widened average-year range from `analysis/paper_a/shocks_ranges_wide.csv` (zone 1, return period 1, 5th and 95th percentile, to one decimal). Two rows changed (nothing else; `harmonised_comparison_lines.csv` is byte-identical):

* "The model, thesis method corrected": reading `41.5 (36.3 to 45.8)` to `41.5 (31.1 to 49.2)`; low 36.3 to 31.1; high 45.8 to 49.2; over corrected 0.87 and 1.1 to 0.75 and 1.19; over improved 0.68 and 0.85 to 0.58 and 0.92; source to the wide csv and "(average year; 5th to 95th percentile of 2,000 draws on 19 choices, decision 115)".
* "The model, improved": only the source text (it keeps 46.2 to 60.1, the 13-choice range; no widened draws exist for the improved method).

README: no table in it repeats the model reference rows, so I added one bullet to the cross-method section stating them, and the sentence that the older tables (`cross_method.csv`, README lines 274, 290, 298, 322) still print 36.3 to 45.8 (written by `cross_method.py`, not changed). The secondary rows were already regenerated in B123 and match the README (146.2 to 343.4; 133.8 to 343.4; 3.52 to 8.27; 2.73 to 6.41; 3.22 to 8.27; 2.50 to 6.41).

`analysis/paper_a/README.md` (B123 section): the own-table paragraph now reads as "an extra fifty-fifty choice of resilience table added at the shock", not each draw's own table, with the reason (V44). The csv name `shocks_ranges_wide_own_table.csv` and the wording in the comment of `shocks_ranges.mjs` still use the old label; both are outside my write list.

## 7. `references.csv` `cited_in`: rows changed

| Id | `cited_in` before | After (author, year only); ids and pages moved to `notes` |
|---|---|---|
| L001 | House of Representatives Standing Committee for Long Term Strategies 1994 (the Jones report, L006), footnote 13 | House of Representatives Standing Committee for Long Term Strategies, 1994 |
| L002 | Henry and Godden 1995 (L003), p. 98 and the reference list on p. 103 | Henry and Godden, 1995 |
| L004 | the Jones report (L006), footnote 12 | House of Representatives Standing Committee for Long Term Strategies, 1994 |
| L005 | the Jones report (L006) | same |
| L035 | Henry and Godden 1995 (L003), p. 98 | Henry and Godden, 1995 |
| L036 | Henry and Godden 1995 (L003), p. 97 (reported in Clarke) | Henry and Godden, 1995 |
| L068 | Lane 2014 thesis (L020), pp. 201 to 202 | Lane, 2014 |

Each `notes` cell gained "Second-hand: read in <old text> (the paper prints only the author and year; register ids and pages are kept here, B125)." `make_references.py A` and `B` were run (no tool edit was needed: `render_csv` already prints `cited_in`). All seven print `(cited in Author, year)` with nothing else in that bracket (A: L002; B: L001, L002, L004, L005, L035, L036, L068); the CHECK text sits in its own bracket after it. The two `references.md` files changed in those lines only (A one line, B seven). The B file has 130 entries because the tool reads the drafter notes (B119: 127 when they are stripped).

**CHECK lines left (A: 17; B: 26)**

* Place of publication (or publisher or editors) missing. A: L063 AUS-MEAT 2005; L228 Centre for Population 2026; L010 CSIRO 2025; L230 Department of Climate Change 2017; L231 Department of Climate Change 2019 (also publisher and the Arcadis author line); L060 Geoscience Australia and ABARE 2010 (also publisher; the chapter file has no title page); L144 Davies 2024, L170 Hughes 2017 (also page range), L171 Sysak 2017 (book editors and place; need the book title pages); L020 Lane 2014; L226 Treasury 2023; L062 USDA 1992. B adds: L051 ABS 1994; L227 Treasury 2021; L250 FIAL 2021; L034 Gutteridge 2005 (publisher too); L134 Wackernagel 1994; L050 Wackernagel 1996 (also edition and year); L036, L068, L035 (below). Each needs the title page imprint of the file on disk.
* Author initials, author form or year. A: L241 ABARES 2026 (corporate in the prose, four named authors on the page: a decision on the form); L242 Department of Climate Change (no year: "n.d." or find a date). B adds: L068 Buzby 2010 (initials, title, publisher, place; unidentified); L035 Nix (initials, year, title, publisher, place; unidentified); L004 (the prose says Borrie, the author line is the inquiry); L143 Chisholm 2000 (volume; the page spells Chisolm).
* Not seen. A and B: L247 Saltelli 2010 and L248 Jansen 1999 (Murray fetches). B: L036, L005, L004, L035, L001 second-hand, no copy of the cited work.
* Other. A and B: L002 Gifford 1975 (DOI "none found"; second-hand, so the DOI is expected to stay empty). B: L067 AUSNUT 2007 (URL, date accessed, version); L041 Fairlie 2008 (volume, pages, DOI; the file is a later chapter version); L099 Productivity Commission 2011 (title, place, series).
* L251 Rawtec 2022 and L252 NHMRC 2006 and L253 ABS 2011 no longer print a CHECK on the current run (the "author initials" line for Rawtec that B119 saw is gone); L252's confirm-year-and-tables note and L253's issue question (decision 2 below) remain in the register.

## 8. Literature from B119: the "can come off" rows (claims csv files not edited)

B119 section 9 named lines that have since moved (B124 trimmed Paper A's csvs). The list below is the current position, found by searching each file for "not seen". It is 30 rows resting on 24 works; **25 rows can come off** (20 works read: the brief's "20" counts works, not rows).

Come off (the label and the text "(decision 111: the label is kept here, not in the prose)" with it):
* `papers/A_results/draft/A_s01-04_claims.csv`: lines 33 (L013, L014), 34 (L013, L014), 52 (L012, L013, L014, L020), 68 (L060, L062, L063), 70 (L062, L063), 85 (L013, L014).
* `A_s05-08_claims.csv`: lines 10 (L013), 13 (L073, L074), 57 (L115, L116, L117), 58 (L014, L020).
* `A_s09-12_claims.csv`: lines 68 (L013), 69 (L013), 90 (L096, L097, L120).
* `A_results/draft/supplementary_claims.csv`: lines 133 (L062), 134 (L063), 263 (L012, L013, L014, L020).
* `papers/B_methods/draft/B_s01-03_claims.csv`: lines 82 (L012, L013, L014), 83 (L073).
* `B_s04-05_claims.csv`: line 229 (L074).
* `B_s06-09_claims.csv`: line 130 (L084).
* `B_methods/draft/supplementary_claims.csv`: lines 320 (L124), 322 (L131), 324 (L116), 325 (L096), 327 (L236).

Changes rather than comes off: `A_s09-12_claims.csv` line 81 (L002, L003): "not seen" to "second-hand, read in L003 p. 98".
Stay "not seen": `A_s01-04_claims.csv` line 140 (L080 Kastner); `B_methods/draft/supplementary_claims.csv` lines 321 (L086 Goldfinger), 323 (L080), 326 (L235 McKay et al.).

Paper B prose: "Burnside bin audit" should read Rawtec 2022 in `papers/B_methods/draft/supplementary.md` lines 175, 176 and 304 (and `supplementary_claims.csv` line 312). The register rows with the same wording are B366 (statement and notes); I did not change them (not asked).

## 9. Old table numbers (item 6)

None to update. Searching every column of `qa/claims_register.csv` and all of `analysis/pasture_2025/README.md` for "Table 5", "Table 6", "Table 7" (and the "main text" and "Paper B" forms near "Table") finds only Henry and Godden Table 5 (B008, B009, B010) and FIAL Table 5 (B366), which are the sources' own tables. The pasture README has no table reference of that kind.

## 10. Paper patches this job found (not made)

* Paper B `papers/B_methods/draft/supplementary.md`, Table S8: row "Aggregate methods, secondary (2021-23 yields)" improved column 2.50 to 6.40 should read 2.50 to 6.41 (the csv now prints 6.41); row "Footprint, secondary" improved column is blank and the csv has 2.73 to 6.41. B156 statement (once the coordinator takes the pending statement at gate 5): "134 to 343" where the register and the paper say "146 to 343" (Paper B Table 3 row, `B_s04-05.md` line 134, reads 146 to 343 for the footprint food row alone, which is right for that row).
* Paper A: nothing new from this job. B124 already carries the widened ranges; the 2011 method counts in the text are the corrected 35 and improved 36, which do not move; the published counts (22 and 39 against 21 and 37) appear in no paper sentence.
* Claims csvs: the label list in section 8.

## 11. Decisions for the coordinator

| # | Row | Choice made | Recommendation |
|---|---|---|---|
| 1 | Which ABS 7215.0 issue the meat calibration reads (L064, edition year not recorded, against L253, the December 2010 issue, read and filed) | Both rows untouched | Name the issue in supplement Table S3a row 4; if it is December 2010, L064 becomes a duplicate of L253 and can be marked superseded |
| 2 | Published method's 2011 population: its own release's (22 and 39) or the `-3` one (21 and 37) | A308, A310 carry both, one population first (V44's preference: the comparison then isolates the method) | Murray picks which the papers print; neither paper prints either today |
| 3 | `cross_method.csv`, `cross_method.py` and the README tables above the B113 section still print the corrected model as 36.3 to 45.8 | Not changed (outside the write list); `cross_method_local.csv` now shows 31.1 to 49.2 | Decide whether `cross_method.py` also takes the widened range, so the two csv files agree |
| 4 | The improved model's reference row keeps its 13-choice range (46.2 to 60.1) | Labelled in the source cell | Leave, or run widened draws for the improved release |
| 5 | Footprint secondary row leaves out build 2 (139.4 to 277.7 on 2021-23 yields; no primary reading) | As B123 built it | V44 note: adding it would read 139.4 to 343.4 (3.36 times); keep, and say so in the row text |
| 6 | B384 intake figures after the head-count change are the builder's, not rerun by a checker | Status says so | Include in the next checker job (V45) with A418 |
| 7 | A418 failure-probability reconciliation: status unverified | Row added | A checker reproduces 5.84% and 6.10% |
| 8 | A038, A184, A188, A402 cannot be computed on the widened basis (no regional draws; script stops at zone 45 on a 152 km2 land difference) | Rows unchanged; A419 states the scope | Decide whether the zone-45 land difference is to be fixed so regional widened draws can run |

## 12. Register rows touched

Changed (15): A014, A183, A187, A196, B046, B156 (Tier A, pending, value and statement unchanged); A195, A308, A310, A390, B144, B247, B350, B372, B384. Added (16): A404 to A419. Defects: X130, X131, X137 changed; X139 added. References: L001, L002, L004, L005, L035, L036, L068.

## Wrong-value check

Wrong-value check: A014 (Tier A, value 30.8, statement "leaves a national capacity of 30.8 million people") has a new widened range of 23.1 to 36.5 million. Writing `value` = "23.1 to 36.5" into the row would be the wrong move, and it was NOT done: the 30.8 stays in `value` and the statement is untouched; the range is in `notes` as "; pending gate 5 (2026-11-18): new value 30.8 with a widened range of 23.1 to 36.5 million ... per B123, checked V44" and in `status` as "independently verified; new value pending gate 5 (B123, V44)". The same assertion (`value` and `statement` equal the old row) passed for all Tier A rows of the register. A second check from the data: with `shocks_ranges_wide.csv` zone 1, return period 10, the 5th percentile is 23,098,884; quoting the 13-choice 27.0 for it would not match.
