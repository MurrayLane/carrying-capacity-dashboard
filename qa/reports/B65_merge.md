# B65: recency sweep candidates registered

Source: qa/reports/B63_candidates.csv (88 rows) and qa/reports/B63_recency_sweep.md. Only qa/literature_register.csv was edited (appended, CRLF kept, 12 columns each).

* Ids added: L144 to L221 (78 rows, one per distinct work; 10 works served more than one point and list every point in used_by, with the priority per point where it differed).
* Read status: 16 read (open copy, not saved), 45 abstract only, 17 record only.
* Kind: 6 book chapters (Davies 2024; Routledge Handbook of Food Waste; Future Food Systems; New Directions in Productivity Measurement; Handbook of Drought and Water Scarcity; Carrying Capacity of China), 72 journal articles.
* Cites Lane noted on Bolleter 2018 (Lane 2017) and Zhang 2018 (Lane 2010). All rows status unverified, local_path and sha256 empty.
* Paper A entered as "results paper", Paper B as "methods paper" (from B61 headings). what_taken is the csv "why" for every row; for the read-in-full works that line is already the report summary.
* Some titles carry non-ASCII characters (curly quotes, en dashes) as on Crossref; the file is now UTF-8 rather than pure ASCII.

## Final row count

221 data rows (header plus 221 lines; was 143, +78).
