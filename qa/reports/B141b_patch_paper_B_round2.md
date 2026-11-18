# B141b: Paper B patched to the second-round response (decisions 141 to 148)

Brief: `qa/briefs/B141b_patch_paper_B_round2.md`, with two additions from the coordinator: the ten-year window figures are cited "B139, checked V53" and its sentence carries the proxy caveat; the bridge diet term is 22.6 million (csv -22.65). No git, no subagents, no network. Written only under `papers/B_methods/` and this report. `paper_B_draft1.md`, `references.md`, every register and `analysis/` are untouched.

## Word counts

* Main text: 7,916 words by `qa/tools/wordcount.py B` on a scratch copy after `assemble_draft.py B` (cap 7,950). Before the patch: 7,916 (sections 1 to 9: 673, 519, 306, 912, 2,691, 1,344, 592, 500, 379).
* Abstract: 250 words (cap 250). Highlights: five, 76, 84, 82, 77 and 77 characters (cap 85). No em dash in any file written.
* The patch added about 1,150 words of prose; about 1,150 were cut from section 4 (families), 5.1 to 5.13, 6.1 to 6.9, 7, 9.1 and 9.5, and the detail moved to the supplement (S1, S2, S3.12, S8) so that nothing is lost. Section 9.5 (about 85 words) is removed and merged into `B_s10_declarations.md`.

## Changed files

* `papers/B_methods/draft/B_s01-03.md`, `B_s04-05.md`, `B_s06-09.md` (prose, Tables 3 to 9, drafter notes)
* `papers/B_methods/draft/B_s01-03_claims.csv`, `B_s04-05_claims.csv`, `B_s06-09_claims.csv`, `supplementary_claims.csv` (new rows flagged "B141b"; superseded fragments flagged)
* `papers/B_methods/draft/supplementary.md` (S1, S2.1, S2.4, S2.5, S2.7 to S2.10, S3 opening, S3.1, S3.4 with Table S10, S3.6, S3.11 with Tables S13 and S14, S3.12 rewritten with the bridge, S3.13 with Table S11, S3.14 with Table S12, S4, S5, S6, S7, S8; Tables S5 and S8 corrected)
* `papers/B_methods/draft/highlights.md`, `B_s10_declarations.md`
* `papers/B_methods/SECTION_SCOPE.md`, `OUTLINE.md` (one B141b note appended to each)
* `qa/reports/B141b_patch_paper_B_round2.md` (this report)

## 1. Drought bound (decisions 141, 146)

Sources: B134 with V49 (and its overclaim notes, all taken).

* Abstract: "Weather and waste take the model from 18.9 to 55.3 million" becomes "One at a time, a weather allowance for the worst year in 100 lowers the model from 41.5 to 18.9 million (40.4 on crops only) and removing avoidable waste raises it to 55.3; across the settings varied together it moves 1.58-fold (5th to 95th percentile)." Highlight 5: "One at a time, weather gives 18.9 million (40.4 on crops only), no waste 55.3".
* 5.8 Test: before, "at 1 in 10 it is 30.8 million, 26% lower, and at 1 in 100 it is 18.9 million, 54% lower. At the 2025 population the failure probability is 5.8 to 6.1% a year ... The Jones committee's 30 to 35 million ... is of the size of the model's 30.8"; after, the model's rule and the crop-only figures (41.2 and 40.4) side by side, "short-term failure probability is 5.8 to 6.1% a year with the factor on every yield ... and below 1% on crops alone", the untested pasture factor named, and the Jones sentence cut (kept in 6.6, Mod minor 10).
* 6.6, 6.10, 6.11, 9.2, Table 3, Table 4 note, Table 5, Table 8 (crop-only row 1.03 first in panel A), Table 9 purpose 1 ("for crops; not tested on pasture-fed output"), 7.2, 7.6, 8.1 carry the companion. 18.9 with 40.4, the factor 2.19 with 1.03, 5.8 to 6.1% with "below 1%".
* "97%": not used in the main text. 6.6 says "almost all of the fall" (short term); S3.6 gives 93% to 98% by how the pasture rows are separated and about half in the long term at 1 in 100 (V49).
* S5: pasture-fed meat output is set by national meat output; window 0.24 (0.21 to 0.27) and 0.14 (0.12 to 0.16), calibration 0.03 (0.02 to 0.04) and 0.01 (0.01 to 0.02) drawn; dairy and wool series not varied; plus or minus 20% moves capacity 33.4 to 49.5 million, "an illustration at 20% either way, not a bound" (V49); the undrawn list names "the deviation of national pasture output from the observed meat series" so the count of 23 holds. PAL: 1.4 to 1.8 spans 41.5 to 32.7 (1.27), NHMRC 1.2 to 2.2 spans 48.0 to 26.9 (1.78). 6.9 carries the pasture sentence; the PAL ends are in S5 and Table 8.

## 2. Shares as ranges (decision 142)

Sources: B135 with V50 (the appendix amendments and V50's overstatement notes, all taken).

* Abstract s5, before "equalising closed 4.1% ... 38.5% ... narrowed that spread by about a third"; after "-1% to 8% across references ... 28% to 46%, most of it the footprint and HALF". Highlight 2 carries the classification: "If productivity is an input, footprint and HALF close most of their gap to the model".
* 5.11 and Table 6 lead with the reference-free rows; line (a) "-1% to 8% across references from 31.1 to 53.6 million, each method left out, the fish reading dropped and other variants: about none throughout" (4.1% as the base case); line (b) "28% to 46% across the variants, and 5% to 36% of the distance to the median of the centres (9% to 36% without the combined land scale-up variant)"; "mostly (about 87%) the productivity conversion of the footprint and HALF"; the narrowing "with it left out the spread widens by 12%, and with any other single method left out it narrows by 23% to 48%". Table S13 (new) holds the robustness table.
* Line (b) is the footprint's own accounting and line (a) a counterfactual ("Australia's physical hectares divided by a per-person footprint in world-average hectares", V50's wording); the algebra is one sentence (4.29, 2.06 and 2.47 for build 1); the binding-land-type reading 53.9 to 77.9 million is in 5.10, 5.14 and Table 3, with 1.30 to 1.88 times the model and the pooled 64.8 to 117.0 in Table S8; the pasture is a smaller surplus (S3.11, V50's correction of "shortfall").
* World-average range: the energy balance has no world-average reading, so the abstract, 5.10, 7.6, Table S8 read 146 to 343 million (3.5 to 8 times), not 134 to 343 (R05b issue 1, EE minor 1).

## 3. Line (c) and the bridge (decision 144)

Sources: B139 with V53.

* Line (c) in 5.11, Table 6 (new block), the abstract, 9.1 and S3.11 (Tables S13 and S14): 14.7% of the distance to the model, 20% to the median, spread narrowing 26% (0.65 to 0.48), "less than on line (b)"; band 10% to 16%; grain exception (1.10); loss factors on the food balance mix; 8.0 against 7.376 MJ stated (Table 7 note and S3.11).
* The bridge (5.14, Table 7 panel B, S3.12): seven switches, G1 averages diet -22.6, pasture-fed yield -13.0, cropland yield -6.4, land pool -6.3, non-food land -4.4, waste -17.9, requirement +36.2; one decomposition at a time (the six-switch figures are in S3.12 only). Before: "what remains above the model is consistent with a feature that the model carries"; after: "The pairing is a sufficient cause of the gap, not shown to be the only one", the pool 18% of the gap on HALF's own pooling and 60% of a larger gap with energy substitution, the protein-held variant 85.4 (dairy allowed only to fall; 92.4 if it may rise, S3.12). Variant 1 is described as "inside the footprint's pooled span of 64.8 to 84.6 and above HALF's 76.0", not "93% of the way".
* Table 8 in three panels from `design_choices_panels.csv`: the ladder dropped (6.10, Figure 3, 6.11 without the 2.22 sentence); bundles (Australian settings, time frame), the upper bound (diet C) and the Monte Carlo marked; diets A and B ranked; the L035 Gifford 40.5 to 70 Mha row flagged as unverified in the register.
* Window and production comparison: 5.1 (two sentences), S3.13 with Table S11, S3.14 with Table S12. The window sentence, as V53 requires and the coordinator added: FAOSTAT 2021 to 2023 is a proxy for the model's own windows (meat 2020-21 to 2024-25, with a record 2024-25 cattle year), so the +6% (44.1 million, +6.3%) is "an upper indication and not a measured effect"; it does not say the livestock window decides it. Ten-year figures (+20.8% crop production, +7.3% yield, -0.4% livestock; 44.13; outside years 40.73) are cited "B139, checked V53" in the claims rows.

## 4. The model's roles (decision 143)

Table 9 recast as the author's judgement with a blind second rating by an AI checker session; one model column (the land-and-diet balance), the failure view's four ratings in the caption and not counted as a method; the second rating disclosed on the seven-column version (25 of 28 cells; three differences adopted); "No outside person has rated the table ... the table is not offered as a finding"; the abstract has no Table 9 finding ("Section 7 gives the author's judgement of method fit by purpose"). 7.6 reads "In the author's ratings no single method serves all four purposes". The HALF and Cassidy authors: 5.2 keeps "The authors were not consulted"; the contact in progress is for the response letter only, as decision 143 and the brief say. S7 says the purpose definitions are the second rater's and match the model's frame.

## 5. Keywords and the mirror row

Keywords confirmed (decision 129): carrying capacity; food security; land use; Australia; method comparison; ecological footprint; sensitivity analysis (seven). Mirror row: the 13-setting range is dropped from Table 4, because the row reads better beside the 19- and 18-setting rows without it; the range stays in Table S3 and S5 says it was not rerun. Table 4's note says so.

## 6. Minor issues (R05b (e))

Worked:
* Readings: world-average range starts at 146 (5.10, abstract, 7.6, Table S8; energy balance out of the secondary group); 211 noted as 1990-91 land (5.10, S3.1); Foran and Poldy's 30 to 32 and 76 to 80 against 40 and 41 (5.7); people per hectare in one table (Table S10); 2011 land against 2021-23 land (5.12); Simpson's 1.758 ha and Wackernagel et al.'s 9.0 and 14.0 ha beside Table S2 (S4); "release land" reworded (6.7).
* Captions: regeneration notes removed from Tables 3, 4, 8 and S5 (R05b checked that the csv files were regenerated); Table 5's "(p. 78)" moved to the caption.
* Span: highlight 1 and the abstract say both ends are soft.
* Model detail: diet C an upper bound (6.5, Table 8, with 0.06 and 0.13 ha); the 2.22 sentence dropped; pasture per person between guideline diets (S4: not proportional, the cause not traced, red-meat share a candidate not checked).
* Wording: 6 opens in the present tense; one competing-interests statement (9.5 merged into the declaration); MJ with kcal in brackets at 4.6, 4.10, 5.1, 5.6, 6.1; "the model" in place of "the balance" in section 7; "the model, failure view" in Tables 3, 5, S5; Kinnunen's six crop types named (8.2); the Jones framing kept in 6.6 and cut from 5.8; the abstract at the 250 cap (the new findings displaced older numbers).
* References: Gerten 2020 and Fader 2013 cited directly (S2.4, S2.9, S8); Buzby 2010 replaced in 8.5 by Muth et al. 2011 and Lane 2014 pp. 201 to 202.

Stands, with reason:
* Counts by route (EE minor 16, Mod minor 12): no csv holds the selection record; R05b assigns it to a separate job.
* Table 2 and Figures 1 to 3: placeholders, figures job under decision 99.
* AI declaration model names, CRediT name, DOI: Murray (decisions 120, 131).
* Mod's alternative span ("10 to 110"): amends decision 118, Murray's.
* Waste factor 1.33 against a 1.14 ceiling (Mod minor 2): needs a small check of the mechanism; no record explains it; left as a decision row.
* Units: kcal remain in Table 1, the supplement tables and S3.1 where the sources print kcal.
* The S3 readings table (R05b group 1) is met in part: Table S10 for people per hectare, Tables 3, 5 and S5 for the rest.
* R05b issue 11's "same choices in other methods" table and the van den Bergh and Rietveld 2004 link in the introduction: not in this brief; the word cap leaves no room for the second.

## 7. Literature

Cited directly where the text already makes the point (both are on disk, in `references.md` and marked read by B119): Gerten et al. 2020 (L083; S2.9, 3.4 and 10.2 billion people) and Fader et al. 2013 (L105; S2.4 and S8). Not cited, because they are not on disk and not in the register or are marked fetched but not read: van den Bergh and Verbruggen 1999, Fiala 2008, Kitzes et al. 2009 (two papers) and Arrow et al. 1995 (no file, no register row); Borucke 2013 (L125, record only); Mottet 2017 (L122, record only); Porkka 2013 (L255) and Alexander et al. 2017 (L256), fetched not read and "not cited" in the register; Kummu 2012, Monfreda 2004 or 2008, Pradhan 2014, Daily and Ehrlich 1992 and Kastner's trade-embodied land (no file). Listed for the register job and for Murray's fetch.

References to add: none. References uncited in the paper and supplement: Beltran-Peña, Rosa and D'Odorico 2020 (L182, the route to Gerten before the direct citation). Reference-list items to fix by the register job: "Buzby, 2010 (cited in Lane, 2014)" (printed in the generated Tables S3a and S5; L068 is unidentified), the "[CHECK]" notes on Wackernagel 1994 and Wackernagel and Rees 1996.

## 8. Numbers, with their report and checker

| Figure in the paper | Report | Checker |
|---|---|---|
| 41.2, 41.0, 40.4 (crops only); 41.4, 40.8; 24.7 long term; 1.03; below 1% a year; 5.8 to 6.1% | B134 | V49 (41.192, 40.988, 40.450; 24.682; 1.026) |
| 0.8% and 2.5% lower (crops only) | B134 | V49 (arithmetic from the above) |
| 93% to 98%; about half in the long term | V49 | V49 (B134's 97% and 95% amended) |
| 33.4 and 49.5 (plus or minus 20%); 0.24, 0.14, 0.03, 0.01 | B134 | V49 (33.431, 49.467; 0.2413, 0.1413, 0.0337, 0.0141) |
| 48.0, 26.9, 41.5 to 32.7, 1.27, 1.78; improved 61.8 and 35.2 | B134 | V49 |
| Improved crop-only 53.2, 52.0 (approximate) | B134 | V49 (53.15, 51.99; rule differs 0.1% to 0.4%) |
| -1.1% to 6.8%, -1.2% to 7.8%; 27.7% to 45.9%, 23.2% to 52.8%; 5.4% to 35.5% (9.4% without); 10.5%; 8.2%; 22% to 48% narrowing; widens 11.5% | B135 (appendix) | V50 |
| 4.29, 2.06, 2.47; 4.47, 2.97, 3.23; 53.9 to 77.9; 1.30 to 1.88; 1.01 to 1.45; 64.8 to 117.0 | B135 | V50 |
| about 87% | V50 | V50 |
| Line (c): 14.7%, 20.0%, 26.2% (0.65 to 0.48), 16.4%, 10.1% to 11.7%, 21.0%, 20.7%; 1.512; 0.8202; 1.10 | B139 | V53 |
| Line (c) shares to the geometric mean (20.7%, 21.7% for c3), c2 and c3 median shares, the 303 kg, the 1,912 and 2,892 kcal | B139 | not reproduced by V53 |
| Bridge averages, 34.46, 75.97, 41.50, 18%, 60%, 113.6, 85.4 (84.9, 86.2), 92.4; six-switch figures | B139 | V53 (builder's switch definitions; diet -22.64 against csv -22.65) |
| Table 8 panels A and B (1.03 to 3.77; 2.41; 1.64 to 2.50; 1.11, 1.30; 4.43, 6.36; footprint ratios) | B139 | V53 |
| Table 8 panel C (eleven factors) | B139 | V53 against the register; the 1.73 row unverified (flagged) |
| Production comparison: field crops 0.00018%, fruit and vegetables 13.12% and 59.17%, milk 0.09% to 3.52% | B139 | V53 |
| Land 0.00 Mha, wool 2.8%, meat calibrations 1.086 and 1.155, 7.6% and 21.8% | B139 | not reproduced by V53 |
| Ten-year window: +20.8%, +7.3%, -0.4%; 44.13 (+6.3%); 41.40; 44.25; 40.73 (-1.9%); +27.2%, +14.1%, +8.7%; factors; by item | B139 appendix | V53 appendix (follow-up) |
| 3.00 Mt against 2.26 and 2.01 Mt; "record 2024-25" | V53 | V53's wording; not a checked series maximum (FAOSTAT's ten-year beef maximum was not checked) |
| 146 to 343, 3.5 to 8 times (3.52, 8.27) | Table S8 (B046) | the checks that passed B046; arithmetic |
| 17.3% and 38.2% (raster); 10.7 MJ (2,550 kcal), 8.8 MJ (2,100 kcal) | sensitivity README; arithmetic at 4.184 kJ per kcal | not in this wave's reports |

## 9. Claim rows the register job must change or add

Change (values per the builder report and its checker):
* B003 (18.9 to 55.3): two separate one-at-a-time changes from 41.5; 18.9 (40.4 on crops only) and 55.3; the crop-only span is 40.4 to 55.3. B001, B137 gain 40.4 (40.45). B096 gains 41.2. B130 gains "short term" and "below 1% a year on crops alone". B167 gains 1.03. B134 gains 0.8% and 2.5%. B157, B198, B199, B218, B224, B230 gain crop-only companions; B138, B245, B226 hold only with the factor on every yield.
* B276: line (a) -1% to 8% across references (4.1% base case); line (b) 28% to 46% (38.5% base case); to the median 5% to 36% (9% to 36% without the combined variant); line (c) 14.7% with the 10% to 16% band. B277: spread of centres, the commodity-balance dependence (widens 11.5%; 23% to 48% otherwise), line (c) 0.65 to 0.48 (26%), 6.2 to 4.1.
* B156 and B046 (world-average range 146 to 343, 3.5 to 8 times, energy balance out of the group); B270 gains the ratios and the binding reading beside the pooled one; B247 cause clause rewritten from the bridge (pairing a sufficient cause and one of several); B182 (diet C an upper bound; A 1.60 and B 3.77 new); B185 and B186 (ratios between methods, Panel B); B194, B188, B243, B333, B364 (Panel A order: 1.03, 1.09, 1.17, 1.27, 1.33, 1.48, 1.60, 1.76 to 1.78, 2.14, 2.19, 2.67, 3.77; bundles and diet C outside); B238 (Table 9 purpose 1, "for crops"); B369, B371 (PAL ends); B262, B374 (the production comparison behind 363.5 Mha); the abstract data-claim row ("abstract, 2").
* B333 and B194 also drop "land mattered least"; B185 and B186 no longer sit in an ordered table of model runs.
New rows (Tier B proposals, already entered with the flag "B141b" in the claims csvs): the 22 supplement rows and the 66 main-text rows listed there, among them line (c) cells, the bridge G1 to G4 averages, the protein-held 85.4, Panel C's eleven factors, the production comparison rows, the ten-year window rows and the S5 Sobol and plus-or-minus-20% rows.

## 10. Flags for the coordinator

* Table 7 panel B (the bridge) and Table 6's line (c) block share the existing table numbers, so Tables 8 and 9 keep the numbers the decisions use.
* "Record 2024-25 cattle year" follows V53; no checked report states that 3.00 Mt is a series maximum.
* The 5.1 window sentence is short; the full sentence with the caveat is in S3.14.
* Tables S3a and S5 are generated from csv files and print "Buzby 2010".
* `numbers_lint.py` was run on the four files (output kept in the scratch folder, outside the repository); it does not recognise derived figures, so the table above is the check.

## Wrong-value check

EXAMPLE only, not for use: "Equalising closes 4% to 36% of the distance to the median of the method centres on line (b)." This uses the builder's unamended B135 low end (4.1%, from its superseded land scale-up variant) and is caught against V50, which rebuilt that variant and found 5.4% (`harmonised_robustness.csv`, combined scale-up variant, line (b), median of method centres: 0.054), so the sentence in the paper reads "5% to 36% (9% to 36% without the combined land scale-up variant)".

Register rows touched: none.
