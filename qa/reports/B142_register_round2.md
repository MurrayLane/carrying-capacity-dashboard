# B142: the registers after the second-round computations and patches; the Springer reference form for Paper A

Builder report. Brief: `qa/briefs/B142_register_round2.md`. No git, no subagents, no network. Written: `qa/claims_register.csv`, `qa/references.csv`, `qa/literature_register.csv`, `qa/defects.csv`, `qa/tools/make_references.py`, `papers/A_results/draft/references.md` and `papers/B_methods/draft/references.md` (both by the tool only) and this report. No paper section file, frozen release or `results/` file was touched; nothing in `papers/B_methods/` was edited by hand (B143b works there).

## 0. Summary

* **Tier A rows pending gate 6: 30.** 25 existing rows (7 for Paper A, 18 for Paper B) carry the new value in `notes` and a pending status, with `value` and `statement` unchanged; 5 new Tier A rows (4 for Paper A, 1 for Paper B) are added pending the gate. Table in section 1.
* **Claims register:** 813 data rows become 894 (81 added: 48 for Paper A, 33 for Paper B). 81 existing rows changed (33 Tier A, 48 Tier B or C); 735 of the 816 lines (header, the two blank lines in the file as found, and the rows) are byte-identical to the file as found. On every Tier A row only `status`, `verifier_report` and `notes` differ (checked by script).
* **Decision 140** applied: A363 pending (0.671; 1.455), A328 value 23.6%, A369 statement, notes on A002, A005 and A012.
* **References:** `make_references.py` has `--style springer`; Elsevier Harvard stays the default. Paper A built with `--style springer` (54 entries, 18 CHECK; before 59 and 18), Paper B with the default (128 entries, 29 CHECK; before 128 and 29). No em dash in either list.
* **Literature register:** 12 rows changed, none added (the Borrie row L004 exists). **Defects:** X140 and X118 closed, X141 left open and unchanged, X142 to X148 added.
* **Three rows the brief lists with the Tier A rows are Tier B in the register** (A418, A382, A317). No value moves on any of them, so nothing is pending; their status moves to independently verified with the checker named (section 2).

## 1. Tier A rows marked pending gate 6 (id; current; pending; job; checker)

Existing rows: `status` reads "independently verified; new value pending gate 6 (<job>, <checker>)"; `notes` gains "; pending gate 6 (2026-11-18): new value <x> per <job>, checked <checker>" with the earlier status kept in the notes; the checker's report is added to `verifier_report`. `value` and `statement` are unchanged.

| Id | Current value | Pending value | Job | Checker |
|---|---|---|---|---|
| A036 | 2: Mackay Whitsunday; North Tasmania | 0 clean and robust on the 19-choice ranges; 1 (SA Arid Lands, land-definition case) keeps its 2025 status; 7 do not | B132 | V47 |
| A038 | 2 (herd-cycle ranges); 3 (13-choice ranges) | 7: Wet Tropics; Desert Channels; Mackay Whitsunday; Rangelands; North Tasmania; Southern Gulf; Corangamite (the herd-cycle 2 and the 13-choice 3 stay as the record) | B132 | V47 |
| A184 | 21 (21 to 22 across the range) | 21 at the central figure; 19 to 26 with each region at its own end (a bracket no single draw reaches); 21 to 24 in a single draw | B132 | V47 |
| A199 | 5 (2025); 3 (2011) | 5 and 3 unchanged; on the 19-choice ranges 4 at the 95th percentile and 3 at the 5th (names in the row); 3 (2011) the same on the 2025 weather table | B132, B133 | V47, V48 |
| A196 | 0.89; 0.95 | 0.95 (0.953) in 2025; 2011 0.89 (0.894) on the thesis table, 0.95 (0.946) on the 2025 table; almost all of the fall is the table | B133 | V48 |
| A009 | 15.35 and 15.6 within 13.3 to 18.8 | levels unchanged; paired result added: short term no fall in 2,000 paired draws (2.3 to 16.5 million); long term 26.1% fall (52.2% on holdings land) | B133 | V48 |
| A363 | 0.670; 1.454 | 0.671; 1.455 (22,336,514 people; decision 140) | B138 | V52 |
| B276 | 4% (line a); 39% (line b); 0.59 to 1.42 | line (a) -1.1% to 6.8% to 41.5 (4.1% base), -1.2% to 7.8% across references; line (b) 27.7% to 45.9% (38.5% base), 23.2% to 52.8% across references, 5% to 36% to the median (9% to 36% without the combined scale-up variant); line (c) 14.7% (band 10% to 16%); factors 0.59 to 1.42 unchanged | B135, B139 | V50, V53 |
| B277 | (a) 0.65 to 0.70 and 6.2 to 7.0; (b) 0.65 to 0.44 and 6.2 to 3.7 | line (b) as before, depends on the commodity balance (widens 11.5% without it; narrows 23% to 48% with any other single method out); line (c1) 0.65 to 0.48 (26%) and 6.2 to 4.1 | B135, B139 | V50, V53 |
| B156 | 65 to 211; 133.8 to 343.4; 12 to 41 | 65 to 211 unchanged; secondary 146 to 343 (3.5 to 8 times; the energy balance has no world-average reading); 12 to 41 unchanged | B141b | V44, V54b |
| B046 | 64.8 to 117.0; 146.2 to 343.4 | values unchanged; the statement would add 3.5 to 8.3 times the model and the binding reading 53.9 to 77.9 (row B270) | B135, B141b | V50, V54b |
| B003 | 18.9 to 55.3 | 18.9 (40.4 on crops only) and 55.3 as two separate changes from 41.5, not a joint range; crop-only span 40.4 to 55.3 | B134, B139 | V49, V53 |
| B130 | 5.8 to 6.1 | 5.8 to 6.1% a year (short term, factor on every yield); below 1% a year on crops alone (a bound at the last run point) | B134, B139 | V49, V53 |
| B194 | 1.09; 1.17 to 1.33; 1.29 | 1.03 (crop-only drought) and 1.09 are the smallest factors; waste 1.17 to 1.33; the Australian settings 1.29 is a bundle outside the single-choice order | B134, B139 | V49, V53 |
| B182 | 7.88 | 7.88 unchanged, restated as an upper bound (diet C); diet A 1.60 and diet B 3.77 are new rows | B139 | V53 |
| B185 | 2.41 | 2.41 unchanged, restated as a ratio between methods (Panel B) | B139 | V53 |
| B186 | 4.43 to 6.36 | 4.43 to 6.36 unchanged, restated as ratios between methods (Panel B) | B139 | V53 |
| B001 | 18.9 | 18.9 on every yield and 40.4 on crops only | B134 | V49 |
| B096 | 30.8 | 30.8 on every yield and 41.2 on crops only | B134 | V49 |
| B137 | 18.92 to 41.5 | 18.92 to 41.5 on every yield; crop-only low end 40.45 | B134 | V49 |
| B167 | 2.19 | 2.19 on every yield and 1.03 (1.026) on crops only | B134 | V49 |
| B188 | 1.58 vs 2.14 to 6.36 | 1.58 against 2.14 to 6.36 unchanged; drops "or 2.22 from minimum to maximum"; adds the crop-only 1.03 below 1.58 | B134, B139, B141b | V49, V53, V54b |
| B193 | 4 | 4 unchanged; crop-only low ends 24.7 and 40.4 give factors 2.55 and 1.56 to 62.9 | B134 | V49 |
| B187 | 1.58 | 1.58 unchanged; the 2.22 is dropped from the paper's sentence | B141b | V54b |
| B005 | 9 to 100 | 9 to 100 unchanged; "a factor of 10.6" is not printed; ladder rows B189 to B192 (Tier A) are not in the paper and are named in the row for the digest | B141b | V54b |
| A430 (new) | none | 0 of 2,000 paired draws fall short term; difference 2.32 to 16.48 million (abstract) | B133 | V48 |
| A431 (new) | none | 26.1% of paired draws fall long term; -0.87 to +3.40 million (abstract) | B133 | V48 |
| A449 (new) | none | two diet layers add 5.6 million; land and livestock together add 2.5 million (abstract) | B137 | V51 |
| A462 (new) | none | ten-year diet window: 39.1 million (39.7 unrounded) (abstract, decision 149) | B138 | V52 |
| B402 (new) | none | line (c1) closes 14.7% of the distance, band 10% to 16% (abstract) | B139 | V53 |

Tier A rows touched with a note only (value and statement unchanged, nothing pending): A001, A002, A003, A005, A014, A039, A088, A223. A184's V47 note and A039's V47 wording ("its 2025 status holds in every draw") are in their notes.

Named but not marked: A418, A382 and A317 are Tier B in the register; B189 to B192 are Tier A rows that V54b says are not in Paper B (named in B005's note, not changed).

## 2. Tier B and C rows changed (id; tier; before; after; job, checker)

Rule used: a row is "applied" (value or statement changed, status `independently verified (<job>, <checker>, 2026-11-18)`) when the checker reproduced the figure the change rests on; the earlier status, value and statement are kept in the note as "status was", "value was" and "statement was". Where the builder's proposal is a wording point on a figure the checker did not reach at row level, the row gets a note only and its status is left as it was.

Value changed:

| Id | Tier | Before | After | Job, checker |
|---|---|---|---|---|
| A041 | B | 1: SA Arid Lands | 2: Desert Channels; SA Arid Lands | B132, V47 |
| A042 | B | short 3 and 3; long 2 and 1 | short 3 and 7; long 2 and 2 | B132, V47 |
| A043 | B | 6 against 2; 3 against 1 | 6 against 0; 3 against 1 | B132, V47 |
| A188 | B | 24 | 24; 22; 26; 24 to 25 | B132, V47 |
| A402 | B | 21; 21; 22; 24 | 21; 19; 26; 7; 24; 22; 26; 4 | B132, V47 |
| A419 | B | no regional widened draws | widened regional draws exist (all 60 zones) | B132, V47 |
| A328 | B | 24.6; 23.7 | 24.6; 23.6 | B138, V52 |
| B095, B097, B098 | B | 37.0; 26.3; 22.9 | each with its crop-only companion 41.4; 41.0; 40.8 | B134, V49 |
| B099 to B103 | B | 47.9; 39.9; 34.3; 29.9; 24.7 | each with an approximate crop-only companion 53.5; 53.2; 52.8; 52.5; 52.0 | B134, V49 |
| B134 | B | 26; 54 | 26; 54; 0.8; 2.5 | B134, V49 |
| B157 | B | 30.8; 18.9 | 30.8; 18.9; 41.2 (crops only); 40.4 (crops only) | B134, V49 |
| B333 | B | 1.09; 1.17 to 1.33; 1.29; 2.14; 2.19; 2.41; 2.66; 2.67; 4.43 to 6.36; 7.88 | Table 8 panel A order: 1.03; 1.09; 1.17; 1.27; 1.33; 1.48; 1.60; 1.76 to 1.78; 2.14; 2.19; 2.67; 3.77; bundles 1.29 and 2.66; upper bound 7.88 | B139, V53 |

Statement amended (value unchanged): A013 (26.1% of paired draws fall; "not because capacity fell" is not established), A056 (19-choice 5th percentile 148,681 below the population), A339 (tested with the 19-choice ranges file), A343 (not a clean flip; one of seven inside its range), A369 (the national 2011 row becomes the regional sum, decision 140), B243 and B364 (the drought allowance has two values, 2.19 and 1.03), B245 (30.8 holds with the factor on every yield; 41.2 on crops alone), B247 (the cause clause rewritten from the bridge; pairing a sufficient cause, not the only one), B270 (output over consumption ratios; binding land type 53.9 to 77.9 million, 1.30 to 1.88 times), B369 (one-at-a-time PAL ends 48.0 and 26.9).

Note only (status unchanged unless stated): B138, B198, B199, B218, B224, B226, B230, B238 (crop-only companions or the "only with the factor on every yield" qualifier); B262 and B374 (the production comparison behind 363.5 Mha); B363, A072 (the paired draws meet the stated need); A012 (decision 140, 24% either way); A376 and A380 (the diet-window effect is a different measure from the decomposition term); B371 (PAL ends as context). Status moved with a note: A418 (V48 stands as the checker; base values 5.84 and 6.10 reproduced), A382 (V51 reproduces every eight-layer cell; source of Table 2), A317 (V51 reproduces all 128 year cells; as-built 43.5 to 55.4 independently verified; 43.3 to 55.8 where the series is held; restating is a decision; X118 closed).

Checker amendments taken: V47 (A402 and A184 name the single-draw 21 to 24 as the count a year can show; the 19 and 26 bracket every region at its own end), V48 (A196 "almost all the table"; A430 "for 2025"; failure range anchors named), V49 (B130 "short term"; the 93% to 98% share; "an illustration, not a bound"), V50 (line (b) median low end 5.4%, "-1% to 8% across references", "about 87%", "smaller surplus"), V51 (S4 "all meats", "consistency check"; loo caveat), V52 (national-vector partition only; crops-only 2011 subsets; both 39.1 and 39.7), V53 (grain exception, 10% to 16% band, one decomposition at a time, ten-year window as an upper indication), V54b (B157's 41.2 is inside the range).

## 3. Rows added (81; continue the series: A420 to A467, B395 to B427)

Status "independently verified (<job>, <checker>, 2026-11-18)" unless stated. Tier B except the five Tier A rows pending gate 6.

| Ids | Job, checker | What |
|---|---|---|
| A420 to A423 | B132, V47 | the 19-choice flip verdicts (short 8, 1, 0, 7; long 3, 1, 1, 2), the 97 to 88 rows, the 74 of 120 zone rows (A423 unverified: V47 did not count them) |
| A424 to A427 | B132, V47 | zone ranges (North Tasmania, Mackay Whitsunday, South West Queensland); the zone 45 fix and the unchanged national draws |
| A428, A429 | B132, V47 | average-year tipping counts; tipping regions at the 95th and 5th percentile |
| A430, A431 (Tier A) | B133, V48 | paired short term (0 of 2,000) and long term (26.1%) |
| A432 to A437 | B133, V48 | holdings-only and shared-only differences; unpaired shares; 2011 on the 2025 weather table (national and regional); the failure range (linear and logarithmic) |
| A438 to A441 | B137, V51 | drought-factor variants (factors and all-output capacities); area-weighted 1 in 100; the crop-only column (A440 unverified); the leave-one-out caveat (A441 unverified: V51's route only) |
| A442 | B137 | the observed livestock-output ratio: unverified (no checker) |
| A443 to A445 | B137, V51 | the meat identity ratios, 2021-23 and 2010-12; red meat and milk ratios; at the model's own intake (A444 unverified: V51's route only) |
| A446 | B137, V51 | the residue bound (194,427; 48,724; 7.9%) |
| A447 to A450 | B137, V51 | eight-layer forward and reverse values, short and long; the two diet layers 5.6 and 2.5 million (A449, Tier A); regions by largest layer (42; 31) |
| A451 to A453 | B138, V52 | reference periods; midpoint ratios (short term verified; A453 long term unverified) |
| A454 to A456 | B138, V52 | projection crossings (2066; 2068; 2034; 2.6 times); higher cases (A456 unverified: V52 did not check them) |
| A457 | B138, V52 | age-sex energy 8.31 MJ, 1.038 |
| A458, A459 | B138, V52 | partition figures on the national yield vector and the state basis |
| A460, A461 | B138 | the arable-share relaxation (A460) and the dairy relaxation (A461): unverified |
| A462 to A464 (A462 Tier A) | B138, V52 | diet window: 39.1 and 39.7; effect 3.55 and 4.16, worth 2.42 million, 29.5% of the rise; 2021-23 the lowest-beef window |
| A465, A466 | B138, V52 | 2011 subsets (32.7 to 34.0; 13.3 to 15.5; 22% to 27%; crops alone under 0.1 million); regions over capacity 20 to 23 (A466 unverified) |
| A467 | B141a | 21.7 million at 1 in 20, 79%: arithmetic, unverified |
| B395 to B399 | B135, V50 | shares robustness: line (a) and line (b) ranges, energy balance alone and footprint and HALF out, narrowing and the commodity-balance dependence, the land scale-up variant |
| B400, B401 | B135, V50 | output over consumption ratios; the binding-land-type multiples (1.30 to 1.88; 1.01 to 1.45; pooled 1.56 to 2.82; 1.21 to 2.18) |
| B402 (Tier A) to B406 | B139, V53 | line (c): 14.7% and its band; median, spread and per-method; variants c2 to c4; the 10% to 16% band; robustness ranges (B406 unverified: V53 did not reproduce the csv) |
| B407 to B411 | B139, V53 | bridge: end points and total; G1 averages; G2; pool 18% and 60%, G3 and G4 starts; protein-held 85.4 |
| B412 to B415 | B139, V53 | Table 8 panels A, B and C; Panel C's L035 row unverified (register holds 70 Mha only) |
| B416 to B418 | B139, V53 | production window: five held years, ten years, years outside 2021-23 |
| B419, B420 | B139 | production comparison (land, field crops, fruit and vegetables, milk: V53); wool and meat (B420 unverified) |
| B421 to B427 | B134, V49 | crop-only companions (41.4, 41.2, 41.0, 40.8, 40.4; 24.7 long term), factor 1.03, failure below 1%, the 93% to 98% share, pasture one at a time, PAL one at a time, the meat-window and calibration Sobol indices |

Unverified rows (14), as the brief asks: A423, A440, A441, A442, A444, A453, A456, A460, A461, A466, A467, B406, B415, B420. The three the brief names are among them: B137's observed livestock-output ratio (A442), B138's arable-share relaxation (A460) and B141a's 21.7 million at 1 in 20 (A467). Each says in its `status` why no checker reached it.

Not added: the crop-only companions for the 2011 and mirror releases (B124 to B128, B104, B105) were not computed by B134, so nothing exists to register; that is a decision row for Murray.

## 4. References

**Tool.** `qa/tools/make_references.py A|B [--style elsevier|springer] [--out PATH]`.
* `springer` (Paper A, decision 140): "Surname, I., Surname, I., & Surname, I. (Year). Title. Journal, Volume(Issue), pages. https://doi.org/...", full journal names, plain text; chapters, books, reports, theses and web items follow the same pattern (editors as "I. Surname & I. Surname (Eds.)", pages "(pp. x-y)", web "Accessed d Month yyyy"). **Basis:** Paper A's own journal guide is not recorded in the repository (`papers/B_methods/JOURNAL_REQUIREMENTS.md` is Paper B's, Land Use Policy), so this is the standard Springer basic author-date form as the brief states it, and the tool's docstring says so.
* `elsevier` stays the default and its entries are unchanged.
* New: rows of `qa/references.csv` whose status starts "uncited" are left out of both lists, and "uncited in A" or "uncited in B" leaves a row out of that paper's list only (a stale claims-csv row or an ambiguous prose match does not bring it back; an uncited row the prose does cite is kept and reported); `NAMED_CITATIONS` takes citations that carry no year in the prose (L004).

**Entries.** Added: ABARE 2010 (L053; Paper A's supplement cites it; it was the one register-fallback entry in A); Schön and Böhringer 2023 (L114) with umlauts and initials (Schön, A.-M.; Böhringer, M., from the title page, the title dash set as a colon); the Borrie 1975 inquiry (L004; a row existed in `qa/references.csv` and `qa/literature_register.csv`, but Paper B's prose cites it with no year, so no list carried it; the named-citation rule takes it). L215 checked: Li, Y., Yang, Y., Yan, H., You, Z. (B127's correction holds; no change). Marked uncited: Beltran-Peña L182 and Summerhayes and Baker 2026a L150 (no paper cites them; L150 was brought into Paper A's list by an ambiguous prose match with 2026b, L148). Kastner L080, Khorsandi 2022 L073 and 2023 L074 are cited by Paper B (supplement S2, section 4, supplement) and not by Paper A, so they are marked "uncited in A" only, which is what B141a reports. L172 (Higgins 2018a, marked uncited by B127) also leaves Paper A's list. Two uncited titles carried an em dash (L178, L185) and read with a colon.

**CHECK counts.**

| List | Entries before | CHECK before | Entries after | CHECK after |
|---|---|---|---|---|
| Paper A (Springer) | 59 | 18 | 54 | 18 |
| Paper B (Elsevier) | 128 | 29 | 128 | 29 |

Paper A: five entries leave (L073, L074, L080, L150, L172), none carried a CHECK; L053 keeps one CHECK (its reason changes from "title; place of publication" to "author form: ABARE in the prose, ABARES on the title page"). Paper B: L182 leaves (no CHECK), L114 loses its "author initials" CHECK, L004 enters with one (the identity of the work rests on footnote 12 of the Jones report), so the count is level. Both lists are deterministic (two runs give identical files). **No em dash in either list** (0 and 0 counted), none in the tool, none in `qa/references.csv`. Fallback (register-title) entries: 0 in both lists (were 1 and 1).

Left alone: the CHECK notes on Wackernagel 1994 and Wackernagel and Rees 1996 that B141b names (places of publication are not in the register; adding them from memory would be unsourced); "Buzby, 2010" in the generated Tables S3a and S5 is a defect row (X142). Rerun `python3 -I qa/tools/make_references.py B` after B143b finishes, because the list reads Paper B's current prose and claims csvs.

## 5. Literature register (12 rows changed, none added)

* Read, with the page, for the works the round-two patches cite for the first time: Gerten 2020 L083 ("read (B119 abstract and PDF pp. 3, 7 and 10)"); Fader 2013 L105 ("read (B119 targeted; PDF pp. 2, 4, 8, 14 and 16)"); Muth 2011 L069 (PDF p. 25; replaces "Buzby 2010" in Paper B 8.5); ABARE 2010 L053 (Tables on pp. 214, 154, 76; the $5,000 level at printed p. 25, note a, from B137). Their `used_by` fields name the new citing sections.
* L004 (Borrie): `used_by` and a note record the Paper B citation; status stays unverified (the report is not on hand). L114: note on the authors' names. L215: checked. L182, L150: `used_by` and note say neither paper cites them; L080, L073, L074: notes say "not cited in Paper A, cited in Paper B".
* I checked the register rows named in B141a and B141b and V54b; I found no other work cited for the first time.

**Referee works not on disk** (copied from `qa/reports/B119_literature_reconcile.md` section 6; for Murray):

1. Fiala 2008, Ecological Economics 67(4): 519-525. https://doi.org/10.1016/j.ecolecon.2008.07.023 . QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Measuring%20sustainability%3A%20Why%20the%20ecological%20footprint%20is%20bad%20economics%20and%20bad%20environmental%20science&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT
2. van den Bergh and Verbruggen 1999, Ecological Economics 29(1): 61-72. https://doi.org/10.1016/s0921-8009(99)00032-4 . QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Spatial%20sustainability%2C%20trade%20and%20indicators%3A%20an%20evaluation%20of%20the%20ecological%20footprint&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT
3. Kitzes et al. 2009, Ecological Economics 68(7): 1991-2007. https://doi.org/10.1016/j.ecolecon.2008.06.022 . QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,A%20research%20agenda%20for%20improving%20national%20Ecological%20Footprint%20accounts&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT
4. Kitzes et al. 2009, Ecological Economics 68(4): 929-930 (reply to Fiala). https://doi.org/10.1016/j.ecolecon.2008.11.001 . QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Interpretation%20and%20application%20of%20the%20Ecological%20Footprint%3A%20A%20reply%20to%20Fiala%20%282008%29&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT
5. Arrow et al. 1995, Ecological Economics 15(2): 91-95. https://doi.org/10.1016/0921-8009(95)00059-3 . QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Economic%20growth%2C%20carrying%20capacity%2C%20and%20the%20environment&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT
6. Pradhan et al. 2014, Environmental Science & Technology 48(16): 9463-9470. https://doi.org/10.1021/es5005939 . QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Food%20self-sufficiency%20across%20scales%3A%20how%20local%20can%20we%20go%3F&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT
7. Kitagawa 1955, JASA 50(272): 1168-1194. https://doi.org/10.1080/01621459.1955.10501299 . QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Components%20of%20a%20difference%20between%20two%20rates&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT (Das Gupta 1993 is on disk, L257.)
8. Seufert, Ramankutty and Foley 2012, Nature 485: 229-232. https://doi.org/10.1038/nature11069 . QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Comparing%20the%20yields%20of%20organic%20and%20conventional%20agriculture&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT
9. Ponisio et al. 2015, Proceedings of the Royal Society B 282: 20141396. https://doi.org/10.1098/rspb.2014.1396 (free copy: https://pmc.ncbi.nlm.nih.gov/articles/PMC4286047/). QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Diversification%20practices%20reduce%20organic%20to%20conventional%20yield%20gap&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT

## 6. Defects (`qa/defects.csv`: 140 rows become 147)

* **X140 closed** (B132, checked V47): `fixed_in` gains the V47 check; the note lists the register rows that take the 19-choice results.
* **X118 closed** (B137, checked V51): V51 reproduces 128 of 128 year cells; the note says A317 is independently verified as built and supersedes the earlier "stays unverified".
* **X141 open**, unchanged (byte-identical): the `make_readme_tables.py` hard-coding stays in it, no second row.
* New: X142 ("Buzby, 2010" printed in the generated Tables S3a and S5; L068 unidentified; open). X143 (the `monte_carlo.mjs` part option B132 suggests, kind "wish (not a defect)"; open). X144 (Table S7 rows, the Table 5 note and S3.8 and Table S5 print values from before X139 was fixed; V54b; open). X145 (199 stale flagged rows in the claims csvs, 113 failed traces; V54b; open). X146 (the 0.62 MJ between 8.0 and 7.376 MJ is not traced; B139 and V53; open). X147 (the improved release's crop-only rule differs 0.1% to 0.4% from its own drought run; B134 and V49; open). X148 (two faults in `harmonised_robustness.py` found by V50; closed in the B135 appendix).

## 7. Register rows touched

Claims register, changed (81): A001, A002, A003, A005, A009, A012, A013, A014, A036, A038, A039, A041, A042, A043, A056, A072, A088, A184, A188, A196, A199, A223, A317, A328, A339, A343, A363, A369, A376, A380, A382, A402, A418, A419, B001, B003, B005, B046, B095, B096, B097, B098, B099, B100, B101, B102, B103, B130, B134, B137, B138, B156, B157, B167, B182, B185, B186, B187, B188, B193, B194, B198, B199, B218, B224, B226, B230, B238, B243, B245, B247, B262, B270, B276, B277, B333, B363, B364, B369, B371, B374. Added: A420 to A467, B395 to B427.
`qa/references.csv`: changed L073, L074, L080, L150, L182 (status), L178, L185 (title dash); added L053, L114 (189 rows become 191). `qa/literature_register.csv`: changed L004, L053, L069, L073, L074, L080, L083, L105, L114, L150, L182, L215. `qa/defects.csv`: changed X118, X140; added X142 to X148.

## 8. Checks (as B122)

* 18 columns on every claims row (the two blank lines between A419 and B386 were in the file and are kept); 12, 8 and 21 columns on the literature, defects and references csv files.
* Row counts: claims 813 plus 81 added is 894; literature 257 (no addition); defects 140 plus 7 is 147; references 189 plus 2 is 191. No duplicate id in any file.
* CRLF line endings on every line of all four csv files (CR count equals LF count).
* Untouched rows byte-identical: claims 735 of 816 lines unchanged (81 changed, matching the list above); literature 246 of 258; defects 139 of 141 (two existing rows carry quotes the csv writer would not add, so the file was written line by line and they are untouched); references 183 of 190.
* On every Tier A claims row only `status`, `verifier_report` and `notes` differ from the file as found (script check, no exception).
* No em dash in any of the four csv files, the two reference lists, the tool or this report. Time words were searched for in everything I added; the few that remain are in quoted source text or the term "first-order index".
* Both reference lists regenerate to identical files on a second run; `python3 -I qa/tools/make_references.py B` with the default reproduces the pre-change entries for every row except L004, L114 and L182.

## 9. For the coordinator

* **Brief's Tier A list against the register:** A418, A382 and A317 are Tier B (no value moves; status updated). If the gate 6 digest should list them, they are in section 2.
* **Per-paper "uncited":** the brief lists Kastner, Khorsandi 2022 and 2023 with the rows to mark uncited where no paper cites them; Paper B cites all three, so they are marked "uncited in A" (a status form the tool reads), not uncited outright.
* **B143b** is editing Paper B: rerun the Paper B list after it finishes.
* The Paper A form is the standard Springer author-date form (no record of the journal's own guide in the repository); if Murray has the Population and Environment instructions, the renderer is one function (`render_csv_springer`).
* Decision 140 and the csv files: the release csv files hold 22,326,388 (frozen); the new rows and notes carry both figures, and A434's note gives the third-decimal moves (0.894 reads 0.893, 0.904 reads 0.905).
* Open items taken from the reports and left as decisions: crop-only companions for the 2011 and mirror releases; the ABS 2015-16 and 2020-21 explanatory notes, ABS 4316.0, ERP at 2007, 2008 and by age and sex, and ABS 3222.0 (B138 and B137 fetch lists for Murray, not repeated here).

## Wrong-value check

Example of what was NOT done: A363 (Tier A) was not changed outright from `0.670; 1.454` to `0.671; 1.455`, nor its statement from "(22,326,388 people)" to "(22,336,514 people)". The row keeps its value and statement and carries, in `notes`, "pending gate 6 (2026-11-18): new value 0.671; 1.455 (22,336,514 people, the regional sum of the 53 regions); was 0.670; 1.454 on the national row 22,326,388; capacity does not move per B138, checked V52 (decision 140 ...)", with `status` "independently verified; new value pending gate 6 (B138, V52)". A script check confirms that no Tier A row changed in `value` or `statement`; a wrong edit of that kind would show as a field difference outside `status`, `verifier_report` and `notes`.
