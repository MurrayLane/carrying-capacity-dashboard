# B71 reader corrections after V27

Brief: `qa/briefs/B71_reader_corrections.md`. Source of the corrections: `qa/reports/V27_blind_check_readings.md`. Each correction was checked against the paper on disk with `pdftotext` before writing. Files written: `qa/literature_register.csv`, `qa/defects.csv`, this report.

| Row | What changed | Page checked |
|-----|--------------|--------------|
| L156 Mayberry 2019 | The cattle line now says five of the six pathways take the herd to 25 million (23.6 million in the adjusted Feedlot Futures pathway) and High Value Beef cuts it to 20 million; the 25 million figure entry says the same | p. 14 ("with the exception of the High Value Beef pathway ... 25 million") and p. 15 ("reduce the total national beef herd to 20 million") |
| L153 Hochman 2017 | The 4,405 kg/ha intercept is cited to p. 2074 (Fig. 3 caption p. 2076); the CO2 range 354.4 to 400.8 ppm to p. 2074 | p. 2074 (regression and CO2 range), p. 2076 (caption) |
| L183 Mcdougall 2020 | Notes no longer say 15 city studies; Table 2 has 14 entries, 13 cities plus one worldwide study. The 1680 hours figure is cited to p. 8. The 250/160/118% values are cited to Table 4 on p. 8 and the text on p. 9 | Table 2 on pp. 3-4; p. 8 (1680 h, Table 4); p. 9 (text values) |
| L148 Summerhayes and Baker 2026 | Only the 500 surveys were in Brisbane; the policies and interviews span the three states | p. 963 |
| L161 Mirosa 2020 | The "significant reduction by 2030" is tied to the UN Sustainable Development Goal, not stated as the Strategy's own aim | p. 228 |
| L200 Haddaway 2020 | The quoted "major pitfalls in the conduct and reporting of systematic reviews" is placed in the abstract on p. 1582 | p. 1582 |

Each row has a note appended to `notes` in the form "; B71 (2026-11-11): corrected after V27: ...". The wording fixes were made in the line that held the error (`what_taken` for L156, L153, L148 and the L183 page slips; `notes` for L183's count, L161 and L200). Nothing else was changed.

Checks before saving: 225 data rows plus the header, 12 columns each, parses with Python's csv module, no em dashes, line endings unchanged (CRLF throughout).

Defect id added: X104 in `qa/defects.csv`. It records the pattern that full readers cite a figure to the page of the related discussion rather than the page where it is printed, and that two readers stated a count that missed an exception the paper spells out. Unsampled B67 rows (L152, L155, L159, L180, L186, L190, L192, L218) keep their page citations unverified at page level; the drafter must cite from the paper, not the register.

Register rows touched: L156, L153, L183, L148, L161, L200.

Wrong-value check: EXAMPLE ONLY, not written to the register: "High Value Beef cuts the herd to 25 million (pp. 14-15)." This would be wrong, because p. 15 gives 20 million for that pathway; 25 million is the level of the other pathways.
