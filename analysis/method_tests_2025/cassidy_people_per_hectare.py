#!/usr/bin/env python3
"""Method test: people nourished per hectare (Cassidy, West, Gerber and Foley 2013, Environ. Res. Lett. 8: 034015) applied to Australia on current data.
Usage (repository root): python3 -I analysis/method_tests_2025/cassidy_people_per_hectare.py   (reads fbs / half_fbs_countries.csv and fao_qcl_countries.csv; writes cassidy.csv)
       python3 -I analysis/method_tests_2025/cassidy_people_per_hectare.py --match-harvests   (B93, decision 88: also reads fao_qcl_countries_2020.csv when present; writes
         cassidy_matched.csv only, and never over an existing file; cassidy.csv is not touched)

Harvest matching (B93). The food balance books some crops one year behind the crops file: its production for year N is the crops-file harvest of year N-1 (in Australia wheat, barley,
oats, rapeseed and the winter pulses; V31a). The plain run pairs food-balance production and uses of year N with crops-file harvested area of year N. With --match-harvests each item's
lag is tested on the files themselves (food-balance production of N against crops-file production of N and of N-1, for every N in 2021 to 2023 whose N-1 is on disk); an item is
lagged when its N-1 match is within 5% on average and less than half its same-year gap. Lagged items take crops-file area of N-1; all other items, production and uses are unchanged.

The recipe as the paper describes it: for each major crop, the calories produced and the cropland it uses; allocate the crop's calories to human food, animal feed and 'other' (biofuels, industrial) from the
food balance; feed calories reach people only as meat, eggs and dairy at the paper's feed-to-food efficiencies (Table 1: dairy 40%, eggs 22%, chicken 12%, pork 10%, beef 3%); exports follow the average use of
importing countries; calories divided by a 2,700 kcal a day diet (985,500 kcal a year) and by cropland gives PEOPLE FED PER HECTARE, on calories produced and on calories delivered to the food system.
Cropland only: grazing is excluded by the authors (beef counts only if grain-fed; sheep and goats not at all).
Differences from the paper (a reconstruction): 21 crops (cereals, roots, pulses, groundnuts, soybeans, rapeseed, sunflower, sugar) of its 41; FAOSTAT food balance 2011 and 2021-23, not 1997-2003 and EarthStat;
crop energy per kg and the grain-fed share of beef are ASSUMED (below), as the paper's SI was not read; oilseed processing is split 50:50 oil and cake (calories); the oil goes to food and other uses as vegetable oil does worldwide."""
import csv, collections, os, sys
MATCH = '--match-harvests' in sys.argv[1:]
def load(path, key):
    d = collections.defaultdict(dict)
    for r in csv.DictReader(open('analysis/method_tests_2025/' + path)):
        if r['Value'] != '': d[key(r)][r['Year']] = float(r['Value'])
    return d
F = load('half_fbs_countries.csv', lambda r: (r['Area'], r['Item'], r['Element']))
Q = load('fao_qcl_countries.csv', lambda r: (r['Area'], r['Item'], r['Element']))
HAVE_2020 = MATCH and os.path.exists('analysis/method_tests_2025/fao_qcl_countries_2020.csv')
if HAVE_2020:
    for k, v in load('fao_qcl_countries_2020.csv', lambda r: (r['Area'], r['Item'], r['Element'])).items(): Q[k].update(v)
def yv(d, yrs): v = [d[y] for y in yrs if y in d]; return sum(v) / len(v) if v else 0.0
KCAL = {'Wheat and products': 3300, 'Rice and products': 3600, 'Barley and products': 3500, 'Maize and products': 3650, 'Rye and products': 3400, 'Oats': 3900, 'Millet and products': 3700, 'Sorghum and products': 3400,
        'Cereals, other': 3400, 'Cassava and products': 1600, 'Potatoes and products': 770, 'Sweet potatoes': 860, 'Yams': 1180, 'Roots, Other': 1000, 'Beans': 3400, 'Peas': 3400, 'Pulses, Other and products': 3400,
        'Groundnuts': 5670, 'Soyabeans': 4460, 'Rape and Mustardseed': 4880, 'Sunflower seed': 5800, 'Sugar (Raw Equivalent)': 3870}
AREA = {'Wheat and products': ['Wheat'], 'Rice and products': ['Rice'], 'Barley and products': ['Barley'], 'Maize and products': ['Maize (corn)'], 'Rye and products': ['Rye'], 'Oats': ['Oats'], 'Millet and products': ['Millet'],
        'Sorghum and products': ['Sorghum'], 'Cereals, other': ['Cereals n.e.c.', 'Triticale', 'Buckwheat', 'Fonio', 'Quinoa', 'Canary seed', 'Mixed grain'], 'Cassava and products': ['Cassava, fresh'],
        'Potatoes and products': ['Potatoes'], 'Sweet potatoes': ['Sweet potatoes'], 'Yams': ['Yams'], 'Roots, Other': ['Taro', 'Yautia', 'Edible roots and tubers with high starch or inulin content, n.e.c., fresh'],
        'Beans': ['Beans, dry'], 'Peas': ['Peas, dry'], 'Pulses, Other and products': ['Chick peas, dry', 'Cow peas, dry', 'Pigeon peas, dry', 'Lentils, dry', 'Broad beans and horse beans, dry', 'Lupins', 'Vetches', 'Bambara beans, dry', 'Other pulses n.e.c.'],
        'Groundnuts': ['Groundnuts, excluding shelled'], 'Soyabeans': ['Soya beans'], 'Rape and Mustardseed': ['Rape or colza seed'], 'Sunflower seed': ['Sunflower seed'], 'Sugar (Raw Equivalent)': ['Sugar cane', 'Sugar beet']}
OILSEED = ['Groundnuts', 'Soyabeans', 'Rape and Mustardseed', 'Sunflower seed']
LIVE = {'milk': ('Milk - Excluding Butter', 640, .40), 'eggs': ('Eggs', 1430, .22), 'poultry': ('Poultry Meat', 1600, .12), 'pork': ('Pigmeat', 2420, .10), 'beef': ('Bovine Meat', 2500, .03)}
BEEF_GRAIN_SHARE = 0.20
PERSON_YEAR = 2700 * 365                                                        # kcal
def shares(area, item, yrs, oil_food):
    u = {k: yv(F.get((area, item, el), {}), yrs) for k, el in (('food', 'Food'), ('feed', 'Feed'), ('proc', 'Processing'), ('other', 'Other uses (non-food)'))}
    tot = sum(u.values())
    if tot <= 0: return {'food': 0, 'feed': 0, 'other': 0}
    s = {k: v / tot for k, v in u.items()}
    if item in OILSEED:                                                          # processing: half oil (food or other as oil), half cake (feed)
        return {'food': s['food'] + s['proc'] * .5 * oil_food, 'feed': s['feed'] + s['proc'] * .5, 'other': s['other'] + s['proc'] * .5 * (1 - oil_food)}
    return {'food': s['food'] + s['proc'], 'feed': s['feed'], 'other': s['other']}
def run(area, yrs, b=BEEF_GRAIN_SHARE, lagged=()):
    wf = lambda it, el: yv(F.get(('World', it, el), {}), yrs)
    oil_food = wf('Vegetable Oils', 'Food') / (wf('Vegetable Oils', 'Food') + wf('Vegetable Oils', 'Other uses (non-food)'))
    P = sum(wf(i, 'Production') * 1e3 * k * (b if n == 'beef' else 1) for n, (i, k, e) in LIVE.items())            # product kcal (t -> kg)
    R = sum(wf(i, 'Production') * 1e3 * k * (b if n == 'beef' else 1) / e for n, (i, k, e) in LIVE.items())
    eff = P / R
    prod = food = feed = other = delivered = ha = 0.0
    for item, k in KCAL.items():
        p = yv(F.get((area, item, 'Production'), {}), yrs); ex = yv(F.get((area, item, 'Export quantity'), {}), yrs)
        cal = p * 1e6 * k                                                          # 1000 t -> kg x kcal/kg
        if cal <= 0: continue
        es = min(1.0, ex / p) if p else 0.0
        own, wld = shares(area, item, yrs, oil_food), shares('World', item, yrs, oil_food)
        s = {k2: (1 - es) * own[k2] + es * wld[k2] for k2 in own}
        prod += cal; food += cal * s['food']; feed += cal * s['feed']; other += cal * s['other']
        ay = tuple(str(int(y) - 1) for y in yrs) if item in lagged else yrs                       # harvest matching: area of the harvest the food balance books
        if item in lagged: assert all((y in Q.get((area, n, 'Area harvested'), {})) or not Q.get((area, n, 'Area harvested')) for n in AREA[item] for y in ay), ('area year missing', area, item, ay)
        ha += sum(yv(Q.get((area, n, 'Area harvested'), {}), ay) for n in AREA[item])
    delivered = food + feed * eff
    return dict(produced=prod, food=food, feed=feed, other=other, delivered=delivered, ha=ha, eff=eff, oil_food=oil_food)
if MATCH:
    OUTM = 'analysis/method_tests_2025/cassidy_matched.csv'
    assert not os.path.exists(OUTM), 'cassidy_matched.csv exists; not overwritten'
    LAGREF = dict(AREA, **{'Sugar (Raw Equivalent)': ['Raw cane or beet sugar (centrifugal only)']})   # sugar: compare sugar with sugar, not with cane
    def lag_test(area):
        rows, lagged = [], []
        for item in KCAL:
            f = F.get((area, item, 'Production'), {})
            d = {0: [], 1: []}
            for y in ('2021', '2022', '2023'):
                for L in (0, 1):
                    yq = str(int(y) - L)
                    qv = [Q[(area, n, 'Production')][yq] for n in LAGREF[item] if yq in Q.get((area, n, 'Production'), {})]
                    if y in f and f[y] > 0 and qv and sum(qv) > 0 and (L == 0 or yq in ('2020', '2021', '2022') and (HAVE_2020 or yq != '2020')): d[L].append(abs(f[y] * 1e3 - sum(qv)) / sum(qv))
            if not d[0] or not d[1]: rows.append([area, item, '', '', 'no data']); continue
            m0, m1 = sum(d[0]) / len(d[0]), sum(d[1]) / len(d[1])
            lag = 1 if (m1 < .05 and m1 < m0 / 2) else 0
            if lag: lagged.append(item)
            rows.append([area, item, round(100 * m0, 2), round(100 * m1, 2), lag])
        return rows, tuple(lagged)
    LAGS = {a: lag_test(a) for a in ('Australia', 'World')}
    print('per-item lag (mean gap % of food-balance production N against crops-file N and N-1; lag 1 = booked one year behind):')
    for a in LAGS:
        for r in LAGS[a][0]: print(r)
    hdr = ['period', 'country', 'pairing', 'items paired with the previous year\'s harvested area', 'cropland of these crops (Mha)', 'people fed per ha, produced', 'people fed per ha, delivered',
           'people fed by delivered calories (million)']
    outm = [hdr]
    windows = [('2021-23', ('2021', '2022', '2023'))] if HAVE_2020 else []
    windows.append(('2022-23', ('2022', '2023')))
    for label, yrs in windows:
        for c in ('Australia', 'World'):
            sets = [('same year (as cassidy.csv)', ()), ('harvest-matched', LAGS[c][1])]
            if c == 'World': sets.append(('sensitivity: Australia\'s lagged items shifted (the world data show no lag)', LAGS['Australia'][1]))
            for nm, lg in sets:
                r = run(c, yrs, lagged=lg)
                outm.append([label, c, nm, '; '.join(lg) if lg else 'none', round(r['ha'] / 1e6, 2), round(r['produced'] / r['ha'] / PERSON_YEAR, 2), round(r['delivered'] / r['ha'] / PERSON_YEAR, 2),
                             round(r['delivered'] / PERSON_YEAR / 1e6, 1)])
    if not HAVE_2020: print('fao_qcl_countries_2020.csv not found: the 2021-23 window cannot be matched; 2022-23 only')
    csv.writer(open(OUTM, 'w', newline='')).writerows(outm)
    for r in outm: print(r)
    raise SystemExit(0)
out = [['period', 'country', 'cropland of these crops (Mha)', 'calories produced (1e15 kcal)', 'food %', 'feed %', 'other %', 'delivered % of produced', 'people fed per ha, produced', 'people fed per ha, delivered', 'people fed by delivered calories (million)']]
for label, yrs in (('2011', ('2011',)), ('2021-23', ('2021', '2022', '2023'))):
    for c in ['World', 'United States of America', 'India', 'China', 'Brazil', 'Australia']:
        r = run(c, yrs)
        out.append([label, c, round(r['ha'] / 1e6, 1), round(r['produced'] / 1e15, 2), round(100 * r['food'] / r['produced']), round(100 * r['feed'] / r['produced']), round(100 * r['other'] / r['produced']),
                    round(100 * r['delivered'] / r['produced']), round(r['produced'] / r['ha'] / PERSON_YEAR, 1), round(r['delivered'] / r['ha'] / PERSON_YEAR, 1), round(r['delivered'] / PERSON_YEAR / 1e6, 1)])
csv.writer(open('analysis/method_tests_2025/cassidy.csv', 'w', newline='')).writerows(out)
for r in out: print(r)
sens = [['grain-fed share of beef', 'average feed-to-food efficiency', 'Australia 2021-23 people fed per ha, delivered', 'World 2011 delivered']]
for b in (0.0, 0.2, 0.5, 1.0):
    ra, rw = run('Australia', ('2021', '2022', '2023'), b), run('World', ('2011',), b)
    sens.append([b, round(ra['eff'], 3), round(ra['delivered'] / ra['ha'] / PERSON_YEAR, 1), round(rw['delivered'] / rw['ha'] / PERSON_YEAR, 1)])
print(); [print(r) for r in sens]
print('Cassidy 2013 (about 2000): world produced 9.46e15 kcal, food 55%, feed 36%, other 9%, delivered 59%, 10.1 produced and 6.0 delivered people per ha on 947 Mha; US 16.1 and 5.4; India 6.5 and 5.9; China 13.5 and 8.4; Brazil 10.6 and 5.2')
