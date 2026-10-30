#!/bin/bash
# Tropical-staples template (SCOPE.md E16): the nutrition-constrained diet (ten micronutrients, no food above 3 times its present intake except the staples)
# with at least 0, 10, 20, 30 or 40% of energy from banana, sweet potato and cassava; Australia, Queensland, Northern Territory; writes staples.csv.
#   bash analysis/nutrition_lp_2025/run_staples.sh RELEASE OUT_DIR        (repository root)
REL=${1:-2025-improved}; OUT=${2:-/tmp/nutrition_staples}; mkdir -p "$OUT"
for z in 1 26 60; do for pr in short long; do for s in 0 0.1 0.2 0.3 0.4; do
  python3 -I analysis/nutrition_lp_2025/optimise.py $REL $z $pr $OUT/${z}_${pr}_s$s.json 1 micro cap3 staples$s >/dev/null 2>&1
done; done; done
python3 -I - "$OUT" "$REL" <<'PY'
import json, glob, os, csv, sys
out, rel = sys.argv[1:3]; rows = [['release', 'zone', 'preset', 'staples_min_energy_share', 'capacity_default', 'capacity_optimised', 'staples_energy_share', 'staples_g_day']]
ST = ('banana', 'Sweet potato', 'Cassava', 'Sweet potato orange')
for f in sorted(glob.glob(out + '/*.json')):
    r = json.load(open(f)); d = r['diet_optimised']; kJ = r['optimised_totals']['kJ']
    sg = sum(x['g_day'] for x in d if x['name'] in ST)
    rows.append([rel, r['zone'], r['preset'], r.get('staples', 0), round(r['capacity_default']), round(r['capacity_optimised']) if r['history'] else '', '', round(sg)])
csv.writer(open(os.path.join(os.getcwd(), 'analysis/nutrition_lp_2025/staples.csv'), 'w', newline='')).writerows(rows); print(len(rows) - 1, 'runs')
PY
