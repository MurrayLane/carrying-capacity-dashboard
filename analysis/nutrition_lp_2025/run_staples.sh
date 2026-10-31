#!/bin/bash
# Tropical-staples template (SCOPE.md E16): the nutrition-constrained diet (ten micronutrients, no food above 3 times its present intake except the staples)
# with at least 0, 10, 20 or 30% of energy from banana, sweet potato and cassava; Australia, Queensland, Northern Territory; "range" keeps the
# food-group ranges of the Diet sheet, "relaxed" lifts the upper limit on starchy vegetables and fruit and the lower limit on cereals, "relaxed+protein55" also sets the protein floor to 55 g a day (the NHMRC RDI averaged over men and women) instead of the family diets' 95 g. Global search; each variant starts from the stricter one (range -> relaxed -> relaxed+protein55); skips runs already in OUT_DIR. Writes staples.csv.
#   bash analysis/nutrition_lp_2025/run_staples.sh RELEASE OUT_DIR        (repository root)
REL=${1:-2025-improved}; OUT=${2:-/tmp/nutrition_staples}; mkdir -p "$OUT"
for z in 1 26 60; do for pr in short long; do for s in 0.3 0.2 0.1 0; do
  R=$OUT/${z}_${pr}_s${s}
  [ -s ${R}_range.json ] || python3 -I analysis/nutrition_lp_2025/optimise.py $REL $z $pr ${R}_range.json 1 micro cap3 staples$s >/dev/null 2>&1
  [ -s ${R}_relaxed.json ] || python3 -I analysis/nutrition_lp_2025/optimise.py $REL $z $pr ${R}_relaxed.json 1 micro cap3 relaxgroups staples$s start=${R}_range.json >/dev/null 2>&1
  [ -s ${R}_prot55.json ] || python3 -I analysis/nutrition_lp_2025/optimise.py $REL $z $pr ${R}_prot55.json 1 micro cap3 relaxgroups protfloor55 staples$s start=${R}_relaxed.json >/dev/null 2>&1
done; done; done
python3 -I - "$OUT" "$REL" <<'PY'
import json, glob, os, csv, sys
out, rel = sys.argv[1:3]; rows = [['release', 'zone', 'preset', 'groups', 'staples_min_energy_share', 'feasible', 'capacity_default', 'capacity_optimised', 'staples_energy_share', 'staples_energy_share_default']]
for f in sorted(glob.glob(out + '/*.json')):
    r = json.load(open(f)); ok = r.get('staples', 0) == 0 or r['capacity_optimised'] > r['capacity_default'] * 1.0005          # an infeasible run ends at the default diet
    rows.append([rel, r['zone'], r['preset'], ('relaxed+protein55' if r.get('protfloor') else 'relaxed') if r.get('relaxgroups') else 'range', r.get('staples', 0), 'yes' if ok else 'no', round(r['capacity_default']), round(r['capacity_optimised']) if ok else '', round(r['staples_energy_share'], 3) if ok else '', round(r['staples_energy_share_default'], 3)])
csv.writer(open(os.path.join(os.getcwd(), 'analysis/nutrition_lp_2025/staples.csv'), 'w', newline='')).writerows(rows); print(len(rows) - 1, 'runs')
PY
