# Provenance audit of both papers: the consolidated report

Question asked: "Where is the full cross check of all data and facts report?" This document is the answer. It says what was checked, how, what was found, what was changed and what is still open, for Paper A (results) and Paper B (methods). Every number comes from a file named beside it or from a report id; the table in section 10 says what each file holds. No new check was run to write this report.

## 1. What was audited and the standard

Decision 73 (`qa/DECISIONS.md`) set the scope: the facts the two section scopes cite (476 claims, 36 data sources, 179 literature rows), not every register row. The two-route rule: a Tier A claim needs two agreeing routes and a Tier B or C claim needs one; the 209 claims in the second-route job were all Tier B or C, and each was given a second, independently derived route (B89). Every check was blind: the checker states a tolerance before comparing, builds its own value from the source (own code, or the page read from the file), and only then opens the register or the builder's report. Every checker also ran a deliberate wrong-value test to show the check can fail (for example V30a: three planted wrong values, 104 comparisons, 3 mismatches, all three reported FAIL; V33: a planted population of 89,604 gave 4 mismatching rows in each new release).

Two figures need a note. The 476 is decision 73's count. The maps (`qa/provenance_A.md`, `qa/provenance_B.md`) list 343 distinct claims for Paper A and 311 for Paper B as the scopes stand after the rewrites (B92a, B92b), 644 distinct ids in all by a count of the maps' fact rows, so the basis of the 476 is not stated in the inputs. The 118 earlier literature rows are 179 less the 61 rows of the page-level reads (decision 76: 48 read before the page rule plus 13 weak rows).

## 2. Summary table

| Layer | Items in scope | Checked | Held | Corrected | Still open | Reports |
|---|---|---|---|---|---|---|
| Data sources | 36 | 36 (12 each in three groups) | 36: 11 verified, 25 verified with notes | 36 register statuses set, 2 stored paths added (D13, D14), stale hashes and counts fixed; 2 pipeline-side value mismatches found (magnesium, 304 people) and logged, not fixed | 5 defects: X107, X108, X112, X113, X114 | V30a, V30b, V30c, B87 |
| Literature | 179 (61 in the page-level reads plus 118 earlier) | 61 in B85: 27 read at page level, 34 with no file | 17 (14 confirmed as written, 3 with a wording or provenance note) | 10 rows corrected | 34 rows with no file; 40 cited rows with an empty path sorted into lists A (15), B (15), C (10) | B85a, B85b, B85c, B88 |
| Claims | 476 | 209 given a second route; 55 gap-attribution rows given a one-route check | 185 of the 209 (128 plain, 57 with a note); 55 of 55 gap-attribution rows (34 plain, 21 with a note, 0 fail) | 18 rows corrected; 5 gap-attribution rows reworded; 15 rows realigned | 5 unverified, 1 withdrawn, 21 Tier A rows pending gate 4 | V31a to V31e, B89, B93, B95 |
| Logic | 164 points (91 in Paper A, 73 in Paper B) | 164 | 84 supported (42 and 42) | 76 partly and 4 not supported, all answered in the scope rewrites; 3 computations | decisions for Murray and 4 computations with no decision row (section 9) | V32a, V32b, B92a, B92b, B90, B91, B93, B94 |
| Drafts | 21 sections (12 in Paper A, 9 in Paper B) | 21 | every number traced in both checks; no section needs rework | 15 fails fixed (7 and 8); 23 overstated sentences answered (13 and 10) | 3 points for Murray from B96b and the register-side items | D02 to D07, V34a, V34b, B96a, B96b |

## 3. Data sources (36)

Method: blind checkers opened each source, confirmed file, hash and origin, and compared a sample of pipeline values with the source (decision 74). Where the origin was a web host, one request was made per host and file with a plain client string and no retry. Counts are from the summary table of each V30 report.

| Id | What it is | Verdict | Values checked | Note |
|---|---|---|---|---|
| A01 | ABS 4306.0 Apparent Consumption of Foodstuffs 1991-92 (scan) | verified with notes | 14 | No URL; ABS catalogue entry (released 21/06/1994) confirmed |
| A19 | prelim models/resilience 150 years.xls | verified | 16 (56 anchor cells) | Claim A321 quoted the wrong table (section 5) |
| D15 | Lane 2014 PhD thesis, QUT eprint 67485 | verified | 12 plus 16 Table 16 state figures | Sha256 equal to the file at the eprint URL |
| D18 | FAOSTAT crops and livestock bulk file | verified | 5 plus 11,938 extract rows | Origin URL confirmed |
| D23 | half_fbs_countries.csv (FAOSTAT food balance extract) | verified with notes | 6 plus 28,290 rows | Extract drops item codes: "Miscellaneous" holds two series (X114) |
| D26 | fao_world_land_production.csv | verified | 5 plus 2,730 rows | Every QCL row equals D18, every RL row equals D19 |
| D31 | ABS ERP by SA2 (ABS_ANNUAL_ERP_ASGS2021) | verified with notes | 7 (8 SA2s) | API host unreachable, only 2025 checked; file has 2,454 rows, register said 2,473 |
| D43 | release chain (releases, results/releases.json) | verified with notes | 6 plus 46 build hashes and 98 input hashes | Register sha256 stale; 8 of 23 releases frozen, not 3 |
| D46 | data/2025-land | verified | 6 plus 960 cells | Recomputed independently from its two inputs |
| D49 | data/abs-2022-25 | verified with notes | 11 | Queensland oats yield is negative (X112); API unreachable |
| D52 | data/sa2 land use and land types | verified with notes | 8 | CLUM raster and boundaries not stored |
| D56 | data/2025 yield layer | verified with notes | 5 plus 1 year value | Provenance counts 138 and 86 added; livestock matrix matches the locked hash |
| A03 | OWID HALF index table (comparator) | verified with notes | 9 plus row count | Title said 170 countries; file holds 169 and World (X115) |
| A27 | NHMRC Nutrient Reference Values | verified with notes | 11 | Magnesium 365 against 362.5 (X107) |
| D16 | Lane, Dawes and Grace 2015, accepted manuscript | verified with notes | 7 | Register hash not reproducible: QUT restamps the cover (75 bytes); size 432,249 is the check |
| D19 | FAOSTAT Land Use bulk file | verified with notes | 210 extract rows, 6 claim values | File date is 2026-10-01, not 2025-10-01 |
| D24 | half_qcl_world.csv | verified with notes | 1,800 rows, 6 named | Raw bulk hash is recorded and reproduces |
| D27 | fao_au_production_1997_2023.csv | verified with notes | 15 rows, 7 derived | Origin is D18 |
| D33 | ABS ASGS Edition 3 SA2 boundaries | verified with notes | 2,450 points, 6,729 pairs | Sha256 supplied (c4dc5bac...d148); redirect URL recorded |
| D44 | data/2011 default inputs | verified | 2,760 cells, 2 files byte-compared | Identical to the archive files once carriage returns are removed |
| D47 | data/2025-population | verified with notes | 16 rule checks, 2,760 cells | 304 people lost in allocation (X108); release patches long-term fibre |
| D50 | data/abs-history grain series | verified with notes | 47 rows (94 values) | Two of six years checked against the origin |
| D53 | data/sa2 adjacency and centroids | verified with notes | 2,450 points, 6,729 pairs, 5 named | "Centroid" is a representative point |
| D57 | data/2025 pasture and dairy files | verified with notes | 180 A15 values, 60 zone yields, 4 conversions, 3 shares | CLUM, GAEZ and D36 parts not checkable |
| A04 | Henry and Godden 1995 (scan) | verified | 9 printed values plus 2 recipe checks | No origin URL |
| A28 | AUSNUT 2023 food nutrient profiles | verified with notes | 1,976 (152 units by 13) | Workbook holds 3,741 foods, READMEs say 3,742 (X113) |
| D17 | FAOSTAT Food Balances bulk file | verified with notes | 23 named plus the D22 re-cut | File not stored; identity rests on a hash-matched copy outside the repositories |
| D22 | fbs_au_world_2021_23.csv | verified | 6,603 rows | Re-cut from D17 identical |
| D25 | half_landuse.csv | verified | 174 rows | Re-cut from D19 identical |
| D28 | fao_qcl_countries.csv | verified | 7,444 rows | Re-cut from D18 identical |
| D42 | model/model.xls | verified with notes | 12,141 constant cells, 8,100 yield cells, 6 named | Origin commit 04a612e not checkable without git |
| D45 | data/2011-thesis | verified with notes | 2,940 plus 2 capacities | "Noosa Biosphere" column reuses region 36 and is skipped |
| D48 | data/abs-2016-21 (ABS NRM cubes, mapped) | verified with notes | 1,282 | Earlier years rested on unregistered copies; stored in B87 |
| D51 | data/nrm2011 | verified with notes | 426 | CLUM raster not stored; 2 differences explained by method |
| D55 | data/regions (model output) | verified | 16 structural and summary figures | Long-term K=53 map behind claim A124 is not in the folder |
| D58 | data/2025 consumption proxies, red meat mix, organic factors | verified with notes | 25 | Origin is D17 (exact match), not D20 |

Source-value check results (V30a, V30b, V30c summaries): V30a 0 value mismatches, V30b 2 (magnesium, 304 people), V30c 0.

**Mismatches found.**
1. Magnesium (A27, X107): `analysis/nutrition_lp_2025/optimise.py` uses 365 mg; the stated rule (average of 400, 420, 310, 320 from NHMRC page 188) gives 362.5 mg, 0.7% tighter. Code unchanged; decision needed.
2. 304 people (D47, X108): data/2025-population gives Australia 27,608,200, the ERP of D31 for the same 2,450 SA2s gives 27,608,504. Cause not traced; V30c lists Jervis Bay (305 people) outside the 2011 zones, which may account for it, not tested.
3. Stale hashes and counts: D43 sha256 `c9dff86c...` against files `680a4ff0...`, results/releases.json `0fbf7dc3...` against `0ca09173...`, 29 input hashes against 98, 3 frozen releases against 8; D31 2,473 rows against 2,454; D19 and `qa/fao_bulk_hashes.csv` file date 2025-10-01 against 2026-10-01; D16 hash not reproducible from the origin; A03 title 170 against 169.

**Register changes made (B87).** 36 rows moved from unverified to "independently verified (V30x, 2026-11-13)" with the clause for each note; D13 and D14 took stored paths under `carrying-capacity-models/data/abs_cubes/` with the four NRM csv cubes (D48 notes carry their hashes); the Land Use date in `qa/fao_bulk_hashes.csv` was corrected; defects X107 to X115 were added, X115 fixed in B87. FAOSTAT zips were not copied (decision 81).

## 4. Literature (61 rows at page level plus the earlier 118)

The 61 rows of decision 76 were read against the files by B85a (21 rows), B85b (20) and B85c (20). Twenty-seven were read at page level (B85a 7, B85b 12, B85c 8, three of them second-hand rows checked against Henry and Godden 1995: L002, L035, L036); 34 had no file and only a note was appended. Of the 27: 14 confirmed as written, 3 confirmed with a wording or provenance note (L015 refined to the share of cropland available, p. 1 and p. 10; L017 where the habitable-land figures 158, 138, 22 and 49.5 come from, the Our World in Data csv; L073 where the abstract's third method is the second with lower efficiency, p. 1), and 10 corrected.

**The ten corrections.**

| Row | Before | After | Page |
|---|---|---|---|
| L025 Lin et al. 2018 | notes: 1.773 for both editions; 1.79 not found | 2012 edition 1.787 (the 1.79); 1.773 is the 2015 edition | p. 8, Table 1 |
| L042 Fearnside 1985 | row described a 42-page Spanish translation, original not opened; calorie minimum 2,500; "money" | file is the English original, Human Ecology 13(3): 331-369, 39 pages; minimum 2,550 in text and caption (the 2,500 is the translation's); "cash" | pp. 352, 353 |
| L023 Simpson et al. 2000 | Wackernagel et al.'s 7.38 given without qualification | 7.38 is without sea products (8.11 with) | p. 13 |
| L060 Geoscience Australia and ABARE 2010, ch. 12 | 35.2% taken as printed in the chapter | chapter prints 400 L/t (Table 12.12); 35.2% is 400 L at 0.88 kg a litre; 14.8% is that times 42% oil content | p. 331 |
| L124 Shepon et al. 2016 | 17% for eggs and dairy; 0.5 acre a person | 17% is calories only (protein: dairy 14%, eggs 31%); 0.5 acre is the mean American diet as modified by the swap | Fig. 1 and section 2.1 (web copy, no pages) |
| L007 Foran and Poldy 2002 | Tables 1.1 and 2.5 both named as requirement tables | Table 1.1 (p. 31) is population, Table 2.5 (p. 64) holds requirements; the two ranges are not printed, derived as 30.0, 30.5, 31.8 and 79.9, 76.8, 75.6 | pp. 31, 64 |
| L020 Lane 2014 thesis | "about 2012" for the GFN Country Trends citation; section 6.1.2 to p. 115 | no printed date (pp. 115, 403), removed; 6.1.2 runs pp. 111 to 117; 6.4.1 pp. 124 to 125 | pp. 111 to 125 |
| L024 Wackernagel et al. 2002 | name "National Footprint Accounts"; supporting information as a country table | article says "our global accounts"; supporting information is the 1999 results and an annotated spreadsheet (contents not seen); text names US 9.7, UK 5.4, Germany 4.7 global hectares | pp. 9266, 9268 |
| L034 Gutteridge | 7.33 ha as the basis of 180,000 | 7.33 is an intermediate step; 180,000 rests on 12 ha per capita; the workbook holds neither | report p. 32 |
| L055 Lane 2010 Land Use Policy | Douglas Shire and Peters in what_taken | neither is in the text or reference list; the Noosa item is Summers 2004 | p. 5 |

**The file mix-up caught and fixed.** V31b found that the file named for L009 (Bellotti 2017) was Tucker 2020, "We know how many people the earth can support". B89 read the replacement (sha256 f8004487..., "How many people can Australia feed?"): 61 and 36.6 million confirmed, a web article with no page numbers, the 24.4 million domestic population not printed. The related identity error was L042 (above), where the file at the path was the English original and the row described the translation.

**Rows with no file** (B85 not reached: L001, L006, L009, L011, L012, L013, L014, L030, L037, L038, L039, L059, L062, L063, L068, L069, L072, L074, L083, L084, L086, L087, L096, L097, L099, L105, L106, L107, L116, L125, L127, L131, L138, L067; 34 rows). B88 (`acquisitions_2026-11-13.md`) sorted the 40 cited rows with an empty path (decision 82):
* **List A, number-bearing, to fetch (15):** L006, L009, L012, L013, L014, L020, L053, L060, L062, L067, L069, L083, L105, L106, L107. L020, L053 and L060 are held in the archive and need filing, not fetching. L083 and L105 are judgement calls.
* **List B, reference-only (15):** L037, L038, L039, L080, L084, L087, L096, L097, L099, L116, L124, L125, L127, L131, L138.
* **List C, second-hand by design or unobtainable (10):** L001, L002, L011, L030, L035, L036, L059, L063, L068, L072.

B85b also records that L006, L067, L086, L097 and L106 still carry "read" in the register with no file behind them.

## 5. Claims (476 cited; 209 given a second route)

### Verdict tally by job (as each checker's report prints it)

| Job | Subject | Claims | Pass | Pass with a note | Fail | Cannot determine |
|---|---|---|---|---|---|---|
| V31a | method-test claims | 53 | 40 | 11 | 2 | 0 |
| V31b | text-fact claims | 44 | 20 | 13 | 7 | 4 |
| V31c | Paper A and comparison claims | 40 | 21 | 16 | 3 | 0 |
| V31d | scripts and scale-curve claims | 54 | 36 | 12 | 4 | 2 |
| V31e | comparator claims | 18 | 11 | 5 | 2 | 0 |
| Total | | 209 | 128 | 57 | 18 | 6 |

After the merge (B89): 128 plain passes, 57 passes with a note, 18 corrected after a fail, 5 unverified, 1 withdrawn, 209 in all. The two sets are not row-for-row equal because B89 reclassified: B037 stays withdrawn (a V31b fail), B045 is corrected (V31a passed it with a note, V31e failed the label), B052 became a pass with a note (its register note held a stale rebuild figure), and B161 became a pass with a note once L009 was read. No Tier A row was in the 209; A019 was left untouched (section 9).

### Every corrected row (B89)

| Id | Tier | Before | After | Check |
|---|---|---|---|---|
| A064 | B | 193,162 to 2,413; 9 to 356 times (published method) | 170,101 to 2,125; 10 to 349 times (corrected method) | V31c |
| A276 | B | nothing but diet and waste moves the short term by more than 10% | nothing but diet, waste and a 20% rise in livestock output does | V31c |
| A321 | B | South Australia 0.36, Western Australia 0.49 | 0.35 and 0.47 (2025-resilience; 0.36 and 0.49 were the thesis archive rows) | V31d, V31e |
| A323 | B | cuts the 2025 long-term figure to 9.7 million | (0.0023 to 1, other settings short term) cuts the 2025 short-term figure from 41.5 to 9.7 million | V31c |
| A324 | B | unused pasture (1.8 million km2 excess) | pasture fully used (need 3.49 against 3.32 held, short term); the unused land is 1.96 million km2 of non-agricultural land; value 1.8 to 1.96 | V31d |
| A327 | C | livestock output (+20%) missing from the long-term list | added to the long-term list; short-term list marks it as the +20% step | V31b |
| B045 | B | 17.38 and 445.4 Mha in 1991-92 | in 1991 (values unchanged; the 1991-92 means are 16.89 and 447.5) | V31a, V31e |
| B047 | B | a fifth to a third of the food row | about a sixth of the food row (16%) | V31b |
| B061 | C | 70 of 90 commodities | 66 of 90, with the 24 left-out items listed | V31a |
| B079 | B | 21 crops | 22 crop items (value 22; 1,061) | V31a |
| B122 | C | 2,500 kcal in the text, 2,550 in a caption | 2,550 kcal a person a day (English original, L042, pp. 352, 353) | V31b |
| B166 | C | 41 to 49 million; fruit, vegetables and dairy are not exported | 41 to 54 million; exported far less (11% to 26%) than wheat and beef (67% to 78%) | V31b |
| B199 | B | 22 to 25 at 50 years and 19 to 21 at 100 | 23 to 30 at 50 years and 19 to 25 at 100 | V31e |
| B225 | B | 49.7 improved | 58.3 improved (doubled-cropland run) | V31e |
| B232 | C | Gifford doubled cropland | scaled intensive land from 40.5 to 70 Mha, a factor of 1.73, as Henry and Godden report | V31b |
| B239 | B | HALF o, PPH o | HALF partly, PPH partly | V31d |
| B240 | B | FP o | FP partly | V31d |
| B242 | C | three planning-oriented studies (7; 3) | four (7; 4) | V31b |

B037 is not corrected: the arithmetic gives 0.300 (0.299 unrounded), not 0.298, and no equivalence factor is supported, so it stays withdrawn (X044). Beyond the 18, B89 made register edits on 15 passes with a note (for example A315 4.65 to 4.66, B052 rebuild 34.07 to 34.37, A320 sources set to D17 only).

### The FAOSTAT harvest-year finding and its effect

FAOSTAT's food balance file books Australia's winter cereals, canola and winter pulses one year behind its crops file: FBS wheat 2022 = QCL wheat 2021 (36,237 kt) and FBS 2023 = QCL 2022 (41,199 kt) (V31a); canola and the pulses other than field peas also lag, sorghum and meat do not (B93). Effect: the Cassidy test only. On Australia 2021-23 the delivered figure moves from 6.01 to 5.78 people a hectare (-3.8%) and produced from 10.49 to 10.08; on 2022-23 from 6.39 to 6.00 (-6.1%); people fed (147.4 million) do not change; the world does not change (7.87 on 2021-23). The all-cropland reading moves from about 190 to about 183 million (B084), and the harmonised factor from 0.594 to 0.618 (B273): both are Tier A and pending gate 4. B081, B085 and B258 carry the pairing. The Foran and Poldy rows mix the files too but no printed figure moves (V31a); no other method test mixes them (digest). Defects X111 (the question) and X117 (the Cassidy consequence, fixed in B93).

### The gap-attribution rows (B93, decision 88)

B278 to B332, 55 rows, each recomputed from the inputs where plain arithmetic allowed: 34 pass, 21 pass with a note, 0 fail. The 21 notes: B278 to B288, B293 and B294 (share confirmed only to the precision of the csv's two-decimal columns); B320 (the two-decimal columns cannot settle "less than 8%"); B301 to B304 and B322 (residual within the rounding of the published whole number: the shares +731%, -24%, -3%, +234%, -779% and -239% are replaced by "within rounding"); B295 and B306 (right value, the README table double-rounds -12.48 to -13 and 32.8546 to 32.86). Foran and Poldy residuals (0.372 and 0.043 Mt) are outside rounding, so V32b's proposal to call them within rounding does not hold. B95 applied the wording, changed the table generator to print "within rounding" and the unrounded cells (X127), and set the 55 statuses to "self-checked (B93, 2026-11-13)".

### The register layout fault

B318 to B332 had every field after `unit` shifted by one column (`unit` held the README locator, `output_locator` the unit, `depends_on` the csv locator, `notes` the related ids). Found by B93 (X126), realigned in B95 with contents unchanged.

## 6. Logic and consistency

Method: one Opus checker per paper (V32a for Paper A, V32b for Paper B) tested whether each point's evidence supports it, with no contradiction within or between the papers; verdicts S supported, P partly, N not supported.

| Paper | Points | Supported / partly / not | Other counts |
|---|---|---|---|
| A (12 sections) | 91 | 42 / 48 / 1 | 10 cross-paper disagreements listed (X1 to X10) |
| B (9 sections) | 73 | 42 / 28 / 3 | 18 contradictions with the paper or the decisions; 8 cross-paper disagreements counted, 6 distinct |

### Paper A: the ten problems and what was done

| # | Problem (V32a) | What was done | Kind |
|---|---|---|---|
| 1 | North East Victoria's 2011 population copied from Goulburn Broken | Traced, corrected in two new releases, rerun, blind-checked (section 7) | computation (B90, V33) |
| 2 | Regional share of national capacity has two values (44% and 23% against 63%, 33% to 38%) | Yield basis named at every regional sum; state basis is the conservative bound; A095 (63%) still unverified | scope rewrite (B92a); A095 for a job |
| 3 | Narrative credits production, the decomposition credits diet (consumption +4.18 and red-meat mix +1.81 of +8.2) | Question 1 and takeaway reworded in the scope; OUTLINE.md is outside the job | scope rewrite (B92a); OUTLINE.md for a job |
| 4 | Clean and robust flips not tested against method tier | Tier named as untested; with the correction two clean flips remain (Mackay Whitsunday, North Tasmania); the tier test not run | scope rewrite; the test for Murray |
| 5 | "Long-term change lies inside the uncertainty range" does not test change | Worded as smaller than the spread across 2025 input choices; claim rows A366 and A367 added for the meat window and the 50/50 resilience weight; paired Monte Carlo not run | scope rewrite, B95; the computation for Murray |
| 6 | Releases mixed across sections | Scenarios and stores rerun on 2025-fixed; store releases frozen; release named at every figure (section 7) | computation (B91) and scope rewrite |
| 7 | Two opposite ratio conventions | People over capacity (above 1 is over) for both papers; A149, A343, A344 restated in B95; A196 pending gate 4; A005, A163, A167, A171 not restated | scope rewrite; rows for Murray |
| 8 | A106 quotes published figures as the corrected finding | Statement reads 33.3, 25.7 and 21.0 with basis; L013's row prints 25.6 and was not edited | scope rewrite and register (B95) |
| 9 | Section 8 tipping counts without the section 3 tests | Counts reported only with the tests; A200 statement and A197 corrected (81; 85; 91); flip tests on the 1-in-10 count not run | scope rewrite, B95; the computation for Murray |
| 10 | Literature rows asked to say more than they do (L153, PMSEIC 22 plus 40, Mayberry quotation, L099, L072) | L153 dropped from section 4; "yield potential"; 22 plus 40 attributed to Lawrence, Richards and Lyons; L099 and L072 have no file | scope rewrite (B92a) |

### Paper B: the ten problems and what was done

| # | Problem (V32b) | What was done | Kind |
|---|---|---|---|
| 1 | Jones committee figures rest on an unread report | Quoted "as summarised in" the source read; no "reproduces"; the report is Murray's to fetch (decision 89); the draft omits the figure | scope rewrite (B92b); Murray |
| 2 | Footprint low end 103 million quoted as current data | Reworded "146 to 343 million on current yields (103 at 1990 world yields)", "about three to eight times" (section 7) | B94, B92b |
| 3 | Failure view is the author's model, so agreement is by construction | Described as the model read through Fearnside's frame; B157's containment sentence deleted; "the model's range" out of B156 (pending gate 4) | scope rewrite, B95 |
| 4 | "Factor of 4 by definition alone" mixes tiers | Question Q8 put to Murray (D3); the draft follows the recommended reading | scope rewrite; Murray |
| 5 | Span "9 to 100 million" has two soft ends | Both declared at first use; question Q9 put to Murray (D4) | scope rewrite; Murray |
| 6 | Monte Carlo range read as the model's uncertainty | "The spread across the settings the author judges defensible (1.26)"; 81% from one judged choice | scope rewrite |
| 7 | "Diet and weather matter most" is not what the factors show | Ordered as `design_choices.csv` orders them; row B333 added in B95 | scope rewrite, B95 |
| 8 | Harmonised comparison claims more than it shows | Footprint keeps its spread; B276 quoted as 10 to 18%; B277's as-run low is 12 (pending gate 4) | scope rewrite |
| 9 | Waste wording follows superseded decision 44 | Decision 72 wording; L230, L231, L242 cited | scope rewrite |
| 10 | Energy-balance "reproduction" and gap-attribution shares overstate | Arithmetic reproduces 109 and 96 from printed totals, totals not rebuilt; shares replaced by "within rounding"; 55 rows checked (section 5) | computation (B93), B95 |

### Cross-paper disagreements and their resolutions

Resolved in one table written in the "whole paper" part of both scopes (B92a; B92b X-1 to X-13):

| Item | Resolution |
|---|---|
| Waste (A X6; B 1) | Decision 72 wording: 6% setting halves the model's retail-and-consumer share; national goal is whole-chain halving by 2030 (L230); 7.3 Mt 2016-17 (L231); 7.6 Mt is the 2021 Feasibility Study (L242) |
| PMSEIC and Lawrence (B 2) | 22 plus 40 is Lawrence, Richards and Lyons, in Paper A section 8 only (decision 46); PMSEIC's 60 million is unsourced |
| Monte Carlo (X3; B 4) | "13 sampled, 12 vary in the 2025 corrected and published releases" |
| Red-meat 0.528 (X4) | unit "share of meat" in both papers |
| Judgement-end rows (X5) | both papers quote the V31d wording |
| Thesis long-term figure (X1) | 9.43 published and 15.35 corrected on 2011 data; 15.6 is 2025 |
| "9 to 14 million" (X2) | named "published method" wherever it appears |
| Little meat against none (X7) | corrected release only (118.0 against 112.4); improved release peaks at no meat |
| "5% meat and eggs" (X8) | 76.8 million (A258, corrected) and 103.3 million (B179, improved), each with its release |
| Where the margin fails (X9) | above balance at 1 in 10, below at 1 in 20; failure probability 5.8 to 6.1% a year, about 1 in 16 to 17 (B130) |
| 15.5 million (X10) | trade recovery in Paper A (41.5 less the regional sum 26.0); SA2 sum in Paper B (B176) |
| Cause of the scatter (B 3) | "by definition and by method" (decision 35) |
| "Described and tested in Paper B" (B 5) | Paper B section 6 point 9 states the test with B116 |
| 2011 to 2025 material (B 6) | Paper A alone; the section 7 draft's 2011 sentences flagged out |

V32a's ratio convention is also in the table (people over capacity). B92a left V32b item 3 to the coordinator and B92b resolved it.

## 7. The three findings that changed a result

### North East Victoria (B90, V33, ERRATA errors 8 and 9)

* **What.** Zone 22 carried 204,651 people at 30 June 2011, the same to the person as Goulburn Broken (zone 19), with infrastructure of 149 km2 derived from it. The copy is in the earliest land-use workbook, every model workbook, thesis Table 25 (p. 382) and `baseline/baseline_2011.csv`; the rebuild inherited it. Found by V32a.
* **Source and correction.** ABS ERP at 30 June 2011 by SA2 (D31) allocated to the zone as the 2025 population is: **98,604**; second route, ABS 3218.0 cube `32180ds0002_2001-11.xls`: 98,642, within 38 people. Applied as a method module (population 98,604, infrastructure 72 km2, non-agricultural 3,034 km2) in two new releases, `2011-fixed-2` and `2011-improved-2`; the five published releases keep the copy.
* **Check.** V33 rebuilt it blind: 14 items pass (population, every cell of both new results files, the shock and flip files); route 2 could not be checked (the cube is not stored). Status moves: corrected method North East Vic 194% to 93% of capacity (over to under), published method 205% to 99%, improved 186% to 90%; Victoria 104% to 102%.

| Measure (corrected method, 2011, 53 regions) | Before | After |
|---|---|---|
| Regions over capacity, short term | 23 | 22 |
| Short-term flips 2011 to 2025 | 9 (8 over to under, 1 under to over) | 8 (7, 1) |
| Clean and robust flips | 3 (Mackay Whitsunday, North Tasmania, North East Vic) | 2 (Mackay Whitsunday, North Tasmania) |
| Net fall against clean flips, short term | 7 against 3 | 6 against 2 |
| Share of 2011 people in over-capacity regions, average year | 82% | 81% |
| Over at 1 in 10, under in an average year (2011) | 1 (Corangamite) | 2 (adds North East Vic) |
| Improved method, 2011 short term over capacity | 22 | 21 |
| Long-term counts (36 over) and all capacities | unchanged | unchanged |

Seven Tier A rows moved (A029, A033, A034, A036, A164, A165, A199) and three Tier B rows (A043, A197, A308); all are marked pending gate 4 or changed under the Tier rule (B95). ERRATA error 9: Fitzroy (zone 33) and Wet Tropics (zone 39) share one 2011 population, 230,982 and 169 km2 of infrastructure; ABS gives 235,629 and 246,885; no status changes on any 2011 release with either; logged, not corrected (X124).

### The footprint low end (B94, decision 85)

The footprint's 103 million is at 1990 world yields; on 2021-23 yields it is 146 (B268: 146.2). Statements B046, B156 and B247 were reworded with values unchanged: before "103 to 343 million ... about two to eight times"; after "146 to 343 million on current yields (103 million at 1990 world yields) ... about three to eight times". Arithmetic: 343 / 41.5 = 8.3, 146 / 41.5 = 3.5, 103 / 41.5 = 2.5. Three lines of `papers/B_methods/SECTION7_DRAFT.md` carry the same change (V32b counted four places; B94 found three). V34b then found that the energy and people-per-hectare methods read as low as 134, so the draft writes "134 to 343 million on current yields (the footprint 146 to 343 ...)"; "three to eight times" holds (134 / 41.5 = 3.2).

### Scenarios on the corrected release (B91, decision 86)

The named scenarios were computed on `2025-improved` while the paper reports `2025-fixed` (V32a problem 6). Reference on the corrected release: 41.5 million short term, 15.6 long term, 16 and 32 regions over capacity (improved: 53.6 and 18.5, 15 and 36).

| Scenario | Before (improved) | After (2025-fixed) |
|---|---|---|
| Field crops -24%, long term | -5.34%, 36 regions | -0.65%, 34 regions |
| Field crops -24% short term, and -12% short term | -0.26%; -0.11% | -0.20%; -0.09% |
| A223 pair: field-crop shock against the 1-in-10 drought | -0.3% against -26% | -0.2% against -26%, one release |
| Waste at the 6% target, short and long | +8.67% and -4.14% | +16.40% and -8.15% |
| No avoidable waste, short term | +17.29% | +33.21% |
| One-year grain store, long term | +48.27%, 27.4 million, 27 regions | +48.45%, 23.2 million, 25 regions |
| Two-year grain store, long term | +64.21%, 30.4 million | +64.47%, 25.7 million |
| One-year and two-year store as years of drought | about 16; about 10 (9.7) | about 16 (16.1); about 10 (9.8) |
| CSIRO fuel 340 litres, long term | -18.75%, 37 regions | -1.83%, 37 regions |

Unchanged: drought-proofing +59.7%, livestock output, diet and the other measures already on 2025-fixed. The stores and drought-proofing are on one release and remain the largest long-term measures (+60%, +64%, +48%); the next largest is waste at the national target (-8.15%). **The fuel method effect:** same fuel settings on both releases (210 litres, biofuel share 1), so the 18.75% to 1.83% change is a method effect of the improved release; it was not decomposed and nothing is to be written about the 19% without it (X125). Recycling is not the same measure on the two releases (improved: share of the stage uptake pattern; corrected: the thesis recycling setting), so those rows are labelled, not compared (digest D5). `2025-store-1` and `2025-store-2` were frozen and locked (26 input hashes each). Eight Tier A rows are pending gate 4 (A205, A206, A219, A220, A223, A264, A265, A266); the Tier B and C rows A202 to A227 were changed or relabelled in B95 (B95 section 2).

## 8. The first drafts

**Drafted (decision 91; jobs D02 to D07).** Both papers, written from the scopes as rewritten, taking the scope's recommended option on every open question and flagging it, with a Tier A value awaiting gate 4 cited at its pending value with a flag. Paper A: `papers/A_results/draft/A_s01-04.md`, `A_s05-08.md`, `A_s09-12.md` with a `_claims.csv` for each, assembled as `paper_A_draft1.md`. Paper B: `papers/B_methods/draft/B_s01-03.md`, `B_s04-05.md`, `B_s06-09.md` with a `_claims.csv` for each, assembled as `paper_B_draft1.md`.

**How checked.** V34a (Paper A, 12 sections) and V34b (Paper B, 9 sections): each number traced to a claims register value, a pending gate 4 value or a committed csv cell; each cited page opened in the file on disk; each sentence tested against what its row supports; header rules (release named, ratio convention, yield basis, "53 regions (52 NRM regions and the Northern Territory)", no em dashes, British spelling, decision 33 tone, word budget within 15%); then the claims csvs. A planted wrong value was caught in both.

**What the checks found.** Every traced number matched. V34a: 7 fails, 13 sentences stronger than their evidence, no section needing rework. V34b: 8 fails, 10 stronger sentences, sections 2 and 6 ready for Murray, none needing rework.

| Check | Fails |
|---|---|
| V34a | F1 corrections counted as two (three modules); F2 long-term table (Table 6 in the first draft) missing recycling; F3 wheat correlation worded "across Australia" against decision 51; F4 method effects on the published base named as corrected; F5 table number clash; F6 Botterill misattributed; F7 four sections over the word budget (5, 8, 9, 11) |
| V34b | F1 Department of Agriculture 2014 sentence unsupported; F2 Douglas Shire cited through Lane 2010; F3 "146 to 343" contradicts Table 3 (low is 134); F4 Simpson "dairy share" is all milk; F5 claims csv ids and flags; F6 works with no file cited plainly; F7 licence sentence; F8 section 5 over budget (2,841 words against about 2,300) |

**What was fixed (B96a, B96b).** All fails and all overstated sentences were applied. Paper A: tables renumbered 1 to 11, subsections in reading order, one citation style, the 156-litre fuel difference explained (the measure sets both terms, the named scenario the long term only), word counts brought within limits (section 5 1,058 to 1,026, section 8 921 to 896, section 9 1,064 to 950, section 11 1,509 to 1,468). Paper B: Table 3 fidelity cells reworded, "as reported" and "not seen; cited from its abstract" labels added, section 5 cut from 2,627 to 2,365 prose words, headings 4.7 to 4.10 reordered to the outline labels. Per the spend log both papers were reassembled.

**Left for Murray and the register job.**
1. The label "(not seen; cited from its abstract)" is the brief's wording; for several works the register records a full-text read of an open copy not on disk (Khorsandi 2022 and 2023, Kastner, Goldfinger, Röös, Ridoutt 2020, Wiedmann and Lenzen, Shepon, Erb), so fetching the files (decision 82) would let the labels go (B96b).
2. Section 8.5 says the thesis model borrowed a carcase-to-retail factor for beef from USDA Handbook 697; ERRATA row 2 says the shipped model had 1.0 and that 0.705 was in earlier workbooks (B96b).
3. Section 7.1 says "the four planning-oriented studies" and names five (V34b; B242 counts Noosa and Douglas Shire as one).
4. The span: the draft keeps "about 9 to 100 million" and names Henry and Godden's 109 as above it; flagged `[open: span]` (B96b, V34b S1).
5. Register edits: B156 and B247 statements to the 134 form; B215 (0.09 and 0.0 against `diet_land.csv` 0.06, 0.13, 0.19); B060 against B318 (3,203 against 3,364 Mha); L087, L117, L182 fields; year fixes for the DCCEEW page ("n.d.") and L234 ("ABARES undated"); the fibre-need unit in Table 5 (B96a, B96b, V34b).
6. The assembled `paper_A_draft1.md` and `paper_B_draft1.md` were outside both checks; the B96a and B96b reports say they were not edited, the spend log says reassembled, and the difference was not tested.

## 9. Still open

Owner is Murray (a decision) or a job (a builder or a blind check). Ids are decision, defect, claim or literature ids.

1. **Gate 4 digest D1 (ERRATA error 9 and the Fitzroy copy).** Correct Fitzroy and Wet Tropics in the same new releases with a blind check (digest recommends); which zone carries the copy is not settled (ABS: Fitzroy 235,629, Wet Tropics 246,885; shared value 230,982). Murray; X124. B90 had recommended record only.
2. **D2, the national 2011 population row.** Keep 22,326,388 and say the regions sum to 22.22 million (22,220,341) (recommended), or reset it. Murray; moves A002 (22.3 to 22.2), A005 (1.49 to 1.50), A328 (+23.7% to +24.2%) if reset.
3. **D3, Paper B Q8.** "15.6 to 55.3 million, a factor of 3.5, and 62.9 with the Australian settings" (recommended). Murray.
4. **D4, Paper B Q9.** "About 90 million (around 100 in the report's words)" with ratios kept on 100 (recommended); changing to 90 moves three Tier A ratios. Murray.
5. **D5 and the recycling scenario.** Drop it from Paper A section 11 (recommended): the two releases' recycling settings are not the same measure. Murray; rows A211 to A214, A227.
6. **Gate 4 approval of digest statements A to E.** 21 Tier A rows pending (A029, A033, A034, A036, A164, A165, A199, A196, A205, A206, A219, A220, A223, A264, A265, A266, B084, B273, B156, B277, B083). Murray replies "approved" or names a number.
7. **B156 and B247 wording.** The registered statements read "146 to 343 million on current yields"; the draft reads 134 to 343 with the footprint 146 to 343 (V34b F3). Murray (decision 85), then the register job.
8. **A144 denominator.** 94% of people in long-term over-capacity regions: 93.7% over the regions' sum (22,220,341), 93.3% over the national row; holds or moves with D2 (V33 finding 2). Murray with D2.
9. **Jones report.** Murray fetches the 1994 committee report (decision 89, list A L006); until read, B196, B197, B138, B245 stay unverified and the figure is quoted as summarised (X120).
10. **Unverified rows cited in the drafts:** A309 (Mackay Whitsunday on 2011-improved; `method_status.csv` not rerun), A317 (herd-cycle range; build_years.py fails at 2016-17, X118), A129 and A132 (section 12.2), A231, A232, A243 and A244 (Table 11), A095 to A097 (Table 3 cells), A215 (Table 7 and the fuel sentence), A367 (the 50/50 resilience weight). A job to check each.
11. **Works labelled "not seen".** The works named in section 8 point 1 above and the 34 rows with no file; Murray's fetch list A (15 rows) settles most (decision 82).
12. **The CSIRO fuel method effect (X125).** Decompose the 18.75% against 1.83% before anything is written about it. A job; rows A218, A226.
13. **movers.csv land ratio column (X116).** `land_only_ratio` is published-method values in a corrected-method table (Goulburn Broken 1.21 against 1.03). Rebuild on the corrected tier or label it. Murray decides; a job.
14. **The 304 people (X108).** Trace in `land_2011_method.py`; Jervis Bay (305) untested. A job.
15. **Paper B 7.1 count.** "Four planning-oriented studies" names five. Murray or the drafter.
16. **The Handbook 697 sentence.** Section 8.5 against ERRATA row 2. Murray.
17. **Magnesium (X107).** Keep 365 and say so, or use 362.5. Murray.
18. **Oats yields (X112).** How oats yields are taken where levied production understates the crop. Murray.
19. **Scripts needing the release switch to 2011-fixed-2** (`method_status.csv`, `long_term_regions.csv`, `regions_in_depth.py`, `make_readme_tables.py`) and freezing the two new releases (B90 decision 1); A308's output cell and the long-term table's 2011 cells (94%, 33%, labelled `2011-fixed`, V34a) depend on it. A job.
20. **Computations with no decision row** (V32a, B92a): the tier test of the flips, flip tests on the 1-in-10 count, the paired Monte Carlo of the 2011 to 2025 difference, a population-input check in the flip classification. Murray.
21. **Claim rows left:** A019 (cite L012 for 40,450,144; the thesis prints 40,439,187, V31e); A106 (L013 prints 25.6, A106 25.7); A005, A163, A167, A171 not restated to people over capacity; A113 (77 million not reproducible, X119); B163 (NFF figure untraced, X121). Murray or a job.
22. **Register housekeeping:** the sentence "so sha256 is unknown" remains in D17, D18, D22, D23, D25, D26 and D28; sources rows for the ABS 3218.0 cube, D31 `used_by` and D44 notes (B90 section 9) not written; D50 cubes not stored; X113 (AUSNUT 3,741 against 3,742), X114 (D23 duplicate labels); L050 and L062 rows skipped in B95. A job.
23. **Outline and file edits outside the scope jobs:** OUTLINE.md question 1, takeaway and "10 to 15 million"; `analysis/comparison_2025/movers.md` Hawkesbury line; DISCUSSION_MEASURES.md D5 was applied in B95. A job.

## 10. Where everything is recorded

All paths are under `qa/` unless stated.

| File | What it holds |
|---|---|
| `DECISIONS.md` | Decisions 73 to 91 (scope, the audit jobs, pacing, the three result changes, the drafts) |
| `reports/V30a_sources.md`, `V30b_sources.md`, `V30c_sources.md` | Blind checks of 12 data sources each: identity, origin, values, verdict, mismatches, rerun commands |
| `reports/B85a_page_reads.md`, `B85b_page_reads.md`, `B85c_page_reads.md` | Page-level reads of 61 literature rows (27 read, 34 no file) and the ten corrections |
| `reports/B86_provenance_map_tool.md` | The map generator, its parsing rules, first tallies and broken links |
| `reports/B87_register_tidy.md` | Source register changes after V30, stored ABS cubes, defects X107 to X115 |
| `reports/acquisitions_2026-11-13.md` | B88: 40 cited works with no file sorted into lists A, B, C with QUT links |
| `reports/V31a_claims.md` to `V31e_claims.md` | Second-route checks of 209 claims, per claim: route, my value, verdict; FAOSTAT year finding |
| `reports/B89_merge_V31.md` | The merge into the claims register: tally, 18 corrected rows, unverified rows, defects X116 to X122 |
| `reports/V32a_logic_A.md`, `V32b_logic_B.md` | Logic checks: section tables, the ten problems per paper, cross-paper disagreements |
| `reports/B90_ne_vic_population.md` | North East Victoria trace, correction, files changed, dependent analyses, claim rows that move |
| `reports/V33_ne_vic_check.md` | Blind second route on B90: 14 items pass, route 2 not checkable |
| `reports/B91_scenarios_corrected.md` | Scenarios and stores on 2025-fixed, store releases frozen, rows that change |
| `reports/B92a_scope_rewrite.md`, `B92b_scope_rewrite.md` | The two section scopes rewritten to the V32 fixes, cross-paper resolutions, items left pending |
| `reports/B93_gap_attribution_and_cassidy.md` | One-route check of B278 to B332, lag per item, Cassidy with harvests matched |
| `reports/B94_footprint_wording.md` | Footprint low-end rewording of B046, B156, B247 and three draft lines |
| `reports/B95_apply_audit_changes.md` | Register changes applied (21 Tier A rows pending gate 4), rows added (A366, A367, B333), defects X123 to X127 |
| `reports/digest_2026-11-13.md` | Gate 4 digest: statements 1 to 8 and decisions D1 to D5 |
| `reports/V34a_draft_check_A.md`, `V34b_draft_check_B.md` | Blind checks of the first drafts |
| `reports/B96a_fix_draft_A.md`, `B96b_fix_draft_B.md` | The fixes applied to the drafts and what was left |
| `reports/PROVENANCE_AUDIT_2026-11-13.md` | This report |
| `provenance_A.md`, `provenance_B.md` | Generated maps: fact, claim, output cell, script, data row, original source, with each link's status. Paper A: 91 points, 343 distinct claims (96 A, 225 B, 22 C), 23 sources verified, 0 unverified, 16 literature rows with no file; Paper B: 73 points (72 parsed), 311 distinct claims (59, 227, 25), 27 sources verified, 0 unverified, 33 literature rows with no file. Regenerate with `tools/make_provenance.py` |
| `sources_register.csv`, `literature_register.csv`, `claims_register.csv` | The three registers (the claims register at 700 data rows after B95) |
| `defects.csv` | Defect log; X107 to X127 are this audit's |
| `fao_bulk_hashes.csv` | Hashes and dates of the three FAOSTAT bulk files |
| `spend.csv` | Job log with tokens by model (section 11) |
| `briefs/` | The builder and checker briefs, including `B97_audit_report.md` |
| `../ERRATA.md` | Errors 8 (North East Victoria) and 9 (Fitzroy and Wet Tropics) |
| `../papers/A_results/SECTION_SCOPE.md`, `../papers/B_methods/SECTION_SCOPE.md` | The rewritten scopes |
| `../papers/A_results/draft/`, `../papers/B_methods/draft/` | The first drafts and their claims csvs |

## 11. Cost

The 35 rows of `qa/spend.csv` dated 2026-11-13, summed. The tokens column holds one logged total per job (input and output together; `tokens_in` is empty).

| Model | Rows | Logged tokens | Rows with no count |
|---|---|---|---|
| Opus | 26 | 5,983,170 | 4 (V30a, V31d, V32a, B96b) |
| Sonnet | 9 | 1,549,237 | 0 |
| Total | 35 | 7,532,407 | 4 |

Sonnet rows: B85a 157,613; B85b 179,010; B85c 172,827; B86 129,130; B87 188,168; B88 112,417; B89 226,600; B94 80,242; B95 303,230. The notional cost column is empty in every row.

Basis note (HANDOFF.md): "Cost basis from 2026-11-10: about 1% of the weekly allowance per 150,000 Opus-weighted logged tokens; targeted Sonnet reads about 10,000 tokens a paper, full Opus reads 20,000 to 45,000." At that rate the 5,983,170 Opus tokens alone come to about 40% of the weekly allowance (5,983,170 / 150,000 = 39.9). That is a floor: the weight of the Sonnet tokens is not given in the inputs and four Opus rows carry no count.

## Coordinator's notes on two open items above (2026-11-14)

* The reassembled drafts (`paper_A_draft1.md`, `paper_B_draft1.md`) were regenerated by `qa/tools/assemble_draft.py` after B96a and B96b, so they carry the fixed section files; the builders did not edit them because the tool does. V34a and V34b checked the section files, which are the same text.
* The 476 cited claims is the count of distinct claim ids in the two scopes on 2026-11-13 before the scope rewrites (the sizing script behind decision 73); the provenance maps count ids after B92a and B92b added and removed citations.
