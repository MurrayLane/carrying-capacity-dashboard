# Builder brief B64: merge the B62 reading into the literature register

Edit only `qa/literature_register.csv` (keep line endings and all 12 columns) and append to `qa/reports/B64_merge.md`. No git; no subagents; plain language. Source: `qa/reports/B62_classics_reading.md` (per-row updates, corrections and five proposed new rows).

1. Rows L040, L041, L044, L045, L046, L047, L048, L049: `read_or_reported` "read", `what_taken` as the report gives, `local_path` and sha256, status `self-checked (B62 full text)`; apply the corrections (L044 Hardin argues for the concept, not a critic; L047 Meyer and Ausubel extend it; L049 delete the out-of-order note; L040 quote the results figures 2.04 to 6.08 million; L041 note that the file is an undated later chapter version without its tables and that the 2007-8 article in The Land is still to be obtained).
2. Add the five new rows (Rees 1992, Rees 1996, Hopfenberg 2003, Gilland 2006 with DOI 10.1007/s11111-007-0034-9 and the note that the file is misnamed Gillard2007.pdf, Chisholm 2000) with the fields and sha256 the report gives, status `self-checked (B62 full text)`.
3. L050 note: neither Rees 1992 nor Rees 1996 states an equivalence factor; Rees 1996 uses world-average productivities (p. 207). L002 note: Chisholm 2000 (new row) gives a second-hand route to the CSIRO 1975 figures (60 million on protein, 82 on energy, 140 on water); still second-hand.
Report: rows changed with old and new `what_taken`, rows added, the final row count.
