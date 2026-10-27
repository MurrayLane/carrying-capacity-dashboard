#!/usr/bin/env python3
"""Proxies for the change since 2011 in the consumption defaults of the model's short-term (today's) settings.

Usage: python3 -I consumption_proxies.py DIR          (run from the repository root; downloads three open files into DIR if they are not there)
Writes data/2025/consumption_proxies.json: for each default, the 2011 value, the proxy, the figures behind it and the value proposed.

Method (Murray, 2026-10-27: use an alternate source or proxy for the change wherever one exists, otherwise keep 2011): the 2011 default is multiplied by the change of an
open series between a base period around 2011 and the latest period. The ratio keeps the 2011 definition of the default even where the source's definition differs from the original's.
  meat and eggs 13%       share of meat + eggs in all food by weight, FAO food balance sheet for Australia, mean 2010-12 against mean 2021-23
  red meat 64%            beef + mutton and goat + pig (the model's "Meat red" is beef, lamb, veal, pork) as a share of those plus poultry, same source and periods
  liquid fuel 2520 L      sales of all petroleum products (ML) per person, Australian Petroleum Statistics, year to June 2011 against year to June 2025, population at 30 June (ABS ERP)
  biofuel 0.5%            ethanol-blended fuel sold (ML) as a share of all petroleum products, same source and years (the ethanol content is about a tenth of the blend; biodiesel sales are not published)
  timber 1 m3            apparent consumption per person (production + imports - exports) of sawnwood, wood-based panels and fuel wood (the model counts houses, buildings and firewood), FAO forestry
                          production and trade, mean 2010-12 against mean 2021-23
  organic 2%             certified organic land: the 2011 default is "just over 12 million hectares (about two percent)" in Murray's own paper (Organic agriculture in human carrying capacity modelling, draft of
                          Feb 2016, archive file "Organic/Organic yeild comparisons 040216.docx"), so the default is scaled by hectares: 44.4 million ha (Australian Organic Market Report snapshot 2026) over 12.0
Not updated for want of a series with a 2011 baseline: textiles (23 kg), natural fibre share (50%), wool share of natural fibre (12%), avoidable food waste (12%: US figures, SCOPE.md E4), recycling (0%),
activity level (1, sedentary), resilience (1 year). The long-term settings are scenarios, not measurements, and are not touched.
"""
import csv, datetime, json, os, sys, urllib.request, zipfile
import openpyxl
ROOT = os.getcwd(); D = sys.argv[1]; os.makedirs(D, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36'}
FILES = {'fbs.zip': 'https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_Oceania.zip', 'forestry.zip': 'https://bulks-faostat.fao.org/production/Forestry_E_Oceania.zip',
         'aps.xlsx': 'https://data.gov.au/data/dataset/d889484e-fb65-4190-a2e3-1739517cbf9b/resource/a5825135-47fa-4c59-a4e8-94e19511cb95/download/australian-petroleum-statistics-data-extract-august-26.xlsx'}
for n, u in FILES.items():
    if not os.path.exists(os.path.join(D, n)): open(os.path.join(D, n), 'wb').write(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=300).read())
def fao(zipname, member):
    return [r for r in csv.DictReader(zipfile.ZipFile(os.path.join(D, zipname)).open(member).read().decode('latin1').splitlines()) if r['Area'] == 'Australia']
fbs = fao('fbs.zip', 'FoodBalanceSheets_E_Oceania_NOFLAG.csv'); forest = fao('forestry.zip', 'Forestry_E_Oceania_NOFLAG.csv')
P1, P2 = (2010, 2011, 2012), (2021, 2022, 2023)
def num(x): return float(x) if x not in ('', None) else 0.0
def food(item, P): return sum(num(next((r['Y%d' % y] for r in fbs if r['Item'] == item and r['Element'] == 'Food supply quantity (kg/capita/yr)'), 0)) for y in P) / len(P)
FOOD = ['Cereals - Excluding Beer', 'Starchy Roots', 'Sugar & Sweeteners', 'Pulses', 'Treenuts', 'Oilcrops', 'Vegetable Oils', 'Vegetables', 'Fruits - Excluding Wine', 'Meat', 'Offals', 'Animal fats', 'Eggs', 'Milk - Excluding Butter', 'Fish, Seafood']
def diet(P):
    tot = sum(food(i, P) for i in FOOD); red = sum(food(i, P) for i in ('Bovine Meat', 'Mutton & Goat Meat', 'Pigmeat', 'Meat, Other')); pou = food('Poultry Meat', P)
    return dict(meat_eggs_share=(food('Meat', P) + food('Eggs', P)) / tot, red_share=red / (red + pou), beef_kg=food('Bovine Meat', P), poultry_kg=pou, meat_kg=food('Meat', P), total_food_kg=tot)
d1, d2 = diet(P1), diet(P2)

def fy_sums(sheet, cols):
    ws = openpyxl.load_workbook(os.path.join(D, 'aps.xlsx'), read_only=True, data_only=True)[sheet]; rows = list(ws.iter_rows(values_only=True)); h = list(rows[0]); out = {}
    for r in rows[1:]:
        if isinstance(r[0], datetime.datetime):
            y = r[0].year + (1 if r[0].month >= 7 else 0); o = out.setdefault(y, {k: 0.0 for k in cols})
            for k in cols:
                v = r[h.index(k)]
                if isinstance(v, (int, float)): o[k] += v
    return out
fuel = fy_sums('Sales of products', ['Total (ML)', 'Ethanol-blended fuel (ML)'])
pop = {}
for r in csv.DictReader(open(os.path.join(ROOT, 'data/sa2/population_erp.csv'))):
    for y in ('2011', '2025'): pop[y] = pop.get(y, 0.0) + float(r[y] or 0)
l2011 = fuel[2011]['Total (ML)'] * 1e6 / pop['2011']; l2025 = fuel[2025]['Total (ML)'] * 1e6 / pop['2025']
e2011 = fuel[2011]['Ethanol-blended fuel (ML)'] / fuel[2011]['Total (ML)']; e2025 = fuel[2025]['Ethanol-blended fuel (ML)'] / fuel[2025]['Total (ML)']

def timber(P):
    prow = next(r for r in fbs if r['Item'] == 'Population' and r['Element'] == 'Total Population - Both sexes'); pops = {y: num(prow['Y%d' % y]) * 1000 for y in P}
    def cons(item, y):
        g = lambda el: num(next((r['Y%d' % y] for r in forest if r['Item'] == item and r['Element'] == el), 0))
        return g('Production') + g('Import quantity') - g('Export quantity')
    return sum(sum(cons(i, y) for i in ('Sawnwood', 'Wood-based panels', 'Wood fuel')) / pops[y] for y in P) / len(P)
t1, t2 = timber(P1), timber(P2)
org1, org2 = 12.0, 44.4                                     # million hectares certified organic: the 2011 paper, the 2026 report
out = {'method': __doc__.split('Method')[1].split('Not updated')[0].strip(), 'periods': {'base': P1, 'latest': P2},
 'meategg': dict(default_2011=0.13, ratio=d2['meat_eggs_share'] / d1['meat_eggs_share'], base=d1, latest=d2),
 'redmeat': dict(default_2011=0.64, ratio=d2['red_share'] / d1['red_share']),
 'fuel': dict(default_2011=2520, ratio=l2025 / l2011, litres_per_person_2011=l2011, litres_per_person_2025=l2025),
 'biofuel': dict(default_2011=0.005, ratio=e2025 / e2011, ethanol_blend_share_2011=e2011, ethanol_blend_share_2025=e2025),
 'timber': dict(default_2011=1.0, ratio=t2 / t1, m3_per_person_base=t1, m3_per_person_latest=t2),
 'organic': dict(default_2011=0.02, ratio=org2 / org1, organic_Mha_2011=org1, organic_Mha_2025=org2)}
def snap(v, step): return round(round(v / step) * step, 6)
out['proposed'] = {'meategg': snap(0.13 * out['meategg']['ratio'], 0.005), 'redmeat': round(0.64 * out['redmeat']['ratio'], 3), 'fuel': round(2520 * out['fuel']['ratio'], -1), 'biofuel': round(0.005 * out['biofuel']['ratio'], 4),
                   'timber': snap(1.0 * out['timber']['ratio'], 0.1), 'organic': round(0.02 * out['organic']['ratio'], 2)}
json.dump(out, open(os.path.join(ROOT, 'data/2025/consumption_proxies.json'), 'w'), indent=1)
for k in ('meategg', 'redmeat', 'fuel', 'biofuel', 'timber', 'organic'): print(f'{k:9s} 2011 default {out[k]["default_2011"]:>7}  change x{out[k]["ratio"]:.3f}  proposed {out["proposed"][k]}')
print({k: round(v, 3) for k, v in d1.items()}); print({k: round(v, 3) for k, v in d2.items()})
