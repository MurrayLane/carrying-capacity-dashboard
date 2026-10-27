# Land and population per SA2 (SCOPE.md B1, B2)

SA2 (ASGS Edition 3, 2021) is the base unit (B0). Everything here is per SA2 and sums to any grouping.

| File | What |
|---|---|
| `zonal_land_use.py` | Zonal histogram: area of each ALUM version 8 class in each SA2, from the ABARES Catchment Scale Land Use raster, December 2023, 50 m, EPSG:3577 (equal-area, so a cell is exactly 0.0025 km2). Needs rasterio and geopandas; runs in about three minutes. Output `data/sa2/land_use_by_sa2.csv` |
| `land_types.json` | **Draft** mapping of the raster's secondary classes to the model's five land types, with the choices that need review |
| `land_types.py` | Applies the mapping: `data/sa2/land_types_by_sa2.csv` |
| `data/sa2/population_erp.csv` | Estimated resident population by SA2, 2011 to 2025 (30 June), ABS Data API `ABS_ANNUAL_ERP_ASGS2021`, on 2021 boundaries |
| `test_land.py` | Checks on the committed tables |

Sources, both CC BY 4.0: the raster is `clum_50m_2023_v2.zip` from data.gov.au (dataset "Catchment scale land use of Australia and commodities – Update December 2023"); the SA2
boundaries are `SA2_2021_AUST_SHP_GDA2020.zip` from the ABS digital boundary files. ABARES cut the raster with the 2021 SA2 mask, so the layers share their edge.

## Checks

* Total land and water: 7,687,605 km2 against the 2011 model's 7,687,574 km2 (and the ABS's published SA2 areas, 7,688,095 km2). In 2,450 SA2s the raster area is within 0.1% of the official
  area in the typical case; the exceptions are two Torres Strait SA2s that the raster covers only in part.
* 23 SA2s have no land use (non-spatial codes such as "no usual address", and islands the raster omits). All have population rows or none; see `test_land.py`.

## National totals under the draft mapping, against the 2011 model (km2)

| | CLUM 2023 | 2011 model |
|---|---|---|
| Cropping | 437,510 | 305,997 |
| Pasture | 3,828,660 | 3,639,794 |
| Nature reserve | 1,968,531 | 1,811,007 |
| Infrastructure | 59,549 | 16,298 |
| Non-agricultural | 1,393,356 | 1,914,478 |
| Total | 7,687,605 | 7,687,574 |

Differences to expect and not to read as change: the 2011 model took cropping and pasture from the ABS census, reserve from CAPAD 2008, infrastructure as an estimate (730 m2 per person) and
non-agricultural as the remainder. This layer measures all five from one raster, with a different definition of each. Cropping here is cropping land (including fallow and irrigated crops), not the
area sown in a year. The comparison with 2011 is a land-definition effect plus a real change; D4 should separate them by also mapping the 2010-11 and 2015-16 ABARES land use for the same SA2s
(`Land use of Australia 2010-11 to 2020-21`, data.gov.au), which would give a like-for-like change.

## For Murray to review

The five-way mapping in `land_types.json`: reserve with or without class 1.2 (managed resource protection); whether land in transition and intensive horticulture count as cropping; where water and
mining go; and whether infrastructure is measured (1.2 to 4 times the 2011 estimate, depending on the choices) or estimated from population as in 2011.
