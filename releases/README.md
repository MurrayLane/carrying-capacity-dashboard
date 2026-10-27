# Releases

A release is a fixed combination of **zones**, **data** and **method**. Everything the site shows belongs to one release,
and a saved link names it (`#r=2011-corrected&z=15&p=long`), so an old link or a citation always reproduces what it showed.

| Release | What it is | Acceptance test |
|---|---|---|
| `2011` | The final model: the October 2012 timber update, as found in the QUT repository snapshot, known errors included. The log of updates records that update as not yet online when made (`analysis/model_archive/VERSIONS.md`) | The original servlet's output for all 120 default cases (`baseline/baseline_2011.json`) |
| `2011-thesis` | The June 2012 model and defaults behind the thesis results (Table 16) | The capacities in the thesis results workbook (`baseline/thesis_totals_capacity.csv`), all 120 |
| `2011-corrected` (default) | The 2011 data and method with only the long-term textiles default corrected (12.5 kg to the workbook's 11.5) | Differs from `2011` in nothing else (tested); its 120 results are locked in `baseline/release_2011-corrected.csv` |
| `2025-land` | Layer 1 of the 2025 refresh (status `current`, not locked): land only, by the 2011 method on 2020-21 ABS holdings and the 2023 land-use raster, on the 2011 zones | Differs from `2011-corrected` in land and the reserve share only (tested) |
| `2025-population` | Layer 2: adds 2025 population (infrastructure follows at 730 m2 a person) | Differs from `2025-land` in population, infrastructure and the remainder only (tested) |
| `2025-yields` | Layer 3: adds crop yields from the ABS data of 2022-23 to 2024-25 and the group trend for crops the ABS no longer reports; animal products are still the 2011 values | Differs from `2025-population` in yields only (tested) |

## Rules

1. **A published release is never edited.** Its `release.json` records the SHA-256 of every input file (`inputs`). The build refuses
   to run, and `npm test` fails, if any of those files changes. A correction or a refresh is a new release.
2. **A release says what it changes.** `extends` names the release it builds on; `patches` change defaults (with a reason), `yieldOverrides`
   replace rows of the regional yield block, `yieldMatrix` replaces the whole block (one CSV, a column per Yield sheet row), `model.cellOverrides` change workbook cells. `errata` lists known issues that the release does
   not fix. Descriptions and errata are text and may be clarified; inputs may not.
3. **Corrections go forward.** Errors found in a frozen release are listed in its `errata` and fixed in a later release.
4. **One change per release** where the effect needs to be separated: corrections, each data layer, each method change. The
   Since 2011 page reports the effect of each step (SCOPE.md D7).
5. **Legacy links.** A link with no `r` was made before releases existed, against the 2011 data, and opens `2011`. An empty address opens the default.

## Adding a release

```bash
mkdir releases/2026-data && cp releases/2011-corrected/release.json releases/2026-data/   # edit id, label, status, extends, inputs
# put its data files under data/<id>/, name them in release.json
cd web && node scripts/lock-release.mjs 2026-data        # records the input hashes; refuses to change hashes already recorded
node scripts/make-release-baseline.mjs                   # (adapt the id) locks the new release's 120 results
# add the id to releases/index.json, and a test in web/test/releases.test.js
```

While a release is still being built, give it `"status": "current"`: it is not hash-checked. Change it to `"frozen"` and lock it when it is published.

## Citing

Each frozen release can be archived with its own DOI (Zenodo accepts the CC BY data and results). Create a GitHub release from the
repository at the commit that froze it; the DOI then cites exactly that version.
