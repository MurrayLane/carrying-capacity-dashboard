#!/usr/bin/env python3
"""Error 8 of ERRATA.md: North East Victoria's 2011 population (zone 22) is a copy of Goulburn Broken's (zone 19), 204,651 to the person.
Usage (repository root): python3 -I analysis/population_2011/ne_vic_population.py [ABS_3218_2011_SA2_CUBE.xls]

Route 1 (always): the ABS estimated resident population at 30 June 2011 by SA2 (data/sa2/population_erp.csv, sources register D31, 2021 SA2
boundaries) allocated to the 2011 NRM zones exactly as pipeline/land/land_2011_method.py allocates the 2025 population (an SA2 that straddles
a zone boundary gives each part a share in proportion to its residential land, CLUM class 5.4, or its area where it has none). This is the
basis of the 2025 zone populations (data/nrm2011/land_2011_method_zones.csv), so the 2011 and 2025 figures for the zone are like for like.
Route 2 (with the cube): ABS 3218.0 Regional Population Growth, Australia, 2011 (released 31 July 2012), data cube 32180ds0002_2001-11.xls,
Table 2 (Victoria), column 2011pr, on the 2011 SA2 boundaries; the same SA2s with the shares of route 1 for the four that straddle the zone.

Writes analysis/population_2011/zone_population_2011.csv (every zone: the 2011 default population, the route-1 figure, and whether the default
population is shared with another zone) and methods/north-east-vic-population/method.json (the module that applies the correction:
population, and the infrastructure land the 2011 method derives from it at 730 m2 a person, with non-agricultural land as the remainder)."""
import collections, csv, json, os, re, sys

rd = lambda p: list(csv.DictReader(open(p)))
classes = {int(r['Value']): re.match(r'[\d.]+', r['TERTV8']).group(0).rstrip('.') for r in rd('data/sa2/clum_classes.csv')}
under = lambda code, prefixes: any(code == p or code.startswith(p + '.') for p in prefixes)
erp = {r['sa2_code']: float(r['2011'] or 0) for r in rd('data/sa2/population_erp.csv')}
names = {r['sa2_code']: r['sa2_name'] for r in rd('data/sa2/land_2011_method_by_sa2.csv')}
M = {int(k): v for k, v in json.load(open('pipeline/land/zone_to_nrm2011.json'))['zones'].items()}
piece = collections.defaultdict(lambda: collections.defaultdict(float))
for r in rd('data/nrm2011/land_use_by_sa2_nrm2011_piece.csv'):
    p = piece[(r['zone_name'], int(r['nrmr_code_2011']))]; k = float(r['km2']); p['total'] += k
    if under(classes[int(r['class_code'])], ('5.4',)): p['residential'] += k
by_sa2 = collections.defaultdict(dict)
for (s, n), p in piece.items(): by_sa2[s][n] = p
nrm, parts_of = collections.defaultdict(float), collections.defaultdict(list)
for s, parts in by_sa2.items():
    key = 'residential' if sum(q['residential'] for q in parts.values()) > 0 else 'total'; T = sum(q[key] for q in parts.values())
    for n, p in parts.items(): nrm[n] += erp.get(s, 0) * p[key] / T; parts_of[n].append((s, p[key] / T))
zone = {z: sum(nrm[c] for c in codes) for z, codes in M.items()}
old = {int(r['regionId']): r for r in rd('data/2011/default-inputs-short-term.csv')}
same = collections.defaultdict(list)
for z in M: same[old[z]['population']].append(z)
with open('analysis/population_2011/zone_population_2011.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['zone', 'name', 'population_2011_default', 'erp_2011_sa2_route', 'default_over_erp', 'default_shared_with_zone'])
    for z in sorted(M): w.writerow([z, old[z]['regionName'], old[z]['population'], round(zone[z]), round(float(old[z]['population']) / zone[z], 3), ';'.join(str(x) for x in same[old[z]['population']] if x != z)])

Z = 22; shares = [(s, sh) for c in M[Z] for s, sh in parts_of[c] if erp.get(s, 0) * sh >= 0.5]
print(f'zone {Z} {old[Z]["regionName"]}: 2011 default {int(old[Z]["population"]):,}; ERP 30 June 2011, route 1 (D31, 2021 SA2s): {zone[Z]:,.0f}')
for s, sh in sorted(shares, key=lambda t: -erp[t[0]] * t[1]): print(f'  {s} {names.get(s, ""):28s} share {sh:.4f}  ERP {erp[s]:>7,.0f}  in zone {erp[s] * sh:>7,.0f}')
for p, zs in same.items():
    if len(zs) > 1: print('2011 default population shared by zones', zs, p)
if len(sys.argv) > 1:
    import xlrd
    t2 = xlrd.open_workbook(sys.argv[1]).sheet_by_name('Table 2'); c11 = {}
    for r in range(t2.nrows):
        v = t2.row_values(r)
        if isinstance(v[3], float) and v[3] >= 1000: c11['2' + str(int(v[3]))] = (v[5], v[16])
    # the 2021 SA2s of the zone and the 2011 SA2 that holds each (Wodonga 21074 was split into Wodonga and Baranduda - Leneva in 2016)
    to2011 = {'204021065': '21065', '204021066': '21066', '204021067': '21067', '204031068': '21068', '204031069': '21069', '204031070': '21070',
              '204031071': '21071', '204031072': '21072', '204031073': '21073', '204031075': '21075', '205021082': '21082', '216021412': '21412'}
    t = 0.0; seen = set()
    for s, sh in shares:
        c = to2011.get(s) or ('21074' if s in ('204031491', '204031492') else None)
        if c is None or c in seen: continue
        seen.add(c); t += c11[c][1] * sh; print(f'  route 2: {c} {c11[c][0]:28s} 2011pr {c11[c][1]:>7,.0f} x {sh:.4f}')
    print(f'route 2 (ABS 3218.0 2011, 2011 SA2s, 2011pr): {t:,.0f}')

pop = round(zone[Z]); inf = round(pop * 730 / 1e6); o = old[Z]
non = int(o['nonAg']) + int(o['infrastr1']) - inf
assert int(o['cropping']) + int(o['pasture']) + non + inf + int(o['nature1']) == int(o['cropping']) + int(o['pasture']) + int(o['nonAg']) + int(o['infrastr1']) + int(o['nature1'])
mod = {
  'id': 'north-east-vic-population',
  'label': "North East Victoria's 2011 population: the ABS estimate, not Goulburn Broken's",
  'line': 'improved',
  'description': (f"A correction to the data, not to the method (error 8 of ERRATA.md). In the 2011 default inputs North East Vic (zone 22) carries a population of "
                   f"{int(o['population']):,}, the same to the person as Goulburn Broken (zone 19), and an infrastructure area of {o['infrastr1']} km2 derived from it "
                   f"(the 2011 land method sets infrastructure at 730 m2 a person). The copy is in the author's land-use workbook (Yield data/NRM - Landuse.xls, sheet xSummary, "
                   f"cells Y20 and Y23), in every model version after it and in the thesis's Table 25 (p. 382). The ABS estimated resident population of the zone at 30 June 2011 "
                   f"is {pop:,} (sources register D31, SA2s allocated to the 2011 NRM zone as for the 2025 population; analysis/population_2011/ne_vic_population.py). The module "
                   f"sets the zone's population to {pop:,} and its infrastructure to {inf} km2, with non-agricultural land the remainder ({non} km2), so the total area is unchanged. "
                   f"It is applied before state-population-sum, so Victoria's population (the sum of its regions) falls by the same amount. The national row is not changed."),
  'zoneInputs': {str(Z): {'population': pop, 'infrastr1': inf, 'nonAg': non}},
  'errata': [
    "Error 8 of the error register (ERRATA.md). Capacity does not depend on the population input; the infrastructure area moves capacity only where a module shares the reserve and infrastructure shortfall (reserve-pro-rata).",
    "The national population (22,326,388) is the sum of the regions with the copy and is left as it is, as state-population-sum leaves it; the 53 regions now sum to 106,047 less.",
    "Fitzroy (zone 33) and Wet Tropics (zone 39) also share one population to the person (230,982, and 169 km2 of infrastructure); this module does not change them (ERRATA.md error 9)."
  ]
}
os.makedirs('methods/north-east-vic-population', exist_ok=True)
open('methods/north-east-vic-population/method.json', 'w').write(json.dumps(mod, indent=2, ensure_ascii=False) + '\n')
print('wrote methods/north-east-vic-population/method.json and analysis/population_2011/zone_population_2011.csv')
