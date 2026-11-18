# The widened draws for every zone (B132, X140 fixed)

2000 Latin hypercube draws of 19 choices (`MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 MC_ZONES=all`, seed 20261027), all 60 zones, short and long term. Ranges: `results/ranges_2025-fixed_wide_zones.csv`.

Zone 45 (Northern and Yorke): the land_raster draw uses the raster cropping and pasture on the release land total (non-agricultural land 3,911 to 4,063 km2; the holdings land of the release is 152 km2 larger than the raster build, X140). Only the zone 45 columns are affected; every national and state column equals the earlier widened draws to the person.

**Zones under capacity at the base whose 5th percentile is below their population (17 of 74 zone-and-term rows with a 5th percentile below the population; the others are over capacity at the base already):**

| Zone | Name | Kind | Term | p5 | Base | Population | p5 over population |
|---|---|---|---|---|---|---|---|
| 2 | NSW-ACT | state | short | 7,956,910 | 10,566,157 | 9,076,673 | 0.877 |
| 22 | North East Vic | region | short | 102,805 | 129,164 | 114,355 | 0.899 |
| 32 | Desert Channels | region | short | 2,666 | 92,671 | 10,875 | 0.245 |
| 32 | Desert Channels | region | long | 867 | 26,847 | 10,875 | 0.080 |
| 34 | Mackay Whitsunday | region | short | 135,581 | 199,114 | 153,841 | 0.881 |
| 35 | Northern Gulf | region | long | 6,909 | 33,553 | 9,846 | 0.702 |
| 38 | Southern Gulf | region | short | 3,555 | 46,690 | 27,303 | 0.130 |
| 39 | Wet Tropics | region | short | 232,918 | 315,100 | 285,138 | 0.817 |
| 40 | SA | state | short | 1,677,253 | 2,055,085 | 1,902,338 | 0.882 |
| 44 | Kangaroo Island | region | long | 4,591 | 5,222 | 5,212 | 0.881 |
| 45 | Northern and Yorke | region | long | 83,415 | 94,288 | 92,250 | 0.904 |
| 46 | SA Arid Lands | region | long | 3,122 | 8,217 | 8,049 | 0.388 |
| 47 | SA Murray Darling Basin | region | long | 133,828 | 150,674 | 145,343 | 0.921 |
| 49 | WA | state | short | 2,548,963 | 3,110,186 | 3,044,382 | 0.837 |
| 52 | Rangelands | region | short | 24,757 | 167,279 | 157,948 | 0.157 |
| 54 | South West WA | region | long | 385,254 | 431,529 | 399,099 | 0.965 |
| 57 | North Tasmania | region | short | 148,681 | 187,593 | 156,393 | 0.951 |

All rows with a 5th percentile below the population: short term 28, long term 46 (of 60 zones each; Australia, the seven states and the 52 regions, the Northern Territory counted once as zone 60).
