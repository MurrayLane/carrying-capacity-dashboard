# Errata register: errors found in the thesis model and the publications

A record of the errors found while rebuilding the model, for Murray to send to publishers in time. **Nothing has been sent and no wording has been drafted or agreed**; this file holds the facts, the evidence and the size of each error so that a note can be written from one place. Whether to issue a note for the thesis and for each paper is Murray's call.

Rule (as for `DISCUSSION.md`): the moment an error is found, add a row here with its evidence and size. Figures are from `results/` (release ids in brackets) and can be regenerated with `cd web && npm run results`.

An **error** is a disagreement between the workbook and the source it cites, or between two parts of the published record. A change of method that is a judgement (US loss factors, recycling, reserve land) is **not** an error and is listed at the end only so that it is not mistaken for one.

## Errors

| # | Error | Where it sits | Evidence | Size (Australia unless stated) | Publications affected | Confidence | Status |
|---|---|---|---|---|---|---|---|
| 1 | **Biodiesel yield counts the oil content twice.** The workbook multiplies a yield that is already per tonne of oilseed by the oil content again (canola 14.8% where 35.2% is the source's yield) | Workbook `Base!K336:K344`; thesis section on liquid fuel and biofuel; every capacity result that uses biofuel land | ABARE, *Australian Energy Resource Assessment* (2009), Table 12.12: 400 litres a tonne is per tonne of oilseeds. `analysis/liquid_fuel_2025/README.md` | Long term: 9.43 to 15.75 million alone (15.35 with error 2 corrected); short term +0.1 million. Method module `biodiesel-yield` | Thesis (long-term results and Table 16); Lane 2017 *Population and Environment* 38(3) Table 2 (long-term 9,431,487 and the regional long-term figures); Lane, Dawes and Grace 2014 and 2015 where they quote long-term results (to check line by line) | Confirmed from the thesis's own source | To send |
| 2 | **Beef carcase-to-retail yield is 1.0.** Beef (dressed) has no loss between carcase and retail cut, while lamb, veal and pork have 0.894, 0.83 and 0.776. Earlier workbook versions had 0.705 and a note reverting it "because the ABS figures are carcase weight", which is the reason the factor is needed | Workbook `Base!K175` | The author's note in `Base model (12).xls` (models archive); USDA ERS carcase-to-retail factor 0.705; AUS-MEAT 68.7% meat yield; ABS 7215.0 gives its own carcase-to-boneless factor of 1.5 (0.667). `analysis/constants_audit/README.md` | Short term: 40.45 to 33.31 million (-17.6%, with error 1). Regions sum 22.98 to 20.97 million, states sum 28.28 to 25.68. Long term unchanged (no meat in the long-term diet to speak of: 7.5%) | Thesis; Lane and Dawes 2013 (UES, "just over forty million"); Lane, Dawes and Grace 2014 (40,450,144) and 2015 (Table 2 and the scale argument: national 40 million against about 23 million summed over regions); Lane 2017 (short-term columns) | About 93% (yield between 0.667 and 0.705; the range gives 33.3 to 34.4 million) | To send. Murray kept the correction 2026-10-28 |
| 3 | **Thesis Table 16 and the 2015 and 2017 tables were produced with earlier settings than the thesis text states.** `Totals.xls` has timber 0.5 m3 (Table 7 and the site: 1), short-term biofuel 0.53% (0.5%) and long-term infrastructure 365 m2 (500) | Thesis Table 16; 2015 Table 2; 2017 Table 2 against its own Table 1 | `analysis/model_archive/PAPERS.md`, `VERSIONS.md`; release `2011-thesis` reproduces them | National and state figures move at most 3.3%; regional long-term figures up to 29% (timber yield per region and `Base!K348`: North Central Vic, Border Rivers-Gwydir, Murray, Wimmera, Northern and Yorke). The 2017 "13 regions" is 14 under the final method (Wimmera sits on its capacity) | Thesis Table 16; Lane, Dawes and Grace 2015; Lane 2017 (Table 1 against Table 2; Figure 3 map; "13 regions"; "23 million") | Certain | To send, if Murray wishes (small) |
| 4 | **The online dashboard's long-term textiles default is 12.5 kg;** the thesis (Table 7), the appendix and the workbook have 11.5 | Dashboard default file | `analysis/model_archive/` | Under 0.1% nationally; up to 3.7% in one region (Alinytjara Wilurara) | The site only; no paper quotes it | Certain | Corrected in release `2011-corrected` |
| 5 | **Stale numbers in the dashboard's help text** (fuel 2,600 L, biofuel 1%, timber 0.5 m3) against the defaults the thesis gives (2,520 L, 0.5%, 1 m3) | Site help text | `SCOPE.md` B8 | Text only | The site only | Certain | Corrected in the rebuild |

## Corrected headline figures (the corrected method, releases `2011-fixed` and `2025-fixed`)

| | As published (`2011-corrected`) | Corrected (`2011-fixed`) |
|---|---|---|
| Australia, short term | 40.45 million | 33.31 million |
| Australia, long term | 9.43 million | 15.35 million |
| 52 regions summed, short term | 22.98 million | 20.97 million |
| 52 regions summed, long term | 4.05 million | 5.11 million |
| Regions with a population above capacity, short / long term | 21 / 38 | 22 / 35 (so 17, not 14, regions under capacity in the long term) |

The scale ratio of the 2015 paper (national capacity about 40 million against about 23 million summed over regions, a ratio of 1.76) becomes 33.3 against 21.0, a ratio of 1.59: the direction of the finding holds and the size is smaller. The short-term rise from 2011 to 2025 holds on the corrected method (33.3 to 39.5 million, outside the 90% range of the 2025 figure's uncertainty); the long-term rise (15.35 to 15.9) is not distinguishable from the uncertainty (`analysis/sensitivity_2025/README.md`).

## To check line by line before anything is sent

* Which long-term results each paper quotes (2014 and 2015 papers: the table above says "to check"). The text of the papers is extracted from the published full texts in `analysis/model_archive/` (`paper_claims.mjs`).
* The regional figures affected by error 2 (all 52 regions, short term) and by error 1 (all regions, long term): `results/2011-fixed.csv` has them.
* Whether the wording of the thesis text itself (not only the tables) states the biodiesel yield or the beef yield; section numbers have been given wrongly before, so look them up before citing.

## Changes that are not errors (listed so they are not mistaken for corrections)

Judgement-based method changes in the improved tier (`methods/README.md`): reserve land shortfall shared pro rata; recycling split by stage, origin, dry matter and the law in force (the thesis credits wet grams of waste against dry-feed ratios and at 100% recycling feeds the whole pig, poultry, egg and fish industry on waste: a feasibility finding rather than a computational error); US retail and consumer loss factors aligned to the Australian measurement. Limits of the model that cannot be modelled are in `DISCUSSION.md`.
