#!/usr/bin/env python3
"""Paper A section 9(b): the effect of each method choice region by region (2025 data; 2011 alongside), from results/method_effects.csv.
Usage (repository root): python3 -I analysis/paper_a/method_effects_by_region.py   (writes method_effects_by_region.csv, method_effects_summary.csv, method_status.csv)

Each module's effect alone is the capacity change when only that module is applied to the published (thesis-method) release; the corrections are biodiesel-yield and beef-carcase-yield, the improvements the other six.
Shown as a share of the published capacity. The 53 regions are the 52 NRM regions and the Northern Territory."""
import csv, statistics, collections
R = list(csv.DictReader(open('results/method_effects.csv')))
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
csv.writer(open('analysis/paper_a/method_effects_by_region.csv', 'w', newline='')).writerows(heat)
csv.writer(open('analysis/paper_a/method_effects_summary.csv', 'w', newline='')).writerows(summ)
# status of each region on its own population under the three tiers
stat = [['vintage', 'term', 'regions over capacity: published', 'corrected', 'improved', 'status changes published to corrected', 'status changes corrected to improved', 'regions that change corrected to improved']]
for v in ('2025', '2011'):
    for t in ('short', 'long'):
        rs = regions(v, t); over = lambda r, key: float(r[key]) < float(r['population'])
        o = {k: [r for r in rs if over(r, k)] for k in ('capacity_published', 'capacity_corrected', 'capacity_improved')}
        pc = [r['name'] for r in rs if over(r, 'capacity_published') != over(r, 'capacity_corrected')]; ci = [r['name'] for r in rs if over(r, 'capacity_corrected') != over(r, 'capacity_improved')]
        stat.append([v, t, len(o['capacity_published']), len(o['capacity_corrected']), len(o['capacity_improved']), len(pc), len(ci), '; '.join(ci)])
csv.writer(open('analysis/paper_a/method_status.csv', 'w', newline='')).writerows(stat)
for r in summ:
    if r[0] == '2025': print(r)
print(); [print(r) for r in stat]
