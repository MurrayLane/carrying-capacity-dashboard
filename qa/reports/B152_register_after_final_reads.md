# B152: registers and reference lists after the final-read patches (B149a, B149b)

Builder report. Brief `qa/briefs/B152_register_after_final_reads.md`. No git, no subagents, no network. Written: `qa/claims_register.csv`, `qa/references.csv`, `qa/literature_register.csv`, `papers/DECLARATIONS.md`, `papers/A_results/draft/references.md`, `papers/B_methods/draft/references.md` and this report. `qa/sources_register.csv` is unchanged: every year and URL the new entries needed was already in its rows (where it had none, the entry says so). No paper section file, script, frozen release or `results/` file was touched. CRLF line endings and the two blank rows of the claims register are kept (the 894 unchanged rows are byte-identical; only the 30 rows listed in section 4 differ).

## 0. Read this first: the tool needs a four-line fix, and the two lists were built with it

The committed `qa/tools/make_references.py` cannot do three things the brief expects, and I may not edit it (not in my write list):

1. **The "b" suffix stays.** The last loop of `main()` forces `ylabel = year + LETTER[id]` for every id in the LETTER table, even when the "a" partner is not in the list. So ABARES (2026b), Higgins et al. (2018b) and Summerhayes and Baker (2026b) print with "b" although their "a" works are out. Regenerating confirms it: the committed tool still prints all three with "b".
2. **Nothing can list an entry whose prose form has no year or whose first word is "ABS".** The scan needs a four-digit year and drops a bare "ABS" (it is in STOP). So ABS 2021 and the six "n.d." sources (ABS n.d.a to n.d.d, FAO n.d.a, n.d.b) cannot be found; and the companion paper (L259) is found only by the phrase "Paper A", which B149b removed from the text ("Lane, in preparation").
3. **"UN" is not read as a corporate author**, so UN (2015) gets a spurious "author initials" CHECK.

The fix (`diff` against the committed tool, ROOT line aside) is:

```
41c41,43   NAMED_CITATIONS = {"L004": ("B", "National Population Inquiry (Borrie)"), "L259": ("B", "Lane, in preparation"),
                              "L260": ("A", "ABS n.d.a"), "L261": ("A", "ABS n.d.b"), "L262": ("A", "ABS n.d.c"), "L263": ("A", "ABS n.d.d"),
                              "L264": ("A", "ABS 2021"), "L266": ("A", "FAO n.d.a"), "L267": ("A", "FAO (n.d.b)")}
142        ... "Rawtec", "DCCEEW", "UN"}                                  (add "UN" to CORP_WORDS)
1137       if e["id"] in LETTER and e["year"] and len(groups[letter_key(e) if e["form"] == "csv" else (e["authors"], e["year"])]) > 1:
```

I ran a scratch copy of the tool with exactly these changes (outside the project) and wrote its output to the two `references.md` files with `--no-ids` (A with `--style springer`); no entry was edited by hand and two runs are identical. **Apply the same change to `qa/tools/make_references.py` before anyone regenerates, or the next run drops the new entries and brings back the "b" labels.** The counts below are given both ways.

## 1. Reference lists: entries and CHECK counts

| | Entries before | CHECK before | Entries after (patched tool, as written) | CHECK after | Entries with the committed tool | CHECK with the committed tool |
|---|---|---|---|---|---|---|
| Paper A (springer, `--no-ids`) | 57 | 18 | 68 | 20 | 61 | 16 |
| Paper B (`--no-ids`) | 127 | 28 | 128 | 19 | 127 | 18 |

"Before" is a run of the committed tool at the start of this job (B145 reported 128 and 29 for B; the difference is Buzby and Mottet, which the tool no longer lists). Paper A rose by 11: ABS (2021), ABS (n.d.a to n.d.d), ABARES (2023), FAO (n.d.a, n.d.b), DCCEEW (2025), DCCEEW (2026), UN (2015); NHMRC was already listed. ABARES (2026a) stays out ("uncited in A"). Paper B rose by one (the companion paper).

Confirmations asked for:

* Paper A: ABARES 2026a is not listed; ABARES (2026), Higgins et al. (2018) and Summerhayes and Baker (2026) print as plain years (with the patched tool; the committed tool keeps the "b").
* Paper B: Buzby and Mottet are not listed; Nix and Migration Committee are not listed (uncited, B149b recast the prose); the companion paper is listed as "Lane, M., in preparation. Australia's carrying capacity 2011 to 2025 by region on the corrected releases. Manuscript." (patched tool only); Schon and Bohringer (Sustainability 15 (11), 8675, 2023) prints correctly with its diacritics and DOI.
* No em dash in either list. No person's name occurs in any printed CHECK text (two printed notes that named a cited work's author or a committee chair, L004 and L001, were reworded; "Murray fetches" is gone from L247, L248, L252 in the literature register as well).

### New data-source entries (Paper A), all type `dataset` unless stated

Series name, year, URL and access date come from `qa/sources_register.csv` (ids in the notes of each row). Where the sources register has no release year the year is "n.d." with the letter the paper uses. The letters come out as the paper prints them only because the entry titles sort in the right order (ABS_ANNUAL_ERP_..., Agricultural Commodities, Australian Agriculture, Historic; FAOSTAT Food balances before FAOSTAT Production).

| Id | Entry | Filled | Left for the author |
|---|---|---|---|
| L260 | ABS (n.d.a) ERP by SA2 (flow ABS_ANNUAL_ERP_ASGS2021) | name, URL (data.api.abs.gov.au) | release label; date accessed (D31: file dated 2026-10-27 only) |
| L261 | ABS (n.d.b) Agricultural Commodities NRM cubes | name, URL, accessed 2026-10-26 (D01, D13, D48) | none (the cubes span several releases, so n.d.) |
| L262 | ABS (n.d.c) Australian Agriculture series and Livestock Products | name, URL | date accessed (D29, D30 date only the findings) |
| L263 | ABS (n.d.d) Historic Agricultural Commodities 1860 to 2022 | name | URL; date accessed (D41: unknown) |
| L264 | ABS (2021) ASGS Edition 3 digital boundary files | name, URL, accessed 2026-11-13 (the V30b check download) | the pipeline copy's own retrieval date is unknown |
| L265 | ABARES (2023) Catchment Scale Land Use, update December 2023 | name, year, publisher | URL; date accessed (D32 gives no address) |
| L266 | FAO (n.d.a) FAOSTAT Food balances (2010 onwards and the Oceania series) | name, URL (D17) | date accessed |
| L267 | FAO (n.d.b) FAOSTAT Production: crops and livestock products | name, URL, accessed 2026-11-13 (V30a served the file) | none |
| L268 | DCCEEW (2026) Australian Petroleum Statistics, extract August 2026 | name, year, URL (D35) | publisher (department assumed; D35 names only data.gov.au); date accessed |
| L269 | DCCEEW (2025) Australian Energy Statistics 2025, Table F | name, year, URL (A18) | publisher (department assumed); date accessed |
| L270 | UN (2015) Sustainable Development Goal Target 12.3 (type web) | name and year from the paper's own citation | everything else: title, issuer, URL, date accessed (not in the sources register) |

NHMRC (2006) is L252, already in the list; see below. The register rows L260 to L270 are added to `qa/literature_register.csv` (kind "data source (reference entry)", ids of the sources register in the notes).

### The 26 fillable [CHECK] fields of Paper B (B145 table), worked from the files on disk

Filled (10 of the 26 rows, no CHECK left on them):

| Id | Entry | Field | Filled with | Basis on disk |
|---|---|---|---|---|
| L051 | ABS 1994 | place | Canberra | last page: Information Services, ABS, PO Box 10, Belconnen ACT 2616; produced by the Australian Government Publishing Service |
| L228 | Centre for Population 2026 | place | Canberra | imprint page: The Treasury, Langton Crescent, Parkes ACT 2600 |
| L227 | Treasury 2021 | place | Canberra | same imprint address |
| L226 | Treasury 2023 | place | Canberra | same imprint address |
| L010 | CSIRO and University of Queensland 2025 | place | Australia | the cover citation prints "CSIRO, Australia"; no city is printed |
| L062 | USDA 1992 | place | Washington, DC | address line on the front matter ("Washington, DC 20005-4788, June 1992") |
| L134 | Wackernagel 1994 | place | Vancouver | signed approval page: The University of British Columbia, Vancouver, Canada |
| L252 | NHMRC 2006 | year, version, table numbers (and "not seen") | 2006; version 1.2, updated September 2017; Tables 3 and 4 | the PDF is on disk (it is also sources register A27, read in V30b); title page, imprint (ISBN online 1864962437, suggested citation "Canberra: NHMRC; 2006"), Table 3 (PAL 1.2 to 2.2, note b) and Table 4 (macronutrients) read. Authors now "National Health and Medical Research Council [NHMRC]" so that Paper A's in-text "NHMRC" finds it |
| L253 | ABS 2011 (Livestock Products, December 2010) | confirm the meat calibration | confirmed | the four quarters to June 2010 in this issue give beef plus veal 2,108,776 t and mutton plus lamb 574,311 t; the archive's 2010 figures (2,290,969 and 663,519 t) over these are 1.0864 and 1.1553, the calibration 1.086 and 1.155 (the code reads the monthly workbooks 7215009 to 7215012, which agree with this issue's totals to 0.04%) |
| L242 | DCCEEW n.d. | year | n.d. | the saved page prints only "Last updated: 19 December 2025", a revision date; both papers cite it as n.d., so the in-text form stands |

Place fills for L051, L228, L227, L226, L010 and L062 rest on the issuer's printed address, not on a line headed "place of publication"; each note says so. Decision row for the author: confirm them, or give the imprint.

Left (16 rows), with what was looked at:

| Id | Entry | Still needed | Looked at on disk |
|---|---|---|---|
| L230 | DCCEEW 2017 | place | front matter prints "Commonwealth of Australia" and no city |
| L250 | FIAL 2021 | place | the cover address (Manly NSW) is the consultant's, not the publisher's |
| L020 | Lane 2014 | place | title page prints the university and February 2014, no city |
| L067 | AUSNUT 2007 | URL, access date, version | the workbook (sheet "Ausnut07-full", 6,356 rows) names no issuer, version or address |
| L143 | Chisholm 2000 | volume; surname spelling | page image opened: "Anthony Chisolm", "BHERT News, 2000", no volume or issue exists; the CHECK on volume is the tool's, the spelling CHECK stays |
| L231 | DCCEEW 2019 | publisher, place, Arcadis as author | executive summary names project partners only |
| L041 | Fairlie 2008 | volume, pages, DOI | the file is the chapter version ("first published in The Land 4, in 2008") |
| L060 | Geoscience Australia and ABARE 2010 | publisher, place | no title page; file metadata names Geoscience Australia and April 2010 |
| L002 | Gifford et al. 1975 | DOI | second-hand; no file |
| L034 | Gutteridge 2005 | publisher, place | prints the commissioning body (Dept. of Natural Resources and Mines) only |
| L248 | Jansen 1999 | not seen | no file |
| L247 | Saltelli et al. 2010 | not seen | no file |
| L050 | Wackernagel and Rees 1996 | place, edition, year | title page and first chapter page of the 50-page scan opened: no imprint |
| L001 | Taylor 1922 | end page, initials | second-hand (committee report footnote) |
| L005 | National Population Council 1992 | the report itself | second-hand |
| L004 | National Population Inquiry 1975 | identity of the work cited under the chair's name | second-hand |

Also left in the Paper B list, outside the 26: the companion paper (L259: publisher and place, to update at submission) and the two fallback entries Douglas Shire and Noosa (L039, L038: year, title, issuer). Paper A's own CHECK entries outside the 26 (ABARE 2010 author form, AUS-MEAT place, Davies, Hughes, Sysak editors and place, DCCEEW 2017, 2019 and Lane 2014 place, Geoscience Australia, Gifford, Jansen, Saltelli) were not part of this job and are unchanged apart from the closures above.

Decision rows for the author: (a) Paper A section 2 prints "(FAO n.d.)" (`A_s01-04.md` line 35) while the list entry and the supplement say FAO (n.d.a); the paper line needs the "a". (b) NHMRC is "NHMRC" in Paper A's text and "National Health and Medical Research Council" in Paper B's; the list carries both as "National Health and Medical Research Council [NHMRC]". (c) DCCEEW (n.d.) could be DCCEEW (2025) if the author prefers the page's revision date; it would then need the letter a/b with the Energy Statistics entry and a text change in both papers. (d) B_s10_declarations.md still reads "the verified registers" (B149b left it; see section 3).

## 2. Claims register: 917 data rows become 924 (7 added, 30 changed)

Tier rule as B122: no Tier A `value` or `statement` was changed (checked by comparing every changed Tier A row with its old text: ten rows, all identical); Tier A rows pending gate 6 stay pending; only notes were added to them, with one status addition on A312 (statement wording pending gate 6).

### Rows changed

| Id | Tier | What changed |
|---|---|---|
| A011, A014, A017 | A | note only (abstract fuel sentence; highlight 3 range; 2011 land reference wording) |
| A430, A431, A462 | A | note only; pending gate 6 kept (paired-draw basis wording; both diet-window values printed once) |
| A312 | A | note with the proposed statement ("moves by one region at most ... by four"); status adds "statement wording pending gate 6 (B152, from B149a)"; statement and value untouched |
| B153 | A | note: the paper's printed wording in 5.10 and the Figure 2 caption; the proposed statement stands; pending gate 6 kept |
| B167, B188 | A | note only; pending gate 6 kept (the 2.19 and 1.03 comparison wording) |
| A152, A153, A404, A407, A438, A446, A066, A304, A306, A346 | B | note only (where the abstract, 7.1, 8.1, 9.2, 12 and the conclusions now use them) |
| A441 | B | statement and value gain the range "27.4 to 29.1 million" across the leave-one-out variants; status unchanged (one route only); old statement and value recorded in the note |
| B247, B410 | B | cause clause replaced as the paper prints it: "pooling step" for "pooling rule"; "not shown to be a sufficient cause" out; "closes the gap only if ... equal energy or equal energy and protein" becomes "reaches HALF when ... equal energy (81.7), equal energy and protein (85.4; 92.4 if dairy may rise), or a lower meat share (107.7)"; B410's value gains 81.70; 85.4; 92.4; 107.69; status "independently verified (B146b, V40 and V53, 2026-11-18) for the figures; clause wording self-checked (B149b, 2026-11-19)"; old text in the notes. B410's last clause (diet the largest single feature) is not printed in the paper and is unchanged and still flagged |
| B433 | B | statement: "Table 5 column (e)" becomes the column heading "Line (b): Australia's own productivity" (the Table 5 heading rows: the letters (a) to (e) are gone from the paper; B433 is the only row that quoted one) |
| B352, B354, B411, B437, B238, B364 | B | note only (the three conditions of the pairing sentence; the Figure 1 placement; the two drought comparisons) |

### Rows added (Tier B, series continued)

| Id | Statement in short | Status |
|---|---|---|
| A480 | weather setting alone closes the long-term shortfall (34.3 against 27.6 million); low fuel raises capacity (3.7 against 15.6) | self-checked (B149a; csv cells re-read here) |
| A481 | Table S17: 19 choices, 7 shared, 12 2025-only (11 vary, 1 fixed), 18 of 19 vary (B149a's correction of V57a's "7 + 6 + 1") | self-checked; the seven checked by V48 |
| A482 | region counts move by 1 (short term 15, 16, 15) and 4 (long term 36, 32, 36) | self-checked (arithmetic on A304 and A306) |
| A483 | Supplementary Figure S1: 53 regions, 650,000 km2 cap, 0.757 and 0.694, 1,100 by 1,021 pixels at 170 dpi | self-checked (csv cells and png header re-read here) |
| B439 | Figure 2 overplot: 14 distinct readings of 19 on each of lines (a) and (b) | self-checked (counted from the csv here) |
| B440 | the model is placed at purpose 1 in Figure 1; by the caption's rule it would sit at purpose 2 or 3 | self-checked (B238 to B241 re-read) |
| B441 | the three versions: 49.4, 41.5, 53.6 million (Table 4, section 1) | self-checked (three cells of model_entry.csv re-read) |

### Claims-csv rows flagged B149a or B149b with no register id: where each now sits

Every row carrying a number is covered by a register row; a row with no number needs none.

* Paper A abstract: paired draws (165) A430, A431, A481; fuel (166) A480; 37% (167) A407; 39.1 and 39.7 (168) A462; partition (169) A346; seven shared (170) and section 2 pointer (171) A481; data-source citations (172) the entries L260 to L270 and L252; 1-in-10 range in highlight 3 (A014, A404); highlight 5 A480.
* Paper A body: 0.19 million (section 4) A446; 2011 SA2 40% (5.1) A017; 7.1 A480; 8.1 two methods A438 and A441 (no new row: the figures were already there); 9.1 A430, A431, A481; 9.2 counts A482; section 11 A480; five zones (12) A066 (the same five, re-read from the csv); conclusions A462, A482, A407.
* Paper A supplement: Figure S1 A483; Table S17 A481; S4 two methods A438 and A441. No register change for: Table 3 row order, the Figure 4 caption rule (no number), "clean and inside the range on 13 choices" (wording), S11 and S8 wording, declarations.
* Paper B: abstract pooling and pairing (85, 86), 7.6, 9.1, 5.14 and highlight 4 rows: B247, B410 with B352, B354, B411, B437; versions sentence (89) B441; Figure 1 caption B440; Figure 2 overplot B439; drought comparison (6.10, 9.2) B364 and B188 (no new row: B364 already states both comparisons); Table 5 headings B433; Supplementary S3 variant sentence B354 and B411. No register change for: Table 2 register ids (they are literature ids), the definitions of pairing and pooling, "the authors were not consulted", the DOI placeholder, the release-code key, "(requirement and waste cannot be separated)".

## 3. `papers/DECLARATIONS.md`

Two edits, matching `A_s13_declarations.md`:

1. Section 1 (the short AI declaration): "draft text from my outline and the verified registers" becomes "draft text from my outline and the checked results".
2. Section 3 (Paper A variant of the competing-interests text): "every figure carries its own register row and independent check" becomes "every number and figure was checked by an independent re-derivation".

"To check every number and citation by independent re-derivation" was already in section 1. Open: section 1 is also the text Paper B uses, and `B_methods/draft/B_s10_declarations.md` still says "the verified registers" (B149b made no change there). The master now matches Paper A's file only; the author decides whether Paper B takes the same wording.

## 4. Register rows touched

Changed (30): A011, A014, A017, A066, A152, A153, A304, A306, A312, A346, A404, A407, A430, A431, A438, A441, A446, A462, B153, B167, B188, B238, B247, B352, B354, B364, B410, B411, B433, B437. Added (7): A480 to A483, B439 to B441. References: 10 rows changed in `qa/references.csv` for the fills above plus notes on L020, L034, L041, L050, L060, L067, L143, L231, L250, L001, L004 (record of what was opened; two CHECK texts reworded); 11 added (L260 to L270). Literature register: L260 to L270 added; L252 (local path, read status, notes), L247 and L248 (wording) changed.

## 5. Wrong-value check

Example of what was NOT done: **A312** (Tier A, independently verified; its statement is "The short-term count of over-capacity regions is robust to the method tier (15, 16, 15) but the long-term count is not (36, 32, 36): six regions ... change status ..."). Applied outright, the paper's new wording would have replaced that gate-approved statement with "moves by one region at most between the published, corrected and improved methods (15, 16, 15) and the long-term count by four (36, 32, 36)", a statement the author has not approved, and the register would then say something no gate saw. The row keeps its old `statement` and `value`; the proposed text sits in the note and the status reads "statement wording pending gate 6 (B152, from B149a)". The same check on figures I computed: 27,438,890 / 27,608,200 = 0.9939, so "0.6% below" holds (a planted "1.0% below" fails); 2,290,969 / 2,108,776 = 1.0864 and 663,519 / 574,311 = 1.1553 reproduce the calibration 1.086 and 1.155 (a planted 1.09 does not match at three decimals); 34,274,878 > 27,608,200 and 3,705,376 < 15,623,209 give the A480 reading, and swapping the two comparisons (the pre-fix sentence) fails on fuel; 19 - 4 - 1 = 14 matches the distinct-value count of both Figure 2 lines.
