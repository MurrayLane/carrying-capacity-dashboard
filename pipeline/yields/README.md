# Yield pipeline

The method that turns agricultural statistics into the regional yields the model uses, written as code and checked against
the original workbooks. It is the method of thesis section 8.1 with the numbers and decisions the thesis does not state.
A refresh runs new data through the same stages; nothing in the method changes (SCOPE.md D1).

```
raw cube (ABS, per year) --1--> t/ha per commodity and zone, per year --2--> five-year average --3--> model Yield sheet (g/m2)
```

| Stage | Code | What it does |
|---|---|---|
| 1 crops | `yields.py` | t/ha = tonnes / hectares, where trees become hectares at a recorded density (oranges 278.7 trees/ha, apples 640, almonds 100 and so on), vegetable area is scaled up 2.04%, seed is deducted in t/ha (wheat 0.0665, oats 0.0425, potatoes 3.0 and so on), mushrooms are divided by 839 |
| 1 animals | `livestock.py` | The land under grazing and hay is shared among a zone's animals by dry sheep equivalent (DSE); each product's yield is its production over its share of that land (plus feedlot land and grain). Poultry, pigs and fish are the mean of seven grain and oilseed yields over a feed conversion ratio |
| 2 | `average.py` | Five-year mean as the workbook computes it: a missing year is left out, a year that gives 0 counts as 0 |
| 3 | `fill.py` | Where a pair is marked suitable and has no average, the national average times the zone's "major crops yield %" (the mean zone/national ratio over wheat, oats, barley, sorghum, maize, canola and potatoes); then every figure is divided by (1 + 0.55 x the zone's irrigation share) and converted to g/m2 |

## Checked against the archive

`verification_output.txt` (needs the private archive: `MODELS_DIR=/path/to/Models python3 -I verify_<name>.py`).

| Check | Result |
|---|---|
| `verify_crops.py`: raw cubes to the adjusted year sheets, 91 crop rows, five years | **every populated cell matches, 8,051 of 8,051** (to nine digits) |
| `verify_livestock.py`: file 4 class counts to the animal-product rows | 3,108 of 3,134 populated cells match (99.2%); the other 26 are regions where the workbook's grain average is undefined or differs slightly |
| `verify_average.py`: year sheets to the five-year averages | 3,010 of 3,015 (99.8%); 5 dairy cells |
| `verify_end_to_end.py`: raw cubes to the model's Yield sheet, 133 commodities x 60 zones | **7,895 of 7,980 cells exactly (98.9%)**; every crop row matches, the 85 differences are animal products and the two derived milk rows |

`test_yields.py` holds the method's arithmetic on small invented cubes and runs in CI without the archive.

## What is recorded as data, not rebuilt as a rule

These are decisions or inputs in the original work that no formula reproduces. Each is a file here, with its source, and each is
what a refresh has to replace or re-decide.

| File | What | For a refresh |
|---|---|---|
| `archive_deletions.json` | Cells removed as unreliable (file 3), and the later removals made with the file 5 diagnostic sheets and judgement. The thesis states a 10 ha / 10 t minimum and removal of ABS-flagged figures; the archive applies no numeric threshold | Apply the ABS reliability flags (relative standard error) and the documented flags: a figure reported in one year only and under half or over double the national value; two years only and under a tenth of it |
| `archive_fill_mask.json` | The 1,842 commodity-zone pairs the author judged climatically suitable for filling | A rule or a fresh, documented judgement |
| `archive_derived_yields.json` | 31 derived commodities (berries, melons, grouped citrus and stone fruit, buckwheat = wheat x 0.75, quinoa, rye, spelt, nuts, herbs, tropical crops, honey, goat and sheep milk) | Rebuild from their national estimates (the Ag yield sheet of file 5) |
| `archive_livestock_inputs.json` | Class counts, feedlot numbers, grazing and hay area, milk by zone and the national production totals, per year, as harmonised in each year's sheet | New data, harmonised to the same classes |
| `archive_livestock_parameters.json` | DSE factors, feed conversion ratios, feedlot land per head (identical in all five years) | Keep, or revise as a method change |
| `method.json` | Seed rates, area increases, trees per hectare | Keep; add commodities as the ABS adds them |

`extract_method.py` writes all of these from the original workbooks.

## Known gaps

- The ABS item definitions changed between years, and the original workbook harmonised them differently in 2006 and 2007, 2008 and 2010,
  and 2009. The pipeline takes the harmonised classes as they stand; a refresh needs its own harmonising step for the new cubes.
- The mushroom divisor is 839.0 in the year sheets; the adjustments file records 837.8 (a 0.14% difference in the original files).
- The thesis describes the fill as a cereal ratio; the workbook averages seven crops (see `analysis/model_archive/README.md` for the effect).
