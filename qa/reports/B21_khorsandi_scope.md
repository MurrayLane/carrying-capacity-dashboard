# B21: scoping an eighth method test, Khorsandi et al. 2022 on Australian 2025 data (decision 24)

Scoping only. Nothing was run and no analysis file was made. Page numbers are the printed page of each article (Khorsandi 2022 is pages 1 to 10 of Science of the Total Environment 817: 153038; Khorsandi 2023 is pages 1 to 10 of Heliyon 9: e15079).

## What was read
* Full text of both papers, from the open-access copies at the Wageningen repository (https://edepot.wur.nl/563369 for 2022; https://edepot.wur.nl/629497 for 2023). The publisher PMC page for 2023 was behind a bot check and was not used.
* Not reached: the supplementary Appendix A of 2022 (Tables A1 to A7: data sources, the Mesgaran suitability parameters, per-unit results) and the authors' Google Earth Engine code (github.com/mostafakhorsandi/WRCC, named in 2023 p.2; GitHub access was not enabled for this session). Where a constant would sit in those, this report says so.
* Repository side: the Khorsandi section of `qa/reports/B17_reading.md`; `analysis/method_tests_2025/README.md` (opening, the Cassidy section, the cross-method table) and `cassidy_people_per_hectare.py`; `analysis/scale_curve_2025/README.md`; `analysis/gaez_2025/`; `data/sa2/`; `analysis/SOURCES.md`; `analysis/irrigation_review/README.md`.

## 1. The method, step by step

**What it answers.** "How many people can be fed in Iran, self-sufficiently?" (2022 p.2). No trade by assumption, no social limit; K is biophysical, "optimistic" throughout (2022 p.3, p.10).

**Step 1. Land suitability (the land bound).** A suitability index SI from 0 to 1 is built for every cell by replicating Mesgaran et al. 2017, from soil, climate and topography layers (2022 p.5 to 6). For each variable the score is 0 at or below its minimum, rises linearly to 1 at its lowest optimum value, and is 1 above (Eq. 3, p.6); the parameters come from Mesgaran 2017 and sit in the supplement (not reached). The index does not use water explicitly (p.7). Land with SI above a threshold is the productive area A.

**Step 2. Theoretical capacity at unlimited yield.** K = A / B, from Eq. 9 on p.6 (the limit of Franck et al. 2011, Eq. 8, as yield per area goes to infinity). B is the infrastructure area each person occupies and cannot farm: **1,500 m2** (Franck et al. 2011; De Wit's lowest value was 750 m2) (p.6; used in 2022 p.7 and 2023 p.5). The food requirement n drops out when yield is unlimited; the bound is land only.

**Step 3. Water bound (what sets A).**
* Maximum level of water consumption for a hydrological unit, MLWC = X17 − X21 (net water consumption minus excessive water use), from the Iran Ministry of Energy's 23-variable water cycle (Eq. 2, p.5; Appendix Fig. A1). Allocating this much means turning all possible blue water into green water (p.5).
* Actual evapotranspiration (AET) is taken from TerraClimate for the land with SI above a trial threshold (p.3 to 4). AET rises linearly as the threshold falls below 0.4 (Fig. 2, p.4). The threshold SIBalance is found, unit by unit, by solving AET = MLWC, "in a trial and error manner" (p.3).
* Iran as one unit (L0): SIBalance = 0.074, A = 195,304.95 km2, AET from A = 62.64 BCM against available water 61.62 BCM (p.7; Table 2, p.8). The same search is repeated in each smaller unit (p.7).

**Step 4. Realistic yield through HANPP (the third bound).**
* HANPP is 25% of net primary production (NPP), "at all spatial scales" (p.7; range 20 to 30% from Vitousek 1986 and Haberl 2014).
* NPP is the MODIS product at 250 m (p.4; the pixel size is as the paper states it).
* One gram of carbohydrate gives 4 kcal (De Wit 1967; p.7).
* Food need is **3,000 kcal a person a day** (p.6, p.8); the paper notes FAO figures of 2,100 (India) to 3,500 (United States) and the EAT-Lancet 2,500, and chose 3,000 for Iran.
* K = (HANPP summed over A, in kcal a day) / n (2023 Eq. 3, p.2). The 2022 text states the idea (p.6, p.7); the exact expression with B is in the supplement (not reached). Note on the arithmetic: the 35.49 million of scenario 7 over A = 195,305 km2 and 3,000 kcal a day implies about 50 g of dry matter a square metre a year as HANPP (about 200 g of NPP), by my arithmetic and ignoring B; it is a plausibility figure, not stated by the authors.

**Step 5. Four scales.** L0 nation (1 unit), L1 main basins (6), L2 main sub-basins (30), L3 ministry study areas (609) (p.5). K is computed in each unit and summed. With one unit the water is pooled across the country (perfect internal trade); with 609 units each unit lives on its own water (p.7).

**Step 6. Nine scenarios** (Table 1, p.3; values Table 3, p.8):

| No. | Land rule | Yield | Water | K (people) |
|---|---|---|---|---|
| 1 | SI > 0 | unlimited | none | 165,869,730 |
| 2 | SI > SIBalance | unlimited | national pool | 130,203,303 |
| 3 | SI > 0.2 | unlimited | none | 68,064,206 |
| 4 | SI > 0.4 | unlimited | none | 11,431,186 |
| 5 | SI > 0.6 | unlimited | none | 2,591,962 |
| 6 | SI > 0.8 | unlimited | none | 868,150 |
| 7 | SI > SIBalance | 25% of NPP | national pool | 35,491,273 |
| 8 | varied locally | 25% of NPP | local (609 units) | 20,217,020 |
| 9 | 2020 land cover (ESRI, 10 m): cropland 148,434 km2, AET 55.3 BCM | (observed) | beyond the limit, groundwater deficit | (current population 83,992,953) |

By scale (Table 2, p.8): theoretical K 130.2, 115.3, 98.4, 76.8 million at L0, L1, L2, L3; HANPP K 35.5, 27.7, 24.2, 20.2 million. So summing local units falls to 59% (theoretical) and 57% (HANPP) of the national figure.

**Step 7. The time series.** K(t) from observed MODIS NPP 2001 to 2020 is set against UN population (p.4, p.6 Fig. 5); this gives the "overshoot and collapse" reading and is not part of a static capacity.

**The 2023 simple form (Heliyon).** Two things, both stated on pages 2 to 7:
* Eq. 2 and Eq. 3 restate the two methods: K1 = A/B (B = 1,500 m2, p.5) and K2 = integral of HANPP over A divided by n.
* A meta-model that relates K to the representative area of a scale: **K = a ln(A) + b** (Eq. 4, p.4), where A is the mean suitable area per unit at that scale (so one unit at L0, 6, 30, 609 units at L1 to L3; L3 mean 189.05 km2, p.6). Fitted: **K1 = 8 x 10^6 ln(A) + 3 x 10^7** (Eq. 5) and **K2 = 2 x 10^6 ln(A) + 8 x 10^6** (Eq. 6) (p.7). With A in square kilometres these give 127.5 and 32.4 million at L0 (A = 195,305) and 71.9 and 18.5 million at L3, against 130.2, 35.5, 76.8 and 20.2 (my arithmetic; the unit of A is not printed beside the equations, but square kilometres fits).
* Read-outs: the lines meet the K = 0 axis at 1.12 local hectares per person (method 1) and 2.31 (method 2), and meet each other at 0.85 ha, which the authors turn into a 92 m cell size (p.8 to 10). These are interpretations of a fitted line, not measurements.
* The logarithm is read as diminishing returns (p.9). It is a curve fitted to four points; the authors give no goodness of fit in the text.

## 2. What the method needs, and what the repository holds

| Need | Status | Where or from what |
|---|---|---|
| Land area by unit (SA2, SA3, SA4, state, NRM region, nation) | On hand | `data/sa2/land_types_by_sa2.csv` (cropping, pasture, nature, infrastructure, non-agricultural km2), `land_2011_method_by_sa2.csv`, and the region totals in `web/public/data/<release>/regions.json` and `data/2025-land/default-inputs-*.csv` |
| Suitable land (the SI bound) | Partly on hand | `data/sa2/arable_share_gaez_by_sa2.csv` (temperate: wheat, barley, rapeseed) and `arable_share_gaez_broad_by_sa2.csv` (ten field crops), each the share of an SA2 whose GAEZ v4 cells are very suitable, suitable or moderately suitable, rainfed, high input, 1981 to 2010 (`analysis/gaez_2025/arable_share_by_sa2.py`). This is a share in one class band, not Mesgaran's continuous SI, so thresholds of 0.2, 0.4, 0.6 and 0.8 cannot be cut from it. The GAEZ rasters are not stored; the script reads them from a folder. To be obtained for a threshold series: GAEZ v4 suitability and attainable-yield rasters (FAO, public), or Mesgaran's inputs (SoilGrids, a climate set, SRTM) plus the parameters in the Mesgaran 2017 paper |
| Population by unit (for the scale curve and for comparing K with people) | On hand | `data/sa2/population_erp.csv` (2011 to 2025), region populations in the release data |
| Per-person infrastructure area B | Derivable | A constant (1,500 m2 in the paper). The model's own settings carry a per-person infrastructure setting (730 in `data/2025-land/default-inputs-short-term.csv`; units not checked here), so the two can be set side by side |
| Daily food need n | On hand | A constant (3,000 kcal; the repository's Cassidy test uses 2,700, `cassidy_people_per_hectare.py` line 34) |
| NPP (annual, gridded) | To be obtained | MODIS MOD17A3HGF (NASA; annual NPP, public but needs an Earthdata login), or the same through Google Earth Engine or AppEEARS; an Australian alternative is the CSIRO or TERN products built on MODIS. Nothing in the repository holds NPP |
| Actual evapotranspiration on the suitable land | To be obtained | TerraClimate AET (the paper's own source, global, about 4 km, public); or the Bureau of Meteorology AWRA-L landscape model (Australia only) |
| Available water per unit (the Australian meaning of MLWC) | To be obtained and defined | There is no single Australian number for "maximum sustainable consumption" per unit. Candidates: Bureau of Meteorology Australian Water Resources Assessment and Water Accounts (national and regional renewable water), ABS Water Account Australia, and Murray-Darling Basin Plan diversion limits for the one basin where a legal cap exists. The ABS Water Use on Australian Farms 2020-21 cubes in `analysis/SOURCES.md` (`WUAFDCNRM202021.xlsx`, by NRM region) give water applied, which is use, not supply; the irrigation review (`analysis/irrigation_review/`) already reads them. Choosing the definition is a decision, and it sets the result |
| Hydrological units (L1 to L3 in the paper) | To be obtained | Drainage divisions and river basins of the Bureau's Geofabric, or the older AWRC basins (counts to be confirmed from the source). The repository holds administrative units and the 53 NRM regions, not river basins; NRM regions are catchment-based and the closest on hand |
| Cropland from land cover for the "current situation" row | On hand | `data/sa2/land_use_by_sa2.csv`, CLUM classes; the model's cropping km2 by region |

## 3. The fidelity check

Murray's rule (README opening) makes the Australian application the test and the author's figure a check on the implementation. Three levels, from most to least reachable:

1. **Arithmetic, reachable with no new data.** The paper's own numbers close on its formulas: A = 195,304.95 km2 over B = 1,500 m2 gives 130.2 million (exact to the printed 130,203,303; p.7 to 8, my arithmetic). The land-only scenarios give implied areas (K x 1,500 m2): about 248,800 km2 (scenario 1, 165.9 million), 102,100 (scenario 3, 68.1), 17,100 (scenario 4, 11.4), 3,900 (scenario 5, 2.6) and 1,300 (scenario 6, 0.87). And the 2023 equations reproduce the four-scale results to within about 2 to 8% (127.5 against 130.2, 71.9 against 76.8, 32.4 against 35.5, 18.5 against 20.2). This is the same kind of check the Henry and Godden test used, and it shows the recipe is read correctly.
2. **The nation as one unit (130.2 and 35.5 million), reachable from public data with a stated gap.** Table 2 prints the national water figure (61,619 MCM) and the target A (195,305 km2), so the national search is checkable: rebuild SI for Iran from public layers, take TerraClimate AET on the cells above a threshold, and find the threshold where AET reaches 61.6 BCM; the paper says it is 0.074 and that A is 195,305 km2 (AET 62.64 BCM). That needs Mesgaran's variable parameters (his paper and the supplement) and Iran-wide rasters: a separate Iran data job, session-size, with a mid-sized gap expected because TerraClimate AET and the authors' trial-and-error AET need not agree. The HANPP figure (35.5) then needs MODIS NPP over that A. The land-only scenarios (165.9, 68.1, 11.4, 2.6, 0.87 million) are checkable the same way without the water step.
3. **The scale figures (76.8 and 20.2 million, and 115.3, 98.4, 27.7, 24.2), not reachable.** They need the ministry's basin boundaries and per-unit water cycle (X17, X21 for 609 units), which the paper does not print and which are not public as far as the paper shows.

So: one headline figure can be checked from public data, **130.2 million (and the land-only scenario series)**, at the cost of an Iran build; the cheapest honest check is level 1, arithmetic, as in the Henry and Godden test. I would report level 1 and state that levels 2 and 3 were not rebuilt.

## 4. The Australian reading

* **Scales.** The nation (1), the states (7 in the scale-curve work), the 53 NRM regions, SA4 (89), SA3 (336), SA2 (2,450) all exist on hand and match the results paper's scale curve exactly (`analysis/scale_curve_2025/README.md`; 2025 short term: 75%, 44%, 58%, 44%, 37% of the national figure). River basins would be the true analogue of the paper's L1 to L3 if the Geofabric is added.
* **A necessary point about the scale.** If the bound is land and NPP only, K is the sum of A (or of HANPP) over the units, which is additive: the sum over any partition equals the national figure and there is no scale curve at all. In Khorsandi the entire fall (130.2 to 76.8) comes from the water step: each unit has to find its suitability threshold against its own water, so water cannot move between units. So a scale curve on this method requires the water bound; land plus HANPP alone gives one number per scale and no curve.
* **What it compares against.** (a) The corrected thesis model: 41.5 million short term, 15.6 long term, improved 53.6 and 18.5 (`model_entry.csv`). (b) The other methods in the cross-method table (134 to 343 million for the calorie and land methods; 12 to 41 for the binding-item methods). (c) The shape of the scale curve of the results paper: Khorsandi falls to 59% (theoretical) and 57% (HANPP) at the finest level, 609 units; the thesis model falls to 37% (short term) at 2,450 SA2s and to 44% at the 53 NRM regions. The two curves differ in cause: Khorsandi's loss is water that cannot travel; the thesis model's loss is crop land and pasture that cannot be paired (the NRM diagnosis). (d) The 2023 log fit, K = a ln(A) + b, can be fitted to the Australian scale points to ask whether the same shape holds.

## 5. Where it differs from the thesis method

| | Khorsandi 2022 and 2023 | Thesis method (resource-based land and diet balance) |
|---|---|---|
| Land | Suitability index, continuous, with thresholds; infrastructure at 1,500 m2 a person | Land types (cropping, pasture, nature, infrastructure), with yields by zone |
| Water | Central: a per-unit balance sets how much land can be farmed | An irrigation share that raises yield by a flat 55%; no water balance (`analysis/irrigation_review/`) |
| Ceiling | An NPP ceiling: 25% of NPP, 4 kcal a gram | Yields from observed data, no biological ceiling |
| Diet | One flat energy figure (3,000 kcal), all biomass counted as food | A diet with food groups, waste, meat and dairy |
| Pasture and crops | Not distinguished: any suitable area yields calories | The pairing of pasture-fed food with crops is what binds (`scale_curve_2025`) |
| Weather | Long-term means (the K(t) series from 2001 to 2020 NPP is a separate reading) | A resilience allowance by percentile (1 in 10, 1 in 100 years) |
| Trade | Self-sufficient, no exports counted out | Self-sufficient; exports not subtracted either |
| Fuel, fibre, timber, reserve | Not present | Present |

What it sees that the thesis method does not: a water limit by unit, a continuum of land quality rather than a type, and an upper bound from photosynthesis. What it does not see: the pairing of rangeland pasture with crops, any diet beyond one energy number (no protein, no food groups), waste, weather beyond the mean, fuel and fibre, and the part of NPP that is straw, roots or inedible grass.

## 6. Size and risk

| Part | Size | Why |
|---|---|---|
| (a) The simple 2023 formula on data on hand | **Quick** | A (arable share x SA2 area) over B = 1,500 m2, summed at each scale, and the log fit, from `arable_share_gaez_*` and `land_types_by_sa2.csv`. But see the risk below: at 1,500 m2 a person, every 100,000 km2 of A is 66.7 million people, so the land bound is not binding for Australia and the number is uninformative as a capacity |
| (b) The land-suitability bound (thresholded) | **Small** if the GAEZ class bands are accepted as the suitability layer (rerun `arable_share_by_sa2.py` per class band; the rasters must be downloaded); **session-size** if Mesgaran's continuous index is rebuilt for Australia, which is not needed for the comparison | GAEZ and Mesgaran are different indices, so the thresholds of the paper cannot be matched exactly; the test would use GAEZ and say so |
| (c) The water bound | **Session-size** | Needs an Australian definition of available water per unit (a decision for Murray), AET on suitable land (TerraClimate or AWRA-L), and the trial-and-error threshold search per unit at each scale. This is the only part that produces the scale curve |
| (d) The HANPP bound | **Small**, session-size if the download of MODIS NPP is blocked by login and another NPP source must be built | Zonal means of annual NPP over the suitable cells; the raster handling already exists in `arable_share_by_sa2.py` (cell centres joined to SA2s). Constants: 25%, 4 kcal a gram, 3,000 kcal a day |
| The whole test with fidelity level 1 | **Session-size** | (c) dominates |

**What could make the test misleading for Australia**
* **Rangeland.** Nearly all of Australia's pasture is rangeland with very low NPP. If rangeland cells enter A (any SI above zero), 25% of grass NPP is counted as human food, which is wrong for biomass people cannot eat; if they are left out, the pasture-fed meat and dairy that the thesis model counts are not counted at all. Either choice moves the answer by an amount that the method cannot adjudicate, because it has no pasture-to-food conversion. The scale curve of the thesis model is driven by exactly this land (`scale_curve_2025`: eight units hold 71% of the pasture).
* **Irrigation.** In Iran, water is the binding resource and the paper turns "all possible blue water into green". Australia's irrigated crops sit in a few basins (0.5% of farmland, 4.6% of cropped land is watered, `irrigation_review`), most farmland is rain-fed, and rain-fed AET is capped by rain on the spot, not by a basin budget. So the water balance may bind in the Murray-Darling and nowhere else, and the choice of "available water" (rainfall-based, renewable, or with environmental flows kept) decides whether it binds at all. The result would reflect the definition, not the land.
* **Exports.** The method counts everything the land can produce as eaten at home. Australia exports most of its farm output, so a K from this method reads as "if every calorie produced were eaten here", like Henry and Godden (134 to 211 million in the README), not as a population the present system feeds.
* **Averaging.** NPP is a mean over years and includes roots and straw; the harvested food share of NPP is lower than 25% for many crops. The 25% is Iran's assumption carried over (the authors note it is unclear for Iran, 2023 p.10).
* **Comparing the scale curves.** Administrative units (SA2, NRM) are not hydrological units, so a drop at 53 NRM regions mixes boundary and water effects, as in the thesis scale curve (README, limits).

## 7. Recommendation

Run it, in two stages, and report it as a ceiling, not a capacity. The simple 2023 form alone (a) is quick but says nothing about Australia: at 1,500 m2 a person the land bound is far above any other method's reading, and the log fit has no meaning without a water step, because land plus NPP sum without loss across any partition and give no scale curve; so running only the simple form would add a number and no information. The method earns a place in the cross-method table and in the scale-curve section only through the water bound (c), which is where Khorsandi's own 40% fall comes from and which gives a second, independent reading of what scale does to Australian capacity (water that cannot move, set against the thesis model's land and pasture that cannot be paired). Stage one is (a), (b) with GAEZ bands and (d) at the national scale with level-1 fidelity (arithmetic), which is small; stage two is (c) at the 53 NRM regions and, if Murray wishes, river basins, which is session-size and needs one decision from him: what "available water" means for an Australian unit. If that decision is not made, catalogue only (the B17 entry stands) is the sound fallback, and stage one is not worth running by itself.
