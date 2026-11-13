# B98a: Paper A (results) cut to under 8,000 words, with an abstract (decision 92)

Brief: `qa/briefs/B98a_cut_paper_A.md`. Files written: `papers/A_results/draft/A_s01-04.md`, `A_s05-08.md`, `A_s09-12.md`, their three `_claims.csv` files, the new `papers/A_results/draft/supplementary.md` and `supplementary_claims.csv`, and this report. `paper_A_draft1.md` was not touched. No register row was touched.

## How words were counted

The V34a counter (`wc.py`, prose only): headings, table rows, table captions, figure and table placeholders, footnotes and the drafter notes are excluded; bold lead-ins and the conclusions and availability paragraphs are counted. The abstract sits above section 1 and is not counted in the main text.

## Word counts per section

| Section | Before | After | Scope budget | 70% floor | After as share of budget |
|---|---|---|---|---|---|
| 1 Introduction | 1,032 | 873 | 900 | 630 | 97% |
| 2 Method and data in brief | 575 | 477 | 600 | 420 | 80% |
| 3 Short-term picture | 787 | 676 | 800 | 560 | 85% |
| 4 What drove the change | 566 | 466 | 500 | 350 | 93% |
| 5 Scale curve | 1,026 | 679 | 900 | 630 | 75% |
| 6 Mechanism | 449 | 397 | 400 | 280 | 99% |
| 7 Long term | 748 | 572 | 800 | 560 | 72% |
| 8 Shocks | 896 | 779 | 800 | 560 | 97% |
| 9 How sure | 950 | 638 | 900 | 630 | 71% |
| 10 Regions in depth | 895 | 705 | 1,000 | 700 | 71% |
| 11 Discussion: measures | 1,468 | 1,049 | 1,300 | 910 | 81% |
| 12 Limitations and conclusions | 769 | 663 | 700 | 490 | 95% |
| **Total** | **10,161** | **7,974** | 9,600 | 6,720 | 83% |

Every section is above 70% of its budget. Sections 9 (638 against 630) and 10 (705 against 700) sit just above their floors, and the total is 26 words under the limit, so any later addition needs an equal cut.

## Abstract

214 words, under "## Abstract" at the top of `A_s01-04.md`: question, data and method, findings, implication. Headline figures: national short-term capacity 33.3 to 41.5 million against a population of 22.3 to 27.6 million (about 1.5 times; section 3); a 100-year plan covers 57% of the 2025 population (section 7); the SA2 sum is 37% of national short-term capacity (section 5). It also gives 53 regions, 2,450 SA2s and the 1-in-10 and 1-in-20 margin (section 8). Every figure is in the main text and has a row under section "Abstract" in `A_s01-04_claims.csv`. The rows resting on A196, A357, A358, A362 to A364 and A264 carry [gate 4].

## What moved to supplementary information

| Block (main-text section) | New place | Words moved | Named in the brief? |
|---|---|---|---|
| Swan's capacity and population figures and the coast examples (3); the regional decomposition figures for Central West NSW, Murrumbidgee-ACT, Murray, Swan and Fitzroy (4) | S1 | 202 | no (added, see below) |
| Contiguous-split detail: proportional-to-land test, random groupings with their five-draw caveat, SA4 and SA3 against random, the 650,000 km2 cap, Supplementary Figure S1 (5.3); and boundary detail: state shares on the two partitions, SA4 406, WA Rangelands and SA4 511, stranded pasture, unused land, Kurtz et al. 2020 (5.2) | S2 | 337 | split detail yes; boundary detail added |
| Scenario table (old Table 7, now Table S2), recycling and fuel sentences, the unexplained 340-litre method effect (8.3) | S3, Table S2 | 75 | yes |
| Method-tier tables (old Tables 8 and 9, now Tables S3 and S4), variance shares (81%, 36%, 52%) and what they belong to, regional effects of each correction and improvement, the six regions named (9) | S4, Tables S3 and S4 | 383 | yes |
| Region-by-region depth: Hawkesbury-Nepean-Sydney, the Murray with Murrumbidgee-ACT, Avon, SA Arid Lands with the Eyre Peninsula, in full (10) | S5 | 593 | yes |
| Measures with no read source beyond the model (field-crop and horticulture yields, all yields, irrigation, cropland from pasture, 7.5% meat, no avoidable waste, full recycling, 156-litre fuel); 11.7's model-only measures (meat output in bad years, fish, pulses, herd cycle, state worst-year factors, settlement, further measures); full measures table (old Table 11, now Table S5); also the grain-store split, the pool's bad-year and long-term factors and shortfalls, Higgins et al. 2018b and Davis et al. 2020 (11) | S6, Table S5 | 587 | measures and table yes; store, pool and supply-chain detail added |
| Diet at SA2 scale (37%, 33%, 45%, 95%), the swap figures 53.6 to 86.9 million, gardens 7% (12.2) | S7 | 117 | no (added) |

Total moved: 2,294 words. Table S1 (preset settings, named in section 2) is a placeholder in `supplementary.md`, not built (N-A2, decision 66), so the reference resolves. Each main-text block keeps a pointer and its main finding: 5.3 keeps the 76% and 69% split, 66.1% and the lower-bound wording; 8.3 keeps the field-crop shock, the waste scenario and the grain stores; 9 keeps the five judgement ends, the national effects of the two corrections and dairy, the tier counts and the interaction; 10 keeps an essential paragraph on the four regions plus the North Tasmania and North East Victoria paragraphs and Table 7; 11 keeps the five measures with a read source (livestock, diet, waste, stores, drought) and the export-diversion paragraph.

Why blocks beyond the brief's list moved: the named blocks, the merges and the tightening reached about 8,450 words. Section 10's 700-word floor meant its four-region paragraph could not shrink to a short summary. The added blocks are detail of the same kind, each with a pointer left in place.

**For the coordinator.** These scope content-list numbers now print only in the supplement: the variance shares 81%, 36% and 52% (section 9, item 4; the brief names them for moving); the random-grouping spreads (section 5, item 7; the five-draw caveat moved with them); the herd-cycle range and the state worst-year factors, SA 0.35 and WA 0.47 (section 11, item 9; model-only measures, named for moving); and the NSW, SA and WA partition shares. I read "never cut" as "never lose from the paper". Please confirm that reading, or say which numbers to restore and what to cut instead.

## Merged (each figure kept where it is a finding; the other place cites the section)

1. Populations of 22.3 and 27.6 million: kept in section 3; section 1.1 cites section 3.
2. "The model is the author's own, built for the thesis": kept in 1.3; section 2 cites 1.3.
3. The 2025 layer list: kept in section 4; section 2 cites section 4.
4. Scale-curve yield basis: kept in section 5; dropped from section 2.
5. Five regions tipping at 1 in 10 in three states: kept in section 8; dropped from section 2.
6. Drought factor from the 150-year cereal record: kept in section 2, which now carries the page (Lane 2014, p. 193); section 8 cites section 2.
7. Long-term flips: kept in section 7; sections 3 and 9 cite it. Section 9 keeps the gate-4 short-term flip values.
8. Method tier as a flip caution, and the 2025-range-only robustness test: kept in section 9; section 3 cites it.
9. Older 2011 boundaries: kept in sections 3 and 12; dropped from section 4's caveats.
10. Lane et al. 2015 finding: section 5 cites 1.3.
11. Schreiber et al. 2021 on capacity studies: kept in 12.1; dropped from section 5.
12. Field-crop measures 0 to 2.4% and livestock +9.7%: kept in section 11; section 6 cites it.
13. SA Arid Lands pasture, cropland and 41 thousand: kept in section 5; section 6 cites it.
14. Dairy's regional effects (-27%, +22%): kept in section 9 and S4; section 6 cites section 9.
15. Long-term range 13.4 to 16.5 million: kept in section 9; section 7 cites it. Capacities of 15.35 and 15.6 million: kept in section 7; section 9 cites it.
16. Tier counts (15, 16, 15; 36, 32, 36) and the six regions: kept in section 9 and S4; section 7 cites section 9.
17. Oil stocks at 61 against 90 days: moved from section 7 to 12.4, replacing the uncounted exposure sentence there (same source).
18. Average-year multiples of 1.49 and 1.5: kept in section 3 and Table 6; 8.1 cites them.
19. The 2017 to 2019 drought as a three-year deficit: kept in 1.5; 8.4 cites it and keeps the single-year finding.
20. Hughes and Lawson 2017, the state difference: kept in section 10 with its figures; dropped from 8.4.
21. The 13 choices, the Paper B pointer and the unsampled 2011 inputs: kept in section 2; section 9 cites it.
22. Citations for the two corrections: kept in section 2; 9.2 cites section 2 (S4 keeps them too).
23. Pasture 3.49 against 3.32 million km2, 1.96 million km2 unused, and the 10% to 99% cropland-share test: kept in section 6; dropped from the frame of section 11.
24. Waste-scenario effects (48.3 and 14.3 million, the step back in the long term): kept in section 8; 11.3 cites section 8 and keeps the decision 72 wording in full.
25. "Neither store changes the short term": kept in section 8.
26. The single weather factor for every yield: kept in section 12's opening and S6; dropped from section 11's cautions, which become three.
27. Long-term fuel figure (15.6 to 3.7 million): kept in section 7; 12.4 cites it.
28. Conclusions: the long-term capacities (15.35 and 15.6) and "between 2011 and 2025" dropped as repeats. Every gate-4 value in the conclusions stays.

## Cut, not moved (one line each)

1. 1.1: "The Intergenerational Reports and the Population Statement set the government's framing", because the next sentences name the reports.
2. 1.1: "Davies (2024) sets out both readings of this growth", because both quotations remain.
3. 1.1: the Parr 2018 sentence (no figure; L145). **Flag:** the scope lists L145 for point 1, so restore it if Murray wants it. It costs 15 words.
4. 1.4: James and O'Neill 2016, p. 187 (no figure); the same work stays in section 10 at p. 183 with its figure.
5. 1.3: "This paper takes up how the picture changes..." and "This paper brings the whole picture forward...", because the five questions and section 2 say both.
6. 1.5: "the authors' model estimate" after "A regional economic model put", a doubled label (scope point 5 used the phrase).
7. Section 3: the parenthetical "(Swan's 2011 status is a boundary artefact)", because the next sentences say it.
8. Section 5: "Only a consistent yield basis gives a clean curve...".
9. Section 5: the long-term shares in prose, because Table 3 prints all ten and the prose keeps "to 20% for the SA2s in 2025".
10. 7.2: the per-setting values (13.0, 11.7, 14.7, 19.0, 11.1, 19.7, 22.8) and "The fibre settings are large", because Table 5 prints them. The weather allowance and fuel stay in prose (scope item 3).
11. Section 7: the opening "This section asks what a plan..." sentence.
12. Section 12: "which the four points below take in turn" and "The five questions of section 1 are answered in turn".
13. Sentence-level tightening throughout. No number changed and no claim was widened.

## Claims csvs

* Rows for moved sentences are in `supplementary_claims.csv`, under section S1 to S7. Rows exist for both copies where a figure is printed in both the main text and the supplement (section 10's essential paragraph against S5; 9.2 against S4; 11.6 against S6). New rows cover the abstract, the supplement's composed sentences in S6 and S4, and the supplement's "all" rows. Rows for merged or cut sentences were removed (26 rows, none flagged; one of them a duplicate of the moved Table S5 waste row).
* Numbering: within each section, prose sentences are numbered 1 to n. Figure placeholders, table captions, table rows and the footnote are labelled ("Figure 4", "Table 3 caption", "Table 7 row 3", "footnote 1"). This replaces the mixed conventions of the first draft, where sections 5 to 8 numbered table rows as sentences.
* Fragments were updated to the new wording wherever the wording changed. The `9-12 all` row now lists main Tables 1 to 7 and supplementary Tables S1 to S5.

## Checks

* Number coverage: the V34a script `nums.py`, run on the three section files, finds no number missing from the claims csvs. The same check, run on `supplementary.md` against `supplementary_claims.csv`, finds none missing.
* Flags: [gate 4] appears on 77 rows (73 before; the extra rows are the abstract and the duplicated copies), and no flagged row was dropped. Every number in a [gate 4] fragment of the first-draft csvs still prints in the paper. Only the old Table 11 grain-store rows (48.4%, 64.5%) now print only in the supplement, because the brief moves that table; section 8 keeps 48.45% and 64.47% and section 11 keeps 48% and 64% with 23.2 and 25.7 million. The [open: Qn] mentions are in the drafter notes, which are unchanged apart from a B98a note at the top of each.
* No em or en dashes in any file written. British spelling; no time words.
* References: main Tables 1 to 7 (the regions table, old Table 10, is now Table 7, and section 5 points to it for SA Arid Lands), Figures 1 to 8, Supplementary Sections S1 to S7, Tables S1 to S5 and Supplementary Figure S1 all resolve. Wiedemann's table is written "their Table 1" so it cannot be read as this paper's Table 1.
* Header rules kept: the release is named at every figure; people over capacity; the yield basis at every regional sum; "53 regions (52 NRM regions and the Northern Territory)" at first use in each section, now also in S2.

## Wrong-value check

**Example (deliberate, not applied):** cutting section 8.3's sentence "A store of one year of grain raised the long-term capacity by 48.45% and a store of two years by 64.47%, with no short-term effect." would save 25 words. It would break rule 4 (a [gate 4] value: A220 and A222, pending B91) and the brief's instruction to keep the grain stores in section 8. I made the cut on a scratch copy and ran the gate-value check. It reported ('8', '46', '48.45') and ('8', '46', '64.47') as printed only in the supplement. On the delivered files the same check reports only the old Table 11 rows the brief moved. So the check can fail.

Scripts are in the session scratch folder `b98a/py/`: `split.py` and `remap.py` (sentence units), `run_map.py`, `overrides.py`, `gen.py` and `write.py` (csv remapping), `verify.py`, `cover.py` (number coverage, main and supplement) and `gatecheck.py`.
