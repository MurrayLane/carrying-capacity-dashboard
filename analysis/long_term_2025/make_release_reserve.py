#!/usr/bin/env python3
"""Writes releases/2025-reserve/release.json: an alternate of 2025-resilience in which a shortfall of reserve and built land is shared by cropping, pasture and non-agricultural land in proportion to their areas.
Usage: python3 analysis/long_term_2025/make_release_reserve.py          (repository root)

The workbook (Settings rows 54 to 56) takes the land that the reserve and infrastructure settings need beyond what exists from non-agricultural land first, then from pasture, then from cropping,
so in Australia and in most states a 30% reserve costs no productive land at all. The alternate replaces the three cells C55, D55 and E55 ('Updated (minus res+blt)'): with X the shortfall
(reserve plus infrastructure required less existing), each of the three land types loses X in proportion to its area; a surplus still goes to non-agricultural land, as before.
"""
import json, os
ROOT = os.getcwd(); X = '((F55+G55)-(F54+G54))'; S = '(C54+D54+E54)'
def lose(c): return f'=IF({S}=0,0,IF({X}>0,{c}54*MAX(0,1-{X}/{S}),{c}54))'
cells = {'C55': lose('C'), 'D55': lose('D'), 'E55': f'=IF({S}=0,0,IF({X}>0,E54*MAX(0,1-{X}/{S}),E54-{X}))'}
parent = json.load(open(os.path.join(ROOT, 'releases/2025-resilience/release.json')))
rel = {'id': '2025-reserve', 'label': 'Alternate: reserve and infrastructure shortfall shared across cropping, pasture and non-agricultural land', 'status': 'current', 'extends': '2025-resilience',
       'description': "An alternate to 2025-resilience, not a later layer, and a change to the method (three formulas in Settings!C55:E55). The workbook meets any shortfall of reserve and infrastructure land from non-agricultural land first, then pasture, then cropping, so a 30% reserve costs Australia nothing; here the shortfall is shared by cropping, pasture and non-agricultural land in proportion to their areas, in the sense of a reserve that is representative of the land (the Kunming-Montreal Target 3 asks for ecologically representative protected areas). The data layers are those of 2025-resilience. Regions whose existing reserve already meets the setting are unchanged; the long-term result falls where the 30% target exceeds the existing reserve.",
       'layer': parent['layer'], 'vintage': parent['vintage'],
       'model': {'file': parent['model']['file'], 'cellOverrides': {**parent['model']['cellOverrides'], 'Settings': cells}},
       'errata': ["A method change recorded as an alternate (SCOPE.md E13). It treats arid non-agricultural land as equal to farmland for the purpose of the reserve; a reserve weighted toward the productive east and south-west would cost more, one in the rangelands less.",
                  "The short-term reserve setting is the raster share rounded to a whole percent, so the short term changes slightly where rounding makes it exceed the existing reserve."]}
os.makedirs(os.path.join(ROOT, 'releases/2025-reserve'), exist_ok=True); json.dump(rel, open(os.path.join(ROOT, 'releases/2025-reserve/release.json'), 'w'), indent=2)
idx = json.load(open(os.path.join(ROOT, 'releases/index.json')))
if '2025-reserve' not in idx['order']: idx['order'].insert(idx['order'].index('2025-resilience-loo') + 1, '2025-reserve'); json.dump(idx, open(os.path.join(ROOT, 'releases/index.json'), 'w'), indent=2)
print('wrote releases/2025-reserve/release.json;', cells['C55'])
