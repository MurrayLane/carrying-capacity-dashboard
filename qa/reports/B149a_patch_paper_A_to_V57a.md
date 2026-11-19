# B149a: Paper A and its letter patched to the final read V57a

Builder report. Brief: `qa/briefs/B149a_patch_paper_A_to_V57a.md`. Input: `qa/reports/V57a_final_read_paper_A.md`. No register, reference list, paper assembly file or analysis script was edited. The gate 6 approval is pending: the keyword count (7) and the A317 range are left as they were (see F10). No numbers were recomputed; every new figure is a figure from a checked report, and each has a row in the claims csvs (rows marked "B149a").

Files changed (all under `papers/A_results/` unless named):
`draft/A_s01-04.md`, `draft/A_s05-08.md`, `draft/A_s09-12.md`, the three matching `_claims.csv`, `draft/highlights.md`, `draft/highlights_claims.csv`, `draft/A_s13_declarations.md`, `draft/A_s13_declarations_claims.csv`, `draft/acknowledgements_and_statements.md` (not in the brief's list but it carried the same "register row" sentence), `draft/supplementary.md`, `draft/supplementary_claims.csv`, `response_letter_round2.md`, `OUTLINE.md`, `SECTION_SCOPE.md`, `analysis/figures_2025/paper_A/figures.csv` (Figure 4 caption cell only), and this report.
Not touched: `paper_A_draft1.md`, `paper_A_submission.md`, `references.md`, `qa/` registers, any script.

## 1. The 16 fails, in order

**F1 Abstract, fuel direction. Fixed.** Abstract says only the weather setting explains the shortfall (34.3 million without it) and low fuel raises capacity. Section 7.1 says the weather setting lowers the figure and the low-fuel setting raises it. Highlight 4 reads "weather lowers it, fuel raises it". Letter answer 10 matches.

**F2 Abstract, paired draws. Fixed.** Abstract: the 2,000 paired draws are on the seven shared choices and give higher short-term capacity in 2025; the 26% long-term fall appears once the 2025-only choices are drawn. Section 9.1 says the same (26% "once the 2025-only choices are drawn", none on the shared choices alone). Letter 3.4 and the opening paragraph match.

**F3 Section 8.1 weather-record variants. Fixed.** 8.1 names both methods: 29.2 to 31.6 million on the model's table method (above the population in every variant) and 27.4 to 29.1 million on the leave-one-out reference (one variant, area-weighted from 1990-91, 0.6% below). Table S13's note says the same. Letter 3.5 and the third-round answer say the same.

**F4 Letter misquotes. Fixed.** Second referee 3 quotes "Short-term capacity is therefore close to a statement of how far meat production covers meat eaten, at the herd and diet of each year." Point 7 quotes "not as the NRM regions of 2025." Point 3.4 says the abstract's second sentence begins "At fixed settings" (it is the second sentence of the new abstract).

**F5 Letter false claims. Fixed.** Climate phase: the letter says the note to Table 1 labels it. Word count: 7,934 (abstract 248). Workflow language: out of the supplement (see F9); the letter's statement is true. "Box" is "paragraph". Point 3.2's broken sentence mended. The manuscript line is the paper's title without "Paper A". The "Draft for the author. Not sent." line is left for the author to remove on sending.

**F6 Shared choices named. Fixed, with a correction to V57a's suggested sentence.** Supplementary Section S4 gains Table S17, the 19 choices with the seven both years share marked, the 12 that are 2025 only, and how the pairing treats each (from the B133 report). V57a's sentence ("the seven drawn for both years, the six drawn for 2025 only, and the one fixed") sums to 14; the right split is 7 shared, 11 that vary for 2025 only, 1 fixed (the long-term feeding benchmark): 19. Section 9.1 points to the list; section 2 points to S4 as well. S4's "The 13 are as follows" is "the choices of Table S17 less the six added below".

**F7 Supplementary Figure S1. Kept, with a caption row in the supplement.** The placeholder line is replaced by a full caption that states the image resolution (1,100 by 1,021 pixels at 170 dpi, lower than the other figures) and names the file in S11 (`analysis/regionalise_2025/ideal_K53_cap650k.png`). I could not add a `figures.csv` row or copy the image (outside my write scope): listed for the figures job (section 4).

**F8 "Robust". Fixed.** Section 3 "clean and robust on 13 choices" is "clean and inside the range on 13 choices". Section 9.2 and conclusion 4 say the short-term count of regions over capacity moves by one region at most with the method tier (15, 16, 15) and the long-term count by four (36, 32, 36). Remaining uses of "robust" are all on the full set of 19 choices.

**F9 Internal labels. Fixed except as noted.**
* Declarations (`A_s13_declarations.md`, `acknowledgements_and_statements.md`): "every number and figure was checked by an independent re-derivation"; "draft text from my outline and the checked results". `papers/DECLARATIONS.md` (the source of both) needs the same two edits.
* Supplement: no backticked path and no release code remains outside S11 (grep: none). Captions read "the corrected 2025 release", "the scale-curve table named in Section S11" and so on. S11 gains the source file for each supplementary table, the panel-name key for Figure S6 (the scenario ids), a release key that defines "organic", "store-1" and "store-2" and "release chain", and a note that S11 is the only place with codes and paths. The supplement's title line no longer says "Paper A". "Fetch for the author" (Table S11 three times, S10 once) is gone, as are "Built from the sources register", "claims rows" and the time words in S10, Table S15 and Figure S6.
* The paper file's title line ("Paper A, results: ..."), the "First draft ... Not for circulation" line and the drafter appendix belong to the working draft; `assemble_draft.py --submission` strips them. Not edited.
* `references.md` (header comment, `<!-- Lnnn -->` ids, [CHECK] markers): B145's list; not touched.
* The main text's data-availability sentence says "the claims and sources registers are published with the archive"; V57a did not fail it and it describes archive contents, so it stands.

**F10 Keywords. Pending gate 6.** Seven keywords left in `highlights.md`. If the approval comes: drop "drought" or "land use".

**F11 Reference form. Stands.** Entries are APA-like as the tool renders them; to leave, and for Murray's check of the journal page.

**F12 References. In-text done; list for the register job below.** ABARES 2026b is cited as ABARES (2026); Higgins et al. 2018b as 2018 (supplement S6); Summerhayes and Baker 2026b as 2026 (section 1.3). The data sources named in the text carry in-text citations (section 2: ABS n.d.a, FAO n.d.a, NHMRC 2006; section 5: ABS 2021; Table 1: ABARES 2023; Table S11 and S10: the rest). Bolleter (2018): stands as the author's decision (letter unchanged).

**F13 Abstract, 1-in-10 range. Fixed.** Abstract: "30.8 million in a 1-in-10 year, with capacity below the population in 37% of draws". Highlight 3 gives the range: "Weather 1 in 10: 30.8 million (range 23.1 to 36.5); crops, grain-fed animals, 41.2" (82 characters).

**F14 Partition effect. Fixed.** Abstract: "a partition effect argued to follow from the model's rule that pasture cannot carry crops". Conclusion 5: "a partition effect that the model's substitution rule is argued to drive". Highlight 5 ("a partition effect") is a label and is unchanged.

**F15 Diet window. Fixed as decided.** Abstract: "39.1 million (39.7 on unrounded inputs)", once; the count allowed it (248 words). Conclusion 1 carries both values as well. The letter's third-round answer is updated to say so.

**F16 Smaller points. Fixed except the figure-side items.**
* Five zones named in section 12 (from the older-boundary flag in `regional_flips-3_wide.csv`): Alinytjara Wilurara, Desert Channels, Northern and Yorke, SA Murray Darling Basin, Swan.
* 2011 SA shares: section 5.1 says "against a 2020-21 land reference (Table 4)"; the Figure 4 caption says the 2011 line from State to SA4 changes the land reference.
* Sections 11 and 7.2 agree: section 11 says the long term is set mainly by the weather allowance and by fuel (section 7).
* Conclusion 3: "a 1-in-10 year leaves 30.8 million".
* Table 3: rows (and the list in section 4) follow the order the layers were added, with infrastructure land second; no value moved. The caption's "order of the rows below" is exact.
* the phrase "the three years 2021-23" replaces the one with a time word.
* Figure 4 caption (section file and `figures.csv`): "a group that mixes states takes the yields of the state with most cropland, so the solid bar depends on that rule and can pass 100%; the hatched bar, on one national yield vector, cannot."
* Figure 7 column names, region names, Figures 3 and 7 height: figures job (section 4).

## 2. Sentences changed (main text, abstract before and after)

Abstract before, fuel and paired sentences: "In all 2,000 paired draws on the seven choices both years share, 2025 capacity exceeds 2011; the long-term change is not established (26% of paired draws fall)." and "A long-term preset (...) covers 57% of the 2025 population; weather and fuel settings explain most of the shortfall."
Abstract after: "In all 2,000 paired draws on the seven shared choices, 2025 short-term capacity is higher; the long-term change is not established (26% of draws fall once the 2025-only choices are drawn)." and "A long-term preset (...) covers 57% of the 2025 population; only the weather setting explains the shortfall (34.3 million without it), while low fuel raises capacity."
Other abstract sentences: 1-in-10 sentence (F13), diet window (F15), flips sentence ("None of eight short-term status flips ..."), partition sentence (F14). The opening question was cut to hold 248 words; the abstract opens with the model.

Body, before then after:
* Section 8.1: "gives a 1-in-10 capacity of 29.2 to 31.6 million, above the population in every variant but one, which sits 0.6% below it (27.4 million: ...)" then "gives a 1-in-10 capacity of 29.2 to 31.6 million on the model's table method, above the population in every variant, and 27.4 to 29.1 million on the leave-one-out reference ..., where one variant (the area-weighted record from 1990-91) sits 0.6% below the population".
* Section 4: after the 0.19 million, added "Within pasture the area cancels; the 0.19 million comes from idle cropland, credited to pasture at the higher 2025 yield per hectare (Supplementary Section S10)." Cut to pay for it: "the net fall of six regions ..." sentence (section 3, repeated the next paragraph), "Crop yields add little, because ..." (reduced to "Crop yields add little (section 6)."), the duplicate "An ideal contiguous split ..." sentence (5.3), "Its 2011 status sits close to balance and has no range" (10), "The modules interact ..." (9.2), and the 5.4 sentence on the 2011 SA shares (moved to 5.1).
* Section 2: "which the ABS publishes and have not been fetched" is "which the ABS publishes and this paper does not use".
* Section 9.1, 12, conclusions: as in F2, F8, F14, F15, F16.

## 3. Register job (not done here)

* Delete ABARES (2026a) (uncited); relabel ABARES (2026b) as ABARES (2026) (section 1.4).
* Relabel Higgins et al. (2018b) as Higgins et al. (2018) and Summerhayes and Baker (2026b) as Summerhayes and Baker (2026); the "a" entries are gone.
* New entries for data sources named in the text (series name, year, URL from `qa/sources_register.csv`; the register has no release year for several, so "n.d." with a letter is proposed, to confirm):
  * ABS (n.d.a). Estimated resident population by SA2 (ABS Data API, annual ERP, ASGS 2021). https://data.api.abs.gov.au (D31; file dated 2026-10-27; release label not recorded).
  * ABS (n.d.b). Agricultural Commodities, Australia: NRM region data cubes, 2006-07 (7125.0), 2007-08 to 2009-10 (7121.0) and 2016-17 to 2020-21. https://www.abs.gov.au/statistics/industry/agriculture/agricultural-commodities-australia (D01 to D10, D13, D48).
  * ABS (n.d.c). Australian Agriculture (broadacre, horticulture, livestock), 2022-23 to 2024-25, and Livestock Products. https://data.api.abs.gov.au and https://www.abs.gov.au/statistics/industry/agriculture (D29, D30).
  * ABS (n.d.d). Historic Agricultural Commodities, 1860 to 2022 (workbook of Agricultural Commodities, Australia 2021-22). URL not recorded (D41).
  * ABS (2021). Australian Statistical Geography Standard (ASGS) Edition 3, July 2021 to June 2026, digital boundary files (SA2, SA3, SA4). https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs/edition-3-july-2021-june-2026 (D33).
  * ABARES (2023). Catchment Scale Land Use of Australia and commodities, update December 2023 (ALUM version 8, 50 m). data.gov.au dataset of that name (D32).
  * FAO (n.d.a). FAOSTAT Food Balances (food balance sheets, 2010 onwards; and the older Oceania series). https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_All_Data_(Normalized).zip (D17, D20).
  * FAO (n.d.b). FAOSTAT Crops and livestock products. https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_All_Data_(Normalized).zip (D18).
  * NHMRC (2006). Nutrient Reference Values for Australia and New Zealand including Recommended Dietary Intakes, version 1.2 (updated 2017). NHMRC, Canberra. No URL held (A27, L252).
  * DCCEEW (2026). Australian Petroleum Statistics, data extract August 2026. data.gov.au (D35); publisher to confirm.
  * DCCEEW (2025). Australian Energy Statistics 2025, Table F. https://www.energy.gov.au/sites/default/files/2025-08/australian_energy_statistics_2025_table_f.xlsx (A18); publisher to confirm.
  * UN (2015). Sustainable Development Goal Target 12.3 (cited in S6 as "UN Target 12.3"): not in the sources register; the author supplies the source.
* The year letters (n.d.a to n.d.d, FAO n.d.a and n.d.b) must match the in-text citations: section 2 (ABS n.d.a; FAO n.d.a; NHMRC 2006), section 5 (ABS 2021), Table 1 (ABARES 2023), Table S11, S10 (the rest).
* The `references.md` header comment, the `<!-- Lnnn -->` ids and the [CHECK] markers (F9): B145.
* `papers/DECLARATIONS.md`: the two wording edits of F9.
* B151's submission build must be rerun after these edits (the abstract, highlights, supplement and letter all changed).

## 4. Figures job (not done here; no script edited)

* Figures 3 and 7 are 250 mm high, above Springer's 234 mm page depth: a landscape or two-panel layout.
* Figure 7 column names to match the text: "Australian losses" to "Australian loss factors"; "Dairy on good land" to "Dairy on land that can carry it"; "Organic ruminants" to "Organic ruminant factor" (Table S3 uses the last).
* Region names in Figures 2, 3 and 5 to 7 ("Border Rvs Maranoa-Balonne", "South West Qld", "North East Vic", "NT") to the full names the text uses.
* Figure 4: the script's own caption string (`fig4_scale_curve.py`, line 51) carries the old sentence; replace it with the `figures.csv` text. The legend entry "NRM regions (catchments)" uses a term found nowhere else; the 2011 State point is joined to the 2011 SA4 point by one line (the caption says the land reference changes there).
* Figure 3: the labels "+1,174%" and "+1,468%" spill over neighbouring cells; "-32%" touches the cell edge.
* Figure S6: panel row names are scenario ids with spaces ("fuel csiro 340"); the S11 key maps them to plain names, but plain names on the figure are better.
* Supplementary Figure S1: add a `figures.csv` row (the caption is in the supplement) and regenerate `analysis/regionalise_2025/ideal_K53_cap650k.png` at 300 dpi with `map_regions.py`; the present file is 170 dpi, as the caption says.

## 5. Word counts

* Main text (`python3 qa/tools/wordcount.py A`, run on the repository files; the assembly was run on a scratch copy under the scratchpad, so `paper_A_draft1.md` is untouched): sections 1 to 12 = 705, 932, 542, 891, 640, 609, 518, 1064, 783, 354, 201, 695; **TOTAL 7,934** (limit 7,950).
* Abstract: **248** words (150 to 250).
* Highlights (characters): 83, 83, 82, 85, 80 (limit 85).
* Keywords: 7 (pending gate 6).
* Em dashes: none in any file under `papers/A_results/`, in `figures.csv` or in this report.
* Time words: none in the edited files (removed from the letter and supplement).
* Every new number or changed claim has a "B149a" row in the claims csvs; abstract rows replaced by the new wording are marked superseded.

## 6. Wrong-value check:

Example only. The pre-fix abstract sentence "weather and fuel settings explain most of the shortfall" tested against Table 6: the shortfall is the long-term capacity of 15.6 million against 27.6 million people. Table 6, weather allowance put back to its short-term value (1 year): 34.3 million, +119%, which exceeds 27.6 and so closes the shortfall; the setting explains it. Table 6, liquid fuel put back to its short-term 2,360 litres: 3.7 million, -76%, which widens the shortfall; the low-fuel setting is what keeps long-term capacity from falling to 3.7 million, so it does not explain the shortfall, it works the other way. The sentence is wrong for fuel and was replaced. The replacement tested against the same table: "only the weather setting explains the shortfall (34.3 million without it), while low fuel raises capacity" matches both rows. The same check on the paired-draw sentence: 26% falls only on the all-draws basis (long term, `paired_change_2011-2025.csv`), none on the shared-choices basis, so "26% of paired draws fall" beside "the seven choices both years share" was a wrong-basis value; the new sentence names the basis.

## 7. Process note

One read-only `git status` was run by mistake (the brief says no git commands); nothing was changed by it.
