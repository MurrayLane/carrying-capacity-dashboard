# B103: citation fields for every cited work (decision 98)

Builder B103. Files written: `qa/references.csv` (new), `qa/tools/make_references.py` (edited), `papers/A_results/draft/references.md` and `papers/B_methods/draft/references.md` (regenerated), this report. The literature register, the prose and the claims csvs were not edited. The only network use was api.crossref.org, one request at a time, with a plain client string.

## What was built

`qa/references.csv` has one row for each of 179 register ids: the 169 ids in the two B102 lists, plus ids cited in the claims csvs or named by id in the prose that the B102 lists missed (L188; L011, L072, L157, L164, L169, L178 from the prose), plus L001 (Taylor 1922), L195 (O'Neill 2018) and L047 (Meyer and Ausubel). It has the 19 columns of the brief. Every row says in `source_of_fields` where its fields came from, and `notes` carries the detail.

The generator now reads `qa/references.csv` first and falls back to the register's title field for any id with no csv row (none needed now). A row is flagged [CHECK] when a required field for its type is empty, or when its notes carry a segment starting "CHECK:".

Two small generator changes beyond reading the csv, both in the prose scan: the csv year now counts when matching a prose citation to a row (so the year-less short forms Hardin, Cohen and the rest match their rows), and the curly apostrophe in O'Neill is treated as a plain one. Because of these, Paper A lists one more entry (L157) and Paper B three more (L001, L047, L195) than the B102 run; all four were already named in the prose.

## Counts

| | Paper A | Paper B |
|---|---|---|
| Entries in the list, B102 run | 84 | 124 |
| Entries marked [CHECK], before (B102 run) | 83 | 123 |
| Entries in the list, now | 85 | 127 |
| Entries marked [CHECK], now | 21 | 30 |

Two runs of the generator give identical output for both papers (cmp on the printed report, and the same md5 on each `references.md` after a third run). `qa/references.csv` parses with Python's csv reader: 179 data rows, 19 columns in every row, no repeated or empty id.

### Fields filled, by source

Counted per filled field (the `type`, authors, year, title, container, volume, issue, pages, DOI, publisher, place, editors, edition, URL and accessed columns; not the notes):

| Source | Fields |
|---|---|
| Crossref | 1,225 |
| PDF on disk (title pages and first pages read) | 148 |
| Register (title field, origin, dated column, notes) | 95 |
| Not found | the gaps listed under "still flagged"; nothing was filled for them |
| Journal abbreviations, from the table in the generator (130 filled; blank for 6 serials where I was not sure, 7 entries) | counted apart |

By entry (the `source_of_fields` column): 140 Crossref; 1 Crossref plus PDF on disk (L001 Taylor); 7 PDF on disk; 18 PDF on disk with some fields from the register; 13 register only.

Crossref DOIs: 131 rows had a DOI in the register title or origin, plus the L001/L042/L086/L139/L140/L141 DOIs found by Crossref title search (matched on title, journal, volume and pages), giving 138 Crossref records. Two register DOIs returned 404 from Crossref because they are not Crossref DOIs: L003 (AgEcon Search) and L143 (Informit). Both rows were filled from the PDF on disk and the register instead.

Register problems found on the way (the register was not edited):
- L086 (Goldfinger and others 2014, the reply) carries the DOI of the paper it criticises (L085). The reply's own DOI, 10.1016/j.ecolind.2014.04.025, was found by Crossref search and is in the csv.
- L044 Hardin: the Crossref title has the section label "AIBS News:" in front; the csv uses the title printed on page 1 of the PDF.
- L150: Crossref holds the title in capitals; the register's sentence-case title is used.
- Year differences, csv year (Crossref print year) against the register: L150 2026 (register and prose 2025, online-first), L157 2017 (register 2016; the prose says 2017, so the register row is the one to correct), L209 2023 (register 2022), L210 2021 (register 2020), L237 2007 (register 2008; Crossref print 2007, online 2008), L142 2007 (register 2006).
- Files whose first page gives a different year from the register: L241 (ABARES, June 2026, register and prose 2025), L228 (Centre for Population, copyright 2026, register and prose 2025), L051 (ABS 4306.0, released 21 June 1994 for the reference year 1991-92; prose "ABS 1991"), L005 (National Population Council: the Jones report footnotes say 1992, its text and the register 1991), L041 (Fairlie: the file says The Land 4, 2008; the register says Winter 2007-8 and the prose 2007).
- Corporate authors keep the short form the prose uses (ABS, ABARES, CSIRO, Treasury, PMSEIC); the full name is in the publisher column where the page gives it. L010 and L241 have named authors or editors on the page; they are in the editors column and the notes.

## Entries still flagged, and why

Paper A (21):

- L241 (ABARES 2026): prose year (ABARES 2025) against June 2026 on the file; author form (corporate ABARES in the prose, four named authors on the page)
- L063 (AUS-MEAT 2005): publisher; place of publication; title as printed
- L228 (Centre for Population 2026): place of publication; prose cites Centre for Population 2025; the copyright year on the file is 2026
- L144 (Davies 2024): book editors; place of publication
- L230 (Department of Climate Change 2017): place of publication
- L231 (Department of Climate Change 2019): publisher; place of publication; authors (prepared by Arcadis per the register)
- L242 (Department of Climate Change None): year
- L060 (Geoscience Australia and ABARE 2010): publisher; place of publication
- L002 (Gifford 1975): DOI (none in the register or Crossref; confirm whether one exists)
- L170 (Hughes 2017): book editors; place of publication; page range
- L020 (Lane 2014): place of publication
- L161 (Mirosa 2020): book editors; place of publication
- L099 (Productivity Commission 2011): confirm the title, place and any series from the document
- L150 (Summerhayes 2026): year 2026 here (Crossref print/issue year; Crossref online year 2025) against 2025 in the register
- L171 (Sysak 2017): book editors; place of publication
- L138 (Thompson 2011): author initials; DOI (none in the register or Crossref; confirm whether one exists)
- L167 (Timmer 2024): book editors; place of publication
- L227 (Treasury 2021): place of publication
- L226 (Treasury 2023): place of publication
- L062 (USDA None): year; publisher; place of publication; authors
- L157 (Wiedemann 2017): year 2017 here (Crossref print/issue year; Crossref online year 2016) against 2016 in the register

Paper B (30):

- L051 (ABS 1994): place of publication; prose year (1991) against release year 1994
- L067 (AUSNUT 2007): URL; date accessed; version
- L068 (Buzby 2010): author initials; title; publisher; place of publication
- L143 (Chisholm 2000): volume; author surname spelling (Chisolm on the page, Chisholm in the register)
- L010 (CSIRO 2025): place of publication
- L230 (Department of Climate Change 2017): place of publication
- L231 (Department of Climate Change 2019): publisher; place of publication; authors (prepared by Arcadis per the register)
- L242 (Department of Climate Change None): year
- L041 (Fairlie 2008): volume; pages or article number; DOI (none in the register or Crossref; confirm whether one exists); prose cites Fairlie 2007; the file says 2008 a
- L002 (Gifford 1975): DOI (none in the register or Crossref; confirm whether one exists)
- L142 (Gilland 2007): year 2007 here (Crossref print/issue year) against 2006 in the register
- L034 (Gutteridge 2005): publisher; place of publication
- L210 (Herrington 2021): year 2021 here (Crossref print/issue year; Crossref online year 2020) against 2020 in the register
- L020 (Lane 2014): place of publication
- L036 (Migration Committee 1986): title; publisher; place of publication; second-hand, the committee report is not identified
- L069 (Muth 2011): author initials; title; publisher; place of publication; title (candidate not confirmed)
- L005 (National Population Council 1992): year 1992 in the footnotes against 1991 in the register and the prose; second-hand, the report itself is not on hand
- L004 (National Population Inquiry 1975): identity of the work cited as Borrie 1975 rests on that footnote and the register's B04 note, not on a copy of the report; the
- L209 (Navarro Garcia 2023): year 2023 here (Crossref print/issue year; Crossref online year 2022) against 2022 in the register
- L035 (Nix None): author initials; year; title; publisher; place of publication; second-hand, the work is not identified
- L099 (Productivity Commission 2011): confirm the title, place and any series from the document
- L199 (Qiu 2024): book editors
- L108 (Qiu 2024): book editors; not cited by content in the prose; 'Qiu 2024' in the paper B introduction (regional functional planning) is L199
- L237 (Saltelli 2007): place of publication; year 2007 here (Crossref print/issue year; Crossref online year 2008) against 2008 in the register
- L001 (Taylor 1922): end page and initials rest on the Jones report footnote, not on the article
- L227 (Treasury 2021): place of publication
- L226 (Treasury 2023): place of publication
- L062 (USDA None): year; publisher; place of publication; authors
- L134 (Wackernagel 1994): place of publication
- L050 (Wackernagel 1996): place of publication; edition (or confirm first edition); year 1996 is from the register, not printed on the pages read

Reasons, in groups:
- Place of publication not printed on the pages read: the Commonwealth reports (L226, L227, L228, L230, L231, L010, L051, L034, L020, L134, L050, L060), and chapter or book records where Crossref has no place (L144, L161, L167, L170, L171, L237).
- Book editors not in Crossref: L144, L161, L167, L170, L171, L108, L199. The chapter records name no editors.
- No copy and no identification, so the register's words are all there is: L035 (Nix), L036 (Migration Committee), L062 (USDA Handbook 697), L063 (AUS-MEAT), L067 (AUSNUT), L068 (Buzby), L069 (Muth; B04 names a candidate, not opened, so not filled), L099, L138. L002, L004 and L005 are second-hand, with fields taken from the Henry and Godden reference list or the Jones report footnotes.
- Year disagreements to settle: L001 (Taylor, see below), L005, L041, L051, L142, L150, L157, L209, L210, L228, L237, L241.
- Other: L143 has no volume or issue (a newsletter) and a spelling difference in the author's name (Chisolm on the page); L231 does not name its issuer on the first page; L242 has no date; L108 is in the list only because "Qiu 2024" matched two rows, and the prose citation is L199; L001's initials and end page come from the Jones report footnote (Crossref gives the given name Griffith and the start page only).

## The five unregistered prose citations

B102 listed five prose citations with no register row. Checked against the register and Crossref:

1. **Wiedemann 2017.** A row exists: L157 (register year 2016, Animal Production Science 57(6): 1149-1162). The prose names it by id ("Wiedemann 2017 (L157)"). Crossref gives print year 2017, online 2016. The register would need its year corrected to 2017. It was missed because the row says 2016.
2. **FAO 2021.** Not a work: the prose phrase is "FAO 2021-23" for the data years of the export diversion figures (A_s09-12.md line 138), with no release named. L071 is the FAO/ICAC survey, a different item. If a citation is wanted, the register would need a dataset row: FAO, the Food Balance Sheets domain of FAOSTAT, years 2021-23, release or download date, URL, date accessed.
3. **FAOSTAT 2021.** The same case for Paper B ("FAOSTAT 2021-23", B_s01-03.md and B_s04-05.md): a dataset row for FAOSTAT with domains used, years 2021-23, release or download date, URL and date accessed.
4. **O'Neill et al. 2018.** A row exists: L195 (O'Neill, Fanning, Lamb and Steinberger 2018, Nature Sustainability 1(2): 88-95, DOI 10.1038/s41893-018-0021-4). The register needs nothing; the generator's matcher missed it because of the curly apostrophe, now fixed. It is in Paper B's list.
5. **Van den Bergh and Rietveld 2004.** No row (L126 is van den Bergh and Grazi 2014, a different work). B_s01-03.md line 80 says "not acquired and not in the register". The register would need a full row. A Crossref search finds a record that fits (van den Bergh and Rietveld, "Reconsidering the Limits to World Population: Meta-analysis and Meta-prediction", BioScience 54(3): 195, 2004, DOI 10.1641/0006-3568(2004)054[0195:rtltwp]2.0.co;2); nothing in the repo says this is the work the prose means, so it is not in the csv.

So three have no row and need one (FAO 2021 and FAOSTAT 2021 as one dataset row if the prose keeps them as citations, and Van den Bergh and Rietveld 2004); two have rows the B102 matcher missed.

## The a/b mapping

Checked against the prose, the page numbers and the claims csvs. The mapping is fixed in the generator (`LETTER` table), because the csv has no letter column.

| In the prose | Id | Work | Letter in the list |
|---|---|---|---|
| Higgins et al. 2018a, p. 196 (A$6.8 billion road and rail cost, A_s09-12.md line 83) | L172 | Informing transport infrastructure investments using TraNSIT, Comput. Electron. Agric. 154: 187-203 (p. 196 falls inside it) | 2018a |
| Higgins et al. 2018b, p. 341 (northern supply chains, seasonal flooding, supplementary.md) | L173 | Informing major government programs for rural transport infrastructure in northern Australia, Rangel. J. 40(4): 341-351 | 2018b |
| Grafton et al. 2018b (A_s09-12.md line 105; claims csv says 2018b is L189) | L189 | The paradox of irrigation efficiency, Science 361 | 2018b |
| (not cited alone; claims csv: "the 2018a work is L188") | L188 | Grafton and Wheeler, Economics of water recovery in the Murray-Darling Basin | 2018a |
| Qiu 2024 (B_s01-03.md line 15, China's regional functional planning); the prose has no letters | L199 | Carrying Capacity and China's Regional Functional Planning, chapter in the Springer book | 2024a |
| (no prose citation by content) | L108 | Carrying Capacity: Theory and Research Methods, chapter 1 of the same book | 2024b, flagged: it is in the list only through the ambiguous match |
| Hughes et al. 2022, p. 11 (A_s01-04.md line 27) | L152 | Modelling the effects of climate change on the profitability of Australian farms, Clim. Change | 2022a |
| Hughes 2022 (listed as a scope source not cited, A_s09-12.md) | L169 | Defining drought from the perspective of Australian farmers, Clim. Risk Manag. | 2022b |
| Summerhayes and Baker 2025 and 2026 (the prose uses the online-first year for L150) | L150 and L148 | Integrating urban land use planning (print 2026); Transforming food security policymaking (print 2026) | 2026a and 2026b; the prose years need changing |
| Lane 2014 with a page number (A_s05-08.md, "Lane 2014, p. 266") | L020 | The PhD thesis, QUT | no letter: its author line is Lane alone |
| Lane et al. 2014 / Lane, Dawes and Grace 2014 | L012 | Essential parameters of a resource-based carrying capacity assessment model, Ecol. Model. 272 | no letter: three authors |

In B102 the letters ran by title order, which gave Higgins 2018a to L173 and 2018b to L172. That was the reverse of the prose, and is now fixed. The prose uses "Higgins et al." and "Grafton et al." for the lettered works; an a/b is needed in the text wherever two entries share a first author and year.

## Wrong-value check

Wrong-value check: example only, not a value in the csv. Writing "Lane, J." for the author of the thesis (L020) would be wrong: the title page prints "Murray Lane (M. Arch, B. Blt Env., B. Arts)", so the csv has "Lane, M.", and the Crossref records for L012 to L014 also give Murray. For every Crossref row, first-author surname, volume and first page were compared with the register's own text; no mismatch was found. No initial, page or DOI was invented: where a field could not be read from Crossref, the PDF or the register it is empty and the entry is flagged.

## Notes for the editor

- Titles with an em dash (L097, L160, L178, L185) are as published by the journals; they are quoted work titles, not prose.
- The csv has no letter column, so the a/b letters live in the generator. If the prose later changes its citation years (Summerhayes and Baker, Fairlie, ABARES, Centre for Population, ABS), rerun the generator; the csv does not need to change.
- Crossref's capitalisation of titles (some Title Case) is kept as the journal prints it; the Elsevier sentence-case rule has not been applied.
- Abbreviations were left blank for 6 serials (7 entries) where I was not sure of the List of Title Word Abbreviations form: Australian Commodities, BHERT News, Earth's Future, Elementa, Search and The Land. The 130 abbreviations filled come from a table in the generator and still need a check against the List of Title Word Abbreviations.
