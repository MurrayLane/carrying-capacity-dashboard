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

## What Murray can fetch, if he wants beef settled

1. **ABARES, Australian beef: financial performance of beef farms** (latest edition; the tables of physical characteristics by region: area operated, beef cattle numbers, turn-off rate, beef cattle sold, average sale weight, northern and southern). The page: `agriculture.gov.au/abares/research-topics/surveys/beef`; the same PDFs are on `mla.com.au` under the farm survey (`.../trends--analysis/abares-farm-survey/`). Save the PDF or the Excel tables.
2. **NT Department of Agriculture and Fisheries, Pastoral Market Update** (monthly) and the **livestock movement statistics reports** (NT to interstate, within NT, interstate to NT; biannual): `daf.nt.gov.au`.
3. **WA DPIRD, Cattle industry update** (turn-off, interstate transfers by Ceduna, live export from WA ports): `dpird.wa.gov.au`.
With 1 and 2 the productivity index by region can be built (kilograms sold per DSE or per hectare for northern and southern farms, Queensland and the NT separately).

## Conclusion

* No change is made yet: the national figure is independent of the regional split and wool supports uniform output per DSE for sheep, but the ABARES turn-off rates say the rule is wrong for beef in the direction above, worth 10 to 20% for southern states (sensitivity); the size needs the survey tables listed below.
* **What would settle it for beef** is output by region of origin: the ABARES farm survey (AAGIS, beef cattle farms by region: kilograms sold per hectare and per DSE) or MLA's regional data. Both sit on domains this container cannot reach (`HANDOFF.md`). If Murray can fetch the AAGIS regional physical tables, the next step is a productivity-per-DSE index by region (northern pastoral zones against high-rainfall ones) and a test of what it does to the regional results.
* Recorded as `DISCUSSION.md` row 20.
