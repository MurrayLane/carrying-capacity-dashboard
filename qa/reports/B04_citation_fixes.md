# B04: citation fixes and identifiers

Date of work and of every "accessed" entry: 2026-11-07. Changed files: `qa/literature_register.csv` (columns `title`, `origin`, `dated_or_accessed`, `notes` only; 72 rows kept, `status` and `read_or_reported` untouched) and this report. Local files were read from `carrying-capacity-models/`; text was extracted with `pdftotext` or LibreOffice into the session scratchpad, and scanned PDFs were opened as page images. No PDF was put into either repository.

Web sources worked through Crossref (api.crossref.org), search-result summaries and page fetches. Where a page could not be opened (QUT ePrints 403, NLA access-denied page, AgEcon Search 403, State Library NSW 500, Adelaide host not reachable) the row says so.

## Part 1

### 1. Gutteridge: 2005 or 2006; the "14 times" ratio
* Evidence: `Literature review/Gutteridge 2005.doc` (converted to text). Title block: "Ecological foot print and carrying capacity studies of South East Queensland: A comparison and discussion of results", Michael Gutteridge, 12 August 2005; "commissioned by the Dept. of Natural Resources and Mines". Its Paper 1 is dated June 2005. The 180,000 figure is in it (text lines on "a population of around 180,000 people").
* `Gutteridge2006_slides.ppt` (converted to PDF): title "South East Queensland's Ecological Footprint & Carrying Capacity / How big is the pond?"; slides repeat 180,000; the file shows no date; one slide says "SEQ 2.6m (2005) and 3.7m (2026)".
* Thesis (`Papers and manuscripts/Lane-2014-PhD-thesis-QUT-eprint-67485.pdf`): cites the report as "(Brisbane: Department of Natural Resources and Mines, Queensland Government, 2005)" and the slides as "How Big is the Pond? ... (Brisbane: 2006), slide 8".
* Finding: the study is 2005. 2006 belongs to the slides only. The comparators README line 24 pairs "Gutteridge's 2006 Southeast Queensland study" with the 180,000 and "14 times", which is the report's result, so it should read 2005 (or name the slides).
* "14 times": not in the report and not in the slides (both searched for "14", "times", "fourteen"). The only hit is the thesis, text-extract line 5542, PDF page 125: "the existing population of Southeast Queensland is 14 times over its resource-based carrying capacity", written by the thesis author. The slides' 2.6 million over 180,000 is 14.4; the report's population (2,331,740 from the NRM SEQ Draft Plan 2004) over 180,000 is 13.0. So the ratio is the thesis's derived figure, not Gutteridge's statement.

### 2. Henry and Godden: 1994 or 1995
* Evidence: page images of the PDF. Running head on p.98: "Review of Marketing and Agricultural Economics, Vol. 63, No. 1, April 1995". First page (p.97) authors L.A. Henry and D.P. Godden, Department of Agricultural Economics, University of Sydney. Reference list p.103 gives Gifford et al. 1975 as Search 6(6), 212-223.
* IDEAS record https://ideas.repec.org/a/ags/remaae/12469.html: 1995, April, vol. 63(01), DOI 10.22004/ag.econ.12469.
* The paper itself says (p.97) the Inquiry was called "in February 1994". A different, earlier item exists: Henry and Godden 1994, "Robustness of Estimates of Australia's Sustainable Population", AARES 38th conference, Wellington, February 1994 (AgEcon Search record 148240, seen in a search result; the page returned 403). The Jones inquiry (December 1994) most likely cites that conference paper. I could not check the inquiry text: the 176-page PDF is a scan and no OCR is installed.
* Finding: the journal note is 1995. "1994" in the Jones row may be a correct citation of a different (conference) paper; it is not a wrong year for the journal note. The coordinator should decide whether to add a clause.

### 3. Lane and Dawes 2013: journal
* Crossref record https://doi.org/10.1007/978-94-007-7756-9_3: book chapter, "Carrying Capacity Dashboard Analyses: Australian Case Studies of Populations Scaled to Place", Lane and Dawes, in *Urban Environment*, Springer Netherlands, 2013, pp. 27-37. The book (DOI 10.1007/978-94-007-7756-9) is "Urban Environment: Proceedings of the 11th Urban Environment Symposium (UES), held in Karlsruhe, Germany, 16-19 September 2012", editors Rauch, Morrison, Norra and Schleicher.
* Finding: "Urban Environment" (PUBLICATIONS.md, PAPERS.md) is right, and "UES" is the symposium. "Urban Ecosystems" (CORRECTION_NOTES.md) is wrong. It is a book chapter, not a journal article. The thesis lists the 19 September 2012 UES talk.

### 4. ABARE Australian Energy Resource Assessment
* File: `carrying-capacity-models/references re production yields/Non-food/Fuel - Abare - Biofuel Australian Energy Resource Assessment 2009.pdf` (26 pages; PDF title "Australian Energy Resorce Assessment - Chapter 12 - Bioenergy"; author field Geoscience Australia; creation date 1 April 2010). Printed pages run 309 to 334.
* Table 12.12 "Estimated energy and fuel yields for different feedstocks" is on printed page 331 (file page 23): Oilseeds, Biodiesel 400 L/t; "Source: O'Connell et al. 2009b". The same page's text reads "400 litres of biodiesel per tonne of oilseeds". The chapter is Chapter 12 Bioenergy.
* The sibling file "Fuel - Abare - Australian Energy Resource Assessment 2009.pdf" is Chapter 3 Oil.
* Date: Geoscience Australia catalogue record (fetched, https://ecat.ga.gov.au/geonetwork/srv/api/records/a05f7892-efe9-7506-e044-00144fdd4fa6): "Australian Energy Resource Assessment", authors Geoscience Australia and ABARE, date 2010, persistent id https://pid.geoscience.gov.au/dataset/ga/70142, PDF https://d28rz98at9flks.cloudfront.net/70142/70142_complete.pdf. A search result gives release in March 2010.
* Finding: one report, not two. The correct year is 2010 ("April 2010" in ERRATA line 36 is nearer, the chapter PDF was made on 1 April 2010). "2009" comes from the file name and the data year. The correct author is Geoscience Australia and ABARE.

### 5. Simpson, Petroeschevsky and Lowe: journal name
* Title page, running heads on pp. 12, 14, 16 and 18, and the citation line all read "Australian Journal of Environmental Management" (ISSN 1322-1698, 7:1, 11-18, DOI 10.1080/14486563.2000.10648479). The title page names the authors as Rod W. Simpson, Anna Petroeschevsky and Ian Lowe.
* Crossref files the same DOI under "Australasian Journal of Environmental Management" (the later name of the journal). So the register's and README's "Australasian" is the current publisher name, and "Australian" is what is printed on the article. The register title now uses the printed name; the coordinator chooses.

### 6. SoFSR (CSIRO and UQ food system report)
* Date: CSIRO news release dated 2 June 2025 (https://www.csiro.au/en/news/all/news/2025/june/first-national-stocktake-of-australias-food-system-reveals-hidden-costs-and-big-opportunities, fetched). PDF created 22 May 2025 (metadata). README "June 2025" is right.
* Title page: Nelson R, Lim-Camacho L, Robinson CJ (eds) (2025) Towards a state of the food system report for Australia. CSIRO; ISBN 978-1-4863-2151-3. Food System Horizons is the CSIRO and University of Queensland initiative (foreword text).
* Page: the sentence is on printed page 30 (footer "Food System Horizons 30"; PDF page 39): "The other 30% feeds a population of 27 million (ABS, 2024), so Australia is estimated to be able to feed another 63 million people, or around 100 million people in total. This metric is misleading as an indicator of food security because it assumes that commodities are food." Page 30 is confirmed. (It is the only page with "63 million".)

### 7. Foran and Poldy: series name
* Title page: "Future Dilemmas / Options to 2050 for Australia's population, technology, resources and environment / Working paper series 02/01 / CSIRO Resource Futures October 2002". Page 2: "CSIRO Resource Futures Working Paper 02/01, Barney Foran, Franzi Poldy, CSIRO Sustainable Ecosystems"; ISBN 0 95808453 X.
* Finding: the series is "CSIRO Resource Futures Working Paper 02/01". "CSIRO Sustainable Ecosystems" is the division. The phrase "CSIRO Sustainable Ecosystems Working Paper 02-01" appeared only in the register's old title text; I found no project document that uses it. The Science Queensland republication page spells the title "Options to 2025" in the fetch summary, against 2050 on the title page (looks like a typo on that page).
* URLs: https://scienceqld.org/wp-content/uploads/2026/04/fulldilemmasreport02-01.pdf and https://scienceqld.org/wp-content/uploads/2026/04/dilemmas_distilled2002.pdf (from the republication page, fetched).

### 8. Lane 2011: venue
* `analysis/model_archive/PAPERS.md` line 10: "Lane (2011) Resilience in Urban Design (IUDC)". PUBLICATIONS.md says "Urban Design" only.
* The 4th International Urban Design Conference, theme "Resilience in Urban Design", was held on the Gold Coast in September 2011 (dates 21-23 or 22-23 September differ between search results). The thesis lists "23 September 2011: 4th International Urban Design Conference, Gold Coast" among Lane's presentations (text-extract line 14019).
* Not established: the paper's own title, whether proceedings were published, any DOI or ePrint. Searches found none.

### 9. Lane 2017 and ePrints 99790
* Same work. Crossref: DOI 10.1007/s11111-016-0264-9, "Exploring short-term and long-term time frames in Australian population carrying capacity assessment", *Population and Environment* 38(3): 309-324, print date March 2017, online 2016-10-05. OpenAlex location list for that DOI includes http://eprints.qut.edu.au/99790/ and https://eprints.qut.edu.au/99790/1/POEN-D-16-00022_R2.pdf as the submittedVersion. The QUT page itself returned 403, so the record was not opened. No second Lane time-frames paper was found.

## Part 2: identifiers added (details in each row's `notes`)
DOI or stable URL recorded: L003, L006, L007, L008, L009, L010, L012, L013, L014, L015, L016, L017, L022, L023, L024, L025, L026, L040, L043, L044, L045, L046, L047, L048, L049, L053, L054, L055, L060, L069 (candidate). `unknown (searched 2026-11-07)` recorded: L001, L002, L004 (candidate catalogue URL in the cell), L005, L031, L041, L042, L050, L056, L057, L058, L068, L036.
Not searched, still plain `unknown`: L011, L018, L019, L027, L028, L030, L032, L033, L034 (report location), L035, L037, L038, L039, L051, L052, L059, L061 to L067, L070 to L072. Several are vague labels with no work to search for.

## Part 3: "read as cited" rows (read_or_reported unchanged)
* L001 Griffith Taylor: no primary text found; the 65 million figure appears in no web source I found (ADB says about 19 or 20 million).
* L002 Gifford et al. 1975, Search 6(6): 212: not found online. Citation as printed in Henry and Godden p.103 is in the row.
* L004 Borrie 1975: candidate NLA digitised copy https://nla.gov.au/nla.obj-1928629357/view (first report, Population and Australia). The page returned an access-denied page, so it is unconfirmed.
* L005 National Population Council 1991: catalogue record only (State Library NSW, chair Glenn Withers; about 1992). No full text.
* Bonus: L006 (Jones inquiry) is online at https://aphref.aph.gov.au/house/committee/reports/1994/1994_pp457.pdf; title page opened and matches.

## Corrections for the coordinator to apply (file, line, change)
* `CORRECTION_NOTES.md` line 60: heading "Lane and Dawes 2013 (Urban Ecosystems)" to "(Urban Environment)"; it is a book chapter in Springer's *Urban Environment* proceedings (UES, Karlsruhe 2012).
* `CORRECTION_NOTES.md` line 11 and `ERRATA.md` line 27: "ABARE (2009)" to "Geoscience Australia and ABARE (2010), Australian Energy Resource Assessment, chapter 12". `ERRATA.md` line 36: "April 2010" is closer; give 2010 and the table page (p.331).
* `analysis/liquid_fuel_2025/README.md` line 98: "ABARE, Australian Energy Resource Assessment 2009, chapter 12" to Geoscience Australia and ABARE 2010. Line 6: "ABARES Australian Energy Resource Assessment, 2008 data" names ABARES for a 2010 ABARE and Geoscience Australia work; check.
* `analysis/comparators_2025/README.md` line 24: "Gutteridge's 2006 Southeast Queensland study" to 2005 (report) and say that "14 times" is the thesis's wording, not Gutteridge's.
* `analysis/comparators_2025/README.md` line 28: "Australasian Journal of Environmental Management" to "Australian Journal of Environmental Management" (as printed), or give both.
* `analysis/comparators_2025/README.md` line 14: "Henry and Godden 1994" is probably the AARES conference paper (see item 2); either leave and add "(conference paper)" or confirm against the inquiry text.
* `PUBLICATIONS.md` line 13: "Lane 2011 Urban Design" to "Lane 2011, 4th International Urban Design Conference (Resilience in Urban Design), Gold Coast". Line 14: add that the 2013 item is a book chapter in the UES proceedings.
* `PUBLICATIONS.md` line 17 "the time-frames paper (ePrints 99790)": name it as Lane 2017, Population and Environment 38(3), DOI above.

## Surprising or inconsistent
* The thesis says Gutteridge's population is "14 times over", which neither of Gutteridge's own files states (item 1).
* The Jones inquiry cites a Henry and Godden that is probably a 1994 conference paper, so the "1994 versus 1995" question may be two works.
* Crossref and the printed journal name differ for Simpson et al. (item 5).
* Henry and Godden's IDEAS record gives pages 1-7; the file is pp. 97-103.
* The Science Queensland page says "Options to 2025" for a report titled "Options to 2050".
* Lane and Dawes 2013 is a conference-proceedings chapter, but ERRATA, PUBLICATIONS and the register kind field call it a journal article ("journal article (author's own)" in L054, left unchanged).

## Check first
1. L054 (journal answer rests on Crossref only; the ePrints 54114 link is assumed, not opened).
2. L060 and the three files that cite ABARE (2009); the Table 12.12 page and the year feed a Tier A correction (biodiesel).
3. L003 versus the inquiry's "Henry and Godden 1994" (needs the inquiry text, scanned).
4. L034 "14 times" wording; the Lane 2014 thesis states it, so a thesis claim is affected.
5. L005 and L004 (catalogue-only candidates), and L069 (candidate only).
