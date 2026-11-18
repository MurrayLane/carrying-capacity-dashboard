# B120 report: freeze 2011-fixed-3 and 2011-improved-3; gap-attribution threshold to 5%

## Files changed
- releases/2011-fixed-3/release.json (status frozen; 13 input hashes recorded)
- releases/2011-improved-3/release.json (status frozen; 20 input hashes recorded)
- releases/README.md (two rows added to the table of frozen releases, one line each on what they correct)
- results/releases.json (regenerated; only the two entries changed, status current to frozen)
- analysis/method_tests_2025/bases_fidelity.py (threshold 0.01 to 0.05, docstring and column name "under 5%")
- analysis/method_tests_2025/make_readme_tables.py (column name, comment and table heading "under 5%")
- analysis/method_tests_2025/gap_attribution_readable.csv (regenerated)
- analysis/method_tests_2025/README.md (Table S1 block regenerated with `--write --only gap_attribution`; no other block touched)
- qa/reports/B120_freeze_and_threshold.md (this report)

Claims register rows touched: none (never edited).

## 1. Freeze
Locked with `node scripts/lock-release.mjs <id>`. Recorded hashes (SHA-256):
- Both releases share: model/model.xls f14140154e55754713a7d5c60643f1abab8b5a8c8c9891b9a0e0cf85286ff5bd; data/2011/default-inputs-short-term.csv d71758c4ce193c60d21aa45a9e0318bb3608ea8998b31cf7fc3fced07a93b4f4; data/2011/default-inputs-long-term.csv 682cfd316e6ef6a2c34eefff5368f7b4145bb50fd18bd8b66e0ebb47f6d4010a; releases/2011-corrected/release.json a738f479e836ccb45562f51a311d2dc483041472b0121ba37b807fcdd459e61b; releases/2011/release.json 47f3f6422f97e10778c6392bca1e435f951ad26cb195cfe77399c6c210c78340; methods/zone-population-2011/method.json 0be3ade3cf694f648eff5cd514124bb761504dd70895b8f86b7ec6a99f8fb99e.
- 2011-fixed-3: own release.json daf7cc8aa0a027b4c4495f9c7cbeacdac44c864c907ada085235b847eeaa0c9d; 2011-fixed-2 91db320d...; 2011-fixed 74a97f1b...; plus methods state-population-sum, biodiesel-yield, beef-carcase-yield, north-east-vic-population (all in the file).
- 2011-improved-3: own release.json 00d35c373bc3a8262273874eaa9690780281d0b30395761b4757a70060cc16b1; 2011-improved-2 545ce4dc...; 2011-improved 09b78f74...; plus 9 method files and data/2025/dairy_farm_yield_by_zone.csv a11742de... (all in the file).

Test: `node --test web/test/releases.test.js`: 27 tests, 27 pass, 0 fail.
Results csvs: after `build:data` and `make-results.mjs 2011-fixed-3 2011-improved-3`, every results/*.csv is byte-identical to its copy from before (checked with cmp, no difference). results/releases.json differs from before in those two entries only.

## 2. Threshold 1% to 5%
`bases_fidelity.py` run (all four csvs rewritten; the other three, bases.csv, fidelity.csv, intake_variant.csv, are byte-identical by cmp). The only change in gap_attribution_readable.csv beside the renamed column and the ill-conditioned flag is the printed share.

Rows whose presentation changed from a share to people-or-points (64 rows, all now an absolute change; none of these has a people figure except where noted, and HALF Australia was already in this form at 0.8%):
- HALF, World 2011 (residual 2.2%): 13 rows (causes a, b1, b2, b3, b4, b5, a+b1, a+b5, b1-b4, a+b1-b4, a+b1-b5, c+, c-)
- HALF, United States 2011 (3.3%): the same 13 causes
- HALF, Argentina 2011 (4.6%): the same 13 causes
- Simpson pasture, Australia 1991-92 (2.3%): 13 rows (a1, a2, b-low, b-high, c1, c2, c3, d1, d2, e x3, f)
- Foran and Poldy, grain 1997-98 (1.2%): 7 rows (b x5, c1, c2, b+c1 counted as listed in the csv)
- Foran and Poldy, meat 1997-98 (1.2%): 5 rows (b x4, c3)
Unchanged: HALF India (7.2%), the Cassidy rows (22% to 37%), the Henry and Godden rows (within rounding). Rows with an empty printed share (Simpson a3, Foran and Poldy grain a) only changed the flag.

## Wrong-value check:
Example only, not a real value. If model/model.xls in 2011-fixed-3 were changed so its hash read f14140154e55754713a7d5c60643f1abab8b5a8c8c9891b9a0e0cf85286ff5be (last character altered from d to e), it would not match the recorded f14140154e55...ff5bd, and the build and `npm test` would refuse to run. No file was altered to test this.
