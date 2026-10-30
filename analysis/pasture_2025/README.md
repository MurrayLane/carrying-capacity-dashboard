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

**Module `regional-beef-output`** (`make_regional_beef.py`, improved tier): cattle meat yield of the northern zones (Queensland and its regions, the Northern Territory, the WA Rangelands, WA state in proportion 0.50) times 0.83, southern zones times 1.254 so that national beef is unchanged (the northern zones hold 60% of the national beef dry sheep equivalents). Mechanism: a module may carry `yieldFactors` (a row of the Yield sheet and a factor per zone), applied by `build-data.mjs` and by the in-memory evaluation of `results-lib.mjs`. Effects are in `results/` (`method_effects.csv`).

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

The order is the same. Set against Queensland (= 1), the receipts per hectare are NSW 7.4, Victoria 15.1, Tasmania 19.4, South Australia 0.27, Western Australia 0.23, Northern Territory 0.17; the model's yields are NSW 2.2, Victoria 10.0, Tasmania 11.5, SA 0.65, WA 0.54, NT 0.33 before the regional factor and **NSW 3.3, Victoria 15.0, Tasmania 17.3, SA 0.99, WA 0.69, NT 0.33 after it**. So the factor brings Victoria and Tasmania into line with the receipts, and leaves NSW too low (3.3 against 7.4) and the pastoral states too high (SA 0.99 and WA 0.69 against 0.27 and 0.23; the NT 0.33 against 0.17). The shortfall is state by state: the arid rangelands of South Australia and Western Australia are still credited with about three times the beef per hectare the receipts imply. The comparison is not like for like (area operated includes cropping and other land and sheep on mixed farms; receipts carry price differences; the SA and NT samples are small), so it is recorded and not used to change the factor. The physical tables that would settle it are in the ABARES Farm Data Portal (https://www.agriculture.gov.au/abares/data/farm-data-portal, a data portal rather than a file; the page named in the data tables' index).

## What Murray can fetch, if he wants beef settled further

1. **ABARES, Australian beef: financial performance of beef farms** (latest edition; the tables of physical characteristics by region: area operated, beef cattle numbers, turn-off rate, beef cattle sold, average sale weight, northern and southern). The page: `agriculture.gov.au/abares/research-topics/surveys/beef`; the same PDFs are on `mla.com.au` under the farm survey (`.../trends--analysis/abares-farm-survey/`). Save the PDF or the Excel tables.
2. (Done 2026-10-30: the NT movement statistics are in the archive and read, above.)
3. **WA DPIRD, Cattle industry update** (turn-off, interstate transfers by Ceduna, live export from WA ports): `dpird.wa.gov.au`.
With 1 and 2 the productivity index by region can be built (kilograms sold per DSE or per hectare for northern and southern farms, Queensland and the NT separately).

## Conclusion

* No change is made yet: the national figure is independent of the regional split and wool supports uniform output per DSE for sheep, but the ABARES turn-off rates say the rule is wrong for beef in the direction above, worth 10 to 20% for southern states (sensitivity); the size needs the survey tables listed below.
* **What would settle it for beef** is output by region of origin: the ABARES farm survey (AAGIS, beef cattle farms by region: kilograms sold per hectare and per DSE) or MLA's regional data. Both sit on domains this container cannot reach (`HANDOFF.md`). If Murray can fetch the AAGIS regional physical tables, the next step is a productivity-per-DSE index by region (northern pastoral zones against high-rainfall ones) and a test of what it does to the regional results.
* Recorded as `DISCUSSION.md` row 20.
