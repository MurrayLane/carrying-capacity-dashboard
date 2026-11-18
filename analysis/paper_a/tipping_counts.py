#!/usr/bin/env python3
"""B132 (decision 134): the regional tipping counts at 1 in 10 and 1 in 20 on a set of zone ranges.

Usage (repository root):
  python3 -I analysis/paper_a/tipping_counts.py                       the widened ranges of every zone: reads analysis/paper_a/shocks_ranges_wide_zones.csv and
                                                                      analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide_all.csv, writes analysis/paper_a/shocks_counts_wide_zones.csv
  python3 -I analysis/paper_a/tipping_counts.py RANGES.csv DRAWS.csv OUT.csv [DRAWS_ID]     another set (for example analysis/paper_a/shocks_ranges.csv, the 13-choice draws
                                                                      analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_all.csv and DRAWS_ID 2025-fixed_all, which reproduces the counts of B112)
The 53 regions are the 52 NRM regions (kind region) and the Northern Territory (zone 60), the set the paper counts. A region is over capacity when its population is above its capacity.
Each region's drought factor is the zone's own (the `factor` column of the ranges file, the release's resilience table, as in B112 and B123), applied to every draw; the central figure is the release itself at that return period.
Columns: over at the central figure; over at the 95th-percentile capacity (the most favourable end of the range); over at the 5th-percentile capacity (the least favourable end);
regions whose population lies inside their 5th to 95th percentile (named); and, over the draws, the 5th, 50th and 95th percentile of the number of regions over capacity in one draw
(each draw's capacity in every region times that region's factor, so the draw's regions are evaluated together)."""
import csv, sys
A = sys.argv[1:]
RANGES = A[0] if A else 'analysis/paper_a/shocks_ranges_wide_zones.csv'
DRAWS = A[1] if len(A) > 1 else 'analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide_all.csv'
OUT = A[2] if len(A) > 2 else 'analysis/paper_a/shocks_counts_wide_zones.csv'
DID = A[3] if len(A) > 3 else None
def pct(v, q):
    s = sorted(v); i = q * (len(s) - 1); lo = int(i); hi = min(lo + 1, len(s) - 1); return s[lo] + (s[hi] - s[lo]) * (i - lo)
rows = [r for r in csv.DictReader(open(RANGES)) if DID is None or r['draws'] == DID]
draws = list(csv.DictReader(open(DRAWS)))
out = [['draws', 'return_period', 'regions', 'over_at_central', 'over_at_p95_capacity', 'over_at_p5_capacity', 'inside_range', 'inside_range_names', 'draw_count_p5', 'draw_count_p50', 'draw_count_p95']]
for T in sorted({int(r['return_period']) for r in rows}):
    rg = [r for r in rows if int(r['return_period']) == T and (r['kind'] == 'region' or r['zone'] == '60')]
    P = lambda r: float(r['population'])
    over = lambda r, col: P(r) > float(r[col])
    inside = [r for r in rg if float(r['p5']) <= P(r) <= float(r['p95'])]
    cnt = [sum(1 for r in rg if float(d[f"{r['zone']}_short"]) * float(r['factor']) < P(r)) for d in draws]
    out.append([DID or rows[0]['draws'], T, len(rg), sum(over(r, 'central') for r in rg), sum(over(r, 'p95') for r in rg), sum(over(r, 'p5') for r in rg),
                len(inside), '; '.join(r['name'].strip('"') for r in inside), round(pct(cnt, .05)), round(pct(cnt, .5)), round(pct(cnt, .95))])
with open(OUT, 'w', newline='') as f: csv.writer(f).writerows(out)
for r in out[1:]: print(*r, sep=' | ')
