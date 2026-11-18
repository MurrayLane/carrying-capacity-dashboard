#!/bin/sh
# B137 (X118). From the repository root; needs the built data (cd web && node scripts/build-data.mjs) and the ABS livestock files.
#   sh analysis/years_2025/rebuild_years.sh ABS_DIR WORK_DIR
# Writes analysis/years_2025/years_rebuilt_series_where_held.csv (2016-17 to 2019-20 on placeholders, 2020-21 onward on the national series: the release's own method)
#        analysis/years_2025/years_rebuilt_placeholders.csv   (all eight years on placeholders: reproduces the committed analysis/reliability_2025/years.csv except its base row)
set -e
ABS="$1"; WORK="$2"
python3 -I analysis/years_2025/build_years_fixed.py "$WORK/mixed" "$ABS" > /dev/null
node analysis/sensitivity_2025/evaluate.mjs "$WORK/mixed/years.json" analysis/years_2025/years_rebuilt_series_where_held.csv
B137_ALL_PLACEHOLDERS=1 python3 -I analysis/years_2025/build_years_fixed.py "$WORK/off" "$ABS" > /dev/null
node analysis/sensitivity_2025/evaluate.mjs "$WORK/off/years.json" analysis/years_2025/years_rebuilt_placeholders.csv
