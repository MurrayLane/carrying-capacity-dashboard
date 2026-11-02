#!/bin/bash
# Batch of regionalisations for the results (appends to analysis/regionalise_2025/summary.csv; each run takes a couple of minutes)   cd web && bash ../analysis/regionalise_2025/run_regionalise.sh
cd "$(dirname "$0")/../../web"
for cfg in "short 53 650000" "short 53 325000" "short 53 1300000" "short 53 100000000" "short 89 650000" "short 336 650000" "long 53 650000" "long 89 650000"; do
  set -- $cfg; node ../analysis/regionalise_2025/regionalise.mjs 2025-fixed $1 $2 $3 > /tmp/regionalise_$1_$2_$3.log 2>&1
done
