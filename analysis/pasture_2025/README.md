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

## Conclusion

* No change is made: the national figure is independent of the regional split, the one product that can be tested by state of origin (wool) supports uniform output per DSE, and the meat tests are blocked by interstate livestock movement.
* **What would settle it for beef** is output by region of origin: the ABARES farm survey (AAGIS, beef cattle farms by region: kilograms sold per hectare and per DSE) or MLA's regional data. Both sit on domains this container cannot reach (`HANDOFF.md`). If Murray can fetch the AAGIS regional physical tables, the next step is a productivity-per-DSE index by region (northern pastoral zones against high-rainfall ones) and a test of what it does to the regional results.
* Recorded as `DISCUSSION.md` row 20.
