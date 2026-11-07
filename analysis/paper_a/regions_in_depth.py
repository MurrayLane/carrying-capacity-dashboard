"""Section 10: regions in depth. Run from the repository root: python3 -I analysis/paper_a/regions_in_depth.py
Writes regions_in_depth.csv (one row per region and term) and regions_in_depth.md (tables generated from the csv).
Reads only existing outputs; changes nothing else."""
import csv, json, os, statistics

OUT = 'analysis/paper_a'
def rd(f): return list(csv.DictReader(open(f)))
def fnum(x): return float(x) if x not in ('', None) else None

CASES = [  # group, zone, role
    ('Hawkesbury-Nepean-Sydney', 5, 'capital with hinterland'),
    ('Murray and Murrumbidgee-ACT', 9, 'Murray-Darling Basin'),
    ('Murray and Murrumbidgee-ACT', 10, 'Murray-Darling Basin'),
    ('Avon', 50, 'south-west WA cropping belt'),
    ('North Tasmania', 57, 'status flip'),
    ('SA Arid Lands and Eyre Peninsula', 46, 'rangeland mechanism'),
    ('SA Arid Lands and Eyre Peninsula', 43, 'rangeland mechanism (paired)'),
]
MODS = ['biodiesel-yield', 'beef-carcase-yield', 'reserve-pro-rata', 'recycling-stage', 'loss-factors-australia',
        'regional-beef-output', 'organic-ruminant-factor', 'dairy-good-land']

res = {(r['release'], r['zone'], r['preset']): r for r in rd('results/2011-fixed.csv') + rd('results/2025-fixed.csv')}
flips = {(r['zone'], r['term']): r for r in rd('analysis/paper_a/regional_flips.csv')}
movers = {(r['zone'], r['preset']): r for r in rd('analysis/comparison_2025/movers.csv')}
shocks = {(r['release'], r['zone'], r['return_period']): r for r in rd('analysis/paper_a/shocks_by_region.csv')}
longt = {(r['release'], r['zone']): r for r in rd('analysis/paper_a/long_term_regions.csv')}
meff = {(r['vintage'], r['term'], r['zone']): r for r in rd('analysis/paper_a/method_effects_by_region.csv')}
rng = {(r['zone'], r['setting']): r for r in rd('results/ranges_2025-fixed.csv')}
reg = {rel: json.load(open(f'web/public/data/{rel}/regions.json'))['regions'] for rel in ('2011-fixed', '2025-fixed')}
zones_md = json.load(open('pipeline/land/zone_to_nrm2011.json'))['zones']
land_zone_csv = {r['zone']: r for r in rd('data/nrm2011/land_2011_method_zones.csv')}

# ---------- cross-checks over all 53 regions ----------
all_zones = sorted(int(z) for z in zones_md)
issues = []
def chk(label, a, b, tol=0.5):
    if a is None or b is None or abs(a - b) > tol:
        issues.append((label, a, b))
for z in map(str, all_zones):
    for term in ('short', 'long'):
        r11, r25 = res[('2011-fixed', z, term)], res[('2025-fixed', z, term)]
        tag = f'zone {z} {r25["name"]} {term}'
        f = flips[(z, term)]; m = movers[(z, term)]
        for key, rr, col in (('population 2011', r11, 'population'), ('population 2025', r25, 'population'),
                             ('capacity 2011', r11, 'capacity'), ('capacity 2025', r25, 'capacity')):
            chk(f'{tag}: regional_flips {key} vs results', fnum(f[key]), fnum(rr[col]))
        for key, rr, col in (('pop2011', r11, 'population'), ('pop2025', r25, 'population'),
                             ('cap2011', r11, 'capacity'), ('cap2025', r25, 'capacity')):
            chk(f'{tag}: movers {key} vs results', fnum(m[key]), fnum(rr[col]))
        for yr, rr in (('2011', r11), ('2025', r25)):
            chk(f'{tag}: over_capacity {yr} vs population>capacity', fnum(rr['over_capacity']),
                1.0 if fnum(rr['population']) > fnum(rr['capacity']) else 0.0, 0)
            chk(f'{tag}: regional_flips over {yr} vs results', fnum(f['over ' + yr]), fnum(rr['over_capacity']), 0)
            chk(f'{tag}: movers over{yr} vs results', fnum(m['over' + yr]), fnum(rr['over_capacity']), 0)
        rg = rng[(z, term)]
        chk(f'{tag}: ranges base vs results 2025', fnum(rg['base']), fnum(r25['capacity']))
        if term == 'short':
            for rel, rr in (('2011-fixed', r11), ('2025-fixed', r25)):
                chk(f'{tag}: shocks return period 1 vs results {rel[:4]}', fnum(shocks[(rel, z, '1')]['capacity']), fnum(rr['capacity']))
        else:
            for rel, rr in (('2011-fixed', r11), ('2025-fixed', r25)):
                chk(f'{tag}: long_term_regions vs results {rel[:4]}', fnum(longt[(rel, z)]['capacity_long']), fnum(rr['capacity']))
        for vint in ('2011', '2025'):
            chk(f'{tag}: method_effects population {vint} vs results', fnum(meff[(vint, term, z)]['population']),
                fnum((r11 if vint == '2011' else r25)['population']), 0.5)
        if not (fnum(rg['p5']) <= fnum(rg['p50']) <= fnum(rg['p95'])):
            issues.append((f'{tag}: range not ordered', rg['p5'], rg['p95']))
        if not (fnum(rg['p5']) <= fnum(r25['capacity']) <= fnum(rg['p95'])):
            issues.append((f'{tag}: 2025 base capacity outside its own 5th to 95th range', r25['capacity'], f"{rg['p5']} to {rg['p95']}"))
    for rel in ('2011-fixed', '2025-fixed'):
        chk(f'zone {z}: regions.json population vs results {rel[:4]}', reg[rel][z]['population'], fnum(res[(rel, z, 'short')]['population']), 0.5)
    L = reg['2011-fixed'][z]['land']; zc = land_zone_csv.get(z)
    if zc:
        chk(f'zone {z}: 2011 regions.json cropping vs old_cropping in land_2011_method_zones.csv', L['cropping'], fnum(zc['old_cropping']), 1)
        chk(f'zone {z}: 2011 regions.json pasture vs old_pasture', L['pasture'], fnum(zc['old_pasture']), 1)
        chk(f'zone {z}: 2011 regions.json nonAg vs old_nonAg', L['nonAg'], fnum(zc['old_nonAg']), 2)
        L5 = reg['2025-fixed'][z]['land']
        chk(f'zone {z}: 2025 regions.json cropping vs cropping in land_2011_method_zones.csv', L5['cropping'], fnum(zc['cropping']), 1)
        chk(f'zone {z}: 2025 regions.json pasture vs pasture', L5['pasture'], fnum(zc['pasture']), 1)
        chk(f'zone {z}: 2025 regions.json nonAg vs nonAgricultural', L5['nonAg'], fnum(zc['nonAgricultural']), 2)
    # flip label consistent between files
    fs, ml = flips[(z, 'short')], movers[(z, 'short')]
    flagset = set()
    if ml['land_definition_effect_flag'] == 'yes': flagset.add('land definition')
    if ml['boundary_older_2011'] == 'yes': flagset.add('older 2011 boundary')
    # regional_flips keeps one label; where both flags apply it shows 'land definition'
    if (fs['artefact flag'] != '') != bool(flagset) or (fs['artefact flag'] and fs['artefact flag'] not in flagset):
        issues.append((f'zone {z}: artefact label differs between regional_flips and movers', fs['artefact flag'], sorted(flagset)))

# ---------- the csv ----------
def pct(a, b): return None if not a else round(100.0 * (b - a) / a, 1)
rows = []
for group, z, role in CASES:
    zs = str(z)
    for term in ('short', 'long'):
        r11, r25 = res[('2011-fixed', zs, term)], res[('2025-fixed', zs, term)]
        f, m, rg = flips[(zs, term)], movers[(zs, term)], rng[(zs, term)]
        p11, p25, c11, c25 = (fnum(r11['population']), fnum(r25['population']), fnum(r11['capacity']), fnum(r25['capacity']))
        me = meff[('2025', term, zs)]
        eff = sorted(((fnum(me[k + ' (% of published)']), k) for k in MODS), key=lambda t: -abs(t[0]))
        row = {
            'group': group, 'zone': z, 'region': r25['name'], 'role': role, 'term': term,
            'population_2011': int(p11), 'population_2025': int(p25),
            'capacity_2011': int(c11), 'capacity_2025': int(c25),
            'capacity_over_population_2011': round(c11 / p11, 4), 'capacity_over_population_2025': round(c25 / p25, 4),
            'excess_population_2025': int(p25 - c25),
            'over_capacity_2011': int(r11['over_capacity']), 'over_capacity_2025': int(r25['over_capacity']),
            'flip': f['flip'], 'clean_and_robust': f['clean and robust'],
            'status_2025_robust_to_range': f['2025 status robust to the range'],
            'land_definition_flag': 'yes' if m['land_definition_effect_flag'] == 'yes' else '',
            'older_2011_boundary_flag': 'yes' if m['boundary_older_2011'] == 'yes' else '',
            'land_only_ratio': m['land_only_ratio'],
            'range_2025_p5': int(float(rg['p5'])), 'range_2025_p50': int(float(rg['p50'])), 'range_2025_p95': int(float(rg['p95'])),
            'method_effect_1_module': eff[0][1], 'method_effect_1_pct': eff[0][0],
            'method_effect_2_module': eff[1][1], 'method_effect_2_pct': eff[1][0],
        }
        for rel, yr in (('2011-fixed', '2011'), ('2025-fixed', '2025')):
            for rp in ('10', '100'):
                if term == 'short':
                    s = shocks[(rel, zs, rp)]
                    row[f'capacity_1_in_{rp}_{yr}'] = int(float(s['capacity']))
                    row[f'capacity_over_population_1_in_{rp}_{yr}'] = round(float(s['capacity']) / float(s['population']), 4)
                else:
                    row[f'capacity_1_in_{rp}_{yr}'] = ''
                    row[f'capacity_over_population_1_in_{rp}_{yr}'] = ''
            L = reg[rel][zs]['land']
            row[f'cropping_km2_{yr}'] = L['cropping']; row[f'pasture_km2_{yr}'] = L['pasture']; row[f'non_agricultural_km2_{yr}'] = L['nonAg']
        rows.append(row)
cols = list(rows[0].keys())
with open(f'{OUT}/regions_in_depth.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(rows)

# ---------- the md, every number read back from the csv ----------
C = {(r['zone'], r['term']): r for r in rd(f'{OUT}/regions_in_depth.csv')}
def n(x): return f'{int(float(x)):,}'
def x2(x): return f'{float(x):.3f}'
def sg(x): return f'{float(x):+.1f}%'
def status(v): return 'over capacity' if v == '1' else 'under capacity'
NAMES = {'hawkesbury - nepean - sydney': 0}
md = ['# Section 10: regions in depth', '',
      'Generated by `analysis/paper_a/regions_in_depth.py`; every figure below is read from `analysis/paper_a/regions_in_depth.csv` (one row per region and term), which is built from the corrected releases (`results/2011-fixed.csv`, `results/2025-fixed.csv`) and the existing outputs named in the source column. People are whole persons; land is km2; capacity is the number of people the region could feed. Short term is the average year at the release defaults; the 1-in-10 and 1-in-100 drought capacities are short-term settings (`analysis/paper_a/shocks_by_region.csv`); the long term is the 100-year plan (no drought return period is run for it). The 5th to 95th percentile range is the Monte Carlo range for 2025 (`results/ranges_2025-fixed.csv`); 2011 has no range.', '']
MED = f"{statistics.median(float(movers[(str(z), 'short')]['land_only_ratio']) for z in all_zones):.2f}"
cur = None
for group, z, role in CASES:
    zs = str(z); s, l = C[(zs, 'short')], C[(zs, 'long')]
    if group != cur:
        md += [f'## {group} ({role})', '']; cur = group
    md += [f'### {s["region"]} (zone {z})', '', '| Item | 2011 | 2025 | Source |', '|---|---|---|---|']
    md.append(f'| Population | {n(s["population_2011"])} | {n(s["population_2025"])} | `results/<release>.csv` |')
    md.append(f'| Short-term capacity | {n(s["capacity_2011"])} | {n(s["capacity_2025"])} | `results/<release>.csv` |')
    md.append(f'| Short-term capacity over population | {x2(s["capacity_over_population_2011"])} | {x2(s["capacity_over_population_2025"])} | computed from the two rows above |')
    md.append(f'| Short-term status | {status(s["over_capacity_2011"])} | {status(s["over_capacity_2025"])} | `regional_flips.csv` |')
    md.append(f'| Long-term capacity | {n(l["capacity_2011"])} | {n(l["capacity_2025"])} | `results/<release>.csv`, `long_term_regions.csv` |')
    md.append(f'| Long-term capacity over population | {x2(l["capacity_over_population_2011"])} | {x2(l["capacity_over_population_2025"])} | computed |')
    md.append(f'| Long-term status | {status(l["over_capacity_2011"])} | {status(l["over_capacity_2025"])} | `regional_flips.csv` |')
    md.append(f'| Short-term capacity at a 1-in-10 drought | {n(s["capacity_1_in_10_2011"])} ({x2(s["capacity_over_population_1_in_10_2011"])} times population) | {n(s["capacity_1_in_10_2025"])} ({x2(s["capacity_over_population_1_in_10_2025"])}) | `shocks_by_region.csv` |')
    md.append(f'| Short-term capacity at a 1-in-100 drought | {n(s["capacity_1_in_100_2011"])} ({x2(s["capacity_over_population_1_in_100_2011"])}) | {n(s["capacity_1_in_100_2025"])} ({x2(s["capacity_over_population_1_in_100_2025"])}) | `shocks_by_region.csv` |')
    md.append(f'| 5th to 95th percentile, short term | not sampled | {n(s["range_2025_p5"])} to {n(s["range_2025_p95"])} (median {n(s["range_2025_p50"])}) | `results/ranges_2025-fixed.csv` |')
    md.append(f'| 5th to 95th percentile, long term | not sampled | {n(l["range_2025_p5"])} to {n(l["range_2025_p95"])} (median {n(l["range_2025_p50"])}) | `results/ranges_2025-fixed.csv` |')
    for lab, k in (('Cropping land, km2', 'cropping_km2'), ('Pasture land, km2', 'pasture_km2'), ('Non-agricultural land, km2', 'non_agricultural_km2')):
        md.append(f'| {lab} | {n(s[k + "_2011"])} | {n(s[k + "_2025"])} | `web/public/data/<release>/regions.json` |')
    md.append(f'| Two largest method-module effects, short term (2025, % of published) | | {s["method_effect_1_module"]} {sg(s["method_effect_1_pct"])}; {s["method_effect_2_module"]} {sg(s["method_effect_2_pct"])} | `method_effects_by_region.csv` |')
    md.append(f'| Two largest method-module effects, long term (2025, % of published) | | {l["method_effect_1_module"]} {sg(l["method_effect_1_pct"])}; {l["method_effect_2_module"]} {sg(l["method_effect_2_pct"])} | `method_effects_by_region.csv` |')
    def flipword(r, t):
        if not r['flip']: return f'{t} term: no flip'
        return f'{t} term: {r["flip"]}, ' + ('clean and robust' if r['clean_and_robust'] == 'yes' else 'not clean and robust')
    md.append(f'| Status change | | {flipword(s, "short")}; {flipword(l, "long")} | `regional_flips.csv` |')
    md.append(f'| 2025 status robust to the range | | short term {s["status_2025_robust_to_range"]}; long term {l["status_2025_robust_to_range"]} | `regional_flips.csv` |')
    flags = []
    if s['land_definition_flag']: flags.append('land definition (the land layer alone moves capacity by more than 2 times or less than 0.5)')
    if s['older_2011_boundary_flag']: flags.append('2011 zone drawn on an older boundary')
    md.append(f'| Land-definition and boundary flags | | {"; ".join(flags) if flags else "none"}; land-only ratio {s["land_only_ratio"]} | `movers.csv` |')
    if s['land_definition_flag']:
        md += ['', f'Reading: the {s["region"]} change in capacity between 2011 and 2025 is a land-definition artefact, not a real change. With only the 2025 land layer swapped in, capacity is {s["land_only_ratio"]} times the 2011 capacity (`movers.csv`; the median of the 53 regions is {MED}), so the status flip is not a finding about this region.']
    md.append('')

md += ['## Comparison of the seven regions', '',
       'Short term unless stated. Ratio is capacity over population (below 1 is over capacity). Excess population is population minus capacity in 2025 (positive means over capacity), the quantity mapped in `migration_map.png`.', '',
       '| Region | Population 2025 | Capacity 2025 | Excess population 2025 | Ratio 2011 | Ratio 2025 | Ratio at 1-in-10 | Ratio at 1-in-100 | Long-term ratio 2025 | 2025 range (5th to 95th) as ratio | Short-term status 2011 to 2025 | Flags |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
for group, z, role in CASES:
    zs = str(z); s, l = C[(zs, 'short')], C[(zs, 'long')]
    p = float(s['population_2025'])
    fl = []
    if s['land_definition_flag']: fl.append('land definition')
    if s['older_2011_boundary_flag']: fl.append('older boundary')
    md.append(f'| {s["region"]} | {n(p)} | {n(s["capacity_2025"])} | {int(float(s["excess_population_2025"])):,} | {x2(s["capacity_over_population_2011"])} | {x2(s["capacity_over_population_2025"])} | {x2(s["capacity_over_population_1_in_10_2025"])} | {x2(s["capacity_over_population_1_in_100_2025"])} | {x2(l["capacity_over_population_2025"])} | {float(s["range_2025_p5"])/p:.3f} to {float(s["range_2025_p95"])/p:.3f} | {status(s["over_capacity_2011"])} to {status(s["over_capacity_2025"])} | {", ".join(fl) or "none"} |')
md.append('')
md += ['## Checks across the files', '',
       f'Every one of the 53 regions, both terms, was compared across `results/2011-fixed.csv`, `results/2025-fixed.csv`, `regional_flips.csv`, `movers.csv`, `shocks_by_region.csv` (return period 1), `long_term_regions.csv`, `results/ranges_2025-fixed.csv` (base), `method_effects_by_region.csv` (population), the over-capacity flag against population greater than capacity, the two flag sets, and the 2011 and 2025 land in `regions.json` against `data/nrm2011/land_2011_method_zones.csv`. Disagreements found: {len(issues)}.', '']
for lab, a, b in issues[:60]:
    md.append(f'* {lab}: {a} against {b}')
md.append('')
open(f'{OUT}/regions_in_depth.md', 'w').write('\n'.join(md))
print(len(rows), 'rows;', len(issues), 'disagreements')
for i in issues[:60]: print(i)
