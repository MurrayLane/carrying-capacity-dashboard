# What changed carrying capacity between the 2011 data and the 2025 data

SCOPE.md D4. `decompose.mjs` applies each cause alone to the 2011 data and then all together (release `2025-consumption`); the full table, both presets and all 60 zones, is `capacity_by_cause.csv`.
The method and the diet's food-group detail are the 2011 ones throughout, so each column is a data effect. Consumption means the six short-term defaults of `analysis/consumption_2025/` (meat and egg share, red meat share, fuel, biofuel,
timber, organic share); the long-term settings are scenarios and do not change. Population does not enter capacity; it changes whether a zone is over or under its capacity, shown in the last two columns (people divided by
capacity: above 1 is over capacity).

## Short-term settings (today's diet and production)

| Zone | 2011 | land only | crop yields only | livestock only | consumption only | all 2025 | people 2011 | people 2025 | people / capacity 2011 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Australia | 40,450,144 | 37,266,007 | 40,655,584 | 46,760,459 | 44,493,806 | 47,450,080 | 22,326,388 | 27,608,200 | 0.552 | 0.582 |
| NSW-ACT | 10,038,535 | 9,042,250 | 10,138,583 | 11,950,743 | 10,984,062 | 11,849,176 | 7,454,854 | 9,076,673 | 0.743 | 0.766 |
| Victoria | 5,986,079 | 5,373,415 | 6,184,270 | 7,024,194 | 6,333,450 | 6,875,788 | 5,419,900 | 7,073,857 | 0.905 | 1.029 |
| Queensland | 6,228,219 | 6,510,613 | 7,162,302 | 7,231,357 | 6,184,037 | 8,733,807 | 3,908,395 | 5,669,806 | 0.628 | 0.649 |
| South Australia | 2,070,223 | 1,888,847 | 2,072,755 | 2,412,496 | 2,221,336 | 2,355,076 | 1,311,000 | 1,902,338 | 0.633 | 0.808 |
| Western Australia | 3,697,385 | 3,272,434 | 3,704,316 | 3,729,209 | 3,962,367 | 3,521,010 | 1,889,000 | 3,044,382 | 0.511 | 0.865 |
| Tasmania | 225,920 | 222,689 | 247,328 | 253,377 | 243,453 | 300,123 | 474,000 | 576,261 | 2.098 | 1.920 |
| Northern Territory | 33,429 | 30,074 | 35,304 | 61,547 | 30,463 | 60,666 | 229,711 | 264,883 | 6.872 | 4.366 |

## Long-term settings

| Zone | 2011 | land only | crop yields only | livestock only | consumption only | all 2025 | people 2011 | people 2025 | people / capacity 2011 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Australia | 9,431,487 | 9,755,181 | 11,808,166 | 9,448,739 | 9,431,487 | 12,241,414 | 22,326,388 | 27,608,200 | 2.367 | 2.255 |
| NSW-ACT | 1,609,575 | 1,751,795 | 1,935,744 | 1,611,118 | 1,609,575 | 2,109,213 | 7,454,854 | 9,076,673 | 4.632 | 4.303 |
| Victoria | 539,589 | 550,703 | 803,227 | 539,794 | 539,589 | 820,233 | 5,419,900 | 7,073,857 | 10.044 | 8.624 |
| Queensland | 516,284 | 539,693 | 702,650 | 519,956 | 516,284 | 741,638 | 3,908,395 | 5,669,806 | 7.570 | 7.645 |
| South Australia | 830,042 | 760,010 | 858,486 | 838,377 | 830,042 | 881,444 | 1,311,000 | 1,902,338 | 1.579 | 2.158 |
| Western Australia | 2,105,909 | 1,863,871 | 2,133,372 | 2,053,184 | 2,105,909 | 1,840,302 | 1,889,000 | 3,044,382 | 0.897 | 1.654 |
| Tasmania | 24,414 | 24,065 | 28,248 | 24,444 | 24,414 | 27,884 | 474,000 | 576,261 | 19.415 | 20.666 |
| Northern Territory | 3,722 | 3,348 | 4,683 | 5,324 | 3,722 | 6,836 | 229,711 | 264,883 | 61.717 | 38.748 |

## Reading it

* **Short term, Australia: 40.5 to 47.5 million.** Less pasture on holdings (the ABS grazing area fell 9%, partly a change of its land-use categories) takes 3.2 million off. Crop yields add 0.2 million: crops hardly bind the
  short-term result. Livestock adds 6.3 million: red meat is more than four fifths of the land in the short-term diet, and the cattle and sheep meat produced per animal and per hectare of grazing rose. Consumption adds
  4.0 million: Australians eat less beef (down a third a head) and slightly less meat overall. The causes do not add up (interaction -0.4 million) because they act on the same land.
* **Long term, Australia: 9.4 to 12.2 million.** Crop yields are the cause: 2.4 million of the 2.8 million. Wheat, barley and canola yields roughly doubled against the drought years of 2006-2010, and the long-term
  diet is cropping-land limited. Land adds 0.3 million; livestock and consumption do nothing here (the long-term settings are scenarios).
* **Population 22.3 to 27.6 million.** Today's population is 55% of the short-term capacity in 2011 and 58% now; against the long-term capacity it is 2.4 times in 2011 and 2.3 times now. Capacity grew about as fast as the
  population in the short term.
* **Caveats that matter more than the third digit.** Three years of crop data (2022-25), two of them very good winter-crop years; a five-year meat window that ends in two years of heavy slaughter; wool, milk and feedlot
  grain placeholders; vegetables, fruit and nuts carried at their 2016-21 group factor; the five zones of older boundaries (`analysis/land_2011/README.md`); organic share the least certain default. Each should be re-run with
  the alternative choice before the figures go on a page (see the note on sensitivity runs in SCOPE.md D4).
