# Builder brief

You are a builder helper. The coordinator (the main session) wrote this brief and will review your work, so do not try to decide what anything means.

Rules, no exceptions:
* Write only the file(s) named under "Write". Read anything else, change nothing else. Do not run git; the coordinator commits.
* Do not change any result, script or data file. Do not spawn subagents.
* Never invent. If you cannot establish a field, write `unknown` and list it in your report. Copy citations and titles exactly as you find them and record where you found them.
* Every row must rest on something you opened (a file, a page). A path in a row means the file exists: check it.
* Plain, specific notes. No time words (tonight, later, for now, not urgent).
* Repository root: /home/user/carrying-capacity-dashboard (public). The private archive is /home/user/carrying-capacity-models; refer to its files as `carrying-capacity-models/<path>`. Both exist on this machine.

Standing decisions you must not reopen: two papers only; the methods paper tests each method on Australian 2025 data and gives no reproduction gate; corrected values are assumed; the results paper gives 2011 as corrected only. Read `qa/CARD.md` and `qa/README.md` (the schemas) first.

Report format (your final message): (1) what you wrote and the row count; (2) every field or row you could not establish; (3) anything surprising or that looks wrong in the project's own documents; (4) rows a human should check first.

## Task B01: the data and archive sources register

Write: `qa/sources_register.csv` (header exactly as in `qa/README.md`; status `unverified` on every row).

Include one row for each of these, and for any data source you find the analyses use that is not listed:
1. Every input listed in `analysis/SOURCES.md` (reuse its checksums; recompute with `sha256sum` and flag any mismatch).
2. The FAOSTAT extracts in `analysis/method_tests_2025/`: `fbs_au_world_2021_23.csv`, `half_fbs_countries.csv`, `half_qcl_world.csv`, `half_landuse.csv`, `fao_world_land_production.csv`, `fao_au_production_1997_2023.csv`, `fao_qcl_countries.csv`. For each: the FAOSTAT bulk file it was cut from (names and URLs are in the header comment of `extract_fbs.py`, `extract_fao_world.py`, `extract_fao_half.py`, `extract_fao_countries.py`), the years and areas kept, and the sha256 of the extract. The raw bulk files are not stored; say so.
3. Archive items used as data or comparators, in `carrying-capacity-models/Comparators/` (ABS 4306.0 1991-92, ABS 7503.0 1990-91, the OWID HALF csv, Henry and Godden) and `carrying-capacity-models/Yield data/Abare commodities 2010 historic.pdf`; sha256 each.
4. The model workbook `model/model.xls` and the releases (`results/releases.json` has their hashes): one row for the workbook and one for the release chain.
5. The data folders under `data/` (read each folder's README or script header to say what the source is, its date and licence if stated).
6. `results/` generated files are NOT sources; skip them.

`read_or_reported`: `read` if the file in the register is the primary source, `reported` if it is a secondary summary (for example the OWID table of Alexander's index), `not reached` if the primary was not opened. `what_taken` is one line (which tables, which years, which columns). `used_by` names the scripts or sections that use it.
