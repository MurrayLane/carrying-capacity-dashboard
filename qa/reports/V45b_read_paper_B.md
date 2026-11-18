# V45b: blind read of the revised Paper B draft

Brief: `qa/briefs/V45b_read_paper_B.md`. Files read: `papers/B_methods/draft/paper_B_draft1.md` (whole, read first), `supplementary.md`, `highlights.md`, `references.md`, the four claims csvs, `qa/claims_register.csv`, `qa/literature_register.csv`, the checker reports V36 to V42, the builder reports B113 to B116, `papers/B_methods/OUTLINE.md` and `JOURNAL_REQUIREMENTS.md`, every csv or report the claims rows name, and the Jones committee PDF (L006, read as text). No git, no subagents, no network. This report is the only repository file written; my scripts are in the session scratch folder (`v45b/trace.py`, `tables.py`, `cover.py`, `mk.py`). The assembled draft body is identical, line for line, to the three section files (checked with diff).

## Tolerance

Exact for every printed number: a number passes only if the file the claims row (or the table caption) names prints it, either as the same string or as a value that rounds to it at the draft's printed digits (for example 41503537 in a csv for "41.5 million", 0.385 for "38.5%"). A value derived by arithmetic from printed values but not itself printed is a fail. Page numbers, years in citations, section, table and build labels are locators, not figures; they are listed in the appendix as "locator" and not counted as fails.

## Wrong-value example

Example only. I fed the trace check the 1-in-10 capacity of section 5.8 misread as 30.3 million in place of 30.8. Against `analysis/method_tests_2025/fearnside_failure_curve.csv` the true value returns line 3 (`2025-fixed,27.6082,41.5,37.03,30.81,...`), and the wrong value returns no match: `true 30.8 -> ('rounded(x1)', 3, ...)`, `WRONG 30.3 -> None`. So the check can fail.

## Counts

* Numbers in the claims rows of the four csvs: 1,444 occurrences. Pass 1,324; locators 116; fail 4.
* Table cells in the main text and supplement checked against the files their captions name: 1,114. The script could not place 17; each was resolved by hand and the results are in the fails list below (7 of them are fails or provenance fails; the rest are explained in table notes and pass).
* Numbers in the prose with no claims row of their own: the coverage script found 304 candidate numbers whose string is in no claims fragment. On hand inspection they are table cells covered by a whole-row claims row (Tables 6, 8, S1, S5, S6, S7) or by a caption row, page and year locators, or arithmetic restatements. None is a figure with no row at all, with one exception: the 3.79% of Table 7 (variant 2's meat-and-egg share) has no row of its own; it is printed in `qa/reports/V40_check_B114.md` (variant 2 table) and in B114.
* How sure the automatic match is: rounding matches can hit an unrelated number in the same file. I checked about 40 rounding matches by hand and found 4 false hits (world delivered 7.9, the SA2 local share 54%, the 26% fall at 1 in 10, the 1,000 bootstrap resamples); each was then found on the right line by hand (appendix). Table and prose numbers that matter to the argument were checked by hand as well (sections 5.3 to 5.14, 6.1 to 6.11, 7, 9, the abstract and the highlights).

Total fails (all kinds, listed below): 4 trace fails in claims rows, 8 trace or provenance fails in tables and notes, 3 checker-wording fails, 1 Tier A pending mismatch, 11 logic fails, 13 consistency fails, 5 citation and reference groups, and 5 journal or style fails.

## Trace fails (number; section; claims row; file; printed where)

| # | Number | Section | Claims row | File named | Printed where | Verdict |
|---|---|---|---|---|---|---|
| T1 | 54% (lower at 1 in 100) | 5.8 | B_s04-05, sentence 42 | `fearnside_failure_curve.csv` | not printed; 1 - 18.92/41.5 = 54.4% derived (the csv prints 0.74 for 1 in 10, so the 26% passes, but nothing prints 0.46 or 54) | fail (derived, not printed) |
| T2 | 6.40 (aggregate secondary, times the improved model) | Table S8 | supplementary, Table S8 row 8 | `cross_method_local.csv` | the csv prints 6.41 (line 14); 6.40 is only in the builder's `B113_harmonised_both_lines.md` line 35 | fail |
| T3 | 2.48 | Table S8 | supplementary, Table S8 row 9 | `cross_method_local.csv` | not in the csv; only in B113 line 35, the builder's secondary row that V39 replaced | fail |
| T4 | 1.92 | Table S8 | supplementary, Table S8 row 9 | `cross_method_local.csv` | as T3 | fail |
| T5 | +21.6% (Simpson feed cropland, build 3) | Table S6 | supplementary, Table S6 row 6 | `fidelity.csv` | `fidelity.csv` line 7 prints 21.6; V42 (line 33 and its comparison table) gives 21.7 (0.1156/0.095 = 1.2168); the prose prints 21.7 | fail (same quantity, two values; Table S6 carries the builder's figure) |
| T6 | 21.7% (feed cropland) | Table 3, footprint fidelity cell | B_s04-05, Table 3 row 3 | `fidelity.csv` ("feed cropland +21.7%") | the csv prints 21.6, not 21.7; the claims row misquotes it; the caption names only `cross_method.csv`, which carries none of 21.7, 11.9 or 8.4 | fail (row misquotes its file; caption omits `fidelity.csv`) |
| T7 | 183 million; factor 0.62 | Table 3 note, Table 5 and its note, S3.4 | B_s04-05, Table 5 note; supplementary S3 33 | `cassidy_matched.csv` | that file prints 5.78 people a hectare and 25.51 Mha, not 183 or 0.62; 183 is in `analysis/method_tests_2025/README.md` line 204 and register B084 notes; 0.618 in register B273 notes and `B93_gap_attribution_and_cassidy.md` | fail on provenance (values right, file wrong) |
| T8 | 41.5 (31.1 to 49.2) | Table 3, corrected model row | B_s04-05, Table 3 row 8 | row: `ranges_2025-fixed_wide.csv` (pass); caption: `cross_method.csv` | `cross_method.csv` line 8 and `cross_method_local.csv` still print 36.3 to 45.8; the Table 3 note explains only the improved range | fail on caption provenance |
| T9 | 31.1, 49.2, 1.58 | Table 8, Monte Carlo row | B_s06-09, Table 8 row 13 | row: `ranges_2025-fixed_wide.csv` (pass); caption: `design_choices.csv` | `design_choices.csv` line 14 prints 36.3, 45.8, 1.26 and "13 uncertain choices"; no note | fail on caption provenance |
| T10 | 275.8 (HALF secondary) | Table S8 | supplementary, Table S8 row 7 | `cross_method_local.csv` | the csv prints 276 and 276.0 (line 7); 275.8 is in `harmonised_comparison.csv` and V39 | fail on provenance (minor) |
| T11 | 1992 (National Population Council) | Table 1 | B_s01-03, Table 1 NPC row | the Jones report | para 2.15 of the report reads "The 1991 National Population Council report estimated 50 million"; Table 1 and `references.md` say 1992 | fail (year differs from the source the row names) |
| T12 | 182.2 and 324.8 | Table S7 | supplementary, Table S7 rows 2 and 9 | `intake_variant.csv`, V42 | the table prints V42's values, as its caption says, but the two claims fragments still read 182.3 and 324.3 and the csv was not regenerated | fail (claims rows out of step with the table) |

Every other number in the claims rows passes; the full trace table, fails first, is the appendix.

## Checker wording: places the draft does not use the checker's amended wording or value

Paper B rows name builder reports B113, B114, B115, B116 (checked by V39 to V42), and B118, B120 and B122. No Paper B row names B110, B111 or B112 as a report (the strings B110 to B112 in the csvs are register ids for the Monte Carlo ranges), so V36 to V38 apply to Paper A. B118, B120, B121 and B122 have no checker report among V36 to V44 (V44, which appeared while this read ran, checks B123, which no Paper B row names), so their wording cannot be confirmed against a checker.

1. **V41, the span by definition.** V41 failed "by definition alone the model spans 18.9 to 55.3 million" as unsupported: under the rule the paper itself adopts in 6.9, a loss factor is a setting, so 55.3 (no avoidable waste) is a setting, and the corrected definition rows reach 15.5 (unit) and 15.6 (time frame). The draft keeps the builder's wording in the abstract (sentence 7), highlight 5, section 6.10 and section 9.2. The drafter notes say decision 118 keeps it and leave the tension to the coordinator; it is still a place the draft does not follow the checker.
2. **V42, Simpson feed cropland.** V42 gives +21.7%; Table S6 (and `fidelity.csv`) print the builder's +21.6% (T5).
3. **V39, the improved multiple and the 1990 row.** V39 asks for 6.41 from the unrounded 343.4 and for secondary rows on 2021-23 yields with 103 only as a qualifier. Table S8 prints 6.40 and a separate row "Footprint at 1990 world yields | 103 | 2.48 | 1.92", the builder's ratios (T2 to T4).

Followed as amended (pass): V39's "spread among method centres" and the 19-reading set; the 134 to 343 secondary range; V40's "consistent with" and the variant 1 sentence (5.14), the 7.6 rewrite and the 8.4 qualifier; V41's 97% first-order sum, about 3% interactions, five of six settings at one end, 18 of 19 vary, six judged settings named, PAL 1.4 to 1.8 as part of 1.2 to 2.2, no "every definition" and no 2011 sentence; V42's 5% threshold made consistent, units in Table S1, the four Cassidy delivered rows, the "paper years" label, the US other-use share, crop-plus-pasture and feed cropland in 5.4, 3,718 kcal, and the 10.9 and 12.9 tops.

Not taken up, noted only: V39's sensitivity of the centre references (51% or -28% with a fixed centre) is not printed beside the 16.0% and 17.2%; V42's New Zealand rerun on printed inputs (101.88, -25.0%) and its consumption-only lower bound are not in the supplement. Variant 3's 172.3 (5.14 and Table 7) traces to `pairing_relaxed.csv` but no checker reached it (V40: cannot determine); the claims csv flags it unverified.

## Tier A rows pending gate 5: the sentences that carry them

Register rows for Paper B that are Tier A with "pending gate 5": B046, B058, B068, B112, B156, B159, B187, B188, B272, B276, B277. The draft carries the pending (checker-passed) value in each of these places:

| Register row | Sentence or cell | Draft value | Pending value | Verdict |
|---|---|---|---|---|
| B156 | Abstract s3; 5.10 s1 to s3; 7.6 s2; 9.1 s4 | about 65 to 211 million, 1.6 to 5 times; 134 to 343 million, about three to eight times; commodity balance 12 to 41 | 65 to 211, 1.6 to 5; 134 to 343, 3.2 to 8.3; 12 to 41 | pass ("three to eight" rounds 3.2 to 8.3) |
| B156, B272 | Highlight 3 | 1.6 to 2.8 times | 1.56 to 2.82 (footprint), 1.83 (HALF) | pass |
| B276 | Abstract s5; 1 (closing paragraph); 5.11 s4; 9.1 s2 to s3; highlight 2 | 4.1% (line a), 38.5% (line b) | 4% (4.1%), 38.5% | pass |
| B276 | Table 6 caption | factor split 9.6% and 41.3% | 9.6%, 41% | pass |
| B276 | Table 5 column (c) | input factors 0.62 to 1.42 overall (Cassidy 0.62 to 0.77) | "input factors 0.59 to 1.42 unchanged" | **mismatch**: the draft carries 0.62 (harvest-matched, gate 4 value of B273), the pending gate 5 value is 0.59; the register row needs the same change or the table a note |
| B277 | Abstract s5; 5.11 s4; 9.1 s3 | spread of method centres narrows by about a third (0.646 to 0.440; 6.22 to 3.70); about a sixth over 19 readings | same | pass |
| B046 | 5.4 test; Table 3 footprint row | 64.8 to 117.0 (together 64.8 to 84.6); 146 to 343 on current yields, 103 at 1990 yields | same | pass |
| B058 | 5.5 fidelity; Table 3 HALF cell; S3.3 | world -2.2%, Australia +0.8%; printed inputs +2.8% and +8.4%; India -7.2%; partly | same | pass |
| B068, B272 | 5.5 test; 5.10; Table 3; Table 5 HALF row; Table S8 | 76.0 primary (1.83, 1.42); 276 or 275.8 secondary (6.65, 5.15) | same | pass |
| B112, B159 | Table 3 corrected row; Table 4 corrected row; 5.10 s4; 6.9 | 41.5 (31.1 to 49.2) | same | pass (caption provenance, T8) |
| B187 | Abstract s7; 6.9; 6.11; 9.2; highlight 5; Table 8 last row | 1.58 (2.22 lowest to highest) | same | pass |
| B188 | 6.11; Table 8 | 1.58 against 2.14, 2.19, 2.41 to 6.36, 2.66, 2.67; above 1.09, 1.17 and 1.33, 1.29 | same, no "every definition" | pass |

## Logic fails, with the sentence and a suggested rewrite

1. **Abstract s7, highlight 5, 6.10 s1, 9.2 s1: "By definition alone the model spans 18.9 to 55.3 million."** Section 6.9 classes a loss factor as a setting, so the 55.3 (avoidable waste to none) is a setting by the paper's own rule, and the definition rows of section 6 go lower than 18.9: the unit (15.5, 6.7) and the time frame (15.6, 6.8). Rewrite, keeping decision 118's figures but saying what they are: "Varying the weather allowance and avoidable waste, the corrected model spans 18.9 to 55.3 million; the unit and the time frame take it as low as 15.5 and 15.6 million." The highlight then needs its own words, for example "Weather and waste move one model from 18.9 to 55.3 million; settings, by 1.58" (77 characters).
2. **6.9 s3: "Definitions are reported one at a time (sections 6.1 to 6.8)".** 6.2 (the Australian settings) and 6.3 (waste) are settings under the rule two sentences earlier. Rewrite: "Definitions (sections 6.1 and 6.4 to 6.8) and two groups of settings (6.2 and 6.3) are reported one at a time."
3. **9.1 s4: "relaxing the pairing of pasture-fed food with crops brings the model to those readings (section 5.14)".** Variant 1 (81.7) passes HALF (76.0) and footprint build 1 (64.8) but reaches 93% of build 3 (84.6) and is far below the footprint's top reading, 117.0. V40 failed the same overreach. Rewrite: "relaxing the pairing alone brings the model to 81.7 million, above HALF and footprint build 1 and 93% of the way to build 3 (section 5.14)."
4. **7.3 s1: "because one model run under each definition spans most of it (section 6.10)".** On the log scale 18.9 to 55.3 is 45% of 9.4 to 100; even 15.5 to 62.9 is 59%, and the span to 100 needs the export count. Rewrite: "because one model run under each definition reaches from 15.5 to 62.9 million, and the proportional count of exports carries it to the published 100 million (section 6.10)."
5. **7.5 s1: "HALF, reproduced closely on 2011 data (section 5.5)".** HALF is graded partly reproduced (8.4% high on the authors' printed inputs; New Zealand not reproduced). Rewrite: "HALF, partly reproduced on 2011 data (within 1% for Australia on the current FAOSTAT revision; section 5.5)".
6. **Abstract s2: "Five published methods and the author's own land-and-diet model ... were applied to one Australian data set (FAOSTAT 2025, data for 2021 to 2023)".** The model runs on its own 2025 data layer (ABS holdings, meat window 2020-21 to 2024-25), "taken as the same vintage" (S3); footprint build 3 also uses 1990 world yields. Rewrite: "... were applied to Australian data for 2021 to 2023 (FAOSTAT 2025 for the published methods; the model's own 2025 layer of the same vintage)".
7. **7.7 s2: "because readers argue most about it".** No figure or source supports this. Rewrite: "The land base stays on the list, although it moved the answer least, because the published estimates differ most visibly on it (Table 1)", or cut the clause.
8. **6.10 s4: "on a ladder of ten steps that multiply to the whole".** `ladder.csv` has ten rungs, and the rungs from 9.4 to 100 give eight steps; the tenth rung (223.9) is beyond the span. Rewrite: "on a ladder of nine rungs from 9.4 to 100 million (eight steps) that multiply to the whole".
9. **7.1 s6: "The model's four ratings agreed".** The model has eight cells in Table 9 (two columns, "read two ways"), and S7 says all differences were on other methods. Rewrite: "The model's eight ratings agreed".
10. **5.8 s4 against 6.6 s4.** 5.8: Jones's 30 to 35 million "agrees with the model's 30.8 million at 1 in 10 in scale"; 6.6: Jones's figure "cannot be placed on the model's curve of failure probability", while `ladder.csv` labels the 1-in-10 rung "Jones: 30 to 35". Rewrite 5.8: "The Jones committee's 30 to 35 million after a safety margin is of the same size as the model's 30.8 million at 1 in 10, though it is not a return period (section 6.6)."
11. **S4 s1: "The diet with no meat or eggs was the highest point on the improved release, at 103.6 million".** Table S2 on the same release has optimised diets at 202.1 and 422.3. Rewrite: "the highest of the guideline diets".

The abstract says nothing the body does not, apart from item 6. The highlights match the body (items 1 for highlight 5).

## Consistency fails

1. **Simpson feed cropland: 21.7% (5.4, Table 3, S3.2, S3.9) against +21.6% (Table S6).** Rewrite Table S6 to "0.116 (+21.7%)" and regenerate `fidelity.csv`.
2. **Cassidy crop count: 22 crop items (5.6 twice, S3.4) against "harvested area of 21 crops, 24.5 Mha" (Table S5, Cassidy as-run row).** Rewrite the cell: "harvested area of 22 crop items, 24.5 Mha".
3. **Cassidy all-cropland reading: 183 (Table 3, Table 5, S3.4) against 190 (Table S5 "the 190 million reading applies the rate to all 31.65 Mha") and "145 to 190 million" (Table S9 reason).** Rewrite Table S5: "the all-cropland reading (about 183 million harvest-matched, 190 on the same-year pairing)"; in Table S9 add "(183 harvest-matched)".
4. **Figure 3 placeholder: "the energy count of exports (223.9 million)" against 184 to 264 million (6.1) and 183.9 and 263.9 (Table 8).** Rewrite: "its top rung, the midpoint of the two energy counts of exports (223.9 million, from 184 and 264)".
5. **Commodity balance grain: 3.06 times the model (Table 5 column d, from 127) against 3.05 (Table S7, from 126.6).** Rewrite Table 5 to 0.29 to 3.05, or note that Table 5 uses whole millions.
6. **Table S8 footprint secondary: improved-model column blank, while `cross_method_local.csv` gives 2.73 to 6.41.** Fill the cell.
7. **Table 3 and Table 4 placement.** Table 4 (5.9) is printed before Table 3 (5.10). The journal wants tables numbered in order of appearance; move Table 3 above 5.9 or renumber.
8. **Supplement table order.** Tables run S1, S5, S6, S7, S8, S2, S3a, S3, S4, S9; the introduction says "Tables S1 to S9" and leaves out S3a. Renumber in order of appearance.
9. **5.5 s5: "Table 3 gives the other countries."** Table 3 gives only the Australia, world and New Zealand HALF grades; the other countries are in Table S6 and Table S1. Rewrite: "Table S6 gives the other countries."
10. **Figure placeholders against the figure list.** `OUTLINE.md` lists four figures (methods map, cross-method readings, design choices, purpose matrix); the draft places Figures 1 to 3, and the purpose matrix is Table 9. Figures 1 and 2 are not cited in the prose (only their placeholders name them). Cite each ("Figure 1 maps ..."; "Figure 2 sets ...") and update the outline's list.
11. **5.12 s4: "9.2 million people on Australia's land".** The land base in 5.1 is 363.5 Mha; the 9.2 million is on Australia's 2011 cropland and pasture, 396.1 Mha (S3.7). Rewrite: "9.2 million people on Australia's 2011 agricultural land (396.1 Mha)".
12. **8.6 s2: "Simpson's 0.312 ha of crop land for plant foods (the rebuild gave 0.107 ha)".** 5.2 grades on the printed inputs, which is build 3 (0.074); 0.107 is build 1. Rewrite: "(the builds gave 0.074 to 0.142 ha)", as S3.2 says.
13. **9.1 s5 leaves out the feed cropland.** "not Simpson's plant-food cropland or crop-plus-pasture total" omits the feed cropland on the thesis rates (21.7% high, not reproduced), which V42 asked to name and which 5.4 names. Add "feed cropland on the thesis rates".

"Not seen" appears nowhere in the prose. **"Reported in" appears in the prose** (fail, brief item 5): main text 3.1 ("cited as reported in a held work"), 8.5 three times ("both as reported in Lane 2014", "as reported in the archive's errata", "as reported in Lane 2014"); supplement S2.2 ("both cited as reported in Henry and Godden 1995"), S2.4 ("Fader et al. 2013, as reported in Clapp 2017"), S2.5 ("Blomqvist et al. 2013, as reported in Giampietro and Saltelli 2014"), S2.9 ("Gerten et al. 2020, as reported in Beltran-Peña, Rosa and D'Odorico 2020"), S8 ("Fader et al. 2013, as reported in Clapp 2017, p. 91"). Elsevier Harvard form for a secondary citation is "(Fader et al., 2013, cited in Clapp, 2017, p. 91)"; use "cited in" throughout, and in 3.1 "a work with no file is cited through a held work that cites it". The literature register says L083 (Gerten) and L105 (Fader) were fetched in B119, so those two may be cited directly.

## Citations and references

Elsevier Harvard, author and date. 126 entries in `references.md`, 24 still marked [CHECK].

* **Cited in the prose or tables, not in `references.md`:** Centre for Population 2026 (section 1); Schön and Böhringer 2023 (S2.6); Geoscience Australia and ABARE 2010 (S8); Taylor 1937 (Table 1; only Taylor 1922 is listed); NHMRC Nutrient Reference Values (6.9, S5, Table S3a); FIAL 2021, Burnside 2022 and ABS 7215.0 (Table S3a).
* **Cited under a name or year that matches no entry:** "Li et al. 2018" (S2.9) against the entry "Yi, L., Yanzhao, Y., ..., 2018"; "The Jones committee (1994)" against "House of Representatives Standing Committee for Long Term Strategies, 1994"; "Borrie 1975" (Table 1) against "National Population Inquiry, 1975"; "ABS 4306.0" (S3.2) against "ABS, 1994"; "National Food Waste Strategy 2017", "National Food Waste Baseline 2019" and "DCCEEW, ... web page" (S8) against the three "Department of Climate Change, Energy, the Environment and Water" entries (2017, 2019, n.d.); "CSIRO and UQ 2025" (4.4, 6.1, Table 8) against "CSIRO and University of Queensland 2025" elsewhere; "Buzby and Wells, Muth et al." (Table S5) against "Buzby 2010; Muth 2011" (8.5).
* **In `references.md`, not cited anywhere:** Bentham et al. 2020, Cohen 2017, Poore and Nemecek 2018, Productivity Commission 2011, Reutter, Lant and Lane 2017, Rosa et al. 2020 (economic water scarcity), Tucker 2020.
* **Form:** narrative citations print three or more authors in full and the year without brackets ("Peters, Wilkins and Fick 2007 built", "Simpson, Petroeschevsky and Lowe 2000 applied", "Graymore, Sipe and Rickson 2010 rank"); Elsevier Harvard wants "Peters et al. (2007)".
* **In `references.md`:** an em dash in the Reutter et al. 2017 title (line 187), "[CHECK: not seen, Murray fetches]" in the Jansen 1999 entry (line 117), and "reported in Clarke" in the Migration Committee entry (line 157).

## Journal checks

| Check | Result | Verdict |
|---|---|---|
| `python3 qa/tools/wordcount.py B` | 1: 716, 2: 576, 3: 323, 4: 1112, 5: 2265, 6: 1302, 7: 699, 8: 539, 9: 406; **TOTAL 7938** | pass (at most 7,950) |
| Abstract words | **249** (counted twice, by whitespace split) | pass (at most 250; one word to spare) |
| Highlights | 5 bullets; characters including spaces 74, 82, 82, 76, **85** | pass (3 to 5; at most 85); highlight 5 sits on the limit and carries logic fail 1 |
| Keywords | 7 | pass (1 to 7); "method comparison", "land use", "food security", "carrying capacity", "ecological footprint", "sensitivity analysis" are phrases, where the guide prefers single words |
| Em dash (U+2014) | `paper_B_draft1.md` 0, `supplementary.md` 0, `highlights.md` 0, `references.md` **1** (line 187, a title) | fail in references |
| Time words | "Planners still need the concept" (2, s1 of the last paragraph); "what no method yet does" (heading 8); "Its deposit on Zenodo is on hold" (9.4); "the earlier 13-setting range", "the earlier analysis", "The earlier factor split" (Table 4 caption, Table 6 caption, S5) refer to earlier states of the work; "today's" (Table S4 item 3, acceptable as a diet name). "Production shocks have become more frequent" (8.1) is tied to Cottrell et al. 2019, acceptable. "since 2011", "since 2016", "since 1990" are dated. | fail (the first five) |
| Decision 33 tone | No sentence judges another author's competence or honesty. Quoted verdicts (Sayre "empirically vacuous", Price "seriously flawed") are on the concept; the CSIRO report calls its own measure misleading; "errors" refers to the author's own thesis. | pass |
| AI declaration | `JOURNAL_REQUIREMENTS.md` item 26 asks for a declaration of generative AI use before the references; the draft has none (7.1 discloses the AI second rater only). B121 drafted one in `papers/DECLARATIONS.md`; it is not in the draft. | fail |
| Internal labels in the paper | "(decision 57)" (S2.1), "second build (V05)" (Table S7), "V42 spot-checked it" and "the figures the blind check reached" (Table S7 caption) | fail (a reader cannot resolve them) |

## Three places a referee who has not seen Paper A or the repository would be lost

1. **What the thesis method's errors were.** Section 1, 5.9 and Table 4 rest on "the thesis method as built, errors kept" (49.4 and 14.1) against "corrected" (41.5 and 15.6), and the 9.4 million low end is "before its errors were corrected", but Paper B never says what was corrected. One sentence after the first sentence of 5.9: "The corrections, listed in the archive's errata (Lane 2014 errata, in the repository named in section 9.4), are [the two or three largest, named], and together they move the short-term figure from 49.4 to 41.5 million and the long-term figure from 14.1 to 15.6 million."
2. **The unit of self-sufficiency in 6.7.** "The states summed to 75% of that, and the SA2s to 37%", "the state yield basis", "the release land" and "The full curve is in the companion results paper" assume Paper A. One sentence at the start of 6.7: "Each unit (the nation, its 7 states and territories, or its 2,450 Statistical Areas Level 2, SA2s, of the Australian Bureau of Statistics) is fed only from its own land, at the yields of its state (state yield basis) or of its own zone (local yield basis), and the sum of the units' capacities is compared with the nation's."
3. **"The earlier factor split" in the Table 6 caption and S3.11, and "the earlier 13-setting range" in Table 4 and S5.** These refer to a measure and an analysis from earlier drafts that the paper does not define. One sentence in place of the caption's last sentence: "A second measure, the share of each method's log ratio to 41.5 that its input factor accounts for (inputs over inputs plus method, five methods weighted equally), gives 9.6% on line (a) and 41.3% on line (b)"; and in the Table 4 caption, "the mirror and improved rows keep a 13-setting range of 1,000 draws, run before six settings were added (section S5)".

## Register rows touched

None. `qa/claims_register.csv` and `qa/literature_register.csv` were read, not edited.

## Rerun

From the scratch folder `v45b/`: `python3 -I trace.py rows.json` (claims rows), `python3 -I tables.py` (table cells), `python3 -I cover.py` (numbers with no row), `python3 -I mk.py` (verdicts); `python3 qa/tools/wordcount.py B` from the repository root.

## Appendix: trace table, every number in the claims rows (fails first)

"How matched": literal means the same string on that line; rounded(xk) means the file value times k rounds to the printed number at its printed digits. "register Bnnn" means the register row the claims row names. Table cells checked against their captions' files are summarised above (1,114 cells; fails T5 to T12).

| Verdict | Number | Section | Claims row | Printed where (file:line, how matched) |
|---|---|---|---|---|
| FAIL | 54 | 5 | B_s04-05, sentence 42 | 54% lower is not printed in fearnside_failure_curve.csv or any named file (1 - 18.92/41.5 = 54.4%, derived) |
| FAIL | 6.40 | S3 | supplementary, Table S8 row 8 | printed only in qa/reports/B113_harmonised_both_lines.md:35 (builder, unamended); cross_method_local.csv:14 prints 6.41 (V39 amends to 6.41) |
| FAIL | 2.48 | S3 | supplementary, Table S8 row 9 | printed only in qa/reports/B113_harmonised_both_lines.md:35 (builder's unamended secondary row); cross_method_local.csv, the file the row names, does  |
| FAIL | 1.92 | S3 | supplementary, Table S8 row 9 | as 2.48: only in B113_harmonised_both_lines.md:35; not in cross_method_local.csv |
| pass | 9 | 1 | B_s01-03, sentence 1 | analysis/comparators_2025/harmonisation.csv:13 (literal) |
| pass | 100 | 1 | B_s01-03, sentence 1 | analysis/comparators_2025/harmonisation.csv:10 (literal) |
| pass | 1 | 1 | B_s01-03, sentence 1 | analysis/comparators_2025/harmonisation.csv:14 (literal) |
| pass | 109 | 1 | B_s01-03, sentence 1 | analysis/comparators_2025/harmonisation.csv:4 (literal) |
| pass | 1995 | 1 | B_s01-03, sentence 1 | analysis/comparators_2025/harmonisation.csv:4 (literal) |
| pass | 100 | 1 | B_s01-03, sentence 1 | analysis/comparators_2025/harmonisation.csv:10 (literal) |
| pass | 9.4 | 1 | B_s01-03, sentence 3 | results/2011-thesis.csv:3 (rounded(x1e-06)) |
| pass | 2011 | 1 | B_s01-03, sentence 3 | results/2011-thesis.csv:2 (literal) |
| pass | 2025 | 1 | B_s01-03, sentence 4 | results/2025-mirror.csv:2 (literal) |
| pass | 14.1 | 1 | B_s01-03, sentence 4 | results/2025-mirror.csv:3 (rounded(x1e-06)) |
| pass | 9 | 1 | B_s01-03, sentence 4 | results/2011-thesis.csv:18 (literal) |
| pass | 14 | 1 | B_s01-03, sentence 4 | results/2011-thesis.csv:28 (literal) |
| pass | 100 | 1 | B_s01-03, sentence 5 | analysis/method_tests_2025/published_values.csv:43 (literal) |
| pass | 27 | 1 | B_s01-03, sentence 5 | analysis/comparators_2025/harmonisation.csv:10 (literal) |
| pass | 63 | 1 | B_s01-03, sentence 5 | analysis/comparators_2025/harmonisation.csv:10 (literal) |
| pass | 2025 | 1 | B_s01-03, sentence 5 | analysis/comparators_2025/harmonisation.csv:8 (literal) |
| pass | 90 | 1 | B_s01-03, sentence 6 | register B162,B006:1 (literal) |
| pass | 30 | 1 | B_s01-03, sentence 7 | qa/literature_register.csv L010 what_taken (p. 30 page locator) |
| pass | 10 | 1 | B_s01-03, sentence 10 | qa/literature_register.csv:3 (literal) |
| pass | 480 | 1 | B_s01-03, sentence 10 | qa/literature_register.csv:4 (literal) |
| pass | 1986 | 1 | B_s01-03, sentence 10 | qa/literature_register.csv:4 (literal) |
| pass | 1994 | 1 | B_s01-03, sentence 11 | register B196,B197:1 (literal) |
| pass | 50 | 1 | B_s01-03, sentence 11 | register B197:1 (literal) |
| pass | 50 | 1 | B_s01-03, sentence 11 | register B197:1 (literal) |
| pass | 30 | 1 | B_s01-03, sentence 11 | register B196,B006:1 (literal) |
| pass | 35 | 1 | B_s01-03, sentence 11 | register B196,B006:1 (literal) |
| pass | 2014 | 1 | B_s01-03, sentence 17 | register B229,B101:1 (literal) |
| pass | 2014 | 1 | B_s01-03, sentence 17 | register B229,B101:1 (literal) |
| pass | 2015 | 1 | B_s01-03, sentence 17 | register B229,B101:1 (literal) |
| pass | 2017 | 1 | B_s01-03, sentence 17 | register B229,B101:1 (literal) |
| pass | 2025 | 1 | B_s01-03, sentence 18 | papers/B_methods/OUTLINE.md:13 (literal) |
| pass | 2010 | 1 | B_s01-03, sentence 20 | register B236:1 (literal) |
| pass | 6 | 1 | B_s01-03, sentence 20 | register B236:1 (literal) |
| pass | 2010 | 1 | B_s01-03, sentence 20 | register B236:1 (literal) |
| pass | 2011 | 1 | B_s01-03, sentence 21 | qa/DECISIONS.md:25 (literal) |
| pass | 82 | 1 | B_s01-03, Table 1, Gifford et al. 1975 | analysis/comparators_2025/harmonisation.csv:3 (literal) |
| pass | 60 | 1 | B_s01-03, Table 1, Gifford et al. 1975 | analysis/comparators_2025/harmonisation.csv:3 (literal) |
| pass | 1970 | 1 | B_s01-03, Table 1, Gifford et al. 1975 | analysis/comparators_2025/harmonisation.csv:3 (literal) |
| pass | 109 | 1 | B_s01-03, Table 1, Henry and Godden 1995 | analysis/comparators_2025/harmonisation.csv:4 (literal) |
| pass | 96 | 1 | B_s01-03, Table 1, Henry and Godden 1995 | analysis/comparators_2025/harmonisation.csv:4 (literal) |
| pass | 1990 | 1 | B_s01-03, Table 1, Henry and Godden 1995 | analysis/comparators_2025/harmonisation.csv:4 (literal) |
| pass | 91 | 1 | B_s01-03, Table 1, Henry and Godden 1995 | analysis/comparators_2025/harmonisation.csv:4 (literal) |
| pass | 30 | 1 | B_s01-03, Table 1, Foran and Poldy 2002 | analysis/comparators_2025/harmonisation.csv:3 (literal) |
| pass | 32 | 1 | B_s01-03, Table 1, Foran and Poldy 2002 | analysis/comparators_2025/harmonisation.csv:8 (literal) |
| pass | 76 | 1 | B_s01-03, Table 1, Foran and Poldy 2002 | analysis/comparators_2025/harmonisation.csv:8 (literal) |
| pass | 80 | 1 | B_s01-03, Table 1, Foran and Poldy 2002 | analysis/comparators_2025/harmonisation.csv:8 (literal) |
| pass | 1997 | 1 | B_s01-03, Table 1, Foran and Poldy 2002 | analysis/comparators_2025/harmonisation.csv:8 (literal) |
| pass | 98 | 1 | B_s01-03, Table 1, Foran and Poldy 2002 | analysis/comparators_2025/harmonisation.csv:8 (literal) |
| pass | 2050 | 1 | B_s01-03, Table 1, Foran and Poldy 2002 | analysis/comparators_2025/harmonisation.csv:8 (literal) |
| pass | 2.5 | 1 | B_s01-03, Table 1, Foran and Poldy 2002 | analysis/comparators_2025/harmonisation.csv:8 (literal) |
| pass | 60 | 1 | B_s01-03, Table 1, PMSEIC 2010 | analysis/method_tests_2025/published_values.csv:44 (literal) |
| pass | 40 | 1 | B_s01-03, Table 1, Lane, Dawes and Grace 2014, 2015; Lane 2017 | analysis/comparators_2025/harmonisation.csv:8 (literal) |
| pass | 9 | 1 | B_s01-03, Table 1, Lane, Dawes and Grace 2014, 2015; Lane 2017 | analysis/comparators_2025/harmonisation.csv:13 (literal) |
| pass | 40 | 1 | B_s01-03, Table 1, Lane, Dawes and Grace 2014, 2015; Lane 2017 | analysis/comparators_2025/harmonisation.csv:8 (literal) |
| pass | 23 | 1 | B_s01-03, Table 1, Lane, Dawes and Grace 2014, 2015; Lane 2017 | analysis/comparators_2025/harmonisation.csv:13 (literal) |
| pass | 2011 | 1 | B_s01-03, Table 1, Lane, Dawes and Grace 2014, 2015; Lane 2017 | analysis/comparators_2025/harmonisation.csv:12 (literal) |
| pass | 12 | 1 | B_s01-03, Table 1, Lane, Dawes and Grace 2014, 2015; Lane 2017 | analysis/comparators_2025/harmonisation.csv:13 (literal) |
| pass | 100 | 1 | B_s01-03, Table 1, Lane, Dawes and Grace 2014, 2015; Lane 2017 | analysis/comparators_2025/harmonisation.csv:10 (literal) |
| pass | 61 | 1 | B_s01-03, Table 1, Bellotti 2017 | analysis/comparators_2025/harmonisation.csv:9 (literal) |
| pass | 36.6 | 1 | B_s01-03, Table 1, Bellotti 2017 | analysis/comparators_2025/harmonisation.csv:9 (literal) |
| pass | 2017 | 1 | B_s01-03, Table 1, Bellotti 2017 | analysis/comparators_2025/harmonisation.csv:9 (literal) |
| pass | 100 | 1 | B_s01-03, Table 1, CSIRO and University of Queensland 2025 | analysis/comparators_2025/harmonisation.csv:10 (literal) |
| pass | 27 | 1 | B_s01-03, Table 1, CSIRO and University of Queensland 2025 | analysis/comparators_2025/harmonisation.csv:10 (literal) |
| pass | 63 | 1 | B_s01-03, Table 1, CSIRO and University of Queensland 2025 | analysis/comparators_2025/harmonisation.csv:10 (literal) |
| pass | 2025 | 1 | B_s01-03, Table 1, CSIRO and University of Queensland 2025 | analysis/comparators_2025/harmonisation.csv:8 (literal) |
| pass | 65 | 1 | B_s01-03, Table 1, Taylor 1922; 1937 | analysis/comparators_2025/harmonisation.csv:2 (literal) |
| pass | 20 | 1 | B_s01-03, Table 1, Taylor 1922; 1937 | analysis/comparators_2025/harmonisation.csv:2 (literal) |
| pass | 1937 | 1 | B_s01-03, Table 1, Taylor 1922; 1937 | Jones report PDF (L006) note 13: "Taylor reduced this estimate to 20 million ... 1937" |
| pass | 1937 | 1 | B_s01-03, Table 1, Taylor 1922; 1937 | Jones report PDF (L006) note 13: "Taylor reduced this estimate to 20 million ... 1937" |
| pass | 50 | 1 | B_s01-03, Table 1, Borrie 1975 | Jones report PDF (L006) para 8.4: "a population of 50-60 million" |
| pass | 60 | 1 | B_s01-03, Table 1, Borrie 1975 | register B163:1 (literal) |
| pass | 50 | 1 | B_s01-03, Table 1, National Population Council 1992 | Jones report PDF (L006) para 2.15: "The 1991 National Population Council report estimated 50 million" (the source says 1991; Table 1 says 1992) |
| pass | 50 | 1 | B_s01-03, Table 1, Jones committee 1994 | register B197,B196:1 (literal) |
| pass | 30 | 1 | B_s01-03, Table 1, Jones committee 1994 | register B197,B196:1 (literal) |
| pass | 35 | 1 | B_s01-03, Table 1, Jones committee 1994 | register B197,B196:1 (literal) |
| pass | 30 | 1 | B_s01-03, Table 1, Jones committee 1994 | register B196:1 (literal) |
| pass | 35 | 1 | B_s01-03, Table 1, Jones committee 1994 | register B196:1 (literal) |
| pass | 50 | 1 | B_s01-03, Table 1, Jones committee 1994 | register B196:1 (literal) |
| pass | 40 | 1 | B_s01-03, Table 1 note | analysis/comparators_2025/rerun.csv:2 (literal) |
| pass | 69 | 2 | B_s01-03, sentence 15 | register B334:1 (literal) |
| pass | 115 | 2 | B_s01-03, sentence 15 | register B335:1 (literal) |
| pass | 7.7 | 2 | B_s01-03, sentence 15 | register B336:1 (literal) |
| pass | 1996 | 2 | B_s01-03, sentence 17 | analysis/comparators_2025/rerun.csv:15 (rounded(x100)) |
| pass | 2016 | 2 | B_s01-03, sentence 19 | qa/DECISIONS.md:66 (literal) |
| pass | 2011 | 3 | B_s01-03, sentence 4 | qa/DECISIONS.md:25 (literal) |
| pass | 2011 | 3 | B_s01-03, sentence 5 | qa/DECISIONS.md:25 (literal) |
| pass | 1975 | 3 | B_s01-03, sentence 9 | register B010:1 (literal) |
| pass | 5 | 3 | B_s01-03, sentence 11 | papers/B_methods/OUTLINE.md:13 (literal) |
| pass | 9 | abstract | B_s01-03, sentence 1 | analysis/method_tests_2025/ladder.csv:2 (literal) |
| pass | 100 | abstract | B_s01-03, sentence 1 | analysis/method_tests_2025/ladder.csv:3 (literal) |
| pass | 2025 | abstract | B_s01-03, sentence 2 | papers/B_methods/OUTLINE.md:13 (literal) |
| pass | 2021 | abstract | B_s01-03, sentence 2 | papers/B_methods/OUTLINE.md:72 (literal) |
| pass | 65 | abstract | B_s01-03, sentence 3 | analysis/method_tests_2025/cross_method_local.csv:3 (rounded(x1)) |
| pass | 211 | abstract | B_s01-03, sentence 3 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 1.6 | abstract | B_s01-03, sentence 3 | analysis/method_tests_2025/cross_method_local.csv:3 (rounded(x1)) |
| pass | 5 | abstract | B_s01-03, sentence 3 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 134 | abstract | B_s01-03, sentence 3 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 343 | abstract | B_s01-03, sentence 3 | analysis/method_tests_2025/cross_method_local.csv:5 (literal) |
| pass | 4.1 | abstract | B_s01-03, sentence 5 | analysis/method_tests_2025/harmonised_comparison_lines.csv:31 (rounded(x100)) |
| pass | 38.5 | abstract | B_s01-03, sentence 5 | analysis/method_tests_2025/harmonised_comparison_lines.csv:80 (rounded(x100)) |
| pass | 81.7 | abstract | B_s01-03, sentence 6 | analysis/pasture_2025/pairing_relaxed.csv:3 (rounded(x1)) |
| pass | 41.5 | abstract | B_s01-03, sentence 6 | analysis/pasture_2025/pairing_relaxed.csv:2 (rounded(x1)) |
| pass | 18.9 | abstract | B_s01-03, sentence 7 | analysis/comparators_2025/rerun.csv:47 (rounded(x1)) |
| pass | 55.3 | abstract | B_s01-03, sentence 7 | analysis/comparators_2025/rerun.csv:50 (rounded(x1)) |
| pass | 1.58 | abstract | B_s01-03, sentence 7 | results/ranges_2025-fixed_wide.csv:2 (literal) |
| pass | 5 | abstract | B_s01-03, sentence 7 | results/ranges_2025-fixed_wide.csv:1 (literal) |
| pass | 95 | abstract | B_s01-03, sentence 7 | results/ranges_2025-fixed_wide.csv:1 (literal) |
| pass | 4.1 | 1 | B_s01-03, sentence 22 | analysis/method_tests_2025/harmonised_comparison_lines.csv:31 (rounded(x100)) |
| pass | 38.5 | 1 | B_s01-03, sentence 22 | analysis/method_tests_2025/harmonised_comparison_lines.csv:80 (rounded(x100)) |
| pass | 2050 | 4 | B_s04-05, sentence 12 | register B140:1 (literal) |
| pass | 60 | 4 | B_s04-05, sentence 17 | qa/literature_register.csv L136 what_taken ("feed 60 million people" p. 1) |
| pass | 1 | 4 | B_s04-05, sentence 17 | literature register cell named in the row |
| pass | 40 | 4 | B_s04-05, sentence 17 | qa/literature_register.csv L136 what_taken ("some 40 million people" p. 15) |
| pass | 1996 | 4 | B_s04-05, sentence 19 | analysis/comparators_2025/rerun.csv:15 (rounded(x100)) |
| pass | 1996 | 4 | B_s04-05, sentence 19 | analysis/comparators_2025/rerun.csv:15 (rounded(x100)) |
| pass | 1993 | 4 | B_s04-05, sentence 21 | register B339:1 (literal) |
| pass | 2,700 | 4 | B_s04-05, sentence 27 | register B087:1 (literal) |
| pass | 2,550 | 4 | B_s04-05, sentence 41 | register B122:1 (literal) |
| pass | 6 | 4 | B_s04-05, sentence 46 | register B236:1 (literal) |
| pass | 31.65 | 5 | B_s04-05, sentence 3 | analysis/method_tests_2025/simpson_food.csv:43 (literal) |
| pass | 331.87 | 5 | B_s04-05, sentence 3 | analysis/method_tests_2025/simpson_food.csv:44 (literal) |
| pass | 363.5 | 5 | B_s04-05, sentence 3 | analysis/method_tests_2025/harmonised_comparison.csv:8 (literal) |
| pass | 2021 | 5 | B_s04-05, sentence 4 | analysis/method_tests_2025/harmonised_comparison.csv:8 (literal) |
| pass | 23 | 5 | B_s04-05, sentence 4 | analysis/method_tests_2025/harmonised_comparison.csv:8 (literal) |
| pass | 3,525 | 5 | B_s04-05, sentence 4 | analysis/method_tests_2025/harmonised_comparison.csv:2 (literal) |
| pass | 120.7 | 5 | B_s04-05, sentence 4 | analysis/method_tests_2025/harmonised_comparison.csv:2 (literal) |
| pass | 1990 | 5 | B_s04-05, sentence 11 | register B012:1 (literal) |
| pass | 91 | 5 | B_s04-05, sentence 11 | register B012:1 (literal) |
| pass | 108.9 | 5 | B_s04-05, sentence 12 | analysis/method_tests_2025/henry_godden_summary.csv:2 (literal) |
| pass | 95.7 | 5 | B_s04-05, sentence 12 | analysis/method_tests_2025/henry_godden_summary.csv:2 (literal) |
| pass | 109 | 5 | B_s04-05, sentence 12 | register B008:1 (literal) |
| pass | 96 | 5 | B_s04-05, sentence 12 | register B008:1 (literal) |
| pass | 1990 | 5 | B_s04-05, sentence 13 | analysis/method_tests_2025/henry_godden_summary.csv:2 (literal) |
| pass | 91 | 5 | B_s04-05, sentence 13 | analysis/method_tests_2025/henry_godden_summary.csv:2 (literal) |
| pass | 2021 | 5 | B_s04-05, sentence 14 | register B016:1 (literal) |
| pass | 23 | 5 | B_s04-05, sentence 14 | register B016:1 (literal) |
| pass | 134 | 5 | B_s04-05, sentence 14 | analysis/method_tests_2025/cross_method.csv:2 (literal) |
| pass | 211 | 5 | B_s04-05, sentence 14 | analysis/method_tests_2025/cross_method.csv:2 (literal) |
| pass | 1990 | 5 | B_s04-05, sentence 14 | register B027:1 (literal) |
| pass | 91 | 5 | B_s04-05, sentence 14 | register B027:1 (literal) |
| pass | 1.758 | 5 | B_s04-05, sentence 15 | register B032,B260:1 (literal) |
| pass | 0.095 | 5 | B_s04-05, sentence 15 | register B032:1 (literal) |
| pass | 0.312 | 5 | B_s04-05, sentence 15 | register B032:1 (literal) |
| pass | 1.718 | 5 | B_s04-05, sentence 17 | analysis/method_tests_2025/simpson_food.csv:67 (literal) |
| pass | 1.758 | 5 | B_s04-05, sentence 17 | register B260:1 (literal) |
| pass | 2021 | 5 | B_s04-05, sentence 21 | register B046:1 (literal) |
| pass | 23 | 5 | B_s04-05, sentence 21 | register B046:1 (literal) |
| pass | 146 | 5 | B_s04-05, sentence 21 | analysis/method_tests_2025/harmonised_comparison.csv:13 (literal) |
| pass | 343 | 5 | B_s04-05, sentence 21 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 103 | 5 | B_s04-05, sentence 21 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 3 | 5 | B_s04-05, sentence 21 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 1990 | 5 | B_s04-05, sentence 21 | register B046:1 (literal) |
| pass | 94.8 | 5 | B_s04-05, sentence 25 | analysis/method_tests_2025/half_index.csv:6 (literal) |
| pass | 135.76 | 5 | B_s04-05, sentence 25 | register B057:1 (literal) |
| pass | 2021 | 5 | B_s04-05, sentence 27 | analysis/method_tests_2025/half_index.csv:10 (literal) |
| pass | 23 | 5 | B_s04-05, sentence 27 | analysis/method_tests_2025/half_index.csv:10 (literal) |
| pass | 1.32 | 5 | B_s04-05, sentence 27 | analysis/method_tests_2025/half_index.csv:11 (rounded(x1)) |
| pass | 81.0 | 5 | B_s04-05, sentence 27 | analysis/method_tests_2025/half_index.csv:11 (literal) |
| pass | 363.5 | 5 | B_s04-05, sentence 28 | register B068:1 (literal) |
| pass | 1.318 | 5 | B_s04-05, sentence 28 | register B068:1 (literal) |
| pass | 276 | 5 | B_s04-05, sentence 28 | analysis/method_tests_2025/cross_method.csv:4 (literal) |
| pass | 3 | 5 | B_s04-05, sentence 29 | register B087:1 (literal) |
| pass | 2011 | 5 | B_s04-05, sentence 31 | analysis/method_tests_2025/cassidy.csv:2 (literal) |
| pass | 2000 | 5 | B_s04-05, sentence 31 | register B077:1 (literal) |
| pass | 22 | 5 | B_s04-05, sentence 32 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 42 | 5 | B_s04-05, sentence 32 | analysis/method_tests_2025/cross_method.csv:7 (rounded(x1)) |
| pass | 22 | 5 | B_s04-05, sentence 32 | register B079:1 (literal) |
| pass | 41 | 5 | B_s04-05, sentence 32 | analysis/method_tests_2025/cassidy.csv:3 (literal) |
| pass | 2021 | 5 | B_s04-05, sentence 33 | analysis/method_tests_2025/cassidy_matched.csv:2 (literal) |
| pass | 23 | 5 | B_s04-05, sentence 33 | analysis/method_tests_2025/cassidy_matched.csv:2 (literal) |
| pass | 6.0 | 5 | B_s04-05, sentence 33 | analysis/method_tests_2025/cassidy_matched.csv:8 (literal) |
| pass | 7.9 | 5 | B_s04-05, sentence 33 | analysis/method_tests_2025/cassidy.csv:8 (2021-23 World, delivered 7.9) [auto match was a false positive; checked by hand] |
| pass | 2,700 | 5 | B_s04-05, sentence 34 | register B087:1 (literal) |
| pass | 22 | 5 | B_s04-05, sentence 34 | register B083,B079:1 (literal) |
| pass | 147 | 5 | B_s04-05, sentence 34 | analysis/method_tests_2025/cassidy.csv:13 (literal) |
| pass | 2,700 | 5 | B_s04-05, sentence 34 | analysis/method_tests_2025/cassidy.csv:3 (rounded(x100)) |
| pass | 145 | 5 | B_s04-05, sentence 34 | register B259:1 (literal) |
| pass | 2050 | 5 | B_s04-05, sentence 35 | register B140:1 (literal) |
| pass | 1997 | 5 | B_s04-05, sentence 35 | register B140:1 (literal) |
| pass | 98 | 5 | B_s04-05, sentence 35 | register B140:1 (literal) |
| pass | 1997 | 5 | B_s04-05, sentence 37 | analysis/method_tests_2025/gap_attribution.csv:113 (literal) |
| pass | 98 | 5 | B_s04-05, sentence 37 | analysis/method_tests_2025/gap_attribution.csv:50 (literal) |
| pass | 1.2 | 5 | B_s04-05, sentence 37 | analysis/method_tests_2025/gap_attribution.csv:11 (rounded(x1)) |
| pass | 40 | 5 | B_s04-05, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:13 (literal) |
| pass | 41 | 5 | B_s04-05, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:17 (literal) |
| pass | 128 | 5 | B_s04-05, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:15 (literal) |
| pass | 127 | 5 | B_s04-05, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:18 (literal) |
| pass | 17 | 5 | B_s04-05, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:6 (literal) |
| pass | 12 | 5 | B_s04-05, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:19 (literal) |
| pass | 12 | 5 | B_s04-05, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:19 (literal) |
| pass | 2021 | 5 | B_s04-05, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:3 (literal) |
| pass | 23 | 5 | B_s04-05, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:3 (literal) |
| pass | 150 | 5 | B_s04-05, sentence 40 | analysis/method_tests_2025/harmonised_comparison.csv:23 (literal) |
| pass | 41.5 | 5 | B_s04-05, sentence 41 | analysis/method_tests_2025/cross_method.csv:7 (literal) |
| pass | 1 | 5 | B_s04-05, sentence 42 | analysis/method_tests_2025/fearnside_failure_curve.csv:1 (literal) |
| pass | 10 | 5 | B_s04-05, sentence 42 | analysis/method_tests_2025/fearnside_failure_curve.csv:1 (literal) |
| pass | 30.8 | 5 | B_s04-05, sentence 42 | analysis/method_tests_2025/fearnside_failure_curve.csv:3 (rounded(x1)) |
| pass | 26 | 5 | B_s04-05, sentence 42 | analysis/method_tests_2025/fearnside_failure_curve.csv:3 (last column 0.74, so 26% lower) [derived] |
| pass | 1 | 5 | B_s04-05, sentence 42 | analysis/method_tests_2025/fearnside_failure_curve.csv:1 (literal) |
| pass | 100 | 5 | B_s04-05, sentence 42 | analysis/method_tests_2025/fearnside_failure_curve.csv:1 (literal) |
| pass | 18.9 | 5 | B_s04-05, sentence 42 | analysis/method_tests_2025/fearnside_failure_curve.csv:3 (rounded(x1)) |
| pass | 30 | 5 | B_s04-05, sentence 44 | register B196:1 (literal) |
| pass | 35 | 5 | B_s04-05, sentence 44 | register B196:1 (literal) |
| pass | 30.8 | 5 | B_s04-05, sentence 44 | analysis/method_tests_2025/fearnside_failure_curve.csv:3 (rounded(x1)) |
| pass | 1 | 5 | B_s04-05, sentence 44 | analysis/method_tests_2025/fearnside_failure_curve.csv:1 (literal) |
| pass | 10 | 5 | B_s04-05, sentence 44 | analysis/method_tests_2025/fearnside_failure_curve.csv:1 (literal) |
| pass | 2025 | 5 | B_s04-05, sentence 43 | analysis/method_tests_2025/fearnside_failure_curve.csv:3 (literal) |
| pass | 5.8 | 5 | B_s04-05, sentence 43 | analysis/method_tests_2025/fearnside_failure_curve.csv:3 (literal) |
| pass | 6.1 | 5 | B_s04-05, sentence 43 | analysis/method_tests_2025/fearnside_failure_curve.csv:3 (literal) |
| pass | 1 | 5 | B_s04-05, sentence 43 | analysis/method_tests_2025/fearnside_failure_curve.csv:1 (literal) |
| pass | 16 | 5 | B_s04-05, sentence 43 | analysis/method_tests_2025/fearnside_failure_curve.csv:3 (literal) |
| pass | 17 | 5 | B_s04-05, sentence 43 | analysis/method_tests_2025/fearnside_failure_curve.csv:3 (literal) |
| pass | 12 | 5 | B_s04-05, sentence 50 | analysis/method_tests_2025/cross_method.csv:6 (literal) |
| pass | 41 | 5 | B_s04-05, sentence 50 | analysis/method_tests_2025/cross_method.csv:6 (literal) |
| pass | 40 | 5 | B_s04-05, sentence 50 | analysis/method_tests_2025/cross_method.csv:6 (literal) |
| pass | 41 | 5 | B_s04-05, sentence 50 | analysis/method_tests_2025/cross_method.csv:6 (literal) |
| pass | 145.2 | 5 | B_s04-05, sentence 53 | analysis/method_tests_2025/harmonised_comparison.csv:2 (literal) |
| pass | 148.8 | 5 | B_s04-05, sentence 53 | analysis/method_tests_2025/harmonised_comparison.csv:3 (literal) |
| pass | 110.9 | 5 | B_s04-05, sentence 53 | analysis/method_tests_2025/harmonised_comparison.csv:18 (literal) |
| pass | 112.9 | 5 | B_s04-05, sentence 53 | analysis/method_tests_2025/harmonised_comparison.csv:17 (literal) |
| pass | 2025 | 5 | B_s04-05, Table 4 caption | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 5 | 5 | B_s04-05, Table 4 caption | analysis/method_tests_2025/model_entry.csv:1 (literal) |
| pass | 95 | 5 | B_s04-05, Table 4 caption | analysis/method_tests_2025/model_entry.csv:1 (literal) |
| pass | 10 | 5 | B_s04-05, Table 4 row 1 | analysis/method_tests_2025/model_entry.csv:1 (literal) |
| pass | 100 | 5 | B_s04-05, Table 4 row 1 | analysis/method_tests_2025/model_entry.csv:1 (literal) |
| pass | 2025 | 5 | B_s04-05, Table 4 row 2 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 49.4 | 5 | B_s04-05, Table 4 row 2 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 43.4 | 5 | B_s04-05, Table 4 row 2 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 54.3 | 5 | B_s04-05, Table 4 row 2 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 14.1 | 5 | B_s04-05, Table 4 row 2 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 11.8 | 5 | B_s04-05, Table 4 row 2 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 16.0 | 5 | B_s04-05, Table 4 row 2 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 36.66 | 5 | B_s04-05, Table 4 row 2 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 22.51 | 5 | B_s04-05, Table 4 row 2 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 27.6 | 5 | B_s04-05, Table 4 row 2 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 2025 | 5 | B_s04-05, Table 4 row 3 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 30.81 | 5 | B_s04-05, Table 4 row 3 | analysis/method_tests_2025/model_entry.csv:3 (literal) |
| pass | 18.92 | 5 | B_s04-05, Table 4 row 3 | analysis/method_tests_2025/model_entry.csv:3 (literal) |
| pass | 27.6 | 5 | B_s04-05, Table 4 row 3 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 2025 | 5 | B_s04-05, Table 4 row 4 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 53.6 | 5 | B_s04-05, Table 4 row 4 | analysis/method_tests_2025/model_entry.csv:4 (literal) |
| pass | 46.2 | 5 | B_s04-05, Table 4 row 4 | analysis/method_tests_2025/model_entry.csv:4 (literal) |
| pass | 60.1 | 5 | B_s04-05, Table 4 row 4 | analysis/method_tests_2025/model_entry.csv:4 (literal) |
| pass | 18.5 | 5 | B_s04-05, Table 4 row 4 | analysis/method_tests_2025/model_entry.csv:4 (literal) |
| pass | 15.9 | 5 | B_s04-05, Table 4 row 4 | analysis/method_tests_2025/model_entry.csv:4 (literal) |
| pass | 19.4 | 5 | B_s04-05, Table 4 row 4 | analysis/method_tests_2025/model_entry.csv:4 (literal) |
| pass | 39.93 | 5 | B_s04-05, Table 4 row 4 | analysis/method_tests_2025/model_entry.csv:4 (literal) |
| pass | 24.68 | 5 | B_s04-05, Table 4 row 4 | analysis/method_tests_2025/model_entry.csv:4 (literal) |
| pass | 27.6 | 5 | B_s04-05, Table 4 row 4 | analysis/method_tests_2025/model_entry.csv:2 (literal) |
| pass | 134 | 5 | B_s04-05, Table 3 row 2 | analysis/method_tests_2025/cross_method.csv:2 (literal) |
| pass | 211 | 5 | B_s04-05, Table 3 row 2 | analysis/method_tests_2025/cross_method.csv:2 (literal) |
| pass | 109 | 5 | B_s04-05, Table 3 row 2 | analysis/method_tests_2025/cross_method.csv:2 (literal) |
| pass | 96 | 5 | B_s04-05, Table 3 row 2 | analysis/method_tests_2025/cross_method.csv:2 (literal) |
| pass | 146 | 5 | B_s04-05, Table 3 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:13 (literal) |
| pass | 343 | 5 | B_s04-05, Table 3 row 3 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 103 | 5 | B_s04-05, Table 3 row 3 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 1990 | 5 | B_s04-05, Table 3 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:13 (literal) |
| pass | 103 | 5 | B_s04-05, Table 3 row 3 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 160 | 5 | B_s04-05, Table 3 row 3 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 268 | 5 | B_s04-05, Table 3 row 3 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 343 | 5 | B_s04-05, Table 3 row 3 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 276 | 5 | B_s04-05, Table 3 row 4 | analysis/method_tests_2025/cross_method.csv:4 (literal) |
| pass | 5.8 | 5 | B_s04-05, Table 3 row 5 | analysis/method_tests_2025/cross_method.csv:5 (literal) |
| pass | 6.0 | 5 | B_s04-05, Table 3 row 5 | analysis/method_tests_2025/cross_method.csv:5 (literal) |
| pass | 145 | 5 | B_s04-05, Table 3 row 5 | analysis/method_tests_2025/cross_method.csv:5 (literal) |
| pass | 147 | 5 | B_s04-05, Table 3 row 5 | analysis/method_tests_2025/cross_method.csv:5 (literal) |
| pass | 183 | 5 | B_s04-05, Table 3 row 5 | register B084:1 (literal) |
| pass | 22 | 5 | B_s04-05, Table 3 row 5 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 42 | 5 | B_s04-05, Table 3 row 5 | analysis/method_tests_2025/cross_method.csv:7 (rounded(x1)) |
| pass | 5 | 5 | B_s04-05, Table 3 row 5 | analysis/method_tests_2025/cross_method.csv:4 (literal) |
| pass | 8 | 5 | B_s04-05, Table 3 row 5 | analysis/method_tests_2025/cross_method.csv:4 (literal) |
| pass | 40 | 5 | B_s04-05, Table 3 row 6 | analysis/method_tests_2025/cross_method.csv:6 (literal) |
| pass | 41 | 5 | B_s04-05, Table 3 row 6 | analysis/method_tests_2025/cross_method.csv:6 (literal) |
| pass | 12 | 5 | B_s04-05, Table 3 row 6 | analysis/method_tests_2025/cross_method.csv:6 (literal) |
| pass | 17 | 5 | B_s04-05, Table 3 row 6 | analysis/method_tests_2025/cross_method.csv:6 (literal) |
| pass | 127 | 5 | B_s04-05, Table 3 row 6 | analysis/method_tests_2025/cross_method.csv:6 (literal) |
| pass | 128 | 5 | B_s04-05, Table 3 row 6 | analysis/method_tests_2025/cross_method.csv:6 (literal) |
| pass | 1.2 | 5 | B_s04-05, Table 3 row 6 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 30 | 5 | B_s04-05, Table 3 row 6 | analysis/method_tests_2025/cross_method.csv:6 (literal) |
| pass | 77 | 5 | B_s04-05, Table 3 row 6 | analysis/method_tests_2025/cross_method.csv:6 (literal) |
| pass | 41.5 | 5 | B_s04-05, Table 3 row 7 | analysis/method_tests_2025/cross_method.csv:7 (literal) |
| pass | 30.8 | 5 | B_s04-05, Table 3 row 7 | analysis/method_tests_2025/cross_method.csv:7 (literal) |
| pass | 1 | 5 | B_s04-05, Table 3 row 7 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 10 | 5 | B_s04-05, Table 3 row 7 | analysis/method_tests_2025/cross_method.csv:7 (literal) |
| pass | 18.9 | 5 | B_s04-05, Table 3 row 7 | analysis/method_tests_2025/cross_method.csv:7 (literal) |
| pass | 1 | 5 | B_s04-05, Table 3 row 7 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 100 | 5 | B_s04-05, Table 3 row 7 | analysis/method_tests_2025/cross_method.csv:7 (literal) |
| pass | 103 | 5 | B_s04-05, Table 3 note | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 343 | 5 | B_s04-05, Table 3 note | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 146 | 5 | B_s04-05, Table 3 note | analysis/method_tests_2025/harmonised_comparison.csv:13 (literal) |
| pass | 3 | 5 | B_s04-05, Table 3 note | analysis/method_tests_2025/harmonised_comparison.csv:2 (literal) |
| pass | 2021 | 5 | B_s04-05, Table 3 note | analysis/method_tests_2025/harmonised_comparison.csv:8 (literal) |
| pass | 23 | 5 | B_s04-05, Table 3 note | analysis/method_tests_2025/harmonised_comparison.csv:8 (literal) |
| pass | 190 | 5 | B_s04-05, Table 3 note | analysis/method_tests_2025/cross_method.csv:5 (literal) |
| pass | 134 | 5 | B_s04-05, Table 5 row 2 | analysis/method_tests_2025/harmonised_comparison.csv:3 (rounded(x1)) |
| pass | 211 | 5 | B_s04-05, Table 5 row 2 | analysis/method_tests_2025/harmonised_comparison.csv:6 (rounded(x1)) |
| pass | 145.2 | 5 | B_s04-05, Table 5 row 2 | analysis/method_tests_2025/harmonised_comparison.csv:2 (literal) |
| pass | 148.8 | 5 | B_s04-05, Table 5 row 2 | analysis/method_tests_2025/harmonised_comparison.csv:3 (literal) |
| pass | 0.69 | 5 | B_s04-05, Table 5 row 2 | analysis/method_tests_2025/harmonised_comparison.csv:6 (rounded(x1)) |
| pass | 1.11 | 5 | B_s04-05, Table 5 row 2 | analysis/method_tests_2025/harmonised_comparison.csv:3 (rounded(x1)) |
| pass | 3.50 | 5 | B_s04-05, Table 5 row 2 | analysis/method_tests_2025/harmonised_comparison.csv:2 (rounded(x1)) |
| pass | 3.59 | 5 | B_s04-05, Table 5 row 2 | analysis/method_tests_2025/harmonised_comparison.csv:3 (literal) |
| pass | 103 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:2 (literal) |
| pass | 343 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:10 (literal) |
| pass | 103 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:2 (literal) |
| pass | 160 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:4 (literal) |
| pass | 268 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:15 (literal) |
| pass | 343 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:10 (literal) |
| pass | 139 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:11 (literal) |
| pass | 343 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:10 (literal) |
| pass | 139 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:11 (literal) |
| pass | 160 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:4 (literal) |
| pass | 278 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:3 (rounded(x100)) |
| pass | 343 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:10 (literal) |
| pass | 1.00 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:8 (rounded(x1)) |
| pass | 1.42 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:28 (literal) |
| pass | 3.36 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:11 (literal) |
| pass | 8.27 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:10 (literal) |
| pass | 64.8 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:10 (literal) |
| pass | 117 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:13 (literal) |
| pass | 113 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:17 (rounded(x1)) |
| pass | 117 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:13 (literal) |
| pass | 64.8 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:10 (literal) |
| pass | 84.6 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:15 (literal) |
| pass | 53.9 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:9 (literal) |
| pass | 77.9 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:14 (literal) |
| pass | 1 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:2 (literal) |
| pass | 3 | 5 | B_s04-05, Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv:2 (literal) |
| pass | 276 | 5 | B_s04-05, Table 5 row 4 | analysis/method_tests_2025/harmonised_comparison.csv:16 (rounded(x1)) |
| pass | 275.8 | 5 | B_s04-05, Table 5 row 4 | analysis/method_tests_2025/harmonised_comparison.csv:16 (literal) |
| pass | 1.00 | 5 | B_s04-05, Table 5 row 4 | analysis/method_tests_2025/harmonised_comparison.csv:8 (rounded(x1)) |
| pass | 6.65 | 5 | B_s04-05, Table 5 row 4 | analysis/method_tests_2025/harmonised_comparison.csv:16 (literal) |
| pass | 76.0 | 5 | B_s04-05, Table 5 row 4 | analysis/method_tests_2025/harmonised_comparison.csv:16 (literal) |
| pass | 145 | 5 | B_s04-05, Table 5 row 5 | analysis/method_tests_2025/harmonised_comparison.csv:2 (literal) |
| pass | 183 | 5 | B_s04-05, Table 5 row 5 | register B084:1 (literal) |
| pass | 111 | 5 | B_s04-05, Table 5 row 5 | analysis/method_tests_2025/harmonised_comparison.csv:3 (rounded(x100)) |
| pass | 113 | 5 | B_s04-05, Table 5 row 5 | analysis/method_tests_2025/harmonised_comparison.csv:17 (rounded(x1)) |
| pass | 0.62 | 5 | B_s04-05, Table 5 row 5 | register B273:1 (rounded(x1)) |
| pass | 0.77 | 5 | B_s04-05, Table 5 row 5 | analysis/method_tests_2025/harmonised_comparison.csv:26 (literal) |
| pass | 2.67 | 5 | B_s04-05, Table 5 row 5 | analysis/method_tests_2025/harmonised_comparison.csv:18 (literal) |
| pass | 2.72 | 5 | B_s04-05, Table 5 row 5 | analysis/method_tests_2025/harmonised_comparison.csv:17 (literal) |
| pass | 40 | 5 | B_s04-05, Table 5 row 6 | analysis/method_tests_2025/harmonised_comparison.csv:20 (literal) |
| pass | 17 | 5 | B_s04-05, Table 5 row 6 | analysis/method_tests_2025/harmonised_comparison.csv:21 (literal) |
| pass | 128 | 5 | B_s04-05, Table 5 row 6 | analysis/method_tests_2025/harmonised_comparison.csv:22 (literal) |
| pass | 41 | 5 | B_s04-05, Table 5 row 6 | analysis/method_tests_2025/harmonised_comparison.csv:1 (literal) |
| pass | 12 | 5 | B_s04-05, Table 5 row 6 | analysis/method_tests_2025/harmonised_comparison.csv:20 (literal) |
| pass | 127 | 5 | B_s04-05, Table 5 row 6 | analysis/method_tests_2025/harmonised_comparison.csv:22 (literal) |
| pass | 0.71 | 5 | B_s04-05, Table 5 row 6 | analysis/method_tests_2025/harmonised_comparison.csv:17 (rounded(x0.01)) |
| pass | 1.03 | 5 | B_s04-05, Table 5 row 6 | analysis/method_tests_2025/harmonised_comparison.csv:13 (rounded(x0.01)) |
| pass | 0.29 | 5 | B_s04-05, Table 5 row 6 | analysis/method_tests_2025/harmonised_comparison.csv:21 (literal) |
| pass | 3.06 | 5 | B_s04-05, Table 5 row 6 | analysis/method_tests_2025/harmonised_comparison.csv:22 (literal) |
| pass | 41.5 | 5 | B_s04-05, Table 5 row 7 | analysis/method_tests_2025/harmonised_comparison.csv:1 (literal) |
| pass | 30.8 | 5 | B_s04-05, Table 5 row 7 | analysis/method_tests_2025/harmonised_comparison.csv:24 (literal) |
| pass | 1 | 5 | B_s04-05, Table 5 row 7 | analysis/method_tests_2025/harmonised_comparison.csv:2 (literal) |
| pass | 10 | 5 | B_s04-05, Table 5 row 7 | analysis/method_tests_2025/harmonised_comparison.csv:24 (literal) |
| pass | 18.9 | 5 | B_s04-05, Table 5 row 7 | analysis/method_tests_2025/harmonised_comparison.csv:25 (literal) |
| pass | 1 | 5 | B_s04-05, Table 5 row 7 | analysis/method_tests_2025/harmonised_comparison.csv:2 (literal) |
| pass | 100 | 5 | B_s04-05, Table 5 row 7 | analysis/method_tests_2025/harmonised_comparison.csv:25 (literal) |
| pass | 41.5 | 5 | B_s04-05, Table 5 row 8 | analysis/method_tests_2025/harmonised_comparison.csv:1 (literal) |
| pass | 41.5 | 5 | B_s04-05, Table 5 row 8 | analysis/method_tests_2025/harmonised_comparison.csv:1 (literal) |
| pass | 1.00 | 5 | B_s04-05, Table 5 row 8 | analysis/method_tests_2025/harmonised_comparison.csv:8 (rounded(x1)) |
| pass | 1.00 | 5 | B_s04-05, Table 5 row 8 | analysis/method_tests_2025/harmonised_comparison.csv:8 (rounded(x1)) |
| pass | 53.6 | 5 | B_s04-05, Table 5 row 9 | analysis/method_tests_2025/harmonised_comparison.csv:1 (literal) |
| pass | 53.6 | 5 | B_s04-05, Table 5 row 9 | analysis/method_tests_2025/harmonised_comparison.csv:1 (literal) |
| pass | 1.00 | 5 | B_s04-05, Table 5 row 9 | analysis/method_tests_2025/harmonised_comparison.csv:8 (rounded(x1)) |
| pass | 1.29 | 5 | B_s04-05, Table 5 row 9 | analysis/method_tests_2025/harmonised_comparison.csv:27 (literal) |
| pass | 183 | 5 | B_s04-05, Table 5 note | register B273,B084:1 (literal) |
| pass | 0.62 | 5 | B_s04-05, Table 5 note | register B273,B084:1 (rounded(x1)) |
| pass | 112.9 | 5 | B_s04-05, Table 5 note | analysis/method_tests_2025/harmonised_comparison.csv:17 (literal) |
| pass | 190 | 5 | B_s04-05, Table 5 note | analysis/method_tests_2025/harmonised_comparison.csv:19 (literal) |
| pass | 0.594 | 5 | B_s04-05, Table 5 note | analysis/method_tests_2025/harmonised_comparison.csv:19 (literal) |
| pass | 26.20 | 5 | B_s04-05, sentence 5 | analysis/method_tests_2025/bases.csv:11 (literal) |
| pass | 2025 | 5 | B_s04-05, sentence 5 | analysis/method_tests_2025/bases.csv:2 (literal) |
| pass | 27.6 | 5 | B_s04-05, sentence 5 | analysis/method_tests_2025/bases.csv:3 (rounded(x1)) |
| pass | 1.718 | 5 | B_s04-05, sentence 17 | analysis/method_tests_2025/fidelity.csv:6 (rounded(x1)) |
| pass | 1.758 | 5 | B_s04-05, sentence 17 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 2.3 | 5 | B_s04-05, sentence 17 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 1 | 5 | B_s04-05, sentence 17 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 1.2 | 5 | B_s04-05, sentence 17 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 21.7 | 5 | B_s04-05, sentence 18 | qa/reports/V42_check_B116.md:33 (literal) |
| pass | 4 | 5 | B_s04-05, sentence 18 | analysis/method_tests_2025/fidelity.csv:15 (literal) |
| pass | 11.9 | 5 | B_s04-05, sentence 19 | analysis/method_tests_2025/fidelity.csv:9 (literal) |
| pass | 64.8 | 5 | B_s04-05, sentence 20 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 117.0 | 5 | B_s04-05, sentence 20 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 64.8 | 5 | B_s04-05, sentence 20 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 84.6 | 5 | B_s04-05, sentence 20 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 146 | 5 | B_s04-05, sentence 21 | qa/reports/B113_harmonised_both_lines.md:56 (literal) |
| pass | 343 | 5 | B_s04-05, sentence 21 | qa/reports/B113_harmonised_both_lines.md:35 (literal) |
| pass | 103 | 5 | B_s04-05, sentence 21 | qa/reports/B113_harmonised_both_lines.md:35 (literal) |
| pass | 3 | 5 | B_s04-05, sentence 21 | qa/reports/B113_harmonised_both_lines.md:3 (literal) |
| pass | 1990 | 5 | B_s04-05, sentence 21 | qa/reports/B113_harmonised_both_lines.md:57 (literal) |
| pass | 2.2 | 5 | B_s04-05, sentence 23 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 34.4 | 5 | B_s04-05, sentence 23 | analysis/method_tests_2025/fidelity.csv:12 (rounded(x1)) |
| pass | 35.13 | 5 | B_s04-05, sentence 23 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 0.8 | 5 | B_s04-05, sentence 23 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 113.1 | 5 | B_s04-05, sentence 23 | analysis/method_tests_2025/fidelity.csv:13 (rounded(x1)) |
| pass | 112.20 | 5 | B_s04-05, sentence 23 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 2.8 | 5 | B_s04-05, sentence 23 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 8.4 | 5 | B_s04-05, sentence 23 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 121.6 | 5 | B_s04-05, sentence 23 | analysis/method_tests_2025/fidelity.csv:13 (rounded(x1)) |
| pass | 94.7 | 5 | B_s04-05, sentence 24 | qa/reports/V42_check_B116.md:28 (literal) |
| pass | 94.8 | 5 | B_s04-05, sentence 25 | analysis/method_tests_2025/fidelity.csv:17 (literal) |
| pass | 135.76 | 5 | B_s04-05, sentence 25 | analysis/method_tests_2025/fidelity.csv:17 (literal) |
| pass | 76.0 | 5 | B_s04-05, sentence 28 | analysis/method_tests_2025/cross_method_local.csv:6 (literal) |
| pass | 61 | 5 | B_s04-05, sentence 31 | analysis/method_tests_2025/fidelity.csv:30 (literal) |
| pass | 59 | 5 | B_s04-05, sentence 31 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 41 | 5 | B_s04-05, sentence 31 | analysis/method_tests_2025/fidelity.csv:18 (literal) |
| pass | 67 | 5 | B_s04-05, sentence 31 | analysis/method_tests_2025/fidelity.csv:3 (literal) |
| pass | 32 | 5 | B_s04-05, sentence 31 | analysis/method_tests_2025/fidelity.csv:10 (rounded(x1000)) |
| pass | 6 | 5 | B_s04-05, sentence 31 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 22 | 5 | B_s04-05, sentence 32 | analysis/method_tests_2025/fidelity.csv:5 (literal) |
| pass | 42 | 5 | B_s04-05, sentence 32 | analysis/method_tests_2025/fidelity.csv:11 (literal) |
| pass | 5 | 5 | B_s04-05, sentence 32 | analysis/method_tests_2025/fidelity.csv:2 (literal) |
| pass | 25 | 5 | B_s04-05, sentence 32 | analysis/method_tests_2025/fidelity.csv:25 (literal) |
| pass | 65 | 5 | B_s04-05, sentence 48 | analysis/method_tests_2025/cross_method_local.csv:3 (rounded(x1)) |
| pass | 211 | 5 | B_s04-05, sentence 48 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 1.6 | 5 | B_s04-05, sentence 48 | analysis/method_tests_2025/cross_method_local.csv:3 (rounded(x1)) |
| pass | 5 | 5 | B_s04-05, sentence 48 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 64.8 | 5 | B_s04-05, sentence 48 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 117.0 | 5 | B_s04-05, sentence 48 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 1.56 | 5 | B_s04-05, sentence 48 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 2.82 | 5 | B_s04-05, sentence 48 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 76.0 | 5 | B_s04-05, sentence 48 | analysis/method_tests_2025/cross_method_local.csv:6 (literal) |
| pass | 1.83 | 5 | B_s04-05, sentence 48 | analysis/method_tests_2025/cross_method_local.csv:6 (literal) |
| pass | 134 | 5 | B_s04-05, sentence 49 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 343 | 5 | B_s04-05, sentence 49 | analysis/method_tests_2025/cross_method_local.csv:5 (literal) |
| pass | 31.1 | 5 | B_s04-05, sentence 51 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 49.2 | 5 | B_s04-05, sentence 51 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 19 | 5 | B_s04-05, Table 6 caption | analysis/method_tests_2025/harmonised_comparison_lines.csv:31 (literal) |
| pass | 41.5 | 5 | B_s04-05, sentence 59 | analysis/method_tests_2025/harmonised_comparison_lines.csv:26 (literal) |
| pass | 0.646 | 5 | B_s04-05, sentence 60 | analysis/method_tests_2025/harmonised_comparison_lines.csv:47 (literal) |
| pass | 0.702 | 5 | B_s04-05, sentence 60 | analysis/method_tests_2025/harmonised_comparison_lines.csv:47 (literal) |
| pass | 6.22 | 5 | B_s04-05, sentence 60 | analysis/method_tests_2025/harmonised_comparison_lines.csv:48 (literal) |
| pass | 6.95 | 5 | B_s04-05, sentence 60 | analysis/method_tests_2025/harmonised_comparison_lines.csv:48 (literal) |
| pass | 4.1 | 5 | B_s04-05, sentence 60 | analysis/method_tests_2025/harmonised_comparison_lines.csv:31 (rounded(x100)) |
| pass | 38.5 | 5 | B_s04-05, sentence 61 | analysis/method_tests_2025/harmonised_comparison_lines.csv:80 (rounded(x100)) |
| pass | 0.440 | 5 | B_s04-05, sentence 61 | analysis/method_tests_2025/harmonised_comparison_lines.csv:96 (rounded(x1)) |
| pass | 3.70 | 5 | B_s04-05, sentence 61 | analysis/method_tests_2025/harmonised_comparison_lines.csv:97 (rounded(x1)) |
| pass | -4.9 | 5 | B_s04-05, sentence 62 | analysis/method_tests_2025/harmonised_comparison_lines.csv:38 (rounded(x100)) |
| pass | -6.3 | 5 | B_s04-05, sentence 62 | analysis/method_tests_2025/harmonised_comparison_lines.csv:45 (rounded(x100)) |
| pass | 16.0 | 5 | B_s04-05, sentence 62 | analysis/method_tests_2025/harmonised_comparison_lines.csv:40 (rounded(x100)) |
| pass | 17.2 | 5 | B_s04-05, sentence 62 | analysis/method_tests_2025/harmonised_comparison_lines.csv:94 (rounded(x100)) |
| pass | 5 | 5 | B_s04-05, sentence 65 | analysis/method_tests_2025/gap_attribution_readable.csv:1 (literal) |
| pass | 0.92 | 5 | B_s04-05, sentence 66 | analysis/method_tests_2025/gap_attribution_readable.csv:19 (literal) |
| pass | 5.76 | 5 | B_s04-05, sentence 66 | analysis/method_tests_2025/gap_attribution_readable.csv:24 (literal) |
| pass | 9.2 | 5 | B_s04-05, sentence 66 | analysis/method_tests_2025/gap_attribution_readable.csv:24 (literal) |
| pass | 169.7 | 5 | B_s04-05, sentence 70 | analysis/method_tests_2025/intake_variant.csv:2 (literal) |
| pass | 182.2 | 5 | B_s04-05, sentence 70 | qa/reports/V42_check_B116.md:51 (literal) |
| pass | 132.0 | 5 | B_s04-05, sentence 70 | analysis/method_tests_2025/intake_variant.csv:12 (literal) |
| pass | 324.8 | 5 | B_s04-05, sentence 70 | qa/reports/V42_check_B116.md:53 (literal) |
| pass | 189.0 | 5 | B_s04-05, sentence 70 | analysis/method_tests_2025/intake_variant.csv:4 (literal) |
| pass | 404.8 | 5 | B_s04-05, sentence 70 | analysis/method_tests_2025/intake_variant.csv:6 (literal) |
| pass | 48.1 | 5 | B_s04-05, sentence 70 | analysis/method_tests_2025/intake_variant.csv:14 (literal) |
| pass | 19.7 | 5 | B_s04-05, sentence 70 | analysis/method_tests_2025/intake_variant.csv:15 (literal) |
| pass | 137.2 | 5 | B_s04-05, sentence 70 | analysis/method_tests_2025/intake_variant.csv:16 (literal) |
| pass | 2.7 | 5 | B_s04-05, sentence 72 | analysis/method_tests_2025/intake_variant.csv:12 (rounded(x1)) |
| pass | 9.3 | 5 | B_s04-05, sentence 72 | analysis/method_tests_2025/intake_variant.csv:5 (rounded(x1)) |
| pass | 3.1 | 5 | B_s04-05, sentence 72 | analysis/method_tests_2025/intake_variant.csv:2 (rounded(x1)) |
| pass | 10.9 | 5 | B_s04-05, sentence 72 | analysis/method_tests_2025/intake_variant.csv:5 (rounded(x1)) |
| pass | 3.3 | 5 | B_s04-05, sentence 72 | analysis/method_tests_2025/intake_variant.csv:3 (literal) |
| pass | 12.9 | 5 | B_s04-05, sentence 72 | analysis/method_tests_2025/intake_variant.csv:5 (rounded(x1)) |
| pass | 81.7 | 5 | B_s04-05, sentence 79 | analysis/pasture_2025/pairing_relaxed.csv:3 (rounded(x1)) |
| pass | 76.0 | 5 | B_s04-05, sentence 79 | analysis/pasture_2025/pairing_relaxed.csv:3 (literal) |
| pass | 93 | 5 | B_s04-05, sentence 79 | analysis/pasture_2025/pairing_relaxed.csv:2 (literal) |
| pass | 84.6 | 5 | B_s04-05, sentence 79 | analysis/pasture_2025/pairing_relaxed.csv:3 (literal) |
| pass | 93 | 5 | B_s04-05, sentence 79 | analysis/pasture_2025/pairing_relaxed.csv:2 (literal) |
| pass | 81 | 5 | B_s04-05, sentence 79 | analysis/pasture_2025/pairing_relaxed.csv:3 (literal) |
| pass | 2 | 5 | B_s04-05, sentence 81 | analysis/pasture_2025/pairing_relaxed.csv:2 (literal) |
| pass | 107.7 | 5 | B_s04-05, sentence 81 | analysis/pasture_2025/pairing_relaxed.csv:5 (rounded(x1)) |
| pass | 0.5 | 5 | B_s04-05, sentence 81 | analysis/pasture_2025/pairing_relaxed.csv:3 (rounded(x0.01)) |
| pass | 0.6 | 5 | B_s04-05, sentence 81 | analysis/pasture_2025/pairing_relaxed.csv:3 (rounded(x0.01)) |
| pass | 4.2 | 5 | B_s04-05, sentence 81 | qa/reports/B114_pairing_relaxed.md:74 (literal) |
| pass | 2.5 | 5 | B_s04-05, sentence 81 | qa/reports/B114_pairing_relaxed.md:75 (literal) |
| pass | 118.0 | 5 | B_s04-05, sentence 81 | qa/reports/B114_pairing_relaxed.md:75 (literal) |
| pass | 3 | 5 | B_s04-05, sentence 82 | analysis/pasture_2025/pairing_relaxed.csv:3 (literal) |
| pass | 172.3 | 5 | B_s04-05, sentence 82 | analysis/pasture_2025/pairing_relaxed.csv:6 (rounded(x1)) |
| pass | 82 | 5 | B_s04-05, sentence 84 | analysis/pasture_2025/pairing_relaxed.csv:3 (rounded(x1)) |
| pass | 108 | 5 | B_s04-05, sentence 84 | analysis/pasture_2025/pairing_relaxed.csv:5 (rounded(x1)) |
| pass | 3.5 | 5 | B_s04-05, sentence 77 | qa/reports/B114_pairing_relaxed.md:22 (literal) |
| pass | 4.0 | 5 | B_s04-05, sentence 77 | qa/reports/B114_pairing_relaxed.md:22 (literal) |
| pass | 41.5 | 5 | B_s04-05, Table 6 row 1 | analysis/method_tests_2025/harmonised_comparison_lines.csv:26 (literal) |
| pass | 19 | 5 | B_s04-05, Table 6 row 6 | analysis/method_tests_2025/harmonised_comparison_lines.csv:31 (literal) |
| pass | 19 | 5 | B_s04-05, Table 6 row 7 | analysis/method_tests_2025/harmonised_comparison_lines.csv:31 (literal) |
| pass | 164.7 | 5 | B_s04-05, Table 6 caption | analysis/method_tests_2025/harmonised_comparison_lines.csv:8 (literal) |
| pass | 9.6 | 5 | B_s04-05, Table 6 caption | analysis/method_tests_2025/harmonised_comparison_lines.csv:32 (rounded(x100)) |
| pass | 41.3 | 5 | B_s04-05, Table 6 caption | analysis/method_tests_2025/harmonised_comparison_lines.csv:81 (rounded(x100)) |
| pass | 41.50 | 5 | B_s04-05, Table 7 row 1 | analysis/pasture_2025/pairing_relaxed.csv:2 (literal) |
| pass | 15.62 | 5 | B_s04-05, Table 7 row 1 | analysis/pasture_2025/pairing_relaxed.csv:8 (literal) |
| pass | 81.70 | 5 | B_s04-05, Table 7 row 2 | analysis/pasture_2025/pairing_relaxed.csv:3 (literal) |
| pass | 21.87 | 5 | B_s04-05, Table 7 row 2 | analysis/pasture_2025/pairing_relaxed.csv:9 (literal) |
| pass | 173 | 5 | B_s04-05, Table 7 row 2 | analysis/pasture_2025/pairing_relaxed.csv:3 (literal) |
| pass | 117 | 5 | B_s04-05, Table 7 row 2 | analysis/pasture_2025/pairing_relaxed.csv:3 (literal) |
| pass | 93 | 5 | B_s04-05, Table 7 row 2 | analysis/pasture_2025/pairing_relaxed.csv:2 (literal) |
| pass | 107.69 | 5 | B_s04-05, Table 7 row 3 | analysis/pasture_2025/pairing_relaxed.csv:5 (literal) |
| pass | 21.90 | 5 | B_s04-05, Table 7 row 3 | analysis/pasture_2025/pairing_relaxed.csv:11 (literal) |
| pass | 284 | 5 | B_s04-05, Table 7 row 3 | analysis/pasture_2025/pairing_relaxed.csv:5 (literal) |
| pass | 192 | 5 | B_s04-05, Table 7 row 3 | analysis/pasture_2025/pairing_relaxed.csv:5 (literal) |
| pass | 154 | 5 | B_s04-05, Table 7 row 3 | analysis/pasture_2025/pairing_relaxed.csv:5 (literal) |
| pass | 172.31 | 5 | B_s04-05, Table 7 row 4 | analysis/pasture_2025/pairing_relaxed.csv:6 (literal) |
| pass | 41.5 | 5 | B_s04-05, Table 4 row 3 | analysis/method_tests_2025/model_entry.csv:3 (literal) |
| pass | 31.1 | 5 | B_s04-05, Table 4 row 3 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 49.2 | 5 | B_s04-05, Table 4 row 3 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 15.6 | 5 | B_s04-05, Table 4 row 3 | analysis/method_tests_2025/model_entry.csv:3 (literal) |
| pass | 13.3 | 5 | B_s04-05, Table 4 row 3 | results/ranges_2025-fixed_wide.csv:4 (rounded(x1e-06)) |
| pass | 18.8 | 5 | B_s04-05, Table 4 row 3 | results/ranges_2025-fixed_wide.csv:4 (rounded(x1e-06)) |
| pass | 13 | 5 | B_s04-05, Table 4 caption | results/ranges_2025-mirror.csv:26 (literal) |
| pass | 1,000 | 5 | B_s04-05, Table 4 caption | results/ranges_2025-mirror.csv:2 (rounded(x1000)) |
| pass | 64.8 | 5 | B_s04-05, Table 3 row 3 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 117.0 | 5 | B_s04-05, Table 3 row 3 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 146 | 5 | B_s04-05, Table 3 row 3 | qa/reports/B113_harmonised_both_lines.md:56 (literal) |
| pass | 343 | 5 | B_s04-05, Table 3 row 3 | qa/reports/B113_harmonised_both_lines.md:35 (literal) |
| pass | 103 | 5 | B_s04-05, Table 3 row 3 | qa/reports/B113_harmonised_both_lines.md:35 (literal) |
| pass | 1990 | 5 | B_s04-05, Table 3 row 3 | qa/reports/B113_harmonised_both_lines.md:57 (literal) |
| pass | 2.3 | 5 | B_s04-05, Table 3 row 3 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 76.0 | 5 | B_s04-05, Table 3 row 4 | analysis/method_tests_2025/cross_method_local.csv:6 (literal) |
| pass | 0.8 | 5 | B_s04-05, Table 3 row 4 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 2.2 | 5 | B_s04-05, Table 3 row 4 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 8.4 | 5 | B_s04-05, Table 3 row 4 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 2.8 | 5 | B_s04-05, Table 3 row 4 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 22 | 5 | B_s04-05, Table 3 row 5 | analysis/method_tests_2025/fidelity.csv:5 (literal) |
| pass | 42 | 5 | B_s04-05, Table 3 row 5 | analysis/method_tests_2025/fidelity.csv:11 (literal) |
| pass | 5 | 5 | B_s04-05, Table 3 row 5 | analysis/method_tests_2025/fidelity.csv:2 (literal) |
| pass | 25 | 5 | B_s04-05, Table 3 row 5 | analysis/method_tests_2025/fidelity.csv:25 (literal) |
| pass | 41.5 | 5 | B_s04-05, Table 3 row 8 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 31.1 | 5 | B_s04-05, Table 3 row 8 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 49.2 | 5 | B_s04-05, Table 3 row 8 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 53.6 | 5 | B_s04-05, Table 3 row 9 | results/ranges_2025-improved.csv:2 (rounded(x1e-06)) |
| pass | 46.2 | 5 | B_s04-05, Table 3 row 9 | results/ranges_2025-improved.csv:2 (rounded(x1e-06)) |
| pass | 60.1 | 5 | B_s04-05, Table 3 row 9 | results/ranges_2025-improved.csv:2 (rounded(x1e-06)) |
| pass | 78 | 5 | B_s04-05, Table 5 caption | analysis/method_tests_2025/harmonised_comparison.csv:1 (literal) |
| pass | 3,364 | 5 | B_s04-05, sentence 24 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 3,182 | 5 | B_s04-05, sentence 24 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 2 | 5 | B_s04-05, sentence 8 | analysis/method_tests_2025/fidelity.csv:2 (literal) |
| pass | 10 | 5 | B_s04-05, sentence 8 | analysis/method_tests_2025/fidelity.csv:9 (literal) |
| pass | 10 | 5 | B_s04-05, sentence 8 | analysis/method_tests_2025/fidelity.csv:9 (literal) |
| pass | 2025 | 6 | B_s06-09, sentence 1 | results/releases.json:143 (literal) |
| pass | 100 | 6 | B_s06-09, sentence 4 | analysis/method_tests_2025/ladder.csv:3 (literal) |
| pass | 2,100 | 6 | B_s06-09, sentence 5 | analysis/comparators_2025/energy_exports.py:6 (literal) |
| pass | 87 | 6 | B_s06-09, sentence 5 | register B164:1 (literal) |
| pass | 128 | 6 | B_s06-09, sentence 5 | analysis/comparators_2025/energy_exports.csv:3 (rounded(x1)) |
| pass | 184 | 6 | B_s06-09, sentence 5 | analysis/comparators_2025/energy_exports.csv:8 (rounded(x1)) |
| pass | 264 | 6 | B_s06-09, sentence 5 | analysis/comparators_2025/energy_exports.csv:9 (rounded(x1)) |
| pass | 41.5 | 6 | B_s06-09, sentence 6 | analysis/method_tests_2025/design_choices.csv:2 (literal) |
| pass | 2.41 | 6 | B_s06-09, sentence 6 | analysis/method_tests_2025/design_choices.csv:11 (literal) |
| pass | 4.4 | 6 | B_s06-09, sentence 6 | analysis/method_tests_2025/design_choices.csv:12 (rounded(x1)) |
| pass | 6.4 | 6 | B_s06-09, sentence 6 | analysis/method_tests_2025/design_choices.csv:13 (rounded(x1)) |
| pass | 41.5 | 6 | B_s06-09, sentence 9 | analysis/method_tests_2025/design_choices.csv:2 (literal) |
| pass | 53.6 | 6 | B_s06-09, sentence 9 | analysis/method_tests_2025/design_choices.csv:4 (literal) |
| pass | 1.29 | 6 | B_s06-09, sentence 9 | analysis/method_tests_2025/design_choices.csv:9 (literal) |
| pass | 12 | 6 | B_s06-09, sentence 11 | analysis/method_tests_2025/design_choices.csv:3 (literal) |
| pass | 41.5 | 6 | B_s06-09, sentence 11 | analysis/method_tests_2025/design_choices.csv:2 (literal) |
| pass | 55.3 | 6 | B_s06-09, sentence 11 | analysis/method_tests_2025/design_choices.csv:3 (literal) |
| pass | 1.33 | 6 | B_s06-09, sentence 11 | analysis/method_tests_2025/design_choices.csv:3 (literal) |
| pass | 53.6 | 6 | B_s06-09, sentence 12 | analysis/method_tests_2025/design_choices.csv:4 (literal) |
| pass | 62.9 | 6 | B_s06-09, sentence 12 | analysis/method_tests_2025/design_choices.csv:4 (literal) |
| pass | 1.17 | 6 | B_s06-09, sentence 12 | analysis/method_tests_2025/design_choices.csv:4 (literal) |
| pass | 6 | 6 | B_s06-09, sentence 13 | analysis/waste_2025/README.md:42 (literal) |
| pass | 12.3 | 6 | B_s06-09, sentence 13 | label (UN Target 12.3), not a figure |
| pass | 70 | 6 | B_s06-09, sentence 15 | register B232:1 (literal) |
| pass | 40.5 | 6 | B_s06-09, sentence 15 | register B232:1 (literal) |
| pass | 70 | 6 | B_s06-09, sentence 15 | register B232:1 (literal) |
| pass | 1.73 | 6 | B_s06-09, sentence 15 | register B232:1 (literal) |
| pass | 1975 | 6 | B_s06-09, sentence 17 | register B170,B106:2 (literal) |
| pass | 41.5 | 6 | B_s06-09, sentence 17 | analysis/method_tests_2025/design_choices.csv:2 (literal) |
| pass | 45.1 | 6 | B_s06-09, sentence 17 | analysis/method_tests_2025/design_choices.csv:5 (literal) |
| pass | 1.09 | 6 | B_s06-09, sentence 17 | analysis/method_tests_2025/design_choices.csv:5 (literal) |
| pass | 58.3 | 6 | B_s06-09, sentence 18 | analysis/comparators_2025/rerun.csv:58 (rounded(x1)) |
| pass | 9 | 6 | B_s06-09, sentence 18 | register B109:1 (literal) |
| pass | 15 | 6 | B_s06-09, sentence 19 | analysis/comparators_2025/diet_land.csv:9 (literal) |
| pass | 5 | 6 | B_s06-09, sentence 19 | analysis/comparators_2025/diet_land.csv:2 (literal) |
| pass | 48.3 | 6 | B_s06-09, sentence 19 | analysis/comparators_2025/diet_land.csv:9 (literal) |
| pass | 103.3 | 6 | B_s06-09, sentence 19 | analysis/comparators_2025/diet_land.csv:5 (literal) |
| pass | 2.14 | 6 | B_s06-09, sentence 19 | analysis/method_tests_2025/design_choices.csv:7 (literal) |
| pass | 53.6 | 6 | B_s06-09, sentence 20 | analysis/comparators_2025/diet_land.csv:2 (literal) |
| pass | 422.3 | 6 | B_s06-09, sentence 20 | analysis/comparators_2025/diet_land.csv:12 (literal) |
| pass | 7.88 | 6 | B_s06-09, sentence 20 | analysis/method_tests_2025/design_choices.csv:8 (literal) |
| pass | 2.5 | 6 | B_s06-09, sentence 21 | analysis/comparators_2025/diet_land.csv:4 (literal) |
| pass | 5 | 6 | B_s06-09, sentence 21 | analysis/comparators_2025/diet_land.csv:2 (literal) |
| pass | 103.3 | 6 | B_s06-09, sentence 21 | analysis/comparators_2025/diet_land.csv:5 (literal) |
| pass | 7.5 | 6 | B_s06-09, sentence 21 | analysis/comparators_2025/diet_land.csv:6 (literal) |
| pass | 66.9 | 6 | B_s06-09, sentence 21 | analysis/comparators_2025/diet_land.csv:6 (literal) |
| pass | 50 | 6 | B_s06-09, sentence 24 | analysis/comparators_2025/rerun.csv:6 (literal) |
| pass | 23 | 6 | B_s06-09, sentence 24 | analysis/comparators_2025/rerun.csv:26 (literal) |
| pass | 30 | 6 | B_s06-09, sentence 24 | analysis/comparators_2025/rerun.csv:24 (literal) |
| pass | 100 | 6 | B_s06-09, sentence 24 | analysis/comparators_2025/rerun.csv:7 (literal) |
| pass | 19 | 6 | B_s06-09, sentence 24 | analysis/comparators_2025/rerun.csv:15 (literal) |
| pass | 25 | 6 | B_s06-09, sentence 24 | analysis/comparators_2025/rerun.csv:25 (literal) |
| pass | 100 | 6 | B_s06-09, sentence 25 | analysis/method_tests_2025/design_choices.csv:2 (literal) |
| pass | 41.5 | 6 | B_s06-09, sentence 25 | analysis/method_tests_2025/design_choices.csv:2 (literal) |
| pass | 18.9 | 6 | B_s06-09, sentence 25 | analysis/method_tests_2025/design_choices.csv:2 (literal) |
| pass | 2.19 | 6 | B_s06-09, sentence 25 | analysis/method_tests_2025/design_choices.csv:2 (literal) |
| pass | 2025 | 6 | B_s06-09, sentence 27 | results/scale_curve.csv:86 (literal) |
| pass | 41.5 | 6 | B_s06-09, sentence 28 | results/scale_curve.csv:114 (rounded(x1e-06)) |
| pass | 75 | 6 | B_s06-09, sentence 29 | results/scale_curve.csv:115 (rounded(x100)) |
| pass | 37 | 6 | B_s06-09, sentence 29 | results/scale_curve.csv:165 (literal) |
| pass | 37 | 6 | B_s06-09, sentence 30 | results/scale_curve.csv:165 (literal) |
| pass | 15.5 | 6 | B_s06-09, sentence 30 | results/scale_curve.csv:127 (rounded(x1e-06)) |
| pass | 2.67 | 6 | B_s06-09, sentence 31 | analysis/method_tests_2025/design_choices.csv:6 (literal) |
| pass | 2020 | 6 | B_s06-09, sentence 32 | results/scale_curve.csv:5 (literal) |
| pass | 21 | 6 | B_s06-09, sentence 32 | results/scale_curve.csv:5 (literal) |
| pass | 54 | 6 | B_s06-09, sentence 33 | results/scale_curve.csv:120 (2025-fixed SA2 local, 0.539) [auto match was a 2011 row; checked by hand] |
| pass | 100 | 6 | B_s06-09, sentence 36 | analysis/method_tests_2025/ladder.csv:3 (literal) |
| pass | 30 | 6 | B_s06-09, sentence 36 | analysis/method_tests_2025/ladder.csv:3 (literal) |
| pass | 15.6 | 6 | B_s06-09, sentence 37 | analysis/method_tests_2025/design_choices.csv:10 (literal) |
| pass | 41.5 | 6 | B_s06-09, sentence 37 | analysis/method_tests_2025/design_choices.csv:2 (literal) |
| pass | 2.66 | 6 | B_s06-09, sentence 37 | analysis/method_tests_2025/design_choices.csv:10 (literal) |
| pass | 5 | 6 | B_s06-09, sentence 41 | results/ranges_2025-fixed.csv:1 (literal) |
| pass | 95 | 6 | B_s06-09, sentence 41 | results/ranges_2025-fixed.csv:1 (literal) |
| pass | 18.9 | 6 | B_s06-09, sentence 47 | analysis/comparators_2025/rerun.csv:47 (rounded(x1)) |
| pass | 100 | 6 | B_s06-09, sentence 47 | analysis/comparators_2025/rerun.csv:7 (literal) |
| pass | 55.3 | 6 | B_s06-09, sentence 47 | analysis/comparators_2025/rerun.csv:50 (rounded(x1)) |
| pass | 62.9 | 6 | B_s06-09, sentence 48 | analysis/comparators_2025/rerun.csv:60 (rounded(x1)) |
| pass | 9.4 | 6 | B_s06-09, sentence 50 | analysis/method_tests_2025/ladder.csv:2 (literal) |
| pass | 100 | 6 | B_s06-09, sentence 50 | analysis/method_tests_2025/ladder.csv:3 (literal) |
| pass | 10.6 | 6 | B_s06-09, sentence 50 | register B005:1 (literal) |
| pass | 1.66 | 6 | B_s06-09, sentence 50 | register B189:1 (literal) |
| pass | 9.4 | 6 | B_s06-09, sentence 50 | analysis/method_tests_2025/ladder.csv:2 (literal) |
| pass | 15.6 | 6 | B_s06-09, sentence 50 | analysis/method_tests_2025/ladder.csv:3 (literal) |
| pass | 4.03 | 6 | B_s06-09, sentence 50 | register B190:1 (literal) |
| pass | 15.6 | 6 | B_s06-09, sentence 50 | analysis/method_tests_2025/ladder.csv:3 (literal) |
| pass | 62.9 | 6 | B_s06-09, sentence 50 | analysis/method_tests_2025/ladder.csv:9 (literal) |
| pass | 1.59 | 6 | B_s06-09, sentence 50 | register B191:1 (literal) |
| pass | 62.9 | 6 | B_s06-09, sentence 50 | analysis/method_tests_2025/ladder.csv:9 (literal) |
| pass | 100 | 6 | B_s06-09, sentence 50 | analysis/method_tests_2025/ladder.csv:3 (literal) |
| pass | 2011 | 6 | B_s06-09, sentence 52 | analysis/method_tests_2025/ladder.csv:2 (literal) |
| pass | 2025 | 6 | B_s06-09, sentence 52 | analysis/method_tests_2025/ladder.csv:3 (literal) |
| pass | 1.09 | 6 | B_s06-09, sentence 53 | analysis/method_tests_2025/design_choices.csv:5 (literal) |
| pass | 4.4 | 6 | B_s06-09, sentence 53 | analysis/method_tests_2025/design_choices.csv:12 (rounded(x1)) |
| pass | 6.4 | 6 | B_s06-09, sentence 53 | analysis/method_tests_2025/design_choices.csv:13 (rounded(x1)) |
| pass | 7.88 | 6 | B_s06-09, sentence 53 | analysis/method_tests_2025/design_choices.csv:8 (literal) |
| pass | 9.4 | 6 | B_s06-09, Figure 3 placeholder | analysis/method_tests_2025/ladder.csv:2 (literal) |
| pass | 100 | 6 | B_s06-09, Figure 3 placeholder | analysis/method_tests_2025/ladder.csv:3 (literal) |
| pass | 10.6 | 6 | B_s06-09, Figure 3 placeholder | register B005,B192,B189,B191:1 (literal) |
| pass | 223.9 | 6 | B_s06-09, Figure 3 placeholder | analysis/method_tests_2025/ladder.csv:11 (literal) |
| pass | 1995 | 7 | B_s06-09, sentence 11 | papers/B_methods/SECTION7_DRAFT.md:28 (literal) |
| pass | 1975 | 7 | B_s06-09, sentence 11 | papers/B_methods/SECTION7_DRAFT.md:28 (literal) |
| pass | 30 | 7 | B_s06-09, sentence 11 | register B222:1 (literal) |
| pass | 32 | 7 | B_s06-09, sentence 11 | register B222:1 (literal) |
| pass | 23,600 | 7 | B_s06-09, sentence 15 | register B244:1 (literal) |
| pass | 2011 | 7 | B_s06-09, sentence 16 | analysis/method_tests_2025/half_index.csv:2 (literal) |
| pass | 2021 | 7 | B_s06-09, sentence 16 | analysis/method_tests_2025/half_index.csv:10 (literal) |
| pass | 23 | 7 | B_s06-09, sentence 16 | analysis/method_tests_2025/half_index.csv:10 (literal) |
| pass | 2.4 | 7 | B_s06-09, sentence 16 | register B067:1 (literal) |
| pass | 1 | 7 | B_s06-09, Table 9 row 1 | papers/B_methods/SECTION7_DRAFT.md:13 (literal) |
| pass | 2 | 7 | B_s06-09, Table 9 row 2 | papers/B_methods/SECTION7_DRAFT.md:14 (literal) |
| pass | 9 | 7 | B_s06-09, Table 9 row 2 | papers/B_methods/SECTION7_DRAFT.md:14 (literal) |
| pass | 100 | 7 | B_s06-09, Table 9 row 2 | papers/B_methods/SECTION7_DRAFT.md:14 (literal) |
| pass | 3 | 7 | B_s06-09, Table 9 row 3 | papers/B_methods/SECTION7_DRAFT.md:15 (literal) |
| pass | 4 | 7 | B_s06-09, Table 9 row 4 | papers/B_methods/SECTION7_DRAFT.md:16 (literal) |
| pass | 100 | 8 | B_s06-09, sentence 8 | qa/literature_register.csv L180 what_taken ("within 100 km") |
| pass | 11 | 8 | B_s06-09, sentence 8 | qa/literature_register.csv L180 what_taken ("11 to 28%", p. 229) |
| pass | 28 | 8 | B_s06-09, sentence 8 | qa/literature_register.csv L180 what_taken ("11 to 28%") |
| pass | 0.43 | 8 | B_s06-09, sentence 10 | register B047:1 (literal) |
| pass | 16 | 8 | B_s06-09, sentence 10 | register B047:1 (literal) |
| pass | 697 | 8 | B_s06-09, sentence 15 | ERRATA.md:39 (literal) |
| pass | 0.312 | 8 | B_s06-09, sentence 20 | analysis/method_tests_2025/simpson_food.csv:91 (literal) |
| pass | 0.107 | 8 | B_s06-09, sentence 20 | register B035:1 (literal) |
| pass | 0.854 | 8 | B_s06-09, sentence 20 | analysis/method_tests_2025/simpson_food.csv:80 (literal) |
| pass | 1991 | 8 | B_s06-09, sentence 20 | register B048:1 (literal) |
| pass | 92 | 8 | B_s06-09, sentence 20 | register B048:1 (literal) |
| pass | 18.9 | 9 | B_s06-09, sentence 6 | analysis/comparators_2025/rerun.csv:47 (rounded(x1)) |
| pass | 55.3 | 9 | B_s06-09, sentence 6 | analysis/comparators_2025/rerun.csv:50 (rounded(x1)) |
| pass | 62.9 | 9 | B_s06-09, sentence 6 | analysis/comparators_2025/rerun.csv:60 (rounded(x1)) |
| pass | 100 | 9 | B_s06-09, sentence 6 | analysis/method_tests_2025/ladder.csv:3 (literal) |
| pass | 2025 | 9 | B_s06-09, sentence 8 | results/releases.json:143 (literal) |
| pass | 2025 | 9 | B_s06-09, sentence 13 | results/releases.json:143 (literal) |
| pass | 2025 | 9 | B_s06-09, sentence 13 | results/releases.json:143 (literal) |
| pass | 2025 | 9 | B_s06-09, sentence 13 | results/releases.json:143 (literal) |
| pass | 2011 | 9 | B_s06-09, sentence 14 | LICENSE-DATA.md:7 (literal) |
| pass | 4.0 | 9 | B_s06-09, sentence 14 | LICENSE-DATA.md:5 (literal) |
| pass | 2,000 | 6 | B_s06-09, sentence 41 | analysis/sensitivity_2025/sobol_2025-fixed.csv:3 (rounded(x100)) |
| pass | 19 | 6 | B_s06-09, sentence 41 | analysis/sensitivity_2025/sobol_2025-fixed.csv:31 (rounded(x100)) |
| pass | 18 | 6 | B_s06-09, sentence 41 | qa/reports/B115_monte_carlo_widened.md:33 (literal) |
| pass | 31.1 | 6 | B_s06-09, sentence 41 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 49.2 | 6 | B_s06-09, sentence 41 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 5 | 6 | B_s06-09, sentence 41 | results/ranges_2025-fixed_wide.csv:1 (literal) |
| pass | 95 | 6 | B_s06-09, sentence 41 | results/ranges_2025-fixed_wide.csv:1 (literal) |
| pass | 1.58 | 6 | B_s06-09, sentence 41 | results/ranges_2025-fixed_wide.csv:2 (literal) |
| pass | 26.2 | 6 | B_s06-09, sentence 41 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 58.1 | 6 | B_s06-09, sentence 41 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 2.22 | 6 | B_s06-09, sentence 41 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1)) |
| pass | 13.3 | 6 | B_s06-09, sentence 41 | results/ranges_2025-fixed_wide.csv:4 (rounded(x1e-06)) |
| pass | 18.8 | 6 | B_s06-09, sentence 41 | results/ranges_2025-fixed_wide.csv:4 (rounded(x1e-06)) |
| pass | 39.0 | 6 | B_s06-09, sentence 43 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 41.5 | 6 | B_s06-09, sentence 43 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 97 | 6 | B_s06-09, sentence 44 | qa/reports/B115_monte_carlo_widened.md:53 (literal) |
| pass | 3 | 6 | B_s06-09, sentence 44 | analysis/sensitivity_2025/sobol_2025-fixed.csv:9 (literal) |
| pass | 32 | 6 | B_s06-09, sentence 45 | analysis/sensitivity_2025/sobol_2025-fixed.csv:17 (rounded(x100)) |
| pass | 27 | 6 | B_s06-09, sentence 45 | analysis/sensitivity_2025/sobol_2025-fixed.csv:4 (rounded(x100)) |
| pass | 24 | 6 | B_s06-09, sentence 45 | analysis/sensitivity_2025/sobol_2025-fixed.csv:4 (rounded(x100)) |
| pass | 1.4 | 6 | B_s06-09, sentence 46 | qa/reports/B115_monte_carlo_widened.md:20 (literal) |
| pass | 1.8 | 6 | B_s06-09, sentence 46 | qa/reports/B115_monte_carlo_widened.md:20 (literal) |
| pass | 1.2 | 6 | B_s06-09, sentence 46 | qa/reports/B115_monte_carlo_widened.md:31 (rounded(x1)) |
| pass | 2.2 | 6 | B_s06-09, sentence 46 | qa/reports/B115_monte_carlo_widened.md:97 (literal) |
| pass | 10.6 | 6 | B_s06-09, sentence 50 | analysis/waste_2025/ladder.csv:108 (rounded(x1e-06)) |
| pass | 1.58 | 6 | B_s06-09, sentence 54 | results/ranges_2025-fixed_wide.csv:2 (literal) |
| pass | 1.09 | 6 | B_s06-09, sentence 54 | analysis/method_tests_2025/design_choices.csv:5 (literal) |
| pass | 2.14 | 6 | B_s06-09, sentence 54 | analysis/method_tests_2025/design_choices.csv:7 (literal) |
| pass | 2.22 | 6 | B_s06-09, sentence 55 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1)) |
| pass | 31.1 | 6 | B_s06-09, Table 8 row 13 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 49.2 | 6 | B_s06-09, Table 8 row 13 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 1.58 | 6 | B_s06-09, Table 8 row 13 | results/ranges_2025-fixed_wide.csv:2 (literal) |
| pass | 25 | 7 | B_s06-09, sentence 5 | qa/reports/V28_section7_matrix.md:19 (literal) |
| pass | 28 | 7 | B_s06-09, sentence 5 | qa/reports/V28_section7_matrix.md:1 (literal) |
| pass | 65 | 7 | B_s06-09, sentence 19 | analysis/method_tests_2025/cross_method_local.csv:3 (rounded(x1)) |
| pass | 211 | 7 | B_s06-09, sentence 19 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 134 | 7 | B_s06-09, sentence 19 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 343 | 7 | B_s06-09, sentence 19 | analysis/method_tests_2025/cross_method_local.csv:5 (literal) |
| pass | 81.7 | 7 | B_s06-09, sentence 20 | analysis/pasture_2025/pairing_relaxed.csv:3 (rounded(x1)) |
| pass | 3.8 | 8 | B_s06-09, sentence 14 | qa/reports/B114_pairing_relaxed.md:58 (literal) |
| pass | 12 | 8 | B_s06-09, sentence 14 | qa/reports/B114_pairing_relaxed.md:34 (literal) |
| pass | 107.7 | 8 | B_s06-09, sentence 14 | analysis/pasture_2025/pairing_relaxed.csv:5 (rounded(x1)) |
| pass | 41.5 | 8 | B_s06-09, sentence 14 | analysis/pasture_2025/pairing_relaxed.csv:2 (rounded(x1)) |
| pass | 4.1 | 9 | B_s06-09, sentence 2 | analysis/method_tests_2025/harmonised_comparison_lines.csv:31 (rounded(x100)) |
| pass | 38.5 | 9 | B_s06-09, sentence 3 | analysis/method_tests_2025/harmonised_comparison_lines.csv:80 (rounded(x100)) |
| pass | 1.6 | 9 | B_s06-09, sentence 4 | analysis/method_tests_2025/cross_method_local.csv:3 (rounded(x1)) |
| pass | 5 | 9 | B_s06-09, sentence 4 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 1.58 | 9 | B_s06-09, sentence 7 | results/ranges_2025-fixed_wide.csv:2 (literal) |
| pass | 5 | 9 | B_s06-09, sentence 7 | results/ranges_2025-fixed_wide.csv:1 (literal) |
| pass | 95 | 9 | B_s06-09, sentence 7 | results/ranges_2025-fixed_wide.csv:1 (literal) |
| pass | 2.22 | 9 | B_s06-09, sentence 7 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1)) |
| pass | 70 | S2 | supplementary, sentence 7 | register B010:1 (literal) |
| pass | 70 | S2 | supplementary, sentence 7 | qa/literature_register.csv L003 what_taken (Nix 70 Mha) |
| pass | 10.2 | S2 | supplementary, sentence 37 | qa/literature_register.csv L083 what_taken ("could support 10.2 billion") |
| pass | 2025 | S3 | supplementary, sentence 1 | results/2025-fixed.csv:2 (literal) |
| pass | 2021 | S3 | supplementary, sentence 1 | analysis/method_tests_2025/harmonised_comparison.csv:8 (literal) |
| pass | 0.01 | S3 | supplementary, sentence 2 | analysis/method_tests_2025/harmonised_comparison.csv:2 (rounded(x0.001)) |
| pass | 363.5 | S3 | supplementary, sentence 2 | analysis/method_tests_2025/harmonised_comparison.csv:8 (literal) |
| pass | 26.20 | S3 | supplementary, sentence 2 | analysis/method_tests_2025/harmonised_comparison.csv:28 (literal) |
| pass | 404 | S3 | supplementary, sentence 3 | register B012:1 (literal) |
| pass | 10 | S3 | supplementary, sentence 3 | register B012:1 (literal) |
| pass | 306 | S3 | supplementary, sentence 3 | register B012:1 (literal) |
| pass | 10 | S3 | supplementary, sentence 3 | register B012:1 (literal) |
| pass | 404 | S3 | supplementary, sentence 3 | analysis/method_tests_2025/henry_godden.py:9 (404 x 10^15 J) |
| pass | 1990 | S3 | supplementary, sentence 3 | register B012,B013:1 (literal) |
| pass | 91 | S3 | supplementary, sentence 3 | register B012,B013:1 (literal) |
| pass | 0.1760 | S3 | supplementary, sentence 4 | register B014:1 (literal) |
| pass | 0.2041 | S3 | supplementary, sentence 4 | register B014:1 (literal) |
| pass | 0.1760 | S3 | supplementary, sentence 4 | analysis/method_tests_2025/henry_godden.py:55 (FE, FP = 0.1760, 0.2041) |
| pass | 0.2041 | S3 | supplementary, sentence 4 | analysis/method_tests_2025/henry_godden.py:55 |
| pass | 70 | S3 | supplementary, sentence 5 | register B013,B010:1 (literal) |
| pass | 45.7 | S3 | supplementary, sentence 5 | register B013:1 (literal) |
| pass | 70 | S3 | supplementary, sentence 5 | analysis/method_tests_2025/henry_godden.py:9 (x 70/45.7) |
| pass | 45.7 | S3 | supplementary, sentence 5 | analysis/method_tests_2025/henry_godden.py:9 (x 70/45.7) |
| pass | 138 | S3 | supplementary, sentence 8 | analysis/method_tests_2025/henry_godden_summary.csv:22 (rounded(x1)) |
| pass | 134 | S3 | supplementary, sentence 8 | analysis/method_tests_2025/henry_godden_summary.csv:22 (rounded(x1)) |
| pass | 161 | S3 | supplementary, sentence 8 | analysis/method_tests_2025/henry_godden_summary.csv:23 (rounded(x1)) |
| pass | 156 | S3 | supplementary, sentence 8 | analysis/method_tests_2025/henry_godden_summary.csv:23 (literal) |
| pass | 70 | S3 | supplementary, sentence 8 | analysis/method_tests_2025/henry_godden_summary.csv:2 (literal) |
| pass | 59.95 | S3 | supplementary, sentence 8 | analysis/method_tests_2025/henry_godden_summary.csv:23 (literal) |
| pass | 211 | S3 | supplementary, sentence 8 | analysis/method_tests_2025/henry_godden_summary.csv:24 (rounded(x1)) |
| pass | 205 | S3 | supplementary, sentence 8 | analysis/method_tests_2025/henry_godden_summary.csv:24 (rounded(x1)) |
| pass | 45.7 | S3 | supplementary, sentence 8 | analysis/method_tests_2025/henry_godden_summary.csv:2 (literal) |
| pass | 1990 | S3 | supplementary, sentence 8 | analysis/method_tests_2025/henry_godden_summary.csv:2 (literal) |
| pass | 91 | S3 | supplementary, sentence 8 | analysis/method_tests_2025/henry_godden_summary.csv:2 (literal) |
| pass | 2025 | S3 | supplementary, sentence 9 | register B027:1 (literal) |
| pass | 28.3 | S3 | supplementary, sentence 9 | register B027:1 (literal) |
| pass | 1990 | S3 | supplementary, sentence 9 | register B027:1 (literal) |
| pass | 91 | S3 | supplementary, sentence 9 | register B027:1 (literal) |
| pass | 31 | S3 | supplementary, sentence 10 | register B022:1 (literal) |
| pass | 15.6 | S3 | supplementary, sentence 11 | analysis/method_tests_2025/henry_godden_summary.csv:25 (literal) |
| pass | 8.8 | S3 | supplementary, sentence 11 | analysis/method_tests_2025/henry_godden_summary.csv:25 (literal) |
| pass | 8.8 | S3 | supplementary, sentence 11 | analysis/method_tests_2025/henry_godden_summary.csv:25 (literal) |
| pass | 243 | S3 | supplementary, sentence 11 | analysis/method_tests_2025/henry_godden_summary.csv:25 (literal) |
| pass | 1991 | S3 | supplementary, sentence 12 | register B048,B032:1 (literal) |
| pass | 92 | S3 | supplementary, sentence 12 | register B048,B032:1 (literal) |
| pass | 1990 | S3 | supplementary, sentence 13 | analysis/method_tests_2025/simpson_food.csv:83 (literal) |
| pass | 92 | S3 | supplementary, sentence 13 | analysis/method_tests_2025/simpson_food.csv:2 (literal) |
| pass | 34 | S3 | supplementary, sentence 15 | analysis/method_tests_2025/simpson_food.csv:88 (rounded(x1)) |
| pass | 1 | S3 | supplementary, sentence 17 | analysis/method_tests_2025/simpson_food.csv:17 (literal) |
| pass | 1.737 | S3 | supplementary, sentence 17 | analysis/method_tests_2025/simpson_food.csv:17 (literal) |
| pass | 2 | S3 | supplementary, sentence 17 | analysis/method_tests_2025/simpson_food.csv:48 (literal) |
| pass | 2.385 | S3 | supplementary, sentence 17 | analysis/method_tests_2025/simpson_food.csv:51 (literal) |
| pass | 36 | S3 | supplementary, sentence 17 | analysis/method_tests_2025/simpson_food.csv:85 (rounded(x1)) |
| pass | 0.074 | S3 | supplementary, sentence 19 | analysis/method_tests_2025/simpson_food.csv:63 (literal) |
| pass | 0.142 | S3 | supplementary, sentence 19 | analysis/method_tests_2025/simpson_food.csv:48 (literal) |
| pass | 0.312 | S3 | supplementary, sentence 19 | analysis/method_tests_2025/simpson_food.csv:91 (literal) |
| pass | 2010 | S3 | supplementary, sentence 21 | register B061:1 (literal) |
| pass | 66 | S3 | supplementary, sentence 22 | register B061:1 (literal) |
| pass | 90 | S3 | supplementary, sentence 22 | register B061:1 (literal) |
| pass | 2 | S3 | supplementary, sentence 26 | analysis/method_tests_2025/cross_method.csv:3 (literal) |
| pass | 61 | S3 | supplementary, sentence 27 | analysis/method_tests_2025/cassidy.csv:2 (literal) |
| pass | 59 | S3 | supplementary, sentence 27 | analysis/method_tests_2025/published_values.csv:15 (literal) |
| pass | 4 | S3 | supplementary, sentence 27 | analysis/method_tests_2025/cassidy.csv:7 (literal) |
| pass | 41 | S3 | supplementary, sentence 28 | analysis/method_tests_2025/cassidy.csv:3 (literal) |
| pass | 67 | S3 | supplementary, sentence 28 | register B073:1 (literal) |
| pass | 22 | S3 | supplementary, sentence 29 | register B079:1 (literal) |
| pass | 1,061 | S3 | supplementary, sentence 29 | analysis/method_tests_2025/cassidy.csv:2 (literal) |
| pass | 41 | S3 | supplementary, sentence 29 | analysis/method_tests_2025/cassidy.csv:3 (literal) |
| pass | 947 | S3 | supplementary, sentence 29 | register B079,B077:1 (literal) |
| pass | 4 | S3 | supplementary, sentence 29 | analysis/method_tests_2025/cassidy.csv:7 (literal) |
| pass | 5 | S3 | supplementary, sentence 30 | register B258:1 (literal) |
| pass | 8 | S3 | supplementary, sentence 30 | analysis/method_tests_2025/cassidy.csv:4 (literal) |
| pass | 5.8 | S3 | supplementary, sentence 33 | analysis/method_tests_2025/cassidy_matched.csv:3 (rounded(x1)) |
| pass | 31.65 | S3 | supplementary, sentence 33 | analysis/method_tests_2025/simpson_food.csv:43 (literal) |
| pass | 183 | S3 | supplementary, sentence 33 | register B084:1 (literal) |
| pass | 190 | S3 | supplementary, sentence 33 | analysis/method_tests_2025/cross_method.csv:5 (literal) |
| pass | 5.8 | S3 | supplementary, sentence 33 | analysis/method_tests_2025/cassidy_matched.csv:3 (rounded(x1)) |
| pass | 3,525 | S3 | supplementary, sentence 34 | analysis/method_tests_2025/harmonised_comparison.csv:2 (literal) |
| pass | 2,700 | S3 | supplementary, sentence 34 | register B087:1 (literal) |
| pass | 0.766 | S3 | supplementary, sentence 34 | analysis/method_tests_2025/harmonised_comparison.csv:17 (literal) |
| pass | 1997 | S3 | supplementary, sentence 35 | register B140:1 (literal) |
| pass | 98 | S3 | supplementary, sentence 35 | register B140:1 (literal) |
| pass | 31.578 | S3 | supplementary, sentence 35 | register B140:1 (literal) |
| pass | 3.514 | S3 | supplementary, sentence 35 | register B140:1 (literal) |
| pass | 0.223 | S3 | supplementary, sentence 35 | register B140:1 (literal) |
| pass | 1997 | S3 | supplementary, sentence 37 | analysis/method_tests_2025/foran_poldy_balance.csv:9 (literal) |
| pass | 98 | S3 | supplementary, sentence 37 | analysis/method_tests_2025/foran_poldy_balance.csv:9 (literal) |
| pass | 31.95 | S3 | supplementary, sentence 37 | analysis/method_tests_2025/foran_poldy_balance.csv:9 (literal) |
| pass | 3.47 | S3 | supplementary, sentence 37 | analysis/method_tests_2025/foran_poldy_balance.csv:9 (literal) |
| pass | 1.2 | S3 | supplementary, sentence 37 | analysis/method_tests_2025/gap_attribution.csv:11 (rounded(x1)) |
| pass | 1.2 | S3 | supplementary, sentence 37 | analysis/method_tests_2025/gap_attribution.csv:11 (rounded(x1)) |
| pass | 2021 | S3 | supplementary, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:3 (literal) |
| pass | 23 | S3 | supplementary, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:3 (literal) |
| pass | 52.6 | S3 | supplementary, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:12 (rounded(x1)) |
| pass | 4.66 | S3 | supplementary, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:12 (literal) |
| pass | 0.29 | S3 | supplementary, sentence 38 | analysis/method_tests_2025/foran_poldy_balance.csv:12 (literal) |
| pass | 0.24 | S3 | supplementary, sentence 40 | register B121:1 (literal) |
| pass | 5.8 | S3 | supplementary, sentence 42 | analysis/method_tests_2025/fearnside_failure_curve.csv:3 (literal) |
| pass | 6.1 | S3 | supplementary, sentence 42 | analysis/method_tests_2025/fearnside_failure_curve.csv:3 (literal) |
| pass | 1.5 | S3 | supplementary, sentence 42 | analysis/method_tests_2025/fearnside_failure_curve.csv:5 (literal) |
| pass | 2 | S3 | supplementary, sentence 42 | analysis/method_tests_2025/fearnside_failure_curve.csv:1 (literal) |
| pass | 2025 | S3 | supplementary, sentence 42 | analysis/method_tests_2025/fearnside_failure_curve.csv:3 (literal) |
| pass | 1.5 | S3 | supplementary, sentence 42 | analysis/method_tests_2025/fearnside_failure_curve.csv:5 (literal) |
| pass | 103.6 | S4 | supplementary, sentence 1 | analysis/comparators_2025/diet_land.csv:3 (literal) |
| pass | 2.5 | S4 | supplementary, sentence 2 | analysis/comparators_2025/diet_land.csv:4 (literal) |
| pass | 118.0 | S4 | supplementary, sentence 2 | register B216:1 (literal) |
| pass | 112.4 | S4 | supplementary, sentence 2 | register B216:1 (literal) |
| pass | 12 | S4 | supplementary, Table S2 row 1 | analysis/comparators_2025/diet_land.csv:2 (literal) |
| pass | 57.8 | S4 | supplementary, Table S2 row 1 | analysis/comparators_2025/diet_land.csv:2 (literal) |
| pass | 0 | S4 | supplementary, Table S2 row 2 | analysis/comparators_2025/diet_land.csv:2 (literal) |
| pass | 2.5 | S4 | supplementary, Table S2 row 3 | analysis/comparators_2025/diet_land.csv:4 (literal) |
| pass | 5 | S4 | supplementary, Table S2 row 4 | analysis/comparators_2025/diet_land.csv:2 (literal) |
| pass | 7.5 | S4 | supplementary, Table S2 row 5 | analysis/comparators_2025/diet_land.csv:6 (literal) |
| pass | 10 | S4 | supplementary, Table S2 row 6 | analysis/comparators_2025/diet_land.csv:7 (literal) |
| pass | 15 | S4 | supplementary, Table S2 row 7 | analysis/comparators_2025/diet_land.csv:9 (literal) |
| pass | 2 | S6 | supplementary, sentence 2 | analysis/method_tests_2025/design_choices.csv:2 (literal) |
| pass | 8 | S6 | supplementary, sentence 2 | register B243:1 (literal) |
| pass | 1 | S6 | supplementary, sentence 2 | analysis/method_tests_2025/design_choices.csv:2 (literal) |
| pass | 9 | S6 | supplementary, sentence 2 | register B243:1 (literal) |
| pass | 12 | S6 | supplementary, sentence 2 | analysis/method_tests_2025/design_choices.csv:3 (literal) |
| pass | 1.2 | S6 | supplementary, sentence 3 | analysis/method_tests_2025/design_choices.csv:4 (rounded(x1)) |
| pass | 1.33 | S6 | supplementary, sentence 4 | analysis/method_tests_2025/design_choices.csv:3 (literal) |
| pass | 1.17 | S6 | supplementary, sentence 4 | analysis/method_tests_2025/design_choices.csv:4 (literal) |
| pass | 1.09 | S6 | supplementary, sentence 4 | analysis/method_tests_2025/design_choices.csv:5 (literal) |
| pass | 2 | S6 | supplementary, Table S4 row 2 | analysis/method_tests_2025/design_choices.csv:2 (literal) |
| pass | 3 | S6 | supplementary, Table S4 row 3 | analysis/method_tests_2025/design_choices.csv:3 (literal) |
| pass | 4 | S6 | supplementary, Table S4 row 4 | analysis/method_tests_2025/design_choices.csv:6 (literal) |
| pass | 5 | S6 | supplementary, Table S4 row 5 | analysis/method_tests_2025/design_choices.csv:2 (literal) |
| pass | 6 | S6 | supplementary, Table S4 row 6 | analysis/method_tests_2025/design_choices.csv:13 (literal) |
| pass | 7 | S6 | supplementary, Table S4 row 7 | analysis/method_tests_2025/design_choices.csv:8 (literal) |
| pass | 8 | S6 | supplementary, Table S4 row 8 | register B243:1 (literal) |
| pass | 9.0 | S2 | supplementary, sentence 13 | register B337:1 (literal) |
| pass | 14.0 | S2 | supplementary, sentence 13 | register B338:1 (literal) |
| pass | 31.65 | S3 | supplementary, sentence 33 | analysis/method_tests_2025/simpson_food.csv:43 (literal) |
| pass | 183 | S3 | supplementary, sentence 33 | register B084:1 (literal) |
| pass | 190 | S3 | supplementary, sentence 33 | analysis/method_tests_2025/cross_method.csv:5 (literal) |
| pass | 11 | S8 | supplementary, sentence 2 | register B166:1 (literal) |
| pass | 26 | S8 | supplementary, sentence 2 | register B166:1 (literal) |
| pass | 67 | S8 | supplementary, sentence 2 | register B166:1 (literal) |
| pass | 78 | S8 | supplementary, sentence 2 | register B166:1 (literal) |
| pass | 2.61 | S8 | supplementary, sentence 4 | register B050:1 (literal) |
| pass | 5.96 | S8 | supplementary, sentence 4 | register B050:1 (literal) |
| pass | 44 | S8 | supplementary, sentence 4 | register B050:1 (literal) |
| pass | 8.1 | S8 | supplementary, sentence 5 | register B051:1 (literal) |
| pass | 13.6 | S8 | supplementary, sentence 5 | register B051:1 (literal) |
| pass | 1994 | S8 | supplementary, sentence 5 | register B051:1 (literal) |
| pass | 95 | S8 | supplementary, sentence 5 | register B051:1 (literal) |
| pass | 2030 | S8 | supplementary, sentence 8 | qa/literature_register.csv L230 what_taken ("halving ... by 2030") |
| pass | 7.3 | S8 | supplementary, sentence 9 | qa/literature_register.csv L231 what_taken ("Total 7.3 Mt food waste 2016/17") |
| pass | 7.6 | S8 | supplementary, sentence 10 | qa/literature_register.csv L242 what_taken ("about 7.6 million tonnes") |
| pass | 2.03 | S8 | supplementary, sentence 12 | qa/literature_register.csv L040 what_taken ("2.03 Mha in three land classes") |
| pass | 103.3 | S4 | supplementary, sentence 3 | analysis/comparators_2025/diet_land.csv:5 (literal) |
| pass | 5 | S4 | supplementary, sentence 3 | analysis/comparators_2025/diet_land.csv:2 (literal) |
| pass | 76.8 | S4 | supplementary, sentence 3 | analysis/paper_a/measures.csv:18 (literal) |
| pass | 0 | S8 | supplementary, sentence 14 | qa/literature_register.csv L081 notes ("0-2% (p 472)") |
| pass | 2 | S8 | supplementary, sentence 14 | qa/literature_register.csv L081 notes ("0-2% (p 472)") |
| pass | 16 | S8 | supplementary, sentence 20 | qa/literature_register.csv L105 notes (16% on PDF pp. 2 and 4) |
| pass | 1.718 | S3 | supplementary, sentence 16 | analysis/method_tests_2025/fidelity.csv:6 (rounded(x1)) |
| pass | 1.758 | S3 | supplementary, sentence 16 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 2.3 | S3 | supplementary, sentence 16 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 1.737 | S3 | supplementary, sentence 17 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 1.2 | S3 | supplementary, sentence 17 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 0.116 | S3 | supplementary, sentence 18 | analysis/method_tests_2025/fidelity.csv:7 (rounded(x1)) |
| pass | 3 | S3 | supplementary, sentence 18 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 21.7 | S3 | supplementary, sentence 18 | qa/reports/V42_check_B116.md:33 (literal) |
| pass | 0.098 | S3 | supplementary, sentence 18 | analysis/method_tests_2025/fidelity.csv:7 (rounded(x1)) |
| pass | 0.094 | S3 | supplementary, sentence 18 | analysis/method_tests_2025/fidelity.csv:7 (literal) |
| pass | 0.095 | S3 | supplementary, sentence 18 | analysis/method_tests_2025/fidelity.csv:7 (literal) |
| pass | 10.3 | S3 | supplementary, sentence 20 | analysis/method_tests_2025/fidelity.csv:9 (literal) |
| pass | 1 | S3 | supplementary, sentence 20 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 11.9 | S3 | supplementary, sentence 20 | analysis/method_tests_2025/fidelity.csv:9 (literal) |
| pass | 3 | S3 | supplementary, sentence 20 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 0.014 | S3 | supplementary, sentence 20 | analysis/method_tests_2025/fidelity.csv:10 (rounded(x1)) |
| pass | 0.032 | S3 | supplementary, sentence 20 | analysis/method_tests_2025/fidelity.csv:10 (literal) |
| pass | 0.127 | S3 | supplementary, sentence 20 | analysis/method_tests_2025/fidelity.csv:11 (literal) |
| pass | 0.854 | S3 | supplementary, sentence 20 | analysis/method_tests_2025/fidelity.csv:11 (literal) |
| pass | 2.2 | S3 | supplementary, sentence 24 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 0.8 | S3 | supplementary, sentence 24 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 3.3 | S3 | supplementary, sentence 24 | analysis/method_tests_2025/fidelity.csv:14 (literal) |
| pass | 4.6 | S3 | supplementary, sentence 24 | analysis/method_tests_2025/fidelity.csv:15 (literal) |
| pass | 7.2 | S3 | supplementary, sentence 24 | analysis/method_tests_2025/fidelity.csv:16 (literal) |
| pass | 30.2 | S3 | supplementary, sentence 24 | analysis/method_tests_2025/fidelity.csv:17 (literal) |
| pass | 2.8 | S3 | supplementary, sentence 24 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 8.4 | S3 | supplementary, sentence 24 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 3.4 | S3 | supplementary, sentence 24 | analysis/method_tests_2025/fidelity.csv:14 (literal) |
| pass | 3.0 | S3 | supplementary, sentence 24 | analysis/method_tests_2025/fidelity.csv:15 (literal) |
| pass | 4.1 | S3 | supplementary, sentence 24 | analysis/method_tests_2025/fidelity.csv:16 (literal) |
| pass | 3,364 | S3 | supplementary, sentence 25 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 3,182 | S3 | supplementary, sentence 25 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 118.88 | S3 | supplementary, sentence 25 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 6.0 | S3 | supplementary, sentence 25 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 5.7 | S3 | supplementary, sentence 25 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 94.7 | S3 | supplementary, sentence 25 | qa/reports/V42_check_B116.md:28 (literal) |
| pass | 121.59 | S3 | supplementary, sentence 25 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 8.4 | S3 | supplementary, sentence 25 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 33 | S3 | supplementary, sentence 27 | analysis/method_tests_2025/fidelity.csv:23 (literal) |
| pass | 34 | S3 | supplementary, sentence 27 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 32 | S3 | supplementary, sentence 28 | analysis/method_tests_2025/fidelity.csv:10 (rounded(x1000)) |
| pass | 6 | S3 | supplementary, sentence 28 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 22 | S3 | supplementary, sentence 29 | analysis/method_tests_2025/fidelity.csv:5 (literal) |
| pass | 42 | S3 | supplementary, sentence 29 | analysis/method_tests_2025/fidelity.csv:11 (literal) |
| pass | 5 | S3 | supplementary, sentence 29 | analysis/method_tests_2025/fidelity.csv:2 (literal) |
| pass | 25 | S3 | supplementary, sentence 29 | analysis/method_tests_2025/fidelity.csv:25 (literal) |
| pass | 5 | S3 | supplementary, sentence 45 | analysis/method_tests_2025/gap_attribution_readable.csv:1 (literal) |
| pass | 0.8 | S3 | supplementary, sentence 46 | analysis/method_tests_2025/gap_attribution_readable.csv:18 (rounded(x1)) |
| pass | 2.2 | S3 | supplementary, sentence 46 | analysis/method_tests_2025/gap_attribution_readable.csv:9 (rounded(x0.01)) |
| pass | 3.3 | S3 | supplementary, sentence 46 | analysis/method_tests_2025/gap_attribution_readable.csv:96 (literal) |
| pass | 4.6 | S3 | supplementary, sentence 46 | analysis/method_tests_2025/gap_attribution_readable.csv:21 (rounded(x1)) |
| pass | 2.3 | S3 | supplementary, sentence 46 | analysis/method_tests_2025/gap_attribution_readable.csv:83 (literal) |
| pass | 1.2 | S3 | supplementary, sentence 46 | analysis/method_tests_2025/gap_attribution_readable.csv:11 (rounded(x1)) |
| pass | 7.2 | S3 | supplementary, sentence 47 | analysis/method_tests_2025/gap_attribution_readable.csv:22 (rounded(x1)) |
| pass | 22 | S3 | supplementary, sentence 47 | analysis/method_tests_2025/gap_attribution_readable.csv:86 (literal) |
| pass | 37 | S3 | supplementary, sentence 47 | analysis/method_tests_2025/gap_attribution_readable.csv:113 (rounded(x100)) |
| pass | 0.92 | S3 | supplementary, sentence 48 | analysis/method_tests_2025/gap_attribution_readable.csv:19 (literal) |
| pass | -0.38 | S3 | supplementary, sentence 49 | analysis/method_tests_2025/gap_attribution_readable.csv:19 (literal) |
| pass | 0.6 | S3 | supplementary, sentence 49 | analysis/method_tests_2025/gap_attribution_readable.csv:19 (literal) |
| pass | 5.76 | S3 | supplementary, sentence 49 | analysis/method_tests_2025/gap_attribution_readable.csv:24 (literal) |
| pass | -9.2 | S3 | supplementary, sentence 49 | analysis/method_tests_2025/gap_attribution_readable.csv:24 (literal) |
| pass | 8.47 | S3 | supplementary, sentence 49 | analysis/method_tests_2025/gap_attribution_readable.csv:69 (literal) |
| pass | -13.2 | S3 | supplementary, sentence 49 | analysis/method_tests_2025/gap_attribution_readable.csv:69 (literal) |
| pass | 0.040 | S3 | supplementary, sentence 51 | analysis/method_tests_2025/gap_attribution_readable.csv:30 (rounded(x1)) |
| pass | 0.060 | S3 | supplementary, sentence 51 | analysis/method_tests_2025/gap_attribution_readable.csv:31 (rounded(x1)) |
| pass | 0.071 | S3 | supplementary, sentence 51 | analysis/method_tests_2025/gap_attribution_readable.csv:73 (rounded(x0.001)) |
| pass | 57 | S3 | supplementary, sentence 51 | analysis/method_tests_2025/README.md:535 ("57% of 1991-92 milk consumption") |
| pass | 26.20 | S3 | supplementary, sentence 54 | analysis/method_tests_2025/bases.csv:11 (literal) |
| pass | 2021 | S3 | supplementary, sentence 54 | analysis/method_tests_2025/bases.csv:2 (literal) |
| pass | 23 | S3 | supplementary, sentence 54 | analysis/method_tests_2025/bases.csv:2 (literal) |
| pass | 26.08 | S3 | supplementary, sentence 54 | analysis/method_tests_2025/bases.csv:10 (literal) |
| pass | 15.6 | S3 | supplementary, sentence 55 | analysis/method_tests_2025/bases.csv:2 (literal) |
| pass | 3,718 | S3 | supplementary, sentence 55 | analysis/method_tests_2025/bases.csv:2 (literal) |
| pass | 2,700 | S3 | supplementary, sentence 55 | analysis/method_tests_2025/bases.csv:8 (literal) |
| pass | 11.3 | S3 | supplementary, sentence 55 | analysis/method_tests_2025/bases.csv:8 (literal) |
| pass | 3,525 | S3 | supplementary, sentence 55 | analysis/method_tests_2025/bases.csv:3 (literal) |
| pass | 14.8 | S3 | supplementary, sentence 55 | analysis/method_tests_2025/bases.csv:3 (literal) |
| pass | 8.0 | S3 | supplementary, sentence 55 | analysis/method_tests_2025/bases.csv:12 (literal) |
| pass | 363.52 | S3 | supplementary, sentence 57 | analysis/method_tests_2025/bases.csv:3 (literal) |
| pass | 2 | S3 | supplementary, sentence 58 | analysis/method_tests_2025/fidelity.csv:2 (literal) |
| pass | 10 | S3 | supplementary, sentence 58 | analysis/method_tests_2025/fidelity.csv:9 (literal) |
| pass | 10 | S3 | supplementary, sentence 58 | analysis/method_tests_2025/fidelity.csv:9 (literal) |
| pass | 21.7 | S3 | supplementary, sentence 62 | qa/reports/V42_check_B116.md:33 (literal) |
| pass | 0.715 | S3 | supplementary, sentence 64 | qa/reports/V42_check_B116.md:89 (literal) |
| pass | 20 | S3 | supplementary, sentence 65 | analysis/method_tests_2025/intake_variant.csv:2 (literal) |
| pass | 37 | S3 | supplementary, sentence 65 | analysis/method_tests_2025/intake_variant.csv:2 (literal) |
| pass | 0.82 | S3 | supplementary, sentence 67 | analysis/method_tests_2025/intake_variant.csv:2 (rounded(x1)) |
| pass | 0.86 | S3 | supplementary, sentence 67 | analysis/method_tests_2025/intake_variant.csv:2 (rounded(x1)) |
| pass | 0.92 | S3 | supplementary, sentence 67 | analysis/method_tests_2025/intake_variant.csv:16 (rounded(x1)) |
| pass | 55.3 | S3 | supplementary, sentence 68 | analysis/method_tests_2025/ladder.csv:8 (literal) |
| pass | -4 | S3 | supplementary, sentence 70 | qa/reports/B113_harmonised_both_lines.md:15 (literal) |
| pass | 61 | S3 | supplementary, sentence 70 | analysis/method_tests_2025/harmonised_comparison_lines.csv:42 (rounded(x100)) |
| pass | 0 | S3 | supplementary, sentence 70 | analysis/method_tests_2025/harmonised_comparison_lines.csv:26 (literal) |
| pass | 68 | S3 | supplementary, sentence 70 | analysis/method_tests_2025/harmonised_comparison_lines.csv:30 (rounded(x100)) |
| pass | 26 | S3 | supplementary, sentence 70 | analysis/method_tests_2025/harmonised_comparison_lines.csv:29 (rounded(x100)) |
| pass | 8 | S3 | supplementary, sentence 70 | qa/reports/B113_harmonised_both_lines.md:18 (literal) |
| pass | -15 | S3 | supplementary, sentence 70 | analysis/method_tests_2025/harmonised_comparison_lines.csv:30 (rounded(x100)) |
| pass | 0.5 | S3 | supplementary, sentence 74 | analysis/pasture_2025/pairing_relaxed.csv:3 (rounded(x0.01)) |
| pass | 0.6 | S3 | supplementary, sentence 74 | analysis/pasture_2025/pairing_relaxed.csv:3 (rounded(x0.01)) |
| pass | 4.2 | S3 | supplementary, sentence 74 | qa/reports/B114_pairing_relaxed.md:74 (literal) |
| pass | 2,000 | S5 | supplementary, sentence 7 | analysis/sensitivity_2025/sobol_2025-fixed.csv:3 (rounded(x100)) |
| pass | 19 | S5 | supplementary, sentence 7 | analysis/sensitivity_2025/sobol_2025-fixed.csv:31 (rounded(x100)) |
| pass | 42,000 | S5 | supplementary, sentence 7 | analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv:884 (rounded(x1000)) |
| pass | 18 | S5 | supplementary, sentence 7 | qa/reports/B115_monte_carlo_widened.md:33 (literal) |
| pass | 19 | S5 | supplementary, sentence 7 | qa/reports/B115_monte_carlo_widened.md:10 (literal) |
| pass | 1,000 | S5 | supplementary, sentence 8 | analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md:7 (literal) |
| pass | 13 | S5 | supplementary, sentence 8 | analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md:7 (literal) |
| pass | 1,000 | S5 | supplementary, sentence 9 | analysis/sensitivity_2025/README.md:293 ("1,000 bootstrap resamples") |
| pass | 97 | S5 | supplementary, sentence 10 | qa/reports/B115_monte_carlo_widened.md:53 (literal) |
| pass | 3 | S5 | supplementary, sentence 10 | analysis/sensitivity_2025/sobol_2025-fixed.csv:9 (literal) |
| pass | 0.115 | S5 | supplementary, sentence 12 | analysis/sensitivity_2025/README.md:175 (literal) |
| pass | 0.528 | S5 | supplementary, sentence 12 | analysis/sensitivity_2025/README.md:175 (literal) |
| pass | 50 | S5 | supplementary, sentence 12 | qa/reports/V41_check_B115.md:95 (literal) |
| pass | 50 | S5 | supplementary, sentence 12 | qa/reports/V41_check_B115.md:95 (literal) |
| pass | 1.2 | S5 | supplementary, sentence 14 | qa/reports/B115_monte_carlo_widened.md:31 (rounded(x1)) |
| pass | 2.2 | S5 | supplementary, sentence 14 | qa/reports/B115_monte_carlo_widened.md:97 (literal) |
| pass | 39.0 | S5 | supplementary, sentence 15 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 41.5 | S5 | supplementary, sentence 15 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 29.8 | S5 | supplementary, sentence 16 | qa/reports/B115_monte_carlo_widened.md:56 (literal) |
| pass | 43.1 | S5 | supplementary, sentence 16 | qa/reports/B115_monte_carlo_widened.md:56 (literal) |
| pass | 1.45 | S5 | supplementary, sentence 16 | qa/reports/B115_monte_carlo_widened.md:56 (literal) |
| pass | 13.0 | S5 | supplementary, sentence 16 | qa/reports/B115_monte_carlo_widened.md:12 (rounded(x1)) |
| pass | 16.2 | S5 | supplementary, sentence 16 | qa/reports/V41_check_B115.md:37 (literal) |
| pass | 1.24 | S5 | supplementary, sentence 16 | qa/reports/V41_check_B115.md:37 (literal) |
| pass | 35.6 | S5 | supplementary, sentence 16 | qa/reports/V41_check_B115.md:37 (literal) |
| pass | 51.2 | S5 | supplementary, sentence 16 | qa/reports/V41_check_B115.md:37 (literal) |
| pass | 1.44 | S5 | supplementary, sentence 16 | qa/reports/V41_check_B115.md:37 (literal) |
| pass | 15.3 | S5 | supplementary, sentence 16 | qa/reports/V41_check_B115.md:37 (literal) |
| pass | 19.1 | S5 | supplementary, sentence 16 | qa/reports/V41_check_B115.md:37 (literal) |
| pass | 1.25 | S5 | supplementary, sentence 16 | qa/reports/V41_check_B115.md:37 (literal) |
| pass | 23 | S5 | supplementary, sentence 5 | analysis/sensitivity_2025/README.md:19 (literal) |
| pass | 25 | S7 | supplementary, sentence 16 | qa/reports/V28_section7_matrix.md:19 (literal) |
| pass | 28 | S7 | supplementary, sentence 16 | qa/reports/V28_section7_matrix.md:1 (literal) |
| pass | 24 | S7 | supplementary, sentence 15 | qa/reports/V28_section7_matrix.md:19 (literal) |
| pass | 28 | S7 | supplementary, sentence 15 | qa/reports/V28_section7_matrix.md:1 (literal) |
| pass | 7 | S7 | supplementary, sentence 16 | qa/reports/V28_section7_matrix.md:1 (literal) |
| pass | 7 | S7 | supplementary, sentence 16 | qa/reports/V28_section7_matrix.md:1 (literal) |
| pass | 1 | S7 | supplementary, sentence 16 | qa/reports/V28_section7_matrix.md:5 (literal) |
| pass | 4 | S7 | supplementary, sentence 16 | qa/reports/V28_section7_matrix.md:13 (literal) |
| pass | 5 | S7 | supplementary, sentence 16 | qa/reports/V28_section7_matrix.md:3 (literal) |
| pass | 7 | S7 | supplementary, sentence 16 | qa/reports/V28_section7_matrix.md:1 (literal) |
| pass | 2 | S7 | supplementary, sentence 16 | qa/reports/V28_section7_matrix.md:11 (literal) |
| pass | 6 | S7 | supplementary, sentence 16 | qa/reports/V28_section7_matrix.md:23 (literal) |
| pass | 7 | S7 | supplementary, sentence 16 | qa/reports/V28_section7_matrix.md:1 (literal) |
| pass | 3 | S7 | supplementary, sentence 16 | qa/reports/V28_section7_matrix.md:12 (literal) |
| pass | 2011 | S3 | supplementary, Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv:2 (literal) |
| pass | 34.37 | S3 | supplementary, Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv:18 (literal) |
| pass | 35.13 | S3 | supplementary, Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv:18 (literal) |
| pass | 0.76 | S3 | supplementary, Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv:18 (literal) |
| pass | 2011 | S3 | supplementary, Table S1 row 2 | analysis/method_tests_2025/gap_attribution_readable.csv:2 (literal) |
| pass | 113.12 | S3 | supplementary, Table S1 row 2 | analysis/method_tests_2025/gap_attribution_readable.csv:19 (literal) |
| pass | 112.2 | S3 | supplementary, Table S1 row 2 | analysis/method_tests_2025/gap_attribution_readable.csv:19 (literal) |
| pass | -0.92 | S3 | supplementary, Table S1 row 2 | analysis/method_tests_2025/gap_attribution_readable.csv:19 (literal) |
| pass | 2011 | S3 | supplementary, Table S1 row 3 | analysis/method_tests_2025/gap_attribution_readable.csv:2 (literal) |
| pass | 94.55 | S3 | supplementary, Table S1 row 3 | analysis/method_tests_2025/gap_attribution_readable.csv:20 (literal) |
| pass | 97.73 | S3 | supplementary, Table S1 row 3 | analysis/method_tests_2025/gap_attribution_readable.csv:20 (literal) |
| pass | 3.18 | S3 | supplementary, Table S1 row 3 | analysis/method_tests_2025/gap_attribution_readable.csv:20 (literal) |
| pass | 2011 | S3 | supplementary, Table S1 row 4 | analysis/method_tests_2025/gap_attribution_readable.csv:2 (literal) |
| pass | 109.63 | S3 | supplementary, Table S1 row 4 | analysis/method_tests_2025/gap_attribution_readable.csv:21 (literal) |
| pass | 114.88 | S3 | supplementary, Table S1 row 4 | analysis/method_tests_2025/gap_attribution_readable.csv:21 (literal) |
| pass | 5.25 | S3 | supplementary, Table S1 row 4 | analysis/method_tests_2025/gap_attribution_readable.csv:21 (literal) |
| pass | 2011 | S3 | supplementary, Table S1 row 5 | analysis/method_tests_2025/gap_attribution_readable.csv:2 (literal) |
| pass | 14.63 | S3 | supplementary, Table S1 row 5 | analysis/method_tests_2025/gap_attribution_readable.csv:22 (literal) |
| pass | 15.76 | S3 | supplementary, Table S1 row 5 | analysis/method_tests_2025/gap_attribution_readable.csv:22 (literal) |
| pass | 1.13 | S3 | supplementary, Table S1 row 5 | analysis/method_tests_2025/gap_attribution_readable.csv:22 (literal) |
| pass | 1991 | S3 | supplementary, Table S1 row 6 | analysis/method_tests_2025/gap_attribution_readable.csv:83 (literal) |
| pass | 92 | S3 | supplementary, Table S1 row 6 | analysis/method_tests_2025/gap_attribution_readable.csv:83 (literal) |
| pass | 1.7176 | S3 | supplementary, Table S1 row 6 | analysis/method_tests_2025/gap_attribution_readable.csv:83 (literal) |
| pass | 1.758 | S3 | supplementary, Table S1 row 6 | analysis/method_tests_2025/gap_attribution_readable.csv:83 (literal) |
| pass | 0.0404 | S3 | supplementary, Table S1 row 6 | analysis/method_tests_2025/gap_attribution_readable.csv:83 (literal) |
| pass | 1990 | S3 | supplementary, Table S1 row 7 | analysis/method_tests_2025/gap_attribution_readable.csv:91 (literal) |
| pass | 91 | S3 | supplementary, Table S1 row 7 | analysis/method_tests_2025/gap_attribution_readable.csv:91 (literal) |
| pass | 108.912 | S3 | supplementary, Table S1 row 7 | analysis/method_tests_2025/gap_attribution_readable.csv:97 (literal) |
| pass | 109 | S3 | supplementary, Table S1 row 7 | analysis/method_tests_2025/gap_attribution_readable.csv:21 (literal) |
| pass | 0.088 | S3 | supplementary, Table S1 row 7 | analysis/method_tests_2025/gap_attribution_readable.csv:97 (literal) |
| pass | 1990 | S3 | supplementary, Table S1 row 8 | analysis/method_tests_2025/gap_attribution_readable.csv:91 (literal) |
| pass | 91 | S3 | supplementary, Table S1 row 8 | analysis/method_tests_2025/gap_attribution_readable.csv:91 (literal) |
| pass | 205.9624 | S3 | supplementary, Table S1 row 8 | analysis/method_tests_2025/gap_attribution_readable.csv:104 (literal) |
| pass | 206 | S3 | supplementary, Table S1 row 8 | analysis/method_tests_2025/gap_attribution_readable.csv:104 (literal) |
| pass | 0.0376 | S3 | supplementary, Table S1 row 8 | analysis/method_tests_2025/gap_attribution_readable.csv:104 (literal) |
| pass | 1990 | S3 | supplementary, Table S1 row 9 | analysis/method_tests_2025/gap_attribution_readable.csv:91 (literal) |
| pass | 91 | S3 | supplementary, Table S1 row 9 | analysis/method_tests_2025/gap_attribution_readable.csv:91 (literal) |
| pass | 95.6635 | S3 | supplementary, Table S1 row 9 | analysis/method_tests_2025/gap_attribution_readable.csv:105 (literal) |
| pass | 96 | S3 | supplementary, Table S1 row 9 | analysis/method_tests_2025/gap_attribution_readable.csv:45 (literal) |
| pass | 0.3365 | S3 | supplementary, Table S1 row 9 | analysis/method_tests_2025/gap_attribution_readable.csv:105 (literal) |
| pass | 1990 | S3 | supplementary, Table S1 row 10 | analysis/method_tests_2025/gap_attribution_readable.csv:91 (literal) |
| pass | 91 | S3 | supplementary, Table S1 row 10 | analysis/method_tests_2025/gap_attribution_readable.csv:91 (literal) |
| pass | 187.8881 | S3 | supplementary, Table S1 row 10 | analysis/method_tests_2025/gap_attribution_readable.csv:112 (literal) |
| pass | 188 | S3 | supplementary, Table S1 row 10 | analysis/method_tests_2025/gap_attribution_readable.csv:112 (literal) |
| pass | 0.1119 | S3 | supplementary, Table S1 row 10 | analysis/method_tests_2025/gap_attribution_readable.csv:112 (literal) |
| pass | 1997 | S3 | supplementary, Table S1 row 11 | analysis/method_tests_2025/gap_attribution_readable.csv:113 (literal) |
| pass | 98 | S3 | supplementary, Table S1 row 11 | analysis/method_tests_2025/gap_attribution_readable.csv:50 (literal) |
| pass | 31.95 | S3 | supplementary, Table S1 row 11 | analysis/method_tests_2025/gap_attribution_readable.csv:113 (literal) |
| pass | 31.578 | S3 | supplementary, Table S1 row 11 | analysis/method_tests_2025/gap_attribution_readable.csv:113 (literal) |
| pass | -0.372 | S3 | supplementary, Table S1 row 11 | analysis/method_tests_2025/gap_attribution_readable.csv:113 (literal) |
| pass | 1997 | S3 | supplementary, Table S1 row 12 | analysis/method_tests_2025/gap_attribution_readable.csv:113 (literal) |
| pass | 98 | S3 | supplementary, Table S1 row 12 | analysis/method_tests_2025/gap_attribution_readable.csv:50 (literal) |
| pass | 3.471 | S3 | supplementary, Table S1 row 12 | analysis/method_tests_2025/gap_attribution_readable.csv:115 (literal) |
| pass | 3.514 | S3 | supplementary, Table S1 row 12 | analysis/method_tests_2025/gap_attribution_readable.csv:113 (literal) |
| pass | 0.043 | S3 | supplementary, Table S1 row 12 | analysis/method_tests_2025/gap_attribution_readable.csv:115 (literal) |
| pass | 12.325 | S3 | supplementary, Table S1 row 13 | analysis/method_tests_2025/gap_attribution_readable.csv:126 (literal) |
| pass | 10.1 | S3 | supplementary, Table S1 row 13 | analysis/method_tests_2025/gap_attribution_readable.csv:7 (literal) |
| pass | -2.225 | S3 | supplementary, Table S1 row 13 | analysis/method_tests_2025/gap_attribution_readable.csv:126 (literal) |
| pass | 7.4939 | S3 | supplementary, Table S1 row 14 | analysis/method_tests_2025/gap_attribution_readable.csv:127 (literal) |
| pass | 6.0 | S3 | supplementary, Table S1 row 14 | analysis/method_tests_2025/gap_attribution_readable.csv:127 (literal) |
| pass | -1.4939 | S3 | supplementary, Table S1 row 14 | analysis/method_tests_2025/gap_attribution_readable.csv:127 (literal) |
| pass | 20.9666 | S3 | supplementary, Table S1 row 15 | analysis/method_tests_2025/gap_attribution_readable.csv:135 (literal) |
| pass | 16.1 | S3 | supplementary, Table S1 row 15 | analysis/method_tests_2025/gap_attribution_readable.csv:135 (literal) |
| pass | -4.8666 | S3 | supplementary, Table S1 row 15 | analysis/method_tests_2025/gap_attribution_readable.csv:135 (literal) |
| pass | 6.908 | S3 | supplementary, Table S1 row 16 | analysis/method_tests_2025/gap_attribution_readable.csv:136 (literal) |
| pass | 5.4 | S3 | supplementary, Table S1 row 16 | analysis/method_tests_2025/gap_attribution_readable.csv:136 (literal) |
| pass | -1.508 | S3 | supplementary, Table S1 row 16 | analysis/method_tests_2025/gap_attribution_readable.csv:136 (literal) |
| pass | 8.8168 | S3 | supplementary, Table S1 row 17 | analysis/method_tests_2025/gap_attribution_readable.csv:142 (literal) |
| pass | 6.5 | S3 | supplementary, Table S1 row 17 | analysis/method_tests_2025/gap_attribution_readable.csv:142 (literal) |
| pass | -2.3168 | S3 | supplementary, Table S1 row 17 | analysis/method_tests_2025/gap_attribution_readable.csv:142 (literal) |
| pass | 7.8643 | S3 | supplementary, Table S1 row 18 | analysis/method_tests_2025/gap_attribution_readable.csv:143 (literal) |
| pass | 5.9 | S3 | supplementary, Table S1 row 18 | analysis/method_tests_2025/gap_attribution_readable.csv:143 (literal) |
| pass | -1.9643 | S3 | supplementary, Table S1 row 18 | analysis/method_tests_2025/gap_attribution_readable.csv:143 (literal) |
| pass | 18.4226 | S3 | supplementary, Table S1 row 19 | analysis/method_tests_2025/gap_attribution_readable.csv:149 (literal) |
| pass | 13.5 | S3 | supplementary, Table S1 row 19 | analysis/method_tests_2025/gap_attribution_readable.csv:149 (literal) |
| pass | -4.9226 | S3 | supplementary, Table S1 row 19 | analysis/method_tests_2025/gap_attribution_readable.csv:149 (literal) |
| pass | 11.9495 | S3 | supplementary, Table S1 row 20 | analysis/method_tests_2025/gap_attribution_readable.csv:150 (literal) |
| pass | 8.4 | S3 | supplementary, Table S1 row 20 | analysis/method_tests_2025/gap_attribution_readable.csv:150 (literal) |
| pass | -3.5495 | S3 | supplementary, Table S1 row 20 | analysis/method_tests_2025/gap_attribution_readable.csv:150 (literal) |
| pass | 14.146 | S3 | supplementary, Table S1 row 21 | analysis/method_tests_2025/gap_attribution_readable.csv:156 (literal) |
| pass | 10.6 | S3 | supplementary, Table S1 row 21 | analysis/method_tests_2025/gap_attribution_readable.csv:156 (literal) |
| pass | -3.546 | S3 | supplementary, Table S1 row 21 | analysis/method_tests_2025/gap_attribution_readable.csv:156 (literal) |
| pass | 6.8265 | S3 | supplementary, Table S1 row 22 | analysis/method_tests_2025/gap_attribution_readable.csv:157 (literal) |
| pass | 5.2 | S3 | supplementary, Table S1 row 22 | analysis/method_tests_2025/gap_attribution_readable.csv:157 (literal) |
| pass | -1.6265 | S3 | supplementary, Table S1 row 22 | analysis/method_tests_2025/gap_attribution_readable.csv:157 (literal) |
| pass | 1990 | S3 | supplementary, Table S6 row 1 | analysis/method_tests_2025/fidelity.csv:2 (literal) |
| pass | 91 | S3 | supplementary, Table S6 row 1 | analysis/method_tests_2025/fidelity.csv:2 (literal) |
| pass | 109 | S3 | supplementary, Table S6 row 1 | analysis/method_tests_2025/fidelity.csv:2 (literal) |
| pass | 1990 | S3 | supplementary, Table S6 row 2 | analysis/method_tests_2025/fidelity.csv:2 (literal) |
| pass | 91 | S3 | supplementary, Table S6 row 2 | analysis/method_tests_2025/fidelity.csv:2 (literal) |
| pass | 96 | S3 | supplementary, Table S6 row 2 | analysis/method_tests_2025/fidelity.csv:3 (literal) |
| pass | 206 | S3 | supplementary, Table S6 row 3 | analysis/method_tests_2025/fidelity.csv:4 (literal) |
| pass | 188 | S3 | supplementary, Table S6 row 4 | analysis/method_tests_2025/fidelity.csv:5 (literal) |
| pass | 1991 | S3 | supplementary, Table S6 row 5 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 92 | S3 | supplementary, Table S6 row 5 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 1.758 | S3 | supplementary, Table S6 row 5 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 1991 | S3 | supplementary, Table S6 row 6 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 92 | S3 | supplementary, Table S6 row 6 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 0.095 | S3 | supplementary, Table S6 row 6 | analysis/method_tests_2025/fidelity.csv:7 (literal) |
| pass | 1991 | S3 | supplementary, Table S6 row 7 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 92 | S3 | supplementary, Table S6 row 7 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 0.312 | S3 | supplementary, Table S6 row 7 | analysis/method_tests_2025/fidelity.csv:8 (literal) |
| pass | 1991 | S3 | supplementary, Table S6 row 8 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 92 | S3 | supplementary, Table S6 row 8 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 2.165 | S3 | supplementary, Table S6 row 8 | analysis/method_tests_2025/fidelity.csv:9 (literal) |
| pass | 1991 | S3 | supplementary, Table S6 row 9 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 92 | S3 | supplementary, Table S6 row 9 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 0.032 | S3 | supplementary, Table S6 row 9 | analysis/method_tests_2025/fidelity.csv:10 (literal) |
| pass | 1991 | S3 | supplementary, Table S6 row 10 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 92 | S3 | supplementary, Table S6 row 10 | analysis/method_tests_2025/fidelity.csv:6 (literal) |
| pass | 0.854 | S3 | supplementary, Table S6 row 10 | analysis/method_tests_2025/fidelity.csv:11 (literal) |
| pass | 2011 | S3 | supplementary, Table S6 row 11 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 35.13 | S3 | supplementary, Table S6 row 11 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 2011 | S3 | supplementary, Table S6 row 12 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 112.20 | S3 | supplementary, Table S6 row 12 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 2011 | S3 | supplementary, Table S6 row 13 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 97.73 | S3 | supplementary, Table S6 row 13 | analysis/method_tests_2025/fidelity.csv:14 (literal) |
| pass | 2011 | S3 | supplementary, Table S6 row 14 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 114.88 | S3 | supplementary, Table S6 row 14 | analysis/method_tests_2025/fidelity.csv:15 (literal) |
| pass | 2011 | S3 | supplementary, Table S6 row 15 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 15.76 | S3 | supplementary, Table S6 row 15 | analysis/method_tests_2025/fidelity.csv:16 (literal) |
| pass | 2011 | S3 | supplementary, Table S6 row 16 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 135.76 | S3 | supplementary, Table S6 row 16 | analysis/method_tests_2025/fidelity.csv:17 (literal) |
| pass | 10.1 | S3 | supplementary, Table S6 row 17 | analysis/method_tests_2025/fidelity.csv:18 (literal) |
| pass | 6.0 | S3 | supplementary, Table S6 row 18 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 16.1 | S3 | supplementary, Table S6 row 19 | analysis/method_tests_2025/fidelity.csv:20 (literal) |
| pass | 5.4 | S3 | supplementary, Table S6 row 20 | analysis/method_tests_2025/fidelity.csv:21 (literal) |
| pass | 6.5 | S3 | supplementary, Table S6 row 21 | analysis/method_tests_2025/fidelity.csv:19 (literal) |
| pass | 5.9 | S3 | supplementary, Table S6 row 22 | analysis/method_tests_2025/fidelity.csv:23 (literal) |
| pass | 13.5 | S3 | supplementary, Table S6 row 23 | analysis/method_tests_2025/fidelity.csv:24 (literal) |
| pass | 8.4 | S3 | supplementary, Table S6 row 24 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 10.6 | S3 | supplementary, Table S6 row 25 | analysis/method_tests_2025/fidelity.csv:26 (literal) |
| pass | 5.2 | S3 | supplementary, Table S6 row 26 | analysis/method_tests_2025/fidelity.csv:27 (literal) |
| pass | 67 | S3 | supplementary, Table S6 row 27 | analysis/method_tests_2025/fidelity.csv:3 (literal) |
| pass | 34 | S3 | supplementary, Table S6 row 28 | analysis/method_tests_2025/fidelity.csv:12 (literal) |
| pass | 59 | S3 | supplementary, Table S6 row 29 | analysis/method_tests_2025/fidelity.csv:13 (literal) |
| pass | 1997 | S3 | supplementary, Table S6 row 30 | analysis/method_tests_2025/fidelity.csv:18 (literal) |
| pass | 98 | S3 | supplementary, Table S6 row 30 | analysis/method_tests_2025/fidelity.csv:31 (literal) |
| pass | 31.578 | S3 | supplementary, Table S6 row 30 | analysis/method_tests_2025/fidelity.csv:31 (literal) |
| pass | 1997 | S3 | supplementary, Table S6 row 31 | analysis/method_tests_2025/fidelity.csv:18 (literal) |
| pass | 98 | S3 | supplementary, Table S6 row 31 | analysis/method_tests_2025/fidelity.csv:31 (literal) |
| pass | 3.514 | S3 | supplementary, Table S6 row 31 | analysis/method_tests_2025/fidelity.csv:32 (literal) |
| pass | 0.24 | S3 | supplementary, Table S6 row 32 | analysis/method_tests_2025/fidelity.csv:33 (literal) |
| pass | 0.24 | S3 | supplementary, Table S6 row 32 | analysis/method_tests_2025/fidelity.csv:33 (literal) |
| pass | 16 | S3 | supplementary, Table S6 row 33 | analysis/method_tests_2025/fidelity.csv:20 (literal) |
| pass | 40439187 | S3 | supplementary, Table S6 row 33 | analysis/method_tests_2025/fidelity.csv:34 (literal) |
| pass | 16 | S3 | supplementary, Table S6 row 34 | analysis/method_tests_2025/fidelity.csv:20 (literal) |
| pass | 9431487 | S3 | supplementary, Table S6 row 34 | analysis/method_tests_2025/fidelity.csv:35 (literal) |
| pass | 145.2 | S3 | supplementary, Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv:2 (literal) |
| pass | 169.7 | S3 | supplementary, Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv:2 (literal) |
| pass | 177.0 | S3 | supplementary, Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv:2 (literal) |
| pass | 148.8 | S3 | supplementary, Table S7 row 2 | analysis/method_tests_2025/intake_variant.csv:3 (literal) |
| pass | 182.3 | S3 | supplementary, Table S7 row 2 | analysis/method_tests_2025/intake_variant.csv:3 (literal) |
| pass | 205.8 | S3 | supplementary, Table S7 row 2 | analysis/method_tests_2025/intake_variant.csv:3 (literal) |
| pass | 1 | S3 | supplementary, Table S7 row 3 | analysis/method_tests_2025/intake_variant.csv:4 (literal) |
| pass | 159.8 | S3 | supplementary, Table S7 row 3 | analysis/method_tests_2025/intake_variant.csv:4 (literal) |
| pass | 189.0 | S3 | supplementary, Table S7 row 3 | analysis/method_tests_2025/intake_variant.csv:4 (literal) |
| pass | 207.7 | S3 | supplementary, Table S7 row 3 | analysis/method_tests_2025/intake_variant.csv:4 (literal) |
| pass | 1 | S3 | supplementary, Table S7 row 4 | analysis/method_tests_2025/intake_variant.csv:4 (literal) |
| pass | 385.7 | S3 | supplementary, Table S7 row 4 | analysis/method_tests_2025/intake_variant.csv:5 (literal) |
| pass | 454.2 | S3 | supplementary, Table S7 row 4 | analysis/method_tests_2025/intake_variant.csv:5 (literal) |
| pass | 537.4 | S3 | supplementary, Table S7 row 4 | analysis/method_tests_2025/intake_variant.csv:5 (literal) |
| pass | 1 | S3 | supplementary, Table S7 row 5 | analysis/method_tests_2025/intake_variant.csv:4 (literal) |
| pass | 343.4 | S3 | supplementary, Table S7 row 5 | analysis/method_tests_2025/intake_variant.csv:6 (literal) |
| pass | 404.8 | S3 | supplementary, Table S7 row 5 | analysis/method_tests_2025/intake_variant.csv:6 (literal) |
| pass | 472.1 | S3 | supplementary, Table S7 row 5 | analysis/method_tests_2025/intake_variant.csv:6 (literal) |
| pass | 3 | S3 | supplementary, Table S7 row 6 | analysis/method_tests_2025/intake_variant.csv:2 (literal) |
| pass | 146.2 | S3 | supplementary, Table S7 row 6 | analysis/method_tests_2025/intake_variant.csv:7 (literal) |
| pass | 172.5 | S3 | supplementary, Table S7 row 6 | analysis/method_tests_2025/intake_variant.csv:7 (literal) |
| pass | 192.9 | S3 | supplementary, Table S7 row 6 | analysis/method_tests_2025/intake_variant.csv:7 (literal) |
| pass | 3 | S3 | supplementary, Table S7 row 7 | analysis/method_tests_2025/intake_variant.csv:2 (literal) |
| pass | 316.9 | S3 | supplementary, Table S7 row 7 | analysis/method_tests_2025/intake_variant.csv:8 (literal) |
| pass | 370.9 | S3 | supplementary, Table S7 row 7 | analysis/method_tests_2025/intake_variant.csv:8 (literal) |
| pass | 430.2 | S3 | supplementary, Table S7 row 7 | analysis/method_tests_2025/intake_variant.csv:8 (literal) |
| pass | 3 | S3 | supplementary, Table S7 row 8 | analysis/method_tests_2025/intake_variant.csv:2 (literal) |
| pass | 287.7 | S3 | supplementary, Table S7 row 8 | analysis/method_tests_2025/intake_variant.csv:9 (literal) |
| pass | 337.1 | S3 | supplementary, Table S7 row 8 | analysis/method_tests_2025/intake_variant.csv:9 (literal) |
| pass | 388.6 | S3 | supplementary, Table S7 row 8 | analysis/method_tests_2025/intake_variant.csv:9 (literal) |
| pass | 275.7 | S3 | supplementary, Table S7 row 9 | analysis/method_tests_2025/intake_variant.csv:11 (literal) |
| pass | 324.3 | S3 | supplementary, Table S7 row 9 | analysis/method_tests_2025/intake_variant.csv:11 (literal) |
| pass | 375.8 | S3 | supplementary, Table S7 row 9 | analysis/method_tests_2025/intake_variant.csv:11 (literal) |
| pass | 112.9 | S3 | supplementary, Table S7 row 10 | analysis/method_tests_2025/intake_variant.csv:12 (literal) |
| pass | 132.0 | S3 | supplementary, Table S7 row 10 | analysis/method_tests_2025/intake_variant.csv:12 (literal) |
| pass | 137.6 | S3 | supplementary, Table S7 row 10 | analysis/method_tests_2025/intake_variant.csv:12 (literal) |
| pass | 110.9 | S3 | supplementary, Table S7 row 11 | analysis/method_tests_2025/intake_variant.csv:13 (literal) |
| pass | 129.7 | S3 | supplementary, Table S7 row 11 | analysis/method_tests_2025/intake_variant.csv:13 (literal) |
| pass | 135.2 | S3 | supplementary, Table S7 row 11 | analysis/method_tests_2025/intake_variant.csv:13 (literal) |
| pass | 41.1 | S3 | supplementary, Table S7 row 12 | analysis/method_tests_2025/intake_variant.csv:14 (literal) |
| pass | 48.1 | S3 | supplementary, Table S7 row 12 | analysis/method_tests_2025/intake_variant.csv:14 (literal) |
| pass | 58.1 | S3 | supplementary, Table S7 row 12 | analysis/method_tests_2025/intake_variant.csv:14 (literal) |
| pass | 12.0 | S3 | supplementary, Table S7 row 13 | analysis/method_tests_2025/intake_variant.csv:15 (literal) |
| pass | 19.7 | S3 | supplementary, Table S7 row 13 | analysis/method_tests_2025/intake_variant.csv:15 (literal) |
| pass | 17.9 | S3 | supplementary, Table S7 row 13 | analysis/method_tests_2025/intake_variant.csv:15 (literal) |
| pass | 126.6 | S3 | supplementary, Table S7 row 14 | analysis/method_tests_2025/intake_variant.csv:16 (literal) |
| pass | 137.2 | S3 | supplementary, Table S7 row 14 | analysis/method_tests_2025/intake_variant.csv:16 (literal) |
| pass | 138.1 | S3 | supplementary, Table S7 row 14 | analysis/method_tests_2025/intake_variant.csv:16 (literal) |
| pass | 41.5 | S3 | supplementary, Table S7 row 15 | analysis/method_tests_2025/intake_variant.csv:18 (literal) |
| pass | 41.5 | S3 | supplementary, Table S7 row 15 | analysis/method_tests_2025/intake_variant.csv:18 (literal) |
| pass | 41.5 | S3 | supplementary, Table S7 row 15 | analysis/method_tests_2025/intake_variant.csv:18 (literal) |
| pass | 53.6 | S3 | supplementary, Table S7 row 16 | analysis/method_tests_2025/intake_variant.csv:19 (literal) |
| pass | 53.6 | S3 | supplementary, Table S7 row 16 | analysis/method_tests_2025/intake_variant.csv:19 (literal) |
| pass | 53.6 | S3 | supplementary, Table S7 row 16 | analysis/method_tests_2025/intake_variant.csv:19 (literal) |
| pass | 64.8 | S3 | supplementary, Table S8 row 1 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 117.0 | S3 | supplementary, Table S8 row 1 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 1.56 | S3 | supplementary, Table S8 row 1 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 2.82 | S3 | supplementary, Table S8 row 1 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 1.21 | S3 | supplementary, Table S8 row 1 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 2.18 | S3 | supplementary, Table S8 row 1 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 64.8 | S3 | supplementary, Table S8 row 2 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 84.6 | S3 | supplementary, Table S8 row 2 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 1.56 | S3 | supplementary, Table S8 row 2 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 2.04 | S3 | supplementary, Table S8 row 2 | analysis/method_tests_2025/cross_method_local.csv:4 (literal) |
| pass | 1.21 | S3 | supplementary, Table S8 row 2 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 1.58 | S3 | supplementary, Table S8 row 2 | analysis/method_tests_2025/cross_method_local.csv:4 (literal) |
| pass | 76.0 | S3 | supplementary, Table S8 row 3 | analysis/method_tests_2025/cross_method_local.csv:6 (literal) |
| pass | 1.83 | S3 | supplementary, Table S8 row 3 | analysis/method_tests_2025/cross_method_local.csv:6 (literal) |
| pass | 1.42 | S3 | supplementary, Table S8 row 3 | analysis/method_tests_2025/cross_method_local.csv:6 (literal) |
| pass | 133.8 | S3 | supplementary, Table S8 row 4 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 210.7 | S3 | supplementary, Table S8 row 4 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 3.22 | S3 | supplementary, Table S8 row 4 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 5.08 | S3 | supplementary, Table S8 row 4 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 2.50 | S3 | supplementary, Table S8 row 4 | analysis/method_tests_2025/cross_method_local.csv:2 (rounded(x1)) |
| pass | 3.93 | S3 | supplementary, Table S8 row 4 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 64.8 | S3 | supplementary, Table S8 row 5 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 210.7 | S3 | supplementary, Table S8 row 5 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 1.56 | S3 | supplementary, Table S8 row 5 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 5.08 | S3 | supplementary, Table S8 row 5 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 1.21 | S3 | supplementary, Table S8 row 5 | analysis/method_tests_2025/cross_method_local.csv:3 (literal) |
| pass | 3.93 | S3 | supplementary, Table S8 row 5 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 146.2 | S3 | supplementary, Table S8 row 6 | analysis/method_tests_2025/cross_method_local.csv:5 (literal) |
| pass | 343.4 | S3 | supplementary, Table S8 row 6 | analysis/method_tests_2025/cross_method_local.csv:5 (literal) |
| pass | 3.52 | S3 | supplementary, Table S8 row 6 | analysis/method_tests_2025/cross_method_local.csv:5 (literal) |
| pass | 8.27 | S3 | supplementary, Table S8 row 6 | analysis/method_tests_2025/cross_method_local.csv:5 (literal) |
| pass | 275.8 | S3 | supplementary, Table S8 row 7 | qa/reports/V39_check_B113.md:75 (literal) |
| pass | 6.65 | S3 | supplementary, Table S8 row 7 | analysis/method_tests_2025/cross_method_local.csv:7 (literal) |
| pass | 5.15 | S3 | supplementary, Table S8 row 7 | analysis/method_tests_2025/cross_method_local.csv:7 (literal) |
| pass | 133.8 | S3 | supplementary, Table S8 row 8 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 343.4 | S3 | supplementary, Table S8 row 8 | analysis/method_tests_2025/cross_method_local.csv:5 (literal) |
| pass | 3.22 | S3 | supplementary, Table S8 row 8 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 8.27 | S3 | supplementary, Table S8 row 8 | analysis/method_tests_2025/cross_method_local.csv:5 (literal) |
| pass | 2.50 | S3 | supplementary, Table S8 row 8 | analysis/method_tests_2025/cross_method_local.csv:2 (rounded(x1)) |
| pass | 1990 | S3 | supplementary, Table S8 row 9 | analysis/method_tests_2025/cross_method_local.csv:5 (literal) |
| pass | 3 | S3 | supplementary, Table S8 row 9 | analysis/method_tests_2025/cross_method_local.csv:2 (literal) |
| pass | 103 | S3 | supplementary, Table S8 row 9 | analysis/method_tests_2025/cross_method_local.csv:5 (literal) |
| pass | 2 | S7 | supplementary, Table S9 row 1 | qa/reports/V28_section7_matrix.md:11 (literal) |
| pass | 2 | S7 | supplementary, Table S9 row 2 | qa/reports/V28_section7_matrix.md:11 (literal) |
| pass | 3 | S7 | supplementary, Table S9 row 3 | qa/reports/V28_section7_matrix.md:12 (literal) |
| pass | 2025 | S5 | supplementary, Table S3 row 1 | analysis/sensitivity_2025/sobol_2025-fixed.csv:15 (literal) |
| pass | 19 | S5 | supplementary, Table S3 row 1 | results/ranges_2025-fixed_wide.csv:2 (literal) |
| pass | 31.1 | S5 | supplementary, Table S3 row 1 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 49.2 | S5 | supplementary, Table S3 row 1 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 26.2 | S5 | supplementary, Table S3 row 1 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 58.1 | S5 | supplementary, Table S3 row 1 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 41.5 | S5 | supplementary, Table S3 row 1 | results/ranges_2025-fixed_wide.csv:2 (rounded(x1e-06)) |
| pass | 2025 | S5 | supplementary, Table S3 row 2 | analysis/sensitivity_2025/sobol_2025-fixed.csv:15 (literal) |
| pass | 19 | S5 | supplementary, Table S3 row 2 | results/ranges_2025-fixed_wide.csv:2 (literal) |
| pass | 13.3 | S5 | supplementary, Table S3 row 2 | results/ranges_2025-fixed_wide.csv:4 (rounded(x1e-06)) |
| pass | 18.8 | S5 | supplementary, Table S3 row 2 | results/ranges_2025-fixed_wide.csv:4 (rounded(x1e-06)) |
| pass | 12.4 | S5 | supplementary, Table S3 row 2 | results/ranges_2025-fixed_wide.csv:4 (rounded(x1e-06)) |
| pass | 19.9 | S5 | supplementary, Table S3 row 2 | results/ranges_2025-fixed_wide.csv:4 (rounded(x1e-06)) |
| pass | 15.6 | S5 | supplementary, Table S3 row 2 | results/ranges_2025-fixed_wide.csv:4 (rounded(x1e-06)) |
| pass | 2025 | S5 | supplementary, Table S3 row 3 | register B110:1 (literal) |
| pass | 13 | S5 | supplementary, Table S3 row 3 | results/ranges_2025-mirror.csv:26 (literal) |
| pass | 43.4 | S5 | supplementary, Table S3 row 3 | results/ranges_2025-mirror.csv:2 (rounded(x1e-06)) |
| pass | 54.3 | S5 | supplementary, Table S3 row 3 | results/ranges_2025-mirror.csv:2 (rounded(x1e-06)) |
| pass | 49.4 | S5 | supplementary, Table S3 row 3 | results/ranges_2025-mirror.csv:2 (rounded(x1e-06)) |
| pass | 13 | S5 | supplementary, Table S3 row 4 | results/ranges_2025-mirror.csv:26 (literal) |
| pass | 11.8 | S5 | supplementary, Table S3 row 4 | results/ranges_2025-mirror.csv:3 (rounded(x1e-06)) |
| pass | 16.0 | S5 | supplementary, Table S3 row 4 | results/ranges_2025-mirror.csv:3 (rounded(x1e-06)) |
| pass | 14.1 | S5 | supplementary, Table S3 row 4 | results/ranges_2025-mirror.csv:3 (rounded(x1e-06)) |
| pass | 13 | S5 | supplementary, Table S3 row 5 | results/ranges_2025-fixed.csv:26 (literal) |
| pass | 36.3 | S5 | supplementary, Table S3 row 5 | results/ranges_2025-fixed.csv:2 (rounded(x1e-06)) |
| pass | 45.8 | S5 | supplementary, Table S3 row 5 | results/ranges_2025-fixed.csv:2 (rounded(x1e-06)) |
| pass | 41.5 | S5 | supplementary, Table S3 row 5 | results/ranges_2025-fixed.csv:2 (rounded(x1e-06)) |
| pass | 13 | S5 | supplementary, Table S3 row 6 | results/ranges_2025-fixed.csv:26 (literal) |
| pass | 13.4 | S5 | supplementary, Table S3 row 6 | results/ranges_2025-fixed.csv:3 (rounded(x1e-06)) |
| pass | 16.5 | S5 | supplementary, Table S3 row 6 | results/ranges_2025-fixed.csv:3 (rounded(x1e-06)) |
| pass | 15.6 | S5 | supplementary, Table S3 row 6 | results/ranges_2025-fixed.csv:3 (rounded(x1e-06)) |
| pass | 13 | S5 | supplementary, Table S3 row 7 | results/ranges_2025-improved.csv:26 (literal) |
| pass | 46.2 | S5 | supplementary, Table S3 row 7 | results/ranges_2025-improved.csv:2 (rounded(x1e-06)) |
| pass | 60.1 | S5 | supplementary, Table S3 row 7 | results/ranges_2025-improved.csv:2 (rounded(x1e-06)) |
| pass | 53.6 | S5 | supplementary, Table S3 row 7 | results/ranges_2025-improved.csv:2 (rounded(x1e-06)) |
| pass | 13 | S5 | supplementary, Table S3 row 8 | results/ranges_2025-improved.csv:26 (literal) |
| pass | 15.9 | S5 | supplementary, Table S3 row 8 | results/ranges_2025-improved.csv:3 (rounded(x1e-06)) |
| pass | 19.4 | S5 | supplementary, Table S3 row 8 | results/ranges_2025-improved.csv:3 (rounded(x1e-06)) |
| pass | 18.5 | S5 | supplementary, Table S3 row 8 | results/ranges_2025-improved.csv:3 (rounded(x1e-06)) |
| pass | 12 | S5 | supplementary, Table S3a row 1 | analysis/waste_2025/README.md:7 (literal) |
| pass | 14 | S5 | supplementary, Table S3a row 1 | analysis/waste_2025/README.md:25 (literal) |
| pass | 0 | S5 | supplementary, Table S3a row 2 | methods/loss-factors-australia/method.json:5 (literal) |
| pass | 1 | S5 | supplementary, Table S3a row 2 | methods/loss-factors-australia/method.json:5 (literal) |
| pass | 474 | S5 | supplementary, Table S3a row 2 | qa/reports/B115_monte_carlo_widened.md:17 (literal) |
| pass | 0 | S5 | supplementary, Table S3a row 4 | pipeline/yields/recent/livestock_zone.py:25 (literal) |
| pass | 1 | S5 | supplementary, Table S3a row 4 | pipeline/yields/recent/livestock_zone.py:15 (literal) |
| pass | 1.000 | S5 | supplementary, Table S3a row 5 | qa/reports/B115_monte_carlo_widened.md:20 (literal) |
| pass | 1.286 | S5 | supplementary, Table S3a row 5 | qa/reports/B115_monte_carlo_widened.md:20 (literal) |
| pass | 1.4 | S5 | supplementary, Table S3a row 5 | qa/reports/B115_monte_carlo_widened.md:20 (literal) |
| pass | 1.8 | S5 | supplementary, Table S3a row 5 | qa/reports/B115_monte_carlo_widened.md:20 (literal) |
| pass | 1.356 | S5 | supplementary, Table S3a row 6 | data/abs-2022-25/group_trend.json:27 (rounded(x1)) |
| pass | 1.289 | S5 | supplementary, Table S3a row 6 | data/abs-2022-25/group_trend.json:5 (rounded(x1)) |
| pass | 12 | S3 | supplementary, sentence 56 | analysis/method_tests_2025/bases.csv:14 (literal) |
| pass | 28 | S7 | supplementary, sentence 12 | papers/B_methods/SECTION7_DRAFT.md:29 (literal) |
| locator | 1990 | 1 | B_s01-03, sentence 10 | page, year, label or section number; not a figure |
| locator | 1995 | 1 | B_s01-03, sentence 13 | page, year, label or section number; not a figure |
| locator | 341 | 1 | B_s01-03, sentence 13 | page, year, label or section number; not a figure |
| locator | 343 | 1 | B_s01-03, sentence 13 | page, year, label or section number; not a figure |
| locator | 2018 | 1 | B_s01-03, sentence 15 | page, year, label or section number; not a figure |
| locator | 123 | 1 | B_s01-03, sentence 15 | page, year, label or section number; not a figure |
| locator | 2017 | 1 | B_s01-03, sentence 15 | page, year, label or section number; not a figure |
| locator | 2010 | 1 | B_s01-03, sentence 16 | page, year, label or section number; not a figure |
| locator | 2010 | 1 | B_s01-03, sentence 16 | page, year, label or section number; not a figure |
| locator | 2014 | 1 | B_s01-03, Table 1, Lane, Dawes and Grace 2014, 2015; Lane 2017 | page, year, label or section number; not a figure |
| locator | 280 | 1 | B_s01-03, Table 1, Lane, Dawes and Grace 2014, 2015; Lane 2017 | page, year, label or section number; not a figure |
| locator | 1922 | 1 | B_s01-03, Table 1, Taylor 1922; 1937 | page, year, label or section number; not a figure |
| locator | 8 | 1 | B_s01-03, Table 1 note | page, year, label or section number; not a figure |
| locator | 17 | 1 | B_s01-03, Table 1 note | page, year, label or section number; not a figure |
| locator | 143 | 1 | B_s01-03, Table 1 note | page, year, label or section number; not a figure |
| locator | 601 | 2 | B_s01-03, sentence 7 | page, year, label or section number; not a figure |
| locator | 603 | 2 | B_s01-03, sentence 8 | page, year, label or section number; not a figure |
| locator | 405 | 2 | B_s01-03, sentence 10 | page, year, label or section number; not a figure |
| locator | 2008 | 2 | B_s01-03, sentence 11 | page, year, label or section number; not a figure |
| locator | 131 | 2 | B_s01-03, sentence 11 | page, year, label or section number; not a figure |
| locator | 1999 | 2 | B_s01-03, sentence 12 | page, year, label or section number; not a figure |
| locator | 17 | 2 | B_s01-03, sentence 12 | page, year, label or section number; not a figure |
| locator | 343 | 2 | B_s01-03, sentence 13 | page, year, label or section number; not a figure |
| locator | 2001 | 2 | B_s01-03, sentence 17 | page, year, label or section number; not a figure |
| locator | 5 | 2 | B_s01-03, sentence 28 | page, year, label or section number; not a figure |
| locator | 6 | 2 | B_s01-03, sentence 28 | page, year, label or section number; not a figure |
| locator | 6 | 2 | B_s01-03, sentence 29 | page, year, label or section number; not a figure |
| locator | 4 | 2 | B_s01-03, sentence 29 | page, year, label or section number; not a figure |
| locator | 2009 | 3 | B_s01-03, sentence 1 | page, year, label or section number; not a figure |
| locator | 94 | 3 | B_s01-03, sentence 1 | page, year or label; not a figure |
| locator | 2018 | 3 | B_s01-03, sentence 2 | page, year, label or section number; not a figure |
| locator | 2 | 3 | B_s01-03, sentence 2 | page, year or label; not a figure |
| locator | 2022 | 3 | B_s01-03, sentence 3 | page, year, label or section number; not a figure |
| locator | 414 | 3 | B_s01-03, sentence 3 | page, year, label or section number; not a figure |
| locator | 415 | 3 | B_s01-03, sentence 3 | page, year, label or section number; not a figure |
| locator | 2019 | 3 | B_s01-03, sentence 3 | page, year, label or section number; not a figure |
| locator | 337 | 3 | B_s01-03, sentence 3 | page, year, label or section number; not a figure |
| locator | 2020 | 3 | B_s01-03, sentence 3 | page, year, label or section number; not a figure |
| locator | 1583 | 3 | B_s01-03, sentence 3 | page, year, label or section number; not a figure |
| locator | 2023 | abstract | B_s01-03, sentence 2 | page, year, label or section number; not a figure |
| locator | 5.11 | 1 | B_s01-03, sentence 22 | page, year, label or section number; not a figure |
| locator | 2014 | 1 | B_s01-03, sentence 17 | page, year, label or section number; not a figure |
| locator | 2015 | 1 | B_s01-03, sentence 17 | page, year, label or section number; not a figure |
| locator | 2017 | 1 | B_s01-03, sentence 17 | page, year, label or section number; not a figure |
| locator | 2022 | 1 | B_s01-03, sentence 21 | page, year, label or section number; not a figure |
| locator | 15 | 4 | B_s04-05, sentence 17 | page, year, label or section number; not a figure |
| locator | 1992 | 4 | B_s04-05, sentence 19 | page, year, label or section number; not a figure |
| locator | 89 | 4 | B_s04-05, sentence 26 | page, year, label or section number; not a figure |
| locator | 4 | 4 | B_s04-05, sentence 27 | page, year or label; not a figure |
| locator | 352 | 4 | B_s04-05, sentence 41 | page, year, label or section number; not a figure |
| locator | 2014 | 4 | B_s04-05, sentence 46 | page, year, label or section number; not a figure |
| locator | 3 | 5 | B_s04-05, sentence 1 | page, year, label or section number; not a figure |
| locator | 7 | 5 | B_s04-05, sentence 1 | page, year, label or section number; not a figure |
| locator | 99 | 5 | B_s04-05, sentence 11 | page, year, label or section number; not a figure |
| locator | 99 | 5 | B_s04-05, sentence 11 | page, year, label or section number; not a figure |
| locator | 100 | 5 | B_s04-05, sentence 12 | page, year or label; not a figure |
| locator | 14 | 5 | B_s04-05, sentence 15 | page, year, label or section number; not a figure |
| locator | 285 | 5 | B_s04-05, sentence 17 | page, year, label or section number; not a figure |
| locator | 6 | 5 | B_s04-05, sentence 22 | page, year, label or section number; not a figure |
| locator | 2 | 5 | B_s04-05, sentence 29 | page, year, label or section number; not a figure |
| locator | 3 | 5 | B_s04-05, sentence 29 | page, year, label or section number; not a figure |
| locator | 1 | 5 | B_s04-05, sentence 29 | page, year, label or section number; not a figure |
| locator | 195 | 5 | B_s04-05, sentence 39 | page, year, label or section number; not a figure |
| locator | 2025 | 5 | B_s04-05, sentence 41 | page, year, label or section number; not a figure |
| locator | 78 | 5 | B_s04-05, sentence 57 | page, year, label or section number; not a figure |
| locator | 78 | 5 | B_s04-05, Table 5 row 1 | page, year, label or section number; not a figure |
| locator | 2023 | 4 | B_s04-05, sentence 38 | page, year, label or section number; not a figure |
| locator | 2010 | 8 | B_s06-09, sentence 15 | page, year, label or section number; not a figure |
| locator | 2011 | 8 | B_s06-09, sentence 15 | page, year, label or section number; not a figure |
| locator | 2014 | 8 | B_s06-09, sentence 15 | page, year, label or section number; not a figure |
| locator | 201 | 8 | B_s06-09, sentence 15 | page, year or label; not a figure |
| locator | 202 | 8 | B_s06-09, sentence 15 | page, year or label; not a figure |
| locator | 2007 | 8 | B_s06-09, sentence 16 | page, year, label or section number; not a figure |
| locator | 2016 | 8 | B_s06-09, sentence 13 | page, year, label or section number; not a figure |
| locator | 2008 | S1 | supplementary, sentence 1 | page, year, label or section number; not a figure |
| locator | 126 | S1 | supplementary, sentence 1 | page, year, label or section number; not a figure |
| locator | 2007 | S2 | supplementary, sentence 4 | page, year, label or section number; not a figure |
| locator | 2013 | S2 | supplementary, sentence 11 | page, year, label or section number; not a figure |
| locator | 2017 | S2 | supplementary, sentence 11 | page, year, label or section number; not a figure |
| locator | 90 | S2 | supplementary, sentence 11 | page, year or label; not a figure |
| locator | 2013 | S2 | supplementary, sentence 14 | page, year, label or section number; not a figure |
| locator | 2014 | S2 | supplementary, sentence 14 | page, year, label or section number; not a figure |
| locator | 619 | S2 | supplementary, sentence 14 | page, year or label; not a figure |
| locator | 2013 | S2 | supplementary, sentence 26 | page, year, label or section number; not a figure |
| locator | 4 | S2 | supplementary, sentence 26 | page, year, label or section number; not a figure |
| locator | 2023 | S3 | supplementary, sentence 1 | page, year, label or section number; not a figure |
| locator | 10 | S3 | supplementary, sentence 3 | page, year, label or section number; not a figure |
| locator | 99 | S3 | supplementary, sentence 5 | page, year, label or section number; not a figure |
| locator | 4306.0 | S3 | supplementary, sentence 12 | page, year, label or section number; not a figure |
| locator | 1 | S3 | supplementary, sentence 13 | page, year, label or section number; not a figure |
| locator | 2 | S3 | supplementary, sentence 14 | page, year, label or section number; not a figure |
| locator | 3 | S3 | supplementary, sentence 15 | page, year, label or section number; not a figure |
| locator | 2006 | S1 | supplementary, sentence 8 | page, year, label or section number; not a figure |
| locator | 2 | S1 | supplementary, sentence 8 | page, year, label or section number; not a figure |
| locator | 9 | S1 | supplementary, sentence 9 | page, year, label or section number; not a figure |
| locator | 10 | S1 | supplementary, sentence 9 | page, year, label or section number; not a figure |
| locator | 98 | S2 | supplementary, sentence 7 | page, year, label or section number; not a figure |
| locator | 1 | S3 | supplementary, sentence 41 | page, year, label or section number; not a figure |
| locator | 2016 | S8 | supplementary, sentence 9 | page, year, label or section number; not a figure |
| locator | 17 | S8 | supplementary, sentence 9 | page, year, label or section number; not a figure |
| locator | 2021 | S8 | supplementary, sentence 10 | page, year, label or section number; not a figure |
| locator | 2023 | S8 | supplementary, sentence 16 | page, year, label or section number; not a figure |
| locator | 1990 | S8 | supplementary, sentence 18 | page, year, label or section number; not a figure |
| locator | 2025 | S5 | supplementary, Table S3 row 4 | page, year, label or section number; not a figure |
| locator | 2025 | S5 | supplementary, Table S3 row 5 | page, year, label or section number; not a figure |
| locator | 2025 | S5 | supplementary, Table S3 row 6 | page, year, label or section number; not a figure |
| locator | 2025 | S5 | supplementary, Table S3 row 7 | page, year, label or section number; not a figure |
| locator | 2025 | S5 | supplementary, Table S3 row 8 | page, year, label or section number; not a figure |
| locator | 2016 | S2 | supplementary, sentence 8 | page, year, label or section number; not a figure |
| locator | 2014 | S2 | supplementary, sentence 16 | page, year, label or section number; not a figure |
| locator | 2018 | S2 | supplementary, sentence 17 | page, year, label or section number; not a figure |
| locator | 2012 | S2 | supplementary, sentence 20 | page, year, label or section number; not a figure |
| locator | 2017 | S2 | supplementary, sentence 21 | page, year, label or section number; not a figure |
| locator | 2020 | S2 | supplementary, sentence 23 | page, year, label or section number; not a figure |
| locator | 1979 | S5 | supplementary, sentence 6 | page, year, label or section number; not a figure |
| locator | 2003 | S5 | supplementary, sentence 6 | page, year, label or section number; not a figure |
