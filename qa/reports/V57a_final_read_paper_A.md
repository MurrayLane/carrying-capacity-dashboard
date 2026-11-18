# V57a: final blind read of Paper A before deposit

Read: `papers/A_results/draft/paper_A_draft1.md` (body, declarations and appended drafter notes), `supplementary.md`, `highlights.md`, `references.md`, `A_s13_declarations.md`, `papers/A_results/response_letter_round2.md`, the nine PNGs and `figures.csv` under `analysis/figures_2025/paper_A/`. No number was retraced against the results files (V54a did that); arithmetic was checked only where two printed figures disagree on the page. One file was opened for a claim the text makes about its own table: `analysis/comparison_2025/decomposition_eight_layer_table.csv` (section 4 says the average lies between the forward and reverse walks in every row of Table 3; it does, including crop yields and fuel).

## 1. Fails, most serious first

**F1. Abstract, fuel and the shortfall (overclaim, wrong direction).** `paper_A_draft1.md`, Abstract: "A long-term preset (low meat, organic farming, little fuel, worst year in 100) covers 57% of the 2025 population; weather and fuel settings explain most of the shortfall." Table 6 and section 7.2 show the opposite for fuel: putting fuel back to its short-term value drops capacity from 15.6 to 3.7 million ("the largest on the other side"). The low-fuel setting raises long-term capacity; only the weather setting explains the shortfall (34.3 million without it, above 27.6). Section 7.1 and the highlight say "set most of the figure", which is true; the abstract's "explain most of the shortfall" is not. Fix: "the weather setting explains the shortfall, and the low-fuel setting is what keeps the figure as high as it is".

**F2. Abstract, the paired change (two draw sets read as one).** Abstract: "In all 2,000 paired draws on the seven choices both years share, 2025 capacity exceeds 2011; the long-term change is not established (26% of paired draws fall)." Section 9.1: on the seven shared choices alone no long-term draw falls either; the 26% appears only when the 2025-only choices and the land source are drawn. As written the reader takes the 26% to be from the same paired draws as the first clause, which contradicts section 9.1. The first clause also does not say "short-term". Fix: "In all 2,000 paired draws, short-term capacity in 2025 exceeds 2011; the long-term change is not established once the 2025-only choices are drawn (26% of those paired draws fall)."

**F3. Section 8.1 and the letter, the weather-record variants (one quantity, two values).** `paper_A_draft1.md`, 8.1: "gives a 1-in-10 capacity of 29.2 to 31.6 million, above the population in every variant but one, which sits 0.6% below it (27.4 million ...)". 27.4 lies outside the 29.2 to 31.6 just stated. Table S13 shows why: 29.2 to 31.6 is the thesis-method reference; 27.4 is from a second reference (leave-one-out, factors 0.66 to 0.70, capacities 27.4 to 29.1) that the sentence folds in without giving its range. The letter, first referee 3.5, says "29.2 to 31.6 million at 1 in 10, above the population in every variant", which the third-round answer contradicts. Fix the paper: "gives 29.2 to 31.6 million on the model's table method and 27.4 to 29.1 million on the leave-one-out reference; all are above the population but one, which sits 0.6% below it". Fix letter 3.5 to match.

**F4. Letter quotes that are not in the paper.**
- Second referee, point 3: quotes section 6 as "Short-term capacity therefore reads as a statement of how far meat production covers meat eaten, at the herd and diet of each year." The paper says "is therefore close to a statement ...". The third-round answer says the wording changed, but the second-round quote is left standing as a quotation.
- Second referee, point 7: quotes section 2 as "the 2011 NRM regions kept as a fixed partition in both years, not as today's administrative regions." The paper says "not as the NRM regions of 2025."
- First referee, 3.4: "The abstract opens 'at fixed settings'." The abstract opens "How many people can Australia's regions feed ...?"; "At fixed settings" begins the third sentence.

**F5. Letter statements contradicted by the paper.**
- Second referee, point 1: "The paper does not label the climate phase of each window." The Table 1 note and section 4 do label it (the letter's own third-round answer says so).
- Third round: "The main text is now 7,938 words". `qa/tools/wordcount.py A` prints 7,939.
- First referee, 3.10: "Workflow language is out of the supplement." The supplement keeps "a fetch for the author" (four times, S8 Table S11 and S10), "Built from the sources register" (Table S11), "claims rows" (S11), and file paths and release codes in most table captions (see F9).
- First referee, minor issues: "a box on what the bad-year results can bear". The paper has a bold run-in paragraph in 8.2, not a box.
- First referee, 3.2: "I have not estimated ... beyond that bound, and says the scope and frame changes ... are not documented" is not a sentence (subject missing before "says").
- Manuscript line: the letter's title, "Australia's carrying capacity 2011 to 2025 by region (Paper A, results)", differs from the paper's title and carries an internal label.

**F6. Pointer to a list that is not there.** Section 9.1: "(Supplementary Section S4 lists the choices)". S4 says "The 13 are as follows." and then names only the thirteenth (the long-term feeding benchmark) and the six added choices. The seven choices "both years share" (abstract, 9.1, conclusions) are named nowhere in paper or supplement. A referee cannot reconstruct the 19, the 13 or the 7.

**F7. Supplementary Figure S1 is a placeholder.** `supplementary.md`, S2: "[Supplementary Figure S1: the best contiguous split ... from `analysis/regionalise_2025/summary.csv` ... drawn by `map_regions.py`]". No image is in the figure folder, and S11 says "The nine figure files", which are Figures 1 to 8 and S6 only. Section 5.3 relies on S1 for the contiguous split.

**F8. The word "robust" breaks the paper's own rule.** Section 3 says: '"Robust" is used only for flips that pass on the full set.' The same section then says "The two flips that were clean and robust on 13 choices", and section 9.2 and conclusion 4 call the short-term regional count "robust to the method tier". Fix: "clean and inside the range on 13 choices"; "the short-term count does not change with the method tier".

**F9. Internal labels in deposit files.**
- `paper_A_draft1.md`: the title "Paper A, results: ... on the corrected releases"; the line "First draft, assembled 2026-11-18 ... Not for circulation."; and the whole "Appendix: drafter notes (not for the paper)" (job ids B117 to B143a, V37 to V54a, register ids A038, A317, X118, "decision 115", file paths). The deposit copy must be built without them.
- Declarations (paper and `A_s13_declarations.md`): "every figure carries its own register row and independent check"; "from my outline and the verified registers". "Register row" is internal jargon.
- `supplementary.md`: 61 file paths or backticked items and 85 release codes (`2025-fixed` 54 times, `2011-fixed-3`, `2025-mirror`, `2025-store-1` and others) across S1 to S12 and the Table S1 to S16 captions; Figure S6 defines its scenarios by id ("climate-crops-12:", "fuel-csiro-340:"). The release key in S11 is intended; outside S11 these should be plain names ("the corrected 2025 release").
- `references.md`: the header comment (tool path, "Murray fetches") and an `<!-- Lnnn -->` register id on all 57 entries; two entries read "[CHECK: not seen, Murray fetches]".
- Highlights: clean.

**F10. Keywords.** Seven keywords; the journal usually takes 4 to 6. Drop one (for example "drought" or "land use").

**F11. Reference list form.** The header says "Springer author-date form" but the entries are in APA form: "Cohen, J.E. (1995). Population Growth ... Science, 269(5222), 341–346." Springer's form is "Cohen JE (1995) Population growth and Earth's human carrying capacity. Science 269:341–346". The letter states that applying the guidelines is the author's task; flagged so it is not missed.

**F12. Reference mismatches.**
- ABARES (2026a) is in the list and cited nowhere in paper, supplement or letter. Remove it, and ABARES (2026b) becomes ABARES (2026) in the list and in section 1.4.
- Higgins et al. (2018b) and Summerhayes and Baker (2026b) carry a "b" with no "a" entry in the list.
- Data sources named in prose without a list entry: ABS Agricultural Commodities and the NRM data cubes, ABS Historic Agricultural Commodities, ABS estimated resident population (Data API), ASGS Edition 3, ABARES Catchment Scale Land Use of Australia, FAOSTAT food balances, Australian Petroleum Statistics, Australian Energy Statistics 2025, NHMRC reference body weights, UN Target 12.3. Springer expects data sources cited.
- Bolleter (2018): the entry's DOI encodes 2019 (letter: stands, the author's decision).
- Every other author-year citation in paper and supplement has an entry, and every other entry is cited.

**F13. Abstract, 1-in-10 figure without its range (overclaim by omission).** Abstract: "A cereal-yield weather allowance on all output leaves 30.8 million in a 1-in-10 year". Against 27.6 million people this reads as a safe margin. Section 8.1 gives the range 23.1 to 36.5 million, with 37% of draws below the population, and conclusion 3 says the range contains the population. The abstract should say so too, in about eight words. The same applies to highlight 3.

**F14. Abstract and highlight 5, partition effect stated as mechanism.** Abstract: "a partition effect: cropland can carry pasture-fed food, but pasture cannot carry crops." Section 5: "The dependence of the loss on that rule is argued here, not measured"; section 12: "the loss there may be overstated." Fix: "a partition effect that the model's substitution rule (cropland can carry pasture-fed food, pasture cannot carry crops) is argued to drive".

**F15. Diet window in the abstract and conclusions.** "a ten-year diet window gives 39.1 million for 2025". 39.1 is on the release's rounded diet inputs; on unrounded inputs it is 39.7, so the window is worth 2.4 or 1.8 million (30% or 22% of the rise). Giving only 39.1 states the larger effect. The letter (third round) says this is a deliberate choice; flagged as an author decision against the V52 amendment ("39.1 and 39.7 together").

**F16. Smaller consistency points.**
- Section 12: "five zones carry older 2011 boundaries". The five are named nowhere; only Swan appears (section 3, S1).
- Section 5.1: "On 2011 data the SA2s gave 40% (Table 4)". Table 4's own dagger says the 2011 SA shares "are not comparable with the zone levels above them"; Figure 4 also joins the 2011 State point to the 2011 SA4 point with one line.
- Section 11: "The long term is set by the weather allowance and by cropland"; section 7.2: "mainly a statement about planning for bad years and for fuel". Cropland doubling moves the long term by 8.7% (Table 9); fuel by 76% (Table 6).
- Conclusion 3: "the worst of ten years leaves 30.8 million". A 1-in-10 year is a return period, not the worst of a run of ten years. Fix: "a 1-in-10 year".
- Table 3 caption: "the forward walk (the layers added in the order of the rows below)". The release chain (S12, the eight-layer file) adds infrastructure second, not last. No number changes (infrastructure is zero), but the caption is not exact.
- Time words that drift: paper "the latest three years, 2021-23" (section 2); supplement "the climate effect already observed" (Figure S6), "each latest window" (S10 and Table S15); letter "now" seven times, "today's", "still". The paper's "earlier papers", "earlier set" and "earlier range" are relational and can stay.
- Figure 7 column names differ from the text: "Australian losses" (text: Australian loss factors), "Dairy on good land" (text: dairy on land that can carry it), "Organic ruminants" (Table S3: organic ruminant factor). Region names in Figures 2, 3 and 5 to 7 are abbreviated ("Border Rvs Maranoa-Balonne", "South West Qld", "North East Vic", "NT"), while the text uses the full names.

## 2. Overclaim read (abstract, highlights, section 12, nine captions)

| Item | Verdict |
|---|---|
| Flips and "robust" | Counts agree across abstract, Table 2, sections 3, 7.3, 9.1, conclusions and letter (8 flips: 3 artefacts, 7 not robust, 0 clean; long term 3: 2, 2, 1). The word itself fails F8. |
| Paired change | Fails F2 in the abstract; conclusion 1 and 9.1 are correct. |
| Weather-table comparison | 8.1 and Table 7 say it correctly ("almost all of the apparent improvement ... is the table"; 1 in 10 the same on either table). The record-variant sentence fails F3. |
| Failure range | Passes: 2.3% to 19.4%, median 7.6%, one decimal throughout, anchors named, S8 gives the base 5.8% and the log reading 6.1% as derivation. |
| Diet window | Body passes (both values, both shares); abstract and conclusions F15. |
| Meat identity | Passes in section 6 ("a consistency check, not a validation", all meat, ratios not counts); letter quote F4. |
| Climate phase | Passes (Table 1 note, section 4, S10: "stability within it, not that it is typical"; no bound beyond the paired test claimed). |
| Livestock denominator | Stated the same in sections 4 and 6 and S1, Table S11. The 0.19 million upper bound is given in section 4 without its mechanism (see reader's test 2). |
| Long-term preset | Abstract fails F1. |
| Partition effect | Abstract and highlight 5 F14. |
| 1-in-10 figure | Abstract and highlight 3 F13. |
| Section 12 | Limitations and conclusions read within their numbers apart from "worst of ten years" (F16) and the robust count (F8). |
| Captions | See section 4 below. Figure 4's caption has a dangling "that rule". |

## 3. Journal counts

- Main text, `python3 qa/tools/wordcount.py A`: sections 1 to 12 = 705, 921, 563, 891, 665, 609, 516, 1055, 779, 365, 198, 672; **TOTAL 7939**. At most 7,950: pass (the letter says 7,938, F5).
- Abstract: **245 words**. 150 to 250: pass.
- Highlights (characters): **83, 83, 84, 81, 80**. At most 85: pass.
- Keywords: **7**. Journal usually 4 to 6: fail (F10).
- References: 57 entries, 18 marked [CHECK]; APA form, not Springer (F11); mismatches F12.
- Em dashes: **none** in any of the nine text files (grep for U+2014). En dashes appear only in reference titles and page ranges (33, in `references.md`), as printed by the sources.
- Time words: F16.
- Internal labels: main text sections 1 to 12, abstract and highlights clean; failures in the paper file's header and appendix, declarations, supplement, references and letter (F9, F5).
- Declarations: generative AI, competing interests, funding and CRediT present; complete apart from the placeholders below. They use Elsevier headings; Springer's "Statements and Declarations" also expects data availability there (it sits at the end of section 12) and an ethics and consent line ("not applicable"), neither present.

### [CHECK] markers in `references.md`, with what each needs

| Entry | Needs | Can the author fill it from the item? |
|---|---|---|
| ABARE (2010) | author form, ABARE or ABARES | yes |
| ABARES (2026a) | author form | delete instead (uncited, F12) |
| AUS-MEAT (2005) | place of publication | yes |
| Centre for Population (2026) | place | yes |
| CSIRO and University of Queensland (2025) | place | yes |
| Davies (2024) | book editors; place | yes |
| DCCEEW (2017) | place | yes |
| DCCEEW (2019) | publisher; place; authors (Arcadis) | yes |
| DCCEEW (n.d.) | year | only if the page carries one; otherwise keep n.d. and drop the marker |
| Geoscience Australia and ABARE (2010) | publisher; place | yes |
| Gifford et al. (1975) | DOI | probably none exists; drop the marker after one look |
| Hughes and Lawson (2017) | book editors; place; page range | yes |
| Jansen (1999) | "not seen" | no: the author must read it to confirm it supports the Table S8 estimator |
| Lane (2014) | place | yes |
| Saltelli et al. (2010) | "not seen" | no: as Jansen |
| Sysak and Beilin (2017) | book editors; place | yes |
| Treasury (2023) | place | yes |
| USDA (1992) | place | yes |

## 4. Figures

All PNGs are 300 dpi: Figure 1 at 89.9 mm wide, the rest at 190.0 mm. Legends present in all nine.

| Figure | Legible at size | Caption against drawing | Collisions and notes |
|---|---|---|---|
| 1 (90 mm) | yes | matches: dots, line, thin 19-choice bar 31.1 to 49.2, thick 13-choice band 36.3 to 45.8 | none |
| 2 | yes | matches: 1 green open diamond (SA Arid Lands), 7 violet squares, 2 open (Desert Channels, Southern Gulf); columns match section 3 (+464, +456, +441; +1,283) | none; abbreviated names (F16) |
| 3 | yes | matches: eight columns, clip 50%, labels at 25% or more, hatching for negative | **"+1,174%" and "+1,468%" (SA Arid Lands, land and livestock) spill over the neighbouring cells**; "-32%" (Desert Channels) touches the cell edge. Height 250 mm, above Springer's 234 mm page depth |
| 4 | yes | mostly: points match Table 4 (44/44, 40/37, 20/18). **Caption "The size of the partition effect depends on that rule" has no rule named before it**; 2011 SA points joined to the zone levels (F16); legend says "NRM regions (catchments)", a term used nowhere else | hatched State bars overlap the State markers slightly |
| 5 | yes | matches: grey bars as Table 6, 2011 blue, 2025 orange, floor at 0.01 | none |
| 6 | yes | matches: panel heads 16, 21 and 24 regions agree with 8.2 and S4; orange range lines; floor at 0.001 | x axis labels only 0.001, 0.1 and 10, so the status line at 1 has no tick label (the axis title names it) |
| 7 | yes | matches Table S3 extremes (-22 Wet Tropics, +98 South East Qld, -27 SA Arid Lands, +53 Rangelands, -29 Condamine); Alinytjara Wilurara blank | column names differ from the text (F16); height 250 mm as Figure 3 |
| 8 | yes | matches: circle area, red over capacity, hatched room to spare, grey SA2 centroids; **small circles stated** ("3 of the 53 circles are under 0.5 mm across ... not visible") | leader lines for Border Rvs Maranoa-Balonne, Central West NSW and Lachlan cross other circles; readable |
| S6 | yes | matches Table S2: no short-term tips, long-term names listed | panel row names are scenario ids with spaces ("fuel csiro 340") |

Greyscale (Pillow, mode L): **Figure 3 passes** (hatching carries the sign, shade carries size, labels readable except the two spilled labels above). **Figure 7 passes**; white labels on mid grey (for example "-27", "+29" in the SA Arid Lands row) are low in contrast but readable.

## 5. The reader's test

1. **Which choices are shared?** Abstract, 9.1 and conclusions rest on "the seven choices both years share", and 9.1 points to S4 for the list, which S4 does not give (F6). Sentence to add to S4: "Table S7a lists the 19 choices with their ranges, marking the seven drawn for both years, the six drawn for 2025 only, and the one fixed on the corrected release."
2. **Where does the 0.19 million come from?** Section 4 says a smaller grazing area "raises the livestock yield by the same ratio", so a reader concludes a definitional change cancels to zero, then reads that it "would account for about 0.19 million". Sentence to add after the 0.19 million: "Within pasture the area cancels; the 0.19 million comes from idle cropland, which is credited to pasture at the higher 2025 yield per hectare (Supplementary Section S10)."
3. **Figure 4's State bars.** The caption's "depends on that rule" names no rule, and the solid bars reaching 120% look like an error. Sentence to replace it: "On the state basis a group that mixes states must take one state's yields, so the solid bar depends on which state is chosen and can pass 100%; the hatched bar, on one national yield vector, cannot."

**The sentence I would put first in the abstract:** "In a closed model of Australia's 53 regions, food capacity stayed about 1.5 times the population from 2011 to 2025, yet a 1-in-20 drought year puts it below the population and no short-term regional status change survives the uncertainty and artefact tests."

## 6. Placeholders left for the author

- CRediT statement: **[Author name]** (paper and `A_s13_declarations.md`).
- Data and code availability, section 12: **"DOI: [to be added at release]"**.
- The 18 reference [CHECK] markers in the table above; two (Jansen, Saltelli) need the papers read.
- Fetches named in the supplement (Table S11, S10): the 2025 ERP release label and retrieval date; ERP at 30 June 2007 and 2008 for the 2011 window check; the count of straddling SA2s and the population they move; national age-sex populations at 30 June 2011 and 2025. The letter adds the ABS explanatory notes to the agricultural census and a check of the irrigated share against ABS water use on farms.
- The image for Supplementary Figure S1 (F7).
- Journal form: Springer reference style and Statements and Declarations headings, with data availability and an ethics line (letter: "a task for the author").
- Letter: sign-off "The author", and the "Draft for the author. Not sent." line to remove before sending.

## 7. Register rows touched

None.
