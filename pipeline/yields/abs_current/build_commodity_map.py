#!/usr/bin/env python3
"""Writes commodity_map.json: how each of the model's 91 crop rows is built from the ABS Agricultural Commodities items of 2016-17 to 2020-21.

Each crop has `area` (ha) or `trees` (total trees, as the 2005-10 cubes counted them) and `tonnes`. A list is a set of alternatives: the first
code the ABS published that year is used, and `factor` converts to the model's unit (kg to t, m2 to ha). `status` says how direct the match is:
  direct    the ABS item is the same commodity
  combined  the ABS publishes a group and it is assigned to one model row (see note); the other rows of the group are absent
  absent    the ABS no longer publishes it at NRM level, so the model fills it as it does for any commodity a region does not report
"""
import json, os
C = lambda code, f=1.0: {"code": code, "factor": f}
KG, T, HA, M2 = 0.001, 1.0, 1.0, 1e-4
crops = {}
def d(name, area=None, trees=None, tonnes=None, status="direct", note=""):
    crops[name] = {"status": status, "area": area or [], "trees": trees or [], "tonnes": tonnes or [], "note": note}
for name, k in (("Wheat", "WHT"), ("Oats", "OAT"), ("Barley", "BAR"), ("Sorghum", "SOR"), ("Maize", "MAI"), ("Rice", "RIC"), ("Triticale", "TRI")):
    d(name, [C(f"AGCEREAL_AHA{k}_F")], tonnes=[C(f"AGCEREAL_ATO{k}_F")], note="Triticale is reported 2016-17 to 2018-19 only" if k == "TRI" else "")
d("Sugar cane", [C("AGSUGARCRSAHA_F")], tonnes=[C("AGSUGARCRSATO_F")], note="cut for crushing")
d("Canola", [C("AGOTHCROP_AHACAN_F")], tonnes=[C("AGOTHCROP_ATOCAN_F")])
d("Chickpeas", [C("AGOTHCROP_AHACHI_F")], tonnes=[C("AGOTHCROP_ATOCHI_F")], note="reported 2019-20 and 2020-21 only")
d("Lentils", [C("AGOTHCROP_AHALEN_F")], tonnes=[C("AGOTHCROP_ATOLEN_F")], note="reported 2020-21 only")
d("Peanuts", [C("AGOTHCROP_AHAPNT_F")], tonnes=[C("AGOTHCROP_AKGPNT_F", KG)], note="reported 2016-17 and 2017-18 only")
for n in ("Field beans", "Mung beans", "Field peas"): d(n, status="absent", note="inside the ABS group 'Other pulses and legumes'")
for n in ("Soybeans", "Sunflower"): d(n, status="absent", note="inside the ABS group 'Other oilseeds'")
veg = {  # model row: (area codes, tonnes codes, status, note)
 "Beans (French and runner)": ([C("AGVEGBEANAHA_F")], [C("AGVEGBEANKG_F", KG)], "direct", "the ABS item is 'Beans (including french and runner)'"),
 "Broccoli": ([C("AGVEGEBROCAHA_F")], [C("AGVEGEBROCAKG_F", KG)], "direct", ""),
 "Brussels sprouts": ([C("AGVEGEBRUSAHA_F")], [C("AGVEGEBRUSAKG_F", KG)], "direct", "reported 2016-17 to 2018-19 only"),
 "Cabbages": ([C("AGVEGECABBAHA_F")], [C("AGVEGECABBATO_F")], "direct", ""),
 "Capsicums": ([C("AGVEGECAPSAHA_F")], [C("AGVEGECAPSAKG_F", KG)], "direct", "excluding chillies, as the ABS item says"),
 "Carrots": ([C("AGVEGECARRAHA_F")], [C("AGVEGECARRATO_F")], "direct", ""),
 "Cauliflowers": ([C("AGVEGECAULAHA_F")], [C("AGVEGECAULATO_F")], "direct", ""),
 "Cucumber": ([C("AGVEGCUCUAHA_F")], [C("AGVEGCUCUATO_F")], "direct", "reported 2020-21 only"),
 "Sweet corn": ([C("AGVEGECORNAHA_F")], [C("AGVEGECORNATO_F")], "direct", ""),
 "Lettuce (head)": ([C("AGVEGELETTAHA_F")], [C("AGVEGELETTAKG_F", KG)], "combined", "the ABS publishes all lettuces together; assigned to head lettuce, 'Lettuce (other)' is absent"),
 "Rock and cantaloupe": ([C("AGVEGEMELNAHA_F")], [C("AGVEGEMELNATO_F")], "combined", "the ABS publishes all melons together (including water and bitter melons); assigned here, honeydews and watermelons are absent"),
 "Mushrooms": ([C("AGVEGEMUSHAM2_F", M2)], [C("AGVEGEMUSHAKG_F", KG)], "direct", "area is in m2"),
 "Onions": ([C("AGVEGEONIOAHA_F")], [C("AGVEGEONIOATO_F")], "direct", ""),
 "Peas (green)": ([C("AGVEGEPEASAHA_F")], [C("AGVEGEPEASAKG_F", KG)], "direct", "reported 2016-17 to 2018-19 only"),
 "Potatoes": ([C("AGVEGEPOTAAHA_F")], [C("AGVEGEPOTAATO_F")], "direct", ""),
 "Pumpkins": ([C("AGVEGEPUMPAHA_F")], [C("AGVEGEPUMPATO_F")], "direct", ""),
 "Tomatoes": ([C("AGVEGETOMAAHA_F")], [C("AGVEGETOMAATO_F")], "direct", "fresh market, processing and undercover together"),
 "Other herbs (incl. basil)": ([C("AGVEGEHERBAM2_F", M2)], [C("AGVEGEHERBAKG_F", KG)], "combined", "all herbs including parsley, reported 2020-21 only, area in m2; assigned here, 'Parsley' is absent"),
}
for n, (a, t, s, note) in veg.items(): d(n, a, tonnes=t, status=s, note=note)
fruit = {  # model row: (total trees code, kg code, t code)
 "Oranges": ("AGFRUTORNGTREE_F", "AGFRUTORNGAKG_F", "AGFRUTORNGATO_F"), "Mandarins": ("AGFRUTMANDTRE_F", "AGFRUTMANDAKG_F", "AGFRUTMANDATO_F"),
 "Apricots": ("AGFRUTAPRTRE_F", "AGFRUTAPRIAKG_F", None), "Cherries": ("AGFRUTCHERTREE_F", "AGFRUTCHERAKG_F", "AGFRUTCHERATO_F"),
 "Nectarines": ("AGFRUTNECTREE_F", "AGFRUTNECTAKG_F", "AGFRUTNECTATO_F"), "Peaches": ("AGFRUTPEATREE_F", "AGFRUTPECHAKG_F", "AGFRUTPEACATO_F"),
 "Apples": ("AGFRUTAPPTREE_F", "AGFRUTAPPLAKG_F", "AGFRUTAPPLATO_F"), "Pears": ("AGFRUTNASPTREE_F", "AGFRUTNASPEARAKG_F", "AGFRUTNASPEARATO_F"),
 "Olives": ("AGFRUTOLITREE_F", "AGFRUTOLIVAKG_F", "AGFRUTOLIVATO_F"), "Avocados": ("AGFRUTAVOTREE_F", "AGFRUTAVOCAKG_F", "AGFRUTAVOCATO_F"),
 "Mangoes": ("AGFRUTMANTREE_F", "AGFRUTMANGAKG_F", "AGFRUTMANGATO_F"), "Almonds": ("AGFRUTALMNUM_F", "AGFRUTALMOAKG_F", "AGFRUTALMOATO_F"),
 "Macadamias": ("AGFRUTMACNUM_F", "AGFRUTMCDMAKG_F", "AGFRUTMACAATO_F"),
}
for n, (tr, kg, t) in fruit.items():
    d(n, trees=[C(tr)], tonnes=([C(t)] if t else []) + [C(kg, KG)], note="production in kg to 2018-19, in t from 2019-20" + ("; reported to 2018-19 only" if n == "Apricots" else "") + "; total trees, as the 2005-10 cubes counted them")
d("Strawberries", [C("AGFRUTSTRWAHABEA_F")], tonnes=[C("AGFRUTSTRAWBATO_F"), C("AGFRUTSTRWAKG_F", KG)], note="area of bearing age")
d("Bananas", [C("AGFRUTBANAAHA_F")], tonnes=[C("AGFRUTBANAATO_F")], note="total area")
d("Pineapples", [C("AGFRUTPINEAHA_F")], tonnes=[C("AGFRUTPINEATO_F")], note="total area")
d("Grape", [C("AGGRAPE_AHA_F")], tonnes=[C("AGGRAPE_ATO_F")], note="all grapes, total area")
model = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_crops.json")))["crops"]
for n in model:
    if n not in crops:
        d(n, status="absent", note="cotton is not in the NRM cubes" if n == "Cotton lint" else ("grouped with other citrus or stone fruit, with trees but no production" if n in ("Lemons", "Limes", "Grapefruit", "Plums") else "the ABS no longer publishes this item at NRM level"))
out = {"source": "ABS Agricultural Commodities, Australia, NRM tables 2016-17 to 2020-21; model rows from model_crops.json", "crops": [dict(crop=n, **crops[n]) for n in model]}
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "commodity_map.json"), "w"), indent=1)
from collections import Counter
print(Counter(crops[n]["status"] for n in model))
