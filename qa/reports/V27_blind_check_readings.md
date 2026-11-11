# V27 blind check of the reader pass (B66a to B66f, B67a, B67b)

Checker: independent blind checker. Brief: `qa/briefs/V27_blind_check_readings.md`; rules: `qa/briefs/_checker_rules_results_wave.md`. Nothing in the repository was edited; this report is the only file written there. Working text extracts and the search helper sit in the session scratch folder, outside the repository.

## 1. Tolerance (stated before any comparison)

A register line passes when every figure in it is on the page cited (or in the named section for text-only files) within rounding at the paper's own precision, and the wording claims nothing the paper does not say. A line fails on any figure not found at its citation, any figure differing beyond rounding, or a wording that overstates the paper. Counts and names must match exactly. Where a line cites a page range, a figure anywhere in that range counts as found. Journal (printed) pagination is used throughout; for article-number journals (Global Food Security 24, Land Use Policy, Science Advances) the PDF sheet number is the page.

Method: each PDF was turned to text with `pdftotext -layout`; a small search script takes a printed page and a pattern and reports whether the pattern is on that page and on which pages it occurs anywhere in the paper. Blind summaries below were written from the paper text before the register's `what_taken` and `notes` were opened (only `title`, `local_path` and `used_by` were read first).

## 2. Deliberate wrong value (example, invented, shown failing)

EXAMPLE ONLY, not a register line: "Hochman 2017: water-limited yield potential declined by 37% from 1990 to 2015 (p. 2071)."
Fed to the search script: `p2071 'declined by 37%'` returned MISS, found on no page. The true text, `p2071 'declined by 27%'`, returned OK on pp. 2071 and 2077. The check can fail.

## 3. Row blocks

### L148 (B66a) Summerhayes and Baker 2026, Food Security 18: 961-976
Blind summary: Australian case study (QLD, WA, VIC, federal) of 102 food-related policy documents, 25 policymaker interviews and 500 public surveys; finds food security weakly set as a policy goal, names three perception barriers and proposes a three-tier rights-based approach. Figures wanted for A1.4: 20 of 102 documents cite food security (p. 964); 46% of survey respondents agree food insecurity is prevalent (p. 968).
Register line: 102 documents (QLD 31, WA 30, VIC 32, federal 9) from 40 agencies, July 2021 to Oct 2022; 25 interviews (QLD 15, WA 6, VIC 4) Sept to Dec 2022; 500 surveys Brisbane only, Sept to Nov 2021; 20 of 102; 9 with food security as a specific goal (VIC 8, WA 1, none QLD or federal); 46/21/33%; AUD 3.5 million; notes 17 to 20% severe food insecurity.
Verdict: PASS.
Figures checked: 102, 31/30/32/nine, 40 agencies, July 2021 to October 2022, 25, 15/6/4, Sept to Dec 2022, 500, Brisbane, Sept to Nov 2021, 3.5 million (all p. 963); 20 of 102, nine S-labelled (one WA, eight VIC, none QLD or federal) (p. 964); 46%, 21%, 33% (p. 968); 17% to 20% (p. 962); barriers and three-tier approach (pp. 971-973).
Flag (no fail): the opening sentence "... and 500 public surveys, all in Brisbane (2021)" can be read as placing all three components in Brisbane; the figures list and notes correctly say surveys only. Suggest "500 public surveys (Brisbane only, 2021)".

### L151 (B66a) James and O'Neill 2016, Australian Geographer 47: 179-194
Blind summary: collates ABS census data 1992 to 2011 and non-ABS reports on Sydney Basin agriculture; finds the data contested, small farms undercounted before the 2005-06 census method change, and no conclusive decline; calls for consistent longitudinal data. Figures wanted for A1.4: error margins over 25% (p. 183); 33 versus 366 Liverpool vegetable farms (p. 186).
Register line: 23 non-ABS reports 1993 to 2009; over 25% error margins; 10% decline (Gillespie 2003); over 400 farms and 1,500 ha rise 2000-01 to 2005-06; 33 vs 366.
Verdict: PASS.
Figures checked: 23 reports, 1993 to 2009, "in excess of 25 per cent", ABS 1992 to 2011 (p. 183); 10 per cent decline, 1996-97 and 2000-01 (p. 184); 33 and 366 (p. 186); over 400 farms and 1500 ha, undercounting, "yet to be answered" (p. 187); turf and cut flowers (pp. 186-187); no conclusive trend (p. 188).

### L156 (B66b) Mayberry et al. 2019, Agricultural Systems 175: 13-21
Blind summary: CSIRO emissions study of the Australian red meat sector, 124.1 Mt CO2e (2005) to 68.6 Mt (2015) mainly from less land clearing; six pathways to carbon neutrality by 2030. Productivity enters through a quoted 1990 to 2010 steer trend (Wiedemann 2015a) and feedlot growth. Figures wanted for A11.1: liveweight at processing 538 to 574 kg and daily gain 0.55 to 0.72 kg (p. 14, second-hand).
Register line: as above plus "Six pathways to 2030 hold cattle near 25 million, sheep 70 million, goats 0.5 million"; feedlot 2.8 million (12%) 2015, 0.75 million (3.4%) 1990; 2.34 to 2.18 years; 23.6 million adjusted herd.
Verdict: FAIL (wording).
Figures checked: 124.1, 68.6 (p. 13); 25 million (10-year average, ABS 2017a), 70 and 0.5 million, 2.8 million and 12%, 750,000 and 3.4%, 0.55 to 0.72, 538 to 574, 2.34 to 2.18, 23.6 million, six pathways (all p. 14); SI appendix (p. 15); "as much as 50%" citing Wiedemann 2017 (p. 19). All values found.
Reason: p. 14 says "With the exception of the High Value Beef pathway, all pathways assume that the national beef cattle herd increases to 25 million"; p. 15 says High Value Beef reduces the herd to 20 million. "Six pathways ... hold cattle near 25 million" therefore overstates: five do (one adjusted to 23.6 million), one goes to 20 million. Also the paper says the herd "increases to" 25 million, not "held". The Wiedemann primary-paper page numbers in the notes are outside this file and were not checked.

### L161 (B66b) Mirosa, Pearson and Reynolds 2020, Routledge Handbook of Food Waste, ch. 14: 225-236
Blind summary: review chapter on food waste research and policy in Australia and New Zealand. Australia: earlier estimates of 7.5 Mt (2008-09) and 7.3 Mt (2008); National Food Waste Strategy (Nov 2017); National Food Waste Baseline (March 2019): 7.3 Mt in 2016-17 with stage shares. Figures wanted for A11.3: 7.3 Mt 2016-17, households 2.5 Mt (34%) (p. 229).
Register line: as above, plus 56% households 2008, 1.45 Mt informal (26%); notes say no 50% figure in the chapter.
Verdict: PASS.
Figures checked: 7.5 Mt 2008-2009, 7.3 Mt 2008, 56%, 1.45 Mt and 26% (p. 226); November 2017, four priority areas, "significant reduction ... by 2030" (p. 228); 20 March 2019, 2016-17, 7.3, 2.5 (34%), 2.3 (31%), 1.8 (25%), 1.2, 2.9, 3.2 Mt (p. 229). Confirmed: no "halve" or 50% target anywhere in the chapter.
Flag (no fail): notes call "a significant reduction by 2030" the Strategy aim; on p. 228 the chapter frames it as the UN Sustainable Development Goal the Strategy and CRC "assist the country in pursuit of". The conclusion (chapter is not a source for a halving target) holds.

### L170 (B66c) Hughes and Lawson 2017, in New Directions in Productivity Measurement, ch. 8: 173-194
Blind summary: machine-learning model of ABARES farm survey data separating climate from technology in cropping TFP; climate effect on productivity deteriorated from the mid-1990s, about 5% on average since 2000; climate-adjusted growth over 1% a year since 2006-07. Figures wanted for A11.5: about 5% (p. 191), over 1% a year (p. 184), Table 8.3 regional values (p. 189).
Register line: -4.71% all cropping, WA -7.63, western GRDC -8.20, QLD -4.92, NSW -4.78, VIC -4.67, SA -1.20, southern -4.21, northern -4.07 (Table 8.3, 2000-01 to 2014-15); around 5%; over 1% from 2006-07; notes on "15 to 20 years" (p. 175).
Verdict: PASS.
Figures checked: every Table 8.3 value in the 2000-01 to 2014-15 column (p. 189); 8.2 per cent western GRDC, mid-1990s, 1914-15 to 2014-15 reference, southern decline (p. 187); over 1 per cent since 2006-07 (p. 184); around 5 per cent since 2000 (p. 191); 15 to 20 years (p. 175). The notes' point that Table 8.3 does not support a south-only reading is correct. The chapter does not mention the Future Drought Fund; the register does not claim it does.

### L175 (B66c) Kummu et al. 2020, Global Food Security 24: 100360
Blind summary: global national-scale indicators 1987-89 to 2011-13 for four nutritional components; supply diversity rose for most people at the cost of higher import dependency, and import partners fell more often than rose except for vegetables and fruit. Australia appears in descriptive clusters only. Figures wanted for A11.7 and B8.2: 5.4 and 5.7 billion people with rising supply diversity; 33% vs 31% (protein partners) (p. 6).
Register line: 5.4 billion (101 countries), 5.7 billion (100 countries), 33 and 31%, 40 and 44%, 1.6 billion in 53 countries; Australia among major exporters (p. 4); notes Cluster I (p. 9).
Verdict: PASS.
Figures checked: 5.4, 5.7 billion, 101 and 100 countries, 31%, 33% (36 countries), 44% (79 countries), 40% (45 countries) (p. 6); 1.6 billion in 53 countries (p. 7); Argentina, Brazil, United States, Australia with falling protein production diversity, independency scaling (p. 4); "more often than it increased, except ... vegetables & fruits" (p. 1); Cluster I with Australia (p. 9).

### L188 (B66d) Grafton and Wheeler 2018, Annual Review of Resource Economics 10: 487-510
Blind summary: review of Murray-Darling water recovery; buy-backs far cheaper than infrastructure subsidies; recovered volumes overstated; subsidies may cut return flows; no observable basin-wide link between recovery and flows at the Murray mouth. Figures wanted for A12.3: 1,931 GL recovered to 30 Sept 2017 (p. 494); AUD 2,026 vs 4,970 per ML (Table 2, p. 501).
Register line: 1,931 GL; 1,231 and 699.9 GL; AUD 2,494 and 3,479 million; 2,026 and 4,970 per ML; 12,200 vs 4,700 GL; r = 0.10; 10 and 70% (Kirby et al.).
Verdict: PASS.
Figures checked: 1,931 GL and 30 September 2017 (p. 494); Table 2 totals 2,494 / 3,479 / 1,231.0 / 699.9 / 2,026 / 4,970 with columns RTB then infrastructure (p. 501); "at least 2.5 times" (p. 500); 12,200, 4,700, CSIRO 2008, no comprehensive estimates of return-flow effects (p. 497); 10% and 70%, Kirby et al. (p. 499); r = 0.10, barrage flows against recovered water 2007-08 to 2016-17 (p. 504); "if return flows represent half or more" (p. 505). 4,970 / 2,026 = 2.45, as the notes say.

### L222 (B66d) Badami and Ramankutty 2015, Global Food Security 4: 8-15
Blind summary: tests whether built-up urban land could grow 300 g of vegetables a day for the urban poor in a sample of countries under three scenarios; high-income countries need under 3% of urban area, several low-income countries over 100%; urban agriculture has a limited role in low-income countries. No Australian case. Figure wanted for A12.2: under 3% (high income) against over 100% (low income), medium case (pp. 12-13).
Register line: 300 g target; 19 countries; medium-case values for ten named countries; best-case 10 to 20%; no Australian case.
Verdict: PASS.
Figures checked: 300 g and Table 1 listing 19 countries with 2005-2012 poverty data (p. 11); "less than 3%" (p. 12); Table 3 medium case Canada 1.6, France 1.7, Poland 1.1, UK 2.9, USA 1.3, Chile 0.5, China 0.9, Bangladesh 182.9, DR Congo 131.8, Ethiopia 104.9, Nigeria 157.1, Tanzania 104.6 (p. 13); 10-20% best case and "limited contribution" (p. 14). No Australia or Sydney anywhere in the text.

### L198 (B66e) Zhang et al. 2018, Environmental Impact Assessment Review 68: 90-97
Blind summary: builds an 18-indicator urban resource and environment carrying capacity index for China (water, land, atmosphere, energy, solid waste; AHP weights) under "ecological civilization", applied to Tianjin 2007 to 2015, where the score rose (with dips) within 20 to 70 on a 0 to 100 scale. Says carrying capacity is the basis for urban planning (p. 91). Figure wanted for B1-2.b: the index structure and the Tianjin scores.
Register line: 18 indicators, five groups, AHP; 24.04 (2007) to 71.23 (2015); Lane 2010 cited once (p. 91).
Verdict: PASS.
Figures checked: 18 indicators (p. 90); Table 1 indicators (p. 94); AHP (pp. 91, 93); Table 7 comprehensive scores 24.04 and 71.23 (p. 96); Lane 2010 in text only at p. 91 (and in the reference list p. 97).

### L200 (B66e) Haddaway et al. 2020, Nature Ecology & Evolution 4: 1582-1589
Blind summary: perspective naming eight problems in environmental evidence reviews, judged against systematic review standards, each with fixes; 92 environmental reviews from 2015 scored a median 2.5 of 39 on CEESAT; the authors do not think all reviews must be systematic but ask all to report methods transparently. Figures wanted for B3.1: 92 and 2.5 of 39 (p. 1582); the not-all-systematic statement (p. 1583).
Register line: eight problems (pp. 1583-1586), not all reviews need be systematic (p. 1583), Box 1 (p. 1587); 92; 2.5 of 39; 8.
Verdict: PASS.
Figures checked: 92, 2.5 of 39 (p. 1582); problem 1 and "We do not believe that all reviews should be 'systematic reviews'", "transparently report their methods" (p. 1583); problem 2 (p. 1584); problem 8 (p. 1586); Box 1 (p. 1587).
Flag (no fail): the notes quote "major pitfalls in the conduct and reporting of systematic reviews" at p. 1583; it is in the abstract on p. 1582. The notes' reading that the paper "supports a narrative review that states its selection rule, its search and what it left out (p. 1583)" is an inference from the transparency sentence, not the paper's words.

### L206 (B66f) Ridoutt, Baird and Hendrie 2021, Sustainable Production and Consumption 28: 802-810
Blind summary: 9,341 Australian adult daily diets from the Australian Health Survey, scored on a planetary-boundary weighted impact (climate, water scarcity, cropland scarcity) and diet quality; a guideline-compliant lower-impact pattern cut the impact score about 15% (15.9%) with water-scarcity trade-offs; dietary change alone does not reach the boundaries. This is quadrant analysis of observed diets, not a linear programme. Figures wanted for B4.7: 15.9% and the climate and water trade-off (p. 806).
Register line: 9,341; 3.4 kg, 433 L-e, 7.1 m2; 3.5 kg, 394 L-e, 7.2 m2; 216 L-e and 5.6 m2 targets (1,100 km3, 70%, 9.7 billion); 15.9%; 34.9% down, 6.1% down, 11.6% up; 41.0; 28.9%; 17% and 21%.
Verdict: PASS.
Figures checked: 9,341, 17% and 21% (p. 803); 3.4 kg, 433, 7.1, 216, 5.6, 1100 km3, 70%, 9.7 billion, 100% climate reduction (p. 804); 41.0 for ages 19 to 50, 28.9% (p. 805); 3.5 kg, 394, 7.2 for ages 19 to 50, 15.9%, 34.9%, 6.1%, water-scarcity "increased by 11.6%", no footprint reached its target (p. 806); Meat and Livestock Australia funding (p. 808).

### L215 (B66f) Li, Yang, Yan and You 2018, Journal of Resources and Ecology 9(5): 455-460
Blind summary: short review of water resources carrying capacity methods, mostly from Chinese literature: conventional trend, system dynamics, multi-objective model analysis, comprehensive evaluation and dynamic simulation recursive; finds the methods stagnant and subjective and calls for monitoring and early-warning systems. No capacity values, nothing on Australia. Figure wanted for B4.9: the five methods (p. 455).
Register line: five methods; researcher-set indices and weights in MOMA and CE; DSR closest to physical meaning, needs long high-quality series; methods unchanged for more than ten years; no values or Australian data; first author Li.
Verdict: PASS.
Figures checked: five methods and citation line "LI Yi, YANG Yanzhao, YAN Huimin, et al. 2018" (p. 455); stock, flow, feedback, delay (p. 456, inside the cited 455-458 range); indices and weights "determined by the researchers themselves" (p. 457); section 2.5 DSR, "closer to the physical meaning", long time series and high data quality, "not changed since they were proposed more than ten years ago" (p. 458). No mention of Australia.

### L153 (B67a) Hochman, Gobbett and Horan 2017, Global Change Biology 23: 2071-2081
Blind summary: APSIM simulation at 50 sites shows water-limited wheat yield potential fell 27% from 1990 to 2015, mostly from lower rainfall and partly from heat, with rising CO2 preventing a further 4% loss; actual yields stayed flat as relative yield rose from 39% to 55%. Figures wanted for A1.5 and B8.1: 27% (p. 2071); 83% rainfall, 17% temperature (p. 2077).
Register line: 27%; 1.23 t/ha; 47 kg/ha/yr (1.1%); 4,405 kg/ha intercept "p. 2075 (Fig. 3)"; 83 and 17%; 4% with CO2 "354.4 to 400.8 ppm; pp. 2071, 2077"; 28% and 2.76 mm; 1.05 deg C; 15 of 50 sites; 39 to 55%; 25 kg; 9.2 to 12.6 Mha; notes 23 kg, 1972-1990, frost and heat.
Verdict: FAIL (citation).
Figures checked and found at citation: 27% (pp. 2071, 2075); 1.23 t/ha, 47 kg, 1.1% (p. 2075); 83%, 17%, further 4% (p. 2077) and 4% loss (p. 2071); 28%, 2.76 mm, 1.05 deg C (p. 2077); 15 of the 50 sites, none with a significant rise, 1972-1990 no trend (p. 2075); 39% to 55%, 25 kg (p. 2076); 9.2 to 12.6 Mha (p. 2072); 23 kg (p. 2079); frosts and heatwaves (p. 2077).
Not found at citation: 4,405 kg/ha appears in the regression on p. 2074 and in the Fig. 3 caption on p. 2076, not on p. 2075. CO2 354.4 and 400.8 ppm appear on p. 2074 (354.4 also p. 2075), not on pp. 2071 or 2077. Values are correct; the pages are not. Fix: "4,405; p. 2074 (Fig. 3 caption p. 2076)" and "354.4 to 400.8 ppm; p. 2074".

### L155 (B67a) Wittwer and Waschik 2021, AJARE 65: 918-936
Blind summary: dynamic regional CGE model (VU-TERM) of the 2017-19 drought and 2019-20 bushfires against a no-drought baseline: national real GDP 0.7% or more below base in 2018-19 and 2019-20; NSW 1.1% ($6.9 billion) and 1.6% ($10.2 billion) below; welfare loss present value $63 billion ($53 billion drought, $10 billion fires). Model estimates, not observed losses. Figures wanted for A1.5: 0.7% national and $53 billion (pp. 918, 932).
Register line: 0.7%; NSW 0.4/1.1/1.6% ($2.6/6.9/10.2 billion); New England-North West over 10%; 29,600 FTE (0.92%); 63/53/10; over 28; 33% NSW wheat; 1.6% agriculture share; 40 and 14%; discount rate not stated; 2020 dollars in tables.
Verdict: PASS.
Figures checked: 0.7 per cent, 1.6 per cent agriculture share, $63/$53/$10 billion (p. 918); 40 and 14 per cent (p. 919); 33 per cent wheat, ABARES and Premier and Cabinet (p. 921); 0.4, 1.1, 1.6 per cent and $2.6, $6.9, $10.2 billion (p. 926); 29,600 FTE and 0.92 per cent (p. 927); 0.7 per cent 2018-19, more than 10 per cent New England-North West (p. 928); $63, $53, $10 billion, over $28 billion, lives excluded (p. 932). Discount rate appears only as the symbol r in the welfare equation; Table 3 is in 2020 dollars.

### L183 (B67b) Mcdougall, Rader and Kristiansen 2020, Land Use Policy 94: 104554
Blind summary: Sydney urban agriculture modelled from 13 volunteer gardens (mean 5.94 kg per m2 a year) and land mapping of 20 sample blocks scaled to 6,032 blocks; 25/50/75% yard scenarios supply 15.0/24.4/33.8% of food energy for the 2.67 million residents covered; labour is the binding limit and the 75% scenario is ruled out. Figures wanted for A12.2: 15% (p. 1, Table 4 p. 8); labour limit (p. 9).
Register line: 5.94 kg and 8515 kJ per m2; 15.0/24.4/33.8% with populations; 71.1% of 10 SA4s; 8700 kJ; 15.8% and 107.5%; 670 L; 250/160/118%; 6.8/11.0/14.9 times; 21/33/46%; 6.0 h; notes on 4.9 million, 28% contaminated, 75% ruled out, and "Table 2 (pp. 3 to 4) is a review of 15 city studies, 1% to 30% of calories".
Verdict: FAIL (count in notes).
Figures checked and found: 13 gardens (p. 1); 5.94 kg, 8515 kJ, 8700 kJ, 14.7%, 2,665,234, 71.1%, 4.9 million, 20 SA1 blocks, 0.3 m imagery, 6032 blocks (p. 5); Table 3 mean 6.0 h, 670 L Dunlop (p. 6); 28% contaminated (p. 7); Table 4 15.0/24.4/33.8, 400,666, 651,002, 901,966, 15.8%, 107.5%, 1680 h (p. 8); 250/160/118%, 6.8/11.0/14.9 times, 21/33/46% (p. 9); 75% ruled out, 50% possibly (p. 10).
Not found: Table 2 (pp. 3-4) has 14 entries, 13 city studies (Burlington, Cleveland, Detroit, Guelph, Montreal, Quezon City, Toronto, Oakland, Bologna, Vancouver, Seoul, New York City, Nerima Ward) plus one all-cities global study; the paper never says 15. The "1% to 30%" range holds (p. 2). Minor: 1680 h is on p. 8, not p. 9; 250/160/118% are in Table 4 on p. 8 and the text on p. 9.

### L190 (B67b) Rosa et al. 2020, Science Advances 6: eaaz6031
Blind summary: global monthly agro-hydrological analysis finds 15% of cropland (0.14 billion ha) is rain-fed where renewable water would allow sustainable irrigation but institutions or capital are lacking, up to 25% with deficit irrigation, enough to feed 620 to 840 million more people; the Murray-Darling Basin is named among irrigated regions short of blue water for several months. Figures wanted for A12.3: 15% and 840 million (pp. 1, 3).
Register line: 15% (0.14 billion ha); 25%; 620 million (+105 km3, +6%, 0.76 x 10^15 kcal); 840 million (620 + 160 + 60); 3343 kcal; 810 vs 1083 km3; 23%; 56% (611 km3); 22% (2.23 billion); 76%; 189-235 and 317-417 million; MDB (p. 3); exclusions (p. 8).
Verdict: PASS.
Figures checked: 29 April 2020 (p. 1); 15%, 0.14 billion ha, 620 million, 105 km3, 6%, 0.76, 160 million, 60 million, up to 25%, 1083 km3, 23%, 56%, 611 km3, 76%, Murray-Darling Basin (p. 3); 189 to 235 and 317 to 417 million, high-income and arid regions (p. 4); 810 km3, 22%, 2.23 billion (p. 5); 620 to 840 million, 6 to 8%, 5 arc min, 130 crops (p. 7); 3343 kcal, Composite Runoff V1.0, Variable Monthly Flow, Mueller et al., exclusions of economic viability, nutrient supply, water quality and year-to-year fluctuation (p. 8; method range pp. 7-8 as cited).

## 4. Verdict table

| Row | Job | Verdict |
|-----|-----|---------|
| L148 | B66a | pass |
| L151 | B66a | pass |
| L156 | B66b | fail (wording: "six pathways hold cattle near 25 million"; High Value Beef goes to 20 million) |
| L161 | B66b | pass |
| L170 | B66c | pass |
| L175 | B66c | pass |
| L188 | B66d | pass |
| L222 | B66d | pass |
| L198 | B66e | pass |
| L200 | B66e | pass |
| L206 | B66f | pass |
| L215 | B66f | pass |
| L153 | B67a | fail (citation: 4,405 and 354.4 to 400.8 ppm not on the pages cited) |
| L155 | B67a | pass |
| L183 | B67b | fail (notes count: Table 2 holds 14 studies, not 15) |
| L190 | B67b | pass |

13 pass, 3 fail. No figure in any of the 16 rows was wrong in value; every failure is a page, a count or a wording.

## 5. Pattern across readers

- Values are reliable across all eight jobs: every number checked matches the paper at the paper's precision.
- The weak point is citation precision, and it grows with line length. The B67 "full" readers (B67a, B67b) carry 10 to 13 figures per row and are where pages drift to a neighbouring page: B67a cites a regression intercept and the CO2 range to the page where the related result sits rather than where the number is printed; B67b gives a figure description (1680 h) and table values to the page of the discussion rather than the table. These are off by one or two pages, never wrong in value.
- Counts of items are the second weak point: B66b ("six pathways") and B67b ("15 city studies") each state a count that is one off or that ignores an exception the paper spells out. Readers should count rows or quote the paper's own qualifier.
- Notes are less carefully cited than `what_taken`: two of the flags (B66e L200 quote placed on p. 1583 instead of p. 1582; B66b L161 calling the SDG wording the Strategy's aim) are in notes, not in the figures lists.
- Secondary figures are well handled: B66b (L156, L161) and B67a (L155) explicitly mark numbers the paper quotes from others (Wiedemann 2015a, ARCADIS 2019) or that are model estimates.

## 6. Register rows touched and ids checked

Register rows touched: none. This check edits nothing; corrections above are for the register's owner to apply.
Ids checked: L148, L151, L156, L161, L170, L175, L188, L222, L198, L200, L206, L215, L153, L155, L183, L190.

Files read: `qa/briefs/V27_blind_check_readings.md`, `qa/briefs/_checker_rules_results_wave.md`, `qa/literature_register.csv` (id, title, local_path, used_by first; what_taken and notes last), and the 16 PDFs under `/home/user/carrying-capacity-models/Literature review/` (Summerhayes2026, James2016, Mayberry2019, Mirosa2020, Hughes2017, Kumma2020, Grafton2018, Badami2015, Zhang2018, Haddaway2020, Ridoutt2021, Yi2018, Hochman2017, Wittwer2021, McDougall2020, Rosa2020_Science_Advances_Global_agricultural_economic_water_scarcity). No `.md` full texts were among these rows.
