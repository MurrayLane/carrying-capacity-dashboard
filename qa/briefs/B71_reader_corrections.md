# Builder brief B71: corrections from the blind check V27

Read `qa/reports/V27_blind_check_readings.md`. Rules: plain language; no time words; no em dashes. No git; no subagents; no network. Write only `qa/literature_register.csv`, `qa/defects.csv` and `qa/reports/B71_reader_corrections.md`.

Register fixes, exactly as V27 found them, checking each against the paper on disk before writing (`/home/user/carrying-capacity-models/Literature review/` plus the row's `local_path` without its first path segment; `pdftotext`):
- L156 (Mayberry 2019): the cattle line must say all pathways except High Value Beef reach 25 million and High Value Beef cuts the herd to 20 million (pp. 14-15).
- L153 (Hochman 2017): the 4,405 kg/ha intercept is cited to p. 2074 (Fig. 3 caption p. 2076); the CO2 range 354.4 to 400.8 ppm to p. 2074.
- L183 (Mcdougall 2020): Table 2 has 14 entries, 13 cities plus one worldwide study; the 1680 hours figure is on p. 8; fix the other page slips V27 names.
- L148: say only the 500 surveys were in Brisbane; the policies and interviews span the three states.
- L161: the "significant reduction by 2030" is tied in the chapter to the UN Sustainable Development Goal (p. 228), not stated as the Strategy's own aim.
- L200: the quote V27 places is in the abstract on p. 1582.
For each row append to `notes`: "; B71 (2026-11-11): corrected after V27: <what>". Change nothing else. Check before saving: 225 rows, 12 columns each, parses with Python's csv module, no em dashes introduced, line endings unchanged.

Defects: append one row to `qa/defects.csv` (next id after the last; columns id,date,layer,kind,what,found_by,fixed_in,notes): the V27 pattern that full readers (B67a, B67b) cite a figure to the page of the related discussion rather than the page where it is printed, and that two readers stated a count that missed an exception the paper spells out; found_by V27; fixed_in B71 for the sampled rows; notes: unsampled B67 rows (L152, L155, L159, L180, L186, L190, L192, L218) keep their page citations unverified at page level and the drafter must cite from the paper, not the register.

Report `qa/reports/B71_reader_corrections.md`: a table of the six rows (what changed, page checked), the defect id added, the register rows touched, and "Wrong-value check:" with one deliberate example of a correction that would itself be wrong, marked as an example.
