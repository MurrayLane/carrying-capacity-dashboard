# qa/: the verification state of the project

Built from `QUALITY_PLAN.md` and `ORCHESTRATOR_SCOPE.md`; the decisions Murray took on 2026-11-07 are in `DECISIONS.md` (all seven recommendations approved). The one-page `CARD.md` holds the standing decisions and never-do rules and is re-read after every compaction.

| File | What it holds |
|---|---|
| `CARD.md` | Standing decisions, never-do rules, and the standing-approval rule (how "yes" is read) |
| `DECISIONS.md` | Decisions and their status |
| `sources_register.csv` | Every dataset and every cited work: where from, what was taken, read or reported, checksum, status |
| `claims_register.csv` | Every number and statement in the papers: script, output file, sources, dependencies, tier, status |
| `defects.csv` | Every defect a check caught |
| `spend.csv` | Per job: model, effort, tokens, notional cost, outcome |
| `briefs/` | Worker briefs (one file each); `reports/` worker reports |
| `tools/` | The automatic checks |

## Schemas

**sources_register.csv:** `id` (D01.. for data, L01.. for literature, A01.. for archive items), `kind`, `title`, `origin` (URL or full citation), `dated_or_accessed`, `local_path`, `sha256` (local files), `what_taken`, `read_or_reported` (read / reported / not reached), `used_by` (papers and scripts), `status` (unverified / self-checked / independently verified / Murray-verified / withdrawn), `notes`.

**claims_register.csv:** `id` (B001.. methods paper, A001.. results paper), `paper`, `section`, `statement`, `value`, `unit`, `tier` (A headline: two independent routes; B supporting: one; C context), `script`, `release_or_data`, `output_file`, `output_locator` (column and row or key in the output file), `sources` (ids), `method_source` (id), `depends_on` (claim ids), `status`, `verifier_report`, `last_verified_commit`, `notes`.

**defects.csv:** `id`, `date`, `layer` (1 data, 2 method, 3 calculation, 4 interpretation, 5 literature, 6 reproduction, 7 uncertainty, 8 editorial), `kind`, `what`, `found_by`, `fixed_in`, `notes`.

**spend.csv:** `date`, `job`, `model`, `effort`, `tokens_in`, `tokens_out`, `notional_cost_usd`, `outcome`.
