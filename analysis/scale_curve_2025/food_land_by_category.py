#!/usr/bin/env python3
"""Cropping and pasture land per person per year by food category, today's diet (nutrition model units, `analysis/nutrition_lp_2025/server.mjs`).
Usage: python3 -I analysis/scale_curve_2025/food_land_by_category.py [RELEASE]          (repository root; needs the built data)
Used for the question of what back-yard and small-scale cropping could cover (Murray 2026-11-03)."""
import subprocess, json, collections, sys
rel = sys.argv[1] if len(sys.argv) > 1 else '2025-fixed'
srv = subprocess.Popen(['node', 'analysis/nutrition_lp_2025/server.mjs', rel, '1', 'short'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
def q(o): srv.stdin.write(json.dumps(o) + '\n'); srv.stdin.flush(); return json.loads(srv.stdout.readline())
U = q({'cmd': 'units'}); D = q({'cmd': 'defaultgrams'})
crop = collections.defaultdict(float); past = collections.defaultdict(float); grams = collections.defaultdict(float)
for u in U['units']:
    g = D['grams'][str(u['row'])] / 7; land = u['perGram']['land'] if u['perGram'] else 0.0
    (past if u['type'] == 'pasture' else crop)[u['cat']] += land * g; grams[u['cat']] += g
tc, tp = sum(crop.values()), sum(past.values())
print(f'{rel}: crop {tc * 365 / 1e4:.2f} ha and pasture {tp * 365 / 1e4:.2f} ha a person a year')
print('category            grams/day   crop m2/year   share of crop land   pasture m2/year')
for c in sorted(set(crop) | set(past), key=lambda c: -(crop[c] + past[c])): print(f'{c:18}{grams[c]:9.0f}{crop[c] * 365:14.0f}{crop[c] / tc * 100:14.1f}%{past[c] * 365:18.0f}')
fv = sum(crop[c] for c in ('Vege green', 'Vege orange', 'Vege other', 'Fruit')) * 365
print(f"fruit and non-starchy vegetables: {fv:.0f} m2 of crop land a person a year ({fv / (tc * 365) * 100:.1f}% of crop land), {sum(grams[c] for c in ('Vege green', 'Vege orange', 'Vege other', 'Fruit')):.0f} g a day")
