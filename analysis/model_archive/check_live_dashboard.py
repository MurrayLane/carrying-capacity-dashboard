"""Replays the 120 default cases of baseline/baseline_2011.json against the live dashboard (one request every 0.4 s) and compares the answers.
Usage, from the repository root:  python3 -I analysis/model_archive/check_live_dashboard.py
Result on 2026-10-27: all 120 cases identical to the baseline in capacity and in every land-requirement figure, so the live dashboard runs
release 2011. Its default files (default-inputs-short-term.csv and default-inputs-long-term.csv) are also identical to data/2011/, so the
12.5 kg long-term textiles default is live. The server occasionally resets a connection; rerun the failed cases."""
import json, os, sys, time, urllib.parse, urllib.request
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
base = json.load(open(os.path.join(ROOT, 'baseline/baseline_2011.json')))['cases']
out = {}; bad = 0
for i, (key, c) in enumerate(base.items()):
    body = urllib.parse.urlencode(c['params']).encode()
    req = urllib.request.Request('https://dashboard.carryingcapacity.com.au/ProcessExcel', data=body, headers={'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'carrying-capacity-baseline-check/1.0'})
    try: r = json.loads(urllib.request.urlopen(req, timeout=60).read().decode())
    except Exception as e: print('ERR', key, e); bad += 1; r = None
    out[key] = r; time.sleep(0.4)
same = sum(1 for k, c in base.items() if out[k] and out[k]['popcc'] == c['result']['popcc'] and out[k]['requirements'] == c['result']['requirements'])
print('posted', len(out), 'errors', bad, '| identical to the baseline:', same)
