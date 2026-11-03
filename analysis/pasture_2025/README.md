# Spatial pasture productivity (SCOPE.md E1)

E1 asked whether the regional stock-count average that sets the model's meat yields should be replaced by pasture-growth or stocking-rate rasters. Red meat is most of the land of the short-term diet, so it is the largest lever on the result. This is what the open data can and cannot test.

## What the model assumes

`pipeline/yields/livestock.py` shares a zone's grazing and hay land among its animals by dry sheep equivalent (DSE). A zone's meat is the **national** meat produced (ABS Livestock Products, calibrated to the thesis's 2010 figure) times the zone's share of national DSE, so the yield per hectare is the national meat per DSE times the zone's DSE per hectare of pasture. Two things follow:

* **The national capacity does not depend on the spatial assumption**: the sum over zones is the national meat production, whatever the split. E1 can change regions, not the Australian figure (the Australian zone is computed from national totals).
* **The regional pattern assumes the same output per DSE everywhere.** A zone is productive in the model because it carries many animals per hectare, not because its pasture grows more or its animals turn off faster.

## What the open data can test

| Test | Result |
|---|---|
| ABS meat produced by state against the state's DSE share (`state_production.py`, `state_production.csv`) | Cannot be used: the ABS tables are by **state of slaughter**, not of origin. Victoria produces 22% of cattle meat and 48% of sheep meat from 10% and 22% of the DSE (its abattoirs take animals from other states); the Northern Territory has 7.8% of beef DSE and no slaughter (live export and interstate sales). Queensland, South Australia and Tasmania are within 10% to 25% of their DSE share for cattle. |
| ABS value of cattle and sheep disposals by state (`AALDC_Value_of_livestock_and_products`, Tables 1 and 3) | Cannot be used: the values mirror the state of slaughter or sale (Victoria 47% of sheep disposals). |
| ABS **wool** value by state of the farm against sheep DSE (`wool_by_state.py`, `wool_by_state.csv`) | **Supports the assumption for sheep at state scale**: wool per DSE relative to the nation is 0.93 (NSW-ACT), 1.03 (Victoria), 0.96 (South Australia), 1.03 (Tasmania), 1.20 (Western Australia) and 0.77 (Queensland, 3% of the flock). |
| Live exports (about 0.67 million cattle and 0.59 million sheep in 2023, MLA and DAFF) | They leave the herd without being counted as meat by the ABS (about 5% of cattle meat and 2% of sheep meat in carcase terms). The 2025 layer scales the ABS meat to the archive's 2010 figure (cattle 1.086, sheep and lamb 1.155); that calibration probably already absorbs live exports (2010 had more) but its source is not recorded, so this is not verified. |

## Leads followed up (2026-10-29)

* **ABARES beef farm survey, by region (published ranges, from search summaries; the reports themselves were not reachable).** Northern Australia (northern WA, NT and Queensland) against southern: turn-off rate about 30 to 34% a year against 41 to 47%, and stocking about half the southern rate (roughly 1,800 to 1,900 hectares per large stock unit on the northern farms against 870 to 900 in the south, early 2010s tables). ABARES attributes it to more variable and poorer pasture in the north and improved pasture and fodder crops in the south. The model's rule (the same output per DSE) therefore probably **overstates northern beef and understates southern beef**, the direction being clear and the size not.
* **Sensitivity (`north_south_sensitivity.mjs`, `north_south_sensitivity.csv`)**: northern zones (Queensland, the Northern Territory, half of Western Australia by DSE: 61% of the national beef DSE) at 0.73 of the model's cattle meat yield (the ratio of the turn-off midpoints), the southern zones scaled up (1.40) so that national meat is unchanged. Short-term capacity: NSW-ACT +20.6%, Victoria +12.0%, South Australia +15.7%, Western Australia +3.2%, Tasmania -0.5%; Queensland and the Northern Territory change by under 0.2% (their capacity is set by cropland, not pasture); Australia 0. Long term: NSW-ACT +10.2%, SA +11.1%, Victoria +4.3%. **So the national figure is safe and the southern state figures carry a 10 to 20% uncertainty from this assumption.**
* **Live exports by state of origin**: the Northern Territory exported 184,597 NT-origin cattle through Darwin in 2023 and 274,181 in 2024 (NT DAF Pastoral Market Update, July 2025; some NT cattle leave by interstate ports). NT interstate sales and Queensland, WA and SA movements are reported in biannual NT, WA (DPIRD cattle industry update) and Queensland livestock-movement tables that are not in the open files this container can reach.
* **NLIS** (the national cattle tracing database) holds every movement by property; a 2015 analysis of 2008 to 2012 movements found most stay within a production region, and those that leave stay within the state. The movements are not public.

## Murray's files read (2026-10-29, `Livestock/ABARES-NT-WA/` of the models archive)

ABARES, *Australian beef: financial performance of beef farms* (2012-13 to 2014-15; 2013-14 to 2015-16; 2015-16 to 2017-18), Australian Agricultural and Grazing Industries Survey, northern against southern region:

| 2014-15, average per farm | Northern | Southern |
|---|---|---|
| Area operated (ha) | 23,436 | 5,561 |
| Beef cattle at 30 June | 1,453 | 400 |
| Beef cattle sold | 508 | 197 |
| Turn-off rate (2012-13, 2013-14, 2014-15) | 31, 34, 38% | 41, 46, 47% |
| Branding rate | 70% | 86 to 89% |
| Total live weight of cattle produced (t) | 227 | 75 |
| **Live weight produced per head of herd** | **156 kg** | **188 kg** |
| Hectares per large stock unit | 13 to 14 | 7 |

Ratio of live weight produced per head, north to south: **0.83**; by turn-off rates 0.74 to 0.81. ABARES's northern region is northern Western Australia, the Northern Territory and Queensland (all of it, including the small south-east Queensland farms). The WA DPIRD cattle update (WA turn-off 600,000 to 657,000 head a year, live exports 26% and interstate transfers 7 to 10% of it) and the NT Pastoral Market Update (NT-origin live exports through Darwin 184,597 in 2023 and 274,181 in 2024) are in the folder for the interstate and live-export flows; the ABARES survey does not give a state split of herd and area.

**Module `regional-beef-output`** (`make_regional_beef.py`, improved tier), rebuilt 2026-10-30 on the state-level physical data (next section): each state's cattle meat yield times the state's index of beef output per animal and one constant so that national beef is unchanged. Mechanism: a module may carry `yieldFactors` (a row of the Yield sheet and a factor per zone), applied by `build-data.mjs` and by the in-memory evaluation of `results-lib.mjs`. Effects are in `results/` (`method_effects.csv`). The first version used the region-level 2014-15 ratio (north 0.83, south 1.254).

## The Northern Territory, from Murray's NT waybill files (2026-10-30)

NT Department of Agriculture and Fisheries, cattle movement statistics from the waybill database (generated 27 March 2026; `Livestock/ABARES-NT-WA/nt-cattle-movement-stats-calendar-year.pdf` and the regional, financial-year and slaughter files) and the Pastoral Market Update history (NT cattle through Darwin). The NT's beef herd is about 2 million head (ABS). Cattle leaving the NT to other states in a year: 676,000 (2019), 383,000, 318,000, 466,000, 238,000, 394,000 (2024), mostly to Queensland (the largest), South Australia, Victoria and WA; cattle live exported through Darwin: 221,000 (2019), 271,000, 235,000, 196,000, 180,000, 253,000 (2024). **Turn-off (interstate plus live export) over the herd: 37, 32, 28, 36, 22 and 32% (`nt_turnoff.csv`), mean 31%**, the same as ABARES's 32 to 33% for northern beef farms, against 44% in the south. Only a few tens of thousands of NT cattle a year go interstate for immediate slaughter (Alice Springs to South Australia and Victoria); the rest are finished elsewhere, which is why the NT shows almost no slaughter against 7.8% of the beef dry sheep equivalents. NT cattle are also lighter at sale (live export steers and heifers), so output per head in the NT is, if anything, below the 0.83 of the module. The module's northern factor is confirmed for the Northern Territory.

## ABARES 2021-22 to 2023-24 (Murray's files, 2026-10-30): a second regional check

The newest ABARES release (*Financial performance of livestock farms* and the broadacre data tables, `Livestock/ABARES-NT-WA/FinancialPerformance*_2021-2024_V1.0.0.*`) is financial: farm numbers, area operated and receipts by industry and state, with **no physical data** (cattle numbers, turn-off, sale weight), so it cannot replace the 2014-15 tables behind the factor. It does give beef receipts per farm and area operated for beef specialists by state, hence **beef receipts per hectare operated** (mean 2021-22 to 2023-24, 2023-24 dollars; `beef_receipts_by_state.csv`):

| State | Beef specialist farms | Hectares per farm | Beef receipts per hectare | Model cattle meat, kg per hectare of pasture, before / after the regional factor |
|---|---|---|---|---|
| Tasmania | 565 | 390 | $975 | 107.6 / 134.9 |
| Victoria | 5,288 | 325 | $758 | 93.6 / 117.3 |
| New South Wales | 5,628 | 930 | $369 | 20.5 / 25.7 |
| Queensland | 7,866 | 12,490 | $50 | 9.4 / 7.8 |
| South Australia | 527 | 38,420 | $14 | 6.1 / 7.7 |
| Western Australia | 1,284 | 48,860 | $11 | 5.1 / 5.4 |
| Northern Territory | 148 | 336,230 | $8 | 3.1 / 2.6 |

The order is the same. Set against Queensland (= 1), the receipts per hectare are NSW 7.4, Victoria 15.1, Tasmania 19.4, South Australia 0.27, Western Australia 0.23, Northern Territory 0.17; the model's yields are NSW 2.2, Victoria 10.0, Tasmania 11.5, SA 0.65, WA 0.54, NT 0.33 before the regional factor and **NSW 3.3, Victoria 15.0, Tasmania 17.3, SA 0.99, WA 0.69, NT 0.33 after it**. So the factor brings Victoria and Tasmania into line with the receipts, and leaves NSW too low (3.3 against 7.4) and the pastoral states too high (SA 0.99 and WA 0.69 against 0.27 and 0.23; the NT 0.33 against 0.17). The shortfall is state by state: the arid rangelands of South Australia and Western Australia are still credited with about three times the beef per hectare the receipts imply. **This state-level conclusion was withdrawn: see the regional comparison below.** The physical tables that would settle it are in the ABARES Farm Data Portal (https://www.agriculture.gov.au/abares/data/farm-data-portal, a data portal rather than a file; the page named in the data tables' index).

## The ABARES Farm Data Portal, state by state (Murray's files, 2026-10-30)

`fdp-state-historical.csv` (state estimates 1990 to 2025, beef specialist farms; `abares_state_index.py`, `abares_state_beef_index.csv`) has the physical items the 2021-24 report lacks. Mean 2017 to 2023 per beef farm: ABARES turn-off (sold plus transferred off, over the herd) is NSW 47%, Victoria 44%, Tasmania 42%, South Australia 47%, Western Australia 39%, Northern Territory 39%, **Queensland 35%**; herd per 1,000 hectares 323, 873, 1,072, 16, 20, 32 and 83. **Output per animal kept**, valued as (sold plus transferred) x receipts per head sold over the herd, is $817, 836, 826, 772, 602, 533 and 553 a head (NSW, Victoria, Tasmania, SA, Queensland, WA, NT): an index against the temperate south of **0.99, 1.01, 1.00, 0.93, 0.73, 0.65, 0.67**. That is lower than the 0.83 of the 2014-15 region tables because it carries weight at sale as well as turn-off (WA and NT cattle sell at about $1,350 to $1,420 a head against $1,700 to $1,960). The relative gap in the first version of the module (0.66) was close; the new indices differ for Western Australia (0.65 against 0.83) and South Australia (0.93 against 1.0).

## Regions, not states: the pastoral rangelands are not too high after all (2026-10-30)

`fdp-regional-historical.csv` has the 32 ABARES broadacre regions. Compared region by region (`abares_region_check.py`, `abares_region_check.csv`; beef receipts per hectare operated against the model's cattle meat per hectare of the matching zones, both relative to Queensland West and South West), the arid regions agree: **SA Northern Pastoral 0.24 against the model's 0.19; WA Pilbara and Central Pastoral 0.37 and the Kimberley 0.87 against 0.30 (one zone, the Rangelands); NT 0.66 to 1.17 against 0.58; Queensland Cape York and the Gulf 1.11 against 1.18, Central North 2.44 against 2.11; Victoria South and East 35 against 42; Tasmania 30 against 21.** The earlier state-level comparison that made the SA and WA rangelands look three times too productive was an artefact: the state averages mix the pastoral stations with the cropping regions of the same state, and the receipts per hectare of a state are not comparable with the model's yield per hectare of pasture. The weaker matches are NSW Far West (0.29 against 0.65, the model high by 2) and NSW Tablelands (28 against 9.9, the model low by 3, with an uncertain match of ABARES region to NRM zones) and the Queensland Charleville to Longreach region (3.0 against 1.1; the zones overlap). **No change to the module.**

## What Murray can fetch, if he wants beef settled further

1. **ABARES, Australian beef: financial performance of beef farms** (latest edition; the tables of physical characteristics by region: area operated, beef cattle numbers, turn-off rate, beef cattle sold, average sale weight, northern and southern). The page: `agriculture.gov.au/abares/research-topics/surveys/beef`; the same PDFs are on `mla.com.au` under the farm survey (`.../trends--analysis/abares-farm-survey/`). Save the PDF or the Excel tables.
2. (Done 2026-10-30: the NT movement statistics are in the archive and read, above.)
3. **WA DPIRD, Cattle industry update** (turn-off, interstate transfers by Ceduna, live export from WA ports): `dpird.wa.gov.au`.
With 1 and 2 the productivity index by region can be built (kilograms sold per DSE or per hectare for northern and southern farms, Queensland and the NT separately).

## Conclusion

* No change is made yet: the national figure is independent of the regional split and wool supports uniform output per DSE for sheep, but the ABARES turn-off rates say the rule is wrong for beef in the direction above, worth 10 to 20% for southern states (sensitivity); the size needs the survey tables listed below.
* **What would settle it for beef** is output by region of origin: the ABARES farm survey (AAGIS, beef cattle farms by region: kilograms sold per hectare and per DSE) or MLA's regional data. Both sit on domains this container cannot reach (`HANDOFF.md`). If Murray can fetch the AAGIS regional physical tables, the next step is a productivity-per-DSE index by region (northern pastoral zones against high-rainfall ones) and a test of what it does to the regional results.
* Recorded as `DISCUSSION.md` row 20.

## Pasture quality: dairy on land that can support it (Murray 2026-11-03; `pasture_quality.py`, `two_pool_test.mjs`, `two_pool.csv`)

Decisions (Murray): dairy only on land that can support it at its known yield; improved pasture split from the SA2 land-use data (CLUM); arable share of improved pasture from GAEZ; results as a range.

* **Improved pasture** (`data/sa2/improved_pasture_by_sa2.csv`): the CLUM share of modified (3.2.x) and irrigated modified (4.2.x) pasture among grazing land, applied to the model's pasture of each SA2: **218,000 km2, 6.6% of the pasture** (CLUM modified 213,600 km2 against 3.61 million km2 of native grazing; the ABS gives 45 million ha improved nationally, not available by SA2).
* **Observed milk yield on improved pasture** (`data/2025/pasture_quality_by_zone.csv`): zone milk 2025 (the 2010 archive figure times each state's change in Dairy Australia milk) over the zone's improved pasture. The 16 zones that hold 90% of the milk give **73 g of milk per m2 of improved pasture** (all regions 39; West Gippsland 319, Glenelg Hopkins 89, Corangamite 163, North West Tasmania 295); the workbook's average-pasture dairy yield is 25.7. Beef and sheep also graze improved pasture, so dividing all the milk by all the improved area is a lower bound on dairy's own yield.
* **Arable share** (`analysis/gaez_2025/arable_share_by_sa2.py`, `data/sa2/arable_share_gaez_by_sa2.csv`): the share of each SA2 assessed as very suitable, suitable or moderately suitable on GAEZ v4 (rainfed, high input) for wheat, barley or rapeseed, whichever is the largest; **43%** of the nation's improved pasture lies on such land. A regional rule from a model, not a measurement.
* **How the workbook is changed.** Dairy's land is a pasture use (`Settings!D34`); it is moved to the cropping column (`Settings!C34`), so dairy competes with crops for good land (cropland plus the arable improved pasture) and cannot use rangeland; beef and sheep keep the pasture pool and borrow cropland when it is short, as before. Dairy's yield is the observed 73 g/m2. Non-arable improved pasture stays in the pasture pool and is not open to dairy (conservative).
* **Result** (2025-fixed, short term, state yields; share of the unchanged model's national capacity on today's diet, 41.5 million; columns: unchanged model | improved pasture not arable | GAEZ share | all improved pasture arable):

| Today's diet | Unchanged | a = 0 | GAEZ | a = 1 |
|---|---|---|---|---|
| Australia | 100% | 100% | 110% | 110% |
| States | 75% | 64% | 65% | 66% |
| SA4 | 58% | 47% | 53% | 56% |
| SA3 | 44% | 36% | 43% | 45% |
| SA2 | 37% | 30% | 37% | 39% |

| 2.5% meat and eggs | Unchanged | a = 0 | GAEZ | a = 1 |
|---|---|---|---|---|
| Australia | 284% | 112% | 145% | 188% |
| States | 179% | 97% | 114% | 126% |
| SA4 | 136% | 81% | 99% | 115% |
| SA3 | 108% | 70% | 88% | 101% |
| SA2 | 95% | 63% | 81% | 93% |

* **Reading.** On today's diet the national capacity rises by 10% when improved pasture counts as good land (pasture still binds), and fine scales lose or keep about what they had. On the low-meat diet the picture reverses: the national optimum of 284% (118 million) depended on dairy using the abundant low-quality pasture; with dairy on good land it competes with crops and the capacity is 112% to 188% (46 to 78 million; GAEZ central 60 million). The earlier dairy-yield multiplier test (+24 to 28% at fine scale) kept dairy on pasture and so understated the competition. Dairy at 73 g/m2 takes about 4,400 m2 of good land a person a year, more than all the crops (about 3,300 m2).
* **Limits.** The diet is the NHMRC family with its dairy serves unchanged; a diet that takes less dairy would do better and the nutrition-limited optimisation (`analysis/nutrition_lp_2025`) has not been rerun on this basis. The yield is one national figure applied to every unit; non-arable improved pasture is closed to dairy (the truth for dairy lies between the GAEZ and all-arable columns); the lower bound a = 0 leaves dairy only cropland.

## Adopted in the improved line (2026-11-03): method module `dairy-good-land`

Murray's rule: adopt into the improved line if the national effect exceeds about 5%. It did (today's diet +10%), so the scale analysis above became a module (`methods/dairy-good-land/method.json`), listed last in the improved methods (`analysis/comparison_2025/make_cells.py`).

* **What it does.** `Settings!C34` takes dairy's land formula and `D34` becomes 0, so dairy competes with crops for cropland. For every zone, the arable improved pasture (a share of the zone's pasture, `arable_improved_share` in `data/2025/dairy_good_land_by_zone.csv`) moves from pasture to cropping, and the milk yield (Yield row 97) is 73 g/m2. Shares rather than areas, so the same file applies to the 2011 zones' land and the 2025 zones' land (national share 2.8% of the pasture; improved pasture is 6.6% of the pasture, 218,207 km2, and 43% of it is arable by GAEZ).
* **Effect on the improved cell, Australia, millions** (`results/method_effects.csv`, step in sequence after the other improvements): 2011 short +3.3, long -1.0; 2025 short +5.0, long -1.1.
* **Range for the arable share** (`dairy_range.mjs`, `results/dairy_range.csv`; none of the improved pasture arable | GAEZ | all of it):

| Improved cell, Australia, millions | a = 0 | GAEZ | a = 1 |
|---|---|---|---|
| 2011 short term | 40.1 | 40.1 | 40.1 |
| 2011 long term | 8.6 | 11.6 | 15.4 |
| 2025 short term | 45.1 | 50.7 | 50.7 |
| 2025 long term | 11.3 | 14.7 | 17.5 |

* **Reading.** The short term is insensitive to the arable share wherever cropland already holds the crops plus dairy (all of 2011, and 2025 once a is above zero), because the model lets cropland graze when pasture is short and total land then binds. The long term is sensitive, because a low-meat diet leaves pasture unused and cropland is the scarce type: every km2 of improved pasture that cannot be cropped is a km2 dairy cannot use without displacing crops. The long term falls against the old treatment (dairy on pasture, which was free in that diet) at GAEZ and below, and rises only if most of the improved pasture can be cropped. This is the largest single uncertainty the module adds and is reported as a range, as decided.
* **Limits.** As in the scale analysis: 73 g/m2 applies in every zone, dairy on cropland is assumed to match improved pasture, non-arable improved pasture is closed to dairy, and the shares are 2020-21 land use applied to the 2011 thesis zones. The nutrition-limited optimisation has not been rerun on this basis.

### Queensland and the north: why the module halves Queensland (2026-11-03)

The module cut Queensland's short-term capacity on today's diet from 10.1 to 4.8 million (population 5.67 million). Traced in turn:

1. **Mechanism (checked).** At Queensland's capacity cropland is 99% used (35,137 of 35,387 km2) and only 30% of the pasture is. Dairy takes 20,465 km2 of the cropland (58%) at 73 g/m2, because Queensland has almost no improved pasture to move to cropping. Red meat uses 352,000 km2 of pasture and the rest of the rangeland is idle.
2. **Not the arable share.** Rebuilt for any field crop including sorghum, maize, sugar cane, cotton, soy, sunflower and groundnut (`arable_share_by_sa2.py ... broad`), the arable share of improved pasture moves from 43.2% to 47.0% nationally and Queensland from 4.77 to 4.92 million.
3. **Not a processing mistake.** The CLUM class areas summed over the SA2s match the raster's national totals (modified pasture 179,800 km2). Queensland's own land-use layer (Queensland Land Use - Current, spatial-gis.information.qld.gov.au) gives 1,502 km2 of 'Grazing modified pastures' and 270 km2 of irrigated modified pasture against 1,378,445 km2 of 'Grazing native vegetation': the same as CLUM. The national layer faithfully reproduces what Queensland maps.
4. **The source is inconsistent between states.** The ABS 2007-08 share of grazing land that is improved pasture (the model's own 2011 data, by the same NRM regions: `data/2025/abs_improved_pasture_2007_08_by_zone.csv`, `abs_improved_check.py`) against CLUM, share of each state's grazing land:

| | CLUM (used) | ABS 2007-08 |
|---|---|---|
| NSW-ACT | 13.8% | 33.0% |
| Victoria | 99.8% | 78.5% |
| **Queensland** | **0.1%** | **24.6%** |
| South Australia | 14.1% | 9.6% |
| Western Australia | 5.3% | 6.7% |
| Tasmania | 84.8% | 66.4% |
| Northern Territory | 0.3% | 3.4% |
| Australia (km2 of the model's pasture) | 218,000 | 598,000 |

Victoria, South Australia and Tasmania agree to within the difference of definition and date; New South Wales, Queensland, the Northern Territory and Western Australia are undercounted in CLUM, Queensland by a factor of about 200. The milk figures agree: South East Queensland makes 87,000 t on 105 km2 of CLUM 'improved pasture' (830 g/m2, ten times the rate elsewhere); on the ABS basis the 90%-of-milk zones give 84 g/m2 against 73 on CLUM, so the yield does not depend on the source.
5. **What the ABS basis does** (`dairy_abs_improved_test.mjs`, `results/dairy_abs_basis.csv`; 2025-improved, short term, million; ABS improved share times the zone's pasture-weighted GAEZ arable share, yield 84.4): Queensland 7.2 (4.8 on CLUM; 10.1 before the module), NSW-ACT 13.9 (13.6), Victoria 6.2 (6.0), Tasmania 0.76 (0.73), South Australia and Western Australia unchanged, Australia 51.1 (50.7). With arable shares for any field crop Queensland would be 15.0 and the Northern Territory 0.7, which is not a result: the arable share of the tropical rangeland is high (GAEZ) and the module adds all of it to cropland, available to crops as well as dairy, which is a land conversion far beyond dairy's need.
6. **A second design point.** Moving arable improved pasture into the cropping column makes it available to every crop, not only dairy. Where improved pasture is small (Victoria, South Australia) this changes little; where the ABS shows large improved areas on tropical land (Queensland, Northern Territory) it creates cropland. Dairy needs 4,300 m2 a person; the 'arable improved' areas of Queensland on the ABS basis are many times that.

**Status.** No mistake in the pipeline; the improved-pasture layer is inconsistent across states. The Queensland and Northern Territory (and to a lesser degree New South Wales and Western Australia) state figures under `dairy-good-land` rest on it and are not to be quoted until Murray decides (HANDOFF).

### Root cause of the Queensland anomaly (2026-11-03, second pass)

Murray asked for the root cause, not a choice between sources. What is established, what is not.

* **Where the anomaly arises: in how native and exotic pasture are told apart.** ALUM version 8 puts a grazing paddock in 3.2 (modified pastures) when more than 50% of the dominant species are exotic and in 2.1 (native vegetation) when more than 50% are native. Queensland's land-use metadata (Land use mapping 1999 to 2017, qldspatial) says of this separation: 'Identifying and separating these using imagery, aerial photography and field observation is difficult and unreliable', that grazing classes 'may therefore not be consistent', and that grazing is confused with 2.1.0 and 1.3.0. Queensland was mapped region by region in different years (2011 to 2017). The result, in the state layer itself: 1,378,445 km2 native grazing and 1,502 km2 modified.
* **Direct evidence that it misclassifies the dairy districts.** In the CLUM grazing area of the SA2s that hold Queensland's dairy: Malanda-Yungaburra (Atherton Tableland) 446 km2 native, 66 modified, 14 irrigated pasture; Beaudesert 1,249 native, 6 modified; Boonah 1,556 native, 15 modified; Kilcoy 1,834 native, 1 modified; Gympie surrounds 1,311 native, 2 modified. These are sown kikuyu, paspalum, rhodes and irrigated pasture districts. The same pattern explains South East Queensland's 830 g/m2.
* **Different definitions of 'improved'.** (1) ALUM 3.2: a mapped land cover judgement, more than half exotic species. (2) ABS census: 'Improved pasture used mainly for grazing (ha)', reported by the farmer; the wording of the item does not define improved, and the ABS explanatory note that would was not retrievable (2013-14 release: 49.3 million ha, 12.1% of the 406.3 million ha managed, Tasmania 53.3%, Victoria 41.8%). (3) Agronomic (FutureBeef): fully sown (high input), oversown (low input, legumes into native pasture), ley pasture on cropland, leucaena browse. The three do not coincide: oversown and fertilised native pasture is improved to a farmer and native to a mapper. None of them is 'land that can carry dairy at a known yield'.
* **Can dairy run without improved pasture? Yes, partly, but not on native pasture.** Dairy Australia's categories run from grazing with bail feeding to total mixed ration (cows never graze; 'fully housed or on a feed pad'). National survey 2014-15: 12% of farms were pasture plus partial mixed ration on a feed pad, 1% total mixed ration; in an average year about 60 to 65% of feed is grazed pasture. A total mixed ration herd still needs feed grown somewhere, as grain, silage and hay on cropland, so its land is cropland, which is how the module already charges dairy. A source on Queensland says total mixed ration dominates the Darling Downs. No source found shows milk production at scale from native pasture or rangeland.
* **So the first two options were the wrong question.** CLUM cannot identify dairy land in Queensland (a mapping limit), ABS improved pasture is a farmer-reported category that does not identify it either. What identifies land that carries dairy at a known yield is dairy production itself: where milk is made, at what yield, on how much land.
* **Not established.** Queensland's internal mapping rule for sown pasture (the QLUMP technical documents were not retrievable), and the ABS definition of improved pasture. The Queensland layer's 'commodity' tag for dairy covers only about 2 km2 of pasture and 12 km2 of dairy sheds, so it cannot be used to find dairy land.

## Dairy farm area data and the rebuilt module (2026-11-03)

**Data found** (`dairy_farm_yield.py` holds every figure and its source; `data/2025/dairy_farm_yield_by_state.csv`, `dairy_farm_yield_by_zone.csv`):

* Milk volume and farm numbers by state, financial year 2025, Dairy Australia *Farm business production 2025* (Levies Revenue Services): NSW 1,090 ML on 429 farms, Victoria 5,407 ML on 2,573, Queensland 277 ML on 244, South Australia 416 ML on 160, Western Australia 331 ML on 108, Tasmania 927 ML on 279 (Australia 8,450 ML, 3,793 farms).
* Milk solids per usable hectare, Dairy Farm Monitor Project annual reports, 'Whole farm analysis, physical parameters': Victoria 2024-25 (Northern Victoria 1,053 kg MS/ha, South West Victoria 585, Gippsland 890), NSW 2024-25 (state 702; north 576, south 812), South Australia 2024-25 (581), Western Australia 2024-25 (445), Tasmania 2023-24 (1,120). Usable area is the farm's managed hectares less land of no value to livestock (house, sheds).
* Queensland: the Queensland Dairy Accounting Scheme 2025 (2024-25, 55 farms in four groups: South Queensland grazing 13 farms, partial mixed ration 21, total mixed ration 9, North Queensland grazing 12), milk per farm and usable area per farm: 5,954 litres per usable hectare overall (grazing 5,200, partial mixed ration 7,280, total mixed ration 5,220 on farms that are mostly cropping, North Queensland 5,830).

**What it shows.** Milk per usable hectare of a dairy farm is **613 g/m2 in Queensland, 629 in Western Australia, 790 South Australia, 962 NSW, 1,072 Victoria, 1,399 Tasmania; 1,013 milk-weighted nationally**. The module's earlier 73 g/m2, and the workbook's 26, are milk per m2 of *all* improved pasture, most of which carries beef and sheep: ten to forty times less than what dairy farms achieve on their own land. The usable area of the dairy farms implied by the state milk and these yields is about 8,600 km2 for Australia (Queensland 465 km2; the monitoring-project farms are larger than average so farm numbers times sample area would give about 12,000 km2), against the 218,000 km2 CLUM 'improved pasture' and the 3.3 million km2 of pasture. This is the root of the Queensland result: at 73 g/m2 the model charged Queensland's people 20,465 km2 of dairy land (58% of its cropland) for milk that Queensland's dairy farms produce on about 465 km2.

**The rebuilt module** (`methods/dairy-good-land/method.json`): dairy's land still moves to the cropping column (`Settings!C34`, `D34`), because a dairy farm's feed (forage, fodder crops, irrigated pasture, the grain of a total mixed ration herd) is grown on cropland; the milk yield of every zone is its state's observed yield on dairy farms; the land move from improved pasture and the arable shares are withdrawn (the layer cannot find dairy land in Queensland, and at these yields dairy needs only a few per cent of the cropland, so the extra 'good land' is not needed). The Northern Territory, which has no commercial dairy industry, takes the national milk-weighted yield.

**Results** (improved cell, Australia, million; before the module | with the module as first built at 73 g/m2 | rebuilt): 2011 short term 36.8 | 40.1 | 41.7, long term 12.6 | 11.6 | 13.1; 2025 short term 45.7 | 50.7 | 53.6, long term 15.7 | 14.7 | 18.5. By state (2025, short term, million; before | rebuilt): NSW-ACT 12.9 | 15.3, Victoria 7.2 | 7.7, Queensland 10.1 | 9.6, South Australia 2.3 | 2.6, Western Australia 3.0 | 3.4, Tasmania 0.34 | 0.32. The Queensland anomaly is gone: no state moves by more than 18%.

**Range** (`dairy_range.mjs`, `results/dairy_range.csv`): with the yield halved (bought-in feed counted at the same yield, and the sample's larger-than-average farms) Australia is 53.4 short term and 18.2 long term (2025), Queensland 8.5 and 1.0: the result is insensitive to the dairy yield, because dairy now needs a small part of the cropland.

**Limits.** The yield is milk per usable hectare of the monitoring-project farms, which are larger and more productive than the average farm, and excludes the land that grows bought-in feed and, for some farms, agistment of heifers; one yield per state although regions differ (Victoria 585 to 1,053 kg MS/ha); Tasmania is 2023-24; kg MS to litres is the state's own ratio where read and 13.3 elsewhere. The scale analysis above (`two_pool_test.mjs`, the 110% and 284% tables) used the withdrawn 73 g/m2 and improved-pasture rules and is superseded; it is rerun in the section below. The `abs_improved_*` and `dairy_good_land.py` files remain as the record of the improved-pasture approach.

