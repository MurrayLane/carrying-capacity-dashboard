#!/usr/bin/env python3
"""2011 window subsets (B138 item 6; R05a issue 21; R04b question 4 on the 2011 side).

The 2011 yields are the five-year mean of the archive years 2006 to 2010 (ABS years 2005-06 to 2009-10). 2025's crop window is three years (2022-23 to 2024-25), so this
rebuilds the 2011 yield sheet from each three-year subset of the five archive years (all 10 subsets; the 3 consecutive ones are marked) and evaluates the capacity of release
2011-fixed-3 with those yields. Only the yields change: land, population, diet and method are those of 2011-fixed-3 in every run.

How: the pipeline (pipeline/yields: stage 1 crops and animals, stage 2 mean, stage 3 fill and irrigation conversion) is run on the chosen years, and again on all five years. Each
yield of release 2011-fixed-3 is multiplied by (subset yield / five-year yield) from the pipeline, so the pipeline's own small mismatch with the thesis workbook (85 of 7,980 cells,
pipeline/yields/verification_output.txt) cancels. A cell the five-year run has and the subset run lacks becomes 0 (the zone has no figure in those years and no fill rule supplies one);
a cell the five-year run lacks keeps the release value. Rows 134 to 138 of the release (not in the pipeline) keep the release value.

Needs the private archive: MODELS_DIR=/path/to/Models python3 -I analysis/paper_a/window_subsets_2011.py    (run from the repository root; needs xlrd and node with web/node_modules)
Writes analysis/paper_a/window_subsets_2011.csv, window_subsets_2011_summary.csv and window_subsets_2011_cells.csv (same folder). Deterministic: no random numbers.
"""
import os, sys, re, json, csv, itertools, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'pipeline', 'yields'))
import xlrd
from yields import read_cube, crop_year, norm
from livestock import livestock_year, PRODUCTS
from average import five_year_average
from fill import model_yield

RELEASE = '2011-fixed-3'
YEARS = (2006, 2007, 2008, 2009, 2010)                      # sheet labels; 2006 = ABS 2005-06
LABEL = {2006: '2005-06', 2007: '2006-07', 2008: '2007-08', 2009: '2008-09', 2010: '2009-10'}
D = os.path.join(os.environ['MODELS_DIR'], 'Yield data')
f1 = xlrd.open_workbook(os.path.join(D, '1 NRM-all 5 years - all t and ha.xls')); f5 = xlrd.open_workbook(os.path.join(D, '5 NRM-all 5 years - average.xls'))
DEL = json.load(open(os.path.join(REPO, 'pipeline/yields/archive_deletions.json'))); LS = json.load(open(os.path.join(REPO, 'pipeline/yields/archive_livestock_inputs.json')))['years']
derived = json.load(open(os.path.join(REPO, 'pipeline/yields/archive_derived_yields.json')))['rows']
irr = {int(r['regionId']): float(r['irrigation']) for r in csv.DictReader(open(os.path.join(REPO, 'data/2011/default-inputs-short-term.csv')))}
FILL = {(int(r) - 2, z) for r, zs in json.load(open(os.path.join(REPO, 'pipeline/yields/archive_fill_mask.json')))['fillCells'].items() for z in zs}
adjt0 = f5.sheet_by_name('2009-adjt'); labels = {r: str(adjt0.cell_value(r, 0)) for r in range(1, 103)}
bases = {r: re.sub(r'\s*\(t/ha\)\s*$', '', labels[r]).strip() for r in range(1, 92)}

per_year = {r: {} for r in range(1, 103)}                    # row -> year -> per-zone list
for y in YEARS:
    cube = read_cube(f1.sheet_by_name(str(y)))
    m_all = {(l, c) for l, c in DEL['unreliable'][str(y)]}
    m_later = m_all | {(norm(b + s), c) for b, c in DEL['later'][str(y)] for s in (' (ha)', ' trees (n)', ' (t)', ' lint (t)')}
    for r in range(1, 92): per_year[r][y] = crop_year(cube, bases[r], m_later)
    feedcrops = {b: crop_year(cube, b, m_all) for b in ('Wheat', 'Oats', 'Barley', 'Sorghum', 'Maize', 'Canola', 'Soybeans')}
    ls = livestock_year(LS[str(y)], feedcrops)
    for i, p in enumerate(PRODUCTS): per_year[92 + i][y] = ls[p]


def sheet_for(years):
    avg = {r: five_year_average([per_year[r][y] for y in years]) for r in per_year}
    for r, vals in derived.items(): avg[int(r)] = [None] + vals          # recorded data, the same in every subset
    return model_yield(avg, irr, FILL)


full = sheet_for(YEARS)
RJ = json.load(open(os.path.join(REPO, 'web/public/data', RELEASE, 'regions.json')))
rows = RJ['yieldRows']                                        # 1-based sheet rows; pipeline row r is sheet row r + 3
base_yield = {z: RJ['regions'][str(z)]['yield'] for z in range(1, 61)}
subsets = list(itertools.combinations(YEARS, 3)); consecutive = {(2006, 2007, 2008), (2007, 2008, 2009), (2008, 2009, 2010)}
payload = {'release': RELEASE, 'subsets': []}; cell_rows = [['subset', 'consecutive', 'cells_scaled', 'cells_lost_to_zero', 'cells_kept_no_pipeline_value', 'cells_not_in_pipeline']]
for sub in subsets:
    out = sheet_for(sub); yields = {}; scaled = lost = kept = outside = 0
    for z in range(1, 61):
        v = []
        for i, row in enumerate(rows):
            r = row - 3; b = base_yield[z][i]
            if r not in full: v.append(b); outside += 1; continue
            f, s = full[r][z], out[r][z]
            if f is None or f == 0: v.append(b); kept += 1
            elif s is None: v.append(0.0); lost += 1
            else: v.append(b * s / f); scaled += 1
        yields[str(z)] = v
    name = ' + '.join(LABEL[y] for y in sub)
    payload['subsets'].append({'name': name, 'consecutive': sub in consecutive, 'yields': yields})
    cell_rows.append([name, int(sub in consecutive), scaled, lost, kept, outside])
with tempfile.TemporaryDirectory() as td:
    pj = os.path.join(td, 'yields.json'); json.dump(payload, open(pj, 'w'))
    subprocess.run(['node', os.path.join(HERE, 'window_subsets_2011_eval.mjs'), pj, os.path.join(HERE, 'window_subsets_2011.csv')], check=True, cwd=os.path.join(REPO, 'web'))
with open(os.path.join(HERE, 'window_subsets_2011_cells.csv'), 'w', newline='') as f: csv.writer(f).writerows(cell_rows)
# one row per subset and preset: Australia, the range over the seven states' capacities' sum, the regions over capacity (of 53) and the 2025-to-2011 ratio
res = list(csv.DictReader(open(os.path.join(HERE, 'window_subsets_2011.csv')))); summ = [['subset', 'consecutive', 'preset', 'australia_capacity', 'ratio_to_five_year', 'regions_over_capacity_of_53', 'australia_population_over_capacity', 'ratio_2025_fixed_over_2011']]
for sname in dict.fromkeys(r['subset'] for r in res):
    for preset in ('short', 'long'):
        rr = [r for r in res if r['subset'] == sname and r['preset'] == preset]; nat = next(r for r in rr if r['zone'] == '1')
        regs = [r for r in rr if r['kind'] == 'region' or r['zone'] == '60']
        summ.append([sname, nat['consecutive'], preset, nat['capacity'], nat['ratio_to_five_year_capacity'], sum(int(r['over_capacity']) for r in regs), nat['population_over_capacity'], nat['ratio_2025_over_2011_australia']])
with open(os.path.join(HERE, 'window_subsets_2011_summary.csv'), 'w', newline='') as f: csv.writer(f).writerows(summ)
print('wrote window_subsets_2011.csv, window_subsets_2011_summary.csv and window_subsets_2011_cells.csv')
