"""Stage 1 for animal products (thesis section 8.1 step 10): the land that grazing and hay supports is shared among the animals
of a region by dry sheep equivalent (DSE); each product's yield is its production divided by its share of that land.
Poultry, pigs and fish are not land based: their yield is the mean grain and oilseed yield divided by a feed conversion ratio.

Inputs per year (the numbers that need sourcing):
  regions[zone]  grazingHa, hayHa, headcounts by class (after the harmonising step), sheepFeedlot, cattleFeedlot, milkTonnes     zone 1 is Australia
  national       sheepFeedlotGrainT, sheepMeatT, woolT, cattleFeedlotGrainT, cattleMeatT
Parameters (DSE factors, feed conversion ratios, feedlot land): archive_livestock_parameters.json.
Returns {product: [value for zone 1..60]}; 0 where the workbook returns 0, None where it has no result.
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(HERE, 'archive_livestock_parameters.json')))['parameters']
PRODUCTS = ['Sheep meat', 'Sheep wool', 'Dairy milk', 'Cattle meat', 'Chicken meat', 'Duck meat', 'Turkey meat', 'Chicken eggs', 'Pig meat', 'Fish total', 'Seafood total']
GRAIN_SHEEP = ['Wheat', 'Oats', 'Barley', 'Sorghum', 'Maize']                       # AVERAGE(wheat, oats, barley, sorghum, maize) in the workbook
GRAIN_CATTLE = ['Wheat', 'Barley', 'Sorghum', 'Maize']
GRAIN_FEED = ['Wheat', 'Oats', 'Barley', 'Sorghum', 'Maize', 'Canola', 'Soybeans']


def mean(xs):
    xs = [x for x in xs if x]
    return sum(xs) / len(xs) if xs else None


def livestock_year(inputs, crops):
    """crops: {'Wheat': [t/ha for column 0..60], ...} from stage 1."""
    reg, nat = inputs['regions'], inputs['national']; g = lambda z, k: reg[str(z)].get(k) or 0.0
    out = {p: [None] * 61 for p in PRODUCTS}
    parts = {}
    for z in range(1, 61):
        L, E, notInLamb, rams, feedS = (g(z, k) for k in ('sheepLambs', 'sheepEwesToLamb', 'sheepEwesNotInLamb', 'sheepRams', 'sheepFeedlot'))
        dseS = P['dseLambs'] * L + P['dseEwesToLamb'] * E + P['dseEwesNotInLamb'] * notInLamb + P['dseRams'] * rams
        cows, calves, h12, h2, dbulls = (g(z, k) for k in ('dairyCows', 'dairyHeiferCalves', 'dairyHeifers1to2', 'dairyHeifersOver2', 'dairyBulls'))
        dseD = P['dseDairyCows'] * cows + P['dseDairyHeiferCalves'] * calves + P['dseDairyHeifers1to2'] * h12 + P['dseDairyHeifersOver2'] * h2 + P['dseDairyBulls'] * dbulls
        bb, bc, bcalf, balance, feedC = (g(z, k) for k in ('beefBulls', 'beefCows', 'beefCalves', 'beefBalance', 'cattleFeedlot'))
        dseB = P['dseBeefBulls'] * bb + P['dseBeefCows'] * bc + P['dseBeefCalves'] * bcalf + P['dseBeefBalance'] * balance
        dseA = sum(P[n] * g(z, k) for n, k in (('dseBuffaloes', 'buffaloes'), ('dseDeer', 'deer'), ('dseGoats', 'goats'), ('dseHorsesStud', 'horsesStud'), ('dseHorsesOther', 'horsesOther'), ('dseOtherLivestock', 'otherLivestock')))
        parts[z] = dict(feedS=feedS, dseS=dseS, dseD=dseD, dseB=dseB, dseTotal=dseS + dseD + dseB + dseA, land=g(z, 'grazingHa') + g(z, 'hayHa'), feedC=feedC)
    for z in range(1, 61):
        a, A = parts[z], parts[1]; share = lambda d: (a[d] / a['dseTotal'] if a['dseTotal'] else 0.0)
        cr = lambda names: mean([crops[n][z] for n in names])
        # sheep: meat and wool
        gS = cr(GRAIN_SHEEP)
        grainS = nat['sheepFeedlotGrainT'] if z == 1 else (a['feedS'] / A['feedS'] if A['feedS'] else 0.0) * nat['sheepFeedlotGrainT']
        haGrainS = grainS / gS if gS else None
        haFeedS = a['feedS'] * P['sheepFeedlotHaPerHead']
        haMeatS = None if haGrainS is None else a['land'] * share('dseS') + haGrainS + haFeedS
        shareS = None if z == 1 else (a['dseS'] / A['dseS'] if A['dseS'] else 0.0)
        meatT = nat['sheepMeatT'] if z == 1 else shareS * nat['sheepMeatT']; woolT = nat['woolT'] if z == 1 else shareS * nat['woolT']
        if haMeatS is not None:
            out['Sheep meat'][z] = 0.0 if haMeatS < 1000 else meatT / haMeatS
            haWool = haMeatS - haGrainS - haFeedS
            out['Sheep wool'][z] = 0.0 if woolT < 100 else (woolT / haWool if haWool else None)
        # dairy
        haD = a['land'] * share('dseD'); milk = g(z, 'milkTonnes')
        out['Dairy milk'][z] = 0.0 if haD < 100 else milk / haD
        # cattle meat
        gC = cr(GRAIN_CATTLE)
        grainC = nat['cattleFeedlotGrainT'] if z == 1 else (a['feedC'] / g(1, 'cattleFeedlot') if g(1, 'cattleFeedlot') else 0.0) * nat['cattleFeedlotGrainT']
        shareC = None if z == 1 else (a['dseB'] / A['dseB'] if A['dseB'] else 0.0)
        cmeat = nat['cattleMeatT'] if z == 1 else shareC * nat['cattleMeatT']
        if gC:
            haC = a['land'] * share('dseB') + grainC / gC + a['feedC'] * P['cattleFeedlotHaPerHead']
            out['Cattle meat'][z] = 0.0 if haC < 100 else cmeat / haC
        # not land based
        gf = cr(GRAIN_FEED)
        if gf:
            for prod, k in (('Chicken meat', 'fcrChickenMeat'), ('Duck meat', 'fcrDuckMeat'), ('Turkey meat', 'fcrTurkeyMeat'), ('Chicken eggs', 'fcrChickenEggs'), ('Pig meat', 'fcrPigMeat')):
                out[prod][z] = gf / P[k]
            out['Fish total'][z] = 1 / (1 / (gf / P['fcrFish']) + 1 / P['fishAreaYield'])
            out['Seafood total'][z] = 1 / (1 / (gf / P['fcrSeafood']) + 1 / P['seafoodAreaYield'])
    return out
