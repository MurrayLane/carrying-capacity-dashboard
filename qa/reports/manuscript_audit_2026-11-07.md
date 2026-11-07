# Manuscript audit, 2026-11-07

Every number in the four manuscript documents, tied to `qa/claims_register.csv` by `qa/tools/manuscript_audit.py`. Full list: the .csv beside this file. Numbers are those `numbers_lint.py` scans (single-digit integers without a percent sign are not); a number is matched when a register `value` or `statement` holds it after the rounding and scaling rules in the tool header.

## Summary

| document | numbers | matched | orphans | matched, status not `independently verified` | matched, weak |
|---|---|---|---|---|---|
| papers/A_results/OUTLINE.md | 92 | 92 | 0 | 29 | 8 |
| papers/A_results/DISCUSSION_MEASURES.md | 103 | 103 | 0 | 59 | 13 |
| papers/B_methods/OUTLINE.md | 169 | 167 | 2 | 144 | 14 |
| papers/B_methods/SECTION7_DRAFT.md | 39 | 39 | 0 | 39 | 9 |
| **all four** | 403 | 401 | 2 | 271 | 44 |

## Orphans (2)

* `OUTLINE.md:68` (B, section Method tests (all seven run on) **7503.0**: Henry and Godden's sources were ABS and ABARE 1993. The recipe is arithmetic once the production totals are built, so it is easy to run on 2025 data. For the 1990-91 fidelity check: ABARE (2010 edition, in the archive) covers broadacre, meat and dairy but not fruit, vegetables or eggs; ABS 7503.0 1990-91 (`Comparators/`, 31 pages) gives their gross values and average unit values (eggs $322.5m at $1.54 a dozen, apples, oranges, potatoes), so tonnage is value divided by unit value; the check would still be approximate because energy and protein conversion factors are not published in the paper; run 2026-11-06 (`analysis/method_tests_2025/`): recipe reproduces their 109 and 96 from their own totals (108.9 and 95.7); on FAO 2021-23 data it gives 138 to 211 million (energy) and 134 to 205 (protein) depending on the land base; fidelity of the 1990-91 production totals not rebuilt
* `OUTLINE.md:72` (B, section Method tests (all seven run on) **4306.0**: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebuilt pasture is 1.737 against Simpson's 1.758 and feed crop 0.098 against 0.095, but plant-food crop 0.107 against 0.312 is not reproduced; on 2021-23 data the crop-and-pasture footprint is 1.06 ha a person (1.94 in 1991-92) and the method reads as 160 to 343 million people; independent rebuild 2026-11-07: 140 to 343 million across two readings, because the paper does not state how world pasture is shared among beef, sheep and milk (pasture 1.2% low in one build, 36% high in the other); plant-food crop not reproduced by either

## Matched, status not `independently verified` (271)

### unverified (150)

* `OUTLINE.md:7` **1.5** -> A006: Arc: (1) the comfortable headline, about 1.5 times the population in both years;
* `OUTLINE.md:8` **1.5** -> A006: Headline (corrected releases; to confirm at freeze). Short-term capacity about 1.5 times population in both years (33.3 against 22.3 million in 2011;
* `OUTLINE.md:12` **60** -> A331: Same model, same 60 zones, same method (frozen during the data refresh), data brought forward from 2011 to 2025.
* `OUTLINE.md:27` **60** -> A331: Method and data in brief. The frozen method, the 60 zones, the 2011 and 2025 data sets, the release chain (`methods/README.md`).
* `OUTLINE.md:33` **54%** -> A108: Reads for shape, not for individual SA2s: SA2 units are administrative, the 2011 SA cells use 2020-21 land, and the state-yield basis is the conservative bound (a local-yield basis gives 54% against 3
* `OUTLINE.md:33` **37%** -> A108: Reads for shape, not for individual SA2s: SA2 units are administrative, the 2011 SA cells use 2020-21 land, and the state-yield basis is the conservative bound (a local-yield basis gives 54% against 3
* `OUTLINE.md:41` **22%** -> A308: How sure are the regional results. (Run 2026-11-06, `analysis/paper_a/README.md`: the beef carcase correction lowers the short term 10% to 22% in the beef and cropping regions; dairy on good land move
* `OUTLINE.md:41` **22%** -> A308: How sure are the regional results. (Run 2026-11-06, `analysis/paper_a/README.md`: the beef carcase correction lowers the short term 10% to 22% in the beef and cropping regions; dairy on good land move
* `OUTLINE.md:41` **95** -> A339: Figure 7 is the heat map, `analysis/paper_a/method_effects_heatmap.png`.) (a) Which status flips of section 3 hold across the 5th to 95th percentile ranges for each zone (the Monte Carlo method is des
* `OUTLINE.md:43` **6.5** -> A057: Murrumbidgee-ACT is under capacity in the average year (2.076) but over capacity in the long term (0.411) and at 1 in 100 (0.623); the SA Arid Lands change is a land-definition artefact (land layer al
* `OUTLINE.md:43` **0.49** -> A051: Hawkesbury-Nepean-Sydney carries the land-definition flag too (land layer alone 0.49).
* `OUTLINE.md:45` **9.7%** -> A275: Discussion: what would widen the margin. The ameliorative measures, tested one at a time on the model and read against what binds: livestock productivity and diet composition for the short term (lives
* `OUTLINE.md:45` **5%** -> A275: Discussion: what would widen the margin. The ameliorative measures, tested one at a time on the model and read against what binds: livestock productivity and diet composition for the short term (lives
* `OUTLINE.md:45` **85%** -> A275: Discussion: what would widen the margin. The ameliorative measures, tested one at a time on the model and read against what binds: livestock productivity and diet composition for the short term (lives
* `OUTLINE.md:45` **56%** -> A275: Discussion: what would widen the margin. The ameliorative measures, tested one at a time on the model and read against what binds: livestock productivity and diet composition for the short term (lives
* `DISCUSSION_MEASURES.md:3` **15.6** -> A233: Numbers are Australia, 2025, corrected method unless stated (short term 41.5 million, long term 15.6; population 27.6).
* `DISCUSSION_MEASURES.md:3` **27.6** -> A004: Numbers are Australia, 2025, corrected method unless stated (short term 41.5 million, long term 15.6; population 27.6).
* `DISCUSSION_MEASURES.md:14` **9.7%** -> A275: | Livestock output +10% / +20% | +9.7% / +19.4% | +9.4% / +18.8% | herd productivity and pasture improvement go straight to the binding constraint |
* `DISCUSSION_MEASURES.md:16` **56%** -> A275: | Red meat 30% of meat (more poultry and pork) | +56% | +19% | shifts food from pasture to feed grain |
* `DISCUSSION_MEASURES.md:18` **2.2%** -> A250: | Full recycling of food waste | +2.2% | already assumed | feed-grade, lawful waste only |
* `DISCUSSION_MEASURES.md:20` **2%** -> A244: Irrigated share of cropland 2% / 5% (now 0.7%)
* `DISCUSSION_MEASURES.md:20` **5%** -> A244: Irrigated share of cropland 2% / 5% (now 0.7%)
* `DISCUSSION_MEASURES.md:20` **0.7%** -> A242: Irrigated share of cropland 2% / 5% (now 0.7%)
* `DISCUSSION_MEASURES.md:20` **0.7%** -> A242: | Irrigated share of cropland 2% / 5% (now 0.7%) | +0.7% / +2.4% | the same | water is not a constraint in the model, so this is an upper bound |
* `DISCUSSION_MEASURES.md:20` **2.4%** -> A244: | Irrigated share of cropland 2% / 5% (now 0.7%) | +0.7% / +2.4% | the same | water is not a constraint in the model, so this is an upper bound |
* `DISCUSSION_MEASURES.md:21` **20%** -> A230: Field-crop yields +10% / +20%
* `DISCUSSION_MEASURES.md:21` **0.1%** -> A275: | Field-crop yields +10% / +20% | +0.1% | +0.2% to +0.3% | field crops are not what binds |
* `DISCUSSION_MEASURES.md:21` **0.3%** -> A231: | Field-crop yields +10% / +20% | +0.1% | +0.2% to +0.3% | field crops are not what binds |
* `DISCUSSION_MEASURES.md:22` **25%** -> A252: Cropland +25% taken from pasture
* `DISCUSSION_MEASURES.md:22` **10%** -> A346: in the model cropland can carry pasture-fed products but pasture cannot carry crops, so capacity is the same for any cropland share from 10% to 99% of the combined area and moving land from pasture to
* `DISCUSSION_MEASURES.md:22` **99%** -> A346: in the model cropland can carry pasture-fed products but pasture cannot carry crops, so capacity is the same for any cropland share from 10% to 99% of the combined area and moving land from pasture to
* `DISCUSSION_MEASURES.md:22` **1.96** -> A119: in the model cropland can carry pasture-fed products but pasture cannot carry crops, so capacity is the same for any cropland share from 10% to 99% of the combined area and moving land from pasture to
* `DISCUSSION_MEASURES.md:27` **2.96** -> A315: In 2021-23 Australia produced 4.66 million tonnes of meat and ate 2.96 (a surplus of 57%, the model's 1.5 times); two thirds of beef goes abroad.
* `DISCUSSION_MEASURES.md:27` **57%** -> A315: In 2021-23 Australia produced 4.66 million tonnes of meat and ate 2.96 (a surplus of 57%, the model's 1.5 times); two thirds of beef goes abroad.
* `DISCUSSION_MEASURES.md:27` **1.5** -> A315: In 2021-23 Australia produced 4.66 million tonnes of meat and ate 2.96 (a surplus of 57%, the model's 1.5 times); two thirds of beef goes abroad.
* `DISCUSSION_MEASURES.md:27` **1.5** -> A315: A margin of 1.5 times in an average year therefore exists only if exports yield to domestic need in a bad year.
* `DISCUSSION_MEASURES.md:27` **10** -> A316: At a 1-in-10 year meat production falls to about 3.45 million tonnes, still above domestic use; at a 1-in-20 year it is 2.95, level with it: the model's margin vanishes at 1 in 20.
* `DISCUSSION_MEASURES.md:27` **3.45** -> A316: At a 1-in-10 year meat production falls to about 3.45 million tonnes, still above domestic use; at a 1-in-20 year it is 2.95, level with it: the model's margin vanishes at 1 in 20.
* `DISCUSSION_MEASURES.md:27` **20** -> A316: At a 1-in-10 year meat production falls to about 3.45 million tonnes, still above domestic use; at a 1-in-20 year it is 2.95, level with it: the model's margin vanishes at 1 in 20.
* `DISCUSSION_MEASURES.md:27` **2.95** -> A316: At a 1-in-10 year meat production falls to about 3.45 million tonnes, still above domestic use; at a 1-in-20 year it is 2.95, level with it: the model's margin vanishes at 1 in 20.
* `DISCUSSION_MEASURES.md:27` **20** -> A316: At a 1-in-10 year meat production falls to about 3.45 million tonnes, still above domestic use; at a 1-in-20 year it is 2.95, level with it: the model's margin vanishes at 1 in 20.
* `DISCUSSION_MEASURES.md:28` **43.5** -> A317: The herd as a store. In a drought the herd is sold down, so meat supply rises for a year and falls for several after (the single-year capacity runs 43.5 to 55.4 million across 2016 to 2025 with the he
* `DISCUSSION_MEASURES.md:28` **55.4** -> A317: The herd as a store. In a drought the herd is sold down, so meat supply rises for a year and falls for several after (the single-year capacity runs 43.5 to 55.4 million across 2016 to 2025 with the he
* `DISCUSSION_MEASURES.md:29` **11.5** -> A318: The size of a one-year grain store for domestic use is about 11.5 million tonnes (3.1 for direct use at 112 kg a person and 8.4 for the feed grain embodied in meat, Foran and Poldy's 303 kg a person),
* `DISCUSSION_MEASURES.md:29` **3.1** -> A318: The size of a one-year grain store for domestic use is about 11.5 million tonnes (3.1 for direct use at 112 kg a person and 8.4 for the feed grain embodied in meat, Foran and Poldy's 303 kg a person),
* `DISCUSSION_MEASURES.md:29` **112** -> A318: The size of a one-year grain store for domestic use is about 11.5 million tonnes (3.1 for direct use at 112 kg a person and 8.4 for the feed grain embodied in meat, Foran and Poldy's 303 kg a person),
* `DISCUSSION_MEASURES.md:29` **8.4** -> A318: The size of a one-year grain store for domestic use is about 11.5 million tonnes (3.1 for direct use at 112 kg a person and 8.4 for the feed grain embodied in meat, Foran and Poldy's 303 kg a person),
* `DISCUSSION_MEASURES.md:29` **303** -> A318: The size of a one-year grain store for domestic use is about 11.5 million tonnes (3.1 for direct use at 112 kg a person and 8.4 for the feed grain embodied in meat, Foran and Poldy's 303 kg a person),
* `DISCUSSION_MEASURES.md:29` **52.6** -> A318: The size of a one-year grain store for domestic use is about 11.5 million tonnes (3.1 for direct use at 112 kg a person and 8.4 for the feed grain embodied in meat, Foran and Poldy's 303 kg a person),
* `DISCUSSION_MEASURES.md:37` **593** -> A319: Imports and trade diversification. Australia's fish imports (593 thousand tonnes) are about as large as its food use of fish (641) and it imports much of its fruit, vegetables and pork; the commodity 
* `DISCUSSION_MEASURES.md:37` **641** -> A319: Imports and trade diversification. Australia's fish imports (593 thousand tonnes) are about as large as its food use of fish (641) and it imports much of its fruit, vegetables and pork; the commodity 
* `DISCUSSION_MEASURES.md:37` **12** -> A319: Imports and trade diversification. Australia's fish imports (593 thousand tonnes) are about as large as its food use of fish (641) and it imports much of its fruit, vegetables and pork; the commodity 
* `DISCUSSION_MEASURES.md:37` **17** -> A319: Imports and trade diversification. Australia's fish imports (593 thousand tonnes) are about as large as its food use of fish (641) and it imports much of its fruit, vegetables and pork; the commodity 
* `DISCUSSION_MEASURES.md:39` **4.4** -> A320: Strategic stocks of other kinds. Pulses (4.4 million tonnes produced, mostly exported, long shelf life), frozen or canned protein, seed stocks.
* `DISCUSSION_MEASURES.md:41` **100** -> A321: Crop and regional diversification. The national worst year (the 100-year factor 0.46 of trend) is milder than the factors of New South Wales (0.30), Victoria (0.22), Queensland (0.35) and South Austra
* `DISCUSSION_MEASURES.md:41` **0.46** -> A321: Crop and regional diversification. The national worst year (the 100-year factor 0.46 of trend) is milder than the factors of New South Wales (0.30), Victoria (0.22), Queensland (0.35) and South Austra
* `DISCUSSION_MEASURES.md:41` **0.30** -> A321: Crop and regional diversification. The national worst year (the 100-year factor 0.46 of trend) is milder than the factors of New South Wales (0.30), Victoria (0.22), Queensland (0.35) and South Austra
* `DISCUSSION_MEASURES.md:41` **0.22** -> A321: Crop and regional diversification. The national worst year (the 100-year factor 0.46 of trend) is milder than the factors of New South Wales (0.30), Victoria (0.22), Queensland (0.35) and South Austra
* `DISCUSSION_MEASURES.md:41` **0.35** -> A321: Crop and regional diversification. The national worst year (the 100-year factor 0.46 of trend) is milder than the factors of New South Wales (0.30), Victoria (0.22), Queensland (0.35) and South Austra
* `DISCUSSION_MEASURES.md:41` **0.36** -> A321: Crop and regional diversification. The national worst year (the 100-year factor 0.46 of trend) is milder than the factors of New South Wales (0.30), Victoria (0.22), Queensland (0.35) and South Austra
* `DISCUSSION_MEASURES.md:41` **0.49** -> A321: Crop and regional diversification. The national worst year (the 100-year factor 0.46 of trend) is milder than the factors of New South Wales (0.30), Victoria (0.22), Queensland (0.35) and South Austra
* `DISCUSSION_MEASURES.md:41` **0.67** -> A321: Crop and regional diversification. The national worst year (the 100-year factor 0.46 of trend) is milder than the factors of New South Wales (0.30), Victoria (0.22), Queensland (0.35) and South Austra
* `DISCUSSION_MEASURES.md:43` **9.7** -> A323: Fuel and energy security. Farm diesel is the long term's biggest hidden dependence (without the low-fuel setting the long term falls to 3.7 million); on-farm electrification or biodiesel competes for 
* `DISCUSSION_MEASURES.md:45` **7%** -> A325: Household and community resilience. Stockpiles, community and household gardens (earlier tests: gardens add little; fruit and vegetables are 7% of cropland), local procurement.
* `DISCUSSION_MEASURES.md:51` **5%** -> A275: Several measures (the 5% meat share, no waste) are policy settings far from today's practice; they bound what is possible, not what is likely.
* `OUTLINE.md:11` **100** -> B006: Arc: (1) the puzzle: "100 million", "61 million", "30 to 35 million", "9 to 14 million" are all called carrying capacity;
* `OUTLINE.md:11` **61** -> B006: Arc: (1) the puzzle: "100 million", "61 million", "30 to 35 million", "9 to 14 million" are all called carrying capacity;
* `OUTLINE.md:11` **30** -> B006: Arc: (1) the puzzle: "100 million", "61 million", "30 to 35 million", "9 to 14 million" are all called carrying capacity;
* `OUTLINE.md:11` **35** -> B006: Arc: (1) the puzzle: "100 million", "61 million", "30 to 35 million", "9 to 14 million" are all called carrying capacity;
* `OUTLINE.md:11` **14** -> B006: Arc: (1) the puzzle: "100 million", "61 million", "30 to 35 million", "9 to 14 million" are all called carrying capacity;
* `OUTLINE.md:12` **16** -> B193: Headline (corrected releases; the method tests and design choices are run, `analysis/method_tests_2025/README.md`; the Monte Carlo range is set beside the spread there, the guide in section 7 is not y
* `OUTLINE.md:12` **100** -> B004: Headline (corrected releases; the method tests and design choices are run, `analysis/method_tests_2025/README.md`; the Monte Carlo range is set beside the spread there, the guide in section 7 is not y
* `OUTLINE.md:12` **63** -> B193: Headline (corrected releases; the method tests and design choices are run, `analysis/method_tests_2025/README.md`; the Monte Carlo range is set beside the spread there, the guide in section 7 is not y
* `OUTLINE.md:12` **60** -> B004: Headline (corrected releases; the method tests and design choices are run, `analysis/method_tests_2025/README.md`; the Monte Carlo range is set beside the spread there, the guide in section 7 is not y
* `OUTLINE.md:12` **100** -> B004: Headline (corrected releases; the method tests and design choices are run, `analysis/method_tests_2025/README.md`; the Monte Carlo range is set beside the spread there, the guide in section 7 is not y
* `OUTLINE.md:40` **44%** -> B050: Every land-based method is decided by it: pasture is 44% of Simpson's footprint, beef drives Australia's HALF value, Peters's US diets turn on grazing land, Lenzen and Murray's footprint is mostly pas
* `OUTLINE.md:40` **8.1** -> B051: Every land-based method is decided by it: pasture is 44% of Simpson's footprint, beef drives Australia's HALF value, Peters's US diets turn on grazing land, Lenzen and Murray's footprint is mostly pas
* `OUTLINE.md:40` **13.6** -> B051: Every land-based method is decided by it: pasture is 44% of Simpson's footprint, beef drives Australia's HALF value, Peters's US diets turn on grazing land, Lenzen and Murray's footprint is mostly pas
* `OUTLINE.md:42` **70** -> B232: Henry and Godden's answer rests on Nix's 70 Mha of intensive land;
* `OUTLINE.md:44` **1,000** -> B116: How sure the answer is, as a method. The design choices are also varied together: the Monte Carlo method (Latin hypercube over the 13 sampled choices, of which 12 vary in the 2025 releases because the
* `OUTLINE.md:49` **100** -> B239: why national estimates range from 9 to 100 million (exports, energy balance, definitions);
* `OUTLINE.md:68` **109** -> B008: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **96** -> B008: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **172** -> B009: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **156** -> B009: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **206** -> B009: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **188** -> B009: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **82** -> B010: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **404** -> B012: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **306** -> B012: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **70** -> B013: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **45.7** -> B013: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **17.4** -> B013: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **28.3** -> B013: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **0.1760** -> B014: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **0.2041** -> B014: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **404** -> B012: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **0.1760** -> B014: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **109** -> B008: Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton 109 million (energy), 96 (protein); no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Re
* `OUTLINE.md:68` **31** -> B022: Henry and Godden's sources were ABS and ABARE 1993. The recipe is arithmetic once the production totals are built, so it is easy to run on 2025 data. For the 1990-91 fidelity check: ABARE (2010 editio
* `OUTLINE.md:68` **322.5** -> B254: Henry and Godden's sources were ABS and ABARE 1993. The recipe is arithmetic once the production totals are built, so it is easy to run on 2025 data. For the 1990-91 fidelity check: ABARE (2010 editio
* `OUTLINE.md:68` **1.54** -> B254: Henry and Godden's sources were ABS and ABARE 1993. The recipe is arithmetic once the production totals are built, so it is easy to run on 2025 data. For the 1990-91 fidelity check: ABARE (2010 editio
* `OUTLINE.md:69` **41.5** -> B157: Requirements derived in `analysis/comparators_2025/`; run 2026-11-06 (`analysis/method_tests_2025/`): FAO 1997-98 production within 1.2% of theirs, their balance and the register's 30 meat and 77 grai
* `OUTLINE.md:70` **112.20** -> B059: Australia 112.20 on the paper's basis (percentage of the world's total land, 13,009 Mha), confirmed in the supplement's Table S5 (`Literature review/Alexander2016_SI.pdf`); 158 on the habitable-land b
* `OUTLINE.md:70` **13,009** -> B059: Australia 112.20 on the paper's basis (percentage of the world's total land, 13,009 Mha), confirmed in the supplement's Table S5 (`Literature review/Alexander2016_SI.pdf`); 158 on the habitable-land b
* `OUTLINE.md:70` **158** -> B059: Australia 112.20 on the paper's basis (percentage of the world's total land, 13,009 Mha), confirmed in the supplement's Table S5 (`Literature review/Alexander2016_SI.pdf`); 158 on the habitable-land b
* `OUTLINE.md:70` **1.41** -> B059: Australia 112.20 on the paper's basis (percentage of the world's total land, 13,009 Mha), confirmed in the supplement's Table S5 (`Literature review/Alexander2016_SI.pdf`); 158 on the habitable-land b
* `OUTLINE.md:70` **35.13** -> B052: Australia 112.20 on the paper's basis (percentage of the world's total land, 13,009 Mha), confirmed in the supplement's Table S5 (`Literature review/Alexander2016_SI.pdf`); 158 on the habitable-land b
* `OUTLINE.md:70` **378** -> B255: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **50** -> B259: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **50** -> B259: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **90** -> B061: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **34.4** -> B052: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **35.13** -> B052: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:71` **16.1** -> B077: US 16.1 people fed per hectare on produced calories, 5.4 on delivered calories (world 10.1 and 6.0); circa 2000, cropland only
* `OUTLINE.md:71` **5.4** -> B077: US 16.1 people fed per hectare on produced calories, 5.4 on delivered calories (world 10.1 and 6.0); circa 2000, cropland only
* `OUTLINE.md:71` **10.1** -> B077: US 16.1 people fed per hectare on produced calories, 5.4 on delivered calories (world 10.1 and 6.0); circa 2000, cropland only
* `OUTLINE.md:71` **6.0** -> B077: US 16.1 people fed per hectare on produced calories, 5.4 on delivered calories (world 10.1 and 6.0); circa 2000, cropland only
* `OUTLINE.md:71` **59%** -> B257: Paper read. Counts cropland only: no grazing and no sheep or goats, so it cannot stand for Australia's pastoral capacity. Needs crop use split (food, feed, other) and feed conversion (paper Table 1); 
* `OUTLINE.md:71` **22** -> B078: Paper read. Counts cropland only: no grazing and no sheep or goats, so it cannot stand for Australia's pastoral capacity. Needs crop use split (food, feed, other) and feed conversion (paper Table 1); 
* `OUTLINE.md:71` **6.0** -> B258: Paper read. Counts cropland only: no grazing and no sheep or goats, so it cannot stand for Australia's pastoral capacity. Needs crop use split (food, feed, other) and feed conversion (paper Table 1); 
* `OUTLINE.md:71` **5.8** -> B259: Paper read. Counts cropland only: no grazing and no sheep or goats, so it cannot stand for Australia's pastoral capacity. Needs crop use split (food, feed, other) and feed conversion (paper Table 1); 
* `OUTLINE.md:71` **6.0** -> B258: Paper read. Counts cropland only: no grazing and no sheep or goats, so it cannot stand for Australia's pastoral capacity. Needs crop use split (food, feed, other) and feed conversion (paper Table 1); 
* `OUTLINE.md:71` **5%** -> B258: Paper read. Counts cropland only: no grazing and no sheep or goats, so it cannot stand for Australia's pastoral capacity. Needs crop use split (food, feed, other) and feed conversion (paper Table 1); 
* `OUTLINE.md:71` **8%** -> B258: Paper read. Counts cropland only: no grazing and no sheep or goats, so it cannot stand for Australia's pastoral capacity. Needs crop use split (food, feed, other) and feed conversion (paper Table 1); 
* `OUTLINE.md:72` **5.96** -> B030: Whole footprint 5.96 hectares a person, 1991-92; the food row alone is 2.71 (energy 0.43, garden 0.03, crop 0.41, pasture 1.76, forest 0.08). The paper does not publish the consumption or world-yield 
* `OUTLINE.md:72` **2.71** -> B031: Whole footprint 5.96 hectares a person, 1991-92; the food row alone is 2.71 (energy 0.43, garden 0.03, crop 0.41, pasture 1.76, forest 0.08). The paper does not publish the consumption or world-yield 
* `OUTLINE.md:72` **0.43** -> B031: Whole footprint 5.96 hectares a person, 1991-92; the food row alone is 2.71 (energy 0.43, garden 0.03, crop 0.41, pasture 1.76, forest 0.08). The paper does not publish the consumption or world-yield 
* `OUTLINE.md:72` **0.03** -> B031: Whole footprint 5.96 hectares a person, 1991-92; the food row alone is 2.71 (energy 0.43, garden 0.03, crop 0.41, pasture 1.76, forest 0.08). The paper does not publish the consumption or world-yield 
* `OUTLINE.md:72` **0.41** -> B031: Whole footprint 5.96 hectares a person, 1991-92; the food row alone is 2.71 (energy 0.43, garden 0.03, crop 0.41, pasture 1.76, forest 0.08). The paper does not publish the consumption or world-yield 
* `OUTLINE.md:72` **1.76** -> B031: Whole footprint 5.96 hectares a person, 1991-92; the food row alone is 2.71 (energy 0.43, garden 0.03, crop 0.41, pasture 1.76, forest 0.08). The paper does not publish the consumption or world-yield 
* `OUTLINE.md:72` **0.08** -> B031: Whole footprint 5.96 hectares a person, 1991-92; the food row alone is 2.71 (energy 0.43, garden 0.03, crop 0.41, pasture 1.76, forest 0.08). The paper does not publish the consumption or world-yield 
* `OUTLINE.md:72` **0.095** -> B032: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebui
* `OUTLINE.md:72` **0.312** -> B032: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebui
* `OUTLINE.md:72` **36%** -> B256: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebui
* `OUTLINE.md:73` **0.24** -> B121: Applied to Australia as a method; no check against his figure is possible or needed (his data are Brazilian; the 1990 paper is a five-page overview and gives only the concept and one result, at most 0
* `OUTLINE.md:73` **23,600** -> B121: Applied to Australia as a method; no check against his figure is possible or needed (his data are Brazilian; the 1990 paper is a five-page overview and gives only the concept and one result, at most 0
* `OUTLINE.md:73` **0.5** -> B121: Applied to Australia as a method; no check against his figure is possible or needed (his data are Brazilian; the 1990 paper is a five-page overview and gives only the concept and one result, at most 0
* `OUTLINE.md:73` **2,500** -> B122: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `OUTLINE.md:73` **2,550** -> B122: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `OUTLINE.md:73` **38** -> B122: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `OUTLINE.md:73` **25** -> B122: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `OUTLINE.md:73` **25** -> B122: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `SECTION7_DRAFT.md:14` **100** -> B239: 2. Explaining why national estimates range from 9 to 100 million
* `SECTION7_DRAFT.md:24` **343** -> B247: EP, FP, HALF, PPH ○: they count calories or land in an average year at a single productivity; none has a way to see a bad year or a diet that has to balance (they read 134 to 343 million).
* `SECTION7_DRAFT.md:26` **100** -> B239: Explaining the 9 to 100 million range.
* `SECTION7_DRAFT.md:28` **32** -> B222: CB the 30 to 32 million meat count;
* `SECTION7_DRAFT.md:33` **23,600** -> B244: FAIL ◐: the right idea for a site (Fearnside's own application was 23,600 ha), but he states that KPROG2 needs so much data it is impractical for large areas.
* `SECTION7_DRAFT.md:34` **276** -> B247: FP and HALF use world-average productivity, so they cannot say what a region's own land feeds (they read Australia as 276 to 343 million);
* `SECTION7_DRAFT.md:34` **343** -> B247: FP and HALF use world-average productivity, so they cannot say what a region's own land feeds (they read Australia as 276 to 343 million);

### self-checked (80)

* `OUTLINE.md:41` **0.115** -> A340: The paper will label five range ends as the author's judgement (the meat-window three-way choice, the meat-and-egg low end 0.115, the red-meat low end 0.528, the 50/50 weight on the leave-one-out resi
* `OUTLINE.md:41` **0.528** -> A341: The paper will label five range ends as the author's judgement (the meat-window three-way choice, the meat-and-egg low end 0.115, the red-meat low end 0.528, the 50/50 weight on the leave-one-out resi
* `OUTLINE.md:41` **0.30** -> A342: The paper will label five range ends as the author's judgement (the meat-window three-way choice, the meat-and-egg low end 0.115, the red-meat low end 0.528, the 50/50 weight on the leave-one-out resi
* `OUTLINE.md:43` **10** -> A343: North Tasmania is the clean flip, balanced at a 1-in-10 drought (capacity 1.000 times population) and over capacity at 1 in 100 (0.798);
* `OUTLINE.md:43` **1.000** -> A343: North Tasmania is the clean flip, balanced at a 1-in-10 drought (capacity 1.000 times population) and over capacity at 1 in 100 (0.798);
* `OUTLINE.md:43` **100** -> A343: North Tasmania is the clean flip, balanced at a 1-in-10 drought (capacity 1.000 times population) and over capacity at 1 in 100 (0.798);
* `OUTLINE.md:43` **0.798** -> A343: North Tasmania is the clean flip, balanced at a 1-in-10 drought (capacity 1.000 times population) and over capacity at 1 in 100 (0.798);
* `OUTLINE.md:43` **2.076** -> A344: Murrumbidgee-ACT is under capacity in the average year (2.076) but over capacity in the long term (0.411) and at 1 in 100 (0.623); the SA Arid Lands change is a land-definition artefact (land layer al
* `OUTLINE.md:43` **0.411** -> A344: Murrumbidgee-ACT is under capacity in the average year (2.076) but over capacity in the long term (0.411) and at 1 in 100 (0.623); the SA Arid Lands change is a land-definition artefact (land layer al
* `OUTLINE.md:43` **100** -> A344: Murrumbidgee-ACT is under capacity in the average year (2.076) but over capacity in the long term (0.411) and at 1 in 100 (0.623); the SA Arid Lands change is a land-definition artefact (land layer al
* `OUTLINE.md:43` **0.623** -> A344: Murrumbidgee-ACT is under capacity in the average year (2.076) but over capacity in the long term (0.411) and at 1 in 100 (0.623); the SA Arid Lands change is a land-definition artefact (land layer al
* `DISCUSSION_MEASURES.md:22` **3.49** -> A345: in the model cropland can carry pasture-fed products but pasture cannot carry crops, so capacity is the same for any cropland share from 10% to 99% of the combined area and moving land from pasture to
* `DISCUSSION_MEASURES.md:22` **3.32** -> A345: in the model cropland can carry pasture-fed products but pasture cannot carry crops, so capacity is the same for any cropland share from 10% to 99% of the combined area and moving land from pasture to
* `DISCUSSION_MEASURES.md:27` **4.66** -> B145: In 2021-23 Australia produced 4.66 million tonnes of meat and ate 2.96 (a surplus of 57%, the model's 1.5 times); two thirds of beef goes abroad.
* `OUTLINE.md:11` **100** -> B001: Narrative (Murray asked for a story to drive each paper, 2026-11-06). Claim to test: the 9 to 100 million spread is mostly a spread of questions, not of facts, so the method should follow the purpose.
* `OUTLINE.md:12` **19** -> B003: Headline (corrected releases; the method tests and design choices are run, `analysis/method_tests_2025/README.md`; the Monte Carlo range is set beside the spread there, the guide in section 7 is not y
* `OUTLINE.md:12` **55** -> B003: Headline (corrected releases; the method tests and design choices are run, `analysis/method_tests_2025/README.md`; the Monte Carlo range is set beside the spread there, the guide in section 7 is not y
* `OUTLINE.md:14` **100** -> B005: How much of the spread of published estimates of Australia's capacity (9 to 100 million) is the definition, the diet or the method, and which design choices decide the answer?
* `OUTLINE.md:35` **100** -> B105: Where the other methods expose a weakness in the thesis method, the paper says so (section 4 and section 8); the published 2011 result sits in the register of estimates as one of the 9 to 100 million,
* `OUTLINE.md:44` **13** -> B253: How sure the answer is, as a method. The design choices are also varied together: the Monte Carlo method (Latin hypercube over the 13 sampled choices, of which 12 vary in the 2025 releases because the
* `OUTLINE.md:44` **12** -> B253: How sure the answer is, as a method. The design choices are also varied together: the Monte Carlo method (Latin hypercube over the 13 sampled choices, of which 12 vary in the 2025 releases because the
* `OUTLINE.md:44` **100** -> B179: This is the paper's test of how much of the spread of published estimates (9 to 100 million) can be produced by definition, diet and method choices alone, and the model's range is set beside the other
* `OUTLINE.md:44` **0.115** -> B250: The paper will label five range ends as the author's judgement (the meat-window three-way choice, the meat-and-egg low end 0.115, the red-meat low end 0.528, the 50/50 weight on the leave-one-out resi
* `OUTLINE.md:44` **0.528** -> B251: The paper will label five range ends as the author's judgement (the meat-window three-way choice, the meat-and-egg low end 0.115, the red-meat low end 0.528, the 50/50 weight on the leave-one-out resi
* `OUTLINE.md:44` **0.30** -> B252: The paper will label five range ends as the author's judgement (the meat-window three-way choice, the meat-and-egg low end 0.115, the red-meat low end 0.528, the 50/50 weight on the leave-one-out resi
* `OUTLINE.md:69` **30** -> B143: Requirements derived in `analysis/comparators_2025/`; run 2026-11-06 (`analysis/method_tests_2025/`): FAO 1997-98 production within 1.2% of theirs, their balance and the register's 30 meat and 77 grai
* `OUTLINE.md:69` **77** -> B143: Requirements derived in `analysis/comparators_2025/`; run 2026-11-06 (`analysis/method_tests_2025/`): FAO 1997-98 production within 1.2% of theirs, their balance and the register's 30 meat and 77 grai
* `OUTLINE.md:69` **40** -> B153: Requirements derived in `analysis/comparators_2025/`; run 2026-11-06 (`analysis/method_tests_2025/`): FAO 1997-98 production within 1.2% of theirs, their balance and the register's 30 meat and 77 grai
* `OUTLINE.md:69` **41** -> B153: Requirements derived in `analysis/comparators_2025/`; run 2026-11-06 (`analysis/method_tests_2025/`): FAO 1997-98 production within 1.2% of theirs, their balance and the register's 30 meat and 77 grai
* `OUTLINE.md:69` **127** -> B153: Requirements derived in `analysis/comparators_2025/`; run 2026-11-06 (`analysis/method_tests_2025/`): FAO 1997-98 production within 1.2% of theirs, their balance and the register's 30 meat and 77 grai
* `OUTLINE.md:69` **128** -> B153: Requirements derived in `analysis/comparators_2025/`; run 2026-11-06 (`analysis/method_tests_2025/`): FAO 1997-98 production within 1.2% of theirs, their balance and the register's 30 meat and 77 grai
* `OUTLINE.md:69` **12** -> B153: Requirements derived in `analysis/comparators_2025/`; run 2026-11-06 (`analysis/method_tests_2025/`): FAO 1997-98 production within 1.2% of theirs, their balance and the register's 30 meat and 77 grai
* `OUTLINE.md:69` **17** -> B153: Requirements derived in `analysis/comparators_2025/`; run 2026-11-06 (`analysis/method_tests_2025/`): FAO 1997-98 production within 1.2% of theirs, their balance and the register's 30 meat and 77 grai
* `OUTLINE.md:70` **97.73** -> B053: Australia 112.20 on the paper's basis (percentage of the world's total land, 13,009 Mha), confirmed in the supplement's Table S5 (`Literature review/Alexander2016_SI.pdf`); 158 on the habitable-land b
* `OUTLINE.md:70` **15.76** -> B054: Australia 112.20 on the paper's basis (percentage of the world's total land, 13,009 Mha), confirmed in the supplement's Table S5 (`Literature review/Alexander2016_SI.pdf`); 158 on the habitable-land b
* `OUTLINE.md:70` **94.5** -> B053: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **97.73** -> B053: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **14.6** -> B054: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **15.76** -> B054: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **109.6** -> B055: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **114.88** -> B055: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **94.8** -> B057: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **135.76** -> B057: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:71` **61%** -> B072: Paper read. Counts cropland only: no grazing and no sheep or goats, so it cannot stand for Australia's pastoral capacity. Needs crop use split (food, feed, other) and feed conversion (paper Table 1); 
* `OUTLINE.md:71` **190** -> B084: Paper read. Counts cropland only: no grazing and no sheep or goats, so it cannot stand for Australia's pastoral capacity. Needs crop use split (food, feed, other) and feed conversion (paper Table 1); 
* `OUTLINE.md:73` **41.5** -> B134: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `OUTLINE.md:73` **30.8** -> B134: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `OUTLINE.md:73` **10** -> B134: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `OUTLINE.md:73` **18.9** -> B134: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `OUTLINE.md:73` **100** -> B134: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `OUTLINE.md:73` **6%** -> B130: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `OUTLINE.md:73` **16** -> B130: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `OUTLINE.md:73` **17** -> B130: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `OUTLINE.md:73` **7%** -> B131: Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (
* `SECTION7_DRAFT.md:21` **41.5** -> B134: On the model's data the average-year capacity of 41.5 million falls to 30.8 at a 1-in-10 failure level and 18.9 at 1 in 100; the failure risk at today's population is about 6% a year (7% in 2011).
* `SECTION7_DRAFT.md:21` **30.8** -> B245: On the model's data the average-year capacity of 41.5 million falls to 30.8 at a 1-in-10 failure level and 18.9 at 1 in 100; the failure risk at today's population is about 6% a year (7% in 2011).
* `SECTION7_DRAFT.md:21` **10** -> B245: On the model's data the average-year capacity of 41.5 million falls to 30.8 at a 1-in-10 failure level and 18.9 at 1 in 100; the failure risk at today's population is about 6% a year (7% in 2011).
* `SECTION7_DRAFT.md:21` **18.9** -> B134: On the model's data the average-year capacity of 41.5 million falls to 30.8 at a 1-in-10 failure level and 18.9 at 1 in 100; the failure risk at today's population is about 6% a year (7% in 2011).
* `SECTION7_DRAFT.md:21` **100** -> B246: On the model's data the average-year capacity of 41.5 million falls to 30.8 at a 1-in-10 failure level and 18.9 at 1 in 100; the failure risk at today's population is about 6% a year (7% in 2011).
* `SECTION7_DRAFT.md:21` **6%** -> B217: On the model's data the average-year capacity of 41.5 million falls to 30.8 at a 1-in-10 failure level and 18.9 at 1 in 100; the failure risk at today's population is about 6% a year (7% in 2011).
* `SECTION7_DRAFT.md:22` **30** -> B245: It reproduces the Jones committee's 30 to 35 million at a 1-in-10 allowance (30.8 corrected).
* `SECTION7_DRAFT.md:22` **35** -> B245: It reproduces the Jones committee's 30 to 35 million at a 1-in-10 allowance (30.8 corrected).
* `SECTION7_DRAFT.md:22` **10** -> B245: It reproduces the Jones committee's 30 to 35 million at a 1-in-10 allowance (30.8 corrected).
* `SECTION7_DRAFT.md:22` **30.8** -> B245: It reproduces the Jones committee's 30 to 35 million at a 1-in-10 allowance (30.8 corrected).
* `SECTION7_DRAFT.md:23` **12** -> B248: CB ◐: finds which item runs out first (fish, 12 to 17 million; then meat, 40 to 41), which the aggregate methods cannot; it has no weather and no land.
* `SECTION7_DRAFT.md:23` **17** -> B248: CB ◐: finds which item runs out first (fish, 12 to 17 million; then meat, 40 to 41), which the aggregate methods cannot; it has no weather and no land.
* `SECTION7_DRAFT.md:23` **40** -> B248: CB ◐: finds which item runs out first (fish, 12 to 17 million; then meat, 40 to 41), which the aggregate methods cannot; it has no weather and no land.
* `SECTION7_DRAFT.md:23` **41** -> B248: CB ◐: finds which item runs out first (fish, 12 to 17 million; then meat, 40 to 41), which the aggregate methods cannot; it has no weather and no land.
* `SECTION7_DRAFT.md:24` **134** -> B156: EP, FP, HALF, PPH ○: they count calories or land in an average year at a single productivity; none has a way to see a bad year or a diet that has to balance (they read 134 to 343 million).
* `SECTION7_DRAFT.md:27` **15.6** -> B246: LDB ●: one model, one data set, run under each definition, spans 15.6 to 62.9 million (a factor of 4) without counting exports; counting exports takes it to 100.
* `SECTION7_DRAFT.md:27` **62.9** -> B246: LDB ●: one model, one data set, run under each definition, spans 15.6 to 62.9 million (a factor of 4) without counting exports; counting exports takes it to 100.
* `SECTION7_DRAFT.md:27` **100** -> B246: LDB ●: one model, one data set, run under each definition, spans 15.6 to 62.9 million (a factor of 4) without counting exports; counting exports takes it to 100.
* `SECTION7_DRAFT.md:28` **30** -> B245: CB the 30 to 32 million meat count;
* `SECTION7_DRAFT.md:32` **75%** -> B171: LDB ●: the only method with a unit of land, a diet and a pairing of pasture and crops at the regional level; the unit of self-sufficiency decides the answer (states 75%, NRM regions 44%, SA3 44%, SA2 
* `SECTION7_DRAFT.md:32` **44%** -> B172: LDB ●: the only method with a unit of land, a diet and a pairing of pasture and crops at the regional level; the unit of self-sufficiency decides the answer (states 75%, NRM regions 44%, SA3 44%, SA2 
* `SECTION7_DRAFT.md:32` **44%** -> B172: LDB ●: the only method with a unit of land, a diet and a pairing of pasture and crops at the regional level; the unit of self-sufficiency decides the answer (states 75%, NRM regions 44%, SA3 44%, SA2 
* `SECTION7_DRAFT.md:32` **37%** -> B175: LDB ●: the only method with a unit of land, a diet and a pairing of pasture and crops at the regional level; the unit of self-sufficiency decides the answer (states 75%, NRM regions 44%, SA3 44%, SA2 
* `SECTION7_DRAFT.md:38` **6.2** -> B217: LDB ●: gives the diet's land at Australian productivity (about 6.2 ha a person on the default diet, 0.27 with no meat), the shape of capacity against meat share (a peak at an intermediate share becaus
* `SECTION7_DRAFT.md:38` **0.27** -> B217: LDB ●: gives the diet's land at Australian productivity (about 6.2 ha a person on the default diet, 0.27 with no meat), the shape of capacity against meat share (a peak at an intermediate share becaus
* `SECTION7_DRAFT.md:47` **12** -> B248: ## Minimum reporting checklist (items 2 to 8 are the design choices measured in section 6; items 1 and 9 to 12 are what a reader needs to use the number)

### unverified: figure changed since V02_half_rebuild.md (14)

* `OUTLINE.md:70` **112.20** -> B056: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **113.1** -> B056: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **112.20** -> B056: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **81.0** -> B063: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **1.32** -> B068: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **276** -> B068: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:70` **2%** -> B249: Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value s
* `OUTLINE.md:71` **0.8** -> B056: Paper read. Counts cropland only: no grazing and no sheep or goats, so it cannot stand for Australia's pastoral capacity. Needs crop use split (food, feed, other) and feed conversion (paper Table 1); 
* `SECTION7_DRAFT.md:21` **7%** -> B249: On the model's data the average-year capacity of 41.5 million falls to 30.8 at a 1-in-10 failure level and 18.9 at 1 in 100; the failure risk at today's population is about 6% a year (7% in 2011).
* `SECTION7_DRAFT.md:37` **0.8%** -> B249: HALF ●: built for it, and reproduced well on 2011 data (Australia within 0.8%, world within 2.1%; an independent rebuild agrees within 2%): Australia's HALF fell 28% between 2011 and 2021-23 as beef a
* `SECTION7_DRAFT.md:37` **2.1%** -> B249: HALF ●: built for it, and reproduced well on 2011 data (Australia within 0.8%, world within 2.1%; an independent rebuild agrees within 2%): Australia's HALF fell 28% between 2011 and 2021-23 as beef a
* `SECTION7_DRAFT.md:37` **2%** -> B249: HALF ●: built for it, and reproduced well on 2011 data (Australia within 0.8%, world within 2.1%; an independent rebuild agrees within 2%): Australia's HALF fell 28% between 2011 and 2021-23 as beef a
* `SECTION7_DRAFT.md:37` **28%** -> B067: HALF ●: built for it, and reproduced well on 2011 data (Australia within 0.8%, world within 2.1%; an independent rebuild agrees within 2%): Australia's HALF fell 28% between 2011 and 2021-23 as beef a
* `SECTION7_DRAFT.md:37` **2.4** -> B067: HALF ●: built for it, and reproduced well on 2011 data (Australia within 0.8%, world within 2.1%; an independent rebuild agrees within 2%): Australia's HALF fell 28% between 2011 and 2021-23 as beef a

### self-checked (B23 wording) (9)

* `OUTLINE.md:45` **2%** -> A273: Discussion: what would widen the margin. The ameliorative measures, tested one at a time on the model and read against what binds: livestock productivity and diet composition for the short term (lives
* `OUTLINE.md:45` **1.6** -> A273: Discussion: what would widen the margin. The ameliorative measures, tested one at a time on the model and read against what binds: livestock productivity and diet composition for the short term (lives
* `OUTLINE.md:45` **1.8** -> A273: Discussion: what would widen the margin. The ameliorative measures, tested one at a time on the model and read against what binds: livestock productivity and diet composition for the short term (lives
* `DISCUSSION_MEASURES.md:33` **1.60** -> A273: In the short term the national capacity is 1.60 times the sum of the regions' in an average year and 1.82 at a 1-in-10 year, because pasture and cropland complement each other across regions; in the l
* `DISCUSSION_MEASURES.md:33` **1.82** -> A273: In the short term the national capacity is 1.60 times the sum of the regions' in an average year and 1.82 at a 1-in-10 year, because pasture and cropland complement each other across regions; in the l
* `DISCUSSION_MEASURES.md:33` **10** -> A273: In the short term the national capacity is 1.60 times the sum of the regions' in an average year and 1.82 at a 1-in-10 year, because pasture and cropland complement each other across regions; in the l
* `DISCUSSION_MEASURES.md:33` **2.60** -> A273: In the short term the national capacity is 1.60 times the sum of the regions' in an average year and 1.82 at a 1-in-10 year, because pasture and cropland complement each other across regions; in the l
* `DISCUSSION_MEASURES.md:33` **3.00** -> A273: In the short term the national capacity is 1.60 times the sum of the regions' in an average year and 1.82 at a 1-in-10 year, because pasture and cropland complement each other across regions; in the l
* `DISCUSSION_MEASURES.md:33` **2.60** -> A273: Trade in products between regions (the transport, processing and cold-chain system) recovers about 15.5 million people-equivalents in the short term and 9.6 in the long term (where the multiplier is 2

### independently verified (reconstruction, under-specified) (9)

* `OUTLINE.md:72` **1.737** -> B033: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebui
* `OUTLINE.md:72` **1.758** -> B033: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebui
* `OUTLINE.md:72` **1.06** -> B040: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebui
* `OUTLINE.md:72` **1.94** -> B036: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebui
* `OUTLINE.md:72` **160** -> B044: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebui
* `OUTLINE.md:72` **343** -> B046: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebui
* `OUTLINE.md:72` **140** -> B046: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebui
* `OUTLINE.md:72` **343** -> B046: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebui
* `OUTLINE.md:72` **1.2%** -> B033: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebui

### self-checked (rerun 2026-11-07) (8)

* `OUTLINE.md:74` **41.5** -> B159: In the repository; run 2026-11-06 (`analysis/method_tests_2025/model_entry.csv`, `cross_method.csv`): corrected 41.5 (36.3 to 45.8) short term, 15.6 (13.4 to 16.5) long term; improved 53.6 (46.2 to 60
* `OUTLINE.md:74` **36.3** -> B159: In the repository; run 2026-11-06 (`analysis/method_tests_2025/model_entry.csv`, `cross_method.csv`): corrected 41.5 (36.3 to 45.8) short term, 15.6 (13.4 to 16.5) long term; improved 53.6 (46.2 to 60
* `OUTLINE.md:74` **45.8** -> B159: In the repository; run 2026-11-06 (`analysis/method_tests_2025/model_entry.csv`, `cross_method.csv`): corrected 41.5 (36.3 to 45.8) short term, 15.6 (13.4 to 16.5) long term; improved 53.6 (46.2 to 60
* `OUTLINE.md:74` **53.6** -> B159: In the repository; run 2026-11-06 (`analysis/method_tests_2025/model_entry.csv`, `cross_method.csv`): corrected 41.5 (36.3 to 45.8) short term, 15.6 (13.4 to 16.5) long term; improved 53.6 (46.2 to 60
* `OUTLINE.md:74` **46.2** -> B159: In the repository; run 2026-11-06 (`analysis/method_tests_2025/model_entry.csv`, `cross_method.csv`): corrected 41.5 (36.3 to 45.8) short term, 15.6 (13.4 to 16.5) long term; improved 53.6 (46.2 to 60
* `OUTLINE.md:74` **60.1** -> B159: In the repository; run 2026-11-06 (`analysis/method_tests_2025/model_entry.csv`, `cross_method.csv`): corrected 41.5 (36.3 to 45.8) short term, 15.6 (13.4 to 16.5) long term; improved 53.6 (46.2 to 60
* `OUTLINE.md:74` **15.9** -> B115: In the repository; run 2026-11-06 (`analysis/method_tests_2025/model_entry.csv`, `cross_method.csv`): corrected 41.5 (36.3 to 45.8) short term, 15.6 (13.4 to 16.5) long term; improved 53.6 (46.2 to 60
* `OUTLINE.md:74` **19.4** -> B115: In the repository; run 2026-11-06 (`analysis/method_tests_2025/model_entry.csv`, `cross_method.csv`): corrected 41.5 (36.3 to 45.8) short term, 15.6 (13.4 to 16.5) long term; improved 53.6 (46.2 to 60

### not reproducible (1)

* `OUTLINE.md:72` **0.107** -> B035: ABS 4306.0 1991-92 (`Comparators/`, read from the scan); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables); run 2026-11-06 (`analysis/method_tests_2025/`): on 1991-92 data the rebui


## How to read the matching

* `matched` means a register `value` or `statement` holds the number after rounding or scaling. It does not mean the row is the claim. Small and common numbers (5%, 10, 12, 100, 30.8) land on many rows; the `n_candidates` and `strength` columns in the .csv show this. `weak` is 49 numbers: a rounded or scaled match among more than three rows, or a low word overlap. Treat weak matches as unchecked until a person confirms the row.
* The thousands and millions scaling (41.5 against 41,503,537) is in the tool and tested on its own, but no document number needed it: the register already stores figures in millions.
* Bare years past 2030 (2050) and written zeros ("0%") are not listed. ABS catalogue numbers (4306.0, 7503.0) are read as numbers, so they show as orphans; they are identifiers, not claims.
* Nothing here is a new finding about the science. Orphans are claims the register lacks and the matched-but-not-verified list is what the register has not yet had independently checked.

## Spot checks: ten matches that are right

| # | Document line | Number | Row | Why it is right |
|---|---|---|---|---|
| 1 | B OUTLINE:70 | 113.1 | B056 | Row says rebuilt HALF index for Australia 2011 is 113.1% of world land; the sentence is the same HALF rebuild result. |
| 2 | B OUTLINE:71 | 5.4 | B077 | Cassidy US 5.4 people a hectare on delivered calories; sentence and row are the same sentence. |
| 3 | B OUTLINE:72 | 1.737 | B033 | Rebuilt 1991-92 pasture 1.737 ha a person against Simpson's 1.758; sentence repeats it. |
| 4 | B OUTLINE:68 | 138 | B016 | Doc "138 to 211 million (energy)"; row value 137.6 rounds to 138 at 0 decimals (rounded match). |
| 5 | B OUTLINE:68 | 211 | B018 | Row value 210.7 rounds to 211; row is Henry and Godden with in-use land unchanged, the same quantity. |
| 6 | DISCUSSION:17 | 8.2% | A247 | Row: waste at the national target gives -8.2% on 15.6 (14.3); the table cell is that measure. |
| 7 | DISCUSSION:37 | 593 | A319 | Fish imports 593 thousand tonnes; sentence and row say the same. |
| 8 | DISCUSSION:28 | 55.4 | A317 | Single-year capacity 43.5 to 55.4 million across 2016 to 2025 with the herd cycle; same claim. |
| 9 | A OUTLINE:8 | 1.12 | A183 | National short-term capacity is 1.12 times the population in a 1-in-10 year (30.8 against 27.6 million). |
| 10 | B OUTLINE:68 | 0.1760 | B014 | Four-decimal figure matches the 0.1760 million people per 10^15 J consumption factor exactly; the four decimals make a chance hit very unlikely. |

## Spot checks: ten where the matching is doubtful

| # | Document line | Number | Row chosen | Problem |
|---|---|---|---|---|
| 1 | SECTION7:21 | 6% | B217 | Doc is the failure risk "about 6% a year"; B217 is 6.2 ha a person (rounded to 6). The right row is B130 (5.8 to 6.1% a year), a lower-ranked candidate. |
| 2 | SECTION7:21 | 7% | B249 | Doc is the 2011 failure risk "7%"; B249 is HALF "India 7% low". The right row is B131 (6.7 to 7.1% at the 2011 population). |
| 3 | SECTION7:21 | 10 | B245 | "1-in-10 failure level": B245 does state the 1-in-10 allowance, so the row is plausible, but 59 rows hold a 10 and the match carries no weight on its own. |
| 4 | B OUTLINE:72 | 36% | B159 | Doc: "36% high in the other build" (pasture); B159 holds 36.3 (the lower end of 36.3 to 45.8, a capacity). The number is a coincidence; the claim is probably an orphan. |
| 5 | B OUTLINE:71 | 5% | B077 | Doc: "within 5% to 8% between the two builds"; B077 holds Cassidy's 5.4. A rounding coincidence. |
| 6 | DISCUSSION:14 | 18.8% | A218 | Table cell is livestock output +20% on the improved release; A218 is liquid fuel -18.75%. A different measure and the opposite sign: wrong row, and the claim is not in the register. |
| 7 | B OUTLINE:11 | 100 | B001 | The "9 to 100 million" range ends in 100; B001 is the worst of 100 years. The same digits, a different quantity. |
| 8 | B OUTLINE:44 | 12 | B169 | Doc: "12 [of the 13 sampled choices] vary"; B169 is avoidable waste of 12%. Different quantity. |
| 9 | DISCUSSION:27 | 1.5 | A315 | Doc "margin of 1.5 times" and A315 "the model's 1.5 times" agree in sense, but 12 rows hold 1.5 and the overlap is 0.14; plausible, unconfirmed. |
| 10 | B OUTLINE:41 | 0.30 | A261 | Doc is the red-meat 30% share written 0.30; A261 (red meat 30% of meat) is the right row, reached by the decimal-against-percentage rule, but 17 rows hold 30, so the pick rests on word overlap alone. |

Pattern behind the doubtful list: the ranking prefers the same paper and section and then word overlap, so when a long sentence carries several numbers each number picks the row that fits the whole sentence, not the number's own role. The fix belongs to a person (confirm or reassign the row id for every weak match); the tool cannot read meaning.

## Resolution of orphans and weak matches

Written 2026-11-07 (brief B33). The "How to read the matching" and the two spot-check tables above are the hand-made notes of the first run and describe it as it was then (17 orphans, 49 weak). The summary table at the top is the rerun after the register changes below.

### Orphans (17 numbers): what was done

New register rows are A340 to A346 and B250 to B259 (17 rows). Rows A340 to A342 and B250 to B252 are of kind "setting" (stated in the notes column; the register has no kind column).

| document and line | number | resolution |
|---|---|---|
| A OUTLINE 41 | 0.115 | A340 (setting, judgement; source `analysis/sensitivity_2025/README.md`), self-checked |
| A OUTLINE 41 | 0.528 | A341 (setting, judgement; same source), self-checked |
| A OUTLINE 43 | 0.798 | A343 (North Tasmania; `analysis/paper_a/regions_in_depth.csv`, 1-in-100 column 0.7981), self-checked |
| A OUTLINE 43 | 2.076 | A344 (Murrumbidgee-ACT, average year 2025), self-checked |
| A OUTLINE 43 | 0.411 | A344 (long term 0.4114), self-checked |
| A OUTLINE 43 | 0.623 | A344 (1 in 100, 0.6234), self-checked |
| A DISCUSSION 22 | 99% | A346 (capacity flat for cropland share 10% to 99%), unverified: the document says it is read from an evaluator test and no saved script or output holds the 10% and 99% ends |
| A DISCUSSION 22 | 3.49 | A345 (pasture need, `analysis/scale_curve_2025/README.md`), self-checked |
| A DISCUSSION 22 | 3.32 | A345 (pasture held, same row), self-checked |
| B OUTLINE 44 | 0.115 | B250 (setting), self-checked |
| B OUTLINE 44 | 0.528 | B251 (setting), self-checked |
| B OUTLINE 68 | 7503.0 | identifier (ABS catalogue number), no row |
| B OUTLINE 68 | 322.5 | B254 (ABS eggs $322.5m, from the scan), unverified: not in a generated output |
| B OUTLINE 68 | 1.54 | B254 (eggs at $1.54 a dozen), unverified |
| B OUTLINE 70 | 378 | B255 (the "1,556/1,378" cropland-to-harvested ratio in the Alexander supplement; the tool reads 1,378 as 1 and 378), unverified: a published constant, not found in `half_index.py` |
| B OUTLINE 71 | 145 | B259 (independent rebuild, 5.77 x 25.1 Mha, `qa/reports/V05_cassidy.md`), unverified. B083 already holds "145 to 147" in its value, but the tool drops the leading number of an "N to M" value, so the lower end showed as an orphan |
| B OUTLINE 72 | 4306.0 | identifier (ABS catalogue number), no row |

Two identifiers remain as orphans in the rerun, as intended. The statement of B254 avoids the catalogue number so that 7503.0 stays an identifier.

### Weak matches (49 numbers): decisions

"new" marks a row added in this step. Where the chosen row differs from the audit's first pick the reason says why. The tool's ranking is unchanged, so the .csv still shows its own pick; this table is the decision.

| document | line | number | row | reason |
|---|---|---|---|---|
| A OUTLINE | 8 | -0.3% | A223 | its statement is this sentence; A205 holds the unrounded -0.26% |
| A OUTLINE | 8 | 48% | A264 | one-year grain store +48%; A220 is the same figure unrounded |
| A OUTLINE | 39 | 50 | B098 | list of return periods run, no figure claimed; the 50-year result is B098 (22.9) |
| A OUTLINE | 41 | 27% | A285 | dairy on good land, regional range -27.3 to +22.1 |
| A OUTLINE | 41 | 0.30 | A342 (new) | long-term benchmark low end, setting |
| A OUTLINE | 45 | 16% | A246 | waste at the national target, short term +16.4% |
| A OUTLINE | 45 | 16 | A265 | grain store equals a drought of about 16 years |
| A OUTLINE | 45 | 2% | A275 | field crops, irrigation, cropland move the short term 0 to 2.4% |
| A OUTLINE | 45 | 1.8 | A273 | national capacity 1.60 to 1.82 times the sum of regions |
| A DISCUSSION | 14 | 9.4% | A235 | livestock output +10%, long term 9.4% |
| A DISCUSSION | 14 | 18.8% | A237 | right row, but its figure is stale: see the finding below |
| A DISCUSSION | 15 | 85% | A258 | meat and eggs 5%, short term +85.0% |
| A DISCUSSION | 15 | 26% | A259 | same measure, long term +25.7% |
| A DISCUSSION | 16 | 56% | A260 | red meat 30% of meat, short term +55.6% |
| A DISCUSSION | 16 | 19% | A261 | same measure, long term +18.6% |
| A DISCUSSION | 17 | 16% | A246 | waste at the national target, short term |
| A DISCUSSION | 17 | 33% | A248 | no avoidable waste, short term +33.2% |
| A DISCUSSION | 20 | 2% | A242 | irrigated share 0.02 (A243 is its long term) |
| A DISCUSSION | 20 | 5% | A244 | irrigated share 0.05 (A245 is its long term) |
| A DISCUSSION | 21 | 0.1% | A228 | field-crop yields +10%, short term 0.1% |
| A DISCUSSION | 27 | 1.5 | A179 | margin of 1.5 times in an average year |
| A DISCUSSION | 51 | 5% | A258 | the 5% meat share measure |
| B OUTLINE | 11 | 100 | B005 | the 9 to 100 million spread |
| B OUTLINE | 12 | 16 | B091 | long-term settings, 15.6 |
| B OUTLINE | 12 | 55 | B003 | kept: the span 19 to 55 (B002 holds 55.3 alone) |
| B OUTLINE | 12 | 63 | B108 | improved, no avoidable waste, 62.9 |
| B OUTLINE | 35 | 100 | B005 | the 9 to 100 million spread |
| B OUTLINE | 44 | 12 | B253 (new) | 12 of the 13 sampled choices vary |
| B OUTLINE | 44 | 100 | B005 | the 9 to 100 million spread |
| B OUTLINE | 44 | 0.30 | B252 (new) | long-term benchmark low end, setting |
| B OUTLINE | 68 | 60 | B010 | Gifford et al. 82 and 60 |
| B OUTLINE | 68 | 109 | B015 | kept: "recipe reproduces their 109 and 96 (108.9 and 95.7)"; B008 holds the published pair |
| B OUTLINE | 68 | 96 | B015 | as above |
| B OUTLINE | 70 | 2% | B058 | "an independent rebuild agrees within 2%" is in its statement |
| B OUTLINE | 71 | 59% | B257 (new) | Cassidy's published delivered fraction; B072 holds the rebuilt 61% and the paper values only in its notes |
| B OUTLINE | 71 | 5% | B258 (new) | V05 verdict, within 5% for Australia |
| B OUTLINE | 71 | 8% | B258 (new) | V05 verdict, within 8% for the world |
| B OUTLINE | 72 | 36% | B256 (new) | second build of the Simpson footprint puts pasture 36% high (2.385 against 1.758); B033 carries it only in its notes |
| B OUTLINE | 73 | 6% | B130 | failure probability 5.8 to 6.1% at the 2025 population |
| B OUTLINE | 73 | 7% | B131 | failure probability 6.7 to 7.1% at the 2011 population |
| B SECTION7 | 21 | 30.8 | B096 | worst year of 10, 2025-fixed (B134 states the same sentence) |
| B SECTION7 | 21 | 10 | B096 | the 1-in-10 level |
| B SECTION7 | 21 | 100 | B001 | worst of 100 years, 18.9 |
| B SECTION7 | 21 | 6% | B130 | failure risk a year, not B217 (6.2 ha) |
| B SECTION7 | 21 | 7% | B131 | failure risk in 2011, not B249 (HALF, India 7% low) |
| B SECTION7 | 28 | 30 | B222 | the 30 to 32 million meat count |
| B SECTION7 | 37 | 2% | B058 | independent HALF rebuild agrees within 2% |
| B SECTION7 | 38 | 6.2 | B217 | kept: 6.2 ha a person on the default diet |
| B SECTION7 | 47 | 12 | none | item numbers of the reporting checklist ("items 1 and 9 to 12"), not a claim; no row |

Of the 49 numbers, 13 keep the audit's first pick, 28 are reassigned to another existing row (one of them, the list of return periods, points to the row for the 50-year run), 7 are tied to 6 new rows (A342, B252, B253, B256, B257, B258; B258 serves both 5% and 8%) and 1 needs no row (checklist numbering).

### Findings to decide (not changed, outside this brief)

* **Stale measures rows.** `analysis/paper_a/measures.csv` was regenerated at 11:26 on 2026-11-07, after the livestock row set was widened in `long_term_and_measures.mjs`. It now reads livestock output +10% 45.5 (+9.7%) short and 17.1 (+9.4%) long; +20% 49.6 (+19.4%) short and 18.6 (+18.8%) long; all yields +10% 45.7 (+10.0%) short and 17.2 (+10.0%) long. The register still holds the earlier figures: A234 (9.6%, status independently verified), A236 (49.5, 19.2%), A237 (18.7%), A238 (45.6, 9.8%), A239 (9.8%), and the text of A275 ("+9.6%"). DISCUSSION_MEASURES.md line 14 agrees with the csv, so the register is the stale side. I did not add a duplicate row for 18.8%; the rows should be corrected in place and the verified status of A234 reconsidered. The first-run audit also tied 9.7% to A323 (9.7 million, biofuel) and 19.4% to B115 (19.4 million) as strong matches; both are wrong rows.
* **Lower-end orphan cause.** The tool drops the leading number in a value written "N to M" (found with 145 to 147). Any other register value of that form hides its lower end from the audit.
* **Long-term benchmark influence.** The sensitivity README says the influence of the long-term benchmark is 0 in every zone. That holds for 2025-fixed and 2025-mirror, but 2025-improved shows up to 0.012 in 101 of 120 rows (see B253 notes).
* **Alexander recipe constant.** 1,556/1,378 (B255) is not found in `half_index.py`; whether the rebuild applies it is not checked here.

### Follow-ups from B32 (step 4)

* (a) B117, B119, B120 set to the current Monte Carlo figures, confirmed in `analysis/sensitivity_2025/monte_carlo_2025-fixed_all_summary.csv` (zone 1): short term herd and meat window 0.806 gives 81; long term resilience table 0.521 gives 52; long term herd and meat window 0.363 gives 36. Status `self-checked (rerun 2026-11-07)`.
* (b) B046 statement now reads "140 to 343 million", agreeing with its value, `cross_method.csv` (140 and 343) and V04.
* (c) B112 and B113 are `independently verified` (verifier report `qa/reports/V14_ranges_recheck.md`, commit 1a51ffe). B110, B111, B114, B115 are `self-checked (rerun 2026-11-07)`; their figures agree with the _all summary csv of each release (43.4 to 54.3 and 11.8 to 16.0 mirror; 46.2 to 60.1 and 15.9 to 19.4 improved).
* (d) B088 to B093 are `self-checked (evaluator route; a second implementation against the original workbook is pending, V15)`.
* (e) B159 and B187 confirmed current (41.5 with 36.3 to 45.8; 53.6 with 46.2 to 60.1; 45.764 / 36.333 = 1.26) and set to `self-checked (rerun 2026-11-07)`.
