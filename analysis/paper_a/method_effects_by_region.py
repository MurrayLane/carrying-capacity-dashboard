#!/usr/bin/env python3
"""Paper A section 9(b): the effect of each method choice region by region (2025 data; 2011 alongside), from results/method_effects.csv.
Usage (repository root): python3 -I analysis/paper_a/method_effects_by_region.py   (writes method_effects_by_region.csv, method_effects_summary.csv, method_status.csv);
  with `--release-2011 2011-fixed-3 2011-improved-3 -3` the same three files with -3 in the name (B123; see the comment below)

Each module's effect alone is the capacity change when only that module is applied to the published (thesis-method) release; the corrections are biodiesel-yield and beef-carcase-yield, the improvements the other six.
Shown as a share of the published capacity. The 53 regions are the 52 NRM regions and the Northern Territory."""
import csv, statistics, collections, sys
R = list(csv.DictReader(open('results/method_effects.csv')))
# B123: `--release-2011 FIXED IMPROVED SUFFIX` (for example `--release-2011 2011-fixed-3 2011-improved-3 -3`) takes the 2011 population and the 2011 corrected and improved capacities of
# results/method_effects.csv from those two releases' own results files (results/<release>.csv, both presets, every zone) and writes method_effects_by_region<SUFFIX>.csv,
# method_effects_summary<SUFFIX>.csv and method_status<SUFFIX>.csv beside the old files, which it leaves alone. Everything else is read as before: the published capacity and every effect
# column are the published-method run on 2011-corrected (no -3 release of the published method exists; the effect columns are not recomputed, so the improved method's effects that move with
# the infrastructure area, up to 0.9% of capacity in 75 of 120 cells, are the -2 ones and only the capacity_corrected and capacity_improved columns carry the -3 values).
SUF = ''
if '--release-2011' in sys.argv:
    i = sys.argv.index('--release-2011'); FIX11, IMP11, SUF = sys.argv[i + 1:i + 4]
    res = {rel: {(r['zone'], r['preset']): r for r in csv.DictReader(open(f'results/{rel}.csv'))} for rel in (FIX11, IMP11)}
    for r in R:
        if r['vintage'] != '2011': continue
        k = (r['zone'], r['preset']); f, m = res[FIX11][k], res[IMP11][k]
        if f['population'] != m['population']: raise SystemExit(f'zone {k}: {FIX11} and {IMP11} carry different populations')
        r['population_published_release'] = r['population']
        r['population'], r['capacity_corrected'], r['capacity_improved'] = f['population'], f['capacity'], m['capacity']
MODS = ['biodiesel-yield', 'beef-carcase-yield', 'reserve-pro-rata', 'recycling-stage', 'loss-factors-australia', 'regional-beef-output', 'organic-ruminant-factor', 'dairy-good-land']
TIER = {'biodiesel-yield': 'correction', 'beef-carcase-yield': 'correction'}
def regions(vintage, preset): return [r for r in R if r['vintage'] == vintage and r['preset'] == preset and (r['kind'] == 'region' or r['zone'] == '60')]
heat = [['vintage', 'term', 'zone', 'name', 'population', 'capacity published (thousand)'] + [f'{m} (% of published)' for m in MODS] + ['corrected (% of published)', 'improved (% of published)']]
summ = [['vintage', 'term', 'module', 'tier', 'nation (% of published)', 'regional median', 'regional min', 'regional max', 'regions changed by more than 5%', 'regions with a rise', 'regions with a fall', 'most raised', 'most lowered']]
for v in ('2025', '2011'):
    for t in ('short', 'long'):
        rs = regions(v, t); nat = next(r for r in R if r['vintage'] == v and r['preset'] == t and r['zone'] == '1')
        for r in rs:
            pub = float(r['capacity_published'])
            heat.append([v, t, r['zone'], r['name'], r['population'], round(pub / 1e3)] + [round(100 * float(r['effect_alone_' + m]) / pub, 1) if pub > 0 else '' for m in MODS] + [round(100 * (float(r['capacity_corrected']) / pub - 1), 1) if pub > 0 else '', round(100 * (float(r['capacity_improved']) / pub - 1), 1) if pub > 0 else ''])
        for m in MODS:
            e = [(100 * float(r['effect_alone_' + m]) / float(r['capacity_published']), r['name']) for r in rs if float(r['capacity_published']) > 0]
            vals = [x for x, n in e]
            top = sorted(e, reverse=True)[:3]; low = sorted(e)[:3]
            summ.append([v, t, m, TIER.get(m, 'improvement'), round(100 * float(nat['effect_alone_' + m]) / float(nat['capacity_published']), 1), round(statistics.median(vals), 1), round(min(vals), 1), round(max(vals), 1),
                         sum(1 for x in vals if abs(x) > 5), sum(1 for x in vals if x > 0.05), sum(1 for x in vals if x < -0.05), '; '.join(f'{n} {x:+.0f}%' for x, n in top if x > 0.05), '; '.join(f'{n} {x:+.0f}%' for x, n in low if x < -0.05)])
csv.writer(open(f'analysis/paper_a/method_effects_by_region{SUF}.csv', 'w', newline='')).writerows(heat)
csv.writer(open(f'analysis/paper_a/method_effects_summary{SUF}.csv', 'w', newline='')).writerows(summ)
# status of each region on its own population under the three tiers
stat = [['vintage', 'term', 'regions over capacity: published', 'corrected', 'improved', 'status changes published to corrected', 'status changes corrected to improved', 'regions that change corrected to improved']]
for v in ('2025', '2011'):
    for t in ('short', 'long'):
        rs = regions(v, t); over = lambda r, key: float(r[key]) < float(r['population'])
        o = {k: [r for r in rs if over(r, k)] for k in ('capacity_published', 'capacity_corrected', 'capacity_improved')}
        pc = [r['name'] for r in rs if over(r, 'capacity_published') != over(r, 'capacity_corrected')]; ci = [r['name'] for r in rs if over(r, 'capacity_corrected') != over(r, 'capacity_improved')]
        row = [v, t, len(o['capacity_published']), len(o['capacity_corrected']), len(o['capacity_improved']), len(pc), len(ci), '; '.join(ci)]
        if SUF and v == '2011': row.append(sum(1 for r in rs if float(r['capacity_published']) < float(r['population_published_release'])))     # the published method on its own release's population (the thesis's)
        elif SUF: row.append(row[2])
        stat.append(row)
if SUF: stat[0].append('regions over capacity: published, against the population of the published release itself (2011: the thesis populations; 2025: the same)')
csv.writer(open(f'analysis/paper_a/method_status{SUF}.csv', 'w', newline='')).writerows(stat)
for r in summ:
    if r[0] == '2025': print(r)
print(); [print(r) for r in stat]
