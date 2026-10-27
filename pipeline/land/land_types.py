#!/usr/bin/env python3
"""Apply land_types.json to the SA2 land use table: the five land types of the model, in km2, for every SA2.

Usage: python3 -I land_types.py          (run from the repository root; uses only the standard library)
Writes data/sa2/land_types_by_sa2.csv and prints national totals against the 2011 model and the SA2 area check.
Class codes in the raster table are tertiary ("3.3.1 ..."); a mapping entry such as "3.3" matches every tertiary class whose code starts with it.
"""
import csv, json, os, re, collections
ROOT = os.getcwd()
M = json.load(open(os.path.join(ROOT, 'pipeline/land/land_types.json')))['types']
classes = {int(r['Value']): r['TERTV8'] for r in csv.DictReader(open(os.path.join(ROOT, 'data/sa2/clum_classes.csv')))}
code_of = {v: re.match(r'[\d.]+(?:;\s*[\d.]+)*', classes[v]).group(0) for v in classes}


def type_of(value):
    first = re.split(r';\s*', code_of[value])[0].rstrip('.')            # "5.4.0; 5.4.1" -> 5.4.0
    hits = [t for t, prefixes in M.items() for p in prefixes if first == p or first.startswith(p + '.')]
    if len(hits) != 1: raise SystemExit(f'class {value} ({classes[value]}) maps to {hits}')
    return hits[0]


TYPE = {v: type_of(v) for v in classes}
TYPES = list(M)
sa2 = collections.OrderedDict(); meta = {}
for r in csv.DictReader(open(os.path.join(ROOT, 'data/sa2/land_use_by_sa2.csv'))):
    d = sa2.setdefault(r['sa2_code'], dict.fromkeys(TYPES, 0.0)); d[TYPE[int(r['class_code'])]] += float(r['km2'])
    meta[r['sa2_code']] = (r['sa2_name'], r['sa3_code'], r['sa4_code'], r['state'])
with open(os.path.join(ROOT, 'data/sa2/land_types_by_sa2.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['sa2_code', 'sa2_name', 'sa3_code', 'sa4_code', 'state'] + [f'{t}_km2' for t in TYPES] + ['total_km2'])
    for k, d in sa2.items(): w.writerow([k, *meta[k]] + [round(d[t], 3) for t in TYPES] + [round(sum(d.values()), 3)])
tot = {t: sum(d[t] for d in sa2.values()) for t in TYPES}
ref = {r['regionId']: r for r in csv.DictReader(open(os.path.join(ROOT, 'data/2011/default-inputs-short-term.csv')))}['1']
old = {'cropping': float(ref['cropping']), 'pasture': float(ref['pasture']), 'nature': float(ref['nature1']), 'infrastructure': float(ref['infrastr1']), 'nonAgricultural': float(ref['nonAg'])}
print(f'{"":16s}{"CLUM 2023":>12s}{"2011 model":>12s}')
for t in TYPES: print(f'{t:16s}{tot[t]:12,.0f}{old[t]:12,.0f}')
print(f'{"total":16s}{sum(tot.values()):12,.0f}{sum(old.values()):12,.0f}')
