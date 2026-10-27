# Which model version each publication used

Found by testing each paper's numbers against each release (`paper_claims.mjs`, text extracted from the published full texts on
eprints.qut.edu.au). The releases are described in `releases/README.md`: `2011` is the model that went online and the one the
thesis text and its Tables 7 and 14 describe; `2011-thesis` is the earlier June 2012 model behind thesis Table 16 and `Results/Totals.xls`.

| Publication | Model results it reports | Version | Evidence |
|---|---|---|---|
| Lane (2009, ISSS) and Lane (2010) *Land Use Policy* 27(4) | none (review of methods) | n/a | No model figures |
| Lane (2011) *Resilience in Urban Design* (IUDC) | none ("say, 25 million" is hypothetical) | n/a | No model figures |
| Lane and Dawes (2013) *Urban Environment* (UES), Springer | Australia "just over forty million" short-term, 15% meat-eggs "just over 39 million", vegan "80 million", regions sum "about 23 million", long-term "less than four million" regional and "more than nine million" national | Earlier settings (the June 2012 era) | Its text gives short-term timber as "about half of one cubic metre" per person, the earlier setting (the final model uses 1). The rounded figures themselves fit both versions (39.4 to 39.5, 80.1 to 80.6) |
| Lane, Dawes and Grace (submitted Sep 2013) *Environmental Modelling & Software*, "Construction methodology of a resource-based carrying capacity assessment model" (not in the published list) | Worked example, Tables 5 and 6: Australia 42,834,167; timber 84,276 km2 (1.1%); food 48.8%; red meat 40.3% | A development version of Feb 2013 (`temp model.xls`) | 42,834,167 matches that workbook exactly; neither release gives it |
| Lane (draft, Feb 2016) "Organic agriculture in human carrying capacity modelling" | Reports the organic-yield analysis (51 foods, 40 studies, wheat 69%, overall mean 81%); no capacity figures | n/a | Draft only; the data are in `Organic/Organic comparisons for paper.xls` |
| Lane, Dawes and Grace (2014) *Ecological Modelling* 272 | Australia 40,450,144; land for food 48.9%, biofuel 0.2%, textiles 2.2%, timber 1%, infrastructure 0.4% | **`2011` (final, as released online)** | 40,450,144 exactly; timber 1.0% is `2011` (1.5% under `2011-thesis`); all five shares match |
| Lane, Dawes and Grace (2015) *Population and Environment* 36(3) | Table 2: capacity for Australia and seven states (40,439,187; 10,033,151; 5,975,944; 6,178,020; 2,069,865; 3,696,938; 222,986; 33,274); proportions; states sum 28 million; regions sum 23 million | **`2011-thesis` (Table 16 / `Totals.xls`)** | Table 2 matches `Totals.xls` to the person. The other figures (28, 23, 1.8 and about 4.5 million km2) agree with both versions |
| Lane (2015) IAFOR proceedings | none (argument; historic estimates of national capacity) | n/a | No model figures |
| Lane (2017) *Population and Environment* 38(3) | Table 2: short-term as 2015 plus long-term capacity 9,431,487; 1,609,575; 539,589; 516,284; 830,042; 2,105,909; 24,414; 3,722; "only 13 regions are under-capacity" (long-term); cropping land plateau at 7%; "23 million" with a 3.5% meat-eggs diet and 10% cropping | **`2011-thesis`** | Table 2 matches `Totals.xls` exactly. "13 regions": 13 under `2011-thesis`, 14 under `2011`. "23 million": 23.0 under `2011-thesis`, 22.3 under `2011` |
| Lane (2014) PhD thesis | Table 16 (as the 2015 paper) | `2011-thesis` for Table 16; `2011` for Tables 7 and 14 and the text | Table 14 timber 1,968 m2 per person is `2011`; Table 16 is `Totals.xls` |

## What differs, and whether it changes a conclusion

At national and state scale the two versions agree to within 3.3%, in the cases listed here:

| | Short-term | Long-term |
|---|---|---|
| Australia | 40,450,144 vs 40,439,187 (0.03%) | 9,430,960 vs 9,431,487 |
| QLD | 6,228,219 vs 6,178,020 (0.8%) | same |
| TAS | 225,920 vs 222,986 (1.3%); existing population 210% vs 213% of capacity | same |
| NT | 33,429 vs 33,274 (0.5%) | same |
| SA | same | 816,658 vs 830,042 (1.6%); 161% vs 158% |
| WA | same | 2,035,744 vs 2,105,909 (3.3%); 93% vs 90% |

No state changes between under and over capacity. Of the 52 regions, none changes status short-term, and one changes long-term:
Wimmera, whose population (45,023) sits almost exactly on its capacity (45,016 under `2011-thesis`, 58,455 under `2011`). That is the
whole difference between "13 regions" and "14 regions" in the 2017 paper. The regional figures that do move noticeably long-term
(up to 29%: North Central Vic, Border Rivers-Gwydir, Murray, Wimmera, Northern and Yorke) appear in the 2017 paper's map (Figure 3) and
in the thesis's regional tables.

The 2017 paper's own Table 1 lists the long-term infrastructure default as 500 m2 and timber as 1 m3, but its results (Table 2)
were produced with 365 m2 and an earlier timber setting; Table 1 also gives the short-term biofuel default as 1%. The headline
national figure is the same either way (9,431,487 under both), so the inconsistency does not move the conclusion.

The 2014 paper's tables (rainfall, land use per person, ACLUMP against ABS land use, parameter summary) are in `Papers and manuscripts/Lane_tables_and _captions.docx` (Oct 2013).
The timeline of versions and their dates is in `VERSIONS.md`.

## What can be reproduced from where

| Source of figures | Reproduced by |
|---|---|
| The live dashboard, and the 2014 *Ecological Modelling* paper | release `2011` (identical to the live dashboard in all 120 default cases) |
| Thesis Table 16, the 2015 and 2017 *Population and Environment* tables, the 2017 "13 regions" and "23 million" | release `2011-thesis` only. The live dashboard gives different regional long-term values and cannot reproduce them |
| Thesis text, Tables 7 and 14 | release `2011` (and `2011-corrected` for the long-term textiles value, 11.5 kg) |

## Inputs or calculation?

`decompose_versions.mjs` applies each difference between the two versions alone to the final model. Effect on capacity:

| Cause | Short-term: Australia / worst NRM | Long-term: Australia / worst NRM |
|---|---|---|
| Default inputs (biofuel 0.5% to 0.53%; timber 1 to 0.5 m3; textiles 12.5 to 11.5 kg; infrastructure 500 to 365 m2) | -0.03% / -1.4% (South East Qld, biofuel) | +0.01% / +3.7% (Alinytjara Wilurara, textiles) |
| Timber yield per region instead of one national value (calculation) | 0.0% / 0.0% | 0.0% / -16.5% (North Central Vic) |
| `Base!K348`, the timber usable fraction 0.3624 instead of 0.5665 (calculation) | 0.0% / 0.0% | 0.0% / -9.7% (North Central Vic) |
| Both calculation changes | 0.0% / -3.8% (Border Rivers-Gwydir) | 0.0% / -29.3% (North Central Vic) |
| Everything (= `2011-thesis`) | -0.03% / -1.4% | +0.01% / -28.6% |

So the large regional long-term differences come from the calculation (timber), not from the defaults. The defaults move results by
a few percent at most. The two versions are otherwise the same: every other sheet, row and formula of the workbook is identical
(the June 2012 workbook's different Settings layout reproduces to 0.000%), and the unchanged short-term timber default has no
effect on capacity because timber uses land that is spare (non-agricultural) until the long-term settings, with 5 m3 per person, run short of it.
Timber still changes the land-requirement shares (1.0% against 1.5% of all land for Australia short-term, quoted in the 2014 paper).

## What this means

- The papers' conclusions (national and state capacities, which states are over capacity, the scale effect of about 40 to 23 million,
  and the long-term gap) hold under either version.
- Figures that would read differently under the final method: the 2015 and 2017 tables to the digits given above, the "13 regions"
  statement in 2017 (14), and the regional long-term map.
- For the follow-up papers: cite the release id with every figure (`2011` is the final method; `2011-thesis` reproduces the earlier
  published tables), and state in the data paper that Table 16 and the 2015 and 2017 tables come from the earlier settings.
