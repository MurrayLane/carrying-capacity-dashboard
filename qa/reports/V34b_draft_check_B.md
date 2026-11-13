# V34b: blind check of the first draft of Paper B (methods)

Checker: V34b (decision 91). Brief: `qa/briefs/V34b_draft_check_B.md`, with `qa/briefs/_checker_rules_results_wave.md`.
Files under test: `papers/B_methods/draft/B_s01-03.md`, `B_s04-05.md`, `B_s06-09.md` and their three claims csvs. The file `paper_B_draft1.md` in the same folder was not part of the brief and was not checked.
Order of work: each section was checked against the registers, the csv cells and the papers on disk first. The drafters' claims csvs and drafter notes were opened only after that.
Nothing in the repository was edited. Register rows touched: none.

## 1. Tolerance

* **A number passes** when it equals a claims register value (or a pending gate 4 value in that row's notes) or a committed csv cell, at the precision printed (one unit of the last printed digit). Capacities read from `results/<release>.csv` must round to the printed digit.
* **A citation passes** when the work is in `qa/literature_register.csv` and, where a page is given, the page in the file on disk carries the figure or statement. Pages were opened in the PDFs under `/home/user/carrying-capacity-models/` (scanned pages rendered as images and read).
* **A sentence passes** when it claims no more than its register row, its csv cell or the page supports, and does not contradict a table in the same section.
* Counts and names must match exactly.

## 2. Wrong-value example (the check can fail)

The draft prints the published method's long-term figure on 2025 data as 14.1 million. My script read `results/2025-mirror.csv` (zone 1, preset long, capacity 14,146,847) and compared it with the printed value at one decimal:

* 14.1 against 14.147: PASS.
* 14.2 (a deliberate wrong value) against 14.147: FAIL.

A register search for "14.2" finds only B261, where 14.2 is a wool rate in kg/ha. This shows the search must also check the unit and meaning, which this check did for every hit.

## 3. Results by section

Sentence counts are approximate (abbreviations such as "et al." were not split out). "Numbers checked" counts each distinct figure and page number traced to a register row, a csv cell or a page.

### Section 1. Introduction (845 words of prose against about 800; within 15%)

| Sentences checked | Numbers checked | Fails | Wording issues |
|---|---|---|---|
| about 45, plus Table 1 (7 rows) | 44 (9.4, 14.1, 15.6, 100, 27, 63, 90, 61, 36.6, 60, 40, 10.6, 10 to 480, 82, 60, 109, 96, 40, 9 to 40, 23, the Table 1 cells; pages 280, 30, 1, 15, 97, 98, 100, 21, 341 to 343, 123) | 0 | 3 |

All numbers pass. 9.4, 14.1 and 15.6 match `results/2011-thesis.csv` and `results/2025-mirror.csv` and `results/2025-fixed.csv` (B160, B089, B091). Thesis p. 280 (Table 16) prints 9,431,487, "over 40 million" and "about 23 million". SoFSR p. 30 prints the 27, 63 and "around 100" and the word "misleading". PMSEIC p. 1 (60 million) and p. 15 (some 40 million) are as quoted. Henry and Godden p. 97 gives the 10 to 480 million range (the number is held in the L036 `what_taken` cell, not in a claims row). Page 98 (Table 1: 82 and 60) and page 100 (Table 5: 109 and 96) are as quoted. Chisholm p. 21 is as quoted. Every Table 1 cell matches `harmonisation.csv` or `published_values.csv`.

Wording issues:
1. Table 1, row "Lane, Dawes and Grace 2014, 2015; Lane 2017": it attributes the 40, 9 to 40 and 23 million to L012 to L014, which have no file. The prose cites the thesis instead (p. 280). Suggested route cell: "the author's own (thesis method); read in Lane 2014, p. 280".
2. The Jones committee figure (scope point 1) is left out. The drafter named this conflict (V31b, X120, decision 89). It is a reasoned omission, not a fail, and Murray needs to know about it.
3. Two sentences are stronger than their evidence (section 5, items S1 and S2).

### Section 2. The concept, its refinements and its critics (891 words against about 1,000)

| Sentences checked | Numbers checked | Fails | Wording issues |
|---|---|---|---|
| about 40 | 15 pages (Sayre 124, 126, 131; Hardin 601, 603; Gilland 2; Seidl and Tisdell 405; Price 9 to 10, 17; Cohen 343; Rockström 472; SoFSR 30) | 0 | 0 |

Every quotation was found on the page given: Hardin p. 601 (the "conservative approach" quotation) and p. 603; Seidl and Tisdell p. 405; Sayre p. 131 ("theoretically elegant but empirically vacuous"); Price p. 17 ("seriously flawed", "self-validating belief"); Cohen p. 343; Rockström p. 472. Price p. 9 supports the Tasmanian sheep example and the farmers' stocking decisions. Herrington is given in words only, as scope gap 3 requires. The section complies with decision 43, uses "planetary limits" for Biermann and Kim, and quotes Rees 1992 without a page (the file has no text layer). The tone fits decision 33: the critics' words are quoted, not the author's.

### Section 3. How the review was done (433 words against about 450)

| Sentences checked | Numbers checked | Fails | Wording issues |
|---|---|---|---|
| about 25 | 6 (2011 twice; Grant and Booth p. 94; Greenhalgh p. 2; Sukhera pp. 414 to 415; Snyder p. 337; Haddaway p. 1583) | 1 (F6) | 1 |

The pages pass. Grant and Booth Table 1 is on p. 94. Greenhalgh's point box is on p. 2. Sukhera covers boundaries on p. 414 and inclusion and exclusion on p. 415. Snyder covers the transparency of inclusion criteria on p. 337. Haddaway covers transparent reporting on p. 1583.

Wording issue: point 3 gives no counts by route because no selection record exists (scope gap 1, named by the drafter). The section cannot be complete without those counts.

### Section 4. A catalogue of methods (2,056 words against about 1,800; +14%, just within 15%)

| Sentences checked | Numbers checked | Fails | Wording issues |
|---|---|---|---|
| about 110 | 12 (ten diets, six regimes, three classes, three population paths, 70 Mha p. 98, 60 million p. 1, 40 million p. 15, HALF p. 89, 2,700 kcal p. 4, 2,550 kcal p. 352) | 2 (F1, F2) | 4 |

The pages pass: Henry and Godden p. 98 (Nix's 70 Mha "intensive"), Alexander p. 89 ("HALF is accordingly not predictive"), Cassidy p. 4 (2,700 calories), Fearnside 1985 p. 352 (2,550 calories). The family descriptions match B029, B049, B071, B087, B122, B155 and B166.

Wording issues:
1. The heading numbers do not match the outline labels: B4.7 Optimisation is heading 4.8, B4.8 Integrated is 4.7, and B4.9 Water-bounded is 4.10. The drafter named this conflict.
2. Table 2 and Figure 1 are placeholders, because no catalogue csv exists (scope gap 4).
3. 4.6, Kastner et al. 2012: "split the change in cropland per person ... into the effects of population, yield and diet". The register (L080) says the cropland needed was split. A population effect on cropland per person reads oddly. Suggested: "split the change in cropland needed by world region into the effects of population, yield and diet".
4. Works with no file cited plainly: Blomqvist, Wiedmann and Lenzen, Gerten, Fader, Ridoutt 2020 and Röös. See F6.

### Section 5. Testing the methods on common Australian data (2,841 words of prose against about 2,300; +24%, outside 15%)

| Sentences checked | Numbers checked | Fails | Wording issues |
|---|---|---|---|
| about 120, plus Tables 3, 4 and 5 | about 190 (every prose figure and every cell of Tables 3 to 5 checked against B012 to B085, B090 to B158, B256 to B332, `cross_method.csv`, `harmonised_comparison.csv`, `model_entry.csv`, `simpson_food.csv`, `second_build_values.csv`, `cassidy_matched.csv`; pages H&G 99, 100; Simpson 14; Wackernagel 1994 p. 285; Alexander SI-6; Cassidy 3, 4; Foran and Poldy 64; Fearnside 1990 p. 195; Wackernagel and Rees 1996 p. 78) | 3 (F3, F4, F8) | 4 |

The numbers pass, including the pending gate 4 values: 183 and 0.618 (B084, B273), 22 crop items (B083) and 12 to 343 as run (B277). Table 4 matches `model_entry.csv` cell for cell. Table 5 matches `harmonised_comparison.csv` once the 190 and 0.594 are replaced with the gate 4 183 and 0.618, as the table note says. All pages pass. Henry and Godden p. 99 prints 404, 306, 0.1760, 0.2041 and 70/45.7. Wackernagel 1994 p. 285 prints "34 [kg/ha/yr] of meat". Simpson's Table 1 is on p. 14 with 1.758, 0.095, 0.312 and 0.854. Cassidy's Tables 1 and 2 are on p. 3, and the 41 crops on 947 Mha and the 59% are on p. 4. Fearnside 1990 p. 195 prints "at most 0.24 persons ha-1". Wackernagel and Rees p. 78 has the "twice as productive" adjustment.

Wording issues:
1. 5.4: "the sheep-meat rate the thesis prints". In this paper "the thesis" means Lane 2014, but this rate is Wackernagel's thesis. Suggested: "the rate Wackernagel's thesis prints".
2. 5.4: "build 3 is 22% high" leaves out that the same build is 9% low with the Table A2.4 food energies (README). Suggested: add "(9% low with the alternative energies)", or leave it to Supplementary Table S1.
3. Table 3, people-per-hectare fidelity cell: it describes the agreement between the two builds, not a check against Cassidy (the drafter named this). See the stronger-than-evidence list.
4. Table 3, commodity-balance fidelity cell: "their balance and the 30 and 77 readings reproduced". See the stronger-than-evidence list.

### Section 6. What moves the number (1,945 words against about 1,700; +14%, just within 15%)

| Sentences checked | Numbers checked | Fails | Wording issues |
|---|---|---|---|
| about 95, plus Tables 6, 7 and 8 | about 150 (B003, B050, B051, B069, B106 to B109, B116, B117, B162 to B201, B205 to B217, B232, B243, B250 to B253, A098, A258, A366, A367; `design_choices.csv`, `diet_land.csv`, `variants.csv` zone 1, `ranges_2025-*.csv` zone 1, `results/scale_curve.csv`; pages SoFSR 30, Simpson 14, Lenzen and Murray 238, Alexander 89 and 91, H&G 98 and 99, Peters 2007 p. 148, Spang p. 118, Willett p. 472) | 0 | 3 |

Everything passes. The 54% SA2 sum on the local yield basis matches `results/scale_curve.csv` (2025-fixed, short, SA2, local, 0.539) and A098. Table 8 matches the zone 1 rows of the three ranges files, including the shares of variance. Table 7 matches `diet_land.csv` and `variants.csv`; its Optimised C land cells (0.06, 0.13, 0.19) follow the csv, while register B215 says 0.09 and 0.0, a register inconsistency for the register job. Willett p. 472 prints "cropland use of 0–2%". Spang p. 118 names SDG 12.3. The 1.66 × 4.03 × 1.59 product is described as an identity, as B192 and X-10 require.

Wording issues:
1. The Figure 3 placeholder runs the ladder "from 9.4 to 223.9 million", while the prose says its steps "multiply to the whole" and multiplies only to 100. Suggested: say that the ladder's top step (the energy count of exports, 223.9) lies beyond the published span, and that the 10.6 is the product of the steps from 9.4 to 100.
2. 6.9 cites McKay, Beckman and Conover 1979, Helton and Davis 2003 and Saltelli et al. 2008. All three are "record only" (not opened) in the register. They are standard method citations, but section 3 says record-only rows are a record. Suggested: open one or cite them as the standard sources of the method, with no page.
3. 6.5: "Their work supports diet as a lever on emissions more than on cropland." See the stronger-than-evidence list.

### Section 7. Which method for which purpose (986 words against about 900)

| Sentences checked | Numbers checked | Fails | Wording issues |
|---|---|---|---|
| about 50, plus Tables 9 and 10 | 35 (Table 9 against the `SECTION7_DRAFT.md` matrix, cell by cell; Table 10 factors against `design_choices.csv`; 41.5, 30.8, 18.9, 5.8 to 6.1, 12 to 17, 40 to 41, 30 to 32, 276, 145 to 183, 75, 37, 64.8 to 84.6, 23,600 ha p. 195, 0.8, 2.1, 2, 2.4, 6.2, 0.27, 1.2, 1.33, 1.17, 1.09) | 1 (F3, in 7.6) | 2 |

Table 9 matches the matrix in `SECTION7_DRAFT.md` (28 of 28 cells). Fearnside 1990 p. 195 says KPROG2 "requires so much data that it is impractical for large geographic areas".

Wording issues:
1. 7.1 says "the four planning-oriented studies" and then names five (Peters, Fairlie, Gutteridge, Noosa and Douglas Shire). B242 counts Noosa and Douglas Shire as one. Suggested: "the four planning-oriented studies ... (Noosa and Douglas Shire counted together)", or drop the count.
2. 7.3: "because each reproduces one family of published estimates". See the stronger-than-evidence list.

### Section 8. Limitations and what no method yet does (869 words against about 800)

| Sentences checked | Numbers checked | Fails | Wording issues |
|---|---|---|---|
| about 55 | 16 (Cottrell 130, 135; Hochman 2071; Fearnside 1985 p. 345; Kinnunen 11 to 28% p. 229; 100 km; 0.43 ha, 16% p. 14; 0.312, 0.107, 0.854 p. 14; 94.8 and 135.8 p. 91; 66 of 90; six run points) | 0 (F6 also applies here) | 1 |

The pages pass. Cottrell p. 135 says aggregation "smooths out sudden production losses ... in large countries, such as the United States or Australia". Fearnside 1985 p. 345 lists the criteria. Alexander p. 91 prints New Zealand's 135.8. The red-meat statement in 8.5 rests on `analysis/constants_audit/README.md` ("Red meat is the heaviest group by a factor of ten"), which the scope allows; it has no claims row (scope gap 2).

Wording issue: Erb et al. 2016, USDA Handbook 697, AUSNUT 2007, Buzby 2010, Muth 2011 and Fader et al. 2013 have no file and are cited plainly. See F6.

### Section 9. Conclusions, data and code availability (313 words against about 350)

| Sentences checked | Numbers checked | Fails | Wording issues |
|---|---|---|---|
| 20 | 10 (18.9, 55.3, 62.9, 100, 1.26, 12 to 343 twice, 10%, 10 to 18%, twelve items) | 1 (F7) | 0 |

The figures follow Q8 option (a) and Q9 option (a), as decision 91 asks. `results/releases.json` holds the three releases as frozen, with hashes. Zenodo being on hold matches `qa/CARD.md`.

### Checks across the draft

* **Em dashes:** none in the prose of any section (en dashes: none either).
* **British spelling:** no American forms found ("optimisation", "fertiliser", "carcase" and "programme" are used throughout).
* **Header rules.** The Paper A rules in the brief do not bind Paper B. The cross-paper items that do bind it are all honoured: X-1 waste wording, X-2 PMSEIC, X-3 13 sampled and 12 vary, X-4 "share of meat", X-5 and X-6 diet with release named, X-7 "factor" not ratio, X-8 15.5 named by meaning, X-9, X-10 "published method", X-11 2011 material only as fidelity checks, and X-12 5.8 to 6.1%.
* **Decision 33 tone:** neutral throughout. Other methods are described by what they can and cannot see, and results are reported as reproduced or not reproduced on the access stated.
* **Word budget (prose only, tables and captions excluded):**

| Section | Prose words | Scope budget | Difference | Within 15% |
|---|---|---|---|---|
| 1 | 845 | 800 | +6% | yes |
| 2 | 891 | 1,000 | -11% | yes |
| 3 | 433 | 450 | -4% | yes |
| 4 | 2,056 | 1,800 | +14% | yes (just) |
| 5 | 2,841 | 2,300 | +24% | **no** |
| 6 | 1,945 | 1,700 | +14% | yes (just) |
| 7 | 986 | 900 | +10% | yes |
| 8 | 869 | 800 | +9% | yes |
| 9 | 313 | 350 | -11% | yes |

## 4. Every fail, with its fix

**F1 (section 4.4).** "The statistics they draw on are the national food trade accounts (Department of Agriculture 2014)."
The register does not support this. L137 records that this report has no statement of how many people production feeds, and no 60 million. PMSEIC 2010 cannot draw on a 2014 report: its p. 15 cites DAFF 2009. CSIRO and UQ 2025 cites ABS 2024 on p. 30. Only Ridoutt 2017 cites the 2014 report (L079, L137).
Fix: delete the sentence, or write "National food trade statistics are published by the agriculture department (Department of Agriculture 2014); none of the three counts sets out its own calculation." Source: L137, L079, L136 p. 15, L010 p. 30.

**F2 (section 4.11).** "The planning-oriented studies reviewed in Lane 2010 get one line each here. ... The Noosa and Douglas Shire studies applied carrying capacity to local planning; they are cited through Lane 2010 only."
Lane 2010 does not cover Douglas Shire (B236, V31b note: "Lane 2010 alone lacks Douglas Shire and Peters"). Sections 1 and 3 of the same draft say so.
Fix: "The planning-oriented studies reviewed in the earlier work get one line each here. ... The Noosa study is cited through Lane 2010 and the Douglas Shire study through the thesis (Lane 2014, chapter 6) only." Source: B236; L055; L020.

**F3 (sections 5.10 and 7.6).** 5.10: "The first is the aggregate methods ...: the energy and protein balance, the footprint, HALF and people per hectare. They read 146 to 343 million on current yields". 7.6: "Read as capacities, the aggregate methods give 146 to 343 million on current yields".
Table 3 in the same section gives the energy and protein balance 134 to 211 and people per hectare 145 to 147 (about 183 on all cropland). The group's low on current yields is therefore 134, not 146. The 146 is the footprint's low (build 3 on 2021-23 yields; B046, B268). The number equals the B156 and B247 statements, but the sentence contradicts the table. B156's own note (finding a) records the same problem, and decision 85 approved "146 to 343" as the footprint's low end.
Fix (both places): "They read 134 to 343 million on current yields (the footprint 146 to 343), and 103 million at 1990 world yields: about three to eight times the model." 134/41.5 = 3.2, so "three to eight times" still holds. Source: B019, B046, B083, B068, `cross_method.csv`. The B156 and B247 statements need the same edit, which is for Murray (decision 85) and the register job.

**F4 (section 5.12).** "For Simpson's pasture, a calendar-year reading of consumption and a dairy share each overshoot the residual of 2.3%, by 149% and 175% of it."
B297 (175%) is "all milk on pasture", not a dairy share. B325 shows that a dairy share of about 57% of milk closes the residual (100%). The causes explain 149% and 175% of the residual. They do not overshoot it "by" those amounts.
Fix: "For Simpson's pasture, a calendar-year reading of consumption and putting all milk on pasture each overshoot the residual of 2.3% (149% and 175% of it); a dairy share of about 57% of milk would close it, but the paper prints no share." Source: B297, B298, B325, README gap attribution (c) and (d).

**F5 (claims csvs; brief's last check).**
1. B_s04-05 claims row (5,119) cites B297 for "a dairy share". B297 is all milk on pasture (see F4).
2. B_s06-09 row (6,90) cites "B250 notes" for the 50/50 weight on the resilience table. The row that states it is A367.
3. The flags are inconsistent. The B156 pending statement is flagged [gate 4] at (5,90) but not at (7,42), which quotes the same "146 to 343 ... three to eight times".
4. The prose carries no inline flag. The [gate 4] and [open: Q8/Q9] flags exist only in the csvs, so a reader of the draft cannot see which figures are pending (183, 0.618, 22 crop items, 12 to 343, 100).
5. Numbers in the prose missing from the claims csvs: 4.1 "ten diets", "six farming regimes" and "three classes"; 5.10 "about three to eight times"; 5.12 "within half a unit" and "two to three times its residual"; the Figure 3 placeholder's "223.9" (B195).
Fix: correct the two ids, add the flag at (7,42), add the missing rows, and consider inline flags in the prose until gate 4 closes.

**F6 (section 3, with sections 1, 4, 6 and 8).** "Where a work's reading could not be checked against a file, it was cited as reported or fetched and read before it was cited."
The draft cites several works plainly that have no file. Some were "not reached: no file" in B85: Blomqvist et al. 2013 (L087), Wiedmann and Lenzen 2018 (L131) and Gerten et al. 2020 (L083). Others have no local path and are unverified: Fader et al. 2013 (L105), Ridoutt et al. 2020 (L096), Röös et al. 2017 (L116) and Erb et al. 2016 (L084). The thesis model's sources Buzby 2010 (L068), Muth 2011 (L069), USDA Handbook 697 (L062) and AUSNUT 2007 (L067) also have no file. So does the Table 1 row for Lane, Dawes and Grace 2014, 2015 and Lane 2017 (L012 to L014). Decision 82: number-bearing rows are fetched by Murray, and "the rest stay cited as reported".
Fix: either label these citations "as reported" (or move the US constants to "the thesis model's sources, listed in the archive's errata"), or put the number-bearing ones (Blomqvist's sequestration rate; Gerten's balanced diet) on Murray's QUT fetch list. Alternatively, reword section 3 to what was done: "Works whose reading could not be checked against a file are labelled in the register." Source: decision 82; literature register rows named.

**F7 (section 9.4).** "Code is under the MIT licence; the model workbook, data and results are under CC BY 4.0."
`LICENSE-DATA.md` puts the model workbook (`model/`), the default inputs (`data/`), the 2011 baseline (`baseline/`) and the analysis outputs (`analysis/`) under CC BY 4.0. It does not name `results/`. Source data from the ABS and other agencies "keeps the licence of its publisher".
Fix: "Code is under the MIT licence; the model workbook, default inputs, 2011 baseline and analysis outputs are under CC BY 4.0, and source data keep their publishers' licences (`LICENSE-DATA.md`)." If `results/` is meant to be covered, `LICENSE-DATA.md` needs that line first, which is Murray's decision.

**F8 (section 5, word budget).** The prose is 2,841 words against about 2,300 (+24%; with Tables 3 to 5, 3,692).
Fix: cut about 200 to 500 words. Candidates: the 5.6 harvest-matching paragraph to two sentences, the 5.12 attribution detail (left to Supplementary Table S1), and the 5.11 restatement of Table 5's cells.

## 5. Sentences stronger than their evidence

**S1 (section 1, and the 7.3 heading).** "Published estimates of how many people Australia can feed run from about 9 to 100 million." and "The published span from 9.4 to 100 million is a factor of 10.6."
B005 supports the numbers, but Table 1 in the same section prints Henry and Godden's 109 million (energy), and `harmonisation.csv` also holds their 172 and 206. So the published figures as tabled run above 100.
Suggested: "Most published figures run from about 9 to 100 million; energy counts reach 109 (Henry and Godden 1995)". Alternatively, define the span as figures offered as the number Australia can feed, and say why the energy counts sit outside it. This is for Murray, since B005 and the paper's question rest on 9.4 to 100.

**S2 (section 1).** "Each was offered as an answer to the same question."
B006 (Tier C) says "all called carrying capacity" is the paper's own framing. SoFSR calls its metric misleading for food security. Section 9 says the estimates "answer different questions".
Suggested: "Each was offered as a count of how many people Australia can feed." This is the scope's wording.

**S3 (section 5.11).** "What remains above the model is the pairing of pasture-fed food with crops, which neither method carries."
B247's note says the pairing explanation "is the project's interpretation, not tested by removing the pairing from the model". Section 7.6 hedges this correctly.
Suggested: "What remains above the model is consistent with the pairing of pasture-fed food with crops, which neither method carries; the pairing was not removed from the model to test it."

**S4 (section 5.8).** "It is about 1.5% a year on the improved method and about 2% on the thesis method as built, so the risk depends on the method as much as the capacity does."
The failure probabilities differ by a factor of 3 to 4 (5.8 to 6.1% against 1.4 to 2.2%; B130, B132), while the capacities differ by a factor of about 1.3. No row supports "as much as".
Suggested: "so the failure risk at the 2025 population depends strongly on the method."

**S5 (section 5.12).** "Australia's residual of 0.8% is not explained by the causes tested."
B278 records that the supplement's cropland adjustment (1.129) explains 42% of it. The README attribution line words it the same way as the draft.
Suggested: "Australia's residual of 0.8% is partly explained by the supplement's cropland adjustment (42%) and is not closed by any cause tested."

**S6 (Table 3, people per hectare, fidelity column).** "world and Australia within 5% to 8% between two builds"
This sits under "Fidelity check against its authors", but it is agreement between two builds. Against Cassidy, the calorie shares are within a few points for four of five countries, the United States is not reproduced, and people a hectare are 22 to 42% above the paper (B078).
Suggested cell: "calorie shares within a few points for the world, India, China and Brazil; United States not reproduced; people a hectare 22 to 42% above the paper; two builds agree within 5 to 8%". The csv cell needs the same edit.

**S7 (Table 3, commodity balance, fidelity column).** "their balance and the 30 and 77 readings reproduced"
The authors give no capacity figure (section 4.3), and the 30 and 77 are this project's own derivation from their Table 2.5 (B143, B222).
Suggested: "production within 1.2%; their balance reproduced; the 30 and 77 readings are derived here".

**S8 (section 7.3).** "Each other method was rated partly suited, because each reproduces one family of published estimates and shows what that family counts."
HALF and people per hectare reproduce no Australian published estimate.
Suggested: "because each shows what one family of published estimates counts".

**S9 (section 6.5).** "Their work supports diet as a lever on emissions more than on cropland."
Willett p. 472 supports the cropland half (0 to 2%). The emissions half was not page-checked and has no register row, though the scope's point 5 carries the same line.
Suggested: add the page that carries the emissions finding, or cut the sentence to the cropland result.

**S10 (section 5.4, mild).** "The readings are high because all of Australia's pasture ... counts at world-average productivity, with no pairing of pasture-fed food with crops."
The productivity part is supported by column (e) of Table 5 (B270). The pairing part is the same untested interpretation as S3.
Suggested: "chiefly because".

## 6. Register rows touched

None. Two register inconsistencies were found in passing, for the register job:
* B215 (Optimised C land 0.09 and 0.0) against `diet_land.csv` (0.06, 0.13, 0.19).
* B060 (paper pasture 3,203 Mha) against B318 (the supplement uses 3,364 Mha).

## 7. Overall verdict per section

| Section | Verdict |
|---|---|
| 1. Introduction | needs the listed fixes (S1 for Murray, S2; Table 1 route cell; the Jones row awaits decision 89) |
| 2. The concept, its refinements and its critics | ready for Murray |
| 3. How the review was done | needs the listed fixes (F6; the selection-record counts, scope gap 1) |
| 4. A catalogue of methods | needs the listed fixes (F1, F2; Table 2 and Figure 1 not built; heading numbers) |
| 5. Testing the methods on common Australian data | needs the listed fixes (F3, F4, F8; S3 to S7) |
| 6. What moves the number | ready for Murray (three wording points) |
| 7. Which method for which purpose | needs the listed fixes (F3 in 7.6; S8; the count in 7.1) |
| 8. Limitations and what no method yet does | needs the listed fixes (citation labels under F6 only) |
| 9. Conclusions, data and code availability | needs the listed fixes (F7) |

No section needs rework.

## 8. Rerun and files read

Helper scripts are in the scratchpad (`r.py` prints register rows; `find.py` searches the claims register by value, statement and notes; `csvfind.py` searches every csv under `analysis/`; `pg.sh` finds the PDF page carrying a phrase). For example, from the repository root: `python3 <scratch>/find.py 146 134 145` and `<scratch>/pg.sh "<pdf>" "pattern"`.

Files read: the three drafts and their claims csvs; `papers/B_methods/SECTION_SCOPE.md`; `papers/B_methods/SECTION7_DRAFT.md`; `qa/claims_register.csv`; `qa/literature_register.csv`; `qa/DECISIONS.md` (rows 33, 35, 42, 43, 58, 82, 85, 87, 88, 91); `qa/CARD.md` (Zenodo line); `results/2011-thesis.csv`, `2025-mirror.csv`, `2025-fixed.csv`, `scale_curve.csv`, `ranges_2025-*.csv`, `releases.json`; `analysis/method_tests_2025/` (`cross_method.csv`, `harmonised_comparison.csv`, `model_entry.csv`, `published_values.csv`, `gap_attribution.csv`, README); `analysis/comparators_2025/harmonisation.csv` and `diet_land.csv`; `analysis/nutrition_lp_2025/variants.csv`; `analysis/scale_curve_2025/README.md`; `analysis/constants_audit/README.md`; `LICENSE`, `LICENSE-DATA.md`.

Papers opened at the cited pages: SoFSR 2025, PMSEIC 2010, Lane 2014 thesis, Henry and Godden 1995 (pp. 97 to 100 as images), Chisholm 2000, Cohen 1995, Hardin 1986, Seidl and Tisdell 1999, Sayre 2008, Price 1999, Gilland 2006, Rockström 2009, Grant and Booth 2009, Greenhalgh 2018, Sukhera 2022, Snyder 2019, Haddaway 2020, Bolleter 2018, Simpson 2000, Wackernagel 1994 thesis, Wackernagel and Rees 1996 (p. 78 image), Alexander 2016 and SI, Cassidy 2013, Fearnside 1985 and 1990, Lenzen and Murray 2001, Peters 2007, Peters 2016, Willett 2019, Spang 2019, Cottrell 2019.
