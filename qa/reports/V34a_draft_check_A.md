# V34a: blind check of the first draft of Paper A against the registers (decision 91)

Checker: blind checker under brief `qa/briefs/V34a_draft_check_A.md` and `qa/briefs/_checker_rules_results_wave.md`. Files under test: `papers/A_results/draft/A_s01-04.md`, `A_s05-08.md`, `A_s09-12.md` and their claims csvs. Nothing in the repository was edited; this report is the only file written (scratch scripts sit in the session scratch folder).

## 1. Tolerance

Set before comparing:

* A number in the prose or a table passes when it equals a claims register value, a pending gate 4 value in that row's notes, or a committed csv cell, at the precision printed (a rounded figure passes when the register or csv value rounds to it; shares and ratios within one unit of the last printed digit).
* Counts and names must match exactly.
* A citation passes when the work is a literature register row and, where a page is given, the page on disk carries the figure or statement. Printed page numbers were read off the PDF on disk (`/home/user/carrying-capacity-models/` plus each row's local_path without its first segment).
* A sentence passes when it claims no more than its register row (or the scope's evidence table) supports.
* Header rules: release named at every figure on a release other than the corrected pair; people over capacity for status ratios (a capacity multiple worded as a multiple is allowed); yield basis named at every regional sum; "53 regions (52 NRM regions and the Northern Territory)" at first use in each section; no em dashes; British spelling; decision 33 tone; prose word count within 15% of the scope's budget (tables, captions, headings and figure placeholders excluded).

## 2. Wrong-value example

I copied the three draft files to scratch and changed "33.3 million people in 2011" (section 3) to "33.7 million". My number-coverage script (every number in the prose matched, with digit boundaries, against the claims csv fragments) then reported `('3', '33.7')` as missing, while the unchanged files report nothing missing. Against the register, 33.7 fails A001 (33.3 million, `2011-fixed`). The check can fail.

## 3. Per-section results

Sentence counts are approximate (prose only). Numbers counted include years and page numbers in prose; table cells counted separately.

| Section | Sentences checked | Numbers checked (prose / tables) | Fails | Wording issues | Words (budget, difference) |
|---|---|---|---|---|---|
| 1 Introduction | about 75 | 130 / 0 | 0 | 3 | 1,022 (900, +13.6%) |
| 2 Method and data | about 37 | 57 / 0 | 1 | 1 | 557 (600, -7%) |
| 3 Short-term picture | about 43 | 80 / 17 | 0 | 3 | 775 (800, -3%) |
| 4 What drove the change | about 28 | 52 / 34 | 0 | 2 | 518 (500, +3.6%) |
| 5 Scale curve | about 58 | 141 / 65 | 1 (budget) | 3 | 1,058 (900, +17.6%) |
| 6 Mechanism | about 26 | 39 / 0 | 0 | 3 | 439 (400, +9.8%) |
| 7 Long term | about 47 | 88 / 66 | 1 | 4 | 738 (800, -7.8%) |
| 8 Shocks | about 56 | 137 / 95 | 2 (one is budget) | 3 | 921 (800, +15.1%) |
| 9 How sure | about 58 | 107 / 55 | 1 (budget) | 1 | 1,064 (900, +18.2%) |
| 10 Regions in depth | about 57 | 129 / 51 | 1 | 1 | 899 (1,000, -10%) |
| 11 Discussion | about 91 | 195 / 123 | 3 (one is budget) | 6 | 1,509 (1,300, +16.1%) |
| 12 Limitations and conclusions | about 45 | 83 / 0 | 0 | 3 | 733 (700, +4.7%) |

Every number I traced matched its register row, pending gate 4 value or csv cell at the printed precision. The pages I opened carried the cited statement in every case: Treasury 2021 p. 13; Treasury 2023 pp. 37, 39; Centre for Population 2025 p. 1; Davies pp. 149, 150, 153; Parr p. 16; McDonald p. 3; Summerhayes and Baker 2026 pp. 963-964, 2024 p. 1, 2025 p. 534; James and O'Neill pp. 183, 187; Lawrence and others pp. 30, 32; House committee p. iii; Hochman pp. 2071, 2078; Hughes 2022 p. 11; ABARES Snapshot pp. 5, 10; ABARES 2025 p. 2; Falster pp. 1, 6; Wittwer pp. 919, 932; Bolleter p. 123; Geoscience Australia and ABARE p. 331; Lane 2014 pp. 3, 193, 266; Zumkehr and Campbell p. 246; Peters p. 72; Kinnunen p. 229; Schreiber p. 9; Poore and Nemecek p. 990; Soliman Hunter PDF p. 11; Cottrell p. 135; Hughes 2017 p. 189; PMSEIC pp. 1, 15; Prosser p. 4; Sysak p. 416; Wiedemann 2015 pp. 111, 113; Wright and Cafiero p. S72; Productivity Commission 2023 pp. v, 3; DCCEEW 2017 pp. 3, 8; DCCEEW 2019 p. 3; Higgins 2018a p. 196; Higgins 2018b p. 341; Clapp p. 89; Beltran-Peña p. 4; Mcdougall p. 8. Every cited work is a literature register row. No em dash and no en dash appears in the three files; no American spelling was found. Tone (decision 33) holds: the remarks on other authors (Lawrence's missing base year, PMSEIC's unsourced 60 million) are the wording the scope and decision 46 prescribe.

## 4. Every fail, with its fix

**F1 (section 2).** "The corrected tier applies two corrections to the published method." The release record gives three method modules for `2011-fixed`: state-population-sum, biodiesel-yield and beef-carcase-yield (`results/releases.json`; `analysis/comparison_2025/README.md` line 51; ERRATA error 6). Fix: "The corrected tier applies two corrections to the published method, the biodiesel yield per tonne of oilseed (...) and the carcase-to-retail yield of beef (...), and for 2011 sets each state's population to the sum of its regions (ERRATA error 6), which moves the state ratios but no capacity." Footnote 1 ("computed before the two corrections") needs the same wording.

**F2 (section 7).** Table 6 is titled and introduced as what each long-term setting is worth ("Each setting was put back to its short-term value"), but it leaves out recycling, one of the settings the section names ("full recycling of food waste"). `analysis/paper_a/long_term_levers.csv`, release 2025-fixed, lever "recycling (0 to 1)", column `without` = 15,434,761. Fix: add the row "Recycling of food waste (0 to 1) | 15.4 | -1%".

**F3 (section 8).** "Bad wheat years are also partly correlated across Australia: ENSO and the Indian Ocean Dipole together explain 30 to 41% ..." Decision 51 and the scope (section 8 point 7) set the wording "partly correlated across the southern states"; section 11 already uses it. Fix: "Bad wheat years are also partly correlated across the southern states (Anderson 2019): ENSO and the Indian Ocean Dipole together explain 30 to 41% of wheat variability in Australia and East Africa."

**F4 (section 10).** "In both regions the largest short-term method effects are dairy on good land (+17.8% and +17.9%) and the beef carcase correction (-15.0%)." These are measured on the published base, `2025-mirror` (`analysis/paper_a/method_effects_by_region.csv`, 2025 short, Murray and Murrumbidgee - ACT), but the section says "All figures are on the corrected releases (2011-fixed and 2025-fixed)". This breaks the rule that the release is named at every figure. Fix: "...measured on the published base (2025-mirror, section 9): dairy on good land (+17.8% and +17.9%) and the beef carcase correction (-15.0%)", and change the opening sentence to "All figures except the method effects are on the corrected releases".

**F5 (section 11).** Section 11's measures table is numbered "Table 5", which is also section 7's long-term table, and the section's opening sentence refers to "(Table 5)". Fix: renumber the measures table (for example Table 9, with sections 9 and 10's tables brought into the same plain sequence) and update the reference in the opening paragraph.

**F6 (section 11).** "National drought policy has moved towards self-reliance and preparedness (Botterill 2021; Productivity Commission 2023, p. 3)." The Productivity Commission page carries the shift to self-reliance and preparedness. Botterill does not: his finding (L168) is that the principles of farmer self-reliance and risk management have stayed close to unchanged from the 1992 National Drought Policy to the 2018 Agreement. Fix: "The principles of farmer self-reliance and risk management have stood since the 1992 National Drought Policy (Botterill 2021), and the Future Drought Fund embodies a shift to supporting preparedness (Productivity Commission 2023, p. 3)."

**F7 (word budgets).** Four sections are more than 15% over the scope's budget: section 5, 1,058 words against 900 (+17.6%); section 9, 1,064 against 900 (+18.2%); section 11, 1,509 against 1,300 (+16.1%); section 8, 921 against 800 (+15.1%, one word over the limit of 920). Fix: cut to 1,035, 1,035, 1,495 and 920 words or fewer. Candidates: the five foodshed citations in 5.1, which could become two sentences; the repeat of the flip counts in 9.1, which section 3 already gives in full; and the repeat of the waste-scenario figures in 11.3, which section 8 already gives.

## 5. Sentences stronger than their evidence

1. Section 1.1: "Published estimates ... scatter widely, because they answer different questions by different methods." The scope says "mostly by definition", and the comparison sits in Paper B. Suggest "scatter widely, mostly because they answer different questions".
2. Section 1.4: "A regional capacity result answers the question a regional food plan would ask: which regions could feed their own people from their own land." No read source says regional food plans ask this. Suggest "could inform".
3. Section 1.3: "They left open how the picture changes over time, how robust the regional results are, and how the long term and shocks play out region by region." This is an assertion (scope section 1 gap 4: the citing works are unread). The drafter's notes say so, but the sentence reads as established.
4. Section 3: "The capital-city regions are over capacity in both years and both presets, except Murrumbidgee-ACT". Two sentences on, the paragraph says Swan's 2011 status cannot be used. Suggest "...in both years and both presets (Swan's 2011 status is a boundary artefact, below), except Murrumbidgee-ACT".
5. Section 4: "In the inland cropping regions the short-term gain is mostly livestock". This has no claim row (scope gap 2). In `capacity_by_cause_corrected.csv` livestock is 65% to 86% of the gain in Central West NSW, Lachlan, Namoi and the two Border Rivers regions, but 21% in Murrumbidgee - ACT, and it is negative in the Murray (-97,458 against a gain of 153,025). Suggest "In Central West NSW, Lachlan and Namoi most of the short-term gain is livestock".
6. Section 6: "pasture cannot grow crops (Lane 2014, p. 266)". Page 266 says cropping land can be used for pasture "but not necessarily vice-versa". Suggest "pasture is not necessarily fit for crops (Lane 2014, p. 266), and in the model it cannot carry them".
7. Section 6: "pasture-fed meat raises capacity until the pasture is used up, and lowers it once cropland is drawn into grazing." The register carries two grid points only (B216: 0% and 2.5% meat and eggs). The full diet grid has no claim row (scope section 6 gap 1).
8. Section 6: "In SA Arid Lands cropland binds at every diet tested". No claim row; it rests on `analysis/scale_curve_2025/README.md` only (the drafter notes this).
9. Section 7.3: "Northern Gulf, South West Qld and Lachlan also fed themselves." Northern Gulf carries a land-definition flag (A150 note: land_only_ratio 2.23). Name the flag.
10. Section 9.1: "The judgement ends drive most of the width of the ranges." The variance shares (81%, 36%, 52%) belong to the whole choices (the meat window, the resilience table). Only the equal chances, the 50/50 weight and the low ends are judgement. The scope words it this way, but the evidence shows choice-level shares. Suggest "The choices whose ends or weights rest on judgement drive most of the width".
11. Section 11.5: the Botterill attribution (F6).
12. Section 11.7: "Spreading production across states and varieties therefore lowers national variability." A321 supports states (the national factor is milder than four of six states). Nothing read supports "varieties". Suggest "Spreading production across states therefore lowers national variability".
13. Sentences quoted at the values of rows that are not yet checked (the values pass, but each sentence rests on a single unchecked route): A309, sections 3 and 9 (Mackay Whitsunday on `2011-improved`; `method_status.csv` has not been rerun after B90); A317, section 11.7 (the herd-cycle range; its second route is blocked); A129 and A132, section 12.2; A231, A232, A243 and A244, rows of section 11's measures table.

## 6. Wording issues (not fails)

* Section order: section 1 prints 1.1, 1.4, 1.5, 1.3, and section 11 prints 11.5 before 11.4. Both follow the outline labels (decision 45), but a printed paper should number in reading order and keep the labels in the claims csv. Murray to decide.
* Table numbering mixes a plain sequence (2 to 8) with section-decimal numbers (9.1, 9.2, 10.1); see also F5.
* Citation style: sections 1 to 4 write "Davies (2024)", while sections 5 to 12 write "Lane, Dawes and Grace 2015 found", "Hughes 2017 found", "Wiedemann and others 2015 give" with no parentheses. Multi-author works appear as surname only in sections 1 to 8 ("Hochman 2017") and as "and others" in sections 11 and 12. The same work is "Soliman Hunter 2021" in section 7 and "Soliman Hunter and Taylor 2021" in section 12. Two Grafton 2018 works are registered (L188, L189); the reference list needs 2018a and 2018b. Units are written both "km²" (sections 5 and 6) and "km2" (sections 10 and 11), and both "per cent" and "%".
* Section 3: "South Coast WA, Eyre Peninsula and Glenelg Hopkins are under capacity in both years". This is true in the short term only; Glenelg Hopkins is over capacity in the long term in both years (`movers.csv`). Add "in the short term".
* Section 5: the opening promises that "every regional sum below names its basis", but 5.2's sums (44% against 58%; NSW 17.6 against 25.3; SA 1.2 against 4.8; WA 2.0 against 5.1; 71%, 72%, 51%; 4.50 million km² unused) do not name it. Add "(state-yield basis)" once at the head of 5.2.
* Section 6 gives the flat cropland range as "10% to 100%" (A346's verified note); section 11 gives "10% to 99%" (A346's statement). Use one form.
* Section 7.3: "36 on the published method ... 36 on the improved method" names methods, not releases. Add `2025-mirror` and `2025-improved`.
* Section 7 Table 6: "Fibre need (23 to 11.5)" has no unit.
* Section 8.1 switches within one paragraph between capacity as a multiple (1.49, 1.11, 0.68) and people over capacity (1.12, 1.05). Both forms are allowed, but the paragraph should say which one each figure is, or keep to one.
* Sections 8 and 11 print different values for the same setting on the same release: liquid fuel 156 litres a person, short term 0% and long term +0.78% (Table 8, `scenarios_by_region.csv`), against +0.1% and +0.8% (section 11's table, `measures.csv`). Both are csv cells, but a reader will see two answers. One line should say why they differ, or one source should be used.
* Section 12: "Its climate scenarios scale field-crop yields only, not pasture." Section 8 says the drought allowance scales every yield. Suggest "Its named climate scenarios scale field-crop yields only; its drought allowance scales every yield by a grain-based factor that is untested for pasture."
* Section 12.2: Mcdougall's 15.0% is the expanded-land scenario (verges, vacant land and 25% of yards). Name it.
* Section 11.3 cites the DCCEEW web page as "n.d." although the page reads "Last updated: 19 December 2025"; section 1 cites L234 as "ABARES undated" although its file is named 2026. Register year fixes.

## 7. Claims csvs (opened after the prose checks)

* Coverage: every number in the prose of all twelve sections is matched by a fragment or locator in the drafters' claims csvs (script check with digit boundaries, shown above to catch a planted wrong value). No number is missing.
* `[open: Qn]`: not used in any prose sentence (the two occurrences are inside drafter notes). Correct, since decision 66 settled N-A1 to N-A10.
* `[gate 4]` use:
  * Inconsistent between files. `A_s01-04_claims.csv` flags A354 to A365 (section 4, Table 3, and the ratio convention in section 2) as [gate 4]. `A_s09-12_claims.csv` cites the same values in the conclusions (4.7, 4.2, 1.8, 2.6, 0.1 million; 0.670 to 0.665; 1.454 to 1.767) with no flag, and its notes say these rows "carry no [gate 4] flag". Decision 91 asks for a flag on a Tier A value awaiting gate 4, and decision 90's digest covers A354 to A365, so the flag belongs in both files.
  * A043 is flagged [gate 4] in section 3, but its status is "self-checked (B90)" with no pending value; the drafter explains why (its inputs A029 and A036 are pending). This is acceptable, but it is a flag on a row that does not itself await gate 4.
  * Pending values are flagged where they are printed: A029, A033, A034, A036, A164, A165, A196, A199, A205, A206, A219, A220, A223, A264 to A266. A few sentences cite a pending row only for a definition (A036 note for "5th to 95th percentile"; A029 for the 53-regions wording) and are unflagged, which is right.
* Register ids cited for sentences they do not support:
  * `A_s01-04_claims.csv` 1,49 ("has that changed since 2011") cites A331, which is the 60-zones row.
  * 2,18 ("The corrected tier applies two corrections") cites A332, which is the rule that 2011 appears as corrected only. It does not count the corrections, and the count is wrong (F1).
  * 3,23 ("In the long term four regions flip") cites A042 and A043. The row for four long-term flips is A035.
  * 1,46 ("what would a 100-year self-sufficiency plan ask of each region") cites A010 and A011, the national coverage shares, not anything regional.
* The `A_s01-04` notes give word counts close to mine (1,023, 591, 769, 514). The other two notes give none.

## 8. Other findings the brief did not ask about

* `papers/A_results/draft/paper_A_draft1.md` (91 KB, timestamped after the three section files) sits in the folder under test. The brief does not name it and I did not check it. If it is the assembled paper, it inherits every fix above.
* `analysis/paper_a/long_term_regions.csv` still carries North East Victoria's copied 2011 population (204,651); Table 5's 2011 cells (94%, 33%) come from it under the label `2011-fixed`, while section 2 says the regional 2011 results use `2011-fixed-2`. I recomputed with 98,604 and the regional-sum denominator (the one V33 used for A165): the long-term share stays at 93.8%, so the printed 94% holds. The label mismatch remains.
* `results/releases.json` shows `2025-store-1` and `2025-store-2` frozen and extending `2025-improved`. The draft uses only their resilience tables on `2025-fixed`, which agrees with `scenarios_by_region.csv` and `measures.csv`.

## 9. Register rows touched

None.

## 10. Overall verdict per section

| Section | Verdict |
|---|---|
| 1 Introduction | needs the listed fixes (stronger sentences 1 to 3; subsection order) |
| 2 Method and data | needs the listed fixes (F1) |
| 3 Short-term picture | needs the listed fixes (stronger sentence 4; Glenelg Hopkins wording) |
| 4 What drove the change | needs the listed fixes (stronger sentence 5; gate 4 flag consistency in the claims csv) |
| 5 Scale curve | needs the listed fixes (F7 budget; basis label in 5.2) |
| 6 Mechanism | needs the listed fixes (stronger sentences 6 to 8; range wording) |
| 7 Long term | needs the listed fixes (F2; release ids; Northern Gulf flag) |
| 8 Shocks | needs the listed fixes (F3; F7 budget; ratio wording; fuel 156 consistency) |
| 9 How sure | needs the listed fixes (F7 budget; stronger sentence 10) |
| 10 Regions in depth | needs the listed fixes (F4) |
| 11 Discussion | needs the listed fixes (F5; F6; F7 budget; stronger sentence 12; subsection order) |
| 12 Limitations and conclusions | needs the listed fixes (climate-scenario wording; Mcdougall scenario; unflagged gate 4 values in the claims csv) |

No section needs rework. Every number traced to its register row or csv cell. The fails are wording, release naming, one table omission, one table-number clash, one citation attribution and length.

## 11. Rerun

Scripts in the session scratch folder (`v34a/`): `reg.py ID...` (claims register lookup), `lit.py ID...` (literature register lookup), `pg.py PDF REGEX` (finds a phrase on each PDF page with its page label), `wc.py FILES` (prose word count per section), `nums.py` (number coverage against the claims csvs) and `nums_wrong.py` (the same, run on the copy with the planted wrong value). Run with `python3` from any folder.

## 12. Files read

The brief and `qa/briefs/_checker_rules_results_wave.md`; the three draft files and their claims csvs (the csvs only after the prose checks); `papers/A_results/SECTION_SCOPE.md` (header and sections 1 to 12); `qa/claims_register.csv`; `qa/literature_register.csv`; `qa/DECISIONS.md` (rows 33, 45, 46, 51, 66, 72, 86, 87, 90, 91); `results/releases.json`; `results/scale_curve.csv`; `results/method_effects.csv`; `analysis/comparison_2025/capacity_by_cause_corrected.csv`, `movers.csv` and `README.md`; `analysis/paper_a/regional_flips.csv`, `shocks_summary.csv`, `scenarios_by_region.csv`, `long_term_levers.csv`, `measures.csv`, `method_effects_summary.csv`, `method_effects_by_region.csv`, `method_status.csv`, `regions_in_depth.csv` and `README.md` (interaction line); `analysis/scale_curve_2025/README.md` and `analysis/pasture_2025/README.md` (lines found by search); `analysis/sensitivity_2025/README.md` (judgement-ends paragraph); `ERRATA.md` (errors 6 and 8); `qa/reports/V33_ne_vic_check.md` (line 47); `CITATION.cff`; and the literature PDFs named in section 3.
