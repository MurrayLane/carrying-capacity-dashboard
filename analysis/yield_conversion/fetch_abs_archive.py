#!/usr/bin/env python3
"""Download the archived ABS cubes with NRM-level crop data for 2006-07 to 2009-10.

Usage: python3 -I fetch_abs_archive.py OUT_DIR

The ABS archive pages list each cube under a title but reuse file names across cubes, so
the link is chosen by title. 2005-06 is not available: the 2005-06 small area release
(7125.0) is not in the archive, and the 7121.0 2005-06 cubes are state-level only.
"""
import html, os, re, sys, urllib.parse, urllib.request
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36"}
PAGES = {"7121.02009-10": [("2009-10_NRM_all", r"NRM region")],
         "7121.02008-09": [("2008-09_NRM_all", r"NRM region")],
         "7121.02007-08": [("2007-08_NRM_all", r"State and NRM region")],
         "7125.02006-07": [(f"2006-07_{s}", rf"^{s.replace('_', ' ')} NRM All commodities") for s in
                           ("NSW", "VIC", "QLD", "SA", "WA", "TAS", "NT and ACT")]}
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read()
for page, wanted in PAGES.items():
    s = get(f"https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/{page}?OpenDocument").decode("utf-8", "ignore")
    s = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", s, flags=re.S):
        links = [html.unescape(h) for h in re.findall(r'href="([^"]*openagent&[^"]*\.xls[^"]*)"', tr, flags=re.I)]
        if not links: continue
        title = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", tr))).strip()
        title = title.split(" Released")[0]
        for name, pat in wanted:
            # 2006-07 has two releases per state; the original (06/06/2008) is the one without VACP in its title
            if re.search(pat, title) and "VACP" not in title:
                dest = os.path.join(out, name + ".xls")
                if os.path.exists(dest): continue
                url = "https://www.abs.gov.au" + urllib.parse.quote(links[0], safe="/?&=:.%")
                data = get(url); open(dest, "wb").write(data); print(f"{name}: {len(data):,} bytes")
