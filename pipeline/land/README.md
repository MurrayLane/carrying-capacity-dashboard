# Land and population per SA2 (SCOPE.md B1, B2)

**Default method: the 2011 method** (`land_2011_method.py`, evidence in `analysis/land_2011/`): ABS cropping and grazing, infrastructure at 730 m2 per person, reserve and total area from the raster, non-agricultural as the remainder, allocated to the 2011 zones through `zone_to_nrm2011.json`. The five-type mapping of the raster below (`land_types.json`) is the alternate, fully measured version and is not the default.

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

* Total land and water: 7,687,605 km2 against the 2011 model's 7,687,574 km2 (and the ABS's published SA2 areas, 7,688,095 km2). The raster area of the middle half of the 2,450 SA2s is within 0.05% of the official
  area; the one large exception is Torres Strait Islands (63% covered) and, to a lesser degree, Torres (97%).
* 23 of the ABS's 2,473 SA2s have no land use rows (19 have no boundary at all, such as "no usual address" and migratory codes; four are small islands the raster omits). Every SA2 that has land also has population (`test_land.py`).

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
mining go; and whether infrastructure is measured (59,549 km2 under the draft, 3.7 times the 2011 estimate of 16,298 km2) or estimated from population as in 2011.
