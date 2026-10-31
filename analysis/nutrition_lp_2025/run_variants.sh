#!/bin/bash
# The headline runs of the nutrition model with the global search (successive search, then a scan of the price of pasture land against cropland, then the successive search again),
# each run starting from the diet of the next more constrained one so that a relaxation can never score below the problem it relaxes: fixcap3 (serves per group fixed, no food above 3 times its
# present intake) -> famcap3 (serves per group free within the Diet sheet's range) -> free (no cap); with and without the ten micronutrients; Australia and the seven states, short and long term.
# Skips runs already in OUT_DIR (a run that died can be resumed). Writes variants.csv.
#   bash analysis/nutrition_lp_2025/run_variants.sh RELEASE OUT_DIR        (repository root)
REL=${1:-2025-improved}; OUT=${2:-/tmp/nutrition_variants}; mkdir -p "$OUT"; O=analysis/nutrition_lp_2025/optimise.py
for z in 1 2 15 26 40 49 56 60; do for pr in short long; do for m in nomicro micro; do
  mf=""; [ $m = micro ] && mf="micro"
  [ -s $OUT/${z}_${pr}_${m}_fixcap3.json ] || python3 -I $O $REL $z $pr $OUT/${z}_${pr}_${m}_fixcap3.json 1 $mf fixgroups cap3 >/dev/null 2>&1
  [ -s $OUT/${z}_${pr}_${m}_famcap3.json ] || python3 -I $O $REL $z $pr $OUT/${z}_${pr}_${m}_famcap3.json 1 $mf cap3 start=$OUT/${z}_${pr}_${m}_fixcap3.json >/dev/null 2>&1
  [ -s $OUT/${z}_${pr}_${m}_free.json ] || python3 -I $O $REL $z $pr $OUT/${z}_${pr}_${m}_free.json 1 $mf start=$OUT/${z}_${pr}_${m}_famcap3.json >/dev/null 2>&1
done; done; done
python3 -I - "$OUT" "$REL" <<'PY'
import json, glob, os, csv, sys
out, rel = sys.argv[1:3]; rows = [['release', 'zone', 'preset', 'variant', 'with_micronutrients', 'capacity_default', 'capacity_optimised', 'gain']]
for f in sorted(glob.glob(out + '/*.json')):
    r = json.load(open(f)); z, pr, m, v = os.path.basename(f)[:-5].split('_')
    rows.append([rel, r['zone'], r['preset'], v, 'yes' if m == 'micro' else 'no', round(r['capacity_default']), round(r['capacity_optimised']), round(r['gain'], 3)])
csv.writer(open(os.path.join(os.getcwd(), 'analysis/nutrition_lp_2025/variants.csv'), 'w', newline='')).writerows(rows); print(len(rows) - 1, 'runs')
PY
