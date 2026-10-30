#!/usr/bin/env python3
"""Writes the releases of the comparison grid: data vintage (2011, 2025) by method tier (published, corrected, improved).
Usage: python3 analysis/comparison_2025/make_cells.py          (repository root; the method modules in methods/ must exist)

                  published (thesis method,        corrected (CORRECTIONS:           improved (CORRECTIONS + IMPROVED:
                  bugs kept: line 1)               errors against the thesis's       judgement-based method changes: line 2)
                                                   own sources, no judgement)
  2011 data       2011-corrected (default; 2011)   2011-fixed                        2011-improved
  2025 data       2025-mirror (= 2025-fuel)        2025-fixed                        2025-improved

The tiers separate three kinds of change: the correction of errors (no judgement: the workbook disagrees with the source it cites), the improvements (judgement: a method the thesis did not use) and the data.
Modules that need data of their own vintage (a resilience table recomputed from the data to 2010 for the 2011 cell) are in neither list; they stay alternates (2025-resilience-loo) until the 2011-vintage table exists.
Change a list here, rerun, and every cell follows (then: cd web && npm run results).
"""
import json, os
ROOT = os.getcwd(); CORRECTIONS = ['biodiesel-yield', 'beef-carcase-yield']; IMPROVED = ['reserve-pro-rata', 'recycling-stage', 'loss-factors-australia', 'regional-beef-output', 'organic-ruminant-factor']
def label(m): j = json.load(open(os.path.join(ROOT, f'methods/{m}/method.json'))); return f"{m} ({j['label'][0].lower() + j['label'][1:]})"
fixes, improvements = '; '.join(label(m) for m in CORRECTIONS), '; '.join(label(m) for m in IMPROVED)
rels = {
 '2025-mirror': {'id': '2025-mirror', 'label': 'Published method: 2025 data with the thesis method', 'status': 'current', 'extends': '2025-diet',
   'description': "The 2025 data with the method of the thesis, unchanged and its errors kept (line 1 of the two lines of enquiry): the tip of the data chain, identical to 2025-diet. Compare with 2011-corrected for a like-for-like change since 2011, with 2025-fixed for the effect of correcting errors and with 2025-improved for the effect of the improved method on the same data."},
 '2011-fixed': {'id': '2011-fixed', 'label': 'Corrected method: 2011 data with errors against the thesis sources corrected', 'status': 'current', 'extends': '2011-corrected', 'methods': CORRECTIONS,
   'description': f"The 2011 data and zones of 2011-corrected with the corrections to the method (errors against the thesis's own sources, no judgement): {fixes}. It shows what the thesis's results would have been without them."},
 '2025-fixed': {'id': '2025-fixed', 'label': 'Corrected method: 2025 data with errors against the thesis sources corrected', 'status': 'current', 'extends': '2025-diet', 'methods': CORRECTIONS,
   'description': f"The 2025 data of 2025-diet with the corrections to the method (errors against the thesis's own sources, no judgement): {fixes}. Compare with 2025-mirror for the effect of the corrections and with 2011-fixed for the like-for-like change since 2011 on the corrected method."},
 '2025-improved': {'id': '2025-improved', 'label': 'Improved method: 2025 data with the corrections and the improved method', 'status': 'current', 'extends': '2025-diet', 'methods': CORRECTIONS + IMPROVED,
   'description': f"The 2025 data of 2025-diet with the corrections ({fixes}) and the improved method (line 2): {improvements}. Compare with 2025-fixed for the effect of the improvements alone."},
 '2011-improved': {'id': '2011-improved', 'label': 'Improved method: 2011 data with the corrections and the improved method', 'status': 'current', 'extends': '2011-corrected', 'methods': CORRECTIONS + IMPROVED,
   'description': f"The 2011 data and zones of 2011-corrected with the corrections ({fixes}) and the improved method (line 2): {improvements}. Compare with 2011-fixed for the effect of the improvements on the old data, and with 2025-improved for the effect of the data. The recycling module's practice of 2018-19 is the only data it has, so the 2011 short term borrows it.",
   'errata': ["Resilience: the improved method for the 2025 cell may later include a leave-one-out resilience table; that table is data of its own vintage and has not been computed for the 2011 cell, so it is not in the improved list."]}}
idx = json.load(open(os.path.join(ROOT, 'releases/index.json')))
for rid, rel in rels.items():
    os.makedirs(os.path.join(ROOT, f'releases/{rid}'), exist_ok=True); json.dump(rel, open(os.path.join(ROOT, f'releases/{rid}/release.json'), 'w'), indent=2)
order = [i for i in idx['order'] if i not in rels]
k = order.index('2011-corrected') + 1; order[k:k] = ['2011-fixed', '2011-improved']
k = order.index('2025-fuel'); order[k:k] = ['2025-improved', '2025-fixed', '2025-mirror']
stores = [i for i in order if i.startswith('2025-store-')]; order = [i for i in order if i not in stores]; k = order.index('2025-improved') + 1; order[k:k] = stores        # scenarios on the improved cell follow it
idx['order'] = order; json.dump(idx, open(os.path.join(ROOT, 'releases/index.json'), 'w'), indent=2); print(order[:12])
