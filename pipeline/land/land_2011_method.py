#!/usr/bin/env python3
"""The 2011 land method, recovered from the archive and run on current data, per SA2 and per 2011 zone.

Usage: python3 -I land_2011_method.py ASGS_CUBE.xlsx [POPULATION_YEAR]      (run from the repository root; needs openpyxl)
  ASGS_CUBE.xlsx   AGCDCASGS202021.xlsx, ABS Agricultural Commodities 2020-21 by ASGS Edition 3 regions (analysis/recent_data/fetch_recent.py)
  POPULATION_YEAR  year of data/sa2/population_erp.csv for the infrastructure estimate; default 2025

What the 2011 model did (analysis/land_2011/README.md has the evidence, cell by cell):
  total area       the NRM 2011 polygon areas (Albers); Australia excludes Lord Howe, Christmas, Cocos and Jervis Bay
  cropping         ABS "Land mainly used for crops" (AGPROD_AHACRP_F), mean of five years
  pasture          ABS "Land mainly used for grazing, total" (AGLANDGRAZEHA_F), mean of four years
  infrastructure   population x 730 m2
  reserve          protected areas incl. Indigenous protected land (CAPAD 2008, allocated to NRM regions through an IBRA overlay)
  non-agricultural total - (cropping + pasture + infrastructure + reserve)
Here: total area and reserve are measured on the CLUM raster (reserve = classes 1.1 and 1.2, which reproduce the 2011 reserve within the limits of the 2011
estimate, see the README); cropping and pasture are the same two ABS items for 2020-21, the last year the ABS published them below state level;
infrastructure is the same 730 m2 per person on 2025 population; non-agricultural is the remainder.
SA2 figures are allocated to the 2011 zones through data/nrm2011/land_use_by_sa2_nrm2011_piece.csv: an SA2 that straddles a boundary gives each part a
share of its cropping in proportion to the cropping land in that part, of its grazing in proportion to grazing land, of its population in proportion to
residential land (area where it has none).
"""
import collections, csv, json, os, re, sys
import openpyxl
ROOT = os.getcwd()
cube_path = sys.argv[1]; POP_YEAR = sys.argv[2] if len(sys.argv) > 2 else '2025'
rd = lambda p: list(csv.DictReader(open(os.path.join(ROOT, p))))
classes = {int(r['Value']): re.match(r'[\d.]+', r['TERTV8']).group(0).rstrip('.') for r in rd('data/sa2/clum_classes.csv')}
RESERVE = ('1.1', '1.2'); CROPLAND = ('3.3', '3.4', '3.5', '3.6', '4.3', '4.4', '4.5', '4.6'); GRAZING = ('2.1', '3.2', '4.2'); RESIDENTIAL = ('5.4',)
under = lambda code, prefixes: any(code == p or code.startswith(p + '.') for p in prefixes)

# ---- ABS holdings items at SA2, 2020-21 --------------------------------------------------------------------------------------------------------
ITEM = {'AGPROD_AHACRP_F': 'crops', 'AGLANDGRAZEHA_F': 'grazing'}
abs_ha = collections.defaultdict(dict)
for row in openpyxl.load_workbook(cube_path, read_only=True, data_only=True)['Table 1'].iter_rows(min_row=8, values_only=True):
    if row[2] in ITEM and len(str(row[0])) == 9 and isinstance(row[4], (int, float)): abs_ha[str(row[0])][ITEM[row[2]]] = row[4]

# ---- land per SA2 from the raster; population ---------------------------------------------------------------------------------------------------
sa2 = collections.OrderedDict()
for r in rd('data/sa2/land_use_by_sa2.csv'):
    d = sa2.setdefault(r['sa2_code'], dict(name=r['sa2_name'], total=0.0, reserve=0.0))
    k = float(r['km2']); c = classes[int(r['class_code'])]; d['total'] += k
    if under(c, RESERVE): d['reserve'] += k
pop = {r['sa2_code']: float(r[POP_YEAR] or 0) for r in rd('data/sa2/population_erp.csv')}
with open(os.path.join(ROOT, 'data/sa2/land_2011_method_by_sa2.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['sa2_code', 'sa2_name', 'cropping_km2', 'pasture_km2', 'infrastructure_km2', 'reserve_km2', 'nonAgricultural_km2', 'total_km2', 'population'])
    neg = 0
    for code, d in sa2.items():
        cr = abs_ha[code].get('crops', 0) / 100; pa = abs_ha[code].get('grazing', 0) / 100; inf = pop.get(code, 0) * 730 / 1e6
        non = d['total'] - cr - pa - inf - d['reserve']; neg += non < -0.5
        w.writerow([code, d['name'], round(cr, 3), round(pa, 3), round(inf, 3), round(d['reserve'], 3), round(non, 3), round(d['total'], 3), pop.get(code, 0)])
print(f'{len(sa2)} SA2s; {neg} have a negative remainder before allocation (holdings and reserve overlap)')

# ---- allocation to the 2011 zones ---------------------------------------------------------------------------------------------------------------
M = {int(k): v for k, v in json.load(open(os.path.join(ROOT, 'pipeline/land/zone_to_nrm2011.json')))['zones'].items()}
STATE_OF = {2: range(3, 15), 15: range(16, 26), 26: range(27, 40), 40: range(41, 49), 49: range(50, 56), 56: range(57, 60), 60: [60]}
piece = collections.defaultdict(lambda: collections.defaultdict(float))           # (sa2, nrm) -> measure -> km2
for r in rd('data/nrm2011/land_use_by_sa2_nrm2011_piece.csv'):
    key = (r['zone_name'], int(r['nrmr_code_2011'])); c = classes[int(r['class_code'])]; k = float(r['km2']); p = piece[key]
    p['total'] += k
    if under(c, RESERVE): p['reserve'] += k
    if under(c, CROPLAND): p['cropland'] += k
    if under(c, GRAZING): p['grazing'] += k
    if under(c, RESIDENTIAL): p['residential'] += k
by_sa2 = collections.defaultdict(dict)
for (s, n), p in piece.items(): by_sa2[s][n] = p
nrm = collections.defaultdict(lambda: collections.defaultdict(float))              # nrm code -> measure -> value
for s, parts in by_sa2.items():
    share = lambda key: ({n: p[key] / sum(q[key] for q in parts.values()) for n, p in parts.items()} if sum(q[key] for q in parts.values()) > 0 else {n: p['total'] / sum(q['total'] for q in parts.values()) for n, p in parts.items()})
    sc, sg, sr = share('cropland'), share('grazing'), share('residential')
    for n, p in parts.items():
        t = nrm[n]; t['total'] += p['total']; t['reserve'] += p['reserve']
        t['cropping'] += abs_ha[s].get('crops', 0) / 100 * sc[n]; t['pasture'] += abs_ha[s].get('grazing', 0) / 100 * sg[n]; t['population'] += pop.get(s, 0) * sr[n]
zones = {}
for z, codes in M.items():
    zones[z] = {k: sum(nrm[c][k] for c in codes) for k in ('total', 'reserve', 'cropping', 'pasture', 'population')}
for st, rg in STATE_OF.items():
    if st != 60: zones[st] = {k: sum(zones[r][k] for r in rg) for k in zones[3]}
# the thesis zone 2 (NSW-ACT) also holds the ACT, which is in zone 10; the other state rows sum their own regions
zones[2] = {k: sum(zones[r][k] for r in STATE_OF[2]) for k in zones[3]}
zones[1] = {k: sum(zones[s][k] for s in (2, 15, 26, 40, 49, 56, 60)) for k in zones[3]}
old = {int(r['regionId']): r for r in rd('data/2011/default-inputs-short-term.csv')}
cols = ['zone', 'name', 'cropping', 'pasture', 'nonAgricultural', 'infrastructure', 'reserve', 'total', 'population', 'old_cropping', 'old_pasture', 'old_nonAg', 'old_infrastructure', 'old_reserve', 'old_total', 'old_population']
out = []
for z in sorted(zones):
    d = zones[z]; inf = d['population'] * 730 / 1e6; non = d['total'] - d['cropping'] - d['pasture'] - inf - d['reserve']; o = old[z]
    out.append([z, o['regionName'], d['cropping'], d['pasture'], non, inf, d['reserve'], d['total'], d['population'], *[float(o[k]) for k in ('cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1', 'totalArea', 'population')]])
with open(os.path.join(ROOT, 'data/nrm2011/land_2011_method_zones.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(cols)
    for r in out: w.writerow([r[0], r[1]] + [round(x, 2) for x in r[2:]])
print(f'\n{"":24s}{"cropping":>10s}{"pasture":>10s}{"non-ag":>10s}{"infra":>9s}{"reserve":>10s}{"total":>10s}{"pop (m)":>9s}    old: cropping pasture non-ag reserve')
for r in out:
    if r[0] in (1, 2, 15, 26, 40, 49, 56, 60):
        print(f'{r[1][:23]:24s}' + ''.join(f'{x:10,.0f}' for x in r[2:8]) + f'{r[8] / 1e6:9.2f}    ' + ''.join(f'{x:9,.0f}' for x in (r[9], r[10], r[11], r[13])))
