# V31b: second route for cited one-route claims (decision 83)

Checker: blind checker, brief `qa/briefs/V31b_claims.md`, rules `qa/briefs/_checker_rules_results_wave.md`. Scripts and text extracts are in `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/V31b/` (`land.py`, `ev.mjs`, `ev2.mjs`, `hg.py`, `cmp.py`, `txt/`, `hg/`). No register was edited; no git; no network; no subagents.

Blindness caveat: the brief prints each claim's value beside its id, so I saw the stated values before deriving mine. I derived each value from inputs, papers or my own evaluator runs, not from any output cell the claim cites, and compared after.

## Tolerance

* Counts and labels: exact.
* Model outputs (evaluator capacities): within 0.5%.
* Rounded figures (ratios, percentages, km2, tonnes, ha a person): within one unit of the last printed digit.
* Text facts: the quoted words or table cell must say what the claim says; a figure printed in a paper must match as printed.

## Deliberate wrong values (the check can fail)

`cmp.py` applies the tolerance above. Fed deliberate wrong values it reports a mismatch:

| Test | Stated | Mine | Result |
|---|---|---|---|
| A070 cropland, wrong | 33 km2 | 29.36 | MISMATCH |
| B025 energy ratio, wrong | 2.1 | 1.935 | MISMATCH |
| B158 short-term gain as a model output, wrong | 12.5 million | 12.14 | MISMATCH |
| A070 as stated | 29 | 29.36 | pass |
| B025 as stated | 1.9; 2.1 | 1.935; 2.142 | pass |

The same script also flags B037 (0.298 against 0.2996), a real mismatch, below.

No claim in this batch is tier A, so the two-route rule for tier A does not arise; for every tier B claim my route is the second route.

## Claims

### A069 (tier B)
Route: own reallocation of SA2 cropping (`data/sa2/land_2011_method_by_sa2.csv`) to 2011 NRM pieces by CLUM cropland share (`data/nrm2011/land_use_by_sa2_nrm2011_piece.csv`), summed by `pipeline/land/zone_to_nrm2011.json` (`land.py`); 2011 value read from the 2011 default inputs (`data/2011/default-inputs-short-term.csv`, zone 5).
Mine: 2011 389 km2 (total area 23,120 km2); 2025 layer 191.22 km2 (total 23,120.6 km2). Same area, so no boundary change. Register: 389 to 191. **Pass.** Recommended status: second route agrees (V31b).

### A070 (tier B)
Route: same reallocation as A069 for zone 55 (NRM 503).
Mine: 29.36 km2 (total 3,737.6 km2). Register: 29. **Pass with a note:** Swan, unlike Hawkesbury-Nepean-Sydney, did change boundary (2011 inputs: 13,536 km2 with 5,035 km2 cropping), so the 29 km2 is for 2025 only, as the claim says. Recommended status: second route agrees (V31b).

### A071 (tier C)
Route: `analysis/comparison_2025/movers.md` line 1 and line 25; `papers/A_results/OUTLINE.md` section 10 (line 47).
Mine: movers.md line 1 reads "Murray 2026-11-03: one region per type, from the largest movers; Murray picks"; the five types are in OUTLINE line 47. Register: description. **Pass with a note:** the register note "The set is not yet chosen" is out of date: OUTLINE line 47 records the set chosen on 2026-11-07 (Hawkesbury-Nepean-Sydney, the Murray region with Murrumbidgee-ACT, Avon, North Tasmania, SA Arid Lands with the Eyre Peninsula). Recommended status: checked against the document (V31b); update the note.

### A320 (tier C)
Route: own mean of the committed FAOSTAT extracts (`hg.py`): food balance `fbs_au_world_2021_23.csv` item "Pulses"; crops `fao_au_production_1997_2023.csv` item "Pulses, Total".
Mine: food balance production mean 2021-23 4,374 kt (4.4 million t), exports 64% of production; crops basis mean 2021-23 4.51 million t (4.5). Register: 4.4. **Pass with a note:** 4.4 is the food balance figure; on the crops file for the same years it is 4.5. The food balance books Australian harvests a year late (see the FAOSTAT finding), so "2021-23" on the food balance is in effect the 2020 to 2022 harvests. Name the source as the food balance sheets, not both D17 and D18. Recommended status: second route agrees on D17 (V31b); set the output locator to the food balance extract.

### A327 (tier C)
Route: own evaluator runs on `2025-fixed`, Australia (`ev.mjs`), for the preset measures; national rows of `results/2025-store-1.csv` against `results/2025-improved.csv` for the grain store; livestock output and drought-proofing read from `papers/A_results/DISCUSSION_MEASURES.md` table (lines 14 and 6), which I did not rerun.
Mine: short term above 10%: meat and egg 7.5% +16.2%, 5% +85.0%; red meat 30% +55.6%; waste at 6% +16.4%, none +33.2%; livestock output +20% +19.4% (+10% gives +9.7%, not above 10%). Long term above 10%: drought-proofing +59.7%; grain store one year +48.3% (27.43 against 18.50 million); meat and egg 5% +25.7%; red meat 30% +18.6%; and livestock output +20% +18.8%. Register: description. **Fail (incomplete):** livestock output moves the long term by more than 10% at the +20% step (+18.8%) just as it moves the short term (+19.4%), but the claim lists it for the short term only. Correction: "The measures that move the short term by more than 10% are livestock output (+20%), the meat and egg share, the red-to-white meat switch and waste; the long term by the weather allowance, the grain store, livestock output (+20%) and the same diet changes." Alternatively, keep the list and say livestock output +10% moves neither term by more than 10%.

### A331 (tier C)
Route: counted zones in `results/2011-fixed.csv`, `results/2025-fixed.csv` and both default input sets; OUTLINE line 12.
Mine: 60 distinct zones in each (120 rows: 1 nation, 7 state rows, 52 regions per preset). OUTLINE line 12: "Same model, same 60 zones, same method (frozen during the data refresh), data brought forward from 2011 to 2025." Register: 60. **Pass.** Recommended status: second route agrees (V31b).

### A332 (tier C)
Route: OUTLINE lines 67 to 70.
Mine: "No reconciliation table ... The 2011 results appear as corrected only, with one footnote saying the original published values were updated." Register: description. **Pass.** Recommended status: checked against the document (V31b).

### A333 (tier C)
Route: file search of the repository for figure scripts (`savefig`, matplotlib, svg writers) and images, and for region polygons (`.shp`, `.geojson`, `.gpkg`, `.kml`, `.topojson`); OUTLINE Figures list (lines 58 to 65).
Mine: eight figures listed; scripts with images exist only for Figure 4 (`analysis/scale_curve_2025/plot_scale_curve.py`, `scale_curve.png`), Figure 7 (`analysis/paper_a/plot_method_effects.py`, `method_effects_heatmap.png`) and Figure 8 (`analysis/paper_a/migration_map.py`, `migration_map.png`). The only other plotting script, `analysis/regionalise_2025/map_regions.py`, draws the regionalisation maps, none of the eight. No polygon file is held; `migration_map.py` line 5 says so. Register: 3 of 8. **Pass.** Recommended status: second route agrees (V31b).

### A334 (tier C)
Route: OUTLINE line 21.
Mine: "The 2015 and 2017 papers gave one data vintage and, for the long term, one national and regional picture. This paper brings the whole picture forward to 2025 with the method frozen". Register: description. **Pass.** Recommended status: checked against the document (V31b).

### A335 (tier C)
Route: OUTLINE lines 74 to 76.
Mine: heading "Division of labour with Paper B (proposed 2026-11-06, to confirm)"; B reads the choices nationally, A regionally and over time. Register: description. **Pass.** Recommended status: checked against the document (V31b).

### A337 (tier C)
Route: OUTLINE line 51.
Mine: "What the model cannot carry (`DISCUSSION.md`); ... forced local self-sufficiency (... gardens, fruit and vegetables, diet) as a limitation of the closed-region reading". Register: description. **Pass.** Recommended status: checked against the document (V31b).

### A338 (tier C)
Route: OUTLINE line 39.
Mine: "Capacity is set by pairing pasture-fed food with crops; what a meat limit does to rangeland; dairy pasture quality. ... Sources: `analysis/sensitivity_2025/`." Register: description. **Pass.** Recommended status: checked against the document (V31b).

### A346 (tier B)
Route: own evaluator test (`ev.mjs`): release `2025-fixed`, Australia, cropland set to a share s of the combined cropland and pasture area (pasture the rest), both presets.
Mine: capacity change against the release default is 0.000% for every share from 10% to 100% on both terms (and from 5% short term, 8% long term); it falls below that (2%: -48% short, -66% long; 5%: -15% long). The release share is 8.7%. Cropland +25% taken from pasture: 0.00% both terms. Register: 10% to 99%. **Pass with a note:** holds for Australia; the flat range is wider than stated (to 100%, and from 8% on both terms). Regions were not tested. My script is a saved test; if the register wants one, `ev.mjs` is it. Recommended status: second route agrees, national only (V31b).

### B006 (tier C)
Route: SoFSR report (`Comparators/SoFSR_Full-Report_WEB_2025_Final_22052025.pdf`, foreword); national rows of `results/2011-corrected.csv` and `results/2025-mirror.csv`; Bellotti and Jones files sought.
Mine: "100 million": SoFSR foreword, "It feeds approximately 100 million people, including 27 million Australians". "9 to 14 million": long term 9.43 (2011-corrected) and 14.15 (2025-mirror). "61 million" and "30 to 35 million": not reached (see B161, B196). Register: 100; 61; 30 to 35; 9 to 14. **Pass with a note:** the figures found match; but SoFSR does not call its 100 million a carrying capacity (it says "feeds" and calls the metric misleading), so "all called carrying capacity" is the paper's framing, not each source's word. Recommended status: partly checked (V31b): 100 and 9 to 14 confirmed; 61 and 30 to 35 not reached.

### B008 (tier B)
Route: opened the Henry and Godden scan as images (`hg/`), Table 5, p. 100.
Mine: "Contemporary: contemporary excl. wool/cotton: Energy 109, Protein 96". Register: 109; 96. **Pass.** Recommended status: second route agrees (V31b, read from the scan).

### B010 (tier B)
Route: Henry and Godden 1995 (the only held route to Gifford): Table 1 p. 98, steps (a) to (f) p. 98, Table 5 p. 100; Chisholm 2000 (`Chisholm2000_BHERT.pdf`).
Mine: Table 1: 82 million (energy, "no food exports"), 60 million (protein, "no food exports"); step (d): "Nix's estimated 70m ha of land available for 'intensive' production"; Chisholm quotes "60 million people (82 million) at existing per capita food protein (energy)". Register: 82; 60. **Pass with a note:** both routes are second-hand; Gifford et al. 1975 is not on disk. Nix's 70 Mha is "intensive" land (Table 1 calls it "total potential arable area"). The Borrie attribution comes from the literature register, not from either held source. Recommended status: second route agrees, second-hand only (V31b).

### B022 (tier B)
Route: own rebuild of edible energy from the food balance extract (`hg.py`, my own code on Henry and Godden's recipe): E = 781.6 PJ; scaled people at 70/59.95 and 70/45.7.
Mine: 210.7 against 160.6 million, ratio 1.3118 (+31.2%); equal to 59.95/45.7 since the scale-up is linear. 59.95 = 28.3 (Table 3 sown pasture, Henry and Godden p. 99) + 31.65 (Australia cropping 316,499 km2 in `2025-fixed` regions.json). Register: 31%. **Pass.** Recommended status: second route agrees (V31b).

### B025 (tier B)
Route: own rebuild (`hg.py`): edible energy 781.6 PJ and protein 655.6 x 10^10 g (food balance mean 2021-23, world densities); 1990-91 totals 404 and 306 read from Henry and Godden Table 2, p. 99.
Mine: 1.935 (energy), 2.142 (protein). Register: 1.9; 2.1. **Pass with a note:** the 2021-23 food balance carries the 2020 to 2022 crop harvests (FAOSTAT finding below), so the comparison is with harvests a year earlier than its label; the claim draws on the food balance only, so it does not mix files. "Roughly double" holds for 1.9 to 2.1. Recommended status: second route agrees (V31b).

### B030 (tier B)
Route: Simpson, Petroeschevsky and Lowe 2000 (`Simpson2000.pdf`), Table 1 p. 13 and the Results text.
Mine: Table 1 TOTAL 5.957 ha a person, PASTURE column total 2.612; title "1991-92 (World Productivity, World Carrying Capacity)". Register: 5.96; 2.61. **Pass.** Recommended status: second route agrees (V31b).

### B037 (tier C)
Route: summed the plant-food crop rows of `analysis/method_tests_2025/simpson_food.csv` (1991-92: cereals to nuts, no feed) myself; Simpson text p. 13; Wackernagel and Rees scan page p078.
Mine: 0.1068 ha; 0.107 x 2.8 = 0.2996 (0.300); 0.1068 x 2.8 = 0.299. Simpson's vegetarian crop cell is 0.312 (Table 1). Register: 0.298. **Fail:** the arithmetic gives 0.300 (0.299 unrounded), not 0.298; and the premise is unsupported: Simpson states the estimates "are based on world average productivities" with no equivalence factor, and the Wackernagel and Rees page held on the productivity question (p. 78) gives no 2.8. Recommended status: keep withdrawn (X044); if the sentence is ever revived the figure is 0.300.

### B047 (tier B)
Route: Simpson Table 1 p. 13 and text.
Mine: energy land in the food row 0.43 ha a person (1991-92). 0.43 / 2.711 (food row total) = 15.9%; 0.43 / 2.165 (the food row's crop plus pasture) = 19.9%; Simpson's text: food takes "20 per cent of all land appropriated by energy consumption" (0.43 / 2.173). Register: 0.43, "a fifth to a third of the food row". **Fail (the ratio):** 0.43 holds, but it is about a sixth (16%) of Simpson's food row, a fifth of its crop and pasture part; no reading gives a third. Correction: "Simpson's energy land in the food row (0.43 ha a person in 1991-92) is about a sixth of the food row (16%)."

### B050 (tier B)
Route: Simpson Table 1 and text p. 13.
Mine: 2.612 / 5.957 = 43.8%; text: "approximately 44 per cent of the total EF". Register: 44%. **Pass.** Recommended status: second route agrees (V31b).

### B051 (tier B)
Route: Lenzen and Murray 2001 (`Comparators/1-s2.0-S0921800900002755-main.pdf`), Table 2 row "=Australian usage" and text.
Mine: pasture 8.10, total 13.6 ha a person, 1994-95 input-output tables; components sum to 13.60; text: "Most of Australia's total land use based ecological footprint of 13.6 ha/cap is caused by pastures". Register: 8.10 of 13.6. **Pass.** Recommended status: second route agrees (V31b).

### B059 (tier B)
Route: Alexander et al. 2016 SI Table S5; paper text (sections 2 and 3.1); OWID csv.
Mine: Table S5 Australia 112.20; paper: "global land surface (13,009 Mha (FAOSTAT, 2015a)"; OWID Australia 2011 158; 158 / 112.2 = 1.408. Register: 112.20; 158; 1.41. **Pass.** Recommended status: second route agrees (V31b).

### B070 (tier C)
Route: Alexander et al. 2016, section 3.1.
Mine: "The highest HALF values are for diets in New Zealand, Argentina and Australia at 135.8, 114.9 and 112.2 respectively, due to the high levels of animal products, particularly beef, consumed." Register: statement. **Pass with a note:** the paper says animal products, particularly beef, for the three countries together; it gives no Australia-only beef split. Recommended status: checked against the paper (V31b).

### B077 (tier B)
Route: Cassidy et al. 2013 (`Literature review/Cassidy2013`), Table 2 and text.
Mine: United States 16.1 (produced) and 5.4 (delivered) people a hectare; World 10.1 and 6; "41 crops on 947 million hectares of cropland"; "2700 calorie diet per day"; data "circa 2000". Register: 16.1; 5.4; 10.1; 6.0. **Pass.** Recommended status: second route agrees (V31b).

### B080 (tier C)
Route: Cassidy et al. 2013 text.
Mine: "from 2000 to 2010 ... maize ethanol production jumped from 6% of US maize production to 38% in the year 2010". Register: 6; 38. **Pass with a note:** the shares are of US maize, not world maize. Recommended status: checked against the paper (V31b).

### B121 (tier C)
Route: Fearnside 1990 (`Literature review/Fearnside1990`), p. 194.
Mine: "virtually all Brazilian Amazonia is capable of supporting 0.5-1 persons ha-1 under present technology, whereas KPROG2 indicates that in a 23600 ha study area ... at most 0.24 persons ha-1". Register: 0.24; 0.5 to 1. **Pass.** Recommended status: checked against the paper (V31b).

### B122 (tier C)
Route: Fearnside 1985 English original (`Literature review/Fearnside1985.pdf`, Human Ecology 13(3)) and the Spanish translation.
Mine: English text p. 352: "individual lots can easily fall below the 2550-calories/person/day minimum specified in the input parameters"; Fig. 8 caption p. 353: "standard of 2550 calories per capita per day"; p. 354: total protein 38 g, animal protein 25 g, plus a cash standard; "The length of the run was 25 yr"; failure "averages over the last ten years"; the maximum acceptable probability "can be selected by the planner"; yields and weather drawn to "reproduce observed distributions". The Spanish translation's text has "2500" and its caption 2550. Register: description, "2,500 kcal in the text, 2,550 in a figure caption". **Fail (one detail):** in the English original (L042) the text and the caption both say 2,550; the 2,500 is in the Spanish translation only, so the discrepancy is not "inside the source". Correction: "calories (2,550 kcal a person a day)", with a note that the Spanish translation's text gives 2,500. The rest holds.

### B158 (tier B)
Route: national rows of `results/2025-fixed.csv`, `results/2025-improved.csv`, `results/2011-fixed.csv`, `results/2011-improved.csv`; Monte Carlo ends from `results/likely_range_2025-*.csv`.
Mine: 2025: short 53.64 against 41.50 (+12.14 million); long 18.50 against 15.62 (+2.87). 2011: short +8.38; long -2.29 (13.06 against 15.35). Range ends 2025: short +9.6 (low) and +14.0 (high); long +2.3 and +2.8. Register: 12; 3. **Pass with a note:** the numbers hold for the 2025 national base readings; "every reading" does not: the other methods do not run on the improved tier, and in 2011 the improved tier lowers the long term. Correction: "On 2025 data the improved tier raises the model's own national readings by about 12 million on the short term and 3 on the long term over the corrected one."

### B161 (tier B)
Route: sought Bellotti 2017 at the literature row's `local_path`.
Mine: the file `Literature review/Bellotti2017_TheConversation_How_many_people_can_Australia_feed.html` is not Bellotti: its title is "We know how many people the earth can support", Christopher Tucker, The Journal of Population and Sustainability (2020). No other copy found. Only the arithmetic is checkable: 24.4 + 36.6 = 61.0. Register: 61 (36.6 from exports). **Cannot determine.** Recommended status: unverified; correct L009's `local_path` (the file is the wrong article) and obtain the Conversation piece.

### B163 (tier B)
Route: searched the models archive and the reports held (SoFSR, PMSEIC 2010, Chisholm 2000, the thesis) for the figures.
Mine: no NFF or industry source found; the nearest is PMSEIC 2010 ("we produce enough food today to feed 60 million people"), which is not NFF and gives no drought figure. Register: 75; 60; 30. **Cannot determine.** Recommended status: unverified (no work traced, as L011 says).

### B166 (tier C)
Route: SoFSR body text ("More than 70% ... exported. The other 30% feeds a population of 27 million ... another 63 million people, or around 100 million"); national results rows; own export shares from the food balance extract (mean 2021-23).
Mine: 27 + 63 = 90 ✓. Model average year: 41.5 (corrected), 49.4 (published method), 53.6 (improved). Exports as a share of production: milk 26%, fruit 14%, vegetables 11%, against wheat 78% and beef 67%. Register: description. **Fail (two details):** "41 to 49" mixes the corrected and published tiers and leaves out the improved 53.6 (the comparators README itself gives 41 to 54 for the corrected and improved methods); and fruit, vegetables and dairy are exported, only far less than wheat and beef. Correction: "the gap between the model's 41 to 54 million (corrected and improved) and 90 million is the diet: fruit, vegetables and dairy, which bind the model's diet, are exported far less (11% to 26% of production) than wheat and beef (67% to 78%)."

### B196 (tier B)
Route: sought the Jones committee report (L006) and secondary routes (the thesis section 4, Chisholm 2000).
Mine: no copy on disk; the thesis (p. on the 1994 report) gives a different summary ("ecologists ... 20 to 25 million"; "economists and demographers ... 50 and 60 million") and no 30 to 35. Register: 30 to 35. **Cannot determine.** Recommended status: unverified (paragraphs 2.13 to 2.16 not on disk).

### B197 (tier B)
Route: as B196.
Mine: not found; the thesis's 50 to 60 million is McNicoll's summary of the economists' side, not "50 plus in subsistence terms". Register: 50+. **Cannot determine.** Recommended status: unverified.

### B202 (tier B)
Route: Peters et al. 2016 (`Comparators/Peters-et-al-2016-Elementa-ten-diet-scenarios.pdf`), abstract and sections 3.2 to 3.4.
Mine: baseline 1.08 ha a person a year; cultivated cropland 0.18 and perennial cropland 0.16 for the baseline (0.34); grazing "0.10 to 0.74" across the meat diets (baseline the high end, 1.08 - 0.34 = 0.74); land available 134 million ha cropland plus 299 million ha grazing = 433; baseline capacity 402 million, lacto-vegetarian 807; healthy omnivore 0.93 to 0.25; vegetarian 0.13 to 0.14. Register: 1.08; 0.13 to 1.08; 402 to 807. **Pass.** Recommended status: second route agrees (V31b).

### B218 (tier B)
Route: own evaluator runs (`ev2.mjs`) on `2025-fixed` and `2025-improved`, Australia, short term, for no avoidable waste and drought return periods 5 to 100; the optimised diets read from the diet files `analysis/nutrition_lp_2025/diets_2025-improved/1_short_micro_{fixcap3,famcap3,free}.json` (not `variants.csv`).
Mine: diet 85.46, 202.06, 422.27 against 53.64 million: 1.593 to 7.872. Waste (no avoidable waste): 1.173 (improved) to 1.332 (corrected). Drought allowance: 1.343 to 1.347 at 10 years, 2.174 to 2.194 at 100 years (5 years gives 1.12). Register: 1.6 to 7.9; 1.2 to 1.3; 1.3 to 2.2. **Pass with a note:** the drought span is the 10-year to 100-year return period; the 5-year period (1.12) is outside it. Recommended status: second route agrees (V31b).

### B222 (tier B)
Route: Foran and Poldy 2002 full report, Table 2.5 p. 63 and the embodied-grain sentence below it, extracted from the PDF; own arithmetic over the three population paths (20.6, 25.1, 32.5 million, Table 1.1).
Mine: meat 31.8, 30.5, 30.0 million; grain with feed grain 80.0, 76.9, 75.6 million. Register: 30 to 32; 76 to 80. **Pass** (75.6 rounds to 76). Recommended status: second route agrees (V31b).

### B231 (tier C)
Route: Peters et al. 2016, sections 3.2 and 3.4.
Mine: "Per capita requirements for grazing land accounted for a large portion of the variation across the diets"; "Carrying capacity was shown to be highly sensitive to the starting assumptions about the proportion of land available for cultivated cropping." Register: statement. **Pass.** Recommended status: checked against the paper (V31b).

### B232 (tier C)
Route: Henry and Godden 1995 pp. 98 to 99 (Table 3, step (d)); Chisholm 2000; Fischer et al. 2002 contents.
Mine: Henry and Godden scale 1990-91 production by "70/45.7" (Nix's 70 Mha over intensive land in use) ✓. Fischer et al. are built on climatic, agro-edaphic and crop suitability (contents sections 4.3 to 5.2) ✓. Gifford: Henry and Godden report that Gifford scaled "contemporary proportions of crops, fallow and sown pastures" up to Nix's 70 Mha from 40.5 Mha in use (Table 3: crop 15.8, sown pasture 20.9, fallow 3.8), a factor of 1.73 of all intensive land; neither held source says cropland was doubled. **Fail (first clause, on the held sources):** correction: "Gifford scaled intensive land (crops, fallow and sown pasture) from 40.5 to Nix's 70 Mha". Gifford et al. 1975 itself is not on disk, so a reading of it could support the original wording.

### B233 (tier C)
Route: Alexander et al. 2016, sections 1 and 4.2.
Mine: "grassland is a broad category that covers a diverse range of intensities, from intensively managed pasture to extensively used savannahs"; "countries where grass-fed beef production systems predominate are treated identically ... as all use global average values". Register: statement. **Pass.** Recommended status: checked against the paper (V31b).

### B236 (tier C)
Route: thesis contents (`Papers and manuscripts/Lane-2014-PhD-thesis-QUT-eprint-67485.pdf`), chapter 6; Lane 2010 text (term counts).
Mine: chapter 6 sections: 6.1.1 Limits to Growth, 6.1.2 Ecological Footprint, 6.2.1 and 6.4.1 Southeast Queensland, 6.3.1 Noosa Shire, 6.3.2 Douglas Shire, 6.4.2 New York State, 6.4.3 Britain, 6.5.1 Brazil (Fearnside). Lane 2010 (Land Use Policy 27(4)) covers Limits to Growth, the footprint, South East Queensland, Noosa, Fairlie and Fearnside, but neither Douglas Shire nor Peters. Register: description. **Pass with a note:** the list holds for the thesis; Lane 2010 alone lacks Douglas Shire and Peters. The register's FINDING on Fearnside (reviewed before, yet a new method test) stands. Recommended status: checked against the documents (V31b).

### B242 (tier C)
Route: `papers/B_methods/SECTION7_DRAFT.md` matrix (column heads) and the methods line.
Mine: seven method columns (EP, FP, HALF, PPH, CB, FAIL, LDB) ✓; the planning-oriented studies listed are four (Peters, Fairlie, Noosa and Douglas Shire, Gutteridge's South East Queensland), five if Noosa and Douglas count apart. Register: 7; 3. **Fail (the 3):** right value: four studies as listed (five counting Noosa and Douglas Shire separately). The draft's caution line 64 already drops the number ("the planning-oriented studies of the earlier work"). Correction: drop "three" or write "four".

### B244 (tier C)
Route: Fearnside 1990 p. 194; Fearnside 1985 pp. 352 to 354.
Mine: 1990: "a 23600 ha study area"; "KPROG2, for example, requires so much data that it is impractical for large geographic areas". 1985: failure counted separately per standard (calories, total protein, animal protein, cash). Register: 23,600. **Pass with a note:** both quoted facts are in the 1990 overview (L043), not the 1985 paper; "one criterion per standard" is a paraphrase of the 1985 method. Recommended status: checked against the papers (V31b).

## Summary

| id | tier | verdict |
|---|---|---|
| A069 | B | pass |
| A070 | B | pass with a note |
| A071 | C | pass with a note |
| A320 | C | pass with a note |
| A327 | C | fail |
| A331 | C | pass |
| A332 | C | pass |
| A333 | C | pass |
| A334 | C | pass |
| A335 | C | pass |
| A337 | C | pass |
| A338 | C | pass |
| A346 | B | pass with a note |
| B006 | C | pass with a note |
| B008 | B | pass |
| B010 | B | pass with a note |
| B022 | B | pass |
| B025 | B | pass with a note |
| B030 | B | pass |
| B037 | C | fail |
| B047 | B | fail |
| B050 | B | pass |
| B051 | B | pass |
| B059 | B | pass |
| B070 | C | pass with a note |
| B077 | B | pass |
| B080 | C | pass with a note |
| B121 | C | pass |
| B122 | C | fail |
| B158 | B | pass with a note |
| B161 | B | cannot determine |
| B163 | B | cannot determine |
| B166 | C | fail |
| B196 | B | cannot determine |
| B197 | B | cannot determine |
| B202 | B | pass |
| B218 | B | pass with a note |
| B222 | B | pass |
| B231 | C | pass |
| B232 | C | fail |
| B233 | C | pass |
| B236 | C | pass with a note |
| B242 | C | fail |
| B244 | C | pass with a note |

Totals: 20 pass, 13 pass with a note, 7 fail, 4 cannot determine (44).

## FAOSTAT year finding

It arose for A320 and B025. Comparing the committed extracts year by year: food balance cereals (excluding beer) 2023 59.07 Mt against crops "Cereals, primary" 2022 59.61 Mt and 2023 43.12 Mt; food balance 2022 56.34 against crops 2021 54.96; food balance pulses 2023 5.20 Mt against crops 2022 5.12 and 2023 4.05. So the food balance file carries Australian crop harvests one year late (in line with V30c's wheat finding). Meat does not shift (food balance 2023 5.08 Mt against crops 2023 5.06). Neither claim mixes the two files within one figure: A320's 4.4 is the food balance mean (the crops file gives 4.5 for the same label years), and B025 uses the food balance only; both labels "2021-23" mean, for crops, the 2020 to 2022 harvests.

## Other findings

* L009's `local_path` points to the wrong article: the file named Bellotti2017 is Tucker 2020, "We know how many people the earth can support", The Journal of Population and Sustainability.
* A071's register note ("The set is not yet chosen") is out of date against OUTLINE line 47.
* The register's B047 and B158 notes already flag the faults found here; the comparators and method-test READMEs carry the corrected wording (16% and 22% for B047; "the model's own readings" for B158).

## Register rows touched

None.

## Ids checked

A069, A070, A071, A320, A327, A331, A332, A333, A334, A335, A337, A338, A346, B006, B008, B010, B022, B025, B030, B037, B047, B050, B051, B059, B070, B077, B080, B121, B122, B158, B161, B163, B166, B196, B197, B202, B218, B222, B231, B232, B233, B236, B242, B244.

## Rerun

From `/home/user/carrying-capacity-dashboard`:
`python3 -I <scratch>/V31b/land.py` · `node <scratch>/V31b/ev.mjs` · `node <scratch>/V31b/ev2.mjs` · `python3 -I <scratch>/V31b/hg.py` (its protein line prints in 10^7 g; divide by 1000 for 10^10 g) · `python3 -I <scratch>/V31b/cmp.py`, with `<scratch>` = `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad`. Paper text: `pdftotext -layout` into `<scratch>/V31b/txt/`; Henry and Godden pages rendered with `pdftoppm` into `<scratch>/V31b/hg/`.
