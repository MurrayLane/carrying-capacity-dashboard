# B53: PMSEIC and Grundy readings merged

- `qa/literature_register.csv`: L136 and L135 updated as B52 proposes (both `read`, status `self-checked (B52 full text)`, local_path and sha256 filled). L136 `what_taken` is the report's own words, "we produce enough food today to feed 60 million people" (p. 1), no source, no definition, exports in by implication only.
- `qa/claims_register.csv`: B230 statement now lists the export-inclusive counts as "61, 75, 100 and 60 (PMSEIC 2010, stated without source)"; status `self-checked (B53)`.
- `analysis/method_tests_2025/published_values.csv`: one new row (table `ladder`, PMSEIC 2010, 60.0 million people). No ladder.csv step, per B52.
- `analysis/method_tests_2025/README.md`: regenerated with `make_readme_tables.py --write`; only the per-table commit stamps changed, no table content. The sentence listing 61, 75, 100 is not in this README (it is in `analysis/comparators_2025/README.md` line 98, outside this brief's edit list), so it was not changed.
- `numbers_lint.py` last line: `report: qa/reports/numbers_lint_2026-11-07.csv (3700 rows)`.
