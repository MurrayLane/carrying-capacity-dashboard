# B96a: the V34a check applied to the Paper A first draft

Builder under brief `qa/briefs/B96a_fix_draft_A.md`. Read first: `qa/reports/V34a_draft_check_A.md` in full. Files written: `papers/A_results/draft/A_s01-04.md`, `A_s05-08.md`, `A_s09-12.md`, their three `_claims.csv` files, and this report. Scratch scripts (sentence splitter, renumbering, flag sweep, word count, number coverage) are in the session scratch folder `b96a/`. No register row was touched. `paper_A_draft1.md` was not edited (it is not named in the brief), so it still carries the first-draft text.

## 1. Fixes applied

Line numbers are for the files as they now stand.

| Fix | What changed | File:line |
|---|---|---|
| F1 | Section 2 now reads "applies two corrections to the published method, the biodiesel yield ... and the carcase-to-retail yield of beef ..., and for 2011 sets each state's population to the sum of its regions (ERRATA error 6), which moves the state ratios but no capacity". Footnote 1 now says "computed before the two corrections to the method and before each 2011 state's population was set to the sum of its regions". | A_s01-04.md:37, :43 |
| F2 | Table 5 (was 6) has a new row, "Recycling of food waste (0 to 1) \| 15.4 \| -1%", from `long_term_levers.csv` (2025-fixed, zone 1, `without` 15,434,761, -1.2%). | A_s05-08.md:81 |
| F3 | The sentence now reads "partly correlated across the southern states (Anderson et al. 2019): ENSO and the Indian Ocean Dipole ...". | A_s05-08.md:153 |
| F4 | The section 10 opening now says "All figures except the method effects are on the corrected releases". The Murray sentence now says the method effects "are measured on the published base (2025-mirror, section 9)". | A_s09-12.md:51, :55 |
| F5 | The measures table is renumbered Table 11 (see item 4 below) and the opening reference now reads "(Table 11)". | A_s09-12.md:83, :127 |
| F6 | The Botterill sentence is replaced with the check's wording: Botterill for the unchanged principles since 1992, and the Productivity Commission (p. 3) for the shift to preparedness. | A_s09-12.md:105 |
| Stronger 1 | Now reads "scatter widely, mostly because they answer different questions". | A_s01-04.md:9 |
| Stronger 2 | Now reads "A regional capacity result could inform a regional food plan: ...". | A_s01-04.md:19 |
| Stronger 3 | The assertion "They left open ..." becomes "This paper takes up how the picture changes over time, ...; later work citing them was not checked." | A_s01-04.md:13 |
| Stronger 4 | Now reads "over capacity in both years and both presets (Swan's 2011 status is a boundary artefact, below), except Murrumbidgee-ACT". | A_s01-04.md:68 |
| Stronger 5 | Now reads "In Central West NSW, Lachlan and Namoi most of the short-term gain is livestock". A new sentence gives the regional split: 65% to 86% in Central West NSW, Lachlan, Namoi and the two Border Rivers regions; 21% in Murrumbidgee-ACT; in the Murray, -97,458 against a gain of 153,025. Every csv cell is in the claims csv. | A_s01-04.md:101 |
| Stronger 6 | Now reads "pasture is not necessarily fit for crops (Lane 2014, p. 266), and in the model it cannot carry them". | A_s05-08.md:42 |
| Stronger 7 | The rise-and-fall claim is gone. The text now reads "On the 2025 corrected release a little pasture-fed meat beats none: ..." and "The gain from a little meat therefore holds on the corrected release only", which is what B216 states. | A_s05-08.md:46 |
| Stronger 8 | "cropland binds at every diet tested" (no claim row) is gone. The sentence now restates A116: 326,000 km2 of pasture, 221 km2 of cropland, 41 thousand people on the state-yield basis. | A_s05-08.md:48 |
| Stronger 9 | Now reads "Northern Gulf (which carries a land-definition flag), South West Qld and Lachlan". | A_s05-08.md:94 |
| Stronger 10 | Now reads "The choices whose ends or weights rest on judgement drive most of the width of the ranges." | A_s09-12.md:13 |
| Stronger 11 | Fixed as F6. | A_s09-12.md:105 |
| Stronger 12 | "and varieties" is dropped. | A_s09-12.md:121 |
| Stronger 13 | No checked row exists for these values, so each sentence is marked "unchecked row" in the claims csv flag column: A309 (sections 3 and 9), A317 (section 11.7, and the release mention in section 2), A129 and A132 (12.2), and A231, A232, A243 and A244 (Table 11 rows, and the 12.3 sentence that uses A244). The same flag is added for A215 (Table 7 and the section 8 fuel sentence) and for A095 to A097 (Table 3 cells), which are also unverified. | claims csvs |
| Citation style | One style throughout: narrative "Author (Year, p. n)" and parenthetical "(Author Year, p. n)". "and others" no longer appears. Two authors are written "A and B" and three or more "A et al.". Author counts were taken from the PDFs on disk, for example Hochman et al., Hughes et al. 2022, Hughes and Lawson 2017, Falster et al., Wittwer and Waschik, Sysak and Beilin, Soliman Hunter and Taylor, Lane et al. 2014 and 2015, Lawrence et al. Bolleter, Botterill, Clapp and Ridoutt 2024 are single authors. In-text references to other works' tables now read "their Table 1" and "their Table 8.3". | all three files |
| Grafton | The cited work (L189, the irrigation paradox) is "Grafton et al. 2018b". The claims csv records that 2018a is L188 (Grafton and Wheeler), which the prose does not cite. | A_s09-12.md:167 |
| Units | "km²" is now "km2" (sections 5 and 6) and "per cent" is now "%" (sections 10 and 11). | A_s05-08.md; A_s09-12.md:53, :55, :115 |
| Glenelg Hopkins | Now reads "under capacity in both years in the short term" (`movers.csv` zone 18: over capacity in the long term in both years). | A_s01-04.md:68 |
| Yield basis 5.2 | 5.2 now opens "On the state-yield basis, the 53 regions lost ...". | A_s05-08.md:15 |
| Cropland range | Sections 6 and 11 both now say "10% to 99%" (A346's statement; the V31b note says the flat range is wider). | A_s05-08.md:42; A_s09-12.md:83 |
| Releases in 7.3 | The 36, 32, 36 counts now name 2025-mirror, 2025-fixed and 2025-improved. | A_s05-08.md:98 |
| Ratio convention 8.1 | The paragraph now opens "As a multiple of the population" for 1.49, 1.5, 1.11, 1.12, 0.68 and 0.69. The 1-in-20 figures are introduced "as a status ratio, people over capacity" (1.12, 1.05). | A_s05-08.md:108 |
| 156 litres | Both values are right; they set different things. The measure (`measures.csv`, `long_term_and_measures.mjs` line 61) sets 156 litres in both terms, so it moves the short term by +0.1%. The named scenario (`scenarios/scenarios.json` fuel-ev-156) sets it in the long term only, so its short term is 0%. In the long term they agree: +0.78% is +0.8% at one decimal. This is said in the Table 11 caption, and the Table 7 caption points to it. | A_s09-12.md:127; A_s05-08.md:135 |
| Section 12 climate | Now reads "Its named climate scenarios scale field-crop yields only; its drought allowance scales every yield by a grain-based factor that is untested for pasture." | A_s09-12.md:155 |
| Mcdougall | Now names the 25% land-use scenario: "street verges and vacant land" added to "a quarter of yard space" (p. 8, Table 4; scenario as described in the abstract). | A_s09-12.md:163 |
| Subsection order | Section 1 now runs 1.1, 1.3, 1.4, 1.5 and section 11 runs 11.4 before 11.5. Text blocks were moved whole and the labels kept. One pointer was added: "(+60%, section 11.5)". | A_s01-04.md:3-21; A_s09-12.md:97, :103 |
| Table numbers | Tables now run 1 to 11 in one plain sequence: flips 1, decomposition 2, scale curve 3, long term 4, levers 5, shocks 6, scenarios 7, method effects 8, method status 9, regions in depth 10, measures 11. The bold "Table 9.1." style is gone. Every in-text reference was updated. Figures 1 to 8 and S1 were already sequential. | all three files |
| Gate 4 flags | [gate 4] is now on every claims row that uses a pending value or A354 to A365, in all three csvs. Rows that cite a pending row only through its note or statement (a definition) stay unflagged, as V34a advised. A043's flag is kept, with its reason written in the flag column. | claims csvs |
| Register ids | 1,49 now cites A017 (SA2 share 40% to 37%: "has that changed since 2011"; the row now has sentence number 30). 2,18 now cites `results/releases.json` modules plus `comparison_2025/README.md` line 51 and ERRATA error 6, since no claim row counts the corrections. 3,23 now cites A035. 1,46 now cites A031, A032 and A147 (regional long-term rows; it now has sentence number 27). | A_s01-04_claims.csv |
| Drafter notes | A one-line B96a note at the head of each notes block says that the first-draft table numbers, order and sentence numbers in those notes are historical. | each .md |

Not applied, because they are register-side or outside the brief: the register year fixes for the DCCEEW page ("n.d.") and L234 ("ABARES undated"); the fibre-need unit in Table 5 (the brief does not list it, and no unit is in hand).

## 2. Sentences cut, and word counts

Word counts are prose only. "Checker count" is the V34a `wc.py` count, which also counts bold captions and the supplementary figure placeholder. "Prose count" leaves those out.

| Section | Budget, limit | Before (checker / prose) | After (checker / prose) |
|---|---|---|---|
| 5 | 900, 1,035 | 1,058 / 1,025 | 1,026 / 993 |
| 8 | 800, 920 | 921 / 921 | 896 / 896 |
| 9 | 900, 1,035 | 1,064 / 992 | 950 / 950 |
| 11 | 1,300, 1,495 | 1,509 / 1,465 | 1,468 / 1,468 |

Every other section is within 15% of its budget: section 1 at 1,032 (limit 1,035), section 4 at 566 (575), section 6 at 449 (460), section 12 at 769 (805).

Sentences cut:

* **Section 5:**
  * "New York State could supply 34% of its food needs within an average distance of 49 km (Peters 2009, p. 72)."
  * "Worldwide, 11 to 28% of people could meet their demand for a single crop type within 100 km (Kinnunen 2020, p. 229)." Section 12.1 keeps this figure.
* **Section 8:**
  * "Some statuses hang on a hair: the population of North Tasmania was 1.000 times its capacity at 1 in 10 in 2025." Section 10 keeps this figure.
  * "The store sizes are the model's own scenarios." Section 11.4 keeps this point.
* **Section 9:**
  * "In the short term eight regions changed status between 2011 and 2025 on the corrected method: seven from over to under capacity and one from under to over." Section 3 gives this.
  * "Three others are land-definition artefacts: Desert Channels, Southern Gulf and SA Arid Lands." Section 3 gives this.
  * "In the long term four regions changed status, all from over to under capacity." and "One, South West Queensland, passes every test." Both were merged into "Of the four long-term flips, three carry an artefact flag and two are not robust to the range; one, South West Queensland, passes every test."
* **Section 11:**
  * "The waste scenario of section 8, rerun on 2025-fixed, gives the same result."

No number the scope's content lists require was cut.

## 3. Claims csv rows changed

* **Renumbering.** Sentence numbers were recomputed in all three csvs after the reorders and cuts (about 350 rows), and rows are sorted within each section. In `A_s05-08_claims.csv`, whose fragments are whole sentences, each fragment was rewritten to the new sentence. A check script finds every numbered fragment of `A_s01-04` (131 rows) and `A_s05-08` (199 rows) at its recorded sentence number.
* **Dropped rows (cut sentences):**
  * section 5: Peters, Kinnunen;
  * section 8: the North Tasmania 1.000 row (A343) and the store-sizes row (decision 48);
  * section 9: the "eight regions changed status" row (A034) and the land-definition artefacts row (A037);
  * section 11: the waste repeat row.
* **Merged rows:**
  * 6,13 (B216, two rows into one);
  * 8,6 (A163/A179, A167/A183/A014 and A175/A191/A195 into one row);
  * the long-term flip rows of 9,17.
* **Added rows:**
  * 1,15; 1,23; 1,42;
  * 2,18: two rows (beef carcase sources; ERRATA error 6);
  * 3,31 (A065, A052); 3,36 (Glenelg Hopkins, `movers.csv`);
  * 4,21 and 4,22: four rows (the regional livestock split, with every csv cell);
  * 7,39 (recycling lever cell); 7,52 (A150 flag note);
  * 9,24 (item 10); 10,3 (F4);
  * 11,72 (A321, states only); 12,4 (climate wording).
* **Changed rows:**
  * the four misattributed ids;
  * F1 rows 2,18 and 2,35;
  * 4,6 and other citation-style fragments;
  * 5,21; 6,3; 6,5; 6,16; 7,66;
  * 8,7; 8,49 (fuel note); 8,63 (decision 51);
  * 9,15; 9,30; 10,12; 10,18; 10,19; 10,28;
  * 11,34; 11,43 (F6); 11,64; the Table 11 caption row (156-litre reconciliation);
  * 12,18 (Mcdougall); 12,22 (Grafton 2018b);
  * the two "9-12, all" rows (table numbers; citation style and Grafton a/b);
  * every table caption fragment and table label (renumbered).
* **Flags added:**
  * [gate 4] on: Table 1 rows "Long term 36" and "Long term 32" (A033); 8,8 and 8,9 (A196); 8,27 and 8,29 (A199); 12,30 (A354 to A362); 12,31 (A363, A364); 12,4 (A223 note);
  * reasons written beside existing flags at 3,8 (A043), 4,5, 10,38 and 10,39;
  * "unchecked row" on the rows listed under stronger 13.

## 4. Checks before finishing

* **Em and en dashes:** none in the three files.
* **Number coverage:** V34a's script (digit boundaries) finds every prose number in the claims csvs. No number is missing in any of the three files. Caption numbers are in their caption rows.
* **Table and figure references:** Tables 1 to 11 each have a caption and at least one in-text reference. Table S1 stays in the supporting information. Figures 1 to 8 and Supplementary Figure S1 resolve.
* **Header rules:**
  * Release named: the method effects in section 10 now name 2025-mirror, and 7.3 names its three releases.
  * Ratio convention: 8.1 names each figure's form.
  * Yield basis: named at the head of 5.2, and the other regional sums already named theirs.
  * "53 regions (52 NRM regions and the Northern Territory)" is the first use in every section that uses the count (2, 3, 4, 5, 7, 8, 9, 10, 11).

## 5. Wrong-value check

Example only, made on copies in scratch (`b96a/wrong2/`); nothing in the repository was changed by it. As a deliberate wrong fix, I changed the new item 5 sentence from "livestock carried 65% to 86%" to "65% to 88%" in a copy of `A_s01-04.md`. The number-coverage script then reported `('4', '88')` as missing, while the real files report nothing missing. Against the csv, 88% fails: Border Rvs Maranoa-Balonne is 316,661 / 369,886 = 85.6%, the top of the range. The check can therefore catch a wrong value introduced by a fix.
