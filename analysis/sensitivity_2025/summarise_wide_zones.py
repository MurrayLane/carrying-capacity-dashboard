#!/usr/bin/env python3
"""B132: summarises the widened draws of every zone (monte_carlo_draws_2025-fixed_wide_all.csv: 19 choices, 2,000 draws, 60 zones, short and long term).

Usage (repository root): python3 -I analysis/sensitivity_2025/summarise_wide_zones.py
Writes results/ranges_2025-fixed_wide_zones.csv (zone, preset, p5, p50, p95, min, max, base, then name, kind, population, p5_below_population) and analysis/sensitivity_2025/monte_carlo_2025-fixed_wide_all.md.
Percentile rule of summarise_mc.py (linear between order statistics). base is the release's own capacity (the base column of results/ranges_2025-fixed.csv, which equals the release's
capacity in every zone: checked by check_wide_zones.py against a fixed-value run of monte_carlo.mjs). The population is the release's (web/public/data/2025-fixed/regions.json)."""
import csv, json
DRAWS = 'analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide_all.csv'
data = json.load(open('web/public/data/2025-fixed/regions.json'))['regions']
base = {(r['zone'], r['setting']): int(float(r['base'])) for r in csv.DictReader(open('results/ranges_2025-fixed.csv'))}
def pct(v, q):
    s = sorted(v); i = q * (len(s) - 1); lo = int(i); hi = min(lo + 1, len(s) - 1); return s[lo] + (s[hi] - s[lo]) * (i - lo)
rows = list(csv.DictReader(open(DRAWS))); cols = list(rows[0])
zones = sorted({int(c.split('_')[0]) for c in cols if c[0].isdigit()})
out = [['zone', 'preset', 'p5', 'p50', 'p95', 'min', 'max', 'base', 'name', 'kind', 'population', 'p5_below_population']]
for z in zones:
    for k in ('short', 'long'):
        y = [float(r[f'{z}_{k}']) for r in rows]; R = data[str(z)]
        p5 = round(pct(y, .05))
        out.append([z, k, p5, round(pct(y, .5)), round(pct(y, .95)), round(min(y)), round(max(y)), base[(str(z), k)], R['name'], R['kind'], R['population'], 'yes' if p5 < R['population'] else 'no'])
with open('results/ranges_2025-fixed_wide_zones.csv', 'w', newline='') as f: csv.writer(f).writerows(out)
low = [r for r in out[1:] if r[11] == 'yes']
new = [r for r in low if r[7] >= r[10]]                                     # under capacity (or level) at the base, with the 5th percentile below the population: the status is not settled
md = ['# The widened draws for every zone (B132, X140 fixed)', '',
      f'{len(rows)} Latin hypercube draws of 19 choices (`MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 MC_ZONES=all`, seed 20261027), all {len(zones)} zones, short and long term. Ranges: `results/ranges_2025-fixed_wide_zones.csv`.', '',
      'Zone 45 (Northern and Yorke): the land_raster draw uses the raster cropping and pasture on the release land total (non-agricultural land 3,911 to 4,063 km2; the holdings land of the release is 152 km2 larger than the raster build, X140). Only the zone 45 columns are affected; every national and state column equals the earlier widened draws to the person.', '',
      f'**Zones under capacity at the base whose 5th percentile is below their population ({len(new)} of {len(low)} zone-and-term rows with a 5th percentile below the population; the others are over capacity at the base already):**', '',
      '| Zone | Name | Kind | Term | p5 | Base | Population | p5 over population |', '|---|---|---|---|---|---|---|---|']
for r in new: md.append(f'| {r[0]} | {r[8]} | {r[9]} | {r[1]} | {r[2]:,} | {r[7]:,} | {r[10]:,} | {r[2] / r[10]:.3f} |')
md += ['', f'All rows with a 5th percentile below the population: short term {sum(1 for r in low if r[1] == "short")}, long term {sum(1 for r in low if r[1] == "long")} (of {len(zones)} zones each; Australia, the seven states and the 52 regions, the Northern Territory counted once as zone 60).']
open('analysis/sensitivity_2025/monte_carlo_2025-fixed_wide_all.md', 'w').write('\n'.join(md) + '\n')
for r in new: print(r[0], r[8], r[1], 'p5', r[2], 'population', r[10], 'base', r[7])
print(len(new), 'under capacity at the base with p5 below population;', len(low), 'zone-preset rows with p5 below population')
