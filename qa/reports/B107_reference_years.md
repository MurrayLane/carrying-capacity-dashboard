# B107: reference year decisions and regenerated lists

Builder B107, 2026-11-15. Rule used: the year of the version of record (print volume year for a journal article; the imprint or issue date for a report; for a book the imprint year). Files written: `qa/references.csv`, `qa/literature_register.csv` (title year and notes of the rows below, plus the new row L246), the draft section files and two claims csvs named below, `qa/tools/make_references.py` (LETTER table and one corporate-author word, see below), both `references.md` files, and this report. The register was re-read from disk before the save and checked after it: only my rows differ (L005, L041, L044, L051, L086, L142, L150, L157, L209, L210, L228, L237, L241, L246). The rows L244 and L245 (B106) were not touched.

## Year decisions

| Id | Printed year and where | Register before | Prose before | After |
|---|---|---|---|---|
| L150 Summerhayes and Baker | 2026: Wiley stamp "14682427, 2026, 3" on PDF pages 2 and 3 (volume year, issue 3, pp. 527-544); page 1 carries "(c) 2025" for the online-first copy | 2025 | 2025 | 2026, letter 2026a |
| L148 Summerhayes and Baker (same authors, same year) | 2026 (Food Security 18(4)), already 2026 | 2026 | 2026 | 2026b |
| L157 Wiedemann | 2017: PDF page 1 "Animal Production Science, 2017, 57, 1149-1162" and "Journal compilation CSIRO 2017"; online 5 July 2016 | 2016 | 2017 (A_s09-12, already) | 2017 |
| L209 Navarro Garcia | 2023: the file (PMC text) prints volume 18 and an online date of 5 September 2022 but no print year; volume 18 is the 2023 volume (Crossref, B103). This year rests on the volume, not on a printed year | 2022 | 2022 | 2023 |
| L210 Herrington | 2021: PDF page 1 "Journal of Industrial Ecology 2021;25:614-626"; stamp "2021, 3" on pages 2 and 3; "(c) 2020 by Yale University" is the online-first copy | 2020 | 2020 | 2021 |
| L237 Saltelli and others (book) | 2008: no file on disk (record only). Wiley imprint year; Crossref print record 18 Dec 2007 not used. This decision rests on the register and Crossref, not on a page | 2008 | 2008 (Saltelli et al. 2008) | 2008 (references.csv was 2007) |
| L142 Gilland | 2006: every page of the PDF (misnamed Gillard2007.pdf) reads "Popul Environ (2006) 28:1-16"; online 13 Feb 2007 | 2006 | 2006 | 2006 (references.csv was 2007) |
| L241 ABARES | 2026: page 1 "June 2026"; imprint "Commonwealth of Australia 2026" (PDF page 2) | 2025 | 2025 | 2026, letter 2026a |
| L234 ABARES Snapshot (not in the brief; letter effect only) | February 2026 | none | "ABARES undated" | list now reads 2026b; prose left as undated (see open points) |
| L228 Centre for Population | 2026: imprint "Commonwealth of Australia 2026", ISBN 978-1-923278-34-9 (PDF page 2); no issue date printed; the title keeps "2025 Population Statement" | 2025 | 2025 | 2026 |
| L051 ABS 4306.0 | 1994: title page "embargoed until 11.30 am 21 June 1994", "(c) Commonwealth of Australia 1994" (PDF page 1); reference period 1991-92 | none in title ("1991-92" is the reference period) | "ABS 4306.0", no year | 1994 in references.csv; title and prose unchanged |
| L005 National Population Council | 1992: no file for the report itself; the Jones report (L006) prints "National Population Council, 1992" in seven footnotes and says "the 1992 report" at paras 4.24 and 5.29; only para 2.15 says 1991 | 1991 | 1991 (Table 1 label) | 1992 |
| L041 Fairlie | 2008: the file says it is an edited version of an article "first published in The Land 4, in 2008" (PDF page 1); the file is the later chapter version, no date of its own | none in title | 2007 | 2008 |

## Register faults

- L086: references.csv already carries the reply's own DOI 10.1016/j.ecolind.2014.04.025 (checked); the register text was not edited, a note was added.
- L044: references.csv title "Cultural carrying capacity: a biological approach to human problems" checked against page 1 of the file (the running head "AIBS News" is not part of the title); a note was added to the register row.

## Prose lines changed (file:line)

- A_s01-04.md:9 Centre for Population 2025 to 2026
- A_s01-04.md:23 Summerhayes and Baker 2026 to 2026b (pp. 963-964, L148); 2025 to 2026a (p. 534, L150)
- A_s01-04.md:27 ABARES 2025 to 2026a
- A_s09-12.md:138 "FAO 2021-23 ... carry no release" to "FAOSTAT (2025) data for 2021 to 2023 (A315 to A320); the release is the bulk file dated 14 October 2025 (register row L246)"
- B_s01-03.md:5 (abstract) "(FAOSTAT 2021-23)" to "(FAOSTAT 2025, data for 2021 to 2023)", written in this form because the phrase sits inside brackets
- B_s01-03.md:15 Centre for Population 2025 to 2026
- B_s01-03.md:30 Table 1 label National Population Council 1991 to 1992
- B_s01-03.md:53 Herrington (2020) to (2021)
- B_s01-03.md:80 note 5: Van den Bergh and Rietveld 2004 "not acquired and not in the register" to "now in the register as L245 (filed 2026-11-15)". This is the only place the prose names it.
- B_s04-05.md:11 Fairlie 2007 to 2008
- B_s04-05.md:39 Navarro Garcia et al. 2022 to 2023; Herrington 2020 to 2021
- B_s04-05.md:59 "FAOSTAT 2021-23" to "FAOSTAT (2025) data for 2021 to 2023"
- B_s06-09.md:77 Fairlie 2007 to 2008
- supplementary.md:49 (Paper B) Navarro Garcia et al. 2022 to 2023; Herrington 2020 to 2021

Claims csvs changed to match the quoted text: `B_s01-03_claims.csv` (row for abstract sentence 3; the Table 1 National Population Council row label) and `B_s04-05_claims.csv` (section 5 sentence 2 fragment). The other claims csvs cite these works by register id and carry no year, so they needed no change. Not changed: the `paper_A_draft1.md` and `paper_B_draft1.md` merges (not named in the brief; they still carry the old years) and `B_s04-05.md:71` "the FAO food balance for 2021-23" and `A_s09-12.md:87` "(FAO food balance)", which are not the phrases the brief names. No number in any draft was changed; no em dash was added.

## Dataset row added

L246, kind "dataset (bulk download)": FAOSTAT 2025, "Food Balances (2010-), Food Balance Sheets, all data, normalized", file FoodBalanceSheets_E_All_Data_(Normalized).csv; file dated 14 October 2025 (the citation year), downloaded 6 November 2026; URL https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_All_Data_(Normalized).zip; unpacked csv sha256 2834e1012daaebf4e4f8195fa86ce9063d1c81fdd9d7c04cbf0aba758ccfa020, zip sha256 26200855ed5da3d0805e34219124e241d0e0bc6959d0995ebc77a10dd84cbaf1 (from `qa/fao_bulk_hashes.csv`; source row D17). It has a matching row in `qa/references.csv` (type dataset). Both papers now list it as "FAOSTAT, 2025 ... [dataset]".

## Generator changes

- LETTER table: added L150 a, L148 b (Summerhayes and Baker 2026a, 2026b) and L241 a, L234 b (ABARES 2026a, 2026b). The ABARES pair is a new letter caused by the L241 year change (both are now 2026).
- CORP_WORDS: added "FAOSTAT" so the dataset's corporate author is not flagged for initials.

## CHECK counts

| | Paper A | Paper B |
|---|---|---|
| Entries before | 85 | 128 (127 in B103; L245 added since) |
| CHECK before | 21 | 31 (30 in B103) |
| Entries after | 86 | 129 |
| CHECK after | 19 | 28 |

Two runs of the generator for each paper give identical printed reports and identical `references.md` (md5 A 65bbff16..., B 2553718c...). Registers parse: literature register 246 data rows (245 plus L246), 12 columns each; references.csv 180 data rows (179 plus L246), 19 columns each.

Cleared: L150, L157, L209, L210, L142, L237 year flags; L051 and L228 prose-year flags; L005 and L041 year flags; the two "no register row" prose citations (FAOSTAT 2021, Fairlie 2007) and "FAO 2021" in Paper A; Van den Bergh and Rietveld now resolves to L245.

## Entries still flagged, and why

Paper A (19): L241 author form (corporate in prose, four named authors on the page); L063 publisher, place, title as printed; L228 place; L144 editors, place; L230 place; L231 publisher, place, authors; L242 year; L060 publisher, place; L002 DOI; L170 editors, place, page range; L020 place; L161 editors, place; L099 title, place, series; L171 editors, place; L138 initials, DOI; L167 editors, place; L227 place; L226 place; L062 year, publisher, place, authors.

Paper B (28): L051 place; L067 URL, date accessed, version; L068 initials, title, publisher, place; L143 volume, surname spelling; L010 place; L230 place; L231 publisher, place, authors; L242 year; L041 volume, pages, DOI, and the file is the later chapter version, not the issue 4 article; L002 DOI; L034 publisher, place; L020 place; L036 title, publisher, place (second-hand); L069 initials, title, publisher, place; L005 second-hand, the report itself is not on hand; L004 identity rests on a footnote; L035 initials, year, title, publisher, place; L099 title, place, series; L199 and L108 book editors (L108 is not cited by content); L237 place; L001 end page and initials from a footnote; L227 and L226 place; L062 year, publisher, place, authors; L245 initials, pages, DOI (the row has no references.csv entry; B106's rows, not mine); L134 place; L050 place, edition, year.

## Open points for the editor

1. L234 (ABARES Snapshot): the prose says "ABARES undated" (a deliberate earlier decision, note 8 in A_s01-04) but the list prints it as ABARES 2026b because its page says February 2026. The prose and the list disagree; decide whether the prose becomes "ABARES 2026b".
2. L245 has no row in `qa/references.csv`, so Paper B's list builds it from the register text and prints a garbled journal field (BioScience 54(3): 195-204 ... in the abbreviation warning). B106 owns that row.
3. L237 and L209: the decision rests on Crossref and the register (L237), and on the journal volume (L209), not on a printed year on a page.
4. L041: the file is the later chapter version; the year 2008 is the file's own statement of first publication in The Land, and the register's thesis citation says Winter 2007-8.

Wrong-value check: example only, not a value in any file. Citing "Herrington 2020" would be wrong; the page prints "Journal of Industrial Ecology 2021;25:614-626", so the citation year is 2021 and 2020 is the online-first copyright year.
