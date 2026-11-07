# qa/: the verification state of the project

Built from `QUALITY_PLAN.md` and `ORCHESTRATOR_SCOPE.md`; the decisions Murray took on 2026-11-07 are in `DECISIONS.md` (all seven recommendations approved). The one-page `CARD.md` holds the standing decisions and never-do rules and is re-read after every compaction.

| File | What it holds |
|---|---|
| `CARD.md` | Standing decisions, never-do rules, and the standing-approval rule (how "yes" is read) |
| `DECISIONS.md` | Decisions and their status |
| `sources_register.csv` | Every dataset and archive item: where from, what was taken, checksum, status |
| `literature_register.csv` | Every cited or relied-on work: citation, where obtained, read or reported, where used, status |
| `claims_register.csv` | Every number and statement in the papers: script, output file, sources, dependencies, tier, status |
| `defects.csv` | Every defect a check caught |
| `spend.csv` | Per job: model, effort, tokens, notional cost, outcome |
| `briefs/` | Worker briefs (one file each); `reports/` worker reports |
| `tools/` | The automatic checks |

## Schemas

**sources_register.csv** (data and archive items) and **literature_register.csv** (cited works) share these columns: `id` (D01.. data, A01.. archive item, L01.. literature), `kind`, `title`, `origin` (URL or full citation), `dated_or_accessed`, `local_path`, `sha256` (local files), `what_taken`, `read_or_reported` (read / reported / not reached), `used_by` (papers and scripts), `status` (unverified / self-checked / independently verified / Murray-verified / withdrawn), `notes`.

**claims_register.csv:** `id` (B001.. methods paper, A001.. results paper), `paper`, `section`, `statement`, `value`, `unit`, `tier` (A headline: two independent routes; B supporting: one; C context), `script`, `release_or_data`, `output_file`, `output_locator` (column and row or key in the output file), `sources` (ids), `method_source` (id), `depends_on` (claim ids), `status`, `verifier_report`, `last_verified_commit`, `notes`.

**defects.csv:** `id`, `date`, `layer` (1 data, 2 method, 3 calculation, 4 interpretation, 5 literature, 6 reproduction, 7 uncertainty, 8 editorial), `kind`, `what`, `found_by`, `fixed_in`, `notes`.

**spend.csv:** `date`, `job`, `model`, `effort`, `tokens_in`, `tokens_out`, `notional_cost_usd`, `outcome`.

## Tools

**`tools/numbers_lint.py`** (B07, 2026-11-07). Run `python3 -I qa/tools/numbers_lint.py` from the repository root (about 10 seconds; `--docs`, `--trusted`, `--out`, `--stale` change the inputs). It scans the paper documents and READMEs for every typed number and reports, per number: `found` (anchored: the value is in an output csv that the same document names, or is specific enough to match at most three trusted values anywhere), `not found` (no named output file shows it: a figure quoted from another author, prose arithmetic, or a stale figure; a human sorts these), `ambiguous` (under 1, or under 10), `skipped` (years, dates, ids, citations, hashes), and `stale` (equal, at the same decimals, to a superseded value in the script's default list, unless anchored). The stale list holds the pre-dairy-module improved figures and the old nutrition bounds; add to it whenever a figure is superseded. A plain "is this number anywhere" test cannot fail (with half a million trusted values almost everything matches), so `found` is deliberately strict. Report of the first run: `reports/numbers_lint_2026-11-07.csv`; its five stale hits were all explained (a deliberate note of superseded values, two dated historical entries in `HANDOFF.md`, and one current value equal by coincidence).
