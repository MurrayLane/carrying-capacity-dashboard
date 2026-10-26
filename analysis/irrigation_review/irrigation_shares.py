#!/usr/bin/env python3
"""Which irrigation share should drive a yield uplift?

The 2011 dashboard defines irrigation as irrigated area over ALL farmland. A yield uplift acts on crops, so this
compares that share with the irrigated share of cropped land, and with each crop group, from the ABS 2020-21
Water Use on Australian Farms cubes (area grown and area watered by crop group, by NRM region and by state).

Usage: python3 -I irrigation_shares.py WORK_DIR        (needs openpyxl; downloads the two cubes if absent)
Writes irrigation_shares_2020-21.csv and prints the national crop-group table.
"""
import collections, csv, os, re, sys, urllib.request
import openpyxl
work = sys.argv[1]; os.makedirs(work, exist_ok=True)
BASE = "https://www.abs.gov.au/statistics/industry/agriculture/water-use-australian-farms/2020-21/"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36"}
for fn in ("WUAFDCNRM202021.xlsx", "WUAFDCASGS202021.xlsx"):
    if not os.path.exists(os.path.join(work, fn)):
        open(os.path.join(work, fn), "wb").write(urllib.request.urlopen(urllib.request.Request(BASE + fn, headers=UA), timeout=240).read())
# crop group -> (area grown item, area watered item)
GROUPS = {"cereals excluding rice": ("AGCEREALXRICHA_F", "AGWATRCCRPGRSAHA_F"), "rice": ("AGCEREAL_AHARIC_F", "AGWATROCRPAHARIC_F"),
          "cotton": ("AGCOTTPLTDAHA_F", "AGWATROCRPAHACOT_F"), "sugar cane": ("AGSUGARCANAHA_F", "AGWATROCRPAHASUG_F"),
          "vegetables": ("AGVEGE_AHA_F", "AGWATRVEGEAHA_F"), "fruit and nuts": ("AGFRUT_AHA_F", "AGWATRFRUTAHA_F"),
          "grapes": ("AGGRAPE_AHA_F", "AGWATRGRAPAHA_F"), "other crops": ("AGOTHCROPALL_AHA_F", "AGWATROTHCRPAHA_F"),
          "hay and silage": ("AGPASCRHAYSILAHA_F", "AGWATRPHAYSILAHA_F"), "grazed pasture": ("AGLANDGRAZEHA_F", "AGWATRPACRAHAGRZ_F")}
CROPS = [g for g in GROUPS if g not in ("hay and silage", "grazed pasture")]     # cropped land as the thesis counts crops
def load(fn):
    ws = openpyxl.load_workbook(os.path.join(work, fn), read_only=True)["Table 1"]; d = collections.defaultdict(dict); lab = {}
    for i, row in enumerate(ws.iter_rows(values_only=True)):
        if i < 7 or row[0] is None or row[2] is None: continue
        try: d[str(row[0])][str(row[2])] = float(row[4])
        except (TypeError, ValueError): continue
        lab[str(row[0])] = str(row[1])
    return d, lab
out = []
for fn, geography in (("WUAFDCNRM202021.xlsx", "NRM"), ("WUAFDCASGS202021.xlsx", "ASGS")):
    d, lab = load(fn)
    for code, x in d.items():
        hold, wat = x.get("AGLANDTOTLAHA_F", 0), x.get("AGWATRPRODAHA_F", 0)
        grown = sum(x.get(GROUPS[g][0], 0) for g in CROPS); wcrop = sum(x.get(GROUPS[g][1], 0) for g in CROPS)
        if hold > 0 and grown > 0:
            out.append([geography, code, lab[code], round(hold), round(wat), round(grown), round(wcrop),
                        round(wat / hold * 100, 2), round(wcrop / grown * 100, 2)])
    if geography == "NRM":
        x = d["0"]; print("Australia 2020-21, share of area watered, by crop group")
        for g, (a, w) in GROUPS.items():
            if x.get(a, 0) > 0: print(f"  {g:24s} grown {x[a] / 1e6:7.2f} Mha  watered {x.get(w, 0) / 1e6:6.2f} Mha  {x.get(w, 0) / x[a] * 100:5.1f}%")
        print(f"  {'all farmland':24s} holdings {x['AGLANDTOTLAHA_F'] / 1e6:7.1f} Mha  watered {x['AGWATRPRODAHA_F'] / 1e6:6.2f} Mha  {x['AGWATRPRODAHA_F'] / x['AGLANDTOTLAHA_F'] * 100:5.1f}%")
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "irrigation_shares_2020-21.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["geography", "region_code", "region", "holdings_ha", "area_watered_ha", "crop_area_ha", "crop_area_watered_ha",
                                   "watered_pct_of_all_farmland", "watered_pct_of_cropped_land"]); w.writerows(out)
print(f"wrote {len(out)} regions")
