# The 2011 baseline

The complete output of the original 2011 Carrying Capacity Dashboard servlet for every
default case: 60 zones, short-term and long-term presets, 120 cases in all. This is the
"old version" that every later comparison measures against (SCOPE.md objective 2).

| File | Contents |
|---|---|
| `baseline_2011.json` | Per case: the form values posted, and the servlet's full response (carrying capacity, excess land, land requirements). A `meta` block holds SHA-256 fingerprints of the workbook, servlet class and both default files |
| `baseline_2011.csv` | One line per case: capacity, current population, current as a percentage of capacity, excess land, food land, land required |
| `run_baseline.py` | The script that produced both, so the baseline can be regenerated |

## How it was produced

- Source: the QUT snapshot, commit `04a612e` of this repository, `source/webapps/ccd`.
- Run: the unmodified compiled servlet and the 2011 Apache POI jars, in Apache Tomcat 9.0.123 on OpenJDK 21, on 2026-10-26.
- Inputs: each zone's defaults posted exactly as the 2011 page posts them. The page multiplies percentage parameters by 100 and rounds any value that is not a whole number to one decimal; areas and population carry thousands separators. The script reproduces that.
- The servlet rounds its output to two decimal places.

The Java servlet and Tomcat page are no longer on `main`. They are kept on the `legacy-java` branch (and, as the unmodified QUT snapshot, in history at `04a612e`).

To regenerate:

```bash
git archive 04a612e source/webapps/ccd | tar -x -C /tmp/orig --strip-components=2   # gives /tmp/orig/ccd
# copy /tmp/orig/ccd to TOMCAT/webapps/ROOT, start Tomcat 9, then
python3 -I baseline/run_baseline.py /tmp/orig/ccd http://localhost:8080 baseline
```

## What it is not

It is the model as shipped, not the model as printed in the thesis. The workbook log
records edits after the thesis tables were produced, so some thesis figures differ from
this baseline: individual zones by up to 3.3 percent, and the long-term national total
of regional capacities by 5.6 percent. Papers and reports must say which of the two they
compare against. The short-term national figures agree with the 2015 paper to 0.03 percent.

## Checks

An independent JavaScript evaluation of the same workbook agrees with these results in
all 120 cases to within the servlet's output rounding.
