#!/usr/bin/env python3
"""B134 (decision 141), step 2 of 2: national pasture output plus and minus 20% one at a time through the closed form of pairing_relaxed.py (the model's own pairing, k = 1),
checked against the full model rerun of pasture_output_one_at_a_time.mjs (its csv).
Run from the repository root:  node analysis/pasture_2025/pasture_output_one_at_a_time.mjs && python3 analysis/pasture_2025/pasture_output_one_at_a_time.py
        python3 analysis/pasture_2025/pasture_output_one_at_a_time.py --wrong-value-demo     shows the check failing on a planted wrong value (writes nothing)
Pasture output times f means each pasture-fed food, and the wool in the textile need, takes 1/f of the pasture area a person it took (Settings column D, and D48); the land is unchanged.
The pairing is unchanged: crops use the existing cropland; idle cropland is ceded to pasture square metre for square metre; capacity is the largest population for which both hold.
Oils: the cropland a person for oils and fats (Settings!C45) is not fixed when pasture output moves (animal fat is part of the oil supply; it falls 14% at +20%), so two closed-form readings are given:
'pasture groups only' scales only the pasture area (the reading of the R05b scratch, 49.4 and 33.5) and 'with oils from the evaluator' also sets the oils cropland to the evaluator's value at that setting.
Checks: (1) the unscaled closed form equals the evaluator and results/2025-fixed.csv to 1e-6 (pairing_relaxed.check_base); (2) the closed form with oils from the evaluator equals the full model rerun to 1e-4 (the residual, at most 0.002%, is not traced; one candidate is Settings!H33, a cereals cell that moves by 0.01% and that the closed form holds at base); the pasture-groups-only reading is reported with its difference from the full model (a few hundredths of a million).
Writes pasture_output_one_at_a_time_closed_form_2025-fixed.csv: preset; factor; capacity; change; which land binds; crop and pasture area a person; share of the cropland the crops use."""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pairing_relaxed as pr
import numpy as np
DEMO = '--wrong-value-demo' in sys.argv
rr = list(csv.DictReader(open(os.path.join(HERE, 'pasture_output_one_at_a_time_2025-fixed.csv'))))
oils = {(r['preset'], float(r['pasture_output_factor'])): float(r['oils_cropland_m2_pp']) for r in rr}
full = {(r['preset'], float(r['pasture_output_factor'])): float(r['capacity']) / 1e6 for r in rr}
out = [['release', 'preset', 'pasture_output_factor', 'capacity_million_closed_form_with_oils', 'capacity_million_full_model', 'capacity_million_closed_form_pasture_groups_only', 'change_from_base_million', 'change_from_base_pct', 'which_land_binds', 'cropland_m2_pp', 'pasture_m2_pp', 'cropland_used_share']]
ok = True
for preset in ('short', 'long'):
    base = None
    for f in (0.8, 1.0, 1.2):
        g = pr.load(preset); g['preset'] = preset
        g['p'] = g['p'] / f; g['p_nf'] = g['p_nf'] / f
        n = len(g['c']); one = np.ones(n)
        N0f, _, _ = pr.solve(g, one, one, 1.0)
        io = g['name'].index('oils'); g['c'][io] = oils[(preset, f)]
        N, s, d = pr.solve(g, one, one, 1.0)
        if f == 1.0:
            ok &= pr.check_base(N, g); base = N
        fm = full[(preset, f)] + (1.0 if DEMO and preset == 'short' and f == 1.2 else 0.0)   # EXAMPLE wrong value in demo mode only
        same = abs(N - fm) <= 1e-4 * N; ok &= same
        print('check, %s x%.1f: closed form %.6f M, full model %.6f M: %s' % (preset, f, N, fm, 'PASS' if same else 'FAIL'))
        out.append([pr.RELEASE, preset, f, '%.4f' % N, '%.4f' % fm, '%.4f' % N0f, '', '', d['bind'], '%.1f' % (s @ g['c'] + g['c_nf']), '%.1f' % (s @ g['p'] + g['p_nf']), '%.4f' % (d['crop_km2'] / g['C'])])
    for r in out[-3:]:
        r[6] = '%.2f' % (float(r[3]) - base); r[7] = '%.1f' % (100 * (float(r[3]) / base - 1))
for r in out: print(' | '.join(str(x) for x in r))
if DEMO:
    print('EXAMPLE (deliberate wrong value): the full-model rerun for short x1.2 read 1 million too high; nothing written'); sys.exit(0 if not ok else 1)
if not ok: sys.exit('a check failed')
csv.writer(open(os.path.join(HERE, 'pasture_output_one_at_a_time_closed_form_2025-fixed.csv'), 'w', newline=''), lineterminator='\n').writerows(out)
