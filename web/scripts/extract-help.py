#!/usr/bin/env python3
"""One-off: extract the 2011 page's help text from dashboard.jsp into web/src/data/help.json.

The JSP is retired from main; it remains in git history at commit 04a612e (source/webapps/ccd/dashboard.jsp):
    git show 04a612e:source/webapps/ccd/dashboard.jsp > /tmp/dashboard.jsp
    python3 -I web/scripts/extract-help.py /tmp/dashboard.jsp web/src/data/help.json
The text is carried over verbatim, so it describes the 2011 data and defaults.
"""
import json, re, sys
src = open(sys.argv[1], encoding='utf-8').read()
def clean(html):
    return re.sub(r'\s+', ' ', html).strip()
def next_help(pos):
    m = re.compile(r'<div class="help-info"[^>]*>(.*?)</div>', re.S).search(src, pos)
    return m
out = {'params': {}, 'groups': {}, 'areas': {}, 'sections': {}}
# slider panels: <div id="pFoodRatio" class="ui-slider-panel"></div> followed by its help block
for m in re.finditer(r'<div id="(p[A-Za-z]+)" class="ui-slider-panel"></div>', src):
    h = next_help(m.end())
    if h and h.start() - m.end() < 60: out['params'][m.group(1)] = clean(h.group(1))
# groups: heading then its first help block
for m in re.finditer(r'<div id="(pg[A-Za-z]+)" class="param-group left">\s*<div class="heading">(.*?)<a', src, re.S):
    h = next_help(m.end())
    out['groups'][m.group(1)] = {'title': clean(m.group(2)), 'html': clean(h.group(1)) if h else ''}
# land-area inputs: <label><span>CROPPING</span>...  then <div class="help-info" title="CROPPING">
for m in re.finditer(r'<label[^>]*><span>([A-Z\- ]+)</span><input[^>]*name="(input[A-Za-z]+)"[^>]*>(?:(?!<label).)*?</label>\s*<div class="help-info"[^>]*>(.*?)</div>', src, re.S):
    out['areas'][m.group(2)] = {'title': m.group(1).title(), 'html': clean(m.group(3))}
# the section help blocks
for key, pat in {'landAreas': r'LAND AREAS<a[^>]*></a></h2>\s*<div class="help-info">(.*?)</div>',
                 'projections': r'PROJECTIONS<a[^>]*></a></h2>\s*<div class="help-info">(.*?)</div>',
                 'landUsage': r'LAND REQUIREMENTS: BY USAGE<a[^>]*></a></h2>\s*<div class="help-info">(.*?)</div>',
                 'foodUsage': r'LAND REQUIREMENTS: BY USAGE FOR FOOD<a[^>]*></a></h2>\s*<div class="help-info">(.*?)</div>',
                 'capacity': r'POPULATION <span id="outputCapacityText">ON</span> CAPACITY<a[^>]*></a></h2>\s*<div class="help-info"[^>]*>(.*?)</div>'}.items():
    m = re.search(pat, src, re.S)
    if m: out['sections'][key] = clean(m.group(1))
json.dump(out, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False)
print({k: len(v) for k, v in out.items()}, list(out['params'])[:3], list(out['areas']))
