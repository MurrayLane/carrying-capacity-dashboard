# B62: the concept papers already in the archive, read into the register (decision 37)

Brief: `qa/briefs/B62_classics_reading.md`, with the seven items of `qa/briefs/B50_literature_full_texts.md`. Checked 2026-11-09. Registers were not edited; the row updates are listed for the coordinator in section 4. No network, no git, no subagents.

## 0. Basis and how the files were read

Folder listing of `/home/user/carrying-capacity-models/Literature review/` taken first. The Cohen 1995 item is present (`Cohen1995.pdf`); `Fairlie2007.pdf` is present. **There is no `Gilland2007.pdf`**: the Gilland paper is held as `Gillard2007.pdf` (file name misspelt; the author printed on the paper is Bernard Gilland). I read that file.

| File | PDF pages | Journal pages | How read | sha256 |
|---|---|---|---|---|
| `Hardin1986.pdf` | 8 | 599-606 | text 1-8; page images 2-8 (Read) | 63aeb695bbb40bff34f8d2828211c46ef184566811a8851021ba57bf13f7bcf7 |
| `Seidl1999.pdf` | 14 | 395-408 | text 1-14 | e72a34f4ea1b731e2d5ea86b10f8eaef4fc4f307674ec411b337ae6aebf2386e |
| `Sayre2008.pdf` | 16 (1 cover) | 120-134 | text 1-16 | f4d20a6864ea63b14d3743b6d65f8dd6a758c3aedc9ba1d4b0fbaf958fb5493e |
| `Meyer1999` (file(1): PDF, 6 pages) | 6 | 209-214 | text 1-6 | 29fea1d6b6df1c0f618bcfe58f62ceba10baacb1180924d756486872431abed8 |
| `Price1999.pdf` | 22 | 5-26 | text 1-22 | dcf2c80b89059bdecb25595a81fff18723a926e614c2e461a0306406515079e8 |
| `Cohen1995.pdf` | 7 (1 cover) | 341-346 | text 1-7; page images 1-4 (Read) | 67ffb36287eca8890d20884b08caddc8e699ecc3909347c24c31996acc1b8ed7 |
| `Peters2007.pdf` | 9 | 145-153 | text 1-9 | 7b20d6e54947b1fec049edc8340a8a92da77893319631fe4142a9bcd3fc60cf8 |
| `Fairlie2007.pdf` | 12 (pdfinfo; file(1) says 8) | none printed | text 1-12; page images 1-3 (Read) | 9f634fcd98fcb291011b7ea9a4cbb4cf9fa8a2b67c0e8dcd3eacc0793b6209a1 |
| `Rees1992.pdf` (scan, no text layer) | 10 | 121-130 | page images 1-5, 6-10 (Read) | e43f14bbee1b06f369113ec5455d8340112833ff405df355c125a21f6d4d2278 |
| `Rees1996.pdf` | 21 | 195-215 | text 1-21 | 85211b24486fed4fb41abe241901bedeea14dfafa85df6b73672596d5b272a9e |
| `Hopfenberg2003.pdf` | 9 | 109-117 | text 1-9 | 69d612a101b9616cd435f95888df1ee6580d5f7ec820854bfd1728b8df3db739 |
| `Gillard2007.pdf` | 16 | 1-16 | text 1-16 | c6ec753a07763d95a8bd17ce9947d710edcb9f9c2fc5ddf4fc34ce496d2eb1c4 |
| `Chisholm2000_BHERT.pdf` | 2 | 21-22 | page images 1-2 (Read) | a5f05860b23af35da06289975b1c233c4f5b8596b8b0ba6def158410619dac49 |

**Deviation from the brief.** The brief asks for every page through the Read tool. This session runs under a rule to use the shell wherever it can do the job, so every PDF with a text layer was read in full as extracted text (pdftotext, page breaks kept, so each page is attributable), and the Read tool was used where the text layer was missing or the page order needed checking: all ten pages of Rees 1992 (a scan with no text), both pages of Chisholm (page 2 has no text layer), Hardin pages 2-8 (the extraction mixes columns, so the images fix the page of each figure), Cohen pages 1-4 (to test the register's "out of order" note) and Fairlie pages 1-3 (to see whether the tables are present). Every page of all thirteen files was read; none was skipped. The sha256 of the eight registered files match the register.

**Premises of the brief and register that do not hold:**

* "The first eight are L040 to L050": the eight registered files are L040, L041 and L044 to L049. L042 and L043 are Fearnside (not in this pass) and L050 is Wackernagel and Rees (no file; see section 3.13).
* The Gilland file is `Gillard2007.pdf`, and the paper's running head prints "Popul Environ (2006) 28:1-16" although it was accepted 2 January 2007 and published online 13 February 2007.
* The Fairlie file is not the Winter 2007-8 article in The Land that L041 names (section 1.8).
* Cohen 1995 is not out of page order (section 1.6).

---

## 1. The eight registered papers

### 1.1 Hardin 1986, L044

**(1) Citation as printed.** Garrett Hardin, "Cultural carrying capacity: a biological approach to human problems", AIBS News, *BioScience* Vol. 36 No. 9, October 1986, pp. 599-606 (the text of his AIBS Distinguished Service Award speech, 10 August 1986). No DOI is printed in the file; the register's DOI 10.1093/bioscience/36.9.599 matches the download line (academic.oup.com/bioscience/article/36/9/599).

**(2) What it argues.** Carrying capacity, defined from herd management as "the maximum number of animals that can be supported year after year without damage to the environment" (p. 600), is imprecise but indispensable, and transgressing it degrades the environment and lowers capacity in the years that follow (pp. 600-601). The prudent course is to stay well below the best estimate, as an engineer does with a bridge (p. 601). For people a bare-survival figure is "of no human use"; Hardin proposes *cultural carrying capacity*, always less than the biological capacity and inversely related to the material quality of life assumed (p. 603). He uses energy per head as a crude proxy for that quality (pp. 602-603) and argues that each territory's demand should match its own supply (pp. 604-605).

**(3) Role in the lineage.** Conceptual and normative; the proponent's case for applying the range-management concept to people, with the quality-of-life qualifier. Not a method; it gives one illustrative calculation.

**(4) Register figures.** L044 takes no figure; it records Hardin as "a critic of the concept". **Not supported**: Hardin defends the concept ("Thou shalt not transgress the carrying capacity", pp. 601, 602) and refines it for people. The page range 599-606 and the date are confirmed.

**(5) Figures bearing on capacity ranges.** Energy use per head in 1982 (UN): Ethiopia 31, world 1,823, United States 9,431 kg coal equivalent (p. 602). On that ratio the earth "might support ... about 300 billion people" at the Ethiopian energy budget, and a 40 to 50 billion claim "need not be contradicted" (p. 603); he adds that refining such a maximum is "doubtful" in worth (p. 603). Bangladesh at the world average energy per head: 104 million divided by 38 gives 2.7 million (p. 605). Nothing on Australia.

**(6) Cites Lane?** No. ("John Lane and Bodley Head" in the reference list, p. 606, is a publisher.)

**(7) Row update.** See section 4.

### 1.2 Seidl and Tisdell 1999, L045

**(1) Citation as printed.** Irmi Seidl and Clem A. Tisdell, "Carrying capacity reconsidered: from Malthus' population theory to cultural carrying capacity", *Ecological Economics* 31 (1999) 395-408, ANALYSIS section. PII S0921-8009(99)00063-4 printed (the DOI form is 10.1016/S0921-8009(99)00063-4). Tisdell's address is the University of Queensland, Brisbane.

**(2) What it argues.** The concept rests on Malthus, whose theory was "based on normative assertions and on a mechanistic conception of nature and society" (p. 398), and on the logistic equation, whose fixed r and K, closed system and fixed boundaries do not allow an unequivocal calculation of the upper limit (p. 399). Applied ecology (range, wildlife, tourism) shows several carrying capacities, each tied to a management aim (p. 402). For people the concept becomes social or cultural (biophysical capacity KB at least as large as social capacity KS, p. 403) and its level depends on a chosen social welfare function (pp. 404-405); this shifts it "from a positivist-type concept to a normative one" with "no longer an objective, single level" (p. 405). They conclude that claims of scientific, objectively determined human capacities are untenable and that carrying capacities "are far from being universal constants" (p. 407).

**(3) Role.** Conceptual review and critique; the main source for the normative character of human carrying capacity.

**(4) Register figures.** None taken; "critic of the concept" is supported.

**(5) Figures.** Earth capacity estimates "range between less than 1 billion and 1000 billion" (p. 399, citing Cohen 1995b p. 342). Three reasons the logistic predicts poorly (p. 401). No Australian figure.

**(6) Cites Lane?** No.

### 1.3 Sayre 2008, L046

**(1) Citation as printed.** Nathan F. Sayre, "The Genesis, History, and Limits of Carrying Capacity", *Annals of the Association of American Geographers* 98(1) 2008, pp. 120-134, DOI 10.1080/00045600701734356 (cover page).

**(2) What it argues.** Four uses of the term are traced (p. 120): an engineered attribute of ships from about 1840 (earliest find 1845, p. 122); an attribute of range and game from the 1870s; K of population biology after Odum 1953; and the neo-Malthusian number of people the earth can support after Vogt 1948. In all four the concept is "ideal, static, and numerical", fitting only the first (p. 120). Range scientists in turn rejected it ("Sustained grazing capacity does not exist", p. 126), and logistic growth is rarely if ever observed in the field (p. 129). "If carrying capacity is conceived as static, it is theoretically elegant but empirically vacuous; but if it is conceived as variable, it is theoretically incoherent or at best question-begging" (p. 131). Limits are real but "rarely static or quantifiable" (p. 132).

**(3) Role.** Intellectual history; the fullest lineage source on hand.

**(4) Register figures.** None taken; "critic" supported.

**(5) Figures bearing on Australia.** An 1889 report of "Australian records": under ten inches of rain land is valueless without irrigation; one sheep per square mile per inch of rain; about twenty sheep a square mile more from nine to thirteen inches and seventy from thirteen to twenty (p. 124, citing *Science* 1889). Australian grazing leases were set by stock capacity (p. 124). The strongest critiques of range carrying capacity came from Australia and Africa (Westoby 1980; Westoby, Walker and Noy-Meir 1989; p. 126). Northern Rhodesia: Allan's land carrying capacity method led to about 52,000 people moved of 160,800 calculated (p. 127). Godwin's 1820 figure of 9 billion (p. 121).

**(6) Cites Lane?** No.

### 1.4 Meyer and Ausubel 1999, L047

**(1) Citation as printed.** Perrin S. Meyer and Jesse H. Ausubel, "Carrying Capacity: A Model with Logistically Varying Limits", *Technological Forecasting and Social Change* 61, 209-214 (1999), PII S0040-1625(99)00022-0.

**(2) What it argues.** Models of human growth with a fixed limit "are unrealistic" because technology changes how resources are used (p. 209). The authors let carrying capacity itself rise logistically from k1 to k2 (eqs. 2 to 5, p. 210), which produces "bi-logistic" growth (p. 211). Fitted to England 1541-1975 and Japan 1100-1992, the model dates each industrial revolution (pp. 212-213). The present limits in England and Japan "cannot conceivably be set by food", and future numbers "will require more than estimates of carrying capacity" (p. 213).

**(3) Role.** A formal model of a moving limit (logistic with time-varying K); six parameters fitted by simulated annealing (p. 211).

**(4) Register figures.** None. "Critic of the concept" is **only partly supported**: the paper criticises a fixed K and proposes an extension; it does not reject the concept.

**(5) Figures.** Cohen archives "26 different attempts" (p. 209). Pearl's single logistic gave 2 billion for the globe (p. 212). England: k1 about 5 million by 1650, a second pulse of 50 million, midpoint 1850, characteristic duration 138 years (p. 212). Japan: k1 35 million, about 90 million more, midpoint 1908, 77 years (p. 213). No Australian figure.

**(6) Cites Lane?** No.

### 1.5 Price 1999, L048

**(1) Citation as printed.** David Price (Cornell University), "Carrying Capacity Reconsidered", *Population and Environment: A Journal of Interdisciplinary Studies* 21(1), September 1999, pp. 5-26. No DOI printed.

**(2) What it argues.** The term has long been called unclear, and some ecologists propose abandoning it (p. 6). The logistic fits laboratory cultures but field examples are almost absent (p. 9); limits are multiple and variable (p. 11), and density-dependent regulation needs a constant limit that variable environments do not supply (p. 13). He concludes the concept "is seriously flawed" and "may be no more than a self-validating belief" (p. 17). He replaces it with a windfall effect: populations grow on an unexpected resource and crash when it is spent (pp. 19-21), and argues that human growth since the industrial revolution is such a windfall from fossil fuels, so "the earth has no 'carrying capacity' for a human population in excess of its current level" (p. 23).

**(3) Role.** Critique of the ecological basis, followed by its own limit argument.

**(4) Register figures.** None. "Critic" supported, with the note that Price ends with a strong limit claim of his own.

**(5) Figures bearing on Australia.** The one textbook field example of logistic growth, sheep in Tasmania in the nineteenth century, levelled because farmers chose not to overstock (Davidson 1938; pp. 9-10, Figure 2). Pearl and Reed's US asymptote of about 197 million against 270 million reached (p. 18). Reindeer on St Matthew Island: 29 to about 6,000 in 19 years, then 42 (pp. 20-21).

**(6) Cites Lane?** No.

### 1.6 Cohen 1995, L049

**(1) Citation as printed.** Joel E. Cohen, "Population Growth and Earth's Human Carrying Capacity", *Science* Vol. 269, 21 July 1995, pp. 341-346; DOI 10.1126/science.7618100 (AAAS cover sheet, PDF page 7).

**(2) What it argues.** Earth's capacity "is determined both by natural constraints and by human choices", so it is "dynamic and uncertain", and "human choice is not captured by ecological notions of carrying capacity" (p. 341). Published estimates since 1679 range "from <1 billion to >1000 billion" and diverge over time, the opposite of a constant of nature being measured (p. 342). He groups the methods into six (regional densities, curve fitting, a single constraint such as Penck's food formula, reduction to one factor such as land area, several independent factors under Liebig's law, and system models), notes that the first five are deterministic and static, and that no probabilistic global approach exists, only Fearnside's local one (pp. 342-343). A national capacity "cannot be defined ... independently of other regions if that nation trades" (p. 343). Simple Malthus-Condorcet models with a variable K(t) reproduce the observed growth path (pp. 343-344).

**(3) Role.** Synthesis and method typology; the source for the scatter of estimates and the choice-dependence of human capacity.

**(4) Register figures.** None taken. The register note that "the PDF's pages are out of order (it opens on the reference list)" is **not correct**: the pages run 341 to 346 in order; page 341 carries, at its head, the last notes (73 to 76) of the preceding *Science* article, which is why it looks like a reference list. "Critic" is broadly supported (he rejects ecological notions as adequate for people, p. 343) but Cohen also models capacity formally.

**(5) Figures.** Median of 65 upper bounds 12 billion; using the lower figure of each range, 7.7 billion; UN 2050 projections 7.8 to 12.5 billion (p. 342). Estimates published in 1994 alone ran from <3 to 44 billion (p. 342). Nine definitions of non-human carrying capacity, none adequate for humans (p. 343). A stochastic measure could ask what population "could be maintained 95 years in 100" (p. 343), the same question as Fearnside's failure probability. Australian link: note 18 (p. 345) records that Knibbs used the food-supply formula in 1917 in the Commonwealth Census report (Melbourne).

**(6) Cites Lane?** No.

### 1.7 Peters, Wilkins and Fick 2007, L040

**(1) Citation as printed.** Christian J. Peters, Jennifer L. Wilkins and Gary W. Fick, "Testing a complete-diet model for estimating the land resource requirements of food consumption and agricultural carrying capacity: The New York State example", *Renewable Agriculture and Food Systems* 22(2); 145-153, doi:10.1017/S1742170507001767 (p. 145). Accepted 22 December 2006.

**(2) What it estimates.** A spreadsheet model computes land a person a year for 42 diets (meat and eggs 0 to 381 g a day; fat 20 to 45% of energy; 2,308 kcal), with US loss factors and New York yields for 1999-2003 (pp. 147-148). Land is in three classes: 712 thousand ha usable for all crops, 1,063 thousand ha limited to perennial crops and pasture, and 255 thousand ha pasture, 2,031 thousand ha in all (pp. 148-149); capacity is set by whichever class limits (eq. 2, p. 149). Land per person runs 0.18 to 0.86 ha (p. 149), but capacity varies only threefold, 6.08 to 2.04 million (p. 150), because high-meat diets use the land fit only for pasture and perennials (p. 152). The state could feed about 21% of its population on a 190 g meat, 30% fat diet (p. 152).

**(3) Method family.** Resource-based land and diet (complete-diet land requirement), at state scale, with land-quality classes.

**(4) Register figures.** L040 takes no figure. The DOI and authors are confirmed. B242 places Peters with the balance at other scales: supported. OUTLINE section 6 attributions: "Peters applies US loss rates" confirmed (USDA loss and processing factors, p. 148); "Peters's US diets turn on grazing land" confirmed in substance (pp. 149-152); "Peters finds results highly sensitive to cultivable cropland" **not found in this paper** (it shows the limiting land class changes with diet, pp. 149-152, but makes no sensitivity statement; the claim may come from Peters 2009 or 2016).

**(5) Figures.** A difference inside the paper: the abstract gives 2.0 to 6.2 million (p. 145), the results 2.04 to 6.08 million (p. 150); quote the results. Land per edible energy 0.6 m2 a Mcal (sugar) to 54.6 (lean beef); beef 31 times grain (p. 149). Meat explains 97.2% of the variation in land per person and 87.2% of that in capacity (pp. 149-150). Average US intake 163 g meat and eggs a day (p. 147). No Australian figure.

**(6) Cites Lane?** No.

### 1.8 Fairlie, "Can Britain Feed Itself?", L041

**(1) Citation as printed.** The file prints only "9 / Can Britain Feed Itself?" and the Mellanby 1975 epigraph (PDF p. 1): no author, journal, date, page numbers or DOI. **It is not the Winter 2007-8 article** the register names: the text says "After the foregoing projections were published in The Land magazine in 2008" (PDF p. 11) and gives organic wheat yields for 2007 and 2009 (PDF p. 6), and the heading "9" reads as a chapter number. It is a revised version, probably a book chapter by Simon Fairlie; its source should be identified before it is cited (a lead, not confirmed here: Fairlie's 2010 book *Meat: A Benign Extravagance* has a chapter of this title). The tables it refers to (A to H) are not in the file (PDF pp. 1-3 viewed as images; no table present).

**(2) What it estimates.** Fairlie repeats Mellanby's 1975 "back of the envelope" land budget for UK self-sufficiency (PDF p. 1) under six regimes: chemical, organic and permacultural, each with and without livestock. Chemical stockless farming uses the least land (PDF p. 3); orthodox organic livestock farming uses the most and has "the most difficulty sustaining the full UK population on the land available" (PDF p. 12); a livestock permaculture with grass-fed dairy, pigs on food waste and sewage recycling feeds the population, a share of fibre and the farm fuel on 13.4 Mha, a little over half the country, against nearly 16 Mha for orthodox organic (PDF pp. 8-9). He calls the results "a rough guide" (PDF p. 1).

**(3) Method family.** Resource-based land and diet (Mellanby-style land budget by diet and farming system), national scale.

**(4) Register figures.** None taken. B242 family placement supported.

**(5) Figures.** Mellanby 1975: 15 Mt cereals on under 3.6 Mha, 283 kg a person, about 2,700 kcal a day for 53 million (PDF p. 1); organic needs about 33% more land (PDF p. 2). Same diet for 60.6 million on 86% of the 1975 arable area (PDF pp. 2-3). Chemical stockless could give "a semblance of an animal-based diet ... for about 200 million people" (PDF p. 3). Vegan organic needs 14% more arable land than in use (PDF p. 4). 22 Mha of non-urban land (PDF p. 6). A slip in the text: "over seven tonnes per acre" for 2004 grain (PDF p. 2) reads as per hectare. No Australian figure.

**(6) Cites Lane?** No.

---

## 2. The five papers not in the register

### 2.1 Rees 1992 (new row)

**(1) Citation as printed.** William E. Rees, "Ecological footprints and appropriated carrying capacity: what urban economics leaves out", *Environment and Urbanization*, Vol. 4, No. 2, October 1992, pp. 121-130 (first presented at the Globe '92 Conference, Vancouver, March 1992). No DOI printed.

**(2) What it argues.** Defines carrying capacity for people as the maximum rate of consumption and waste discharge sustainable in a region without impairing its ecosystems, and inverts it: "How much land in various categories is required to support the region's population indefinitely at a given material standard?" (p. 125). The answer is the "ecological footprint"; urban regions "appropriate" capacity from elsewhere through trade (pp. 125-126). Trade lets regions exceed their own capacity without feedback (p. 126). Mainstream economists reject the concept on grounds of technology and substitution; Rees holds it "fundamental to demographic/resource analysis" (p. 129).

**(3) Role.** The founding statement of appropriated carrying capacity and the footprint (with Wackernagel 1991 cited, p. 125, note 17).

**(4) Register figures.** None (unregistered). It does not state an equivalence factor (bears on L050, section 3.13).

**(5) Figures.** Lower Fraser Valley: 1.9 ha a person for food and 3 to 4 ha of forest; 1.7 million people need 8.3 Mha against a valley of 400,000 ha, "at least 20 times" (pp. 125-126). The world's 5.2 billion at that rate would need 25.5 billion ha against 8.8 billion ha productive (p. 129). Food land at 5.5 people a hectare: 17.1 Mha a year for 94 million more people (p. 130). Nothing on Australia.

**(6) Cites Lane?** No.

### 2.2 Rees 1996 (new row)

**(1) Citation as printed.** William E. Rees, "Revisiting Carrying Capacity: Area-Based Indicators of Sustainability", *Population and Environment: A Journal of Interdisciplinary Studies* 17(3), January 1996, pp. 195-215. No DOI printed.

**(2) What it argues.** "This article sides solidly with Hardin" (p. 196): capacity should be read as the maximum human *load* (population times consumption), not a population (p. 197). Technology raises efficiency, not capacity, and rebound can erode it; trade only displaces load to export regions (pp. 201-203). Human carrying capacity is redefined as the maximum sustainable harvest and waste rate "wherever the latter may be located", and inverted into the area needed (p. 203). Footprints show most "advanced" countries running ecological deficits (p. 207, Table 1 p. 209); "not all countries or regions can be net importers of carrying capacity" (p. 210).

**(3) Role.** The footprint method stated as carrying capacity revisited; lineage for the footprint family in section 4 of Paper B.

**(4) Register figures.** None (unregistered). No equivalence factor; the Netherlands food footprint is "based on world average productivities" (p. 207).

**(5) Figures.** Fair Earthshare about 1.5 ha a person (Box 3, p. 205). Vancouver: about 4.2 ha a person, 2.0 Mha for 472,000 people on 11,400 ha, about 174 times (pp. 206-207). Netherlands 14 to 15 times its area (p. 207). 5.8 billion at 4.5 ha would need 26 billion ha against 8.8 billion (p. 210). Table 1 (p. 209) covers Japan, Korea, European countries, Canada and the United States; no Australia.

**(6) Cites Lane?** No.

### 2.3 Hopfenberg 2003 (new row)

**(1) Citation as printed.** Russell Hopfenberg (Duke University), "Human Carrying Capacity Is Determined by Food Availability", *Population and Environment* Vol. 25, No. 2, November 2003, pp. 109-117. No DOI printed.

**(2) What it argues.** Taking the FAO food production index as a time-varying K(t) in the logistic equation reproduces world population 1962-2000 (pp. 112-115). He concludes that human numbers, like those of other species, are "a function of increases in food availability" (p. 116), and that hunger reflects distribution, not total supply (p. 114).

**(3) Role.** A variable-K logistic with food as the single driver (Cohen's third method family, applied dynamically).

**(4) Register figures.** None (unregistered).

**(5) Figures.** K in 2000 is 23.06 billion, 3.79 times population (p. 114). The K series is the index scaled to the 1962 population and then multiplied by a constant of 2.487 chosen "to generate a good fit", with r fixed at 0.03 (p. 114), so the level of K is set by the fit rather than by a food requirement; any use of the 23.06 billion should say so. No Australian figure.

**(6) Cites Lane?** No.

### 2.4 Gilland 2006/2007 (new row; file `Gillard2007.pdf`)

**(1) Citation as printed.** Bernard Gilland, "Population, nutrition and agriculture", *Popul Environ* (2006) 28:1-16, DOI 10.1007/s11111-007-0034-9; received 20 September 2006, accepted 2 January 2007, published online 13 February 2007 (p. 1).

**(2) What it estimates.** Human carrying capacity is treated as a function of food consumption per head (abstract, p. 1). An estimate "can be defensible if it is based on assumptions that apply to a specific year or period, and is not taken as an ultimate limit", and capacity differs from the most people who could be kept alive and from an optimum population (pp. 1-2). With a minimum diet of 40 g animal protein a day (p. 4), the cereal need is about 420 kg a person a year; at 340 kg produced, the world exceeds its capacity by about 25% and the less-developed countries by about 50% (p. 8). With 3,200 Mt of cereals in 2050 the most people who could have 40 g of animal protein is 7.4 billion (p. 11).

**(3) Method family.** Single-constraint food balance (cereal requirement per head from a diet standard), global and regional.

**(4) Register figures.** None (unregistered). Gilland says Cohen "considers the concept to be unscientific" (p. 1); the Cohen 1995 article does not say this (it says the estimates deserve "profound skepticism", p. 342), so do not carry that reading forward.

**(5) Figures.** Supply exceeds intake by 27% (US 2003: 2,757 kcal eaten of 3,754 supplied; UK 1986-88 the same, p. 5), a waste allowance comparable to the model's loss factors. Feed-to-animal-protein ratio 17 (p. 7). New Zealand pasture about 9 t grain equivalent a head (p. 8). Australia appears only as one of the more-developed countries (p. 9).

**(6) Cites Lane?** No.

### 2.5 Chisholm 2000 (new row)

**(1) Citation as printed.** "Land, resources and the idea of carrying capacity", extracted from a paper by Anthony Chisholm (Emeritus Professor, formerly Professor and Head of Agricultural and Resource Economics, La Trobe University, 1988-99) on the Business Council of Australia web site; *BHERT News*, 2000, pp. 21-22. The download line gives search.informit.org/doi/10.3316/aeipt.102627. Two pages; a magazine extract, not a peer-reviewed paper.

**(2) What it argues.** The idea that Australia's population is limited by land and resources "has endured for almost 80 years"; the evidence is that "resource deficiencies need not set population limits in economies that are open to change and technology" (p. 21). Farm output rose about two and a half times over 1950-90 (2.5% a year) with little more land or water, through knowledge (p. 21); land degradation is real but is not linked to population level and is better handled by environmental management (pp. 21-22). For a small trading country world prices are the relevant scarcity measure (p. 22).

**(3) Role.** The economist's case against capacity as a population limit, in the Australian debate.

**(4) Register figures.** Not in the register, but it is a second-hand route to L002: "the estimates made in 1975 by CSIRO scientists ... Australia could feed 60 million people (82 million) at existing per capita food protein (energy) consumption levels" (p. 21). This matches L002 (60 protein, 82 energy).

**(5) Figures bearing on Australia, not in L002.** The same CSIRO work: expanding irrigation to the maximum feasible area "would require an Australian population of 140 million, at present per capita urban water use rates, to absorb Australia's water resources" (p. 21). Australia could be self-sufficient in food, water, energy and minerals (oil apart) "with a much larger population (of the order of at least 50 million)" (p. 22). Productivity gain worth about $15 billion a year against land degradation of about $0.6 billion a year, 1988-89 dollars (p. 21). The National Population Inquiry (1974) "succinctly drew together attempts to estimate the carrying capacity of Australia" (p. 21).

**(6) Cites Lane?** No.

---

## 3. Paper B section 2, "The concept and its critics": points these papers can carry

Written in neutral terms (decision 33): each point states what a source shows or argues, not who was wrong.

1. **The term began in engineering and trade.** "Carrying capacity" first described the cargo a ship could carry (earliest found use 1845) before it described living systems; four uses can be told apart: engineered systems, range and game, the K of population biology, and the number of people the earth can support (Sayre 2008, pp. 120, 122).
2. **Range management gave the working definition, with Australia an early case.** By 1889 Australian records were cited for sheep per square mile per inch of rain, and Australian grazing leases were set by stock capacity (Sayre 2008, p. 124). The herd-management definition is the largest number "supported year after year without damage to the environment" (Hardin 1986, p. 600); "without injury" needs a judgement of what counts as injury (Seidl and Tisdell 1999, pp. 400-401).
3. **The link to the logistic K came in 1953.** Odum named the upper asymptote of the logistic "carrying capacity" (Sayre 2008, pp. 127-128; Price 1999, pp. 6-7).
4. **Field support for a fixed K is thin.** Logistic growth is shown in laboratory cultures but rarely in the field (Price 1999, p. 9; Sayre 2008, p. 129); the classic field case, nineteenth-century Tasmanian sheep, levelled because farmers limited stocking (Price 1999, pp. 9-10). Range scientists in turn concluded that sustained grazing capacity "does not exist" on semi-desert ranges, and some of the strongest critiques came from Australian rangeland ecology (Sayre 2008, p. 126).
5. **Global estimates scatter widely and do not converge.** Estimates since 1679 run from under 1 to over 1,000 billion, and the scatter grows with time; the median of 65 upper bounds is 12 billion and of the lower bounds 7.7 billion (Cohen 1995, p. 342; Seidl and Tisdell 1999, p. 399). This is the world-scale counterpart of the 9 to 100 million spread in Paper B section 1.
6. **A typology of methods already exists at world scale.** Cohen groups estimates into six methods, from regional densities and curve fitting to a single constraint (Penck's food formula), reduction to one factor (land area), several independent factors (Liebig's law) and system models; the first five are deterministic and static (Cohen 1995, pp. 342-343). Paper B's catalogue (section 4) can be set against this.
7. **Human capacity depends on choices as well as on nature.** Diet, technology, distribution, institutions, risk and time horizon all enter (Cohen 1995, p. 343); human capacity is a social or cultural capacity no larger than the biophysical one (Seidl and Tisdell 1999, p. 403) and falls as the assumed quality of life rises (Hardin 1986, p. 603).
8. **The concept becomes normative when applied to people.** The level depends on value judgements and on a chosen social welfare function, so there is "no longer an objective, single level" (Seidl and Tisdell 1999, pp. 404-405, 407). Hardin, from the opposite starting point, reaches a similar place: the proper cultural capacity turns on "our expectations for the quality of life" (Hardin 1986, p. 603).
9. **The limit can be modelled as moving.** Logistic growth under a capacity that itself rises (Meyer and Ausubel 1999, pp. 210-213), a capacity that responds to population (Cohen 1995, pp. 343-344), or a capacity driven by food supply (Hopfenberg 2003, pp. 112-114) each reproduce observed population paths; fitted parameters, not measured requirements, set the level in these models (Meyer and Ausubel 1999, p. 211; Hopfenberg 2003, p. 114).
10. **A static or a variable capacity each has a cost.** A static capacity is "theoretically elegant but empirically vacuous", a variable one hard to make coherent (Sayre 2008, p. 131); a limit inferred from its supposed effect risks being self-validating (Price 1999, p. 17).
11. **Capacity figures have carried policy weight.** Colonial land policy in Northern Rhodesia moved about 52,000 people on carrying capacity calculations (Sayre 2008, p. 127), and the concept's appeal to agencies lies partly in its appearance of precision (Sayre 2008, p. 132). This supports Paper B's emphasis on stating the question and the uncertainty with every figure.
12. **Trade and the unit of analysis matter.** A trading nation's capacity cannot be defined on its own (Cohen 1995, p. 343); trade lets regions run beyond local capacity by drawing on other regions (Rees 1992, p. 126; Rees 1996, pp. 202-203); Hardin argues for matching local demand to local supply (Hardin 1986, pp. 604-605). Peters et al. and Fairlie ask the bounded, self-sufficiency form of the question for a state and a country (Peters et al. 2007, p. 147; Fairlie, PDF p. 1). This is the conceptual root of Paper B's export and scale choices.
13. **Inverting the ratio gives the footprint.** Asking how much land a population needs, rather than how many people a land can hold, turns carrying capacity into an area indicator, the ecological footprint (Rees 1992, p. 125; Rees 1996, pp. 203-205).
14. **Diet changes the answer by a large factor.** On one land base, diet alone moves capacity threefold (2.04 to 6.08 million for New York State) and land per person nearly fivefold, the gap narrowing because meat-rich diets use land fit only for pasture (Peters et al. 2007, pp. 149-152). A dietary standard (40 g of animal protein a day) is what turns a cereal supply into a capacity (Gilland 2006, pp. 4, 8).
15. **A margin for bad years is part of the concept.** Staying well below the best estimate is the prudent use (Hardin 1986, p. 601); under uncertainty society should "err on the safe side" (Seidl and Tisdell 1999, p. 407); a stochastic measure would ask what population can be kept "95 years in 100" (Cohen 1995, p. 343). This is the lineage for the failure-probability view (Fearnside) in sections 4 and 6.
16. **An estimate is tied to its period.** An estimate is defensible when its assumptions apply to a stated year and it is not read as an ultimate limit; capacity is neither the most people who could be kept alive nor an optimum (Gilland 2006, pp. 1-2).
17. **Australia's debate has long used the concept, and has long had an economic counter-view.** The idea that land and resources limit Australia's population has a long history, while an economist's reading is that open economies are not limited by resource endowments and that land degradation is not tied to population level (Chisholm 2000, pp. 21-22); the same piece reports the CSIRO 1975 figures of 60 million (protein) or 82 million (energy) and 140 million to absorb the water resources (Chisholm 2000, p. 21).

### 3.1 Which points still need a post-2016 source (recency rule)

The section is to lead with the recent debate and use these classics for lineage only. On the register's labels and B61:

* **Points 1 to 4 (lineage, definitions, the logistic):** lineage only; the classics are the right sources. Chapman and Byron 2018 (L088, read) can stand as the recent ecological view of the same lineage.
* **Points 5, 7 and 8 (scatter, choices, normative character):** need a post-2016 lead. On hand and read: Cohen 2017 (L106) and Tucker 2020 (L107), both "read, not stored"; Wang 2022 (L109, read) for the land carrying capacity index literature. These are the natural openers; the 1995 and 1999 texts then supply lineage.
* **Point 6 (method typology):** no post-2016 method typology on hand (B61 point B1.2, candidate van den Bergh and Rietveld 2004, itself older). Paper B's own catalogue may be the recent contribution; say so.
* **Points 9 and 10 (moving limit; static against variable):** no post-2016 source on hand that takes up the moving-limit models. Needs one, or keep these as lineage.
* **Point 11 (policy weight of capacity figures):** no recent source on hand; B61 point B2.6 is already marked thin.
* **Points 12 and 13 (trade, scale, footprint):** recent sources on hand and read: Wackernagel et al. 2019 (L129) for the footprint; Fader et al. 2013 (L105) is pre-2016. A post-2016 source on trade and national capacity is still needed.
* **Point 14 (diet):** well covered by recent work read in this project (Peters et al. 2016, L015; Alexander et al. 2016; Schon and Bohringer 2023, L114); Peters 2007 and Gilland become lineage.
* **Point 15 (margin for bad years):** no post-2016 conceptual source on hand; the project's own failure-probability test carries it.
* **Point 16 (estimate tied to a period):** no recent source; can rest on Gilland as lineage or be stated as the paper's own position.
* **Point 17 (Australian debate):** needs post-2016 Australian sources; this is the gap B63 (decision 38) is sweeping for. Chisholm 2000 is lineage and a magazine extract, so it should not lead.

---

## 4. Row updates for the coordinator

### 4.1 Literature register, existing rows

| Row | `read_or_reported` | `what_taken` (proposed) | Corrections and notes |
|---|---|---|---|
| L040 Peters et al. 2007 | read | Complete-diet land model for New York State: 42 diets, 0.18 to 0.86 ha a person (p. 149); capacity 2.04 to 6.08 million from 2.03 Mha in three land classes (pp. 148-150; abstract rounds to 2.0 to 6.2); state feeds about 21% of its people on a 190 g meat diet (p. 152); USDA loss factors (p. 148) | Title, authors, DOI confirmed from p. 145. Peters 2009 is a different paper; the short form "Peters (New York State)" is best tied to this row for the method. OUTLINE s6 "highly sensitive to cultivable cropland" not found in this paper |
| L041 Fairlie | read | Mellanby-style UK self-sufficiency land budget under six farming regimes; chemical stockless least land, orthodox organic livestock most; livestock permaculture on 13.4 Mha (PDF pp. 8-9); conclusion PDF p. 12 | **Correction:** the file is a revised version, not the Winter 2007-8 article in The Land (text cites publication in The Land in 2008 and yields to 2009; headed "9"). 12 PDF pages (pdfinfo; file(1) says 8). No author or date printed; tables A to H absent. Identify the source (lead: Fairlie 2010, *Meat: A Benign Extravagance*, unconfirmed) before citing; cite it by PDF page |
| L044 Hardin 1986 | read | Definition from herd management (p. 600); imprecise but needed, stay well below the best estimate (pp. 600-601); cultural carrying capacity, always below biological capacity and inversely related to quality of life (p. 603) | **Correction:** "critic of the concept" not supported; Hardin is a proponent who refines the concept. Pages 599-606 confirmed |
| L045 Seidl and Tisdell 1999 | read | Human capacity is social and normative, no single objective level (pp. 403-407); KB at least KS (p. 403); estimates <1 to 1,000 billion (p. 399) | Citation confirmed; Tisdell at the University of Queensland |
| L046 Sayre 2008 | read | Four historical uses; static capacity "empirically vacuous", variable capacity question-begging (pp. 120, 131); Australian rangeland origins (p. 124) and critiques (p. 126) | Citation and DOI confirmed (cover page) |
| L047 Meyer and Ausubel 1999 | read | Logistic growth under a logistically rising capacity; England and Japan fits (pp. 210-213) | "Critic" only partly supported: proposes an extension of the concept, criticises a fixed K (p. 209) |
| L048 Price 1999 | read | Concept "seriously flawed", possibly "self-validating" (p. 17); windfall effect in place of K; no capacity above the current population (p. 23); Tasmanian sheep plateau from stocking decisions (pp. 9-10) | Pages 5-26 confirmed; no DOI printed |
| L049 Cohen 1995 | read | Capacity dynamic and choice-dependent (pp. 341, 343); estimates <1 to >1,000 billion, medians 7.7 and 12 billion of 65 (p. 342); six method families (pp. 342-343); national capacity undefined for a trading nation (p. 343) | **Correction:** pages are in order (341-346); page 341 opens with notes 73 to 76 of the preceding article. DOI confirmed on the cover sheet |
| L050 Wackernagel and Rees | no change | no change | Neither Rees 1992 nor Rees 1996 states an equivalence factor (Rees 1996 p. 207 uses "world average productivities"); add this to the note. B037 is already withdrawn (X044) |

### 4.2 Literature register, new rows (proposed ids follow the last id, L138)

| Proposed id | Kind | Title as printed | Origin | local_path | sha256 | read_or_reported | what_taken |
|---|---|---|---|---|---|---|---|
| L139 | journal article | Rees 1992, "Ecological footprints and appropriated carrying capacity: what urban economics leaves out", *Environment and Urbanization* 4(2): 121-130 | no DOI printed | carrying-capacity-models/Literature review/Rees1992.pdf | e43f14bbee1b06f369113ec5455d8340112833ff405df355c125a21f6d4d2278 | read | Capacity inverted into the land a population needs (p. 125); Fraser Valley 20 times its area (p. 126); no equivalence factor |
| L140 | journal article | Rees 1996, "Revisiting Carrying Capacity: Area-Based Indicators of Sustainability", *Population and Environment* 17(3): 195-215 | no DOI printed | .../Rees1996.pdf | 85211b24486fed4fb41abe241901bedeea14dfafa85df6b73672596d5b272a9e | read | Capacity as maximum load (p. 197); redefinition and footprint (pp. 203-205); fair Earthshare 1.5 ha (p. 205); world average productivities (p. 207) |
| L141 | journal article | Hopfenberg 2003, "Human Carrying Capacity Is Determined by Food Availability", *Population and Environment* 25(2): 109-117 | no DOI printed | .../Hopfenberg2003.pdf | 69d612a101b9616cd435f95888df1ee6580d5f7ec820854bfd1728b8df3db739 | read | Logistic with K(t) from the FAO food index; K 23.06 billion in 2000, level set by a fitted constant 2.487 (p. 114) |
| L142 | journal article | Gilland, "Population, nutrition and agriculture", *Popul Environ* (2006) 28: 1-16 | https://doi.org/10.1007/s11111-007-0034-9 (printed) | .../Gillard2007.pdf (file name misspelt) | c6ec753a07763d95a8bd17ce9947d710edcb9f9c2fc5ddf4fc34ce496d2eb1c4 | read | Capacity as population fed 420 kg cereals with 40 g animal protein; world 25% and LDCs 50% over (p. 8); 7.4 billion in 2050 (p. 11); estimates tied to a period (pp. 1-2) |
| L143 | magazine extract | Chisholm, "Land, resources and the idea of carrying capacity", *BHERT News* 2000: 21-22 (extract of a Business Council of Australia paper) | download line: search.informit.org/doi/10.3316/aeipt.102627 | .../Chisholm2000_BHERT.pdf | a5f05860b23af35da06289975b1c233c4f5b8596b8b0ba6def158410619dac49 | read | Economic counter-view in the Australian debate (pp. 21-22); reports CSIRO 1975: 60 million (protein), 82 million (energy), 140 million to absorb water (p. 21); "at least 50 million" self-sufficient (p. 22) |

For **L002** (CSIRO 1975, Gifford et al.): add to notes that Chisholm 2000 p. 21 (L143) reports the same 60 and 82 million and adds the 140 million water figure from the same work; still second-hand.

### 4.3 Claims register

No claims-register row cites L044 to L049. B242 cites L040 and L041; its family placement is supported by both texts. B037 (L050) is withdrawn. No row cites Rees 1992 or 1996, Hopfenberg, Gilland or Chisholm.

### 4.4 Characterisations the texts do not support

* L044 and OUTLINE s2 listing Hardin among "critics": Hardin argues for the concept (pp. 601-603).
* L047 "critic": Meyer and Ausubel extend the concept with a moving limit.
* OUTLINE s6 "Peters finds results highly sensitive to cultivable cropland": not in Peters et al. 2007.
* L041: the file is not the 2007-8 article it is matched to.
* L049 note: Cohen's pages are not out of order.
* Gilland's "Cohen considers the concept unscientific" (Gilland p. 1): not what Cohen 1995 says.
