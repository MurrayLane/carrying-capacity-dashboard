# How the 2011 land areas were made, worked out from the archive, and the same method on current data

Murray's rule (2026-10-27): default to what was done in 2011; where 2011 is wrong, record the corrected approach as an alternate 2011 release. The method below was recovered from
`Models/Yield data/NRM - Landuse.xls` (formulas and year sheets), `Land use/ibra_61_and_nrm_2010.xls`, `Land use/Nature reserve.xls` and the 2011 NRM boundary file
`Land use/Mapinfo_nrmr_2011_aust_midmif.zip`.

## The 2011 method

| Quantity | How it was made | Evidence |
|---|---|---|
| Cropping | Mean of five years, 2005-06 to 2009-10 (sheet labels 2006 to 2010), of the ABS "Land mainly used for agriculture - Crops (ha)" per NRM region | `2006-10!B2 = AVERAGE(B13,B18,B21,B26,B31)`; year sheets 2009a, 2010a hold the ABS rows; Australia 305,997 km2 |
| Pasture | Mean of four years (2007 missing) of the ABS "Total grazing" (improved pasture plus other grazing land) | `2006-10!B3 = AVERAGE(B14,B22,B27,B32)`; 2008a: `(improved + other) x holding area`; 3,639,794 km2 |
| Infrastructure | Population x 730 m2 per person | `2006-10!B5 = B9*730/1000000`; 16,298 km2 = 22,326,388 x 730 m2; the same 730 is the model's infrastr2 default |
| Reserve | Protected area from CAPAD 2008, given to NRM regions by an overlay of IBRA 6.1 bioregions with the 2010 NRM regions (file from the Department, 10 Nov 2011); typed in as numbers | `Summary!B6:` hard-coded; no formula survives. The model's own total (1,811,007 km2) is 23.6% of land |
| Non-agricultural | The remainder: total - (cropping + pasture + infrastructure + reserve) | `Summary!B4 = B8-(SUM(B2,B3,B5,B6))` |
| Total area | The NRM 2011 polygon areas (Albers), Australia without Lord Howe, Christmas, Cocos and Jervis Bay | 55 of the 60 zones equal the polygon areas to within 1.5 km2 (`pipeline/land/zone_to_nrm2011.json`); Australia 7,687,574.6 against polygons 7,687,808.6 less those four areas (234.0) |

## What is not quite right in 2011

1. **Five zones carry older boundaries.** Desert Channels (+74,905 km2 against the 2011 polygon), SA Murray Darling Basin (+16,332), Alinytjara Wilurara (+11,322), Swan (+9,798; it appears to be the Swan region as drawn before the
   Perth boundary change, see `Land use/Swan-Perth boundary change.png`) and Northern and Yorke (+267) use the 2010 overlay areas, the same vintage as the ABS data for those regions. Each zone is consistent with its own ABS data; the regions do not add up to
   their state rows (Queensland regions sum to 4.3% more land than the Queensland row, South Australia 2.8%, Western Australia 0.4%). Capacity per zone is unaffected; sums of zones overcount.
   No alternate release is warranted: the zone figures are right for their own boundaries. Comparisons with new data on 2011 polygons will show a boundary effect in these five.
2. **Reserve is an estimate.** An IBRA-weighted version (overlap x the bioregion's protected share) reproduces only 7 of 53 zones within 5%; the 2011 numbers must have had adjustments I cannot see. On the
   current land-use raster, protected land (classes 1.1 nature conservation and 1.2 managed resource protection, which includes land held for traditional Indigenous uses) is the closest measured match:

   | Measure | National, km2 | Total absolute difference from 2011, as % of the national reserve |
   |---|---|---|
   | 2011 reserve | 1,811,007 | |
   | Class 1.1 alone | 866,651 | 55% |
   | 1.1 and 1.2.5 (Indigenous uses) | 1,888,841 | 14% |
   | 1.1 and 1.2 (all) | 1,968,328 | 16% |

   NT (651,251 against 649,720) and Alinytjara Wilurara (278,437 against 258,523) match to a few percent, which shows the 2011 reserve counted Aboriginal land. Classes 1.1 and 1.2 are used; the
   2008 to 2025 difference of 9% is not separable from the estimate's own error.
3. **Holdings and reserve overlap.** Cropping and grazing are ABS figures for agricultural holdings, which include pastoral leases on protected and Indigenous land, so cropping + pasture + reserve can exceed
   a small area. In 2011 the remainder was positive in every zone; in the present run 1,110 of 2,450 SA2s have a negative remainder but only one zone does (Northern and Yorke, -153 km2). Region figures must be checked
   for a negative remainder; where one occurs it will be shown as zero non-agricultural land and recorded in the release.

None of this changes the 2011 releases. If Murray prefers a corrected 2011 with consistent boundaries, it would replace the five totals by polygon areas and cannot also correct their cropping and pasture (the ABS
data for those regions are on the older boundaries), so it is not offered.

## The same method on current data

`pipeline/land/land_2011_method.py`: the same two ABS items (2020-21, the last year published below state level; SA2 sums equal the national figures exactly), infrastructure at 730 m2 per person on 2025
population, reserve and total area measured on the CLUM December 2023 raster, SA2 figures given to the 2011 zones through an SA2-by-zone overlay (a straddling SA2 divides its cropping and grazing in proportion to
cropping and grazing land in each part). Output: `data/sa2/land_2011_method_by_sa2.csv`, `data/nrm2011/land_2011_method_zones.csv` (all 60 zones, old and new side by side).

National, km2:

| | 2011 model | Current, 2011 method | Change |
|---|---|---|---|
| Cropping | 305,997 | 316,499 | +3% |
| Pasture | 3,639,794 | 3,318,689 | -9% |
| Reserve | 1,811,007 | 1,968,328 | +9% (see 2 above) |
| Infrastructure | 16,298 | 20,154 | +24% (population 22.3 to 27.6 million) |
| Non-agricultural | 1,914,478 | 2,063,387 | +8% |
| Total | 7,687,575 | 7,687,057 | -0.01% (the raster does not cover parts of the Torres Strait and a few small islands) |

The pasture fall is the ABS's: its grazing area for Australia was 364 Mha in 2008 and 332 Mha in 2020-21, after it changed its land-use categories in 2016. Zones with large changes (Desert Channels
5.7 times the cropping, SA Arid Lands 6.5 times) are in the table for D4; the five boundary zones above are expected to differ.
