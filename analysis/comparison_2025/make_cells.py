#!/usr/bin/env python3
"""Writes the releases that make up the two-by-two of the comparison (data vintage x method): releases/2011 (original), 2011-improved, 2025-mirror, 2025-improved.
Usage: python3 analysis/comparison_2025/make_cells.py          (repository root; the method modules in methods/ must exist)

                      thesis method (line 1)              improved method (line 2)
  2011 data           2011-corrected (default; 2011)      2011-improved
  2025 data           2025-mirror (= 2025-fuel)           2025-improved

The improved method is the list of method modules IMPROVED. Modules that need data of their own vintage (a resilience table recomputed from the data to 2010 for the 2011 cell) are not in the list;
they stay alternates (2025-resilience-loo) until the 2011-vintage table exists. Change IMPROVED here, rerun, and every cell follows.
"""
import json, os
ROOT = os.getcwd(); IMPROVED = ['reserve-pro-rata', 'recycling-stage']
mods = {m: json.load(open(os.path.join(ROOT, f'methods/{m}/method.json'))) for m in IMPROVED}
what = '; '.join(f"{m} ({mods[m]['label'][0].lower() + mods[m]['label'][1:]})" for m in IMPROVED)
rels = {
 '2025-mirror': {'id': '2025-mirror', 'label': 'Line 1: 2025 data with the thesis method', 'status': 'current', 'extends': '2025-fuel',
   'description': "The 2025 data with the method of the thesis, unchanged (line 1 of the two lines of enquiry): the tip of the data chain, identical to 2025-fuel. Compare with 2011-corrected for a like-for-like change since 2011, and with 2025-improved for the effect of the improved method on the same data."},
 '2025-improved': {'id': '2025-improved', 'label': 'Line 2: 2025 data with the improved method', 'status': 'current', 'extends': '2025-fuel', 'methods': IMPROVED,
   'description': f"The 2025 data of 2025-fuel with the improved method (line 2): the method modules {what}. Compare with 2025-mirror for the effect of the method on the same data."},
 '2011-improved': {'id': '2011-improved', 'label': 'Line 2: 2011 data with the improved method', 'status': 'current', 'extends': '2011-corrected', 'methods': IMPROVED,
   'description': f"The 2011 data and zones of 2011-corrected with the improved method (line 2): the method modules {what}. Compare with 2011-corrected for the effect of the method on the old data, and with 2025-improved for the effect of the data on the improved method. The recycling module's practice of 2018-19 is the only data it has, so the 2011 short term borrows it.",
   'errata': ["Resilience: the improved method for the 2025 cell may later include a leave-one-out resilience table; that table is data of its own vintage and has not been computed for the 2011 cell, so it is not in the improved list."]}}
idx = json.load(open(os.path.join(ROOT, 'releases/index.json')))
for rid, rel in rels.items():
    os.makedirs(os.path.join(ROOT, f'releases/{rid}'), exist_ok=True); json.dump(rel, open(os.path.join(ROOT, f'releases/{rid}/release.json'), 'w'), indent=2)
order = [i for i in idx['order'] if i not in rels]
order.insert(order.index('2011-corrected') + 1, '2011-improved'); order.insert(order.index('2025-fuel'), '2025-mirror'); order.insert(order.index('2025-mirror'), '2025-improved')
idx['order'] = order; json.dump(idx, open(os.path.join(ROOT, 'releases/index.json'), 'w'), indent=2); print(order[:9])
