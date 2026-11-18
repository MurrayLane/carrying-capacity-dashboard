#!/usr/bin/env python3
"""The movers table (analysis/comparison_2025/movers.csv) with its 2011 population columns taken from a named 2011 release (brief B110).
Usage (repository root): python3 -I analysis/paper_a/movers_release.py RELEASE_2011 OUT.csv
  e.g. python3 -I analysis/paper_a/movers_release.py 2011-fixed-3 analysis/paper_a/movers-3.csv
movers.csv is read, never written (it belongs to analysis/comparison_2025). Every column is kept; pop2011, dpop, ratio2011 and over2011 are recomputed from
results/<RELEASE_2011>.csv (short and long preset rows of the 53 regions), and a column release_2011 names the release. The capacities are checked equal to the
release's own (the 2011 population does not move capacity on the corrected method), so the 2025 columns and the land and boundary flags stay valid.
Run with 2011-fixed-2 it reproduces movers.csv's values exactly (the check in qa/reports/B110_zone_populations_2011.md). Deterministic."""
import csv, sys
rel, out = sys.argv[1], sys.argv[2]
movers = list(csv.DictReader(open('analysis/comparison_2025/movers.csv')))
res = {(r['zone'], r['preset']): r for r in csv.DictReader(open(f'results/{rel}.csv'))}
cols = list(movers[0].keys()) + ['release_2011']
rows = []
for m in movers:
    r = res[(m['zone'], m['preset'])]
    if int(r['capacity']) != int(m['cap2011']): raise SystemExit(f'zone {m["zone"]} {m["preset"]}: {rel} capacity {r["capacity"]} is not movers.csv cap2011 {m["cap2011"]}')
    p = int(r['population']); c = int(m['cap2011'])
    m = dict(m, pop2011=p, dpop=int(m['pop2025']) - p, ratio2011=round(c / p, 2), over2011=int(p > c), release_2011=rel)
    rows.append(m)
w = csv.DictWriter(open(out, 'w', newline=''), fieldnames=cols); w.writeheader(); w.writerows(rows)
print(f'{out}: {len(rows)} rows; over 2011 short {sum(r["over2011"] for r in rows if r["preset"] == "short")}, long {sum(r["over2011"] for r in rows if r["preset"] == "long")}')
