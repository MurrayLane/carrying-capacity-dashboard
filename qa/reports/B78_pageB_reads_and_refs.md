# B78: page-level reads for nine Paper B rows; L050; three Monte Carlo references

Files written: `qa/literature_register.csv` (rows L050, L202, L207, L211, L212, L213, L214, L217, L219, L220 changed; L235, L236, L237 added) and this report. Source folder for every file: `/home/user/carrying-capacity-models/Literature review/`. Network used only for api.crossref.org.

## Part 1: nine rows

**L202 Sukhera 2022.** File is the paper (4 pages, printed pp. 414 to 417). No numerical figure in the row. Confirmed: narrative reviews as a distinct research tradition and the types state-of-the-art, critical and integrative (p. 414); five elements of rigor (pp. 414 to 415); the three types with strengths and weaknesses (p. 416). Corrections: none; pages added.

**L207 van Dooren 2018.** File is the paper (15 pages, Frontiers article 48; Frontiers prints no journal pages, so pages are the article's own 1 to 15). Confirmed: 52 papers (p. 1 abstract; pp. 3 and 5); 12 studies with ecological constraints compared in detail (p. 1 abstract; Table 1, p. 4; p. 7). Corrections: none. Note: the paper's author name is "van Dooren"; the register title has "Van Dooren".

**L211 Jones 2023.** File is the paper (printed pp. 323 to 333). Confirmed: 12 countries, Australia in the list (p. 323 abstract; 12 repeated on pp. 325 and 326; Australia cases pp. 328 and 329). Corrections: none to the figure. Note recorded: the paper also says the network spans 20 countries (p. 324), a different count.

**L212 Mesgaran 2017.** File is the paper as PubMed Central text with no page numbers, so locations are by section (abstract, Introduction, Conclusion). No numerical figure in the row. Confirmed: land suitability from soil, terrain and climate; low precipitation as the overarching limit; water limits on food self-sufficiency. Corrections: none. Page numbers cannot be given from this copy.

**L213 Rosa 2018.** File is the paper (article pp. 1 to 11, footer-numbered; PDF page 2 is article p. 1). Confirmed with pages: 48% (408 km3 a year), 26% of rainfed cultivated lands, 37% more calories, 2.8 billion people, all on p. 1 (abstract); 408 km3 and 37% repeated on p. 5; 26% on p. 7. CORRECTION: the row said irrigation "could expand by 48%". The paper's 48% is the rise in global water consumption for irrigation; the area expansion is 26% of rainfed cultivated lands. what_taken rewritten.

**L214 Kummu 2016.** File is the paper as PubMed Central text, no page numbers, locations by section. Confirmed: per capita water consumption in Australia-Pacific "over 6-fold greater in the 2000s compared to the 1900s" (Results, Water consumption). Added: total consumption there rose 30-fold, so the two are not confused. Corrections: none.

**L217 Gaupp 2019.** File is the author-manuscript copy (11 pages, footer-numbered), not the journal pages 54 to 57; pages cited are manuscript pages. No numerical figure in the row. Confirmed: rising risk of simultaneous failure (p. 1); wheat precipitation risks increased in India and Australia and decreased elsewhere (p. 3). Corrections: none.

**L219 Bodirsky 2020.** File is the paper (printed pp. 1 to 14, article 10:19778). Confirmed: 30 to 45 Exajoules by 2050 (p. 1 abstract; p. 3 results, 45 with range 43 to 47); shift to animal-source foods and empty calories (p. 1). Added p. 4: animal-source share of calories 18% to 24%. Corrections: none.

**L220 Whitton 2021.** File is the paper as PubMed Central text, no page numbers, locations by section. Confirmed: 35 countries, 2000 to 2019; some countries near or at peak; poultry up in most, beef and mutton or lamb down in many (abstract); 15% decline in Australian beef production in the 2019 drought (Discussion 4.3). Corrections: wording tightened to "most" and "many". Flag: the paper's source for the 15% (reference 47) is titled as a 15 per cent fall in beef exports to 1.039 million tonnes, so the paper's own sourcing is loose; the figure is confirmed only as printed in the paper.

All nine rows: read_or_reported "read (B78 page level)", status "self-checked (B78)", note appended.

## Part 2: L050 Wackernagel and Rees

local_path set to `carrying-capacity-models/Literature review/Wackernagel_Rees_1996_pages/`; read_or_reported changed from "not reached" to "read (B44 from the filed scan)". B44 (`qa/reports/B44_wackernagel_scan.md`) names p. 78 only in its index ("Global average; local productivity adjustment"), so I opened the p. 78 page image. what_taken says p. 78 carries the world-average versus local productivity adjustment (land twice as productive as the world average counts as two hectares of average land) and prints no equivalence factor; the only food-land productivity statement is p. 85 (B44). The 2.8 factor is not found on p. 78 and B44 reports none on the scan; the claim rests on MT alone, so status is left "unverified".

## Part 3: three references (Crossref, 2026-11-11)

- L235 McKay, Beckman and Conover 1979, Technometrics 21(2): 239-245, doi:10.1080/00401706.1979.10489755. Crossref title has no leading "A". JSTOR record of the same paper: 10.2307/1268522 (noted in the row).
- L236 Helton and Davis 2003, Reliability Engineering and System Safety 81(1): 23-69, doi:10.1016/s0951-8320(03)00058-9. Journal article confirmed; a report version is 10.2172/806696 (noted).
- L237 Saltelli et al. 2008, Global Sensitivity Analysis: The Primer, Wiley, doi:10.1002/9780470725184 (ISBNs 9780470059975, 9780470725184). Flag: Crossref dates the print record 18 December 2007 (online 21 January 2008); 2008 kept as the imprint year from the brief.

All three: kind per brief, status and read_or_reported "record only", used_by "methods paper (section 6, Monte Carlo method)".

## Checks

- 237 data rows (234 plus 3): pass. 12 columns on every row: pass. Parses with Python csv: pass. Em dashes: none. Line endings: unchanged (CRLF throughout, 238 CRLF for 238 lines, final CRLF kept; unedited file round-tripped byte for byte before editing). Only the ten named rows differ from the prior file, plus the three added.
- Time words checked in the text I added: none.

## Wrong-value check

Example of a wrong citation (marked as an example, not in the register): citing the Rosa 48% as "p. 5". Page 5 prints 408 km3 and 37% in the results discussion, but 48% is printed only on p. 1 (abstract), so "48% (p. 5)" would be wrong.
