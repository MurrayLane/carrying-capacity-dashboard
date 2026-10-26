#!/usr/bin/env python3
"""Download the ABS Agricultural Commodities cubes with NRM-region estimates for 2015-16 to 2020-21.

Usage: python3 -I fetch_abs_current.py OUT_DIR

The ABS changed its file naming and format three times in these years, so the cubes are found by what they say about themselves:
  2015-16, 2016-17   archived 7121.0 pages: the "NRM regions ... (.csv file)" cube
  2017-18 to 2019-20 the .csv cubes on the release page whose title line says "NRM regions" and "AGRICULTURAL COMMODITIES"
  2020-21            AGCDCNRM202021.xlsx (the last year the ABS published NRM tables; later releases are national and state only)
Also fetches the commodity item listings, which map commodity codes between years.
"""
import html, os, re, sys, urllib.parse, urllib.request
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36"}
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
get = lambda url: urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read()
ABS = "https://www.abs.gov.au"
BASE = ABS + "/statistics/industry/agriculture/agricultural-commodities-australia"

def save(name, data):
    p = os.path.join(out, name)
    if not os.path.exists(p): open(p, "wb").write(data); print(f"{name}: {len(data):,} bytes")

# archived pages (2015-16, 2016-17): link chosen by title
for y, pat in (("2016-17", r"NRM region.*\.csv"), ("2015-16", r"NRM regions \(\.csv file\)")):
    s = re.sub(r"<script.*?</script>|<style.*?</style>", "", get(f"{ABS}/AUSSTATS/abs@.nsf/DetailsPage/7121.0{y}?OpenDocument").decode("utf-8", "ignore"), flags=re.S)
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", s, flags=re.S):
        links = [html.unescape(h) for h in re.findall(r'href="([^"]*openagent[^"]*)"', tr, flags=re.I)]
        title = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", tr))).strip()
        if links and title.startswith("Agricultural") and re.search(pat, title) and "Organic" not in title:
            save(f"{y}_NRM.csv", get(ABS + urllib.parse.quote(links[0], safe="/?&=:.%"))); break

# release pages (2017-18 to 2019-20): every .csv, kept when its first lines say NRM regions
for y in ("2017-18", "2018-19", "2019-20"):
    s = get(f"{BASE}/{y}").decode("utf-8", "ignore")
    for l in sorted(set(re.findall(r'href="([^"]+\.csv)"', s))):
        data = get(ABS + l); head = data[:600].decode("latin1")
        if "NRM" in head and "AGRICULTURAL COMMODITIES" in head.upper() and "LAND MANAGEMENT" not in head.upper() and "FARM MANAGEMENT" not in head.upper():
            save(f"{y}_NRM.csv", data); break

save("2020-21_NRM.xlsx", get(f"{BASE}/2020-21/AGCDCNRM202021.xlsx"))
for y, f in (("2015-16_to_2020-21", "2020-21/Agricultural%20Commodity%20data%20item%20listing%202015-16%20to%202020-21.xlsx"), ("2021-22", "2021-22/2021-22%20Agricultural%20Commodities%20data%20item%20listing.xlsx")):
    save(f"item_listing_{y}.xlsx", get(f"{BASE}/{f}"))
