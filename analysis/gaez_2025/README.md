# GAEZ attainable yields of tropical staples (SCOPE.md E12 and E16, 2026-10-30)

**Question.** The model has no yield for yam, taro, coconut or oil palm, and its Northern Territory cassava yield is a borrowed number. FAO's Global Agro-Ecological Zones v4 (GAEZ) gives the attainable yield of each crop everywhere on the land surface, from climate, soil and slope; can it fill the gap?

**Data.** GAEZ v4 theme 4 (`res05`), climate 1981 to 2010 (CRU TS 3.2 historical), high input level, with CO2 fertilisation, variable `yxH{r,a}`: the average attainable yield of the best suitability class in each 5 arc minute grid cell (about 9 km), over all land, rainfed (`r`) or irrigated (`a`). Files: `https://s3.eu-west-1.amazonaws.com/data.gaezdev.aws.fao.org/res05/CRUTS32/Hist/8110H/yxHr_<crop>.tif`, crop codes `csv` cassava, `spo` sweet potato, `yam` yam, `ban` banana, `con` coconut, `olp` oil palm, `suc` sugarcane (the catalogue is at https://gaez-services.fao.org/server/rest/services/res05/ImageServer/query). **GAEZ has no taro.** Units are kg dry weight per hectare (sugarcane kg sugar, oil palm kg oil; User's Guide, https://openknowledge.fao.org/server/api/core/bitstreams/73f77f36-4976-41b9-823c-a82f1f14f87f/content); fresh weight is dry weight divided by one minus the moisture of the AUSNUT 2023 raw food (cassava 62.0%, sweet potato 76%, yam 68.9% taken from taro because AUSNUT has no yam, banana 75.8%). The files are not stored (2 MB each, public); `gaez_yields.py` downloads them.

**Method.** `gaez_yields.py` takes rectangles (listed in the script) around the Top End of the Northern Territory, the Kimberley, Cape York and the north Queensland coast, and four Pacific countries, keeps the land cells, and reports the share of cells where the crop is suitable at all and the mean and 90th percentile yield of the suitable cells. Results: `gaez_yields.csv` (98 rows, rainfed and irrigated); the check against FAO's actual yields of the Pacific countries: `gaez_vs_fao.csv`.

## Results (rainfed, fresh weight t/ha, mean of the suitable cells; share of land cells suitable in brackets)

| | NT Top End | Kimberley | Cape York and north Qld coast | Papua New Guinea |
|---|---|---|---|---|
| Cassava | 12.7 (99%) | 9.1 (99%) | 15.6 (100%) | 20.7 (90%) |
| Sweet potato | 23.6 (99%) | 19.2 (99%) | 28.6 (100%) | 24.4 (90%) |
| Yam | 9.5 (99%) | 7.9 (99%) | 13.0 (100%) | 18.6 (90%) |
| Banana | 12.0 (0.2%) | none | 24.2 (9%) | 32.5 (90%) |
| Coconut, kg dry weight/ha | 1,254 (21%) | none | 2,074 (25%) | 3,634 (67%) |
| Oil palm, kg oil/ha | 1,426 (0.2%) | none | 2,981 (3.7%) | 4,581 (71%) |
| Sugarcane, kg sugar/ha | 2,857 (27%) | 2,618 (4%) | 5,288 (29%) | 8,561 (90%) |

**Does GAEZ agree with what farmers get?** Dividing FAO's actual 2019 to 2023 yields by GAEZ's rainfed value for the four Pacific countries: yam 0.54 to 0.94, cassava 0.47 to 0.92, sweet potato 0.21 to 0.55, banana 0.07 to 0.50 (`gaez_vs_fao.csv`). So for yam and cassava actual yields are 50 to 90% of the attainable ones and GAEZ is a good guide; for sweet potato and banana smallholders reach a fifth to a half. GAEZ is a ceiling, and the mean of the best class in each cell is an upper bound for an area average.

## What it changes

1. **Yam can be added to the model for northern Australia** with an attainable yield of 9.5 t/ha in the Top End (7.9 Kimberley, 13.0 Cape York); at the Pacific ratio of 0.54 to 0.94 an actual yield would be 5 to 9 t/ha in the Top End. Taro is still without a source (FAO Pacific figures only, `analysis/diet_templates/tropical_crops.md`).
2. **The model's northern cassava yield is too high.** The model's cassava row is a copy of the sweet potato proxy (NT 22.7 t/ha, `data/2025/yield_provenance.csv`); GAEZ gives cassava 54% of sweet potato in the Top End, 47% in the Kimberley and 55% in Cape York. The NT sweet potato itself agrees (model 22.7, GAEZ 23.6). Not applied to a release: cassava is not in the default diet, so no published result moves. Run through the tropical-staples diet (20% of energy, ten micronutrients) with `YIELD_SCALE=131:0.54` the NT capacity falls 2.3% in the short term (162,625 to 158,876) and 0.4% in the long term.
3. **Oil palm is not a Top End crop and barely a Cape York one** (0.2% and 3.7% of cells suitable), so palm oil cannot be a tropical-Australian staple in the model; coconut is suitable on a fifth to a quarter of the cells but the GAEZ unit (dry weight of what, kernel or copra) is not stated, so no fresh yield is given.
4. **Banana: GAEZ and the model disagree.** The model's NT banana yield is observed (14.3 t/ha, ABS 2022 to 2025) but GAEZ finds almost none of the Top End suitable, rainfed or irrigated. Taken as the 5 arc minute grid missing the irrigated pockets near Darwin; the observed figure stands.

## Limits

* Rectangles, not the model's zone boundaries (no shapefile in the repository): coarse, and the Top End rectangle includes dry savanna.
* GAEZ high input, rainfed or irrigated, is a model, not a harvest; sweet potato and banana in the Pacific reach a fifth to a half of it.
* Fresh weight uses AUSNUT peeled-food moisture, which differs a little from the moisture of the harvested product (peel, tops).
* 1981 to 2010 climate; GAEZ also has climate-change runs (`res05` other models and RCPs), not used here.

Record: `DISCUSSION.md` rows 5 and 24.
