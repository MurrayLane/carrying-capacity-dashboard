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

## 3. The three flags, investigated (`flags.mjs`, `flags_2025-fixed.csv`, `make_beef.py`)

Murray did not know the derivations (2026-10-28) and asked for them to be found in the existing data, then derived by back-calculation, then assumed. Result:

### A1 beef: found in the archive, and corrected

* **Found.** `superceded/170611 Base model.xls`, row 467: beef processing yield **0.705**, cell note "USDA weights measures 1992: used figure for entire animal (retail cuts) across all cuts. Yield converted to loss." In `superceded/Base model (12).xls` the value is 1.0 and the note reads "Originally used figure of 70.5% as per USDA weights measures 1992: figure for entire animal (retail cuts) across all cuts. **BUT: the ABS yield figures are for carcass weight, not live weight so reverted to 100% processing yield.**" Every later version, and the thesis appendix table, carries 100%.
* **Why the reversion was a mistake.** 70.5% is the USDA carcase-to-retail factor: retail cuts as a share of *carcase* weight (USDA ERS, Nelson, Duewer and Crawford 1989, reevaluated 0.74 down to 0.705 for 1988). It cannot be a live-weight yield (a carcase is about 55 to 62% of live weight). The ABS figures being carcase weight is the reason the carcase-to-retail factor is needed. Further support: AUS-MEAT's beef carcase yield guide in the archive gives 68.7% meat; lamb, veal and pork keep their carcase-to-retail yields (0.894, 0.83, 0.776) and beef was the only red meat without one; with the factor, edible portion times processing is 0.645 for beef against 0.66 to 0.69 for the others.
* **Applied** as the second entry of `CORRECTIONS` (method module `beef-carcase-yield`, `Base!K175` = 0.705). Australia: the module alone lowers the short term by **7.2 million on the 2011 data (-17.8%) and 8.5 million on the 2025 data (-17.7%)**; it adds nothing to the long term alone, because the long-term diet has little red meat, and costs 0.4 and 1.8 million in sequence after the biodiesel correction (which frees the cropland that red meat then competes for). The model's beef demand rises from 42.3 to 60.0 kg of carcase a person a year in the short-term diet; comparing that with the actual Australian consumption (MLA, carcase weight equivalent) has not been done and is a candidate check of the diet, not of the yield.
* **Uncertainty.** 0.705 is the USDA factor of 1988; the AUS-MEAT figure (68.7% meat plus 12% fat, some of which is eaten) is of the same size. A value between 0.69 and 0.74 is defensible and moves the result by about +/-2 million in the short term.

### Checks on A1 (2026-10-28)

1. **Is the model's beef production carcase weight? Yes.** ABS 7215.0 explanatory notes (archived editions): "Red meat is shown in carcass weight and excludes offal". The ABS also gives its own bone-out to bone-in conversion for beef and veal, **1.5** (boneless meat x 1.5 = carcase weight), so boneless meat is 0.667 of the carcase. Three independent agency figures for the carcase-to-boneless-meat yield therefore bracket the value used: ABS 0.667, AUS-MEAT 0.687, USDA 0.705. The ABS beef table (7215009, quarterly tonnes, 2010-11 total 2.09 million tonnes) matches the FAO production for bovine meat (2.129 million tonnes in 2010 and 2011, to which veal adds the difference), which FAO also reports in carcase weight. The author's premise ("the ABS figures are carcase weight") is right; the conclusion drawn from it was the wrong way round.
2. **Does the model's beef demand match what is available?** FAO's food balance for Australia gives a bovine meat supply of 38.6 kg a person in 2010 and **41.9 kg in 2011** in carcase weight (26.9 kg in 2023). Passed through the model's chain (retail loss, consumer loss 20%, edible portion, cooking yield) that supply is **436 g a week of cooked beef at a processing yield of 1.0** and **308 g a week at 0.705**. The model's diet has 438 g a week. So the diet's beef equals the whole of the 2011 national supply only if no carcase-to-cut loss is counted; at 0.705 the supply is a third short of the diet. This **does not discriminate**: the diet is a recommended pattern, not the actual one, the supply includes pet food, trimmings and food-service waste that the chain ignores, and I have no survey figure for beef alone to compare either implied intake with (the Australian Health Survey data in the repository give food groups, not beef). It would fail the 1.0 value only if actual intake is far below 436 g a week, which is likely (the NHMRC recommendation for all lean red meat is 455 g a week) but unchecked.

**Confidence after the checks:** that the 1.0 is a mistake about 90% (the premise is confirmed and three agencies agree on the yield); that the value of the correction is within 0.667 to 0.705, about 85%; the short-term fall is then 16 to 20%.

### A3 butter: not an error that can be shown; left as it is

* **Found.** `prelim models/processing yields.xls`, sheet `dairy`: 20.6 kg of milk make a kilogram of butter (yield 0.0485), and cream left over from reduced-fat and skim milk production could supply 0.679% of that milk as butter. The Base sheet carries the note on the butter row, "This formula includes the cream left over from skim milk production", and the butter row subtracts 0.7% of the skim milk production from its milk requirement (`Base!Y266`). The butter yield 0.195 appears unchanged in every version of the workbook in the archive and in the thesis appendix, with no derivation anywhere.
* **Back-calculation.** 0.195 is five kilograms of milk to a kilogram of butter, a quarter of the sheet's 20.6. It is not reproducible from the sheet. It is consistent with allocating about a quarter of the milk to butter as a co-product of the other dairy products (butter is made from the fat that milk for cheese, skim milk and yoghurt gives up), a standard allocation for joint products; the thesis does not say so.
* **Assumption.** Keep the thesis value (it is a co-product allocation, documented in intent if not in figures). Using the whole-milk yield (0.0485) with no allocation would lower the long term by up to 13% (flag A3 in `flags_2025-fixed.csv`), so the allocation is recorded as an uncertainty (`DISCUSSION.md` row 17). A national check is possible: Australian butter production was 148,000 tonnes in 2008-09 (ABARE commodity statistics, as cited by thedairysite.com) against about 9 billion litres of milk (Dairy Australia; the milk figure is from memory and not checked here), which at 0.0485 would be a third of the milk and at 0.195 under a tenth.

### A4 cotton: negligible, left as it is

The processing yield of cotton (0.836) would be 0.38 if the unit were seed cotton to lint; the effect on Australia is under 0.1% either way. Recorded, not changed.

## 4. What is confirmed and what is not

* **Confirmed and corrected:** the biodiesel yield (ABARE's figure per tonne of seed, `analysis/liquid_fuel_2025/`) and the beef carcase-to-retail yield (the author's own earlier value and note, USDA, AUS-MEAT). Both are in `CORRECTIONS` of `analysis/comparison_2025/make_cells.py`.
* **Assumed:** the butter allocation (kept), cotton (kept).
* **Not yet audited:** lamb, veal and pork processing yields (their cells have no notes; they share the 0.66 to 0.69 range), the 400-odd constants of lower leverage, the serving sizes (Byron 2011, NHMRC), the nutrient values, the non-food rows (timber, built-on land, infrastructure) and the feed conversions of the Yield sheet. Nothing below the groups of section 1 can move the result by more than a percent or so on its own.

## 5. What the corrections do to the comparison (Australia, millions of people)

| | Published (2011 / 2025) | Corrected | Improved |
|---|---|---|---|
| Short term, 2011 | 40.45 | 33.31 | 33.04 |
| Short term, 2025 | 48.00 | 39.52 | 39.18 |
| Long term, 2011 | 9.43 | 15.35 | 12.56 |
| Long term, 2025 | 14.05 | 15.92 | 14.85 |

The short-term increase from 2011 to 2025 is robust to the corrections (+7.6 million as published, +6.2 corrected, +6.2 improved), but the **headline level falls by about 18%** (the 40 million of the 2015 scale paper becomes 33 million). The long-term increase is not robust: +4.6 million as published, **+0.6 million on the corrected method**, +2.3 on the improved, because the corrections lift the 2011 long-term result far more than the 2025.
