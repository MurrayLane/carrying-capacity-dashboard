#!/usr/bin/env python3
"""Paper A section 8: summary of shocks_by_region.csv (drought return periods) and of results/scenarios.csv (named shocks and settings).
Usage (repository root): python3 -I analysis/paper_a/shocks_summary.py   (writes shocks_summary.csv and scenarios_by_region.csv)
       python3 -I analysis/paper_a/shocks_summary.py --scenarios-only   (writes scenarios_by_region.csv only)
scenarios_by_region.csv carries the named scenarios on each reference release, one row per release: results/scenarios.csv (reference 2025-improved, the stores on
2025-store-1 and 2025-store-2) and results/scenarios_2025-fixed.csv (reference 2025-fixed, the stores as their resilience tables on 2025-fixed). Column release is the
release the row was computed on; reference_release the release its change is measured against. Decision 86 (B91)."""
import csv, collections, os, sys
SCEN_ONLY = '--scenarios-only' in sys.argv
if not SCEN_ONLY:
  rows = list(csv.DictReader(open('analysis/paper_a/shocks_by_region.csv')))
  G = collections.defaultdict(dict)
  for r in rows: G[(r['release'], r['zone'])][int(r['return_period'])] = (float(r['capacity']), float(r['population']), r['name'].strip('"'), r['kind'])
  out = [['release', 'return period (years)', 'national capacity (million)', 'national population (million)', 'national capacity over population', 'regions over capacity (of 53)', 'share of population living in over-capacity regions', 'sum of regional capacities (million)', 'sum over national']]
  tip = {}
  for rel in ('2011-fixed-2', '2025-fixed'):   # 2011-fixed-2: 2011-fixed with North East Vic's 2011 population corrected (error 8 of ERRATA.md)
      for T in (1, 5, 10, 20, 50, 100):
          reg = [(z, v[T]) for (rl, z), v in G.items() if rl == rel and v[T][3] != 'nation']
          nat = G[(rel, '1')][T]
          over = [(z, c) for z, c in reg if c[0] < c[1]]
          pop_tot = sum(c[1] for z, c in reg); pop_over = sum(c[1] for z, c in over)
          out.append([rel, T, round(nat[0] / 1e6, 1), round(nat[1] / 1e6, 1), round(nat[0] / nat[1], 2), len(over), '%.0f%%' % (100 * pop_over / pop_tot), round(sum(c[0] for z, c in reg) / 1e6, 1), round(sum(c[0] for z, c in reg) / nat[0], 2)])
      tip[rel] = [(G[(rel, z)][1][2], round(G[(rel, z)][1][0] / G[(rel, z)][1][1], 2), round(G[(rel, z)][10][0] / G[(rel, z)][10][1], 2)) for (rl, z) in G if rl == rel and G[(rl, z)][1][3] != 'nation' and G[(rl, z)][1][0] >= G[(rl, z)][1][1] and G[(rl, z)][10][0] < G[(rl, z)][10][1]]
  csv.writer(open('analysis/paper_a/shocks_summary.csv', 'w', newline='')).writerows(out)
  for r in out: print(r)
  for rel in tip: print('\nregions under capacity in an average year but over capacity at a 1-in-10 year,', rel, len(tip[rel]), ':', sorted(tip[rel], key=lambda t: t[2]))
# named scenarios
res = [['reference_release', 'release', 'scenario', 'term', 'national capacity (million)', 'change on reference', 'regions over capacity (of 53)', 'regions that tip over capacity against the reference']]
for f in ('results/scenarios.csv', 'results/scenarios_2025-fixed.csv'):
    if not os.path.exists(f): raise SystemExit(f'{f} is missing: run web/scripts/make-scenarios.mjs (with --release 2025-fixed for the second file)')
    sc = list(csv.DictReader(open(f)))
    S = collections.defaultdict(dict)
    for r in sc: S[(r['scenario'], r['preset'])][r['zone']] = r
    ref = {'short': S[('reference', 'short')], 'long': S[('reference', 'long')]}
    ref_release = ref['short']['1']['release']
    region_ids = [z for z, r in ref['short'].items() if r['kind'] in ('region',) or z == '60']
    for (name, term), d in sorted(S.items()):
        over = [z for z in region_ids if float(d[z]['capacity']) < float(d[z]['population'])]
        base_over = [z for z in region_ids if float(ref[term][z]['capacity']) < float(ref[term][z]['population'])]
        res.append([ref_release, d['1']['release'], name, term, round(float(d['1']['capacity']) / 1e6, 1), d['1']['change_pct'] + '%', len(over), len(set(over) - set(base_over))])
csv.writer(open('analysis/paper_a/scenarios_by_region.csv', 'w', newline='')).writerows(res)
print(); [print(r) for r in res]
