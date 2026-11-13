# B87: register tidy after the source checks V30a, V30b, V30c (decisions 80, 81)

Brief: `qa/briefs/B87_register_tidy_after_V30.md`. Files written: `qa/sources_register.csv`, `qa/defects.csv`, `qa/fao_bulk_hashes.csv`, six files under `/home/user/carrying-capacity-models/data/abs_cubes/` (new folder), and this report. The claims and literature registers were not touched. No git, no subagents, no network.

## 1. Sources register: rows changed

The file still parses (86 data rows plus the header, 12 columns each, CRLF line ends as before). 36 rows moved from "unverified" to an independently verified status, and 2 more rows (D13, D14) took a stored path. The other 48 rows are byte-identical to before. The statuses read "independently verified (V30x, 2026-11-13)" or "independently verified with notes (V30x, 2026-11-13): <clause>". Each change was checked against the report named before it was written.

| Id | Fields changed | Before | After (short) |
|---|---|---|---|
| A01 | status | unverified | verified with notes (V30a): no URL; ABS catalogue entry (released 21/06/1994) confirmed |
| A19 | status, notes | "contents not re-checked here" | verified (V30a); notes say sheet years reproduced in tables.csv (56 cells) |
| D15 | status | unverified | verified (V30a) |
| D18 | status, origin | "expected" URL | verified (V30a); URL confirmed as the one that served the hashed file |
| D23 | status, origin, notes | "D17 assumed" | verified with notes (V30a); origin names D17, its csv hash and date, "all 28,290 rows"; notes add the duplicate-label warning (Miscellaneous, Eggs, Milk) |
| D26 | status | unverified | verified (V30a) |
| D31 | status, what_taken | 2,473-row table | verified with notes (V30a; API unreachable, 8 SA2 values checked); 2,454-row table |
| D43 | status, sha256, notes | listing hash c9dff86c...; results/releases.json 0fbf7dc3...; 29 input hashes; 3 frozen | verified with notes (V30a); listing hash 680a4ff0...e980 (recomputed on disk, equal); results/releases.json 0ca09173...3de9; 98 input hashes; 8 frozen named, 15 current |
| D46 | status, what_taken | "then population replaced" | verified (V30a); what_taken now says non-agricultural recomputed as the remainder, reserve share recomputed, infrastructure and population kept at 2011 |
| D49 | status | unverified | verified with notes (V30a): production sold equals the ABS release; API unreachable; Queensland oats negative |
| D52 | status | unverified | verified with notes (V30a): raster and boundaries not stored |
| D56 | status, notes | provenance shares without the 138 and 86 cells; livestock matrix "not checked" | verified with notes (V30a); counts added; livestock matrix matches the hash locked in 2025-fixed, 2025-mirror, 2025-improved |
| A03 | status, title | "170 countries and World" | verified with notes (V30b): origin unknown, an Our World in Data grapher export; "169 countries and World" |
| A27 | status, title, origin, notes | title "taken from BLOCKED_SOURCES.md"; origin unknown | verified with notes (V30b); title adds version 1.2 (September 2017) and ISBN 1864962437; origin "NHMRC (publisher)"; notes carry the magnesium 365 against 362.5 |
| D16 | status, notes | (none) | verified with notes (V30b); notes say the hash is of one download, a fresh one differs in 75 bytes of cover stamp and /ID, size 432,249 bytes is the reproducible check |
| D19 | status, origin, dated_or_accessed, notes | "expected" URL; "file dated Oct 2025"; "sha256 is unknown" | verified with notes (V30b); URL confirmed; file dated 2026-10-01 (server 2026-10-02); stale sentence removed |
| D24 | status, notes | "sha256 is unknown" | verified with notes (V30b); the hash is in qa/fao_bulk_hashes.csv and reproduces |
| D27 | status, origin, notes | origin "not stated"; "NO extract script exists"; "sha256 is unknown" | verified with notes (V30b); origin "cut from D18 by extract_fao_au_production.py"; only the 2026-11-07 script statement kept |
| D33 | status, origin, dated_or_accessed, sha256, notes | sha256 unknown; old URL | verified with notes (V30b); sha256 c4dc5bac...d148 (zip, 50,678,443 bytes); redirect-target URL; confirmed 2026-11-13 |
| D44 | status, notes | (none) | verified (V30b); notes add the 26 columns (id, 24 fields, name) |
| D47 | status, notes | (none) | verified with notes (V30b); notes carry the 304 people, the 5,150 excluded people, the fibre patch and CRLF |
| D50 | status, notes | "cubes are not stored" | verified with notes (V30b); notes name the two cubes (71210do004_201011.xls 1ab4505f...8f07; 7121do001_201516.xls faa084ae...7660), still not stored, and the ACT note |
| D53 | status, what_taken, notes | "centroid lon/lat" | verified with notes (V30b); "representative (interior) point ... not the geometric centroid" |
| D57 | status, what_taken, notes | (none) | verified with notes (V30b); milk_tonnes_2025 from D36; notes on the AUS column of A15 and the blank read as 0.0 |
| A04 | status | unverified | verified (V30c) |
| A28 | status, origin | origin unknown | verified with notes (V30c); origin the FSANZ page named in the archive README, marked as not re-fetched |
| D17 | status | unverified | verified with notes (V30c): checked on a hash-matched copy outside the repositories; file not stored |
| D22 | status, notes | "No check of the extract ... was found" | verified (V30c); notes say the re-cut of D17 is identical, 6,603 rows |
| D25 | status, notes | (none) | verified (V30c); re-cut note added |
| D28 | status, notes | (none) | verified (V30c); re-cut note added |
| D42 | status | unverified | verified with notes (V30c): commit 04a612e not checkable without git |
| D45 | status, origin, notes | origin names the scripts only | verified with notes (V30c); origin names the sheets read; notes add the Noosa Biosphere column (reuses region 36, skipped) |
| D48 | status, notes | "raw cubes are not stored, except 2020-21 which is D13" | verified with notes (V30c); notes give the four stored csv names and sha256 |
| D51 | status, notes | (none) | verified with notes (V30c): CLUM raster not stored |
| D55 | status, notes | (none) | verified (V30c); notes say the long-term K=53 map behind claim A124's 69.4% is not in the folder |
| D58 | status, origin, notes | origin names D20 | verified with notes (V30c); origin names D17 (exact match) and D42 / A21; notes add D35 and D21 not stored |
| D13 | local_path, notes | empty; "Raw file is not stored" | `carrying-capacity-models/data/abs_cubes/AGCDCNRM202021.xlsx`; notes say stored. Hash unchanged and equal to the stored copy |
| D14 | local_path, notes | empty; "Raw file is not stored" | `carrying-capacity-models/data/abs_cubes/AGCDCASGS202021.xlsx`; notes say stored. Hash unchanged and equal to the stored copy |

D48's own `local_path` and `sha256` were not changed: they define a listing hash over the folder `data/abs-2016-21`, and adding the csv files there would break it. The csv paths and hashes are in its notes.

## 2. `qa/fao_bulk_hashes.csv`

Land Use row, `fao_file_date`: 2025-10-01 to 2026-10-01 (zip entries, V30a and V30b). Hashes, sizes and the other two rows unchanged.

## 3. Files stored (`/home/user/carrying-capacity-models/data/abs_cubes/`, original names)

| File | Bytes | sha256 | Register row |
|---|---|---|---|
| 2016-17_NRM.csv | 1,384,391 | 49e127dcade25a1d6cca1795ca77aaa52d3579fa1ef7c0395cd7fcde36f4d3fa | D48 notes |
| 2017-18_NRM.csv | 1,407,506 | dc5e4ba85e407b670f2654929283752a875a8b1f50b3352c212b7b4d34f147f5 | D48 notes |
| 2018-19_NRM.csv | 1,417,293 | 1bc6ee4ec976e17c923c8f7692d2a86688dc74a4f4fab4edd55604dcc2e02773 | D48 notes |
| 2019-20_NRM.csv | 1,104,582 | 3e62902f327847fb3d41fdff509e7bccdcc575e649b7507d63dbe4e28a0c3a4e | D48 notes |
| AGCDCNRM202021.xlsx | 479,046 | 04408ebe58ed3b513c71840a877764c2a83fdb449d38e59be9d559e8470b083d | D13 (local_path) |
| AGCDCASGS202021.xlsx | 4,060,250 | 0fdbd3e398b598a24c8bc315e5bd7cae36e8ea4fb6f6cea5a7b745e0950bedf5 | D14 (local_path) |

The four csv hashes equal the prefixes in V30c; the two xlsx hashes equal the D13 and D14 registered values. The FAOSTAT zips were not copied (decision 81).

## 4. Defects added (`qa/defects.csv`, 9 rows, CRLF, the 106 existing rows byte-identical)

| Id | Layer | Kind | Subject | found_by | fixed_in |
|---|---|---|---|---|---|
| X107 | 1 | source value mismatch | magnesium 365 against 362.5 mg (A27, optimise.py) | V30b checker | (empty) |
| X108 | 3 | population lost in allocation | 304 people in 2025 (D47, land_2011_method.py) | V30b checker | (empty) |
| X109 | 4 | citation | claim A321 quotes the thesis table under release 2025-resilience | V30a checker | (empty; V31e) |
| X110 | 4 | label | claim B045 "1991-92" on calendar-1991 land | V30b checker | (empty; V31e) |
| X111 | 2 | possible year offset | FAOSTAT food balance sheets may book harvests a year late | V30c checker | (empty; V31a tests) |
| X112 | 2 | data use | SA oats 0.26 t/ha used as observed; QLD oats negative (D49) | V30a checker | (empty; decision needed) |
| X113 | 8 | count | AUSNUT 3,741 foods against 3,742 in two READMEs | V30c checker | (empty) |
| X114 | 1 | extract design | D23 merges two "Miscellaneous" series | V30a checker | (empty; warning in D23 notes) |
| X115 | 8 | label | A03 title "170 countries" against 169 plus World | V30b checker | B87 |

Only X115 is fixed by this job (the title). The others are recorded, with the register notes carrying the warning where the brief asked.

## 5. Points for the coordinator

* The brief says V30b relied on `AGCDCASGS202021.xlsx` and `AGCDCNRM202021.xlsx`. The reports show V30c relied on those two; V30b's cubes were the two ABS 7121.0 files behind D50 (`71210do004_201011.xls`, `7121do001_201516.xls`). I copied the files the brief names (and decision 81 lists the four NRM csv files). The two D50 cubes are not stored; their names and full hashes are in the D50 notes, and the copies are in the V30b scratch download folder. Storing them is a decision for Murray.
* D47 and defect X108: V30c lists Jervis Bay (901031003, 305 people) among the SA2s outside the 2011 zones, which may be the 304 that V30b could not trace. Recorded as a possibility, not tested.
* Stale sentence "so sha256 is unknown" remains in D17, D18, D22, D23, D25, D26 and D28, although their hashes are recorded in `qa/fao_bulk_hashes.csv`. The reports did not list it for those rows (the brief names D19, D24, D27 only), so I left it. One small follow-up would remove it.
* Not applied because the brief says the claims and literature registers are out of scope: the notes on claims A321 and B045 (V31e), and the "B02" literature rows named in the D15, D16, A04 notes.

## 6. Wrong-value check

The stored copy of D13 hashes to the registered value `04408ebe...b083d`, and the D43 listing hash recomputed on disk equals the new entry. Example of a wrong hash entry, shown only as an example and not written anywhere: D13 sha256 given as `04408ebe58ed3b513c71840a877764c2a83fdb449d38e59be9d559e8470b0830` (last digit changed). The comparison against the stored file reported it as different, so the check can fail. The old D43 entry `c9dff86c...3843` is a real instance of the same fault, found by V30a and corrected above.
