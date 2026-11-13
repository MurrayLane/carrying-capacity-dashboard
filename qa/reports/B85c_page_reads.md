# B85c: page-level reads, group 3 of 3 (decision 76)

Scope: 20 rows of `qa/literature_register.csv`. Files were read from `/home/user/carrying-capacity-models/`. Word and PowerPoint files were converted to PDF to read; scans were read as text or as page images. Nothing was fetched.

## Rows read

**L007 Foran and Poldy 2002 (Future Dilemmas, full report).** The file is the work named. Printed page equals PDF page.
- Confirmed: population 20.6, 25.1, 32.5 million in 2050 and 16.7, 25.5, 50.6 in 2100, Table 1.1 (p.31) and the text (p.45). Table 2.5 (p.64): 2050 requirements of grain 2.136, 2.713, 3.568, meat 2.278, 2.893, 3.804, fish 0.346, 0.439, 0.577 Mt against 1997-98 production 31.578, 3.514, 0.223 Mt. Embodied grain 6, 7.6, 10 Mt (p.64).
- Corrected: what_taken named Table 1.1 and Table 2.5 as requirement tables. Table 1.1 (p.31) is the population table; Table 2.5 (p.64) holds the requirements. The production figures are now given as printed.
- Not printed in the work: the 30 to 32 million (meat) and 76 to 80 million (grain). They follow from dividing production by the per-person requirement (30.0, 30.5, 31.8 and 79.9, 76.8, 75.6 million). what_taken now says so.

**L012 Lane, Dawes and Grace 2014.** Not reached: no file.

**L015 Peters et al. 2016.** Both copies match the work. Pages below are the publisher layout's printed pages (the repository copy is one page further on).
- Confirmed: 402 to 807 million, 1.3 to 2.6 times the 2010 population, 0.13 to 1.08 ha a person a year (abstract, p.1). 1.08 is the baseline diet and 0.13 to 0.14 the three vegetarian diets (p.8). 402 million baseline, 807 million lacto-vegetarian, "without trade" (p.9). Closed food system (pp.2, 3).
- Refined: the sensitivity analysis is on the share of cropland available for cultivated cropping (p.1, p.10).

**L020 Lane 2014 PhD thesis.** The row has no local_path, but the notes quote the thesis file under Papers and manuscripts/ (sha256 matches the notes). Printed page equals PDF page.
- Confirmed: footprint as an inversion of carrying capacity (p.112); "seven global hectares" and Bangladesh 0.7 (p.115); Lenzen and Murray 13.6 ha (p.113); Gutteridge 180,000 (section 6.4.1, p.124); Table 16 (p.280) Australia short-term large-scale 40,439,187 and long-term large-scale 9,431,487; Table 28 (p.385); chapter 6 typology (pp.106 to 136).
- Corrected: "about 2012" for the GFN Country Trends citation has no printed date (notes on p.115, bibliography p.403), so it was removed. Section 6.1.2 runs from p.111 to p.117, not to p.115. Section 6.4.1 is pp.124 to 125.
- For the caller: Table 16 gives Australia short-term 40,439,187, while the L012 row quotes 40,450,144 from the 2014 article. L012 was not reached, so this is not resolved.

**L024 Wackernagel et al. 2002.** The file is the work named. Pages are the journal's (9266 to 9271).
- Confirmed: overshoot from the 1980s (p.9266, p.9268, p.9269); 70% in 1961 and 120% in 1999 (pp.9266, 9268); Table 1 global per-capita figures for 1999 (p.9268); no Australian figure (the word Australia is not in the article).
- Corrected: the article never uses the name National Footprint Accounts; it describes "our global accounts". The supporting information is described as the 1999 calculation results and an annotated spreadsheet (p.9266), not as a country table; its contents were not seen. The text names three countries (United States 9.7, United Kingdom 5.4, Germany 4.7 global hectares, p.9268); this is now in what_taken.

**L034 Gutteridge (report, slides, workbook).** Pages are those of the converted files and may differ from Word's own pagination.
- Confirmed: 180,000 people (report p.32 and p.34; slides 21, 22); 7.33 ha with 300,000 people (report p.31, p.32; slide 20). Report population base 2,331,740 (p.7); slides "SEQ 2.6m (2005)" (slide 13). "14 times" is the thesis's wording (thesis p.125).
- Corrected: 7.33 is an intermediate step; the 180,000 result rests on 12 ha per capita (p.32). what_taken now says so. The workbook holds neither figure.

**L051 ABS 4306.0 1991-92.** Printed page is PDF page minus 4.
- Confirmed: Table 1 (printed pp.5 to 6). Eggs and egg products total 12.4 kg is the 1978-79 average; 1988-89 and 1991-92 read "n.c." (not collected), so 12.4 is the last kilogram value printed (p.6). No pulses line in Table 1; Table 3 (p.13) lists beans and peas only among green vegetables. Figures confirmed.

**L055 Lane 2010 Land Use Policy.** The file is the accepted manuscript of the work named (cover sheet p.1, title p.2). Pages are PDF pages; the text has no printed numbers.
- Corrected: the text does not mention Douglas Shire or Peters (whole text and reference list searched); both were removed from what_taken. The Noosa item is Summers 2004 (p.5).
- Confirmed: Limits to Growth (p.7); Ecological Footprint after Rees and Wackernagel (pp.5, 7); Gutteridge's South East Queensland analysis (p.6); Fairlie (pp.6, 7); Fearnside (pp.7 to 14). No model figures of the author's own; Summers's 61,350 for Noosa Shire is quoted (p.5).

**L036 Migration Committee 1986 (cited by Henry and Godden).** The Migration Committee report was not reached. The citing source named in the notes was read from the scan in the archive: p.97, section 1, "10 to 480 million (Migration Committee 1986, reported in Clarke, p.1)". Figure and attribution confirmed as cited. read_or_reported is left as "reported"; status set to "self-checked (B85)".

## Rows not reached

- L039 Douglas Shire: no file for the study. The thesis passage in the notes was confirmed at thesis p.122 (section 6.3.2). Status unchanged.
- L012, L062, L068, L074, L083, L087, L099, L107, L131, L011, L127: not reached: no file. The L074, L083 and L099 notes mention an open copy in a session scratch area, but give no path or address, so none was used. A file named gerten.pdf sits in this session's scratch folder, but its origin is not recorded in the row, so it was not read. For these rows only a "not reached: no file" line was appended; read_or_reported and status were left as they were.

## Rows touched

L007, L011, L012, L015, L020, L024, L034, L036, L039, L051, L055, L062, L068, L074, L083, L087, L099, L107, L127, L131 (20 rows).

Checks before saving: the file was re-read from disk and written in one step. Row count 243 lines including the header, so 242 rows; 12 columns on every row; parses with Python's csv module; no em dashes; line endings unchanged (CRLF, 243 of 243); a comparison with the file as it stood just before saving shows exactly these 20 rows differ.

## Wrong-value check

Example only, not a finding: a citation such as "Table 2.5, p.46" for the Foran and Poldy food requirements would be wrong; the table is on p.64 (p.46 holds Table 2.1, the city populations).
