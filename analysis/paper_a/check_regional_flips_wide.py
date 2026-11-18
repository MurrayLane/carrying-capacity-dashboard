#!/usr/bin/env python3
"""B132 check: re-derives the 'robust' and 'clean and robust' columns of analysis/paper_a/regional_flips-3_wide.csv from the widened zone ranges (results/ranges_2025-fixed_wide_zones.csv, p5 and p95) and the
2025 populations of analysis/paper_a/movers-3.csv, independently of regional_flips.py, and checks the counts quoted in qa/reports/B132_regional_widened_draws.md.
It also recomputes from the draws (monte_carlo_draws_2025-fixed_wide_all.csv) the shares of draws over capacity and the land-source split quoted in the report and in the README.
Usage (repository root): python3 -I analysis/paper_a/check_regional_flips_wide.py [TERM STAT VALUE]
With the three optional arguments the quoted count is replaced by VALUE (TERM short or long; STAT flips, keep_status, clean_and_robust, not_robust; a wrong value given on purpose must fail). Exit status 1 on any failure."""
import csv, sys
rg = {(r['zone'], r['preset']): (int(r['p5']), int(r['p95'])) for r in csv.DictReader(open('results/ranges_2025-fixed_wide_zones.csv'))}
mv = {(r['zone'], r['preset']): r for r in csv.DictReader(open('analysis/paper_a/movers-3.csv'))}
bad = 0; calc = {'short': {'flips': 0, 'keep_status': 0, 'clean_and_robust': 0, 'not_robust': 0}, 'long': {'flips': 0, 'keep_status': 0, 'clean_and_robust': 0, 'not_robust': 0}}; names = {'short': [], 'long': []}
for r in csv.DictReader(open('analysis/paper_a/regional_flips-3_wide.csv')):
    k = (r['zone'], r['term']); m = mv[k]; p5, p95 = rg[k]; pop = int(m['pop2025']); o25 = int(m['over2025']); o11 = int(m['over2011'])
    robust = (p95 < pop) if o25 else (p5 > pop)
    if (r['2025 status robust to the range'] == 'yes') != robust: bad += 1; print('MISMATCH robust', k, r['name'])
    if o11 == o25: continue
    art = bool(m['land_definition_effect_flag'] or m['boundary_older_2011']); c = calc[r['term']]; c['flips'] += 1; c['keep_status'] += robust; c['not_robust'] += (not robust)
    clean = robust and not art; c['clean_and_robust'] += clean
    if (r['clean and robust'] == 'yes') != clean: bad += 1; print('MISMATCH clean', k, r['name'])
    if robust: names[r['term']].append(r['name'] + (' (artefact flag)' if art else ''))
print(calc, names)
QUOTED = {('short', 'flips'): 8, ('short', 'keep_status'): 1, ('short', 'clean_and_robust'): 0, ('short', 'not_robust'): 7, ('long', 'flips'): 3, ('long', 'keep_status'): 1, ('long', 'clean_and_robust'): 1, ('long', 'not_robust'): 2}
if len(sys.argv) == 4: QUOTED[(sys.argv[1], sys.argv[2])] = int(sys.argv[3]); print(f'EXAMPLE: quoted value replaced by {sys.argv[3]}')
for (t, s), val in QUOTED.items():
    if calc[t][s] != val: bad += 1; print(f'FAIL quoted {t} {s} = {val} but the file gives {calc[t][s]}')
    else: print(f'ok   quoted {t} {s} = {val}')
# figures from the draws: share of draws over capacity (population above the draw's capacity), overall and by land source (land = 0 the ABS holdings, 1 the raster), the energy split, and South West Queensland's lowest long-term draw
draws = list(csv.DictReader(open('analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide_all.csv')))
def share(z, term, pop, f=lambda d: True):
    sel = [d for d in draws if f(d)]; return sum(1 for d in sel if float(d[f'{z}_{term}']) < pop) / len(sel)
NT, MW = 156393, 153841
got = {'North Tasmania over, all draws': share('57', 'short', NT), 'North Tasmania over, holdings land': share('57', 'short', NT, lambda d: d['land'] == '0.0' or float(d['land']) == 0),
       'North Tasmania over, raster land': share('57', 'short', NT, lambda d: float(d['land']) == 1), 'North Tasmania over, energy above 1.2': share('57', 'short', NT, lambda d: float(d['energy']) > 1.2),
       'Mackay Whitsunday over, all draws': share('34', 'short', MW), 'Mackay Whitsunday over, holdings land': share('34', 'short', MW, lambda d: float(d['land']) == 0),
       'Mackay Whitsunday over, raster land': share('34', 'short', MW, lambda d: float(d['land']) == 1), 'South West Qld lowest long-term draw': min(float(d['37_long']) for d in draws)}
want = {'North Tasmania over, all draws': 0.1345, 'North Tasmania over, holdings land': 0.269, 'North Tasmania over, raster land': 0.0, 'North Tasmania over, energy above 1.2': 0.362,
        'Mackay Whitsunday over, all draws': 0.294, 'Mackay Whitsunday over, holdings land': 0.162, 'Mackay Whitsunday over, raster land': 0.426, 'South West Qld lowest long-term draw': 15477}
for k, v in want.items():
    ok = abs(got[k] - v) <= (0.5 if v > 1 else 6e-4)
    if not ok: bad += 1
    print(('ok   ' if ok else 'FAIL ') + f'{k}: {got[k]:.4f} (quoted {v})')
sys.exit(1 if bad else 0)
