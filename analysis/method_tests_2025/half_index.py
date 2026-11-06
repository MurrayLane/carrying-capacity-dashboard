#!/usr/bin/env python3
"""Method test: the HALF index (Human Appropriation of Land for Food; Alexander, Brown, Arneth, Finnigan and Rounsevell 2016, Global Environmental Change 41: 88-98) rebuilt from FAOSTAT.
Usage (repository root): python3 -I analysis/method_tests_2025/half_index.py   (reads the half_*.csv extracts of extract_fao_half.py; writes half_index.csv and half_world.csv)

Recipe (paper and its supplementary information, Alexander2016_SI.pdf):
  1. World cropland area per crop = harvested area x (cropland / harvested area); allocate it among food, feed, processing and non-food use by mass (seed and waste spread pro rata).
  2. Processed crop area goes to the products by value: oil crops 50:50 oil and cake (palm 78:11:11, olives all oil, seed cotton 85:15 lint and seed), sugar cane 70 sugar : 26 molasses : 4 non-centrifugal,
     sugar beet all sugar, maize 90 sweeteners : 10 germ oil. Cake is feed.
  3. Livestock: feed need = product x feed conversion ratio (kg dry feed per kg edible weight; poultry 3.3, pork 6.4, eggs 2.3, beef 25, other meat 15, milk 0.7). Pigs, poultry and eggs take feed
     (and its cropland) in proportion to need; ruminants take the remaining feed and ALL pasture, shared in proportion to need.
  4. Land per tonne of each commodity = its area over its uses, at WORLD-AVERAGE production. A diet's HALF = sum of (tonnes eaten a person x land per tonne) x world population, as % of world land area.
Differences from the paper (a reconstruction): the NEW FAOSTAT food balance (2010 onward) in place of the 2015 download; 70 consumed commodities of the 90 (beverages, stimulants, spices, fish, offals, animal fats are left out);
feed dry matter by assumed dry-matter shares (below); the 2011 cropland and pasture areas of the current FAOSTAT revision."""
import csv, collections, sys
def load(path, key):
    d = collections.defaultdict(dict)
    for r in csv.DictReader(open('analysis/method_tests_2025/' + path)):
        if r['Value'] == '': continue
        d[key(r)][r['Year']] = float(r['Value'])
    return d
Q = load('half_qcl_world.csv', lambda r: (r['Item'], r['Element']))
F = load('half_fbs_countries.csv', lambda r: (r['Area'], r['Item'], r['Element']))
L = load('half_landuse.csv', lambda r: (r['Area'], r['Item']))
def yv(d, yrs): v = [d[y] for y in yrs if y in d]; return sum(v) / len(v) if v else 0.0
AGG = ('Total', 'Primary', 'Equivalent')
LEAF_CROPS = [i for (i, e) in Q if e == 'Area harvested' and not any(a in i.lower() for a in ('total', 'primary', 'equivalent'))]
# FBS item -> QCL area items
AREA = {'Wheat and products': ['Wheat'], 'Rice and products': ['Rice'], 'Barley and products': ['Barley'], 'Maize and products': ['Maize (corn)'], 'Rye and products': ['Rye'], 'Oats': ['Oats'],
        'Millet and products': ['Millet'], 'Sorghum and products': ['Sorghum'], 'Cereals, other': ['Cereals n.e.c.', 'Triticale', 'Buckwheat', 'Fonio', 'Quinoa', 'Canary seed', 'Mixed grain'],
        'Cassava and products': ['Cassava, fresh'], 'Potatoes and products': ['Potatoes'], 'Sweet potatoes': ['Sweet potatoes'], 'Yams': ['Yams'], 'Roots, Other': ['Taro', 'Yautia', 'Edible roots and tubers with high starch or inulin content, n.e.c., fresh'],
        'Beans': ['Beans, dry'], 'Peas': ['Peas, dry'], 'Pulses, Other and products': ['Chick peas, dry', 'Cow peas, dry', 'Pigeon peas, dry', 'Lentils, dry', 'Broad beans and horse beans, dry', 'Lupins', 'Vetches', 'Bambara beans, dry', 'Other pulses n.e.c.'],
        'Treenuts': ['Treenuts, Total'], 'Groundnuts': ['Groundnuts, excluding shelled'], 'Soyabeans': ['Soya beans'], 'Sunflower seed': ['Sunflower seed'], 'Rape and Mustardseed': ['Rape or colza seed'],
        'Cottonseed': ['Seed cotton, unginned'], 'Coconuts - Incl Copra': ['Coconuts, in shell'], 'Palm kernels': ['Oil palm fruit'], 'Olives (including preserved)': ['Olives'], 'Sesame seed': ['Sesame seed'],
        'Oilcrops, Other': ['Linseed', 'Safflower seed', 'Castor oil seeds', 'Mustard seed', 'Other oil seeds n.e.c.', 'Hempseed', 'Poppy seed', 'Melonseed', 'Karite nuts (sheanuts)', 'Tallowtree seeds', 'Tung nuts', 'Jojoba seeds', 'Kapok fruit'],
        'Sugar cane': ['Sugar cane'], 'Sugar beet': ['Sugar beet'], 'Vegetables': ['Vegetables Primary'], 'Fruits - Excluding Wine': ['Fruit Primary']}
AREA_SHARE = {'Cottonseed': 0.15}                                      # seed cotton: 85 lint, 15 seed
DM = {'cereal': .88, 'pulse': .88, 'oilseed': .90, 'root': .35, 'sugarcrop': .25, 'fruitveg': .12, 'milk': .13}   # assumed dry-matter shares of feed
KIND = {**{i: 'cereal' for i in ['Wheat and products', 'Rice and products', 'Barley and products', 'Maize and products', 'Rye and products', 'Oats', 'Millet and products', 'Sorghum and products', 'Cereals, other']},
        **{i: 'root' for i in ['Cassava and products', 'Potatoes and products', 'Sweet potatoes', 'Yams', 'Roots, Other']}, **{i: 'pulse' for i in ['Beans', 'Peas', 'Pulses, Other and products', 'Treenuts']},
        **{i: 'oilseed' for i in ['Groundnuts', 'Soyabeans', 'Sunflower seed', 'Rape and Mustardseed', 'Cottonseed', 'Coconuts - Incl Copra', 'Palm kernels', 'Olives (including preserved)', 'Sesame seed', 'Oilcrops, Other']},
        'Sugar cane': 'sugarcrop', 'Sugar beet': 'sugarcrop', 'Vegetables': 'fruitveg', 'Fruits - Excluding Wine': 'fruitveg'}
OILPROD = {'Soyabeans': [('Soyabean Oil', .5)], 'Rape and Mustardseed': [('Rape and Mustard Oil', .5)], 'Sunflower seed': [('Sunflowerseed Oil', .5)], 'Cottonseed': [('Cottonseed Oil', .5)],
           'Groundnuts': [('Groundnut Oil', .5)], 'Coconuts - Incl Copra': [('Coconut Oil', .5)], 'Palm kernels': [('Palm Oil', .78), ('Palmkernel Oil', .11)], 'Olives (including preserved)': [('Olive Oil', 1.0)],
           'Sesame seed': [('Sesameseed Oil', .5)], 'Oilcrops, Other': [('Oilcrops Oil, Other', .5)]}
CAKESHARE = {'Soyabeans': .5, 'Rape and Mustardseed': .5, 'Sunflower seed': .5, 'Cottonseed': .5, 'Groundnuts': .5, 'Coconuts - Incl Copra': .5, 'Palm kernels': .11, 'Sesame seed': .5, 'Oilcrops, Other': .5}
FCR = {'Bovine Meat': 25, 'Mutton & Goat Meat': 15, 'Meat, Other': 15, 'Milk - Excluding Butter': .7, 'Pigmeat': 6.4, 'Poultry Meat': 3.3, 'Eggs': 2.3}
RUM = ['Bovine Meat', 'Mutton & Goat Meat', 'Meat, Other', 'Milk - Excluding Butter']; MONO = ['Pigmeat', 'Poultry Meat', 'Eggs']
def world(yrs):
    wf = lambda item, el: yv(F.get(('World', item, el), {}), yrs)
    harvested = sum(yv(Q.get((i, 'Area harvested'), {}), yrs) for i in LEAF_CROPS)
    cropland = yv(L[('World', 'Cropland')], yrs) * 1000
    adj = cropland / harvested
    def uses(item): return {'food': wf(item, 'Food'), 'feed': wf(item, 'Feed'), 'proc': wf(item, 'Processing'), 'other': wf(item, 'Other uses (non-food)')}
    area_use = {}                                                       # area (ha) by crop and use
    for item, qn in AREA.items():
        a = sum(yv(Q.get((n, 'Area harvested'), {}), yrs) for n in qn) * adj * AREA_SHARE.get(item, 1.0)
        u = uses(item); tot = sum(u.values()) - wf(item, 'Stock Variation')
        area_use[item] = {k: (a * v / tot if tot else 0.0) for k, v in u.items()}
        area_use[item]['_adj_total'] = a
    # processed area to products
    prod_area = collections.defaultdict(float); cake_area = 0.0; cake_mass = 0.0
    for item, outs in OILPROD.items():
        pa = area_use[item]['proc']
        for oil, sh in outs: prod_area[oil] += pa * sh
        cake_area += pa * CAKESHARE.get(item, 0.0)
    prod_area['Sugar (Raw Equivalent)'] = area_use['Sugar cane']['proc'] * .70 + area_use['Sugar beet']['proc']
    prod_area['Sugar non-centrifugal'] = area_use['Sugar cane']['proc'] * .04
    prod_area['Sweeteners, Other'] = area_use['Maize and products']['proc'] * .90
    prod_area['Maize Germ Oil'] = area_use['Maize and products']['proc'] * .10
    prod_area['Beer'] = area_use['Barley and products']['proc']
    feed_area = sum(a['feed'] for a in area_use.values()) + cake_area
    feed_dm = sum(wf(i, 'Feed') * DM[KIND[i]] for i in KIND) + yv(Q[('Oilcrops, Cake Equivalent', 'Production')], yrs) * .90
    need = {p: wf(p, 'Production') * FCR[p] for p in FCR}
    mono_need = sum(need[p] for p in MONO); rum_need = sum(need[p] for p in RUM)
    mono_area = {p: feed_area * need[p] / feed_dm for p in MONO}
    rum_feed_area = feed_area * max(feed_dm - mono_need, 0) / feed_dm
    pasture = yv(L[('World', 'Permanent meadows and pastures')], yrs) * 1000
    animal_area = {p: (mono_area[p] if p in MONO else (rum_feed_area + pasture) * need[p] / rum_need) for p in FCR}
    # land per tonne eaten (ha per 1000 t of the FBS 'Food' element => ha per tonne x 1000)
    lpt = {}
    for item in AREA:
        if item in ('Sugar cane', 'Sugar beet') or area_use[item]['food'] == 0: pass
        lpt[item] = area_use[item]['food'] / wf(item, 'Food') if wf(item, 'Food') else 0.0
    for p in prod_area:
        u = uses(p); tot = sum(u.values()) - wf(p, 'Stock Variation')
        lpt[p] = prod_area[p] / tot if tot else 0.0
    for p in FCR:
        u = uses(p); tot = sum(u.values()) - wf(p, 'Stock Variation')
        if p == 'Eggs': tot = wf(p, 'Food') + wf(p, 'Feed') + wf(p, 'Other uses (non-food)')
        lpt[p] = animal_area[p] / tot if tot else 0.0
    # butter: milk processed
    u = uses('Milk - Excluding Butter'); milk_proc_area = animal_area['Milk - Excluding Butter'] * u['proc'] / (sum(u.values()) - wf('Milk - Excluding Butter', 'Stock Variation'))
    lpt['Butter, Ghee'] = milk_proc_area / wf('Butter, Ghee', 'Food') if wf('Butter, Ghee', 'Food') else 0.0
    lpt['Milk - Excluding Butter'] = (animal_area['Milk - Excluding Butter'] - milk_proc_area) / wf('Milk - Excluding Butter', 'Food') if wf('Milk - Excluding Butter', 'Food') else 0.0
    # (the FBS 'Food' of milk is the whole-milk equivalent of dairy eaten; the processed share feeds butter, counted separately)
    pop = wf('Population', 'Total Population - Both sexes') if False else yv(F.get(('World', 'Population', 'Total Population - Both sexes'), {}), yrs)
    land = yv(L[('World', 'Land area')], yrs) * 1000
    return dict(lpt=lpt, adj=adj, harvested=harvested, cropland=cropland, feed_area=feed_area, feed_dm=feed_dm, pasture=pasture, pop=pop * 1000, land=land, animal_area=animal_area, area_use=area_use)
def half(w, country, yrs):
    pop = yv(F.get((country, 'Population', 'Total Population - Both sexes'), {}), yrs)
    tot = 0.0; parts = collections.defaultdict(float)
    for item, lp in w['lpt'].items():
        food = yv(F.get((country, item, 'Food'), {}), yrs)               # 1000 t
        ha_pc = food / pop * lp / 1000                                  # t per person x (ha per 1000 t / 1000) = ha per person
        tot += ha_pc
        grp = 'animal' if item in FCR or item == 'Butter, Ghee' else 'crop'
        parts[grp] += ha_pc
    return tot, parts, pop
out = [['period', 'country', 'ha a person', 'animal products', 'crops', 'HALF % of world land']]
res = {}
for label, yrs in (('2011', ('2011',)), ('2021-23', ('2021', '2022', '2023'))):
    w = world(yrs)
    # world average diet = world totals
    world_ha, wparts, wpop = half(w, 'World', yrs)
    res[label] = w
    out.append([label, 'World', round(world_ha, 3), round(wparts['animal'], 3), round(wparts['crop'], 3), round(world_ha * w['pop'] / w['land'] * 100, 1)])
    for c in ['Australia', 'United States of America', 'India', 'New Zealand', 'Argentina', 'China', 'Brazil']:
        ha, parts, p = half(w, c, yrs)
        out.append([label, c, round(ha, 3), round(parts['animal'], 3), round(parts['crop'], 3), round(ha * w['pop'] / w['land'] * 100, 1)])
    print(label, 'adjustment (cropland/harvested):', round(w['adj'], 3), ' harvested Mha:', round(w['harvested'] / 1e6), ' cropland Mha:', round(w['cropland'] / 1e6), ' feed cropland Mha:', round(w['feed_area'] / 1e6),
          ' feed DM Mt:', round(w['feed_dm'] / 1e3), ' pasture Mha:', round(w['pasture'] / 1e6), ' world land Mha:', round(w['land'] / 1e6))
csv.writer(open('analysis/method_tests_2025/half_index.csv', 'w', newline='')).writerows(out)
for r in out: print(r)
print('Alexander 2016, 2011: world 35.13 (0.65 ha a person), Australia 112.20, United States 97.73, India 15.76, New Zealand 135.76, Argentina 114.88; total food area 4,484 Mha: food cropland 871, feed cropland 497, pasture 3,203')
