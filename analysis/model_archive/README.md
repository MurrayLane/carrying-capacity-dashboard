# Model archive: what the original modelling folder contains

Murray Lane's working folder (`Models/`, 854 files, 1.2 GB) is kept in a separate private repository, because it holds
third-party papers and data, correspondence and a contact list that should not be public. This note records what was
found in it and which file is the final version of each thing. Everything below was checked against the files; items
marked "not examined" were not opened beyond their sheet names.

Git does not keep file dates, so versions were ordered by the save dates stored inside each workbook
(`inventory.py`) and then confirmed by comparing formulas and values (`compare_sheets.mjs`, `diff_sheet.mjs`).

## Final version of each thing

| Thing | Final file | Saved | Evidence |
|---|---|---|---|
| Model behind the 2011/12 site | `model/model.xls` in this repo (not in the folder as such) | 2012-10-17 | Closest relatives in the folder: `Carrying capacity dashboard model 021012.xls` (2012-12-19) has identical Base, Yield, Recycle, Diet and resilience formulas and values; its Settings sheet differs only in unused reference rows (long-term irrigation per region in row 152, biofuel default, total land typed rather than summed) |
| Latest standalone Excel model | `Lane_Dashboard_model.xls` | 2013-02-27 | Same Base, Yield, Diet and Recycle calculations as the site (10, 3 and 2 cell references differ only because Settings was renamed Calculations and moved down one row). Adds an interface sheet and a Defaults sheet holding both presets for all 60 zones |
| Thesis appendix tables | `Appendices.xls` | 2012-12-21 | Static values: land use, short-term and long-term inputs (thesis Tables 14 and 16 inputs), diets, climate, yields |
| Thesis results | `Results/Totals.xls` | 2014-01-26 | Thesis Table 16 (large-scale capacities for Australia and the seven states and territories) matches it exactly, all 16 short-term and long-term figures: Australia 40,439,187 and 9,431,487 |
| Food paper scenarios | `Dashboard_for_food_paper_150813.xlsx` | 2013-08-16 | The Lane model plus Tas, Aust and RESULTS sheets |
| Default inputs | `default-inputs.csv`, `default-inputs-longterm.csv` | | Identical to `data/2011/` (line endings only) |
| Full development model (food chain) | `Base model 021012.xls` | 2013-02-27 | Adds Processing loss, relative pref and Popn sheets. Not examined beyond sheet names |
| Yield data chain | `Yield data/1` to `5 NRM-all 5 years ...xls` | 2011-07 to 2011-08 | See below |

Everything in `superceded/` (about 120 files), `Results/Superceded/`, `Dashboard/Superceded/`, `Maps/Superceded/`,
`prelim models/Superceded/` and the `x`-prefixed and `(n)` copies is earlier than the files above.

## Findings that change the plan

1. **The thesis results and the online site come from two different model versions.** The thesis results come from
   the June 2012 model (last saved 2012-08-28 as `superceded/Carrying capacity dashboard model 260612.xls`). From
   October 2012 on, every file, including the one that went online, uses a different timber yield (one national
   value, 0.000894, in place of a value per region) and a different Base!K348 (0.5665 in place of 0.3624).
   `replay_totals.mjs` feeds all 120 `Totals.xls` cases through the site's evaluator: with the June variant it matches
   to 0.000% for every region and both presets; with the shipped model the short-term results match and the
   long-term results differ by up to 42%.
2. **How far apart they are.** Nationally and by state the thesis and the online site agree within about 3%
   (short-term at most 1.3%, long-term at most 3.3%, in WA). By NRM region the long-term figures differ by up to 29%
   (North Central Vic, Border Rivers-Gwydir, Murray, Wimmera, Northern and Yorke), so a regional comparison must
   say which version it uses.
3. **The defaults on the site differ from the thesis in a few places.** Thesis and `Totals.xls` use timber 0.5 m³ in
   the short-term preset (site CSV: 1) and biofuel 0.53% (CSV: 0.5%). In the long-term preset the thesis appendix
   and `Totals.xls` use textiles 11.5 kg (the workbook's own default is `=23/2`; the CSV has 12.5, which looks like
   a typo); `Totals.xls` uses infrastructure 365 m² (the appendix and the CSV have 500).
4. **The yield method is documented and now largely reproduced.** The chain is: raw ABS NRM cubes (file 1; sheets
   2006 to 2010 are 2005-06 to 2009-10, so the 2005-06 cube missing from the ABS archive is here) -> per-year t/ha with
   the file 2 adjustments (seed rates per crop in t/ha, for example wheat 0.0665, oats 0.0425, barley 0.0446, rice
   0.1475; potatoes 3 t/ha for seed; vegetable areas scaled up by 2.04%; orchard tree density per crop to turn tree
   counts into hectares, for example oranges 278.7 trees/ha, apples 640, almonds 100; cotton seed 0.0182; mushroom hay)
   -> deletions (under 10 ha or 10 t, a figure reported in only one year, or under half or over double the national
   average) -> five-year average (file 5, `Aver-add`) -> the model's Yield sheet. Checked against the files:
   - **Last stage, exact.** `yield_stage_check.py`: 5,679 of the 5,705 non-zero crop cells in the model's Yield sheet
     are reproduced to six decimals. 3,839 are the five-year average divided by (1 + 0.55 x the region's irrigation
     share), which confirms the thesis's zero-irrigation rule exactly (the earlier test could only call it consistent).
     1,840 are filled where the region has no data: the national average times the region's "major crops yield %" (the
     mean of regional/national ratios for wheat, oats, barley, sorghum, maize, canola and potatoes, skipping any the
     region does not report; thesis step 13). The 26 that differ are sheep meat, sheep wool and milk (the grazing
     method) and two tomato cells.
   - **First stage, partly.** `per_year_check.py` reproduces 74% to 89% of the computed per-year cells (seed
     deduction, vegetable area and tree density) and the under-10 ha or 10 t deletions. Not yet reproduced: the
     outlier and one-year deletions, label mismatches (herbs, parsley), mushrooms, hay, and the livestock products by
     dry sheep equivalent.
   The whole chain is now code in `pipeline/yields/`, with its own README: crops reproduce exactly, and the model's Yield sheet reproduces
   7,895 of 7,980 cells (98.9%) from the raw cubes.
   Example of the chain, Border Rivers-Gwydir wheat 2008-09: 1,403,001 t on 640,909 ha is 2.189 t/ha; less the seed
   rate 0.0665 gives 2.1226, the value in the adjusted sheet.
5. **The 2011 baseline is unaffected.** It remains the output of the servlet that was online. This archive adds the
   thesis variant as a second reference that can be reproduced exactly.

## Anomalies in the yield data (found while reproducing it)

- **The fill factor is not a cereal ratio, and is extreme for a few regions.** Thesis step 13 describes a cereal ratio; the
  workbook averages seven crops (wheat, oats, barley, sorghum, maize, canola, potatoes). That factor then scales every
  crop a region does not report, so a region with a high-yielding potato crop scales everything up: North West Tasmania
  x2.15, North Tasmania x1.66, Glenelg Hopkins x1.53. Cape York and NT rest on two crops each (x0.57, x0.73).
- **Two tomato cells were overridden by hand.** Corangamite (ABS average 212.6 t/ha, model 79.2) and region 40 (102.9,
  model 50.9). The ABS averages are glasshouse-dominated; the overrides look deliberate but are not documented.
- **Animal products differ by up to 17x between a region and the nation.** West Gippsland milk is 3.89 t/ha against a
  national 0.23. This is by design (grazing land is apportioned by dry sheep equivalent), but the national figure is
  diluted by the arid pastoral zone, so part of the large-scale versus small-scale gap in thesis Table 16 comes from
  using one national yield, not from the land.
- 221 of about 7,900 crop and animal cells are more than 3x or less than 0.2x the national value, mostly these animal products.

## Other useful material (not yet used)

- **Boundaries:** `Maps/Mapinfo_nrmr_2011_aust_midmif.zip` (NRM boundaries 2011), `Maps/NRM.kml` and `Dashboard regions.kmz`
  (the dashboard's 60 zones), `Yield data/Land use/ibra_61_and_nrm_2010.xls`. Needed for the map and the 2011 zones layer.
- **Land use and population:** `Yield data/NRM - Landuse.xls`, `Land use/NRM areas - ABS.xls`, `Nature reserve.xls`,
  `Capad08_national.xls`, `Dashboard/Correspondense/Compare ABS ACLUMP.xls`, `Summary_ABS_vs_ACLUMP.pdf`, and the
  population atlas `population re SLA.pdf` (36 pages, November 2011).
- **Diets and losses:** `Foundation diets/Foundation Selected spreadsheets.xls` (final; earlier copies are in `superceded/`),
  `Buzby - losses/`, `Kantor/`, `Apparent Consumption 99/`, `prelim models/processing yields.xls` (saved 2013-02-21,
  extraction rates with a reference PDF for each in `references re food processing yields/`).
- **Per-region results:** `Results/1a.xls` to `61b.xls` (June 2012 runs, a = short-term, b = long-term) and `Totals.xls`
  with maps and sensitivity sheets (time, food, meat, red meat, activity, waste, recycling, organic, irrigation, fuel...).
- **Interface history:** `Dashboard/` design mockups and the final text `Online text for Dashboard 060312.doc`
  with `References for Dashboard 070312.doc`.

## Not ours, or not for publishing

- Third-party: `AgriLCA_version_3...`, `Optimum popn trust/`, `Erik/`, `solver examples/`, the Cornell papers in `pdf/`
  (New York State carrying capacity), the reference PDFs in `references re ...`, `Peters Fick food data/`, ABS and ABARES files.
- Personal or private: `Dashboard/contact list.xls`, `Dashboard/Cube/` (budget and proposals), `Dashboard/Correspondense/`.
- `Models/` is also a stand-alone git repository inside the working copy of this one and is excluded from it.

`extract_thesis_release.mjs` writes the data behind the `2011-thesis` release (`data/2011-thesis/`, `baseline/thesis_totals_capacity.csv`) from the archive.

## Reproducing

```bash
cd Models && python3 -I ../analysis/model_archive/inventory.py inventory.csv          # embedded dates
node analysis/model_archive/compare_sheets.mjs model/model.xls "Models/Lane_Dashboard_model.xls"
node analysis/model_archive/diff_sheet.mjs model/model.xls "Models/Results/21b.xls" Yield 15
cd web && npm run build:data && MODELS_DIR=/path/to/Models node ../analysis/model_archive/replay_totals.mjs june
```
