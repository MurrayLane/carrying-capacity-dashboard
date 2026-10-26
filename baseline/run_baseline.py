#!/usr/bin/env python3
"""Record the 2011 baseline: every default case through the ORIGINAL Java servlet.

Usage:  python3 -I run_baseline.py WEBAPP_DIR BASE_URL OUT_DIR

WEBAPP_DIR  the original webapp (source/webapps/ccd from commit 04a612e), used for its
            default-inputs CSV files and for the file fingerprints
BASE_URL    where that webapp is running, for example http://localhost:8080
OUT_DIR     receives baseline_2011.json and baseline_2011.csv

Each case posts the same form fields the 2011 page posts. The page copies a region's
defaults into its inputs before posting, so this script copies them the same way:
percent parameters are multiplied by 100 and a value that is not a whole number is
rounded to one decimal place (updateInputValues in dashboard.js); areas and population
are written with thousands separators.
"""
import csv, hashlib, json, os, sys, urllib.parse, urllib.request

webapp, base, out = sys.argv[1:4]

# (csv column, form field, displayRatio) in the order the page lists its sliders
SLIDERS = [
    ("resilience", "inputResilienceYears", 1), ("food", "inputFoodRatio", 100),
    ("meategg", "inputMeateggRatio", 100), ("redmeat", "inputRedmeatRatio", 100),
    ("activity", "inputActivityLevel", 1), ("losses", "inputLossesRatio", 100),
    ("recycling", "inputRecyclingRatio", 100), ("organic", "inputOrganicRatio", 100),
    ("irrigation", "inputIrrigationRatio", 100), ("fuel", "inputFuelTotal", 1),
    ("biofuel", "inputBiofuelRatio", 100), ("fibre", "inputFibreTotal", 1),
    ("fibreNat", "inputFibreNaturalRatio", 100), ("fibreWool", "inputFibreWoolRatio", 100),
    ("timber", "inputTimber", 1), ("infrastr2", "inputInfrastructure", 1),
    ("nature2", "inputNatureRatio", 100),
]
AREAS = [("cropping", "inputAreasCropping"), ("pasture", "inputAreasPasture"),
         ("nonAg", "inputAreasNonAg"), ("infrastr1", "inputAreasBuilt"),
         ("nature1", "inputAreasNature")]

def js_slider(x, ratio):
    v = float(x) * ratio
    return f"{v:.1f}" if v % 1 != 0 else str(int(v))

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

cases = {}
for preset, fn in (("short", "default-inputs-short-term.csv"), ("long", "default-inputs-long-term.csv")):
    for row in csv.DictReader(open(os.path.join(webapp, fn), newline="")):
        p = {"inputRegionId": row["regionId"],
             "inputPopulation": f"{int(row['population']):,}"}
        total = 0
        for col, field in AREAS:
            p[field] = f"{int(row[col]):,}"
            total += int(row[col])
        p["inputAreasTotal"] = f"{total:,}"
        for col, field, ratio in SLIDERS:
            p[field] = js_slider(row[col], ratio)
        body = urllib.parse.urlencode(p).encode()
        with urllib.request.urlopen(base.rstrip("/") + "/ProcessExcel", body, timeout=120) as r:
            res = json.loads(r.read().decode())
        cases[f"{preset}:{row['regionId']}:{row['regionName']}"] = {
            "preset": preset, "regionId": int(row["regionId"]), "regionName": row["regionName"],
            "currentPopulation": int(row["population"]), "params": p, "result": res}

meta = {
    "description": "Complete output of the 2011 Carrying Capacity Dashboard servlet for every default case "
                   "(60 zones x short-term and long-term presets)",
    "source": "QUT snapshot, commit 04a612e of this repository, source/webapps/ccd",
    "files": {name: sha(os.path.join(webapp, name)) for name in
              ("WEB-INF/model.xls", "WEB-INF/classes/au/edu/qut/isr/ProcessExcel.class",
               "default-inputs-short-term.csv", "default-inputs-long-term.csv")},
    "case_count": len(cases),
    "result_fields": {"popcc": "carrying capacity population",
                      "excess": "six rows: excess cropping, pasture, non-agricultural, infrastructure, "
                                "nature reserve, total; each [km2, % of land]",
                      "requirements": "17 rows: red meat, white meat, dairy, cereals, vegetables, fruit, legumes, "
                                      "nuts and seeds, oils, sweeteners, food total, biofuel, textiles, timber, "
                                      "infrastructure, nature reserve, total; each [m2 per person, km2, % of land, % of food land]"},
}
os.makedirs(out, exist_ok=True)
json.dump({"meta": meta, "cases": cases}, open(os.path.join(out, "baseline_2011.json"), "w"), indent=1, sort_keys=True)
with open(os.path.join(out, "baseline_2011.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["preset", "region_id", "region", "current_population", "carrying_capacity",
                "current_as_pct_of_capacity", "excess_land_km2", "excess_land_pct", "food_land_km2", "land_required_km2"])
    for k in sorted(cases, key=lambda k: (cases[k]["preset"], cases[k]["regionId"])):
        c = cases[k]; r = c["result"]
        cap = r["popcc"]; pop = c["currentPopulation"]
        w.writerow([c["preset"], c["regionId"], c["regionName"], pop, cap,
                    round(pop / cap * 100, 1) if cap else "", r["excess"][5][0], r["excess"][5][1],
                    r["requirements"][10][1], r["requirements"][16][1]])
print(f"wrote {len(cases)} cases to {out}")
