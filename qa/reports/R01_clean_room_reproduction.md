# R01 clean-room reproduction report

Commit cloned: d808d00acbf7d9f7216fbe3dcad6feb8c2c13d7b (fresh clone of the GitHub repository; nothing copied from the working checkout).
The working checkout is at 861f4f7, eight commits after d808d00 (it also has uncommitted changes in qa/reports and one more file), so it is not the same revision as the clone. The comparison against it is therefore noted separately below.

## Steps that ran (all exit code 0)
- `cd web && npm ci`: ran. `npm run results`: ran (about 9 minutes here).
- `npm test`: 32 tests, 32 pass, 0 fail, 0 skipped, 0 cancelled.
- analysis/method_tests_2025: henry_godden, simpson_food, half_index, cassidy_people_per_hectare, fearnside_failure_curve, foran_poldy_balance, cross_method, design_choices, then `make_readme_tables.py --write`.
- analysis/paper_a: regional_flips.py, shocks_by_region.mjs then shocks_summary.py, long_term_and_measures.mjs, method_effects_by_region.py, plot_method_effects.py, regions_in_depth.py, migration_map.py, `make_readme_tables.py --write`.
- analysis/comparators_2025/rerun.mjs: its README says it is re-run from the built data, so it was run (writes rerun.csv).
- analysis/scale_curve_2025/plot_scale_curve.py: plain, `--log`, `--local`.

## Reproduced identically (git status of the clone shows no change)
- Everything `npm run results` writes: all `results/<release>.csv`, `comparison_cells.csv`, `method_effects.csv`, `scenarios.csv`, `scale_curve.csv`, and the built data. The tracked release data is byte-identical to the commit.
- Every CSV and JSON the analyses write, in method_tests_2025 (all `*.csv` outputs, including cross_method.csv and design_choices.csv), paper_a (regional_flips, shocks_by_region, shocks_summary, long_term_levers, long_term_regions, measures, store_equivalence, transfers, method_effects_by_region, method_effects_summary, regions_in_depth.csv and regions_in_depth.md, scenarios_by_region, method_status) and comparators_2025/rerun.csv.
- Images by byte: method_effects_heatmap.png, migration_map.png, scale_curve.png, scale_curve_log.png, scale_curve_local.png are unchanged.
- No numeric difference anywhere in any CSV, JSON or Markdown table (largest numeric difference: 0).

## Files that differ from the committed copy (7), and why
| File | First differing line | Kind | Largest numeric difference |
|---|---|---|---|
| analysis/method_tests_2025/README.md | line 15, `<!-- source: henry_godden_summary.csv; commit: b3cc6c9 -->` becomes `commit: d808d00` (26 lines, all of this one kind, in the generated-table markers) | commit hash stamp written by make_readme_tables.py `--write` | none (no table cell changed; zero other changed lines) |
| analysis/paper_a/README.md | line 10, same stamp (16 lines, all of this kind) | commit hash stamp | none |
| analysis/scale_curve_2025/scale_curve.svg, scale_curve_log.svg, scale_curve_local.svg | line 9, `<dc:date>` timestamp | date plus matplotlib's random element ids (`m05a61d1480` and similar) | none; after masking the date and ids the files are identical to the commit |
| analysis/paper_a/method_effects_heatmap.svg | line 9, date; element ids | date and ids, plus the embedded base64 PNG line differs after the first 250 characters | none in numbers; the standalone .png is byte-identical, so the embedded copy differs only in encoding bytes |
| analysis/paper_a/migration_map.svg | line 9, date; element ids | same as above; 4 normalised lines differ, all the embedded base64 PNG | none |

Line endings and paths: no differences.

## Against the working checkout (861f4f7)
- Regenerated results, CSVs, JSON, PNGs: identical to the working checkout.
- The five SVGs: three scale-curve SVGs equal the working copies once date and ids are masked; the heatmap and migration map differ from the working copies only in the date, ids and embedded PNG encoding.
- The two READMEs differ from the working copies only in the commit-hash stamp (working copies carry b3cc6c9).
- Other differences are because the working checkout is ahead: HANDOFF.md, analysis/sensitivity_2025/README.md (Monte Carlo wording), papers/A_results/OUTLINE.md, papers/B_methods/OUTLINE.md, qa/claims_register.csv, qa/defects.csv, qa/spend.csv, qa/briefs (B33, V15), qa/reports/manuscript_audit_2026-11-07.*, qa/tools/manuscript_audit.py. None is an output of a rerun script. The working checkout also has `web/dist` and `__pycache__` folders that the clone does not.

## Not reproducible from the repository alone
- Monte Carlo (analysis/sensitivity_2025 variant runs and `monte_carlo_*` outputs): the variant folder is not in the repository. Needs that variant folder.
- FAOSTAT extract scripts in analysis/method_tests_2025 (extract_fbs.py, extract_fao_world.py, extract_fao_half.py, extract_fao_countries.py, extract_fao_au_production.py): need the FAOSTAT bulk files (food balance sheets, production and land use bulk downloads), which are not in the repository. Their extracted CSVs are committed, and the analysis scripts that read those extracts ran fine.
- The typed constants in simpson_food.py and foran_poldy_balance.py come from PDFs in the models archive (`Comparators/`), which are not in the repository; the scripts ran, but those source values could not be checked against the documents.

## What scripts needed that the repository does not provide
- Python 3.13 with matplotlib and numpy (the only third-party imports in the scripts that ran; already installed here). The repository has no requirements file for them.
- Node 22 (here v22.22.0); `npm ci` supplied the rest.
- rerun.mjs, shocks_by_region.mjs and long_term_and_measures.mjs need the built data in `web/public/data/` (created by `npm run results`, gitignored), so they must run after it.
- No environment variable and no data file was missing for any step that ran.
