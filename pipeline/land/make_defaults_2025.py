#!/usr/bin/env python3
"""The default-input files of the 2025 data layers: the 2011 files with first the land and then the population of data/nrm2011/land_2011_method_zones.csv.

Usage: python3 -I make_defaults_2025.py          (run from the repository root)
Writes data/2025-land/ and data/2025-population/ (short-term and long-term default files, same columns as data/2011).

Land layer         cropping, pasture, reserve (nature1) and total area replaced; infrastructure and population stay at 2011; non-agricultural is the remainder
                   (a negative remainder is shown as zero and counted); the reserve share nature2 follows the 2011 rule (short-term: the existing share to two decimals;
                   long-term: the larger of 30% and the short-term figure, which holds in all 60 zones of the 2011 files).
Population layer   population replaced (2025 estimated resident population, given to the zones in proportion to residential land); infrastructure is population x 730 m2
                   as in 2011; non-agricultural is the remainder again.
Every other default (diet, fuel, fibre, timber, irrigation, recycling and so on) is the 2011 value (Murray, 2026-10-27: if in doubt, default to 2011).
"""
import csv, os
ROOT = os.getcwd()
rd = lambda p: list(csv.DictReader(open(os.path.join(ROOT, p))))
zones = {int(r['zone']): r for r in rd('data/nrm2011/land_2011_method_zones.csv')}
short, long_ = rd('data/2011/default-inputs-short-term.csv'), rd('data/2011/default-inputs-long-term.csv')
fields = list(short[0].keys())


def build(layer, with_population):
    negatives = 0; out = {'short': [], 'long': []}
    for kind, rows in (('short', short), ('long', long_)):
        for r in rows:
            z = zones[int(r['regionId'])]; r = dict(r)
            total, reserve = round(float(z['total'])), round(float(z['reserve']))
            crop, past = round(float(z['cropping'])), round(float(z['pasture']))
            pop = round(float(z['population'])) if with_population else int(float(r['population']))
            infra = round(pop * 730 / 1e6) if with_population else round(float(r['infrastr1']))
            non = total - crop - past - infra - reserve
            if non < 0 and kind == 'short': negatives += 1
            share = round(reserve / total, 2)
            r.update(cropping=crop, pasture=past, nonAg=max(0, non), infrastr1=infra, nature1=reserve, totalArea=total, population=pop,
                     nature2=share if kind == 'short' else max(0.30, share))
            out[kind].append(r)
    d = os.path.join(ROOT, 'data', layer); os.makedirs(d, exist_ok=True)
    for kind, name in (('short', 'default-inputs-short-term.csv'), ('long', 'default-inputs-long-term.csv')):
        with open(os.path.join(d, name), 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(out[kind])
    print(f'{layer}: 60 zones, {negatives} with a negative remainder shown as zero')


build('2025-land', False)
build('2025-population', True)
