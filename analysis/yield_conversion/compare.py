"""Pair the workbook's stored yields with yields rebuilt from the archived ABS cubes.

Env: ABS_XLS_DIR (from fetch_abs_archive.py), MODEL_XLS (model/model.xls). Writes pairs.json.
For each crop and each of the thesis's NRM regions: the mean of yearly yields (production / area, 2006-07 to
2009-10, years with at least 10 ha and 10 t), the workbook's stored yield, and the region's default irrigation share.
"""
import collections, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import parse_abs, xlrd
from parse_abs import norm
data, log = parse_abs.collect()
wb = xlrd.open_workbook(os.environ['MODEL_XLS']); yv, st = wb.sheet_by_name('Yield'), wb.sheet_by_name('Settings')
ROW = {'Wheat': 4, 'Oats': 5, 'Barley': 6, 'Sorghum': 7, 'Maize': 8, 'Rice': 9, 'Sugar cane': 11, 'Canola': 12, 'Potatoes': 52}   # 1-based sheet rows
def cell(sh, r, c):
    return sh.cell_value(r, c) if r < sh.nrows and c < sh.row_len(r) else None
irr = {int(cell(st, 109, c)): cell(st, 123, c) for c in range(1, 64) if isinstance(cell(st, 109, c), float) and isinstance(cell(st, 123, c), float)}
def stored(crop, rid): return yv.cell_value(ROW[crop] - 1, 6 + rid)          # column H is region 1
ALIAS = {
 'NSW': {3: ['Border Rivers-Gwydir'], 4: ['Central West'], 5: ['Hawkesbury-Nepean', 'Sydney Metro'], 6: ['Hunter-Central Rivers'], 7: ['Lachlan'],
         8: ['Lower Murray Darling'], 9: ['Murray'], 10: ['Murrumbidgee'], 11: ['Namoi'], 12: ['Northern Rivers'], 13: ['Southern Rivers'], 14: ['Western']},
 'VIC': {16: ['Corangamite'], 17: ['East Gippsland'], 18: ['Glenelg Hopkins'], 19: ['Goulburn Broken'], 20: ['Mallee'], 21: ['North Central'],
         22: ['North East'], 23: ['Port Phillip and Westernport'], 24: ['West Gippsland'], 25: ['Wimmera']},
 'QLD': {27: ['Border Rivers-Maranoa Balonne', 'Border Rivers and Maranoa Balonne', 'Border Rivers Maranoa-Balonne', 'Border Rivers', 'Maranoa Balonne'],
         28: ['Burdekin'], 29: ['Burnett Mary'], 30: ['Cape York', 'Torres Strait'], 31: ['Condamine'], 32: ['Desert Channels'], 33: ['Fitzroy'],
         34: ['Mackay Whitsunday'], 35: ['Northern Gulf'], 36: ['South East'], 37: ['South West'], 38: ['Southern Gulf'], 39: ['Wet Tropics']},
 'SA': {41: ['Adelaide and Mount Lofty Ranges', 'Adelaide-Mount Lofty Ranges'], 42: ['Alinytjara Wilurara'], 43: ['Eyre Peninsula'], 44: ['Kangaroo Island'],
        45: ['Northern and Yorke'], 46: ['South Australian Arid Lands', 'SA Arid Lands'],
        47: ['South Australian Murray-Darling Basin', 'SA Murray Darling Basin', 'South Australian Murray Darling Basin', 'SA Murray-Darling Basin'], 48: ['South East']},
 'WA': {50: ['Avon'], 51: ['Northern Agricultural'], 52: ['Rangelands'], 53: ['South Coast'], 54: ['South West'], 55: ['Swan']},
 'TAS': {57: ['North'], 58: ['North West'], 59: ['South']},
}
def merged(year, state, names, crop, extra=()):
    a = p = 0.0; found = 0; want = {norm(n) for n in names}
    for (stt, nm), crops in data[year].items():
        if stt == state and norm(nm) in want and crop in crops: a += crops[crop][0]; p += crops[crop][1]; found += 1
    for xs in extra:                                                          # the thesis merges the ACT into Murrumbidgee
        for (stt, nm), crops in data[year].items():
            if stt == xs and crop in crops and norm(nm) in ('act', 'australian capital territory'): a += crops[crop][0]; p += crops[crop][1]; found += 1
    return a, p, found
rows = []
for state, regs in ALIAS.items():
    for rid, names in regs.items():
        for crop in ROW:
            ys = []
            for year in ('2006-07', '2007-08', '2008-09', '2009-10'):
                a, p, f = merged(year, state, names, crop, extra=('ACT',) if rid == 10 else ())
                if a >= 10 and p >= 10: ys.append(p / a * 100)                # g per m2
            fw = stored(crop, rid)
            if len(ys) >= 2 and isinstance(fw, float) and fw > 0:
                m = sum(ys) / len(ys)
                rows.append(dict(crop=crop, rid=rid, state=state, n=len(ys), raw=m, spread=(max(ys) - min(ys)) / m, F=fw, s=irr[rid]))
print(f'{len(rows)} comparable crop-region pairs from {len({r["rid"] for r in rows})} regions:', dict(collections.Counter(r['crop'] for r in rows)))
json.dump(rows, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pairs.json'), 'w'))
