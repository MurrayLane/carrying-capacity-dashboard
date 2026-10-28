# Constants audit (SCOPE.md E18)

The biodiesel yield was wrong by a factor of 2.4 and sat in the workbook, untouched, in every version since 2012 (`analysis/liquid_fuel_2025/README.md`). The earlier model audit (`analysis/model_audit/`) checked arithmetic and internal consistency; it did not trace typed-in constants to their sources. This audit does, in order of leverage.

## 1. Which constants matter (`leverage.mjs`, `leverage_2025-fixed.csv`)

Each group of numeric constants raised by 10% (formulas left alone), Australia's capacity recomputed on `2025-fixed` (the corrected tier). The edible portion, cooking yield, consumer, retail and primary-to-retail losses and processing yield of a food multiply together, so a group's leverage is about 10% for its whole chain and the interest is in which groups carry weight:

| Group (constants) | Short term | Long term |
|---|---|---|
| **Red meat: edible portion, cooking, losses or processing yield (4 foods)** | **+7.1%** | **+3.4%** (losses 0%) |
| Serving size of red meat (4) | -6.8% | -3.5% |
| Fibre: wool and cotton yields (2) | +0.5% | +3.8% |
| Dairy, low fat (15); high fat (13); medium fat (18) processing yields | +0.6%; +0.7%; +0.3% | +1.1%; +0.3%; +0.1% |
| White meat (13) | +0.2% | 0 |
| Fats and oils (14); nuts and seeds (14); cereals, fruit, vegetables, legumes (each under 0.1%) | under 0.1% | under 0.1% |
| Biofuel feedstock (7), after the correction | 0 | +0.03% |
| Feed conversion ratios of the Recycle sheet (7) | 0 | 0 |

Red meat is the heaviest group by a factor of ten, because red meat is most of the land in today's diet; fibre and dairy follow. The leverage depends on which land type binds, so it changes with the settings; the biodiesel yield was far heavier before the correction.

## 2. How well the constants are documented (`note_coverage.csv`)

The workbook documents sources in cell notes (898 in the Base sheet) and by column defaults in row 4 (edible portion and cooking yield: AUSNUT, with Matthews and Kantor; consumer loss: Muth 2011; retail and primary-to-retail loss: Buzby 2010; processing yield: Peters 2005 unless own calculation). Of the constants that are not 1:

| Column | Constants | With a cell note |
|---|---|---|
| Edible portion (E) | 78 | **0** |
| Cooking yield (F) | 86 | 18 (21%) |
| Consumer loss (G) | 275 | 154 (56%) |
| Retail loss (I) | 275 | 158 (57%) |
| Processing yield (K) | 167 | 94 (56%) |
| Primary-to-retail loss (L) | 97 | 46 (47%) |

**All of the red-meat constants (beef, lamb, veal, pork) have no cell note at all**, and red meat is the group with the most leverage. They rest on the column defaults, which cannot be checked from the workbook.

## 3. Flags (`flags.mjs`, `flags_2025-fixed.csv`)

Where the constants can be compared with the references in the models archive, three look inconsistent. None is called an error here: the cells have no notes, so the reasoning behind them is not recorded, and each needs the author's answer. Effect on Australia of changing the constant as the flag suggests (millions of people; base 48.06 short, 17.69 long on `2025-fixed`):

| Flag | What looks inconsistent | If changed | Short term | Long term |
|---|---|---|---|---|
| **A1 beef** | Beef (dressed) has a processing yield of 1.0 and an edible portion of 0.916, a product of 0.916 of the carcase. The other red meats have edible portion times processing yield of 0.66 to 0.69 (lamb 0.768 x 0.894, veal 0.79 x 0.83, pork 0.854 x 0.776). The AUS-MEAT beef carcase yield guide in the archive (`references re food processing yields/Ausmeat - beef yields.pdf`) gives 68.7% meat, 12.0% fat and 19.3% bone. The model's production is carcase weight (the ABS Livestock Products tables). Beef is 69% of the red meat eaten | processing yield 0.75 (product 0.687) | **41.00 (-14.7%)** | 16.25 (-8.2%) |
| | | processing yield 0.85 | 44.05 (-8.4%) | 16.90 (-4.5%) |
| **A3 butter** | Butter (Fats and oils, milk) has a processing yield of 0.195, about 5 kg of milk to a kilogram of butter; butter from whole milk needs about 22 kg (82% fat from 3.7% fat). It may be cream rather than milk (the skim then feeding the skim milk row), which would be a co-product allocation the workbook does not document | 0.045 | 47.05 (-2.1%) | **15.41 (-12.9%)** |
| A4 cotton | Cotton has a processing yield of 0.836; lint is about 35 to 40% of seed cotton. The unit of the cotton yield (lint or seed cotton) is not recorded here | 0.38 | 48.02 (-0.1%) | 17.69 (0) |

What I can say: A1 and A3 are large if they are what they appear to be; A1 would lower the short-term result by up to 15% and the long-term by up to 8%. What I cannot say: whether the edible portion of beef (0.9155) already folds in the boning of the carcase (it is the weighted average of 40 cuts of AUSNUT, thesis section 8.4), or whether the beef production is carcase weight or retail weight. The thesis appendix table prints the same 100% for beef, so it is the thesis's value, not a transcription slip in the workbook.

## 4. What is confirmed and what is not

* **Confirmed against the thesis's own source and corrected:** the biodiesel yield (the first entry of `CORRECTIONS` in `analysis/comparison_2025/make_cells.py`).
* **Flagged, waiting for Murray:** A1 (beef), A3 (butter), A4 (cotton). If Murray confirms the reasoning behind a value, it is recorded here as confirmed; if not, the correction goes into `CORRECTIONS` with the evidence, as the biodiesel did, and the results are regenerated.
* **Not yet audited:** the other 400-odd constants of lower leverage (each group under 1%), the serving sizes (Byron 2011, NHMRC), the nutrient values, the non-food rows (timber, built-on land, infrastructure) and the livestock feed conversions of the Yield sheet. They are documented here by leverage so that the effort is proportionate: nothing below the groups of section 1 can move the result by more than a percent or so on its own.

## 5. Questions for Murray

1. **Beef:** was the carcase-to-cuts yield (boning and trimming, about 69% by AUS-MEAT) included in the edible portion of 0.9155, or is it missing? What is the unit of the beef production in the Yield sheet (carcase weight)?
2. **Butter:** is 0.195 the yield from cream? If so, where does the skim go?
3. **Cotton:** is the cotton yield lint or seed cotton?
