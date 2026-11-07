# B15: how the works that cite Murray's publications use them

Input: `qa/reports/cited_by_openalex_2026-11-07.md`. Output table: `qa/reports/B15_citing_works.csv` (one row per distinct work).

## Result in one paragraph

63 distinct citing works, after merging repeats across the four lists. None could be classed `applies` or `discusses` from its abstract. 41 are `passing` and 22 are `unknown`. The citing literature is overwhelmingly the Chinese "resource and environment carrying capacity" index tradition, which cites the model as a precedent. The few works that sit close to the food-and-land method (the Iran and Java groups) have abstracts that do not say whether they use it, so they stay `unknown` until their full text is read.

## How the abstracts were got, and what the classes rest on

* OpenAlex returned abstracts for some works through a fetch tool that paraphrased them; Crossref and Semantic Scholar supplied others word for word. All 46 rows marked `abstract` rest on an abstract (some read as a paraphrase, not verbatim). 17 rows have no reachable abstract (publisher pages for Elsevier, Springer and Taylor and Francis were blocked, and OpenAlex holds none for these) and are `unknown` with basis `none`.
* No full text page was opened, so no row has basis `full text page`.
* `passing` is given where the abstract shows the work uses a different method on a different question and says nothing of engaging with the model. It is an inference from the abstract alone; a full read could move a row to `discusses`. `unknown` is given where the abstract is absent, or is present but leaves open whether the model is used.

## Counts by class

| Class | Works |
|---|---|
| applies | 0 |
| discusses | 0 |
| passing | 41 |
| unknown | 22 (17 no abstract; 5 abstract present but silent on use) |
| Total | 63 |

## Counts by kind of carrying capacity

| Kind | Works |
|---|---|
| Urban or regional index | 21 |
| Water | 14 |
| Ecological | 12 |
| Other (energy, coast, port, livestock, land use, urban growth) | 11 |
| Food and land | 5 |

Of the 5 food-and-land rows, 3 are Murray's own papers (two journal papers and the conference paper); the other 2 are Khorsandi 2022 and Safitri 2021 below.

## Works classed `applies` or `discusses`

None. The abstract of no citing work states that it uses the land-and-diet method or its results, or that it compares or criticises the method or its findings.

## Closest relatives, held at `unknown` (read the full text first)

* **Khorsandi et al. 2022, Science of the Total Environment** (cites the 2014 paper and the thesis). Estimates Iran's carrying capacity from land suitability, water and crop productivity, giving 35.5 and 20 million people against a population of 84 million, at four spatial scale levels, with food production as the limit. Same question and same family as Murray's method, but built on human appropriation of net primary production, and the abstract does not say it uses Murray's method. This is the work most likely to be a true `applies` or `discusses`.
* **Khorsandi et al. 2023, Heliyon** (cites the 2014 paper and the time-frames paper). A simplified water-based meta-model, validated for Iran, that gives lower and upper bounds at several scales. Built on an earlier process model of the same group; relation to Murray's method not stated.
* **Ebrahimi Sarindizaj 2023, Science of the Total Environment, "Letter to the Editor"** (cites the thesis). No abstract. Published in the same journal after Khorsandi 2022; it may be a comment on that paper. The abstract is silent, so this is not settled.
* **Safitri et al. 2021, ISPRS International Journal of Geo-Information** (cites the 2014 paper, the 2015 paper and the thesis). Java: ecological footprint of physiological needs by land type, with land suitability from a support vector machine. Cites three of Murray's items, which is more than a passing mention would, but the abstract does not say how they are used.
* **Safitri et al. 2020, IOP Conference Series** (cites the 2014 paper and the thesis). Java land suitability for land use planning scenarios, "short-term and long-term"; no carrying-capacity calculation in the abstract.

## The Australian ones

Six rows have an Australian study area.

* Three are Murray's own: Lane, Dawes and Grace on scale (Population and Environment, 2014 online), Lane on short-term and long-term time frames (2016), and Lane's conference paper on the leverage point in the sustainability crisis (IAFOR, 2015). The scale paper is listed here as citing the 2014 paper. No abstracts reachable; `unknown`. They are self-citations and say nothing about outside uptake.
* **Bolleter 2018, "The consequences of three urbanisation scenarios for northern Australia", Australian Planner** (cites the time-frames paper). The abstract reads as a response to the federal white paper's projection of about 5 million people in northern Australia by 2060, and compares three settlement patterns. It does not mention carrying capacity; `unknown`.
* **Bolleter 2018, "Barriers to New Northern Cities", SpringerBriefs in Geography** (cites the time-frames paper). No abstract; `unknown`.
* **Martuwarra RiverOfLife et al. 2025, Australian Journal of Environmental Education** (cites the time-frames paper). Traditional Owner water governance of the Fitzroy River in the Kimberley; no carrying-capacity calculation; `passing`.

No citing work is a food-and-land capacity estimate for Australia, and none is a critique of the model.

## Anything surprising

1. **No application, no critique, from the abstracts.** The coordinator's reading (uptake as a cited precedent in another literature) holds up for 41 of 63 works, and the other 22 could not be shown to differ. The statement that the model is cited and not applied or contested is supported, not proved: the full text of the five relatives above is where it could fail.
2. **63 distinct works, not "about 60"**, after merging the repeats (Khorsandi 2023, Safitri 2021 and Murray's time-frames paper each appear in more than one list). The OpenAlex counts are 51 + 6 + 8 + 6 = 71 listings.
3. **A retracted paper is among the citers.** Luo et al. 2022, Forests, the urban and rural construction land paper (DOI 10.3390/f13091514), is marked "RETRACTED" in its title. It is `passing`; it should not be counted as support.
4. **The Iran group cites the model in three ways** (2014 paper, time-frames paper, thesis) across three papers and a letter, and is the only cluster working on food, land and water limits at several spatial scales. It is the nearest thing to a user community.
5. **The Java pair (Safitri 2020 and 2021) cites three of Murray's items between them**, including the thesis, with abstracts that look like a different method (support vector machine land suitability, ecological footprint).
6. **Murray's own papers account for three of the 63** (the scale paper, the time-frames paper and the IAFOR paper), and the time-frames paper appears in three of the four lists. Outside self-citation, the count of independent citers is 60.
7. **Abstract gaps are not random.** Elsevier, Springer and Taylor and Francis abstracts were not reachable through the sources open here; 17 rows are blank for that reason, including several in the Yellow River and Dongting Lake groups. The unknown count is a limit of access, not of the works.
