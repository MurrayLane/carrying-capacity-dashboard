# Yields from the newest ABS data (2022-23 to 2024-25) and the group-trend rule

Release `2025` of SCOPE.md B9. This folder holds the crop layer only: SA2 cubes, national and state yields, and the rule for crops the ABS does not report.
It does not yet make a model release: that needs the display regions (B0a), land (B1), population (B2) and the livestock inputs (B12).

| File | What |
|---|---|
| `build_recent_cubes.py` | ABS Data API tables to cubes in the pipeline's layout: `data/abs-2022-25/` (Australia, 9 states and territories, 2,000+ SA2s; three years) |
| `recent_yields.py` | Stage 1 and 2 on national and state columns for both windows, against the model's 2006-2010 yields; writes `data/abs-2022-25/national_state_yields.csv` and `group_trend.json` |
| `group_trend.py`, `groups.json` | The rule of SCOPE.md B10 and the four crop groups |
| `test_recent.py` | Rule tests, and checks of the committed cubes against the ABS's published state tables |

## What the data supports

Twelve crops have area and production in 2022-25: wheat, oats, barley, sorghum, maize, rice, sugar cane, canola, chickpeas, faba beans, field peas,
lentils; and three horticultural crops: avocados, bananas (not 2022-23), macadamias. Cotton has area only; triticale, soybeans, sunflower, mung beans,
peanuts and wine grape area are not published. Every vegetable, fruit and nut row except those three has no area after 2020-21.

National yield, t/ha, before the zero-irrigation conversion (model 2006-10 | 2016-21 | 2022-25):

| Crop | 2006-10 | 2016-21 | 2022-25 |
|---|---|---|---|
| Wheat | 1.37 | 1.98 | 2.80 |
| Barley | 1.56 | 2.30 | 2.98 |
| Oats | 1.25 | 1.56 | 1.35 |
| Canola | 1.03 | 1.38 | 1.97 |
| Sorghum | 3.03 | 2.46 | 3.74 |
| Maize | 5.35 | 6.60 | 5.88 |
| Rice | 10.2 | 9.5 | 11.2 |
| Sugar cane | 69.9 | 85.5 | 91.7 |
| Chickpeas | 1.02 | 1.03 | 2.32 |
| Lentils | 0.72 | 1.64 | 1.52 |
| Field peas | 0.83 | - | 0.67 |
| Field beans | 1.05 | - | 1.47 |

2022-23 was a record winter-crop year and 2023-24 a poor one; three years are a short window (B9). All figures are full-year, after the seed deduction.

## The group-trend rule (B10)

Every crop without a usable figure in a window keeps its 2006-2010 regional pattern and its national level moves by its group's factor: the median change
since 2006-2010 of the group's reported crops. A group needs at least three reported crops for its own factor (a median of one or two crops is one crop's
luck); below that, the latest earlier factor is carried forward and marked.

| Group | 2016-21 | 2022-25 |
|---|---|---|
| Field crops | 1.29 (12 crops) | 1.36 (12 crops) |
| Vegetables | 1.12 (18 crops) | 1.12, carried from 2016-21 (no area published) |
| Fruit | 1.02 (15 crops) | 1.02, carried (only avocados and bananas reported) |
| Nuts | 1.00 (2 crops, below the minimum) | 1.00, carried (macadamias only) |

Two things to know. Vegetables and fruit are therefore not updated by anything after 2020-21 beyond what the Hort Innovation tonnes show; they are a
stated carry-forward, not a measurement. And the measured error of this rule on held-out crops (`analysis/recent_data/`) is lower than keeping the old yield
for field crops only.

## Differences of method between windows

* 2006-2010 and 2016-21 convert tree counts to hectares at a recorded density; 2022-25 uses the ABS's total crop area. Avocados and macadamias are not
  like for like across the two, which is why their 2022-25 figures are not used for a group factor.
* 2022-25 production is levied production. At national level it matches the ABS published production (checked in `test_recent.py`).
* 2022-25 has no reliability symbols; cells under 10 ha or 10 t are removed, the thesis minimum, as for 2020-21.

## The regional matrix (`zone_yields.py`)

`data/2025/yield_matrix.csv` holds the 135 rows of the model's Yield sheet for the 60 zones of 2011, and `yield_provenance.csv` says how each of the 8,100 cells was made. SA2 area and production go
to the zones by the share of cropland in each part of a straddling SA2 (`pipeline/land/zones` overlay); the national and state zones take the ABS national and state figures. Then the pipeline's own
stages: the thesis thresholds of 10 ha and 10 t, the three-year mean, the fill of the marked pairs, the zero-irrigation conversion.

Two rules are additions for the levy-based data, because the ABS attributes levied production to where the levy is paid, not where the crop grew (Queensland canola: 8.2 t/ha in 2022-23 on 5,823 ha):
a zone yield over three times or under a tenth of the national yield of the same year is removed (the tenth is the thesis's own lower limit for thin data), and so is a yield at or below zero after the seed
deduction (Queensland oats). 84 of about 1,150 zone-years are removed, 17 of them by the seed rule. Without them, Queensland's long-term capacity rose more than sixfold on one canola figure.

| How a cell was made | Cells |
|---|---|
| Observed 2022-25 (the 15 reported crops) | 455 |
| Filled (marked pair, national x the zone's major-crops factor) | 86 |
| 2011 yield x the crop's own national change (zone has no 2022-25 figure) | 138 |
| 2011 yield x the group factor: vegetables 3,000, fruit 1,980, field crops 780, nuts 480 | 6,240 |
| Carried from 2011 (animal products, honey, wild fish, timber) | 960 |
| No figure | 221 |

## Animal products (`livestock_zone.py`, release `2025-livestock`)

The 2011 livestock method (`livestock.py`: land shared among a zone's animals by dry sheep equivalent, product over its share of the land; poultry, pigs and fish from feed grain over a conversion ratio) on
inputs built as follows. No open source gives class counts below state level after 2020-21 (TableBuilder, ABARES and MLA checked, `analysis/recent_data/README.md`), so:

* **Class counts:** the 2010 counts of each zone (the latest year of the archive; its classes add up to the ABS flock and herd of that year) times the change of the state's sheep, beef cattle and dairy cattle
  totals from 2009-10 to each of 2020-21 to 2024-25 (ABS Australian Agriculture: Livestock series). The mix inside each species is the 2010 mix.
* **Grazing land:** the 2020-21 ABS figure (the land layer's pasture). **Feed grain:** the new crop yields.
* **National meat:** ABS Livestock Products, tonnes produced in each year to June, calibrated to the archive's 2010 figure (cattle x1.086, sheep and lamb x1.155; the archive's source is unrecorded).
* **Placeholders:** wool, milk and feedlot grain follow the flock and herd. Murray can replace them with national wool and milk production (ABARES, AWI, Dairy Australia) and the ALFA feedlot survey; the
  ABS publishes none of them.

National yield change, 2011 to 2025: sheep meat +43%, cattle meat +11%, wool +3% and milk +3% (placeholders), poultry, pigs and eggs +53% (feed grain: the crop yields rose), fish +37%.
Cattle and sheep meat produced rose sharply in 2023-24 and 2024-25 (herd contraction); the five-year mean takes the edge off this, but the result is sensitive to the window.
