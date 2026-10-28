# What changed carrying capacity between the 2011 data and the 2025 data

SCOPE.md D4. `decompose.mjs` applies each cause alone to the 2011 data and then all together (release `2025-fuel`, the tip of the 2025 chain); the full table, both presets and all 60 zones, is `capacity_by_cause.csv`; this file is written from it by `write_readme.py`.
The method and the diet's food-group detail are the 2011 ones throughout, so each column is a data effect. Consumption means five of the six short-term defaults of `analysis/consumption_2025/` (meat and egg share, red meat share, fuel, biofuel,
timber); the long-term settings are scenarios, but two have been updated: the resilience table behind the 100-year setting (`analysis/resilience_2025/`) and the long-term liquid fuel (`analysis/fuel_sectors_2025/`), each a column of its own. The organic update (E5, `analysis/organic_2025/`) is its own column: the organic share and its baseline constant, and new factors for five crops. Population does not enter capacity; it changes whether a zone is over or under its capacity, shown in the last two columns (people divided by
capacity: above 1 is over capacity).

## Short-term settings (today's diet and production)

| Zone | 2011 | land only | crop yields only | livestock only | consumption only | organic update only | resilience table only | fuel only | all 2025 | people 2011 | people 2025 | people / capacity 2011 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Australia | 40,450,144 | 37,266,007 | 40,655,584 | 46,760,459 | 45,014,462 | 40,450,144 | 40,450,144 | 40,450,144 | 48,004,473 | 22,326,388 | 27,608,200 | 0.552 | 0.575 |
| NSW-ACT | 10,038,535 | 9,042,250 | 10,138,583 | 11,950,743 | 11,113,278 | 10,038,535 | 10,038,535 | 10,038,535 | 11,988,169 | 7,454,854 | 9,076,673 | 0.743 | 0.757 |
| Victoria | 5,986,079 | 5,373,415 | 6,184,270 | 7,024,194 | 6,409,134 | 5,986,079 | 5,986,079 | 5,986,079 | 6,957,230 | 5,419,900 | 7,073,857 | 0.905 | 1.017 |
| Queensland | 6,228,219 | 6,510,613 | 7,162,302 | 7,231,357 | 6,263,482 | 6,228,219 | 6,228,219 | 6,228,219 | 8,844,712 | 3,908,395 | 5,669,806 | 0.628 | 0.641 |
| South Australia | 2,070,223 | 1,888,847 | 2,072,755 | 2,412,496 | 2,247,270 | 2,070,223 | 2,070,223 | 2,070,223 | 2,382,576 | 1,311,000 | 1,902,338 | 0.633 | 0.798 |
| Western Australia | 3,697,385 | 3,272,434 | 3,704,316 | 3,729,209 | 4,008,597 | 3,697,385 | 3,697,385 | 3,697,385 | 3,562,059 | 1,889,000 | 3,044,382 | 0.511 | 0.855 |
| Tasmania | 225,920 | 222,689 | 247,328 | 253,377 | 246,484 | 225,920 | 225,920 | 225,920 | 303,775 | 474,000 | 576,261 | 2.098 | 1.897 |
| Northern Territory | 33,429 | 30,074 | 35,304 | 61,547 | 30,815 | 33,429 | 33,429 | 33,429 | 61,378 | 229,711 | 264,883 | 6.872 | 4.316 |

## Long-term settings

| Zone | 2011 | land only | crop yields only | livestock only | consumption only | organic update only | resilience table only | fuel only | all 2025 | people 2011 | people 2025 | people / capacity 2011 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Australia | 9,431,487 | 9,755,181 | 11,808,166 | 9,448,739 | 9,431,487 | 9,472,527 | 9,431,482 | 10,775,555 | 14,054,716 | 22,326,388 | 27,608,200 | 2.367 | 1.964 |
| NSW-ACT | 1,609,575 | 1,751,795 | 1,935,744 | 1,611,118 | 1,609,575 | 1,618,771 | 1,609,577 | 1,844,742 | 2,441,231 | 7,454,854 | 9,076,673 | 4.632 | 3.718 |
| Victoria | 539,589 | 550,703 | 803,227 | 539,794 | 539,589 | 542,088 | 539,588 | 622,930 | 945,426 | 5,419,900 | 7,073,857 | 10.044 | 7.482 |
| Queensland | 516,284 | 539,693 | 702,650 | 519,956 | 516,284 | 520,259 | 516,285 | 597,347 | 864,060 | 3,908,395 | 5,669,806 | 7.570 | 6.562 |
| South Australia | 830,042 | 760,010 | 858,486 | 838,377 | 830,042 | 841,947 | 817,476 | 856,565 | 890,827 | 1,311,000 | 1,902,338 | 1.579 | 2.135 |
| Western Australia | 2,105,909 | 1,863,871 | 2,133,372 | 2,053,184 | 2,105,909 | 2,130,763 | 2,017,662 | 2,126,839 | 1,798,524 | 1,889,000 | 3,044,382 | 0.897 | 1.693 |
| Tasmania | 24,414 | 24,065 | 28,248 | 24,444 | 24,414 | 24,733 | 24,270 | 28,722 | 33,017 | 474,000 | 576,261 | 19.415 | 17.453 |
| Northern Territory | 3,722 | 3,348 | 4,683 | 5,324 | 3,722 | 3,609 | 3,666 | 4,121 | 7,381 | 229,711 | 264,883 | 61.717 | 35.888 |

## Reading it

* **Short term, Australia: 40.5 to 48.0 million.** Less pasture on holdings (the ABS grazing area fell 9%, partly a change of its land-use categories) takes 3.2 million off. Crop yields add 0.2 million: crops hardly bind the
  short-term result. Livestock adds 6.3 million: red meat is more than four fifths of the land in the short-term diet, and the cattle and sheep meat produced per animal and per hectare of grazing rose. Consumption adds
  4.6 million: Australians eat less beef (down a third a head) and slightly less meat overall. The causes do not add up (interaction -0.3 million) because they act on the same land.
* **Long term, Australia: 9.4 to 14.1 million.** Crop yields are the largest cause: 2.4 million of the 4.6 million. Wheat, barley and canola yields roughly doubled against the drought years of 2006-2010, and the long-term
  diet is cropping-land limited. Land adds 0.3 million; the organic update changes the long-term result by +0.04 million (the long-term diet is 100% organic); the resilience table, updated to 2024-25, by -0.00 million (on the 2011 data; Australia's 100-year factor is unchanged, the states differ); the re-derived long-term fuel (210 L, the thesis method on current sector use) by +1.34 million; livestock and consumption do nothing here (the long-term settings are scenarios).
* **Population 22.3 to 27.6 million.** Today's population is 55% of the short-term capacity in 2011 and 57% now; against the long-term capacity it is 2.367 times in 2011 and 1.964 times now.
* **Caveats that matter more than the third digit.** Three years of crop data (2022-25), two of them very good winter-crop years; a five-year meat window that ends in two years of heavy slaughter; wool, milk and feedlot
  grain placeholders; vegetables, fruit and nuts carried at their 2016-21 group factor; the five zones of older boundaries (`analysis/land_2011/README.md`); organic share the least certain default. Each has been re-run with
  the alternative choice: `analysis/sensitivity_2025/README.md` ranks the effects.
