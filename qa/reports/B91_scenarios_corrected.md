# B91: Paper A scenarios and grain stores on the corrected release (decision 86)

Builder brief: `qa/briefs/B91_scenarios_corrected_release.md`. Read: `qa/reports/V32a_logic_A.md` (problem 6; section 8 point 6; section 11 point 6), `papers/A_results/SECTION_SCOPE.md` sections 8 and 11, `papers/A_results/DISCUSSION_MEASURES.md`, `analysis/paper_a/README.md`, `analysis/paper_a/long_term_and_measures.mjs`, `analysis/paper_a/measures.csv`, `results/README.md`, `releases/README.md`, `web/scripts/` (release resolution, locking, scenarios) and the release definitions under `releases/`, including `2025-store-1` and `2025-store-2`. The release of each figure was read from the scripts (which release each one loads), not from the register. The claims register was not edited.

## What was done

1. **Which release each figure was on.** `long_term_and_measures.mjs` computes every row of `measures.csv` (the measures, drought-proofing, waste, diet, livestock, cropland, fuel 156) and `transfers.csv` on `2025-fixed`, but `store_equivalence.csv` on `2025-improved`. The named scenarios (`results/scenarios.csv`, from `web/scripts/make-scenarios.mjs`, read by `shocks_summary.py` into `scenarios_by_region.csv`) are all on `2025-improved`, with the grain stores on `2025-store-1` and `2025-store-2` (both extend `2025-improved`). The drought return periods (`shocks_summary.csv`) are on `2025-fixed`. So the mixed pairs V32a found are: waste (+8.67% / -4.14% improved, against +16.4% / -8.2% corrected); drought-proofing +60% (corrected) beside a two-year store +64% (improved); A223's -0.3% (improved) against -26% (corrected).
2. **Rerun on `2025-fixed`, same definitions.** The grain store is a resilience table. `2025-fixed` and `2025-improved` share one resilience table (checked cell by cell; both scripts now refuse to run if that stops being true), and `2025-store-1` and `2025-store-2` differ from `2025-improved` in that table only (existing test). So the store on the corrected release is the store release's resilience table put on `2025-fixed`, labelled `2025-fixed (resilience table of 2025-store-1)` in every row. Every other named scenario keeps its settings and yield scales and runs on `2025-fixed` against the `2025-fixed` defaults.
   * `web/scripts/make-scenarios.mjs`: new option `--release <id>` writes `results/scenarios_<id>.csv`; without it the script writes `results/scenarios.csv` exactly as before (byte-identical, checked). Added to `npm run results`.
   * `analysis/paper_a/shocks_summary.py`: `scenarios_by_region.csv` now carries both files, with columns `reference_release` and `release` in each row; new flag `--scenarios-only` writes that file alone (used here, so `shocks_summary.csv` was not touched by this job). The improved rows are unchanged.
   * `analysis/paper_a/long_term_and_measures.mjs`: `measures.csv` has a first column `release`; the 19 existing rows are unchanged (all `2025-fixed`), and six rows were added: the one- and two-year stores on `2025-fixed`, and the improved reference with both stores on `2025-store-1` and `2025-store-2`. `store_equivalence.csv` keeps `capacity_long_improved` and adds `capacity_long_fixed`. New `store_years.csv` writes the interpolated drought equivalent of each store on each release (V32a: "A265 and A266 are interpolated with no output file"). New option `--only levers,regions,measures,store,transfers`; this job ran `--only measures,store`, so the 2011 rows of `long_term_levers.csv` and `long_term_regions.csv` were not rewritten (a full run was checked in a scratch folder: those two files and `transfers.csv` came out byte-identical).
   * `analysis/paper_a/make_readme_tables.py`: the named-scenarios table gives improved / corrected side by side; the measures table reads the `release` column and gives the stores on both releases; new option `--only` (this job wrote only `named_scenarios` and `measures`).
3. **Frozen.** `2025-store-1` and `2025-store-2` set to `"status": "frozen"` and locked with `web/scripts/lock-release.mjs` (26 input hashes each, as `releases/README.md` rule 1 describes). Their entries in `results/releases.json` now read `frozen` with the hashes of the rebuilt data. The model hashes did not change; the regions hashes did, because `regions.json` records the hash of `release.json` and the status is part of it. `releases/README.md` and `results/README.md` now name them.
4. **Docs.** `analysis/paper_a/README.md` and `papers/A_results/DISCUSSION_MEASURES.md` name the release of every figure and give both where they differ (table A of DISCUSSION_MEASURES has a new Release column).

Run: `cd web && node scripts/make-scenarios.mjs --release 2025-fixed`; `python3 -I analysis/paper_a/shocks_summary.py --scenarios-only`; `node analysis/paper_a/long_term_and_measures.mjs analysis/paper_a --only measures,store`; `python3 -I analysis/paper_a/make_readme_tables.py --write --only named_scenarios,measures`. `node --test test/releases.test.js`: 25 pass, 0 fail (run on the data as built; `npm test` was not run because it rebuilds every release and B90 was also rebuilding them).

## The scenarios, before and on the corrected release

Australia; change on the release's own reference. Corrected reference: 41.5 million short term, 15.6 long term, 16 and 32 regions over capacity. Improved reference: 53.6 and 18.5, 15 and 36.

| Scenario or measure | Release used before | Figure before | Figure on 2025-fixed | Change |
|---|---|---|---|---|
| Field-crop yields 12% lower, short / long | 2025-improved | -0.11% / -0.35% (36 regions) | -0.09% / -0.28% (34) | small |
| Field-crop yields 24% lower, short / long | 2025-improved | -0.26% / -5.34% (36) | -0.20% / -0.65% (34) | long term much smaller |
| A223 pair: 24% field-crop shock short term against the 1-in-10 drought | 2025-improved ; 2025-fixed | -0.3% against -26% | -0.2% against -26% | -0.3 to -0.2; both now one release |
| Waste at the national target (6%), short / long (named scenario) | 2025-improved | +8.67% / -4.14% (36) | +16.40% / -8.15% (36) | now equals the measures table |
| No avoidable waste, short / long | 2025-improved | +17.29% / 0% (36) | +33.21% / 0% (32) | short term doubles |
| Recycling none, short / long | 2025-improved | -0.11% / -0.23% (36) | 0% / -1.21% (35) | not the same measure (below) |
| Recycling half, short / long | 2025-improved | -0.06% / -0.12% (36) | +1.70% / -0.28% (33) | not the same measure (below) |
| Liquid fuel 156 litres, long (named scenario) | 2025-improved | +0.98% (35) | +0.78% (31) | small |
| Liquid fuel 340 litres (CSIRO), long | 2025-improved | -18.75% (37) | -1.83% (37; 5 tip) | much smaller |
| Grain store, one year, short / long | 2025-store-1 | 0% / +48.27%, 27.4 million (27 regions) | 0% / +48.45%, 23.2 million (25) | % unchanged; level and count change |
| Grain store, two years, short / long | 2025-store-2 | 0% / +64.21%, 30.4 million (25) | 0% / +64.47%, 25.7 million (25) | % unchanged; level changes |
| One-year store as years of drought | 2025-improved (store_equivalence) | about 16 (16.0) | about 16 (16.1) | none |
| Two-year store as years of drought | 2025-improved | about 10 (9.7 here; the register note says 9.6) | about 10 (9.8) | none |
| Regions taken out of over capacity by the stores, long | 2025-store-1 / -2 | 36 to 27 (nine) / 36 to 25 (eleven) | 32 to 25 (seven) / 32 to 25 (seven) | count changes |
| Drought-proofing, long | 2025-fixed | +59.7% (24.9) | +59.7% (24.9) | none, already corrected |
| Livestock output +10% / +20% | 2025-fixed | +9.7% / +19.4% short; +9.4% / +18.8% long | the same | none |
| Diet: meat and eggs 5% / 7.5%; red meat 30% | 2025-fixed | +85% / +26%; +16%; +56% / +19% | the same | none |
| Waste 6% / none (measures table) | 2025-fixed | +16.4% / +33.2% short; -8.2% / 0% long | the same | none |
| Field crops, horticulture, all yields, irrigation, recycling 1, cropland, fuel 156 (measures table) | 2025-fixed | as in `measures.csv` | the same | none |
| Best meat-and-egg share 2.5% (118.0 against 112.4 and 76.8, `diet_scale.csv`) | 2025-fixed | as stated | the same | none |
| Regions as a pool (1.60, 1.82, 2.60, 15.5, 9.6; 20.7 / 19.1; 21.5 / 10.8) | 2025-fixed (3.00 on 2011-fixed) | as stated | the same | none |
| Fuel lever 3.7 million; biofuel share 9.7 | 2025-fixed | as stated | the same | none |
| Herd cycle 43.5 to 55.4 million | 2025-organic (as built) | as stated | not rerun | ABS cubes needed; second route blocked (V31d) |

Readings:
* **The stores and drought-proofing are now on one release** and remain the two largest long-term measures (+60%, +64%, +48%). A grain store is still worth more than any other named scenario in the long term; the next largest on `2025-fixed` is waste at the national target (-8.15%), not fuel (-18.75% before).
* **The CSIRO fuel scenario changes the most**: -18.75% on improved, -1.83% on corrected. The settings are the same on both releases (long-term fuel 210 litres, biofuel share 1), so this is a method effect. It was not decomposed here and needs its own check before anything is written about it.
* **Recycling is not the same measure on the two releases.** On `2025-improved` the setting is the share achieved of the stage uptake pattern (`recycling-stage` module); on `2025-fixed` it is the thesis's own recycling setting, whose short-term default is 0. The corrected rows are computed and labelled, but they do not replace the improved rows as "the same scenario".
* `results/scenarios.csv` and the improved rows of `scenarios_by_region.csv` are unchanged, so every figure as first computed still has its release label.

## Frozen releases and hashes

| Release | Status | model.json SHA-256 | regions.json SHA-256 | release.json SHA-256 (without inputs) |
|---|---|---|---|---|
| 2025-store-1 | frozen (was current) | ac0e363a8cc57a4a54edcc0b972b03eb929b82868b1b714c19c1f427845a6525 | fc61f4b6972e7ab18731e15d8ba4c97cf390d5207e6c3912ed236655dd549c1f (was 8fcb2617...) | f681516738701e0931c52a4e784f20ef4c308a10b9f4b753b118a4e4d3c671eb |
| 2025-store-2 | frozen (was current) | a69b8fa6d919cd9576a89a868934214524ccc5fe17f3cbabaf0d6ba45709a5ab | 45b4482352ad9bb5c9b75be3b22271439c2c26501311bff260d11c4b2a394b4a (was 2ed5f7a8...) | 631e9ec1b2517258f2e82a422799f4006da415e46187d9475bdc175b4f7f946d |

`lockDrift` is empty for both, and the test "every frozen release still has the inputs it was locked with" passes. `results/2025-store-1.csv` and `results/2025-store-2.csv` came out byte-identical. In `results/releases.json` only these two entries were rewritten, because the full rewrite (`make-results.mjs`) stopped on B90's new `2011-fixed-2`, which had no built data. A full `make-results.mjs` run by B90 writes the same values for them.

## Files changed

* `web/scripts/make-scenarios.mjs` (option `--release`)
* `web/package.json` (`npm run results` also writes `scenarios_2025-fixed.csv`)
* `results/scenarios_2025-fixed.csv` (new)
* `results/releases.json` (the two store entries: status and regions hash)
* `results/README.md` (the new file; how releases are frozen)
* `releases/2025-store-1/release.json`, `releases/2025-store-2/release.json` (status frozen, `inputs` recorded)
* `releases/README.md` (a row for the store releases)
* `web/public/data/` (rebuilt by `npm run build:data`; only the two store `regions.json` and `releases.json` differ; B90 rebuilt the folder again afterwards with the same store hashes)
* `analysis/paper_a/long_term_and_measures.mjs` (release column, stores on both releases, `store_years.csv`, `--only`)
* `analysis/paper_a/measures.csv` (release column; six rows added)
* `analysis/paper_a/store_equivalence.csv` (column `capacity_long_fixed` added)
* `analysis/paper_a/store_years.csv` (new)
* `analysis/paper_a/shocks_summary.py` (both reference releases; `--scenarios-only`)
* `analysis/paper_a/scenarios_by_region.csv` (columns `reference_release`, `release`; 22 corrected rows added)
* `analysis/paper_a/make_readme_tables.py` (two tables; `--only`)
* `analysis/paper_a/README.md` (named-scenario and measures tables; section 8 and measures prose)
* `papers/A_results/DISCUSSION_MEASURES.md` (release of every figure; table A Release column; store and waste rows)
* `qa/reports/B91_scenarios_corrected.md` (this report)

Not touched: `qa/claims_register.csv`, 2011 data and releases, `regional_flips.py`, movers files, `shocks_summary.csv`, `long_term_levers.csv`, `long_term_regions.csv`, `transfers.csv`, `results/scenarios.csv`. B90 changed `regional_flips.csv`, `shocks_by_region.csv` and `shocks_summary.csv` alongside this job. B90's full `shocks_summary.py` run also rewrote `scenarios_by_region.csv` with this job's script, and the content is the same.

## Claim rows that change (not applied; B95 applies)

The change applies if the paper moves the named scenarios and stores to the corrected release, which is decision 86's intent. If the improved figures are kept, each row needs only the release named in its statement.

**Tier A (for Murray):**

| Id | Before | After (2025-fixed) |
|---|---|---|
| A205 | -0.26% (climate-crops-24 short, improved) | -0.20% |
| A206 | -5.34%, 36 regions (long, improved) | -0.65%, 34 regions |
| A219 | 0% (store-1 short; release 2025-store-1) | 0%; release `2025-fixed (resilience table of 2025-store-1)` |
| A220 | +48.27%, 27 regions | +48.45%, 25 regions |
| A223 | -0.3 (improved); -26 (corrected) | -0.2; -26, both 2025-fixed (the note "two numbers are on different releases" goes) |
| A264 | +48%; +64% (2025-store-1; 2025-store-2) | +48%; +64% (48.45, 64.47; 2025-fixed with the store tables); locator `results/scenarios_2025-fixed.csv` or `measures.csv` |
| A265 | 27.4 million, about 16 years (improved) | 23.2 million, about 16 years (16.1; `store_years.csv`) |
| A266 | 30.4 million, about 10 years (improved) | 25.7 million, about 10 years (9.8; `store_years.csv`) |

**Tier B and C:**

| Id | Tier | Before | After (2025-fixed) |
|---|---|---|---|
| A202 | B | 53.6; 18.5; 15; 36 | 41.5; 15.6; 16; 32 |
| A203 | B | -0.11% | -0.09% |
| A204 | B | -0.35%, 36 | -0.28%, 34 |
| A207 | B | +8.67% | +16.40% |
| A208 | B | -4.14%, 36 | -8.15%, 36 |
| A209 | B | +17.29% | +33.21% |
| A210 | B | 0%, 36 | 0%, 32 |
| A211 | B | -0.11% | 0% (not the same recycling measure) |
| A212 | B | -0.23%, 36 | -1.21%, 35 (not the same measure) |
| A213 | B | -0.06% | +1.70% (not the same measure) |
| A214 | B | -0.12%, 36 | -0.28%, 33 (not the same measure) |
| A215 | B | 0% | 0% (release label only) |
| A216 | B | +0.98%, 35 | +0.78%, 31 |
| A217 | B | 0% | 0% (release label only) |
| A218 | B | -18.75%, 37 | -1.83%, 37 |
| A221 | B | 0% | 0% (release label only) |
| A222 | B | +64.21%, 25 | +64.47%, 25 |
| A224 | B | 36 to 27; 36 to 25 | 32 to 25; 32 to 25 (seven regions each) |
| A225 | B | holds; locator "every other scenario under 20% in magnitude" | holds; every other scenario under 10% in magnitude (largest waste-target-6, -8.15%) |
| A226 | B | 19 (fuel 340 takes 19% off) | 1.8 (statement needs rewording: fuel 340 barely matters on the corrected release) |
| A227 | B | -0.1; -0.1 to -0.2 | 0 to +1.7 short; -0.3 to -1.2 long (not the same measure) |
| A228 to A263 | A and B | values unchanged | locator only: `measures.csv` has a new first column `release` (= 2025-fixed); the named columns are unchanged |
| A277 | C | table A restates measures.csv and the stores (improved) | table A now has a Release column and gives the stores on 2025-fixed with the improved figures in brackets |

Unchanged in value (already corrected): A234, A235, A240, A241, A246, A247, A258 to A261, A322 (Tier A); A275, A276, A327.

## Register rows touched

None.

## Wrong-value check:

*Example, deliberately wrong, marked as such:* "A one-year grain store on the corrected release raises the long-term capacity by 52% (to 23.7 million)." The script output gives +48.45% and 23.19 million (`analysis/paper_a/scenarios_by_region.csv`, `reference_release=2025-fixed`, `scenario=grain-store-1`, `term=long`; `measures.csv` row `2025-fixed (resilience table of 2025-store-1)`). A checker reading the row by its id and status would pass the 52%. Reading the csv cell catches it.
