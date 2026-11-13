# B93: one-route check of the gap-attribution rows; the Cassidy test with harvests matched (decision 88)

Builder: B93 under `qa/briefs/B93_gap_attribution_and_cassidy.md`. Read: `qa/reports/V31a_claims.md` (FAOSTAT year finding), `qa/reports/V32b_logic_B.md` problem 10, `analysis/method_tests_2025/README.md` (Gap attribution; Cassidy), `gap_attribution.py`, `cassidy_people_per_hectare.py`, `qa/claims_register.csv` rows B278 to B332 (read only). The claims register was not edited.

Bulk files used: `Production_Crops_Livestock_E_All_Data_(Normalized).csv` (sha256 c4ff713e...cac01) and `FoodBalanceSheets_E_All_Data_(Normalized).csv` (sha256 2834e101...fa020); both match `qa/fao_bulk_hashes.csv`.

Scratch (own scripts and outputs): `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/B93/`: `pull_qcl.py`, `pull_fbs.py`, `pull_qcl2.py` (subsets of the two bulk files), `gap_check.py` and `gap_check_out.txt` (part 1), `lag_test.py` and `lag_detail.py` (lag per item over 2011 to 2023), `wrong_value.py` (wrong-value check).

## Summary

* B278 to B332: 55 rows; **34 pass, 21 pass with a note, 0 fail.** Only the Henry and Godden residuals (B301 to B304, B321, B322) lie within the rounding of the published figure; their percent-of-residual shares (+731%, -24%, -3%, +234%, -779%, -239%) should read "within rounding". The HALF, Simpson, Foran and Poldy and Cassidy residuals are all larger than the rounding of the published figure, so their shares stand.
* V32b problem 10 also proposed "within rounding" for Foran and Poldy. That does not hold: the published 31.578 and 3.514 Mt are printed to 0.001 Mt and the residuals are 0.372 and 0.043 Mt.
* Cassidy with harvests matched: **Australia 2021-23 delivered 6.01 as paired, 5.78 matched (-3.8%); produced 10.49 against 10.08 (-3.9%).** On 2022-23 alone: 6.39 against 6.00 (-6.1%), the same as V31a. **The world does not change (7.87 on 2021-23, 7.92 on 2022-23).** No item in the world totals is lagged. The 2020 harvests were extracted from the hashed bulk file, so the full 2021-23 window is matched.

## 1. Gap attribution, B278 to B332

Route. A short script of my own (`gap_check.py`) recomputes each share as (figure - current) / (published - current) x 100. It never reads the "explained %" or "residual" cell. Figures come from the inputs where the inputs are plain arithmetic:
* Henry and Godden: Tables 2, 4 and 5 totals as typed.
* Simpson: ABS 4306.0 and the thesis rates as typed.
* Foran and Poldy: own sums of "Cereals, primary", "Meat, Total" and the listed items from the hashed bulk file.
* Cassidy produced: own sum of food-balance production x kcal x (yield of 1997 to 2003 or 2000 over yield of 2011) over 2011 harvested area, using the extracts and the bulk file.

For HALF and the Cassidy delivered rows there is no own build, so the figure is taken from the csv's figure column. For these rows the share is also bounded by the rounding of the csv's figure and current columns (HALF writes two decimals), and the range is shown.

Own current figures agree with the csv's current column:
* Henry and Godden: 108.912 and 95.6635.
* Simpson: 1.7176.
* Foran and Poldy: 31.9505 and 3.4709.
* Cassidy produced, 2011: world 12.325, United States 20.967, India 8.817, China 18.423, Brazil 14.146.

"Within rounding" means that the residual is no more than half a unit of the published figure's last printed digit.

Tolerance, set before comparing: a figure must be within half a unit of its last printed digit, and a share within one unit of the printed whole percent (or inside the column-precision range plus that unit).

| Row | Stated (figure; share) | Own (figure; share; range) | Route | Residual against the published rounding | Verdict | Note |
|---|---|---|---|---|---|---|
| B278 | [112.74, 42] | [112.74, 41.3, '[40.4, 42.2]'] | csv figure, current, published columns | outside rounding | pass with note | share confirmed only to the precision of the csv's 2-decimal figure and current columns (range shown); figure taken from the csv, no own HALF build |
| B279 | [118.88, -622] | [118.88, -626.09, '[-630.6, -621.6]'] | csv figure, current, published columns | outside rounding | pass with note | share confirmed only to the precision of the csv's 2-decimal figure and current columns (range shown); figure taken from the csv, no own HALF build |
| B280 | [113.15, -3] | [113.15, -3.26, '[-4.4, -2.2]'] | csv figure, current, published columns | outside rounding | pass with note | share confirmed only to the precision of the csv's 2-decimal figure and current columns (range shown); figure taken from the csv, no own HALF build |
| B281 | [113.11, 2] | [113.11, 1.09, '[0.0, 2.2]'] | csv figure, current, published columns | outside rounding | pass with note | share confirmed only to the precision of the csv's 2-decimal figure and current columns (range shown); figure taken from the csv, no own HALF build |
| B282 | [113.2, -8] | [113.2, -8.7, '[-9.8, -7.6]'] | csv figure, current, published columns | outside rounding | pass with note | share confirmed only to the precision of the csv's 2-decimal figure and current columns (range shown); figure taken from the csv, no own HALF build |
| B283 | [115.88, -298] | [115.88, -300.0, '[-302.7, -297.3]'] | csv figure, current, published columns | outside rounding | pass with note | share confirmed only to the precision of the csv's 2-decimal figure and current columns (range shown); figure taken from the csv, no own HALF build |
| B284 | [113.15, -3] | [113.15, -3.26, '[-4.4, -2.2]'] | csv figure, current, published columns | outside rounding | pass with note | share confirmed only to the precision of the csv's 2-decimal figure and current columns (range shown); figure taken from the csv, no own HALF build |
| B285 | [34.06, -40] | [34.06, -40.79, '[-42.4, -39.2]'] | csv figure, current, published columns | outside rounding | pass with note | share confirmed only to the precision of the csv's 2-decimal figure and current columns (range shown); figure taken from the csv, no own HALF build |
| B286 | [35.76, 183] | [35.76, 182.89, '[181.7, 184.1]'] | csv figure, current, published columns | outside rounding | pass with note | share confirmed only to the precision of the csv's 2-decimal figure and current columns (range shown); figure taken from the csv, no own HALF build |
| B287 | [34.88, 67] | [34.88, 67.11, '[66.2, 68.0]'] | csv figure, current, published columns | outside rounding | pass with note | share confirmed only to the precision of the csv's 2-decimal figure and current columns (range shown); figure taken from the csv, no own HALF build |
| B288 | [34.38, 2] | [34.38, 1.32, '[0.0, 2.6]'] | csv figure, current, published columns | outside rounding | pass with note | share confirmed only to the precision of the csv's 2-decimal figure and current columns (range shown); figure taken from the csv, no own HALF build |
| B289 | [94.1, -14] | [94.1, -14.15, '[-14.5, -13.8]'] | csv figure, current, published columns | outside rounding | pass |  |
| B290 | [99.13, 144] | [99.13, 144.03, '[143.8, 144.3]'] | csv figure, current, published columns | outside rounding | pass |  |
| B291 | [109.34, -6] | [109.34, -5.52, '[-5.7, -5.3]'] | csv figure, current, published columns | outside rounding | pass |  |
| B292 | [115.36, 109] | [115.36, 109.14, '[109.0, 109.2]'] | csv figure, current, published columns | outside rounding | pass |  |
| B293 | [14.42, -19] | [14.42, -18.58, '[-19.6, -17.6]'] | csv figure, current, published columns | outside rounding | pass with note | share confirmed only to the precision of the csv's 2-decimal figure and current columns (range shown); figure taken from the csv, no own HALF build |
| B294 | [15.07, 39] | [15.07, 38.94, '[38.2, 39.6]'] | csv figure, current, published columns | outside rounding | pass with note | share confirmed only to the precision of the csv's 2-decimal figure and current columns (range shown); figure taken from the csv, no own HALF build |
| B295 | [1.713, -12] | [1.7126, -12.48, '[-12.5, -12.5]'] | own inputs | outside rounding | pass with note | README table prints -13% (generator rounds the csv -12.5 again); unrounded -12.48, so -12 is right |
| B296 | [1.291, -1057] | [1.2913, -1056.56, '[-1056.6, -1056.6]'] | own inputs | outside rounding | pass |  |
| B297 | [1.788, 175] | [1.7883, 175.13, '[175.1, 175.1]'] | own inputs | outside rounding | pass |  |
| B298 | [1.778, 149] | [1.7779, 149.42, '[149.4, 149.4]'] | own inputs | outside rounding | pass |  |
| B299 | [1.74, 56] | [1.7403, 56.23, '[56.2, 56.2]'] | own inputs | outside rounding | pass |  |
| B300 | [1.73, 30] | [1.7296, 29.5, '[29.5, 29.5]'] | own inputs | outside rounding | pass |  |
| B301 | [108.89, -24] | [108.8908, -24.15, '[-24.2, -24.2]'] | own inputs | within rounding | pass with note | residual 0.09 is within the rounding of 109: print "within rounding", not a share |
| B302 | [109.55, 731] | [109.5548, 730.66, '[730.7, 730.7]'] | own inputs | within rounding | pass with note | residual 0.09 is within the rounding of 109: replace +731% with "within rounding" |
| B303 | [95.65, -3] | [95.6549, -2.56, '[-2.6, -2.6]'] | own inputs | within rounding | pass with note | residual 0.34 is within the rounding of 96: print "within rounding", not a share |
| B304 | [96.45, 234] | [96.452, 234.33, '[234.3, 234.3]'] | own inputs | within rounding | pass with note | residual 0.34 is within the rounding of 96: replace +234% with "within rounding" |
| B305 | [31.28, 180] | [31.2797, 180.09, '[180.1, 180.1]'] | own inputs | outside rounding | pass |  |
| B306 | [32.85, -243] | [32.8546, -242.75, '[-242.8, -242.8]'] | own inputs | outside rounding | pass with note | README table prints 32.86 (double rounding of 32.855); unrounded 32.8546, so 32.85 is right |
| B307 | [30.59, 365] | [30.591, 365.0, '[365.0, 365.0]'] | own inputs | outside rounding | pass |  |
| B308 | [3.6, 303] | [3.6013, 302.67, '[302.7, 302.7]'] | own inputs | outside rounding | pass |  |
| B309 | [3.53, 129] | [3.5266, 129.35, '[129.4, 129.4]'] | own inputs | outside rounding | pass |  |
| B310 | [10.7, 72] | [10.7268, 71.83, '[71.8, 71.8]'] | own inputs | outside rounding | pass |  |
| B311 | [6.5, 64] | [6.5426, 63.68, '[63.7, 63.7]'] | csv figure, current, published columns | outside rounding | pass |  |
| B312 | [7.3, 12] | [7.3193, 11.69, '[11.7, 11.7]'] | csv figure, current, published columns | outside rounding | pass |  |
| B313 | [6.4, 74] | [6.3911, 73.82, '[73.8, 73.8]'] | csv figure, current, published columns | outside rounding | pass |  |
| B314 | [19.3, 35] | [19.2771, 34.72, '[34.7, 34.7]'] | own inputs | outside rounding | pass |  |
| B315 | [7.3, 64] | [7.3436, 63.59, '[63.6, 63.6]'] | own inputs | outside rounding | pass |  |
| B316 | [16.0, 50] | [15.9537, 50.15, '[50.2, 50.2]'] | own inputs | outside rounding | pass |  |
| B317 | [11.2, 82] | [11.2266, 82.33, '[82.3, 82.3]'] | own inputs | outside rounding | pass |  |
| B318 | [1535, 1556, 1318, 1378, 3182, 3364, 1.165, 1.129] | [1535.14, 1556.0, 1317.52, 1378.0, 3182.08, 3364.0, 1.1652, 1.1292] | csv columns (other than the cited cell) |  | pass |  |
| B319 | [1147, 1515, 438, 504] | [1146.79, 1515.4, 437.56, 504.4] | csv columns (other than the cited cell) |  | pass |  |
| B320 | [7.9] | ['largest interval Australia 2011 b4 [7.6, 9.8]', '1 of 25 intervals reach 8'] | csv columns (other than the cited cell) |  | pass with note | on the 2-decimal csv columns Australia b4 lies between 7.6% and 9.8%; "less than 8%" rests on the script's unrounded 7.9 |
| B321 | [18, 67, 8, 22] | [17.593, 67.2998, 7.5274, 22.3764] | own inputs | within rounding | pass | own Henry and Godden chain: 108.912 and 95.664; totals 205.96 and 187.89 |
| B322 | [108.23, 109.55, 94.86, 96.45, -779, 731, -239, 234] | [108.2268, 109.5548, 94.8578, 96.452, -778.9636, 730.6557, -239.446, 234.3292] | own inputs | within rounding | pass with note | arithmetic holds; both residuals are within rounding, so drop the four shares and keep the figures |
| B323 | [34.0, 1.7175, 33.22] | [34.0025, 1.7175, 33.2196] | own inputs |  | pass |  |
| B324 | [1.2913, 1.3222, -1057, -980] | [1.2913, 1.3222, -1056.5598, -980.0292] | own inputs |  | pass |  |
| B325 | [2638, 106, 57, 186, 175] | [2637.6278, 106.436, 57.1009, 186.4, 175.1287] | own inputs |  | pass |  |
| B326 | [31.95, 31.578, 3.471, 3.514, -0.372, 0.043, 1.2, 1.2] | [31.9505, 31.578, 3.4709, 3.514, -0.3725, 0.0431, 1.1795, 1.2255] | own inputs | outside rounding | pass | residuals are outside the rounding of 31.578 and 3.514 (half unit 0.0005 Mt): "within rounding" does not apply to Foran and Poldy |
| B327 | [-243, -301, -216, 129] | [-242.7502, -300.9212, -215.7185, 129.3524] | own inputs | outside rounding | pass |  |
| B328 | [34.37, -650, 3.44, -70] | [34.3717, -650.0993, 3.4408, -69.9482] | own inputs | outside rounding | pass |  |
| B329 | [75, 27, 65, 56, 99, 65] | [74.858, 27.4197, 65.3455, 56.2345, 99.1209, 65.1851] | own inputs (produced); csv columns (world delivered) |  | pass |  |
| B330 | [28] | [27.7056] | csv columns (other than the cited cell) |  | pass |  |
| B331 | [0, 0, 0, 0, 0] | [-0.0, -0.0, -0.0, -0.0, -0.0] | csv columns (other than the cited cell) |  | pass |  |
| B332 | [22, 42] | [22.0297, 42.256] | csv columns (other than the cited cell) |  | pass | smallest World produced 1.220, largest China delivered 1.423 |

Tally: **34 pass, 21 pass with a note, 0 fail.**
* The 21 rows with a note are:
  * B278 to B288, B293 and B294: the share is confirmed only to the precision of the csv columns.
  * B320: the 2-decimal columns cannot settle "less than 8%".
  * B301 to B304 and B322: within rounding, so they need rewording.
  * B295 and B306: the register value is right but the README table prints a double-rounded value.
* All rows are "unverified" in the register. The proposed status for B95 is "one-route checked (B93)", with the notes above.

Register layout defect, for B95: from B318 to B332 the fields after `unit` are shifted by one column. `unit` holds the README locator, `output_locator` holds the unit, `depends_on` holds the csv locator and `notes` holds the related ids. B278 to B317 are laid out correctly.

### "Within rounding" wording for the rows that need it

* B301: "...with the factor 82/466 unrounded the figure is 108.89 against this test's 108.91 and the published 109; the residual (0.09) is within the rounding of the published whole number."
* B302: "...with Gifford's projected 82 at its rounding bound, 82.5, the figure is 109.55 against this test's 108.91 and the published 109; the residual is within rounding, so no share of it is given." This replaces +731%.
* B303: as B301 for protein (95.65 against 95.66 and 96; residual 0.34, within rounding).
* B304: as B302 for protein (96.45; replaces +234%).
* B322: "Moving Gifford's projected population to either edge of its rounding moves the energy figure to 108.23 or 109.55 and the protein figure to 94.86 or 96.45, 0.6 to 0.8 million either way; both residuals are within the rounding of the published whole numbers." This drops -779%, +731%, -239% and +234%.

## 2. README gap-attribution lines to reword (not edited here; B95)

Line numbers are those of `analysis/method_tests_2025/README.md` after this job's Cassidy paragraph. That paragraph added two lines above the section. Lines 384 to 395 sit in the generated table (`make_readme_tables.py`, `t_gap_attribution`), so the change belongs in the generator, not in the README text.

| Line | Prints | Should print | Why |
|---|---|---|---|
| 390 | Henry and Godden energy, (b) 82/466 unrounded: -24% | within rounding | residual 0.09 against half a unit of 109 |
| 391 | Henry and Godden energy, (b) 82.5: +731% | within rounding | same |
| 392 | Henry and Godden protein, (b) 60/294 unrounded: -3% | within rounding | residual 0.34 against half a unit of 96 |
| 393 | Henry and Godden protein, (b) 60.5: +234% | within rounding | same |
| 410 | "Moving either projected population to the edge of its rounding moves the result by several times the residual." | "Moving either projected population to the edge of its rounding moves the result by 0.6 to 0.8 million; the residuals themselves are within the rounding of the published whole numbers." | a multiple of a within-rounding residual carries no information |
| 384 | Simpson (a) sheep-meat rate 34.1: -13% | -12% | the generator rounds the csv's already-rounded -12.5 (unrounded -12.48); register B295 has -12 |
| 395 | Foran and Poldy (b) three-year mean 1996 to 1998: 32.86 | 32.85 | the same double rounding of 32.855 (unrounded 32.8546); register B306 has 32.85 |

Generator rule suggested for B95:
* Print "within rounding" when the residual is within half a unit of the published figure's last digit.
* Round from the script's unrounded values, not from the csv's rounded cells. Writing one more digit to the csv would do this, but it needs a new csv name, as existing csvs are not overwritten.

No other gap-attribution prose repeats a within-rounding share. The Foran and Poldy prose (line 413: "two to three times its residual", -243%, -301%, -216%, 129%) is about residuals outside rounding and can stand. The "Wording for the papers" paragraph (line 416) already says Henry and Godden are "reproduced within the rounding".

## 3. Lag per item (food balance against crops file)

Test: food-balance production of year N against crops-file production of year N (lag 0) and of N-1 (lag 1). The gap is a share of the crops-file figure.
* Long run (`lag_test.py`, `lag_detail.py`): median over N = 2011 to 2023, with a count of the years matching within 0.1%.
* In the script (`--match-harvests`): mean over N = 2021 to 2023. An item is lagged when its N-1 gap is under 5% and under half its same-year gap.
* Sugar is compared with the crops file's "Raw cane or beet sugar (centrifugal only)", sugar with sugar, because cane tonnes are not sugar tonnes.

**Australia**

| Item | Long run: median gap lag 0 / lag 1 (exact years of 13) | Script 2021-23: mean gap lag 0 / lag 1 | Lag |
|---|---|---|---|
| Wheat | 19.0% / 0.00% (0 / 13) | 23.65% / 0.00% | **1** |
| Barley | 10.0% / 0.00% (0 / 13) | 10.51% / 0.00% | **1** |
| Oats | 10.7% / 0.01% (0 / 13) | 40.13% / 0.01% | **1** |
| Rape and mustardseed (canola) | 23.5% / 0.01% (0 / 13) | 24.21% / 0.00% | **1** |
| Pulses, other (chickpeas, lentils, faba beans, lupins, vetches, each lag 1) | 15.9% / 2.5% | 23.74% / 2.61% | **1** |
| Rice | 0.04% / 29.5% (11 / 0) | 0.05% / 277.9% | 0 |
| Maize | 0.06% / 15.6% (9 / 0) | 0.08% / 21.7% | 0 |
| Sorghum | 0.01% / 28.4% (12 / 0) | 0.01% / 128.7% | 0 |
| Peas, dry | 0.07% / 23.7% (7 / 1) | 0.06% / 48.1% | 0 (a winter crop, but booked in the same year) |
| Rye | 0.8% / 1.6% | 1.11% / 0.94% | 0 (food-balance figure rounded to the 1,000 t; long run nearer lag 0) |
| Millet | 0.9% / 0.8% | 0.59% / 0.39% | 0 (flat series rounded to 36,000 to 37,000 t; cannot be told apart; under 0.04 Mt) |
| Cereals, other | 21.7% / 20.6% | 21.19% / 61.26% | 0 (triticale same year, plus about 30 to 35 kt the crops file does not hold) |
| Potatoes | 0.02% / 7.6% (11 / 1) | 12.41% / 13.94% | 0 |
| Sweet potatoes | 14.9% / 14.5% | 10.31% / 13.06% | 0 (food balance imputed from 2015; exact same-year in 2011 to 2014) |
| Beans, dry | 0.5% / 17.0% (6 / 0) | 17.29% / 26.78% | 0 |
| Groundnuts | 1.5% / 23.2% | 1.65% / 27.15% | 0 |
| Soyabeans | 0.8% / 12.9% | 0.30% / 60.57% | 0 |
| Sunflower seed | 0.7% / 19.1% | 0.38% / 59.03% | 0 |
| Sugar (raw equivalent) | against raw sugar, same year exact (4,188 kt 2023; 4,123 kt 2022) | 0.00% / 2.56% | 0 |
| Cassava, yams, other roots | no Australian production | | n/a |

V31a found the lag for wheat, barley and oats. This test adds **canola (rapeseed) and the winter pulses other than field peas**, both also lagged. Sorghum and meat are not lagged, as V31a said.

**World totals.** For every item the same-year gap is the smaller. For example, wheat is 0.87% against 1.61% and barley 1.31% against 7.47% (2021-23). No item matches the year before. The world food balance is a sum of country balances, of which only the southern-hemisphere winter crops are lagged, so no whole item can be shifted. In the world, every item is lag 0.

## 4. Cassidy, paired and matched

Changes made:
* `cassidy_people_per_hectare.py` has a new `--match-harvests` option. It writes `analysis/method_tests_2025/cassidy_matched.csv` only, and refuses to overwrite an existing file. The plain run is unchanged: a rerun in scratch gives a `cassidy.csv` byte-identical to the committed one, and `gap_attribution.py`, which runs the Cassidy script as a side calculation, still reproduces `gap_attribution.csv` byte for byte.
* `extract_fao_countries.py` has a new `--years` option. Its default output is byte-identical to `fao_qcl_countries.csv`. With `--years` it checks the bulk file's sha256 against `qa/fao_bulk_hashes.csv` and does not overwrite an existing output.
* That option wrote `analysis/method_tests_2025/fao_qcl_countries_2020.csv`: 1,863 rows, sha256 69ef6140...474b5b.

Without that file, the matched run falls back to 2022-23 and says so.

| Window | Country | Pairing | Lagged items | Cropland (Mha) | People a ha, produced | People a ha, delivered | People fed (million) |
|---|---|---|---|---|---|---|---|
| 2021-23 | Australia | same year (as `cassidy.csv`) | none | 24.53 | 10.49 | **6.01** | 147.4 |
| 2021-23 | Australia | harvest-matched | wheat, barley, oats, pulses other, rapeseed | 25.51 | 10.08 | **5.78** | 147.4 |
| 2021-23 | World | same year | none | 1,161.76 | 13.69 | **7.87** | 9,146.8 |
| 2021-23 | World | harvest-matched | none (no world item lagged) | 1,161.76 | 13.69 | **7.87** | 9,146.8 |
| 2021-23 | World | sensitivity: Australia's lagged items shifted | as Australia | 1,161.97 | 13.69 | 7.87 | 9,146.8 |
| 2022-23 | Australia | same year | none | 23.99 | 11.28 | 6.39 | 153.2 |
| 2022-23 | Australia | harvest-matched | as above | 25.55 | 10.59 | 6.00 | 153.2 |
| 2022-23 | World | same year | none | 1,164.37 | 13.72 | 7.92 | 9,217.0 |
| 2022-23 | World | harvest-matched | none | 1,164.37 | 13.72 | 7.92 | 9,217.0 |
| 2022-23 | World | sensitivity: Australia's lagged items shifted | as Australia | 1,162.95 | 13.74 | 7.93 | 9,217.0 |

Change for Australia 2021-23:
* Delivered falls from 6.01 to 5.78 (-3.8%) and produced from 10.49 to 10.08 (-3.9%). The matched area is 4% larger: the 2020 winter crop was large and the food balance books it in 2021.
* People fed (147.4 million) do not change, since no area enters them.
* The all-cropland reading becomes 5.776 x 31.65 = 182.8, about 183 million, in place of about 190.
* The grain-fed beef range (0 to 100%) becomes 5.9 to 5.6 in place of 6.1 to 5.8.

On 2022-23 the matched figures reproduce V31a: 6.39 paired and 6.00 matched. V31a's world "7.97 matched" is not reproduced. On the world data no world item is lagged, so the world matched figure equals the paired one (7.92). Shifting Australia's lagged items in the world totals as well gives 7.93, a change of under 0.2%.

README: a short paragraph, "**Harvest matching (B93, decision 88)**", was added to the Cassidy section before "Limits" (line 204). It gives both figures. No other README text was changed.

## 5. Claim rows that change (for B95; register not edited)

Harvest matching (Cassidy, Australia):

| Id | Tier | Before | After |
|---|---|---|---|
| B081 | B | 6.0 delivered (10.5 produced); value "5.8 to 6.0 delivered, 10.0 to 10.5 produced" | 5.8 delivered (10.1 produced) harvest-matched, 6.0 and 10.5 on same-year pairing; state the pairing. If the second build's 5.77 (V05) keeps same-year pairing, compare it with the 6.0 |
| B084 | A | about 190 million on all 31.65 Mha | about 183 million harvest-matched (190 on same-year pairing). Tier A, so to Murray first |
| B085 | B | 0 to 100% beef moves 6.1 to 5.8 | 5.9 to 5.6 harvest-matched (6.1 to 5.8 same-year). The pairing moves the figure by 0.23, about as much as the whole beef range (0.32 to 0.31) |
| B273 | A | the all-cropland reading of 190 falls to 112.9 (factor 0.594) | 183 falls to 112.9 (factor 0.618) harvest-matched. 112.9, 110.9 and 0.766 do not change. Tier A, so to Murray first |
| B258 | B | Australia 5.77 against 6.0 (within 5%) | wording only: state that both figures use same-year pairing; harvest-matched, the project's figure is 5.78 |

No change: B082 (world 7.9 on both pairings), B083 (147 million; no area enters it), B259 (people count).

Gap attribution (statuses for all of B278 to B332; wording for these):

| Id | Tier | Before | After |
|---|---|---|---|
| B301 | B | 108.89; -24 | 108.89; within rounding |
| B302 | B | 109.55; +731 | 109.55; within rounding |
| B303 | B | 95.65; -3 | 95.65; within rounding |
| B304 | B | 96.45; +234 | 96.45; within rounding |
| B322 | B | 108.23; 109.55; 94.86; 96.45 with -779%, +731%, -239%, +234% in the statement | same four figures; shares dropped, "within rounding" |
| B278 to B332 | B | status "unverified" | "one-route checked (B93)": pass for 34, pass with a note for 21 (section 1) |
| B318 to B332 | B | fields after `unit` shifted by one | realign (layout only) |

## Register rows touched

None. This job wrote:
* `qa/reports/B93_gap_attribution_and_cassidy.md`
* `analysis/method_tests_2025/cassidy_matched.csv` (new)
* `analysis/method_tests_2025/fao_qcl_countries_2020.csv` (new)

It edited:
* `analysis/method_tests_2025/cassidy_people_per_hectare.py` (`--match-harvests`)
* `analysis/method_tests_2025/extract_fao_countries.py` (`--years`)
* `analysis/method_tests_2025/README.md` (one Cassidy paragraph)

No existing output csv was overwritten.

## Wrong-value check

Wrong-value check: EXAMPLE ONLY, not a finding. `wrong_value.py` fed the same comparison code two deliberately wrong values:
* B302's share as +713 in place of +731. Own value 730.7: printed FAIL.
* B310's figure as 10.9 in place of 10.7. Own value 10.73: printed FAIL.

So the comparison can fail. The same code then printed pass for the 55 register rows.
