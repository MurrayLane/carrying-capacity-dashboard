"""The yield method of the thesis (section 8.1), as code.

Stage 1  per-year t/ha for each commodity and region from a raw cube          crops_year()
Stage 2  five-year average with the deletion rules                            (average.py)
Stage 3  national-times-factor fill and the zero-irrigation conversion        (fill.py)

A cube is a dict {label: [value per column]} where column 0 is the label's own column and columns 1..60 are the zones in
the order of releases/<id>/regions (Australia first). Values are floats; missing is None.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
METHOD = json.load(open(os.path.join(HERE, 'method.json')))
norm = lambda s: re.sub(r'[^a-z0-9]', '', str(s).lower())
ADJ = {norm(k): v for k, v in METHOD['adjustments'].items()}
AREA_LABEL = {'cottonlint': 'Cotton'}          # the cube's area row for cotton lint is labelled Cotton (ha)


def read_cube(sheet):
    """An xlrd sheet laid out like the archive's raw cubes (label, then one column per zone)."""
    cube = {}
    for r in range(1, sheet.nrows):
        lab = str(sheet.cell_value(r, 0)).strip()
        if lab: cube[norm(lab)] = [v if isinstance(v, float) else None for v in sheet.row_values(r)]
    return cube


def crop_year(cube, base, deleted=(), thresholds=False):
    """t/ha per column for one crop, or None where the cube has no usable figure.
    `deleted` is a set of (normalised label, column) removed as unreliable. For the archive these are recorded; for new cubes they
    come from the ABS reliability flags. `thresholds` additionally applies the 10 ha / 10 t minimum of the thesis text.
    Then: trees become hectares at the recorded density, vegetables' area is scaled up, seed is deducted."""
    area = AREA_LABEL.get(norm(base), base)
    t = cube.get(norm(base + ' (t)'))
    ha = cube.get(norm(area + ' (ha)')); trees = cube.get(norm(area + ' trees (n)'))
    if t is None or (ha is None and trees is None): return None
    area_adj = ADJ.get(norm(area + ' (ha)'), {}); seed = ADJ.get(norm(base + ' (t)'), {}).get('seed', 0.0)
    dens = ADJ.get(norm(area + ' trees (n)'), {}).get('treesPerHa')
    inc = area_adj.get('areaIncrease', 0.0) or 0.0
    out = []
    for c in range(len(t)):
        tt = t[c]
        if trees is not None and dens: n = trees[c]; hh = n / dens if n else None
        else: hh = ha[c] if ha else None
        if c == 0 or tt is None or hh is None or tt <= 0 or hh <= 0: out.append(None); continue
        if thresholds and (hh < METHOD['minHa'] or tt < METHOD['minTonnes']): out.append(None); continue
        if (norm(base + ' (ha)'), c) in deleted or (norm(base + ' trees (n)'), c) in deleted or (norm(base + ' (t)'), c) in deleted: out.append(None); continue
        y = tt / (hh * (1 + inc)) - seed
        if norm(base) == 'mushrooms': y = tt / hh / METHOD['mushroomHayDivisor']
        out.append(y)
    return out
