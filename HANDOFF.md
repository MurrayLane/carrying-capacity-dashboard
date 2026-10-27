# Handoff: where the project stands

Written 2026-10-27 so a new session (or a person) can resume with nothing but this repository. The plan is `SCOPE.md`; this file is the state, the standing decisions and the practical notes that were otherwise only in a chat. Update it at the end of each working session.

## State

* Repository `MurrayLane/carrying-capacity-dashboard`, branch `main`, everything committed and pushed; the Action (`Test and publish`) was green on the last commit. GitHub Pages: switch it on under Settings, Pages, Source: GitHub Actions (not confirmed done). Domain `carryingcapacity.com.au` is owned by Murray.
* The archive of the original models and papers is the private repo `MurrayLane/carrying-capacity-models` (filed into folders on 2026-10-27; its README lists them; the assistant can read and push to it). The file `Organic/Organic comparisons for paper.xls`, the organic papers and the construction-method manuscript are there.
* The git tag `qut-original` was never pushed (the git proxy refused it). The unmodified QUT snapshot is commit `04a612e`.

## Release chain (all `releases/<id>/release.json`)

Published as 2011 replicas: `2011` (as published), `2011-thesis`, `2011-corrected`. Updated method and data, each layer extends the one before and is tested alone: `2025-land` > `2025-population` > `2025-yields` > `2025-livestock` > `2025-consumption` > `2025-organic` > `2025-resilience`. The 2025 releases are status `current` (not hash-locked); freeze when Murray signs off.

Headline, Australia: short term 40.5 million (2011) to 48.0 million (`2025-organic`); long term 9.4 to 12.3 million. Where the change comes from: `analysis/comparison_2025/`. How far it could move: `analysis/sensitivity_2025/` (single choices about -10% to +15% short term, -14% to +6% long term; two pessimistic meat and diet choices together take the short term below 2011).

## Standing decisions (do not reopen)

* Method frozen during the data refresh (SCOPE.md D1). If in doubt default to 2011; if 2011 is wrong record the corrected approach as an alternate 2011 release.
* Every method choice is published BOTH ways: the 2011 replica for the direct comparison AND the updated method and data (SCOPE.md D9).
* Recreate the 2011 zones first (D2); five zones with older boundaries are flagged. Two data windows: 2021 and 2025 (B9).
* Crops the ABS stopped reporting: the group-trend proxy, applied consistently (B10). Livestock: current herd totals on the 2010 class mix, otherwise 2011 (B12).
* A negative non-agricultural remainder is shown as zero. For Australia and the states only cropping and pasture land enter capacity (non-agricultural land absorbs the reserve and infrastructure); in 23 of the 60 zones (short term) and 18 (long term) the reserve and infrastructure settings change capacity.
* No forum, no blog; only the dashboard. Visual pages are done after the modelling is complete (SCOPE.md "Order and dependencies", item 7).
* Method updates that directly inform the data (new meta-analyses, E5) are done now. Contact address for the About page is held (`mc.lane@qut.edu.au` may not persist).

## What is still open

* From Murray, not blocking: national wool and milk production and the ALFA feedlot figure (placeholders in the livestock layer); the source of the 23 kg textiles figure; Seufert 2012 and de Ponti 2012 organic crop-type ratios; whether the 7% organic default stands; whether to add a Peters-style cultivated-cropland share parameter.
* Murray's decision 2026-10-27 on method work: do E8, then E9 as a back-test first (build only if pooling beats the current estimate on a held-out year), then E10, then E1; hold E11 (separate paper), E12 (checks) and E2/E3 (scenarios). **E8 is done** (Monte Carlo ranges, `analysis/sensitivity_2025/`). **E9 back-tested and not adopted** (`analysis/yield_pooling/`: pooling does not beat the plain mean). **E10 done** (`analysis/reliability_2025/`: capacity by single year, 8 years). `zone_yields.py` gained `ZY_SOURCE=2016-21`. **Long-term settings reviewed** (`analysis/long_term_2025/`): resilience 100 years, fuel with biofuel, and where the reserve land comes from are the big ones; candidate rows SCOPE.md E13 to E15. A longer meat window (8 to 20 years) gives 47.95 to 48.45 million short term, so the five-year window is sound; E1 (pasture productivity) is lower priority than I first said (it affects regional spread more than the national figure). **E14 done** (`analysis/resilience_2025/`, release `2025-resilience`, data layer 7; the archive workbook `prelim models/resilience 150 years.xls` is in the models repo). The leave-one-out reference (-9% long term) is published as the alternate release `2025-resilience-loo`; a grain-store input is still open (SCOPE.md E15). **E13 done** as the alternate release `2025-reserve` (reserve shortfall shared pro rata: long term Australia -5.8%). Alternates of `2025-resilience`: `2025-resilience-loo`, `2025-reserve`. The 253 L long-term fuel default is the thesis's own sector-by-sector cut of 2008 use (archive `prelim models/non-food resource data.xls`, sheet `biofuel`; road transport is 58% of it). Fuel and electric vehicles researched (`analysis/liquid_fuel_2025/`): the long-term fuel setting is best read as litres of biofuel grown on the land (253 L, within CSIRO's maximum of about 340 to 365 L), and the total residual liquid fuel need in 2050 is 840 to 1,700 L a person; decision pending on named scenarios. The long-term fuel default was re-derived from Table F (uploaded to the archive's `Energy data/`): thesis method on 2023-24 gives 210 L, light vehicles electrified about 156 L (`analysis/fuel_sectors_2025/`); whether to build a release for either is Murray's decision. Still open under E15: waste and recycling ladder, reference diet, store of grain. Correction: the long-term diet is low-meat (7.5% meat and eggs), not plant-based. Remaining candidates: SCOPE.md E9 to E12 (pooled yield estimates, bad-year capacity, a nutrition-optimisation second model, external anchors), plus E1 pasture productivity (largest lever for the short term), E2, E3, E4 waste factors, E7 item-level diet.
* The sensitivity run did not vary the wool, milk and feedlot placeholders.
* Textiles, fibre shares and avoidable waste are still at 2011 values. Vegetable, fruit and nut group factors are carried from 2016-21. Three-year crop window; five-year meat window ending in heavy slaughter.
* After modelling: visual pages, About page, enabling Pages, B0a display regions beyond the 2011 zones.

## Practical notes for a fresh container

* Web: Node 22; `cd web && npm ci && npm test` (19 tests). Python tests: `python3 -m unittest discover -s pipeline/yields/recent` (and `abs_current`, `pipeline/land`, `pipeline/yields`), run without `-I`.
* Downloaded source files are NOT in the repository except the derived layers under `data/`. To re-run the pipelines: `analysis/recent_data/fetch_recent.py` fetches the ABS files; the READMEs in `pipeline/land/`, `pipeline/yields/recent/`, `analysis/consumption_2025/`, `analysis/organic_2025/` and `analysis/sensitivity_2025/` give each command in order.
* The land scripts need a Python environment with `rasterio geopandas pyogrio shapely openpyxl xlrd`; the ABARES CLUM raster comes from data.gov.au.
* Reachable from the assistant's cloud container: data.gov.au, the ABS, bulks-faostat.fao.org, PLOS. Blocked: agriculture.gov.au (ABARES), mla.com.au, dcceew.gov.au, data.daff.gov.au; ask Murray to check those pages by hand and give him the URL and steps. The shell blocks `sleep`; use a monitor for waits.
* The sensitivity runs need the built data (`cd web && node scripts/build-data.mjs`).
