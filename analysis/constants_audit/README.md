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

**Confidence after the checks (before stage 2):** that the 1.0 is a mistake about 90% (the premise is confirmed and three agencies agree on the yield); that the value of the correction is within 0.667 to 0.705, about 85%; the short-term fall is then 16 to 20%.

### A3 butter: not an error that can be shown; left as it is

* **Found.** `prelim models/processing yields.xls`, sheet `dairy`: 20.6 kg of milk make a kilogram of butter (yield 0.0485), and cream left over from reduced-fat and skim milk production could supply 0.679% of that milk as butter. The Base sheet carries the note on the butter row, "This formula includes the cream left over from skim milk production", and the butter row subtracts 0.7% of the skim milk production from its milk requirement (`Base!Y266`). The butter yield 0.195 appears unchanged in every version of the workbook in the archive and in the thesis appendix, with no derivation anywhere.
* **Back-calculation.** 0.195 is five kilograms of milk to a kilogram of butter, a quarter of the sheet's 20.6. It is not reproducible from the sheet. It is consistent with allocating about a quarter of the milk to butter as a co-product of the other dairy products (butter is made from the fat that milk for cheese, skim milk and yoghurt gives up), a standard allocation for joint products; the thesis does not say so.
* **Assumption.** Keep the thesis value (it is a co-product allocation, documented in intent if not in figures). Using the whole-milk yield (0.0485) with no allocation would lower the long term by up to 13% (flag A3 in `flags_2025-fixed.csv`), so the allocation is recorded as an uncertainty (`DISCUSSION.md` row 17). A national check is possible: Australian butter production was 148,000 tonnes in 2008-09 (ABARE commodity statistics, as cited by thedairysite.com) against about 9 billion litres of milk (Dairy Australia; the milk figure is from memory and not checked here), which at 0.0485 would be a third of the milk and at 0.195 under a tenth.

### A4 cotton: a false alarm (resolved in stage 2)

The processing yield of cotton (0.836) looked like a ginning turnout. It is not: the model's cotton yield is **cotton lint** (the ABS series "Cotton lint", `pipeline/yields/abs_current/model_crops.json`), and 0.836 is the fibre-to-product processing yield worked out in the archive's `non-food resource data.xls`, sheet `fibre-Aust` (rows 12, 18, 20: actual weight over fibre equivalent of cotton trade, 0.836 to 0.838). Wool 0.6902 is the same sheet's clean-yield figure (0.69 to 0.70). Consistent; nothing to change. (Flag A4 in `flags_2025-fixed.csv` is therefore moot.)

## 3b. Stage 2 (2026-10-28): the rest of the high-leverage groups

* **Red meat other than beef: documented in the older workbooks and consistent.** In `superceded/Base model (12).xls` the cell notes give the sources of every constant of lamb, pork and veal: cooking yield from Kantor's averages (lamb 26%, pork 39%, veal 25% loss), consumer loss from Muth et al. 2011, retail loss from Buzby (USDA 2010), processing yield from "USDA weights measures 1992: used figure for entire animal (retail cuts) across all cuts. Yield converted to loss." The final single-row constants are exact unweighted means of the per-cut rows of that workbook (beef 41 cuts, pork 20, veal 2: identical to four places; lamb 27 cuts 0.762 against 0.768 in the final row for the edible portion, an update).
* **The edible portion is cut-level, so the beef correction does not double count.** The beef edible portion 0.9155 is the mean of the AUSNUT inedible portions of 41 retail cuts (blade steak 0.90, fillet 0.93 and so on): it removes bone and fat from the cut, not the carcase-to-cut loss, which is the processing yield.
* **This sharpens the beef finding.** Lamb, pork and veal were kept on the USDA "entire animal (retail cuts)" yield; only beef was reverted on the argument that the ABS figures are carcase weight, and that argument applies equally to the other three. The treatment of beef is the inconsistent one. **Confidence that the beef 1.0 is a mistake: about 93%.**
* **Cheese: consistent within the references, slightly conservative.** The model's milk-to-cheese yield is 0.0909 (11 kg of milk to a kilogram) against 9.5 kg of cheddar per 100 kg of milk as the "general standard factor" and 10.2 to 10.6 kg in Walker's farm data (`references re food processing yields/`): the model's yield is 10 to 14% below the references. Raising it to 0.10 would raise the short-term result by well under 1%. Not changed; recorded.
* **Serving sizes agree with the dietary guidelines.** 65 g of cooked lean red meat, 80 g of cooked lean poultry, 2 large eggs (120 g), 30 g of nuts and a small can of fish (the model has 100 g) are the serves in the Australian Dietary Guidelines consumption page held in the repository (`consumption-food-groups-australian-dietary-guidelines.html`); the 65 g red meat serve is the highest-leverage serving size.
* **Timber: no leverage.** Raising the timber processing yield by 10% changes Australia's capacity by 0.00%; timber land does not bind.
* **Butter** remains the one undocumented high-leverage constant (A3 above).

## 4. What is confirmed and what is not

* **Confirmed and corrected:** the biodiesel yield (ABARE's figure per tonne of seed, `analysis/liquid_fuel_2025/`) and the beef carcase-to-retail yield (the author's own earlier value and note, USDA, AUS-MEAT). Both are in `CORRECTIONS` of `analysis/comparison_2025/make_cells.py`.
* **Assumed:** the butter allocation (kept). **Checked and consistent:** cotton and wool, lamb, pork and veal constants, cheese yield, serving sizes, timber.
* **Not audited:** the fruit and vegetable edible portions and cooking yields (low leverage, under 0.1% a group), the consumer and retail loss factors (Muth and Buzby, US figures; replacing them with Australian ones is SCOPE E4), the nutrient values and the feed conversions of the Yield sheet. Nothing below the groups of section 1 can move the result by more than a percent or so on its own.

## 5. What the corrections do to the comparison (Australia, millions of people)

| | Published (2011 / 2025) | Corrected | Improved |
|---|---|---|---|
| Short term, 2011 | 40.45 | 33.31 | 33.04 |
| Short term, 2025 | 48.00 | 39.52 | 39.18 |
| Long term, 2011 | 9.43 | 15.35 | 12.56 |
| Long term, 2025 | 14.05 | 15.92 | 14.85 |

The short-term increase from 2011 to 2025 is robust to the corrections (+7.6 million as published, +6.2 corrected, +6.2 improved), but the **headline level falls by about 18%** (the 40 million of the 2015 scale paper becomes 33 million). The long-term increase is not robust: +4.6 million as published, **+0.6 million on the corrected method**, +2.3 on the improved, because the corrections lift the 2011 long-term result far more than the 2025.

## 4. Stage 3 (2026-10-29): what is left to audit, by leverage

Leverage recomputed on the improved tier (`leverage_2025-improved.csv` shows the same order as `leverage_2025-fixed.csv`: red meat 7.4% short term per 10%, fibre, dairy; every other food group under 0.1%) and extended to the constants outside the Base loss columns (`leverage_sheets.mjs`, `leverage_sheets_2025-improved.csv`: each row of the Diet, Yield, Settings and Recycle sheets raised by 10%).

* **Fruit and vegetable edible portions and cooking yields: negligible leverage** (under 0.1% for the whole group per 10%) and the main items agree with the USDA edible-portion values within about 10% (apple 0.92, banana 0.65, orange 0.78, potato 0.85, broccoli 0.60, watermelon 0.51, peas 0.36); the one that looks high is melon (0.665 against 0.46 to 0.51 for cantaloupe and honeydew, 186 g a week). Not worth a correction.
* **Feed conversion ratios: zero leverage** on capacity (they act through the recycling credit, which is small).
* **Nutrient values** affect the diet outputs (energy, protein), not capacity; they matter for E11, not here.
* **The Diet sheet's serves by meat share** (NHMRC) are the next largest constants: red meat serves -4.5% short term and -2.1% long term per +10%, white meat and eggs -2.9% and -2.2%. They are the subject of E7 (diet refresh), not an error.
* **Diet row 2 shows +133%** only because it holds lookup keys (the meat-share index); a change of 10% breaks the lookup. Ignore.
* **One new finding: the organic yield factor of the ruminants** (`organic_livestock.mjs`). Yield!G95, G96 and G98 (sheep meat, sheep wool, cattle meat) carry the 0.808 that the workbook gives every row with fewer than three studies (the mean of the crop means); only dairy milk has its own studies (6, 0.807). It acts only in the long term (organic 100%), where cattle meat and sheep wool each move the result by about 3% per 10%. At 0.9 the long term of Australia is 16.03 million (+7.9%), at 1.0 it is 17.25 (+16.1%). **Not an error against a source; an untested assumption with real leverage.** The evidence found: a global meta-analysis of organic livestock (Environ. Res. Lett. 2021, 37 comparisons) gives productivity per animal 12% (±5%) lower, dairy cattle 14% lower, beef only three studies and "smaller gap", sheep and goats no study that qualified; output per hectare was not measured. 0.808 for ruminants is within what is known (per-animal 0.86; land productivity lower) but no Australian grazing figure exists, so it is recorded in `DISCUSSION.md` (row 19) and kept.

Result of the audit by leverage: after the biodiesel and beef corrections, no constant with leverage over 1% remains unchecked except the ruminant organic factor (an assumption) and the diet serves (E7). The audit is therefore complete for the capacity result. The unaudited rest is a matter of nutrition outputs and of data (E7, E11).

## Stage 4: the organic factor of the ruminants, what evidence there is (2026-10-30)

Question: is 0.808 (the mean of the crop studies, given by the workbook to sheep meat, sheep wool and cattle meat) a defensible organic yield for grazing? Long-term capacity of Australia on `2025-improved` is 14.57 million at 0.808, 16.03 at 0.9 and 17.25 at 1.0 (`organic_livestock.mjs`).

* **There is no direct figure for meat or wool.** The one meta-analysis (Environ. Res. Lett. 16, 2021, doi 10.1088/1748-9326/abd65e, read in full): organic animal productivity is 12% (+-5%) lower overall and 14% lower for dairy cattle, but it is productivity **per animal** (milk, eggs, weight gain), from 37 comparisons, 20 of them dairy. It found **three beef comparisons and none for sheep or goats** and excluded beef; for the little beef data it says the gap is "closer to zero" than for dairy. So it supports a per-animal factor of about 0.86 to 0.88 for dairy and says nothing quantitative for ruminant meat or wool, and nothing about output per hectare.
* **Per hectare the mechanism that matters in Australia is phosphorus.** Superphosphate is synthetic and not allowed under organic standards (stated for the EU and the US; the NASAA and Australian Certified Organic standards were not retrievable, so the Australian rule is unverified); rock phosphate is allowed. Australian trials on **improved** pastures: withholding superphosphate roughly halved gross margins in a phalaris and subclover trial (CSIRO, 1977), cut steer liveweight gain by three quarters over seven years on a white clover pasture at the lowest stocking rate (NSW), and a fertilised Hunter Valley paddock carried 25 to 35% more stock (MLA PIRD.96.N11). A 25 to 35% higher carrying capacity means the unfertilised paddock carries 0.74 to 0.80 of it: the same order as 0.808.
* **But most grazing land is not fertilised.** The ABS (Agricultural Commodities 2020-21, `AGPROD_AHAGRI_F` and `AGPROD_AHAGRO_F`): of 331.9 million hectares used for grazing, **45.2 million (13.6%) is improved pasture and 286.7 million (86.4%) other land** (native and rangeland, no fertiliser, so no P penalty from going organic). The organic penalty of 0.74 to 0.80 can apply to at most the improved share of the output. If improved pasture were 14% of grazing output the ruminant factor would be 0.97; if it were half, 0.88; if all, 0.77. Improved pasture carries many more animals a hectare than rangeland, so the output share is well above the area share; this study could not find it (the ABARES farm survey by zone would give it).
* **Reading.** 0.808 is a crop number with no livestock basis, and the pasture mechanism gives a production-weighted factor between about 0.77 and 0.97, most likely 0.88 to 0.93. Raising to 0.9 is better supported than leaving 0.808; it is still an assumption (sketchy). The long-term result moves +7.9% at 0.9, +11% at 0.95; the range 0.77 to 1.0 is -4% to +16%.
* **Recycling.** The long-term setting returns human nutrients to land (recycling stage); where it supplies P the organic penalty is smaller still, but the model does not link the two.
* **Decided (Murray, 2026-10-30) and applied:** module `organic-ruminant-factor` sets Yield!G95, G96 and G98 to 0.9 in the improved line (dairy stays at its own 0.807; published and corrected lines keep 0.808). Australia, improved method: long term 14.57 to **15.75 million** (+8.1%), short term unchanged (45.70). 2011 data, improved: long 12.56 million, the module moves it by almost nothing (the 2011 long term is not bound by grazing output). The Monte Carlo should draw the factor from 0.77 to 1.0 at the next full run.
