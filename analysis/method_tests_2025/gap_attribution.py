#!/usr/bin/env python3
"""Gap attribution for the method tests (decision 34, brief B49): each residual between a method test and the author's published figure,
with the candidate causes changed one at a time, and the share of the residual each one explains.

Usage (repository root):
  python3 -I analysis/method_tests_2025/gap_attribution.py 'Production_Crops_Livestock_E_All_Data_(Normalized).csv'
The argument is the FAOSTAT crops and livestock bulk file the folder's extracts were made from (qa/fao_bulk_hashes.csv; its sha256 is checked).
It is read for the Foran and Poldy single-year and grain-definition tests (Australia 1996 to 1999) and the Cassidy yield test
(world and four countries, 1997 to 2003 and 2011), years the folder's extracts do not hold.
Writes gap_attribution.csv only. No existing output is changed: the method scripts are run here as side calculations, with one input changed at a time,
and their own csv writes are cut from the code before it is run.

Convention. residual = published - current (current = the test's own figure, unrounded). For a run with one cause changed, giving figure x:
  explained % = (x - current) / (published - current) x 100.
100% closes the residual; more than 100% overshoots it; a negative share widens it. Shares of the same residual do not add exactly when causes interact.

Murray's rule: outputs are not adjusted to meet the published figures; each residual is explained by named, tested causes or left as unexplained.
Values typed below are quoted from the sources named beside them (page or table given); everything else is computed from the folder's files."""
import collections, csv, hashlib, os, re, sys

HERE = 'analysis/method_tests_2025/'
OUT = []                       # rows of gap_attribution.csv


def src(name):
    return open(HERE + name).read()


def cut(text, marker):
    """The script's code up to (not including) its first output section, so that running it writes nothing."""
    i = text.index(marker)
    return text[:i]


def patch(text, old, new):
    assert text.count(old) == 1, ('patch target not found exactly once', old)
    return text.replace(old, new)


def row(method, case, cid, cause, fig, cur, pub, note='', digits=4):
    res = pub - cur
    expl = '' if fig is None else round((fig - cur) / res * 100, 1)
    OUT.append([method, case, cid, cause, '' if fig is None else round(fig, digits), round(cur, digits), pub, round(res, digits), expl, note])


# ------------------------------------------------------------------ bulk file (checked against qa/fao_bulk_hashes.csv)
if len(sys.argv) != 2:
    raise SystemExit(__doc__)
QCL_PATH = sys.argv[1]
want = next(r['sha256_csv'] for r in csv.DictReader(open('qa/fao_bulk_hashes.csv')) if r['file'].startswith('Production_Crops_Livestock'))
h = hashlib.sha256()
with open(QCL_PATH, 'rb') as fh:
    for blk in iter(lambda: fh.read(1 << 22), b''): h.update(blk)
assert h.hexdigest() == want, 'the bulk file is not the one hashed in qa/fao_bulk_hashes.csv'
CAS_AREAS = ('World', 'United States of America', 'India', 'China', 'Brazil')
CAS_YEARS = [str(y) for y in range(1997, 2004)] + ['2011']
AU_YEARS = ('1996', '1997', '1998', '1999')
BQ = collections.defaultdict(dict)           # (area, item code, element) -> {year: value}
BN = {}                                      # item code -> name
with open(QCL_PATH, encoding='latin-1') as fh:
    for x in csv.DictReader(fh):
        a, y, el = x['Area'], x['Year'], x['Element']
        if el not in ('Production', 'Area harvested') or x['Value'] == '': continue
        if (a == 'Australia' and y in AU_YEARS and el == 'Production') or (a in CAS_AREAS and y in CAS_YEARS):
            BQ[(a, x['Item Code'], el)][y] = float(x['Value'])
            BN[x['Item Code']] = x['Item']
CODE = {n: c for c, n in BN.items()}

# ================================================================== 1. HALF (Alexander et al. 2016), 2011
half_src = cut(src('half_index.py'), "out = [['period', 'country'")
for old, new in [
        ("adj = cropland / harvested", "adj = OVR.get('adj', cropland / harvested)"),
        ("a = sum(yv(Q.get((n, 'Area harvested'), {}), yrs) for n in qn) * adj", "a = OVR.get(('area', item), sum(yv(Q.get((n, 'Area harvested'), {}), yrs) for n in qn)) * adj"),
        ("wf = lambda item, el: yv(F.get(('World', item, el), {}), yrs)", "wf = lambda item, el: OVR.get(('wf', item, el), yv(F.get(('World', item, el), {}), yrs))"),
        ("area_use['Sugar cane']['proc'] * .70 +", "area_use['Sugar cane']['proc'] * OVR.get('cane_sugar', .70) +"),
        ("area_use['Sugar cane']['proc'] * .04", "area_use['Sugar cane']['proc'] * OVR.get('cane_nc', .04)"),
        ("feed_area = sum(a['feed'] for a in area_use.values()) + cake_area", "feed_area = OVR.get('feed_area', sum(a['feed'] for a in area_use.values()) + cake_area)"),
        ("feed_dm = sum(", "feed_dm = OVR.get('feed_dm') or sum("),
        ("pasture = yv(L[('World', 'Permanent meadows and pastures')], yrs) * 1000", "pasture = OVR.get('pasture', yv(L[('World', 'Permanent meadows and pastures')], yrs) * 1000)"),
        ("land = yv(L[('World', 'Land area')], yrs) * 1000", "land = OVR.get('land', yv(L[('World', 'Land area')], yrs) * 1000)")]:
    half_src = patch(half_src, old, new)
OILPROD0, CAKE0 = None, None
HN = {'OVR': {}}
exec(compile(half_src, 'half_index.py (side run)', 'exec'), HN)
OILPROD0 = {k: list(v) for k, v in HN['OILPROD'].items()}; CAKE0 = dict(HN['CAKESHARE'])
Y11 = ('2011',)
HALF_COUNTRIES = [('World', 'World'), ('Australia', 'Australia'), ('United States of America', 'United States'), ('Argentina', 'Argentina'), ('India', 'India')]
HPUB = {r['row']: float(r['value']) for r in csv.DictReader(open(HERE + 'published_values.csv')) if r['table'] == 'half_fidelity'}


def half_run(ovr=None, oil=None, cake=None):
    HN['OVR'].clear(); HN['OVR'].update(ovr or {})
    HN['OILPROD'].clear(); HN['OILPROD'].update(oil or {k: list(v) for k, v in OILPROD0.items()})
    HN['CAKESHARE'].clear(); HN['CAKESHARE'].update(cake or CAKE0)
    w = HN['world'](Y11)
    res = {}
    for c, _ in HALF_COUNTRIES:
        ha, parts, p = HN['half'](w, c, Y11)
        res[c] = ha * w['pop'] / w['land'] * 100
    return res, w


base, w0 = half_run()
# Supplement (Alexander2016_SI.pdf) and paper values for 2011, as printed
SI = {'cropland Mha': 1556, 'harvested Mha': 1378,                                    # paper p. 89 and SI p. 1: 1556 / 1378 = 1.129
      'pasture Mha': 3364,                                                              # SI p. 2, bovine pasture example
      'world land Mha': 13009,                                                          # paper p. 90
      'soy area Mha': 103.8, 'soy food': 10.1, 'soy feed': 13.3, 'soy proc': 224.1, 'soy nonfood': 0.7, 'soy stock': -2.1,   # SI Table S1 and p. 1 (Mt)
      'poultry Mt': 102.5, 'bovine Mt': 66.2, 'pig need Mt DM': 690.9, 'egg need Mt DM': 161.9,                        # SI p. 1 to 2
      'feed pool Mt DM': 1515.4, 'feed area Mha': 504.4}                                 # SI p. 1 to 2
FCR = HN['FCR']
cur_vals = {'cropland Mha': w0['cropland'] / 1e6, 'harvested Mha': w0['harvested'] / 1e6, 'pasture Mha': w0['pasture'] / 1e6, 'world land Mha': w0['land'] / 1e6,
            'soy area Mha': sum(HN['yv'](HN['Q'].get((n, 'Area harvested'), {}), Y11) for n in HN['AREA']['Soyabeans']) / 1e6,
            'poultry Mt': HN['yv'](HN['F'][('World', 'Poultry Meat', 'Production')], Y11) / 1e3, 'bovine Mt': HN['yv'](HN['F'][('World', 'Bovine Meat', 'Production')], Y11) / 1e3,
            'pig need Mt DM': HN['yv'](HN['F'][('World', 'Pigmeat', 'Production')], Y11) / 1e3 * FCR['Pigmeat'], 'egg need Mt DM': HN['yv'](HN['F'][('World', 'Eggs', 'Production')], Y11) / 1e3 * FCR['Eggs'],
            'feed pool Mt DM': w0['feed_dm'] / 1e3, 'feed area Mha': w0['feed_area'] / 1e6}
for el, k in (('Food', 'soy food'), ('Feed', 'soy feed'), ('Processing', 'soy proc'), ('Other uses (non-food)', 'soy nonfood'), ('Stock Variation', 'soy stock')):
    cur_vals[k] = HN['yv'](HN['F'][('World', 'Soyabeans', el)], Y11) / 1e3
for k in SI:
    OUT.append(['HALF', 'input, 2011', 'b0', f'{k}: this build (FAOSTAT current revision) against the paper or supplement as printed', round(cur_vals[k], 2), '', SI[k], '', '',
                'comparison of inputs, not a run'])
soy_ovr = {('area', 'Soyabeans'): SI['soy area Mha'] * 1e6}
for el, k in (('Food', 'soy food'), ('Feed', 'soy feed'), ('Processing', 'soy proc'), ('Other uses (non-food)', 'soy nonfood'), ('Stock Variation', 'soy stock')):
    soy_ovr[('wf', 'Soyabeans', el)] = SI[k] * 1e3
live_ovr = {('wf', 'Poultry Meat', 'Production'): SI['poultry Mt'] * 1e3, ('wf', 'Bovine Meat', 'Production'): SI['bovine Mt'] * 1e3,
            ('wf', 'Pigmeat', 'Production'): SI['pig need Mt DM'] / FCR['Pigmeat'] * 1e3, ('wf', 'Eggs', 'Production'): SI['egg need Mt DM'] / FCR['Eggs'] * 1e3}
adj_si = SI['cropland Mha'] / SI['harvested Mha']
oil_up = {k: [(o, (s + .005 if s < 1 else s)) for o, s in v] for k, v in OILPROD0.items()}
oil_dn = {k: [(o, (s - .005 if s < 1 else s)) for o, s in v] for k, v in OILPROD0.items()}
cake_up = {k: s + .005 for k, s in CAKE0.items()}; cake_dn = {k: s - .005 for k, s in CAKE0.items()}
HALF_CASES = [
    ('a', 'cropland-to-harvested adjustment 1.129 (1,556/1,378, paper p. 89) in place of 1.165 (this build, FAOSTAT current revision)', dict(ovr={'adj': adj_si})),
    ('b1', 'world pasture 3,364 Mha (SI p. 2) in place of this build\'s 2011 permanent meadows and pastures', dict(ovr={'pasture': SI['pasture Mha'] * 1e6})),
    ('b2', 'world livestock output as the SI prints it (poultry 102.5 Mt, bovine 66.2 Mt; pig and egg output implied by their feed needs of 690.9 and 161.9 Mt over the FCRs)', dict(ovr=live_ovr)),
    ('b3', 'soybean balance and area as SI Table S1 prints them (103.8 Mha; food 10.1, feed 13.3, processing 224.1, non-food 0.7, stock -2.1 Mt)', dict(ovr=soy_ovr)),
    ('b4', 'world land 13,009 Mha (paper p. 90) in place of this build\'s FAOSTAT land area', dict(ovr={'land': SI['world land Mha'] * 1e6})),
    ('b5', 'feed pool 1,515.4 Mt dry matter and feed cropland 504.4 Mha as the SI prints them (derived figures, not FAOSTAT quantities; their dry-matter shares are not printed)', dict(ovr={'feed_dm': SI['feed pool Mt DM'] * 1e3, 'feed_area': SI['feed area Mha'] * 1e6})),
    ('a+b1', '(a) with b1', dict(ovr={'adj': adj_si, 'pasture': SI['pasture Mha'] * 1e6})),
    ('a+b5', '(a) with b5', dict(ovr={'adj': adj_si, 'feed_dm': SI['feed pool Mt DM'] * 1e3, 'feed_area': SI['feed area Mha'] * 1e6})),
    ('b1-b4', 'b1 to b4 together (every FAOSTAT quantity or area the paper or SI prints)', dict(ovr={'pasture': SI['pasture Mha'] * 1e6, 'land': SI['world land Mha'] * 1e6, **live_ovr, **soy_ovr})),
    ('a+b1-b4', '(a) with b1 to b4', dict(ovr={'adj': adj_si, 'pasture': SI['pasture Mha'] * 1e6, 'land': SI['world land Mha'] * 1e6, **live_ovr, **soy_ovr})),
    ('a+b1-b5', '(a) with b1 to b5', dict(ovr={'adj': adj_si, 'pasture': SI['pasture Mha'] * 1e6, 'land': SI['world land Mha'] * 1e6, 'feed_dm': SI['feed pool Mt DM'] * 1e3, 'feed_area': SI['feed area Mha'] * 1e6, **live_ovr, **soy_ovr})),
    ('c+', 'processing shares at the upper rounding bound (oil 50.5, palm oil 78.5 and kernel oil 11.5, cake 50.5 or 11.5, cane sugar 70.5 and non-centrifugal 4.5; the SI prints rounded shares only, Table S4)', dict(ovr={'cane_sugar': .705, 'cane_nc': .045}, oil=oil_up, cake=cake_up)),
    ('c-', 'processing shares at the lower rounding bound (each share 0.5 points lower)', dict(ovr={'cane_sugar': .695, 'cane_nc': .035}, oil=oil_dn, cake=cake_dn)),
]
for cid, label, kw in HALF_CASES:
    res, _ = half_run(**kw)
    for c, nm in HALF_COUNTRIES:
        row('HALF', nm + ' 2011', cid, label, res[c], base[c], HPUB[nm], digits=2)
half_run()

# ================================================================== 2. Simpson food pasture, build 3 (thesis rates), 1991-92
TH = list(csv.DictReader(open(HERE + 'wackernagel_1994_food_factors.csv')))
def th(table, item, note=None):
    hit = [r for r in TH if r['table'] == table and r['item'] == item and (note is None or r['note'] == note)]
    assert len(hit) == 1, (table, item, len(hit)); return float(hit[0]['value'].replace(',', '').split()[0])
E41, E12 = 'Appendix 2.1 e41 clothing {wool}', 'Appendix 2.1 e12 animal products'
RATE = th(E41, 'sheep meat production per hectare')                                    # 34 kg/ha/yr (p. 285)
S_PUB = float(next(r['value'] for r in csv.DictReader(open(HERE + 'published_values.csv')) if r['table'] == 'simpson_fidelity' and r['row'].startswith('Pasture')))
# ABS 4306.0 1991-92 (Comparators/), read from the scan: Table 2 (p. 8), technical note on meat (p. 22), per capita note 2 (p. 21) and ERP by age (p. 25)
ABS_PC = {'1991-92': {'beef': 35.8, 'veal': 1.6, 'lamb': 13.4, 'mutton': 7.6}, '1990-91': {'beef': 39.2, 'veal': 1.5, 'lamb': 14.1, 'mutton': 7.7}}   # kg a person, carcase weight
ABS_T = {'1991-92': {'beef and veal': 650620, 'lamb': 232891, 'mutton': 132873}}         # tonnes available for consumption, carcase weight
POP = {'mean 1990-91 (ABS 4306.0 note 2)': 17176910, 'mean 1991-92 (ABS 4306.0 note 2, used by ABS)': 17390836,
       'ERP 30 June 1991 (ABS 4306.0 p. 25, 8,615,409 males + 8,668,627 females)': 8615409 + 8668627, 'ERP 30 June 1992 (ABS 4306.0 p. 25)': 8710959 + 8771634}
RETAIL = {'beef': (.72, .72), 'veal': (.83, .83), 'lamb': (.80, .85), 'mutton': (.80, .85)}   # ABS 4306.0 p. 22; no mutton factor printed, lamb's range applied (assumption)
red = lambda yr: sum(ABS_PC[yr].values())
cur = red('1991-92') / RATE
assert abs(cur - 1.7176) < 1e-3
M, CS = 'Simpson pasture', 'Australia 1991-92, ha a person'
sheep_kg = th('Table A2.3', '94 mutton & lamb + salted meat trade', 'world production') / th('Table A2.3', 'sheep', 'world head') * 1000
rate_printed_inputs = th(E41, 'average meat production of sheep') * th(E41, 'sheep per animal unit') * th(E12, 'pasture carrying capacity')
rate_unrounded = sheep_kg * 5 * 2.47 * 0.5                                                # p. 284: 2.47 cattle/ha x 0.5 yr, before rounding to 1.24
row(M, CS, 'a1', f'sheep-meat rate {rate_printed_inputs:.2f} kg/ha (5.5 x 5 x 1.24, the printed inputs) in place of the printed 34', red('1991-92') / rate_printed_inputs, cur, S_PUB)
row(M, CS, 'a2', f'sheep-meat rate {rate_unrounded:.2f} kg/ha (Table A2.3 world mutton and lamb over world sheep, {sheep_kg:.3f} kg a sheep, x 5 x 2.47 x 0.5, nothing rounded)', red('1991-92') / rate_unrounded, cur, S_PUB)
row(M, CS, 'a3', 'rate that closes the residual (for reference, not a cause)', None, cur, S_PUB, note=f'{red("1991-92") / S_PUB:.2f} kg/ha')
for lab, pick in (('low', 0), ('high', 1)):
    kg = sum(ABS_PC['1991-92'][k] * RETAIL[k][pick] for k in RETAIL)
    row(M, CS, 'b-' + lab, f'red meat at retail weight, {lab} end of the ABS ratios (beef 72%, veal 83%, lamb and mutton {RETAIL["lamb"][pick] * 100:.0f}%; {kg:.1f} kg)', kg / RATE, cur, S_PUB,
        note='ABS 4306.0 p. 22 prints the ratios but calls a retail factor impractical; no mutton ratio printed')
# dairy on pasture: milk cattle at 1.24 a hectare (p. 284) and world milk a milk animal (Table A2.3, p. 297)
milk_kg_cow = th('Table A2.3', 'milk production', 'world production') / th('Table A2.3', '99 milk animals', 'world production') * 1000
milk_kg_cow_can = th('Table A2.3', 'milk production', 'Canada production') / th('Table A2.3', '99 milk animals', 'Canada production') * 1000
cap = th(E12, 'pasture carrying capacity')
milk_ha, milk_ha_can = milk_kg_cow * cap, milk_kg_cow_can * cap
milk_wme = 23.3 / 0.125                                                                  # ABS 4306.0 Table 1 milk solids, at 12.5% solids (simpson_food.py ASSUMPTIONS)
need = (S_PUB - cur)
row(M, CS, 'c1', f'milk on pasture at the world rate ({milk_ha:.0f} kg/ha: {milk_kg_cow:.0f} kg a milk animal, Table A2.3, x 1.24 a hectare, p. 284) that closes the residual', cur + need, cur, S_PUB,
    note=f'{need * milk_ha:.0f} kg whole milk a person, {need * milk_ha / milk_wme * 100:.0f}% of the 1991-92 consumption of {milk_wme:.0f} kg whole-milk equivalent')
row(M, CS, 'c2', f'all 1991-92 milk ({milk_wme:.0f} kg) on pasture at the world rate', cur + milk_wme / milk_ha, cur, S_PUB)
row(M, CS, 'c3', f'milk at the Canadian rate ({milk_ha_can:.0f} kg/ha, Table A2.3) that closes the residual', cur + need, cur, S_PUB,
    note=f'{need * milk_ha_can:.0f} kg whole milk a person, {need * milk_ha_can / milk_wme * 100:.0f}% of 1991-92 consumption')
row(M, CS, 'd1', f'consumption of 1990-91 in place of 1991-92 (ABS Table 2, {red("1990-91"):.1f} kg)', red('1990-91') / RATE, cur, S_PUB, note='ABS 4306.0 gives financial years only')
cal91 = (red('1990-91') + red('1991-92')) / 2
row(M, CS, 'd2', f'calendar 1991 approximated as the mean of 1990-91 and 1991-92 ({cal91:.2f} kg)', cal91 / RATE, cur, S_PUB, note='an approximation; ABS prints no calendar-year figure')
tot = sum(ABS_T['1991-92'].values())
for k, p in POP.items():
    if 'used by ABS' in k: continue
    row(M, CS, 'e', f'1991-92 red meat tonnes ({tot:,} t) over population {k}: {tot / p * 1000:.2f} kg', tot / p * 1000 / RATE, cur, S_PUB,
        note='the paper names 1991 as its year (a census year) and prints no population')
offal = 3.3                                                                               # ABS 4306.0 Table 1, offal and meat n.e.i., 1991-92
row(M, CS, 'f', f'offal and meat n.e.i. ({offal} kg, ABS Table 1) added to red meat (not a listed cause; a definition test)', (red('1991-92') + offal) / RATE, cur, S_PUB)

# ================================================================== 3. Henry and Godden, fidelity check
HG = {'energy': dict(tot=404, out=466, pop=82, f=0.1760, pub=109, total=764, total_pub=206), 'protein': dict(tot=306, out=294, pop=60, f=0.2041, pub=96, total=601, total_pub=188)}  # Tables 2, 4, 5
M = 'Henry and Godden'
for k, v in HG.items():
    cs = f'{k}, 1990-91, million people'
    c0 = v['tot'] * 70 / 45.7 * v['f']
    row(M, cs, 'a', 'energy and protein factors per item against an aggregate factor: the check uses their printed totals (Table 2); item factors are not published', None, c0, v['pub'],
        note='untestable on the published data; explains 0 by construction')
    row(M, cs, 'b1', f'consumption factor unrounded, {v["pop"]}/{v["out"]} (Table 4: projected population over scaled output) in place of {v["f"]}', v['tot'] * 70 / 45.7 * v['pop'] / v['out'], c0, v['pub'],
        note='the only population in the chain is Gifford et al.\'s projected population; no census year enters')
    for d in (-0.5, 0.5):
        row(M, cs, f'b2{"+" if d > 0 else "-"}', f'Gifford\'s projected population {v["pop"] + d} (rounding bound of the printed {v["pop"]})', v['tot'] * 70 / 45.7 * (v['pop'] + d) / v['out'], c0, v['pub'])
    for d in (-0.5, 0.5):
        row(M, cs, f'b3{"+" if d > 0 else "-"}', f'their total {v["tot"] + d} (rounding bound of the printed {v["tot"]}), unrounded factor', (v['tot'] + d) * 70 / 45.7 * v['pop'] / v['out'], c0, v['pub'])
    row(M, cs, 'c', 'rounding of the published whole number: residual as a share of half a unit', None, c0, v['pub'], note=f'{abs(v["pub"] - c0) / 0.5 * 100:.0f}% of half a unit')
    ct = v['total'] * 70 / 45.7 * v['f']
    row(M, f'{k}, 1990-91 total incl. wool and cotton, million people', 'c', 'same recipe on their "total" row (Table 2 total, Table 5 total): the same rounding test', None, ct, v['total_pub'],
        note=f'{abs(v["total_pub"] - ct) / 0.5 * 100:.0f}% of half a unit')

# ================================================================== 4. Foran and Poldy, 1997-98 production
M = 'Foran and Poldy'
def au(code, yrs): return sum(BQ[('Australia', code, 'Production')][y] for y in yrs) / len(yrs) / 1e6
FP = {'grain': 31.578, 'meat': 3.514}                                                    # Table 2.5, ABS
G, MT = CODE['Cereals, primary'], CODE['Meat, Total']
c_g, c_m = au(G, ('1997', '1998')), au(MT, ('1997', '1998'))
OUT.append([M, 'grain 1997-98, Mt', 'a', 'ABS or ABARE production series for 1997-98: no such figure in Comparators/ (ABS 4306.0 1991-92 and 7503.0 1990-91 only); their 31.578 and 3.514 are themselves the ABS figures',
            '', round(c_g, 3), FP['grain'], round(FP['grain'] - c_g, 3), '', 'untestable on hand'])
for nm, yrs in (('calendar 1997 alone', ('1997',)), ('calendar 1998 alone', ('1998',)), ('three-year mean 1996 to 1998', ('1996', '1997', '1998')), ('three-year mean 1997 to 1999', ('1997', '1998', '1999'))):
    row(M, 'grain 1997-98, Mt', 'b', nm + ' in place of the mean of 1997 and 1998', au(G, yrs), c_g, FP['grain'], digits=3)
    row(M, 'meat 1997-98, Mt', 'b', nm + ' in place of the mean of 1997 and 1998', au(MT, yrs), c_m, FP['meat'], digits=3)
WCG = ['Wheat', 'Barley', 'Oats', 'Maize (corn)', 'Sorghum', 'Triticale', 'Rye', 'Millet', 'Mixed grain', 'Buckwheat', 'Canary seed', 'Cereals n.e.c.']
wcg = sum(au(CODE[n], ('1997', '1998')) for n in WCG if n in CODE and ('Australia', CODE[n], 'Production') in BQ)
row(M, 'grain 1997-98, Mt', 'c1', 'wheat plus coarse grains (cereals less rice) in place of cereals primary', wcg, c_g, FP['grain'], digits=3)
row(M, 'grain 1997-98, Mt', 'c2', 'cereals plus pulses ("grains" in the wide Australian sense) in place of cereals primary', c_g + au(CODE['Pulses, Total'], ('1997', '1998')), c_g, FP['grain'], digits=3)
row(M, 'grain 1997-98, Mt', 'b+c1', 'calendar 1997 alone, wheat plus coarse grains', sum(au(CODE[n], ('1997',)) for n in WCG if ('Australia', CODE.get(n), 'Production') in BQ), c_g, FP['grain'], digits=3)
FPM = ['Meat of cattle with the bone, fresh or chilled', 'Meat of sheep, fresh or chilled', 'Meat of pig with the bone, fresh or chilled', 'Meat, Poultry']
row(M, 'meat 1997-98, Mt', 'c3', 'meat as their text lists it (beef and veal, lamb and mutton, pork, chicken: cattle, sheep, pig and poultry meat) in place of FAO total meat (adds goat, horse, game and others)',
    sum(au(CODE[n], ('1997', '1998')) for n in FPM), c_m, FP['meat'], digits=3)

# ================================================================== 5. Cassidy, people per hectare (about 2000) against this build (2011)
cas_src = cut(src('cassidy_people_per_hectare.py'), "out = [['period', 'country'")
cas_src = patch(cas_src, "cal = p * 1e6 * k ", "cal = p * 1e6 * k * YF.get((area, item), 1.0) ")
cas_src = patch(cas_src, "    eff = P / R\n", "    eff = OVR.get('eff', P / R)\n")
CN = {'YF': {}, 'OVR': {}}
exec(compile(cas_src, 'cassidy_people_per_hectare.py (side run)', 'exec'), CN)
CPUB = {(r['row'], r['column']): float(r['value']) for r in csv.DictReader(open(HERE + 'published_values.csv')) if r['table'] == 'cassidy_fidelity'}
PY = CN['PERSON_YEAR']
CC = [('World', 'World'), ('United States of America', 'United States'), ('India', 'India'), ('China', 'China'), ('Brazil', 'Brazil')]
def crop_yield(area, item, yrs):
    names = CN['AREA'][item]
    pr = sum(BQ[(area, CODE[n], 'Production')].get(y, 0) for n in names if n in CODE for y in yrs)
    ar = sum(BQ[(area, CODE[n], 'Area harvested')].get(y, 0) for n in names if n in CODE for y in yrs)
    return pr / ar if ar else None
def cas(area, yf=None, ovr=None, b=CN['BEEF_GRAIN_SHARE']):
    CN['YF'].clear(); CN['YF'].update(yf or {}); CN['OVR'].clear(); CN['OVR'].update(ovr or {})
    r = CN['run'](area, ('2011',), b)
    return r['produced'] / r['ha'] / PY, r['delivered'] / r['ha'] / PY, r
M = 'Cassidy'
for area, nm in CC:
    p0, d0, r0 = cas(area)
    yfs = {}
    for lab, yrs in (('1997 to 2003 mean (the paper\'s data years, p. 2)', [str(y) for y in range(1997, 2004)]), ('2000 alone', ['2000'])):
        yf = {}
        for item in CN['KCAL']:
            a, z = crop_yield(area, item, yrs), crop_yield(area, item, ['2011'])
            if a and z: yf[(area, item)] = a / z
        yfs[lab] = yf
        p1, d1, _ = cas(area, yf=yf)
        row(M, nm + ', people per ha produced', 'a', f'each crop at its own {lab} yield (FAOSTAT, this bulk file), 2011 area and uses held', p1, p0, CPUB[(nm + ', paper', 'People per ha, produced')], digits=4)
        row(M, nm + ', people per ha delivered', 'a', f'each crop at its own {lab} yield, 2011 area and uses held', d1, d0, CPUB[(nm + ', paper', 'People per ha, delivered')], digits=4)
    for b in (0.0, 1.0):
        _, d1, _ = cas(area, b=b)
        row(M, nm + ', people per ha delivered', 'b1', f'grain-fed share of beef {b:.0%} in place of the assumed 20% (the efficiencies themselves are the paper\'s Table 1)', d1, d0, CPUB[(nm + ', paper', 'People per ha, delivered')], digits=4)
    if area == 'World':
        eff_paper = 0.04 / 0.36                                                       # paper p. 4: 36% of calories to feed, 4% reach people as animal products
        _, d1, _ = cas(area, ovr={'eff': eff_paper})
        row(M, nm + ', people per ha delivered', 'b2', f'average feed-to-food efficiency {eff_paper:.3f} (the paper\'s 4% over 36%, p. 4) in place of this build\'s {r0["eff"]:.3f}', d1, d0, CPUB[(nm + ', paper', 'People per ha, delivered')], digits=4)
        y = yfs['1997 to 2003 mean (the paper\'s data years, p. 2)']
        _, d2, _ = cas(area, yf=y, ovr={'eff': eff_paper})
        row(M, nm + ', people per ha delivered', 'a+b2', 'the 1997 to 2003 yields with the paper\'s average efficiency', d2, d0, CPUB[(nm + ', paper', 'People per ha, delivered')], digits=4)
    row(M, nm + ', people per ha produced', 'c', 'calorie basis: this build uses the paper\'s own 2,700 kcal a day (985,500 a year, p. 5)', p0 * PY / (2700 * 365), p0, CPUB[(nm + ', paper', 'People per ha, produced')], digits=4,
        note='the same basis; explains 0 by construction')
cas(area='World')

hdr = ['method', 'case', 'cause_id', 'cause', 'figure', 'current', 'published', 'residual (published - current)', 'explained % of residual', 'note']
csv.writer(open(HERE + 'gap_attribution.csv', 'w', newline='')).writerows([hdr] + OUT)
for r in OUT: print(r)
