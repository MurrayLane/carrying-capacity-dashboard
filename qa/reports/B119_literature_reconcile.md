# B119: literature reconciled after the revisions (decision 111)

Brief: `qa/briefs/B119_literature_reconcile.md`. No git, no subagents. Network use: open-access and government pages only, one request at a time, a plain client string, nothing about the project in any request. Where a server refused, the refusal is recorded below and nothing was bypassed. Written: `qa/literature_register.csv`, `qa/references.csv`, files in the archive, and this report. No paper file and not `qa/claims_register.csv` were touched; what each needs is listed in section 9.

## 1. Outcome in plain words

* Cited sets: Paper A cites **58** works, Paper B **127**, 151 distinct across both (32 in both before the new rows). Every one has a literature row and a references row. The drops named by B117 (31 rows, for Paper A) and B118 (10 rows, for Paper B) hold for the paper each report covers: none of the 31 is cited by Paper A and none of the 10 by Paper B. Six of B117's 31 (L103, L163, L182, L190, L192, L227) are still cited by Paper B, and L115 from B118's list is still cited by Paper A, so those seven rows are not marked uncited.
* **38** references rows are cited by neither paper and are marked `status` = "uncited (B119)" (a new `status` column; nothing was deleted).
* **7** rows added for the works B117 and B118 named (L247 to L253), **4** more for referee-named works fetched and filed (L254 to L257).
* The "not seen" labels: 30 claims rows (18 in Paper A, 12 in Paper B) rest on 24 works. **20 works were read** from a file found on disk or fetched; **4 stay unseen**: L002 (second-hand by decision 39), L080 (Kastner 2012), L086 (Goldfinger 2014) and L235 (McKay et al. 1979). Murray's list adds Saltelli 2010, Jansen 1999 and the NHMRC tables, new rows that could not be fetched.
* The register said "read" with no file for 22 cited works: 19 have a file on disk (fetched, or found in the archive and linked), and 3 (L068, L080, L086) were changed to "reported".

## 2. Cited sets and drops (task 1)

Method: the register ids in the four claims csvs of each paper, plus the tool's own scan of the section files and supplement with the "Drafter notes" section of each section file removed (the notes name works the text no longer cites). Run on copies in the scratch area; the real `references.md` files were not rebuilt.

| | Paper A | Paper B |
|---|---|---|
| Cited before the new rows | 56 | 120 |
| New rows cited in the text or its Table S8 and S3 rows | +2 (L247, L248) | +7 (L247 to L253) |
| **Cited after** | **58** | **127** |
| B117 and B118 drop lists checked | 31 of 31 not cited | 10 of 10 not cited |
| References rows cited by neither paper | 38 | |

The 38 marked "uncited (B119)": L011, L072, L099, L106, L107, L108, L135, L138, L147, L149, L152, L156, L157, L158, L159, L160, L161, L162, L164, L166, L167, L168, L169, L177, L178, L181, L184, L185, L186, L188, L189, L191, L198, L199, L221, L222, L225, L237. They are 25 of the 31 that B117 dropped for Paper A, 9 of the 10 that B118 dropped for Paper B (L099 and L160 are on both lists, so 32 together), and six that neither report named: L011, L072, L164, L169, L178, L188.

Check of the drop lists against B117 and B118: all 31 ids of B117 (L099, L103, L135, L138, L147, L149, L152, L156 to L163, L166 to L168, L177, L181, L182, L184 to L186, L189 to L192, L222, L225, L227) are absent from the Paper A cited set. Six of them (L103, L163, L182, L190, L192, L227) are still cited by Paper B, so their references rows stay as cited rows. The other 25 are cited by neither paper. The ten of B118 (L099, L106, L107, L108, L115, L160, L198, L199, L221, L237) are absent from the Paper B cited set; **L115 (Poore and Nemecek 2018) is cited by Paper A** (section 6, p. 990), so its row is not marked uncited and B118's drop holds for Paper B only.

Entries the scan cannot match and that stay cited by claims id: A: L010, L060, L062, L228, L242; B: L006, L035, L051, L062, L116 (Roos), L182, L230, L231, L240, L242.

Scan false positives, not works: "Agriculture 2024", "Commodities 2020", "Statistics 2025" (A S6 table text: ABS series titles), "FAO 1990", "FAO 2021", "FAOSTAT 2021", "Mha 1990", "Mha 2021" (year ranges and units in B S3 tables). "Foran and Poldy's 1997" is a data year (1997-98), not a citation.

## 3. "Not seen" reconciled (task 2)

Pages are PDF pages of the file on disk unless "printed" is said. Where the file is an author manuscript, the page numbers are the manuscript's, not the journal's. Files are in `/home/user/carrying-capacity-models/Literature review/` (government and agency documents in `grey/`).

| Id | Work | Outcome | File and pages read |
|---|---|---|---|
| L012 | Lane, Dawes and Grace 2014, Ecological Modelling 272: 220-231 | read; label comes off | QUT ePrints 65503 (author manuscript, 36 pp.); p. 25 prints 40,450,144 and the 48.9% food share; the cover sheet confirms the journal details |
| L013 | Lane, Dawes and Grace 2015, Population and Environment 36(3): 356-371 | read; label comes off | QUT ePrints 75171 (author manuscript, 28 pp.); abstract p. 2; p. 14: over 40 million (national), 28 million (states), 23 million (regions) |
| L014 | Lane 2017, Population and Environment 38(3): 309-324 | read; label comes off | QUT ePrints 99790 (author manuscript, 26 pp.); pp. 1 to 3 (short and long term side by side); p. 26 prints 9,431,487; pp. 11 and 14 give 13 regions |
| L073 | Khorsandi et al. 2022, Sci. Total Environ. 817: 153038 | read; label comes off | Wageningen repository copy, published layout, 12 pp.; abstract p. 1: national 35.5 and local 20 million |
| L074 | Khorsandi et al. 2023, Heliyon 9: e15079 | read; label comes off | Wageningen repository copy, 12 pp.; abstract p. 1 (meta-model, simplified equations, levels L0 to L3) |
| L084 | Erb et al. 2016, Nature Communications 7: 11382 | read; label comes off | open access, 14 pp.; abstract p. 1 (option space) |
| L096 | Ridoutt et al. 2020, Nutrients 12(5): 1212 | read; label comes off | Europe PMC full-text XML and a text rendering; abstract (9341 diets; 7.1 against 6.1 m2 yr-e) |
| L097 | Hendrie et al. 2014, Nutrients 6(1): 289-303 | read; label comes off | Europe PMC full-text XML and a text rendering; abstract (14.5 kg CO2e a day; recommended diets about 25% lower) |
| L116 | Roos et al. 2017, Global Environmental Change 47: 1-12 | read; label comes off | University of Aberdeen copy, 12 pp.; abstract p. 1; "leftover" on pp. 1 to 4, 9, 10 |
| L124 | Shepon et al. 2016, Environ. Res. Lett. 11: 105002 | read; label comes off | open access, 9 pp.; abstract p. 2 (about 120 and 140 million additional people from reallocation), p. 7 |
| L131 | Wiedmann and Lenzen 2018, Nature Geoscience 11: 314-321 | read (opening only; context); label comes off | UNSW accepted manuscript, 28 pp.; pp. 2 to 3 |
| L236 | Helton and Davis 2003, RESS 81(1): 23-69 | read in the report version; label comes off for the use made | Sandia report SAND2001-0417 (135 pp.); PDF p. 19, printed p. 13: the interval-and-pairing construction. Journal page numbers not checked |
| L062 | USDA Handbook 697 | identified and fetched; read; label comes off | USDA ERS, Agricultural Handbook No. 697, June 1992 (AgEcon Search, 75 pp.); Table 7, printed p. 17 (PDF p. 21): beef retail 0.705 and boneless 0.667 for 1988 to 1991 |
| L063 | AUS-MEAT guide 2005 | file was on disk but unlinked in the register; read; label comes off | "Ausmeat - beef yields.pdf" (1 page): 68.7% meat yield; "Copyright AUS-MEAT Limited - 2005"; no place printed |
| L117 | van Zanten et al. 2016 | full file on disk under another name (the register named a missing FIRST_PAGE_ONLY file); read; label comes off | 13 pp.; abstract p. 1 (land use ratio); grassland pp. 1 to 3, 6, 8 to 12 |
| L115 | Poore and Nemecek 2018 | on disk; the 65% is on PDF p. 4 of 7 (printed p. 990); label comes off | the claims csv says "PDF sheet 4 of 6", a count of the wrong length |
| L120 | Tilman and Clark 2014 | on disk; read (abstract, opening); label comes off | 15 pp.; p. 1 |
| L080 | Kastner et al. 2012 | NOT fetched; register changed from "read" to "reported" | refused |
| L086 | Goldfinger et al. 2014 | NOT fetched (closed); register changed from "read" to "reported" |  |
| L235 | McKay et al. 1979 | NOT fetched (closed); stays "record only" |  |

Also found: L073 and L074 were described as "not stored in the repository"; both are filed. L003 (Henry and Godden), L020 (thesis) and L060 (Geoscience Australia and ABARE chapter 12) were on disk and read; the "not seen" labels that list them can lose them. L002 (Gifford et al. 1975) stays "reported": it is second-hand by decision 39.

The register said "read" with no file on disk for six more cited works, none labelled "not seen" in the csvs. Three were filed from open copies (L083 Gerten et al. 2020, PIK Potsdam copy; L105 Fader et al. 2013; L087 Blomqvist et al. 2013) and one (L067 AUSNUT 2007) was in the archive as `prelim models/ausnut07full.xls`, only its path was missing. L069 Muth et al. 2011 was identified (the thesis footnote 843 and reference list print the same work) and fetched. L068 Buzby 2010 was changed to "reported": the archive folder `Buzby - losses` holds ERS spreadsheets, none dated 2010, and the thesis footnotes 835 and 836 name two different Buzby and Wells web items, so the work cited is unidentified. The prose of B (section 6.10 and S2) says "as reported in" for Gerten, Fader, Blomqvist, Muth, Buzby and AUSNUT: with files on disk, Gerten, Fader, Blomqvist, Muth and USDA Handbook 697 can be cited directly if the authors prefer.

One more row says "read" with no file and is cited by neither paper: L082 (Springmann et al. 2018). Left as is.

## 4. New rows (task 3)

| Id | Work | Status | File |
|---|---|---|---|
| L247 | Saltelli, Annoni, Azzini, Campolongo, Ratto, Tarantola 2010, Comput. Phys. Commun. 181(2): 259-270 | not seen; closed; record only (authors, volume and pages from Crossref) | none; Murray fetches |
| L248 | Jansen 1999, Comput. Phys. Commun. 117(1-2): 35-43 | not seen; closed; record only | none; Murray fetches |
| L249 | Gustavsson, Cederberg, Sonesson, van Otterdijk, Meybeck 2011, FAO, Global food losses and food waste | read; Annex 4 printed p. 28 (PDF p. 34): all seven eaten shares of S3 recomputed and agree (0.715, 0.651, 0.950, 0.634, 0.854, 0.610, 0.846) | `grey/FAO2011_Gustavsson_Global_food_losses_and_food_waste_extent_causes_and_prevention.pdf` |
| L250 | FIAL 2021, National Food Waste Strategy Feasibility Study, final report (51 pp.) | read; Table 5 (PDF p. 22) agrees with the project csv for red meat; Table 3 (PDF p. 17) located, not rechecked | `grey/FIAL2021_National_Food_Waste_Strategy_Feasibility_Study_Final_Report.pdf` |
| L251 | Rawtec 2022, City of Burnside Household Bin-by-Bin Audit Results (the work the prose calls "Burnside bin audit 2022") | read; Table 5 (PDF p. 29): meat, dairy, fruit and vegetable rows agree with the project csv; 175 households | `grey/Rawtec2022_City_of_Burnside_Household_Bin_by_Bin_Audit_Results.pdf` |
| L252 | NHMRC and NZ Ministry of Health, Nutrient Reference Values (2006; version 1.2, 2017) | not seen; fetch refused; record only | none; Murray fetches |
| L253 | ABS 2011, Livestock Products, Australia, December 2010 (Cat. 7215.0, released 21 February 2011) | read; explanatory note 12 (PDF p. 15): "Red meat is shown in carcass weight and excludes offal"; PDF p. 16: factor 1.5 for beef and veal | `grey/ABS2011_7215.0_Livestock_Products_Australia_Dec_2010_archived_issue.pdf` |
| L254 | Kniss, Savage and Jabbour 2016, PLoS ONE 11(8): e0161673 (referee-named, not cited) | fetched, not read | Europe PMC XML and text rendering |
| L255 | Porkka et al. 2013, PLoS ONE 8(12): e82714 (referee-named, not cited) | fetched, not read | Europe PMC XML and text rendering |
| L256 | Alexander et al. 2017, Agricultural Systems 153: 190-200 (referee-named, not cited) | fetched, not read | Europe PMC XML and text rendering |
| L257 | Das Gupta 1993, Standardization and Decomposition of Rates (Census Bureau P23-186, 145 pp.) (referee-named lineage, not cited) | fetched, not read | `grey/CensusBureau1993_P23-186_Das_Gupta_Standardization_and_Decomposition_of_Rates_Users_Manual.pdf` |

**L064 (ABS 7215.0).** It carries the same quotation as L253 but no edition year, so it cannot be shown to be the same edition; L064 is left as it was, with a note, and L253 added. The supplement's Table S3a row 4 cites "ABS 7215.0 against the archive" without an issue, so which issue the meat calibration reads is open (decision row below).

**Two corrections the new rows expose.** (a) The prose says "Burnside bin audit"; the author is Rawtec (Burnside is the council). In author-date form it should read "Rawtec 2022". (b) L237 (Saltelli et al. 2008, the Primer) is not the work cited; Saltelli (2010) is.

## 5. Referee literature (task 4)

Paper section means the section where B117 or B118 cites the work today.

| Work (R03) | Status | Cited in the revised paper | Where it would go |
|---|---|---|---|
| A: Cohen 1995 (L049); Price 1999 (L048); Seidl and Tisdell 1999 (L045) | on disk, read | B only (B section 1, and S1 for Price); not A | A section 1: the short paragraph on the carrying-capacity debate (R03a 4) |
| A: Bryan et al. 2016 (L076) | on disk, read | B section 4 and S2; not A | A section 1 (land-use outlook) |
| A: Grundy et al. 2016 (L135) | on disk, read | neither (cut) | A section 1 (land-use outlook) |
| A: Australian National Outlook 2015 (L090) and 2019 (L100) | not on disk: L090 not reached, L100 record only; CSIRO download for 2019 was reset by the server; Hatfield-Dodds et al. 2015 (the Nature paper) is on disk | B S2 cites Hatfield-Dodds 2015 (the Outlook)  | A section 1; list for Murray |
| A: Ponisio 2015; Kniss 2016; Seufert 2012 | Kniss fetched (L254, open); Ponisio free at PMC but bot-check; Seufert not found open; none in the register before B119 except Kniss | neither | A section 7, at the organic setting (0.808; 0.80; about 0.75 in analysis/organic_2025/README.md) |
| A: CSIRO and University of Queensland 2025 (L010) | on disk, read | A 1.1; row and references row present | done |
| A: Wilson and Rees 2005 | not found open; listed for Murray | neither | A section 1 or 7 (small-area population inputs) |
| A: Kitagawa 1955; Das Gupta 1993 | Das Gupta fetched (L257); Kitagawa not found open, listed | neither | A section 4 or its supplement (decomposition lineage), where the README of B111 names them |
| A: AussieGRASS | no work identified; a Queensland Government model, not a paper | neither | ask R03a which output or paper is meant before any search |
| B: Arrow et al. 1995 | not found open; listed (DOI confirmed by Crossref) | neither (R03b is right that it is not mentioned) | B 8.2, the trade paragraph |
| B: van den Bergh and Verbruggen 1999; Fiala 2008; Kitzes et al. 2009 (two); Borucke et al. 2013 | not found open; listed (Borucke is L125, record only) | neither | B sections 2 and 4.5 |
| B: van den Bergh and Rietveld 2004 (L245); Wackernagel et al. 1999 (L244); Cohen 1995; Chisholm 2000 (L143) | on disk, read | B sections 1, 2 and 4.5 (yes); B 8.2 trade paragraph can add them | cited |
| B: Ayres 2000 | not identified: Crossref gives Ayres 1996, Limits to the growth paradigm, Ecological Economics 19(2): 117-134 (10.1016/0921-8009(96)00064-x) and no 2000 item that fits; ask R03b which work | neither | B section 2 |
| B: Haberl et al. 2007; Krausmann et al. 2013 (HANPP family) | free at PMC but PMC served a bot-check; not bypassed; listed | neither | B section 4: HANPP added to the catalogue as a family, not tested (R03b 4) |
| B: Pradhan et al. 2014; Porkka et al. 2013 | Porkka fetched (L255, open); Pradhan not found open, listed | neither | B 6.7 |
| B: Monfreda et al. 2008; Kummu et al. 2012 | not found open; listed | neither | B 6.2 or 6.3 |
| B: Alexander et al. 2017 | fetched (L256, open) | neither | B 6.3 |
| B: Gerten et al. 2020 (L083) | on disk (PIK Potsdam copy); read abstract and p. 3 | B S2, as reported in Beltran-Pena 2020; can be direct | B S2 sentence 37; the 10.2 billion is on PDF pp. 3, 7, 10 |
| B: Springmann et al. 2018 (L082) | closed; register says read with no file; listed | neither | B 6.5 |
| B: Kummu et al. 2020 (L175); Gaupp et al. 2019 (L217) | on disk, read at targeted and page level | Kummu 2020: A section 10; Gaupp: neither | B 8.1 (Gaupp) |
| B: Mottet et al. 2017 (L122) | record only; open access but the publisher page refuses scripts; listed | neither | B 6.2 and the pairing discussion |

## 6. Works for Murray (task 2 and 4)

Works the papers cite and that could not be read. Each line: title, full URL, QUT search.

1. **L080**, Kastner et al. 2012, PNAS 109(18): 6868-6872. URL: https://doi.org/10.1073/pnas.1117054109 (free copy: https://pmc.ncbi.nlm.nih.gov/articles/PMC3345016/). QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Global%20changes%20in%20diets%20and%20the%20consequences%20for%20land%20requirements%20for%20food&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. PNAS page refused (403); PMC served a bot-check page; neither bypassed. Cited in A 4.6 and B S2.20.
2. **L086**, Goldfinger et al. 2014, Ecological Indicators 46: 622-632. URL: https://doi.org/10.1016/j.ecolind.2014.04.025. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Footprint%20facts%20and%20fallacies%3A%20A%20response%20to%20Giampietro%20and%20Saltelli%20%282014%29%20%22Footprints%20to%20nowhere%22&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. Closed. Cited in B S2.16.
3. **L235**, McKay, Beckman and Conover 1979, Technometrics 21(2): 239-245. URL: https://doi.org/10.1080/00401706.1979.10489755. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,A%20Comparison%20of%20Three%20Methods%20for%20Selecting%20Values%20of%20Input%20Variables%20in%20the%20Analysis%20of%20Output%20from%20a%20Computer%20Code&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. Closed. Cited in B S5 for the sampling method; no figure.
4. **L247**, Saltelli et al. 2010, Computer Physics Communications 181(2): 259-270. URL: https://doi.org/10.1016/j.cpc.2009.09.018. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Variance%20based%20sensitivity%20analysis%20of%20model%20output.%20Design%20and%20estimator%20for%20the%20total%20sensitivity%20index&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. Closed; no open copy found. Cited in A and B Table S8 and B S5.
5. **L248**, Jansen 1999, Computer Physics Communications 117(1-2): 35-43. URL: https://doi.org/10.1016/s0010-4655(98)00154-4. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Analysis%20of%20variance%20designs%20for%20model%20output&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. Closed; no open copy found. Cited in A and B Table S8 and B S5.
6. **L252**, NHMRC and NZ Ministry of Health 2006 (version 1.2, 2017), Nutrient Reference Values. URL: https://www.nrv.gov.au/ and https://www.nhmrc.gov.au/sites/default/files/images/Nutrient-reference-aus-nz-executive-summary.pdf. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Nutrient%20Reference%20Values%20for%20Australia%20and%20New%20Zealand%20including%20Recommended%20Dietary%20Intakes&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. Open work; the fetch gave an empty reply and a 503, nothing bypassed. Needed for Tables 3 and 4 (PAL 1.4 to 1.8; 1.2 to 2.2). Cited in B S5 and A S4.
7. **L236 (optional)**, Helton and Davis 2003, Reliability Engineering and System Safety 81(1): 23-69. URL: https://doi.org/10.1016/s0951-8320(03)00058-9. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Latin%20hypercube%20sampling%20and%20the%20propagation%20of%20uncertainty%20in%20analyses%20of%20complex%20systems&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. Only the open Sandia report version was read (report page numbers). Fetch only if journal page numbers are wanted.

Referee-named works not yet cited (not found open, refused by the server, or unidentified; most were not checked one by one for an open copy, because the lookup service limited requests). Fetching them is needed only if the authors decide to cite them.

1. Wilson and Rees 2005, Population, Space and Place 11: 337-360. URL: https://doi.org/10.1002/psp.389. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Recent%20developments%20in%20population%20projection%20methodology%3A%20a%20review&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03a issue 13; A section 1 or 7 (population inputs)
2. Kitagawa 1955, JASA 50(272): 1168-1194. URL: https://doi.org/10.1080/01621459.1955.10501299. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Components%20of%20a%20difference%20between%20two%20rates&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03a issue 13; A section 4 (decomposition lineage). Das Gupta 1993 is on disk (L257).
3. Seufert, Ramankutty and Foley 2012, Nature 485: 229-232. URL: https://doi.org/10.1038/nature11069. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Comparing%20the%20yields%20of%20organic%20and%20conventional%20agriculture&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03a issue 13; A section 7 (organic penalty, about 0.75 in analysis/organic_2025)
4. Ponisio et al. 2015, Proceedings of the Royal Society B 282: 20141396. URL: https://doi.org/10.1098/rspb.2014.1396 (free copy: https://pmc.ncbi.nlm.nih.gov/articles/PMC4286047/). QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Diversification%20practices%20reduce%20organic%20to%20conventional%20yield%20gap&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03a issue 13; A section 7 (0.808). PMC served a bot-check page; not bypassed.
5. van den Bergh and Verbruggen 1999, Ecological Economics 29(1): 61-72. URL: https://doi.org/10.1016/s0921-8009(99)00032-4. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Spatial%20sustainability%2C%20trade%20and%20indicators%3A%20an%20evaluation%20of%20the%20ecological%20footprint&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03b issue 13; B sections 2 and 4.5
6. Fiala 2008, Ecological Economics 67(4): 519-525. URL: https://doi.org/10.1016/j.ecolecon.2008.07.023. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Measuring%20sustainability%3A%20Why%20the%20ecological%20footprint%20is%20bad%20economics%20and%20bad%20environmental%20science&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03b issue 13; B sections 2 and 4.5
7. Kitzes et al. 2009, Ecological Economics 68(7): 1991-2007. URL: https://doi.org/10.1016/j.ecolecon.2008.06.022. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,A%20research%20agenda%20for%20improving%20national%20Ecological%20Footprint%20accounts&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03b issue 13; B 4.5
8. Kitzes et al. 2009, Ecological Economics 68(4): 929-930. URL: https://doi.org/10.1016/j.ecolecon.2008.11.001. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Interpretation%20and%20application%20of%20the%20Ecological%20Footprint%3A%20A%20reply%20to%20Fiala%20%282008%29&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03b issue 13; B 4.5
9. Arrow et al. 1995, Ecological Economics 15(2): 91-95. URL: https://doi.org/10.1016/0921-8009(95)00059-3. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Economic%20growth%2C%20carrying%20capacity%2C%20and%20the%20environment&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03b issue 13; B 8.2 (trade paragraph)
10. Wackernagel and Rees 1997, Ecological Economics 20(1): 3-24. URL: https://doi.org/10.1016/s0921-8009(96)00077-8. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Perceptual%20and%20structural%20barriers%20to%20investing%20in%20natural%20capital%3A%20Economics%20from%20an%20ecological%20footprint%20perspective&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. B105 list; B 4.5, only if a worked figure is quoted
11. Haberl et al. 2007, PNAS 104(31): 12942-12947. URL: https://doi.org/10.1073/pnas.0704243104 (free copy: https://pmc.ncbi.nlm.nih.gov/articles/PMC1911196/). QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Quantifying%20and%20mapping%20the%20human%20appropriation%20of%20net%20primary%20production%20in%20earth%27s%20terrestrial%20ecosystems&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03b issue 13 (HANPP family); B section 4 catalogue
12. Krausmann et al. 2013, PNAS 110(25): 10324-10329. URL: https://doi.org/10.1073/pnas.1211349110 (free copy: https://pmc.ncbi.nlm.nih.gov/articles/PMC3690849/). QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Global%20human%20appropriation%20of%20net%20primary%20production%20doubled%20in%20the%2020th%20century&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03b issue 13 (HANPP family)
13. Pradhan et al. 2014, Environmental Science & Technology 48(16): 9463-9470. URL: https://doi.org/10.1021/es5005939. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Food%20self-sufficiency%20across%20scales%3A%20how%20local%20can%20we%20go%3F&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03b issue 13; B 6.7
14. Monfreda, Ramankutty and Foley 2008, Global Biogeochemical Cycles 22: GB1022. URL: https://doi.org/10.1029/2007gb002947. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Farming%20the%20planet%3A%202.%20Geographic%20distribution%20of%20crop%20areas%2C%20yields%2C%20physiological%20types%2C%20and%20net%20primary%20production%20in%20the%20year%202000&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03b issue 13; B 6.3 or 6.2
15. Springmann et al. 2018, Nature 562: 519-525. URL: https://doi.org/10.1038/s41586-018-0594-0. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Options%20for%20keeping%20the%20food%20system%20within%20environmental%20limits&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03b issue 13; B 6.5. Register row L082 says "read" with no file and no path.
16. Kummu et al. 2012, Science of the Total Environment 438: 477-489. URL: https://doi.org/10.1016/j.scitotenv.2012.08.092. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Lost%20food%2C%20wasted%20resources%3A%20Global%20food%20supply%20chain%20losses%20and%20their%20impacts%20on%20freshwater%2C%20cropland%2C%20and%20fertiliser%20use&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03b issue 13; B 6.3
17. Borucke et al. 2013, Ecological Indicators 24: 518-533. URL: https://doi.org/10.1016/j.ecolind.2012.08.005. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Accounting%20for%20demand%20and%20supply%20of%20the%20biosphere%27s%20regenerative%20capacity%3A%20The%20National%20Footprint%20Accounts%27%20underlying%20methodology%20and%20framework&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03b issue 13 (L125, record only); B sections 2 and 4.5
18. Mottet et al. 2017, Global Food Security 14: 1-8. URL: https://doi.org/10.1016/j.gfs.2017.01.001. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Livestock%3A%20On%20our%20plates%20or%20eating%20at%20our%20table%3F%20A%20new%20analysis%20of%20the%20feed%2Ffood%20debate&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03b issue 13 (L122, record only); an open-access work, but ScienceDirect refuses scripts and Europe PMC does not hold it
19. CSIRO 2019, Australian National Outlook 2019: Australia 2060. URL: https://www.csiro.au/-/media/Showcases/ANO/ANO2_MainReport_WEB_190614.pdf. QUT: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Australian%20National%20Outlook%202019&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT. R03a issue 13 (L100, record only); the download was cut by the server (connection reset). The 2015 report (L090, not reached) was not looked for.

## 7. Second-hand rows (task 5)

Second-hand rows cited by a paper: L001 (Taylor, through the Jones report footnote 13), L002 (Gifford et al., through Henry and Godden 1995 pp. 98 and 103), L004 and L005 (through the Jones report), L035 (Nix, through Henry and Godden p. 98), L036 (Migration Committee 1986, through Henry and Godden p. 97), L068 (Buzby, through Lane 2014 pp. 201 to 202). L080, L086 and L235 are listed by the tool under "second-hand" because the register says "reported"; they are not seen and have no secondary source to name.

* **references.csv:** each of the first seven carries a new `cited_in` column naming the work they were read in. Under the register as B118 left it, L005, L035 and L036 had a "CHECK: second-hand" note; L001, L002, L004 did not say so in a column. L002 reads "Henry and Godden 1995 (L003), p. 98 and the reference list on p. 103".
* **The tool does not print the "cited in" form.** `make_references.py` prints the list "Rows cited only as reported in another work" and a CHECK for three of them, but `render_csv` ignores the new column, so L002 prints as an ordinary article entry ("Gifford, ... 1975. ... Search 6 (6), 212-223."). Not changed (the brief allows no edit to the tool). The change needed is two lines in `render_csv`: after the entry is joined, `if r.get("cited_in"): out += " (cited in %s)" % r["cited_in"]` (the Elsevier form is "cited in Henry and Godden, 1995"). With `cited_in` filled for these seven it will print for all of them.

## 8. make_references.py (task 6)

Run on scratch copies (scratchpad `t1` to `t4`), the real `references.md` files not rewritten.

| Run | Paper A | Paper B |
|---|---|---|
| Files as they stand (drafter notes read by the scan) | 58 entries, 17 CHECK | 130 entries, 26 CHECK |
| Drafter notes set aside, claims ids added for L251 to L253 (what the journal text will produce) | 58 entries, 17 CHECK | 127 entries, 28 CHECK |

The 130 against 127 is six works only the drafter notes name (L099, L106, L107, L115, L160, L221): they leave the list when the notes are stripped.

CHECK lines left, with what each needs (A unless marked B):

* L241 ABARES 2026: author form (corporate in the prose, four named authors on the page). Needs a decision on which form the prose uses.
* L063 AUS-MEAT 2005: place of publication. Not printed on the one page; needs a catalogue entry or Murray.
* L228 Centre for Population 2026; L010 CSIRO 2025; L230 and L231 DCCEEW 2017 and 2019; L226 and L227 Treasury 2023 and 2021 (B); L020 Lane 2014; L051 ABS 1994 (B): place of publication; L231 also publisher and the Arcadis author line. Each needs the title page imprint of the file on disk, which these builders did not re-read.
* L144 Davies 2024; L170 Hughes 2017; L171 Sysak 2017: book editors, place, and for L170 the page range. Need the book title pages.
* L242 Department of Climate Change: year (no year on the page). Needs "n.d." decided or a date found.
* L060 Geoscience Australia and ABARE 2010: publisher and place. The chapter file has no title page; needs the report's front matter.
* L002 Gifford 1975: DOI "none found"; the work is second-hand. Needs the cited-in form (section 7) and no DOI.
* L247 Saltelli 2010 and L248 Jansen 1999 (A and B): not seen. Murray fetches; the CHECK then closes.
* L250 FIAL 2021: place of publication (A did not need it; B). The cover prints none.
* L251 Rawtec 2022 (B): "author initials". The tool does not know Rawtec as a corporate author (its CORP_WORDS list). One word added to that list closes it; not mine to edit.
* L252 NHMRC 2006 (B): not seen; confirm year, version and table numbers once fetched.
* L253 ABS 2011 (B): confirm that the supplement's meat calibration reads the December 2010 issue.
* L062 USDA 1992: place of publication. Not printed on the pages read.
* B only: L067 AUSNUT 2007 (URL, date accessed, version); L068 Buzby 2010 (unidentified); L143 Chisholm 2000 (volume; the spelling Chisolm on the page); L041 Fairlie 2008 (volume, pages, DOI; the file is a later chapter version); L034 Gutteridge 2005 (publisher, place); L036, L005, L004, L035, L001 (second-hand; see section 7); L134 and L050 Wackernagel 1994 and 1996 (place; edition); L226/L227 as above.

"Prose citations with no register row" still printed: only scan false positives (section 2). "Ids with no register row: none." "Prose citations matching more than one register row": ABARES 2026a and b, Higgins et al. 2018b, Lane 2014 and Lane et al. 2014 (A: L012 against L020), Summerhayes and Baker 2026a and b: these are the a/b letters fixed in the tool's LETTER table, not faults.

## 9. What each paper file needs (nothing was edited)

**Claims csvs (the "not seen" labels).** File and line (line 1 is the header):

* A: `A_s01-04_claims.csv` lines 33, 34, 52, 68, 70, 87 come off; line 144 (L080, Kastner) stays. `A_s05-08_claims.csv` lines 10, 13, 57, 58 come off. `A_s09-12_claims.csv` lines 69, 70, 91 come off; line 82 (L002 and L003) changes from "not seen" to "second-hand, read in L003 p. 98". `supplementary_claims.csv` lines 133, 134, 263 come off.
* B: `B_s01-03_claims.csv` lines 82 and 83; `B_s04-05_claims.csv` line 229; `B_s06-09_claims.csv` line 130; `supplementary_claims.csv` lines 320, 322, 324, 325, 327 come off (L124, L131, L116, L096, L236); lines 321 (L086), 323 (L080) and 326 (L235) stay. The "(decision 111: the label is kept here, not in the prose)" text goes with each label that comes off.
* Page column: add the pages in section 3 for the rows that have files (for L062 "printed p. 17"; for L063 "p. 1"; for L013 "p. 14 (manuscript)").
* `register_id` to add (B): `supplementary_claims.csv` rows for the FIAL, Burnside, NHMRC and ABS 7215.0 sources (lines 193, 311, 312 and 315; there is no row for the meat calibration of Table S3a row 4, which needs one with L253) need L250, L251, L252, L253; the Gustavsson row at line 172 needs L249; Table S8 caption and S5 row "Saltelli, Jansen" need L247 and L248 in both papers (A `supplementary_claims.csv` line 164).

**Prose.** Three small changes follow from the files: (1) "Burnside bin audit" should read "Rawtec 2022" (B S3 lines 175, 176 and 304); (2) "USDA Handbook 697, as reported in the archive's errata" (B 6.10) can drop "as reported in the archive's errata" and cite the handbook directly (Table 7, p. 17), or be left; (3) the "as reported in" for Gerten, Fader and Blomqvist (B S2) can be direct. None is required.

**Register note for `qa/claims_register.csv`.** Not edited. Rows citing L062, L063, L069, L249 to L253 can take the new pages. B112 and B113 are unaffected.

## 10. Register rows touched

Literature register (40 rows touched, 11 added): L012, L013, L014, L020, L060, L062, L063, L064, L067, L068, L069, L073, L074, L080, L083, L084, L086, L087, L096, L097, L105, L115, L116, L117, L120, L124, L131, L235, L236, L247, L248, L249, L250, L251, L252, L253, L254, L255, L256, L257.

References csv (55 rows touched; `status` and `cited_in` columns added to every row): L001, L002, L004, L005, L011, L035, L036, L062, L063, L068, L069, L072, L099, L106, L107, L108, L135, L138, L147, L149, L152, L156, L157, L158, L159, L160, L161, L162, L164, L166, L167, L168, L169, L177, L178, L181, L184, L185, L186, L188, L189, L191, L198, L199, L221, L222, L225, L237, L247, L248, L249, L250, L251, L252, L253. Content changed in the original columns only for L062, L063 and L069; every other change is the new columns, notes and the added rows L247 to L253.

Archive files added (12 PDFs, 5 pairs of PMC text files (xml and md), listed by name in the register rows): Lane, Dawes and Grace 2014 and 2015; Lane 2017; Khorsandi 2022 and 2023; Erb 2016; Shepon 2016; Wiedmann and Lenzen 2018; Roos 2017; Gerten 2020; Fader 2013; Blomqvist 2013 (all `Literature review/`); Ridoutt 2020, Hendrie 2014, Kniss 2016, Porkka 2013, Alexander 2017 (XML and md); and 8 files in `Literature review/grey/`: USDA Handbook 697, FAO 2011 Gustavsson, FIAL 2021, Rawtec 2022, ABS 7215.0 December 2010, Sandia 2002 (Helton and Davis), USDA ERS 2011 (Muth et al.), Census Bureau 1993 (Das Gupta).

## 11. Decisions for the coordinator

| # | Row | Choice made | Recommendation |
|---|---|---|---|
| 1 | **Which ABS 7215.0 issue** the meat calibration reads (S3a row 4). L253 is the December 2010 issue; the supplement gives no issue. | L064 untouched; L253 added | Name the issue in the supplement and the references row follows. |
| 2 | **Author manuscripts for Lane 2014, 2015 and 2017.** The pages the papers cite are the journal's (for example "Lane 2014, p. 280" is the thesis; the three journal papers are cited without pages). | Registered with manuscript pages | If a journal page is ever cited, fetch the version of record (links in the register). |
| 3 | **The tool's "cited in" form** (section 7). | Column added, tool unchanged | Approve the two-line change to `render_csv` and the CORP_WORDS word "Rawtec". |
| 4 | **L080 and L086 changed to "reported".** | As the brief orders | They return to "read" when Murray fetches. |
| 5 | **L115 is cited by Paper A**, not only B. | References row kept as cited | None. |

## 12. Wrong-value check

Wrong-value check: example, deliberately wrong and not kept. I set the year of the Gustavsson et al. row (L249) to 2012 in both the register title and `references.csv` on a scratch copy and reran `make_references.py B`: the tool added the line "Gustavsson et al. 2011 [supplementary.md]" to "Prose citations with no register row", so the mismatch with the prose year 2011 was caught; with the true year 2011 the line is absent. A second check, from the reading itself: the claims csv for L115 says "PDF sheet 4 of 6"; the file has 7 pages (the 65% is on PDF page 4 of 7, printed p. 990), so the page note would have failed a check by page count.

