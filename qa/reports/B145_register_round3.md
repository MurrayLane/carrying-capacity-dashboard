# B145: registers after the round-three patches and the figures

Builder report. Brief `qa/briefs/B145_register_round3.md` plus the coordinator's addition (V57b references items). No git, no subagents, no network. Written: `qa/claims_register.csv`, `qa/references.csv`, `qa/literature_register.csv`, `qa/defects.csv`, `papers/A_results/draft/references.md` and `papers/B_methods/draft/references.md` (tool only; A `--style springer`, B default) and this report. No paper section file, frozen release or `results/` file touched. Tier A `value` and `statement` unchanged on every Tier A row.

## 1. Claims register (894 data rows become 917; 23 added, 14 changed)

### Rows changed (id; tier; before; after)

| Id | Tier | Before | After |
|---|---|---|---|
| B247 | B | cause clause "a sufficient cause of the gap (pool 18% ... 60% ...), not shown to be the only one"; independently verified (B139, V53) | clause: not shown to be a sufficient cause; pooling rule 18% of the 34.5 million gap at HALF's exchange rate, 60% of a larger gap from 113.6; the gap to HALF closes only at equal energy (81.7, protein 93 to 81 g) or equal energy and protein (85.4). Value unchanged. Status independently verified (B146b, V40 and V53, 2026-11-18); clause wording is the builder's |
| B410 | B | "a sufficient cause ... and one of several" | same replacement. Last clause (diet the largest feature) not changed and flagged: 5.14 lists the requirement (+36.2) and waste (-17.9) as larger terms than the pasture-fed layer (-13.0) |
| B238 | B | purpose 1: FAIL well suited, LDB well suited; independently verified (V31d) | FAIL partly suited, LDB partly suited; self-checked (B146b, 2026-11-18); author's judgement, second rater has not seen it |
| B242 | C | "rates seven methods"; value 7; 4 | "five published methods and the author's model (six columns in Table 9)"; value 6; 4; self-checked (B146b) |
| B153 | A | independently verified | Tier A: value (12 to 41) and statement unchanged; status "statement wording pending gate 6". **The paper supports the value 12 to 41 and a narrowed statement** (5.10: grain 127 to 128 never binds; V56b section 7). Proposed statement is in the row's notes |
| B130, B137 | A | pending gate 6 | note only: failure view rated partly suited for food security; values unchanged |
| A328 | B | 24.6; 23.6 (applied in B142) | unchanged; note: draft prints 23.6 and no 23.7% remains in the main text or supplement |
| A220 | A | independently verified; approved gate 5 | note; status adds "statement wording pending gate 6" (statement says improved reference, draft states the corrected release with the store table); value unchanged |
| A036, A038, A184, A196, A009 | A | pending gate 6 | note only that the draft prints the pending values; unchanged |

Retired rows: none set. A search of the register for rows that exist only for a sentence B143a, B143b or B146a retired found none: the retired sentences lived in the papers' claims csvs, and the register rows behind them (Swan 0.01 A052, Eyre Peninsula A060, Murrumbidgee A054, Northern Gulf A150, B005 and B192 for the factor 10.6) are data facts that other live rows or tables still cite or that are Tier A pending rows. A150 (cited by no csv) has a README source and was left as it is.

### Rows added (Tier B, series continued)

Paper B: B428 footprint line (c) 98.0 to 176.9 (2.36 to 4.26 times; printed 2.4 to 4.3); B429 HALF 114.9 (2.77); B430 energy and protein balance 219.6 to 225.0 (5.29 to 5.42); B431 Figure 2 counts (19; 5; 76); B432 the 19 line (c) readings as plotted; B433 pasture-alone as-run 316.9 and 385.7; B434 commodity balance 12 to 128 against 12 to 41; B435 section 6.2 first-order identity (41.27, 41.17, 41.50); B436 waste 1.33 against 1.14; B437 variant 1 protein 93 to 81 g; B438 kcal to MJ (2,892 = 12.1; 1,912 = 8.0).
Paper A: A468 the 53-unit partition comparison (68 to 81 against 33; from A122, A123); A469 climate-phase statement (status unverified: Millennium Drought label rests on one README line, La Nina years have no held source); A470 livestock denominator (code lines 38 to 63; self-checked); A471 age-sex sentence (8.30 MJ, 1.038; V52); A472 Figure 8 (53; 16 over, 37 room; 3 under 0.5 mm); A473 Figure 8 labelled excesses; A474 to A479 Figure S6 (53 regions and ten scenarios; 12 and 24%; 340 and 156 litres; one and two years of grain; 6%; tip counts).
Statuses: independently verified where V40, V51, V52, V56a, V56b or V31d reached the figure (named in each row); self-checked otherwise. Every row's arithmetic was recomputed here (multiples, 1/0.88, kcal to MJ, circle counts under 0.5 mm from movers-3.csv, tip counts from scenarios_by_region.csv).

**Discrepancy with the brief:** figures.csv marks only two figures "derived" (A Figure 8 and S6), not eighteen; Paper B's figures.csv has no "derived" flag but lists numbers with no register row of their own (Figure 2 line (c) readings), which are covered by B428 to B432. The other caption numbers of the twelve figures already have rows (B167, B412, B187, B114).

**Not done (outside the brief's list):** about 100 rows marked "new row for the register job" in the Paper A csvs (B143a, B146a) and the new B146b rows in the Paper B csvs have no register ids; only the items the brief names were added.

## 2. References and literature

| | Entries before | CHECK before | Entries after | CHECK after |
|---|---|---|---|---|
| Paper A (springer) | 57 | 18 | 56 | 17 |
| Paper B (default) | 129 | 30 | 128 | 29 |

* The five first-time Paper A citations (Cohen L049, Peters L015, Zumkehr and Campbell L103, Fader L105, Gerten L083) were checked field by field against the files on disk (Literature review and Comparators folders); `source_of_fields` now reads "pdf on disk (opened B145); crossref" and no CHECK is on them. Cohen: the register holds no book details; the file and the cited work are the Science article. Gerten: the file is the accepted manuscript, so no journal page can be cited from it.
* ABARES 2026a (L241) marked "uncited in A" (it leaves Paper A's list; Paper B never cited it). PMSEIC 2010 (L136) kept: cited in S9 only. Mottet (L122): record-only row added to references.csv, status uncited, DOI recorded.
* Addition items: Buzby L068 marked "uncited in B"; L035 and L036 marked uncited ("as cited in Henry and Godden (1995)"); "Murray fetches" reworded to "to be obtained" in L247, L248 and L252 (no list prints a person's name); companion paper added as L259 in both references.csv and literature_register.csv (status "companion paper; status to update at submission"); Mottet row set to record only.
* **The tool does not honour three of these, and I did not edit it (not in my write list).** (a) Buzby and Mottet are still listed in B: `make_references.py` scans the drafter-notes blocks (B_s06-09.md line 245, B_s01-03.md line 112) and "keeps uncited rows the prose cites". (b) Migration Committee 1986 (L036) is still listed because Paper B's section 1 prints "(Migration Committee 1986)"; Nix (L035) did drop. The text has to be recast as "as cited in Henry and Godden (1995)". (c) The companion paper is not listed: "Paper A" has no year, so it needs `NAMED_CITATIONS["L259"] = ("B", "Paper A")` in the tool. Fix needed: the tool stops scanning at "## Drafter notes", plus that one entry; then the lists drop Buzby, Mottet and (after the text edit) L036, and gain L259. No em dash in either list.

Literature register: L258 added (climate-phase labels; only held source `pipeline/yields/abs_current/README.md` line 37; status "reported; a Bureau of Meteorology source to fetch: http://www.bom.gov.au/climate/enso/ and http://www.bom.gov.au/climate/drought/"); L049 status "read, p. 343 (B146a)"; L015, L049, L083, L103, L105 gain Paper A section 1.2 in used_by (L015 also section 6); L136 used in S9 only; L241 note; L122 record only with the DOI; L259 companion paper.

### The 26 fillable [CHECK] fields of Paper B's list (for the before-submit page)

| Id | Field | What is needed |
|---|---|---|
| L051 | ABS 1994 | place of publication |
| L228 | Centre for Population 2026 | place of publication |
| L010 | CSIRO and University of Queensland 2025 | place of publication |
| L230 | DCCEEW 2017 | place of publication |
| L250 | Food Innovation Australia Limited 2021 | place of publication |
| L020 | Lane 2014 | place of publication |
| L227 | Treasury 2021 | place of publication |
| L226 | Treasury 2023 | place of publication |
| L062 | USDA 1992 | place of publication |
| L134 | Wackernagel 1994 | place of publication |
| L067 | AUSNUT 2007 | URL, access date, version |
| L253 | ABS 2011 | confirm the meat calibration reads the December 2010 issue |
| L143 | Chisholm 2000 | volume; surname spelling (Chisolm on the page) |
| L231 | DCCEEW 2019 | publisher, place, whether Arcadis is named as author |
| L242 | DCCEEW n.d. | year |
| L041 | Fairlie 2008 | volume, pages, DOI if any (file is a later chapter version) |
| L060 | Geoscience Australia and ABARE 2010 | publisher, place |
| L002 | Gifford et al. 1975 | DOI if any |
| L034 | Gutteridge 2005 | publisher, place |
| L248 | Jansen 1999 | not seen, to be obtained |
| L247 | Saltelli et al. 2010 | not seen, to be obtained |
| L252 | NHMRC 2006 | not seen; confirm year, version, table numbers |
| L050 | Wackernagel and Rees 1996 | place, edition, year from the imprint |
| L001 | Taylor 1922 | end page and initials from the article |
| L005 | National Population Council 1992 | the report itself (second-hand) |
| L004 | National Population Inquiry 1975 | identity of the work cited as Borrie (second-hand) |

Not fillable from what is held: L036 Migration Committee (recast in text), L068 Buzby and L122 Mottet (drop from the list once the tool is fixed).

## 3. Defects

* Closed: X142 (fixed_in B146b; the generating `bases.csv` and `bases_fidelity.py` still carry the Buzby label), X144 (B143b; checked against the supplement text), X145 (B143a and B143b; no flagged row remains in any of the eleven claims csvs; two decision rows stay by design). X148 was already closed.
* Reviewed and left open with a note: X143, X146, X147. X141 untouched.
* Added: X149 `SECTION7_DRAFT.md` holds the old purpose 1 rating (found_by B146b, open); X150 the `measures.csv` "of cropland" label (found_by B143a, open); X151 Paper A figure scripts' loose checks (V56a; fixed_in the B144a follow-up); X152 Paper B tolerances 0.01 and 0.05 (V56b; fixed_in the B144b follow-up); X153 `numbers_lint.py` overwrote `qa/reports/numbers_lint_2026-11-07.csv` (B146b; open, the coordinator restores it).

## 4. Register rows touched

Changed: B247, B410, B238, B242, B153, B130, B137, A328, A220, A036, A038, A184, A196, A009. Added: B428 to B438, A468 to A479. Format kept (CRLF; the two blank lines as found).

## 5. Wrong-value check

Example of what was NOT done: B130 (Tier A, pending gate 6) was not overwritten with the new value. Applied outright it would have read "5.8 to 6.1% a year (short term; below 1% on crops alone)" in `statement` and `value`, replacing the register's gate-approved text with a figure that waits for Murray's approval. The row keeps its old `value` and `statement`; only a note was added. The same check was run on a computed figure: footprint line (c) top 176.9 against 117.0 x 1.5123 = 176.94 (pass); a planted 176.0 fails against the csv cell.
