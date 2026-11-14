# B102: reference-list generator (decision 98)

Builder B102. Tool: `qa/tools/make_references.py`. Run `python3 qa/tools/make_references.py A` or `B`. It reads the claims csvs, the section files and `qa/literature_register.csv`, edits none of them, and writes `papers/A_results/draft/references.md` or `papers/B_methods/draft/references.md`. Two runs give identical output (checked with cmp on the printed report and md5 on both lists).

## Counts

| | Paper A | Paper B |
|---|---|---|
| Register ids cited in the claims csvs (including supplementary_claims.csv) | 66 | 66 |
| Added because the prose names a work whose register row the script could identify, but no claims csv cites it | 18 | 58 |
| Entries in the list | 84 | 124 |
| Entries marked [CHECK] | 83 | 123 |
| Entries with no CHECK | 1 (L003, Henry and Godden 1995, the only row that gives initials) | 1 (same) |
| Ids with no register row | none | none |

Nearly every entry carries a CHECK for one reason: the register keeps authors as surnames only ("Peters et al."), so initials, and for "et al." rows the full author list, are not in it. The script does not guess initials. This is a register gap, not a parsing failure; the other CHECK reasons are listed per entry below.

Section files scanned: `A_s*.md` / `B_s*.md` and `supplementary.md`. `paper_A_draft1.md` and `paper_B_draft1.md` were not scanned (older merged drafts). Paper B's section files are being edited by B101, so the 58 prose-only entries and the prose lists below will change; rerun the script after B101 finishes.

## Reasons for CHECK, by count

Paper A: author initials 61; place of publication 11 (government reports and chapters, none in the register); end page only the start page is given 7; no page or article number 7; full author list and initials 6; book editors 5; publisher 5; title/issuer/series not separated 5; register title not in the usual form (printed as is) 3; year 2; volume 2; one each for date accessed, URL, page range, thesis title, DOI, "title to confirm".

Paper B: author initials 84; full author list and initials 21; title missing 20; place of publication 15; no page or article number 13; year missing 11; volume 9; journal 7; register title not in the usual form 6; issuer 5; pages 5; end page 4; title/issuer/series not separated 4; DOI none in register 4; publisher 3; URL 2; editors 2; edition 2; one each for date accessed, thesis title, book title, page range.

## Every CHECK entry and what it lacks

### Paper A

- L241 (ABARES 2025): place of publication
- L234 (ABARES None): year; date accessed
- L162 (Ananda 2023): author initials; end page (register gives only '136230')
- L218 (Anderson 2019): author initials; pages or article number
- L063 (AUS-MEAT 68.7% meat yield [ERRATA row 2]; the AUS-MEAT guide 2005): register title not in the usual form; not parsed; register text printed as is
- L222 (Badami 2015): author initials
- L182 (Beltran-Peña 2020): author initials
- L146 (Bolleter 2018): author initials
- L168 (Botterill 2021): author initials
- L228 (Centre for Population 2025): place of publication
- L179 (Clapp 2017): author initials
- L186 (Clinton 2018): author initials
- L216 (Cottrell 2019): author initials
- L002 (CSIRO submission to the National Population Inquiry 1975): register title not in the usual form; not parsed; register text printed as is
- L191 (D'Odorico 2018): author initials
- L144 (Davies 2024): author initials; book editors; publisher; place of publication
- L174 (Davis 2020): author initials
- L230 (Department of Climate Change, Energy, the Environment and Water 2017): place of publication
- L231 (Department of Climate Change, Energy, the Environment and Water 2019): title, issuer, series and place not separated in the register
- L242 (Department of Climate Change, Energy, the Environment and Water None): year; URL
- L154 (Falster 2024): author initials
- L007 (Foran 2002): author initials; title, issuer, series and place not separated in the register
- L060 (Geoscience Australia and ABARE 2010): title, issuer, series and place not separated in the register
- L189 (Grafton 2018): author initials
- L135 (Grundy 2016): full author list and initials
- L166 (Han 2024): author initials
- L097 (Hendrie 2014): full author list and initials
- L173 (Higgins 2018): author initials
- L172 (Higgins 2018): author initials
- L153 (Hochman 2017): author initials
- L229 (House of Representatives Standing Committee on Agriculture 2023): place of publication
- L170 (Hughes 2017): author initials; book editors; publisher; place of publication; page range
- L152 (Hughes 2022): author initials; pages or article number
- L151 (James 2016): author initials
- L080 (Kastner 2012): author initials; pages or article number
- L074 (Khorsandi 2023): author initials
- L073 (Khorsandi 2022): author initials; end page (register gives only '153038')
- L180 (Kinnunen 2020): author initials
- L175 (Kummu 2020): author initials
- L104 (Kurtz 2020): full author list and initials
- L192 (Ladha-Sabur 2019): author initials
- L020 (Lane 2014): author initials; thesis title (register quotes only a section heading)
- L014 (Lane 2017): author initials
- L012 (Lane 2014): author initials; title (register gives only the journal); volume; pages or article number
- L013 (Lane 2015): author initials; title (register gives only the journal); volume; pages or article number
- L185 (Langemeyer 2021): author initials; end page (register gives only '104055')
- L224 (Lawrence 2013): author initials
- L158 (Malau-Aduli 2022): author initials; end page (register gives only '100228')
- L165 (Marchand 2016): author initials
- L156 (Mayberry 2019): author initials
- L147 (McDonald 2017): author initials
- L183 (Mcdougall 2020): author initials; end page (register gives only '104554')
- L161 (Mirosa 2020): author initials; book editors; publisher; place of publication
- L184 (Payen 2022): author initials; pages or article number
- L136 (PMSEIC 2010): issuer, series and publication details not separated in the register; text kept as is
- L115 (Poore 2018): author initials
- L099 (Productivity Commission 2011): title, issuer, series and place not separated in the register
- L233 (Productivity Commission 2023): title, issuer, series and place not separated in the register
- L187 (Prosser 2021): author initials
- L160 (Reutter 2017): author initials
- L096 (Ridoutt 2020): full author list and initials
- L159 (Ridoutt 2024): author initials
- L116 (Roos 2017): full author list and initials
- L190 (Rosa 2020): author initials; pages or article number
- L181 (Schreiber 2021): author initials
- L176 (Soliman Hunter 2021): author initials; end page (register gives only '112472')
- L163 (Spang 2019): author initials
- L149 (Summerhayes 2024): author initials; end page (register gives only '102736')
- L150 (Summerhayes 2025): author initials
- L148 (Summerhayes 2026): author initials
- L171 (Sysak 2017): author initials; book editors; publisher; place of publication
- L138 (Thompson 2011): title is marked 'to confirm' in the register; author initials; DOI (none in the register; confirm whether one exists)
- L120 (Tilman 2014): author initials
- L167 (Timmer 2024): author initials; book editors; publisher; place of publication
- L227 (Treasury 2021): place of publication
- L226 (Treasury 2023): place of publication
- L062 (USDA Handbook 697 [ERRATA 'Information available in 2011): register title not in the usual form; not parsed; register text printed as is
- L117 (van Zanten 2016): full author list and initials
- L239 (Wiedemann 2015): author initials
- L155 (Wittwer 2021): author initials
- L177 (Wood 2018): author initials
- L225 (Wright 2011): author initials
- L103 (Zumkehr 2015): author initials

### Paper B

- L051 (ABS 1991): register title not in the usual form; not parsed; register text printed as is
- L017 (Alexander 2016): full author list and initials; title (register gives only the journal); end page (register gives only '88')
- L218 (Anderson 2019): author initials; pages or article number
- L067 (AUSNUT 2007): URL; date accessed; title
- L009 (Bellotti 2017): register title not in the usual form; not parsed; register text printed as is
- L182 (Beltran-Peña 2020): author initials
- L221 (Bentham 2020): author initials
- L193 (Biermann 2020): author initials
- L087 (Blomqvist 2013): author initials
- L219 (Bodirsky 2020): author initials; pages or article number
- L146 (Bolleter 2018): author initials
- L004 (Borrie 1975): author initials; title; place of publication; issuer
- L076 (Bryan 2016): full author list and initials
- L068 (Buzby 2010): author initials; title; place of publication; issuer
- L016 (Cassidy 2013): full author list and initials; title (register gives only the journal)
- L088 (Chapman 2018): author initials
- L204 (Chaudhary 2019): author initials
- L143 (Chisholm 2000): author initials; volume
- L179 (Clapp 2017): author initials
- L106 (Cohen 2017): author initials
- L049 (Cohen None): year; author initials; title; journal; volume; pages
- L216 (Cottrell 2019): author initials
- L010 (CSIRO 2025): register title not in the usual form; not parsed; register text printed as is
- L002 (CSIRO submission to the National Population Inquiry 1975): register title not in the usual form; not parsed; register text printed as is
- L230 (Department of Climate Change, Energy, the Environment and Water 2017): place of publication
- L231 (Department of Climate Change, Energy, the Environment and Water 2019): title, issuer, series and place not separated in the register
- L242 (Department of Climate Change, Energy, the Environment and Water None): year; URL
- L084 (Erb 2016): full author list and initials
- L105 (Fader 2013): full author list and initials
- L041 (Fairlie None): year; author initials; title; place of publication; issuer
- L042 (Fearnside 1985): author initials; DOI (none in the register; confirm whether one exists)
- L043 (Fearnside 1990): author initials; title and journal (register gives only a note); journal; pages or article number
- L029 (Fischer 2002): full author list and initials; title, issuer, series and place not separated in the register
- L007 (Foran 2002): author initials; title, issuer, series and place not separated in the register
- L208 (Gao 2017): author initials
- L205 (Gazan 2018): author initials
- L083 (Gerten 2020): full author list and initials
- L085 (Giampietro 2014): author initials
- L142 (Gilland 2006): author initials
- L086 (Goldfinger 2014): author initials
- L223 (Grant 2009): author initials
- L091 (Graymore 2010): author initials
- L201 (Greenhalgh 2018): author initials; pages or article number
- L034 (Gutteridge 2005): register title not in the usual form; not parsed; register text printed as is
- L200 (Haddaway 2020): author initials
- L044 (Hardin None): year; author initials; title; journal; volume; pages
- L075 (Hatfield-Dodds 2015): full author list and initials
- L236 (Helton 2003): author initials
- L210 (Herrington 2020): author initials
- L153 (Hochman 2017): author initials
- L141 (Hopfenberg 2003): author initials; DOI (none in the register; confirm whether one exists)
- L006 (House of Representatives Standing Committee for Long Term Strategies 1994): register title not in the usual form; not parsed; register text printed as is
- L229 (House of Representatives Standing Committee on Agriculture 2023): place of publication
- L211 (Jones 2023): author initials
- L080 (Kastner 2012): author initials; pages or article number
- L074 (Khorsandi 2023): author initials
- L073 (Khorsandi 2022): author initials; end page (register gives only '153038')
- L180 (Kinnunen 2020): author initials
- L214 (Kummu 2016): author initials; pages or article number
- L104 (Kurtz 2020): full author list and initials
- L192 (Ladha-Sabur 2019): author initials
- L055 (Lane 2010): author initials; title (register gives only the journal); volume; pages or article number
- L020 (Lane 2014): author initials; thesis title (register quotes only a section heading)
- L014 (Lane 2017): author initials
- L012 (Lane 2014): author initials; title (register gives only the journal); volume; pages or article number
- L013 (Lane 2015): author initials; title (register gives only the journal); volume; pages or article number
- L022 (Lenzen 2001): author initials
- L215 (Li 2018): full author list and initials
- L025 (Lin 2018): full author list and initials
- L165 (Marchand 2016): author initials
- L235 (McKay 1979): author initials
- L212 (Mesgaran 2017): author initials; pages or article number
- L036 (Migration Committee 1986): title; place of publication
- L196 (Montoya 2018): author initials
- L069 (Muth 2011): author initials; title; place of publication; issuer
- L005 (National Population Council 1991): title; place of publication
- L209 (Navarro Garcia 2022): author initials
- L035 (Nix None): year; author initials; title; place of publication; issuer
- L015 (Peters 2016): full author list and initials; title (register gives only the journal)
- L040 (Peters None): year; author initials; title and journal (register gives only a note); journal; pages or article number
- L077 (Peters 2009): author initials
- L136 (PMSEIC 2010): issuer, series and publication details not separated in the register; text kept as is
- L115 (Poore 2018): author initials
- L048 (Price None): year; author initials; title; journal; volume; pages
- L099 (Productivity Commission 2011): title, issuer, series and place not separated in the register
- L199 (Qiu 2024): author initials; book editors; publisher; place of publication
- L108 (Qiu 2024): author initials; book editors; book title (register gives: chapter 1 of a Springer book on carrying capacity of resources, environment, population and economy in China); publisher; place of publication; page range
- L139 (Rees 1992): author initials; DOI (none in the register; confirm whether one exists)
- L140 (Rees 1996): author initials; DOI (none in the register; confirm whether one exists)
- L194 (Rees 2023): author initials
- L160 (Reutter 2017): author initials
- L079 (Ridoutt 2017): full author list and initials
- L096 (Ridoutt 2020): full author list and initials
- L206 (Ridoutt 2021): author initials
- L240 (Rockström 2009): full author list and initials
- L116 (Roos 2017): full author list and initials
- L213 (Rosa 2018): author initials
- L190 (Rosa 2020): author initials; pages or article number
- L237 (Saltelli 2008): author initials; edition (or confirm first edition); place of publication
- L046 (Sayre None): year; author initials; title; journal; volume; pages
- L045 (Seidl None): year; author initials; title; journal; volume; pages
- L124 (Shepon 2016): full author list and initials
- L023 (Simpson 2000): author initials
- L203 (Snyder 2019): author initials
- L176 (Soliman Hunter 2021): author initials; end page (register gives only '112472')
- L163 (Spang 2019): author initials
- L202 (Sukhera 2022): author initials
- L120 (Tilman 2014): author initials
- L227 (Treasury 2021): place of publication
- L226 (Treasury 2023): place of publication
- L107 (Tucker 2020): author initials
- L062 (USDA Handbook 697 [ERRATA 'Information available in 2011): register title not in the usual form; not parsed; register text printed as is
- L207 (Van Dooren 2018): author initials; pages or article number
- L117 (van Zanten 2016): full author list and initials
- L134 (Wackernagel 1994): author initials
- L024 (Wackernagel 2002): full author list and initials; end page (register gives only '9266')
- L129 (Wackernagel 2019): full author list and initials
- L050 (Wackernagel None): year; author initials; title; edition (or confirm first edition); publisher; place of publication
- L109 (Wang 2022): author initials
- L131 (Wiedmann 2018): author initials
- L081 (Willett 2019): full author list and initials
- L198 (Zhang 2018): author initials
- L103 (Zumkehr 2015): author initials

## Sources seen only second-hand, or not read in full

Rows cited only as reported in another work (second-hand): L002
Rows not read in full (abstract only, record only, not read, not reached): L138

Rows cited only as reported in another work (second-hand): L002, L004, L005, L035, L036
Rows not read in full (abstract only, record only, not read, not reached): L108, L235, L236, L237

The list itself does not yet say which works were not seen; that needs a decision on wording (a note under the list, or a column in the author's own check).

## Prose citations

Prose-only ids (register row identified, no claims-csv id behind the citation; these are in the list but should be given a claims-csv row or dropped from the prose):

- Paper A: L099, L135, L138, L146, L149, L158, L160, L161, L162, L163, L166, L167, L177, L184, L185, L186, L190, L222
- Paper B: L004, L005, L024, L025, L029, L074, L075, L076, L079, L080, L084, L086, L088, L091, L096, L099, L103, L104, L106, L107, L108, L109, L115, L116, L117, L120, L124, L129, L131, L141, L160, L165, L176, L190, L192, L193, L194, L196, L198, L199, L204, L205, L206, L207, L208, L209, L211, L212, L213, L214, L215, L216, L218, L219, L221, L226, L227, L237

Prose citations with no register row (not in the list):

Paper A
  FAO 2021  [A_s09-12.md]  (a register row with the same name but no year exists: L071)
  Wiedemann 2017  [A_s09-12.md]

Paper B
  Cohen 1995  [B_s01-03.md]  (a register row with the same name but no year exists: L049)
  FAOSTAT 2021  [B_s01-03.md, B_s04-05.md]
  Fairlie 2007  [B_s04-05.md, B_s06-09.md]  (a register row with the same name but no year exists: L041)
  Hardin 1986  [B_s01-03.md]  (a register row with the same name but no year exists: L044)
  Meyer and Ausubel 1999  [B_s01-03.md, supplementary.md]  (a register row with the same name but no year exists: L047)
  O'Neill et al. 2018  [B_s01-03.md]
  Peters, Wilkins and Fick 2007  [B_s04-05.md, B_s06-09.md, supplementary.md]  (a register row with the same name but no year exists: L040)
  Price 1999  [B_s01-03.md]  (a register row with the same name but no year exists: L048)
  Sayre 2008  [B_s01-03.md, supplementary.md]  (a register row with the same name but no year exists: L046)
  Seidl and Tisdell 1999  [B_s01-03.md]  (a register row with the same name but no year exists: L045)
  Taylor 1922  [B_s01-03.md]  (a register row with the same name but no year exists: L001)
  Van den Bergh and Rietveld 2004  [B_s01-03.md]

Where the note says "a register row with the same name but no year exists", the row is a short-form record with no year (for example L044 Hardin), so the script cannot tie the prose year to it. Those rows are in the list through the claims csvs where cited; the prose year needs checking against the real work. "FAOSTAT 2021", "O'Neill et al. 2018", "Van den Bergh and Rietveld 2004" (the register has van den Bergh and Grazi 2014, a different work) and "Wiedemann 2017" have no register row at all.

Prose citations that match more than one register row (a, b letters are assigned in the list by title order and may not match the letters the prose uses): Paper A: Higgins et al. 2018a and 2018b (L172, L173), Lane 2014 and Lane et al. 2014 (L012, L020). Paper B: Lane 2014 (L012, L020), Qiu 2024 (L108, L199). Letters in the list: Higgins 2018a is L173 and 2018b is L172 (title order); Qiu 2024a is L199 and 2024b is L108. The prose must be checked against these.

## Journal abbreviations not known

Kept in full for a later pass: Australian commodities (L138, ABARES periodical), Earth's Future (L184, L186), BHERT News (L143, a newsletter, not a journal). All other journals were abbreviated from a table inside the script (about 90 titles, ISO 4 style, only forms I am sure of). The table should still be checked against the List of Title Word Abbreviations before submission.

## Other notes

- Dates in page ranges use the en dash. "Horst and Gaolach 2014 (issue 2015)" is given the issue year 2015 where the register has "(issue YYYY)"; "(online YYYY)" is ignored and the first year is used.
- Corporate authors (CSIRO, Treasury, departments, committees) are kept whole and carry no initials CHECK. Government reports have no place of publication in the register, so each carries a CHECK for place.
- Rows the script could not parse safely are printed with the register text as is and a CHECK. Paper A: L002, L062, L063. Paper B: L002, L006, L009, L010, L034, L051, L062.
- The script prints, besides the list: ids with no register row, second-hand rows, prose-only ids, unmatched prose citations, ambiguous prose citations, unknown journal names and the CHECK list. The same report is reproduced here.

## Wrong-value check:

Example only (not a real register row): a register title `Smith and Jones 2019, "A deliberately incomplete example", Nature 12(3)` gives

`Smith, Jones, 2019. A deliberately incomplete example. Nature 12 (3). [CHECK: author initials; pages or article number; DOI (none in the register; confirm whether one exists)]`

so a missing page range, missing initials and a missing DOI are each flagged and nothing is guessed.

## Files written

- `qa/tools/make_references.py`
- `papers/A_results/draft/references.md`
- `papers/B_methods/draft/references.md`
- `qa/reports/B102_reference_list_tool.md`
