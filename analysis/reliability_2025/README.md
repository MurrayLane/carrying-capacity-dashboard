# Capacity year by year (SCOPE.md E10)

Release `2025-organic` uses a three-year window of crop data and a five-year window of herd and meat data. This re-runs the result for each single ABS crop year there is data for
(2016-17 to 2020-21 and 2022-23 to 2024-25; the ABS cubes have no 2021-22), each with THAT year's crops, herds and meat, to see how much the answer depends on the weather and the herd cycle.
Land, population, diet and every other default are those of the release. Build: `python3 -I analysis/reliability_2025/build_years.py WORK_DIR ABS_DIR`, then
`node analysis/sensitivity_2025/evaluate.mjs WORK_DIR/years.json analysis/reliability_2025/years.csv`, then `python3 analysis/reliability_2025/write_readme.py`. Capacity in millions of people.

## Short term (today's diet)

| Crop, herd and meat year | Australia | NSW and ACT | Victoria | Queensland | South Australia | Western Australia | Tasmania | Northern Territory |
|---|---|---|---|---|---|---|---|---|
| 3-year window (the release) | 48.0 | 11.99 | 6.96 | 8.84 | 2.38 | 3.56 | 0.30 | 0.06 |
| 2016-17 | 46.0 | 11.77 | 7.01 | 8.68 | 2.42 | 3.70 | 0.31 | 0.04 |
| 2017-18 | 48.8 | 11.39 | 7.26 | 6.49 | 2.49 | 3.78 | 0.31 | 0.01 |
| 2018-19 | 48.8 | 10.53 | 6.93 | 6.00 | 2.42 | 3.92 | 0.28 | 0.03 |
| 2019-20 | 48.3 | 10.36 | 7.34 | 6.54 | 2.46 | 3.94 | 0.28 | 0.02 |
| 2020-21 | 43.5 | 10.55 | 6.90 | 7.88 | 2.29 | 3.52 | 0.32 | 0.06 |
| 2022-23 | 45.7 | 11.73 | 6.86 | 9.03 | 2.31 | 3.46 | 0.31 | 0.07 |
| 2023-24 | 51.8 | 13.11 | 7.23 | 8.74 | 2.52 | 3.67 | 0.30 | 0.02 |
| 2024-25 | 55.4 | 13.49 | 7.23 | 8.86 | 2.50 | 3.74 | 0.30 | 0.02 |
| lowest year | 43.5 | 10.36 | 6.86 | 6.00 | 2.29 | 3.46 | 0.28 | 0.01 |
| median of the years | 48.5 | 11.56 | 7.12 | 8.28 | 2.44 | 3.72 | 0.30 | 0.03 |
| highest year | 55.4 | 13.49 | 7.34 | 9.03 | 2.52 | 3.94 | 0.32 | 0.07 |

## Long term (low-meat, 100% organic, no avoidable waste)

| Crop, herd and meat year | Australia | NSW and ACT | Victoria | Queensland | South Australia | Western Australia | Tasmania | Northern Territory |
|---|---|---|---|---|---|---|---|---|
| 3-year window (the release) | 12.3 | 2.13 | 0.82 | 0.75 | 0.89 | 1.86 | 0.03 | 0.01 |
| 2016-17 | 13.8 | 2.55 | 0.93 | 0.83 | 0.94 | 1.96 | 0.03 | 0.01 |
| 2017-18 | 11.8 | 2.04 | 0.74 | 0.56 | 0.94 | 1.96 | 0.03 | 0.00 |
| 2018-19 | 10.4 | 1.64 | 0.60 | 0.50 | 0.84 | 2.00 | 0.03 | 0.00 |
| 2019-20 | 10.5 | 1.73 | 0.68 | 0.64 | 0.88 | 2.00 | 0.03 | 0.00 |
| 2020-21 | 13.0 | 2.34 | 0.86 | 0.74 | 0.88 | 1.87 | 0.03 | 0.01 |
| 2022-23 | 13.8 | 2.32 | 0.94 | 0.76 | 0.89 | 1.84 | 0.03 | 0.01 |
| 2023-24 | 13.0 | 2.29 | 0.84 | 0.77 | 0.89 | 1.87 | 0.03 | 0.00 |
| 2024-25 | 11.7 | 1.93 | 0.78 | 0.73 | 0.72 | 1.84 | 0.03 | 0.00 |
| lowest year | 10.4 | 1.64 | 0.60 | 0.50 | 0.72 | 1.84 | 0.03 | 0.00 |
| median of the years | 12.4 | 2.16 | 0.81 | 0.73 | 0.89 | 1.91 | 0.03 | 0.00 |
| highest year | 13.8 | 2.55 | 0.94 | 0.83 | 0.94 | 2.00 | 0.03 | 0.01 |

## What it shows

* **Australia, short term: 43.5 to 55.4 million across the eight years (median 48.5); the release says 48.0.** Lowest 2020-21, highest 2024-25. The release sits in the middle of the years.
* **Australia, long term: 10.4 to 13.8 million (median 12.4); the release says 12.3.** Lowest 2018-19, highest 2016-17.
* **Every single year is above 2011** (40.5 million short term, 9.4 long term), including the 2018-19 drought for the long term. The statement that capacity has risen does not depend on which years are chosen.
* **The two settings are driven by different things.** The long term follows the crop weather: its lowest year (2018-19) is a drought year and the field-crop group factor for that year is 1.03, against 1.70 in the record year 2022-23. The short term follows the herd cycle: cattle meat produced was 2.10 million tonnes in 2020-21 (herd rebuilding) and 3.00 million tonnes in 2024-25 (heavy slaughter) with almost the same beef herd (0.993 and 1.04 of its 2009-10 size), and red meat is most of the land in today's diet.
  A year of heavy slaughter is not a year the land can sustain, so the top of the short-term range is a high estimate, not a typical one. The five-year meat window of the release is there to smooth this.
* **States move more than the nation.** Queensland's short-term figure runs from 6.0 to 9.0 million and the Northern Territory's by a factor of several; the herd and drought cycles do not coincide across states.

## Limits

* Eight years is too few to name a 1-in-10 year. The lowest of eight is a rough guide to a bad year, not a probability.
* Crops the ABS does not report take a group factor made from that year's reported crops (30 crops in 2016-21, 12 to 15 in 2022-25). The vegetable, fruit and nut factors are therefore smoother than the weather they stand for; the real year-to-year range is a little wider than shown.
* Only the national and state zones are evaluated: the 2016-21 cubes are on NRM boundaries that were not allocated to the 2011 zones.
* Years 2016-17 to 2019-20 use the 2020-21 land layer and the 2025 population; feed grain for the animals comes from that year's national yields.
