#!/bin/bash
# Runs the nutrition-constrained optimisation for Australia and the seven states, short and long term, in four variants; writes variants.csv and one JSON per run in $OUT.
#   bash analysis/nutrition_lp_2025/run_all.sh RELEASE OUT_DIR        (repository root)
REL=${1:-2025-improved}; OUT=${2:-/tmp/nutrition_lp}; mkdir -p "$OUT"
for z in 1 2 15 26 40 49 56 60; do for pr in short long; do
  python3 -I analysis/nutrition_lp_2025/optimise.py $REL $z $pr $OUT/${z}_${pr}_free.json 1 >/dev/null 2>&1
  python3 -I analysis/nutrition_lp_2025/optimise.py $REL $z $pr $OUT/${z}_${pr}_fixcap3.json 1 fixgroups cap3 >/dev/null 2>&1
  python3 -I analysis/nutrition_lp_2025/optimise.py $REL $z $pr $OUT/${z}_${pr}_famcap3.json 1 cap3 >/dev/null 2>&1
done; done
python3 -I - "$OUT" "$REL" <<'PY'
import json, glob, os, csv, sys
out, rel = sys.argv[1:3]; rows = [['release', 'zone', 'preset', 'variant', 'capacity_default', 'capacity_optimised', 'gain']]
for f in sorted(glob.glob(out + '/*.json')):
    r = json.load(open(f)); v = os.path.basename(f).rsplit('_', 1)[1][:-5]
    rows.append([rel, r['zone'], r['preset'], v, round(r['capacity_default']), round(r['capacity_optimised']), round(r['gain'], 3)])
csv.writer(open(os.path.join(os.getcwd(), 'analysis/nutrition_lp_2025/variants.csv'), 'w', newline='')).writerows(rows); print(len(rows) - 1, 'runs')
PY
