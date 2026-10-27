#!/usr/bin/env python3
"""The organic yield factors (SCOPE.md E5): how the 2011 ones were made, and the update from the newer evidence.

Usage: python3 -I organic_factors.py          (from the repository root; needs xlrd)
Writes data/2025/organic_factors.json.

The 2011 factors (Yield!G, organic yield as a proportion of conventional) were recovered from `Organic/Organic comparisons for paper.xls`, sheet yield-final: the mean over the studies of the
ratio, for the 14 crops with three or more studies; for every other row the mean of all 52 crop means, 0.808. The 2011 default organic share of 2% (Settings!B15) is also the constant
inside Yield!E2, `=Settings!B15-2%`: yields come from ABS data that already include the 2% of organic land, so the multiplier on a yield is 1 - (organic share - 2%) x (1 - factor), and
equals 1 at the default.

The update:
  * Default factor 0.808. Newer evidence agrees: Ponisio et al. 2015 (Proc R Soc B 282: 20141396; 115 studies, 1,071 comparisons) found organic yields 19.2% lower, a ratio of 0.808 (95% interval 0.771 to
    0.845), and no significant difference between legumes and non-legumes or perennials and annuals; Kniss et al. 2016 (PLoS ONE 11: e0161673; commercial yields of more than 10,000 US organic farms,
    2014) found 0.80 across all crops. The 2011 default is kept.
  * Crops with a commercial ratio in Kniss et al. 2016 (wheat 0.66, oats 0.80, barley 0.76, maize 0.65, soybeans 0.68): the new factor is the mean of the 2011 literature mean and Kniss's
    commercial ratio. The literature mean comes mostly from trials and farm comparisons and Kniss from what organic farmers harvested, so each gets half.
  * Baseline organic share: Yield!E2 becomes `=Settings!B15-0.07`, the 2011 constant moved with the default (analysis/consumption_2025: 12 Mha to 44.4 Mha of certified organic land).
Not obtained: the crop-type ratios of Seufert et al. 2012 (Nature 485: 229) and the crop-specific ratios of de Ponti et al. 2012: the full texts were not reachable. Murray can supply the figures.
"""
import json, os, xlrd
ROOT = os.getcwd()
ws = xlrd.open_workbook(os.path.join(ROOT, 'model/model.xls')).sheet_by_name('Yield')
KNISS = {'Wheat': 0.66, 'Oats': 0.80, 'Barley': 0.76, 'Maize': 0.65, 'Soybeans': 0.68}
rows = {}
for r in range(3, 138):
    name = str(ws.cell_value(r, 0)).split(' (')[0].strip()
    if name in KNISS: rows[name] = (r + 1, ws.cell_value(r, 6))
out = {'baseline_share_2011': 0.02, 'baseline_share_2025': 0.07, 'default_factor': 0.808, 'ponisio_2015': {'ratio': 0.808, 'ci95': [0.771, 0.845], 'studies': 115, 'comparisons': 1071}, 'kniss_2016_all_crops': 0.80, 'crops': {}}
for name, k in KNISS.items():
    row, old = rows[name]; out['crops'][name] = {'yield_sheet_row': row, 'factor_2011': old, 'kniss_2016': k, 'factor_2025': round((old + k) / 2, 4)}
json.dump(out, open(os.path.join(ROOT, 'data/2025/organic_factors.json'), 'w'), indent=1)
for n, v in out['crops'].items(): print(f"{n:9s} row {v['yield_sheet_row']:2d}  2011 {v['factor_2011']:.3f}  Kniss {v['kniss_2016']:.2f}  new {v['factor_2025']:.3f}")
