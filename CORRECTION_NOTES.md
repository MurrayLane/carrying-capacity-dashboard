# Draft correction notes (for Murray to review; nothing has been sent)

Drafted 2026-11-05 from `ERRATA.md` (rows 1 and 2 for the wording, 'Checked line by line' for each paper's own figures). Each note opens with the same two paragraphs (the wording Murray agreed) and then lists only the statements in that paper that change. Page numbers are from the accepted manuscripts and must be checked against the published versions. Figures regenerate with `node analysis/model_archive/corrected_claims.mjs` from `web/`.

The shared opening, used in every note below:

> In rebuilding the model for a new data set, two conversion factors were found to have been applied on a different basis from the one their sources state.
>
> **Beef.** The model converts reported beef production into meat available to eat. The ABS reports red meat in carcase weight, which still includes bone and fat, so a carcase-to-retail yield is needed. For beef it was incorrectly set to 1.0, so bone and trimmed fat were counted as food. Restoring the USDA factor (0.705) lowers short-term national capacity by about 7 million people, to about 33 million.
>
> **Biodiesel.** The yield of biodiesel from oilseeds was taken from ABARE (2009), which gives 400 litres per tonne of oilseed. The model mistakenly multiplied this by the seed's oil content a second time, so canola yielded 14.8% of its mass as biodiesel where the source implies 35.2%. Correcting this raises long-term national capacity from 9.4 to about 15 million people.

---

## 1. Thesis (QUT ePrints 67485)

*Shared opening, then:*

**Statements that change**

* Short-term national capacity, "over 40 million" (abstract; pp. 160, 256, 305, 354): **33.3 million**, 1.5 times the population of 22.3 million (not "almost twice").
* Table 16 and its text (pp. 280, 355): national 33.3 million against 21.0 million summed over the regions, a ratio of 1.59 (was 40.4 against 22.9, 1.76). The regions fall short of the national figure by about a third, not "almost half". States, short term (NSW-ACT, Victoria, Queensland, SA, WA, Tasmania, NT): 8.35, 5.34, 6.71, 1.78, 3.18, 0.25, 0.03 million.
* Long-term national capacity, "about nine million" (p. 282): **15.4 million**, 1.45 times the population (not 2.4 times).
* "Only 13 of the 60 regions are actually under capacity" in the long term (p. 272): **17**. The stated reason, biofuel land, no longer holds.
* Long term with biofuel set to zero, "about 18 million": 15.5 million.
* Appendix Table 28 (pp. 386, 388, 391): beef (dressed) carcase-to-retail yield 100.0% becomes 70.5%; biodiesel from canola 14.8% becomes 35.2%.

## 2. Lane, Dawes and Grace 2014 (Ecological Modelling)

*Shared opening, then:*

**Statements that change.** The only results statement is Australia's capacity: 40,450,144 becomes **33,307,814**. The land shares of the same paragraph (food 48.93%, biofuel 0.23%, textiles 2.16%, timber 1.04%, infrastructure 0.38%) become 49.46%, 0.09%, 1.78%, 0.85%, 0.32%. No conclusion of the paper rests on these values.

## 3. Lane, Dawes and Grace 2015 (Population and Environment)

*Shared opening, then:*

**Statements that change**

* "Over 40 million", "just over forty million, almost twice the current population" (abstract, section 4): **33.3 million, about 1.5 times**.
* Table 2 and section 4.3: national, states and regions 40.4, 28.2 and 22.9 million (ratio 1.76) become **33.3, 25.6 and 21.0 million (1.59)**. Excess land, national against regional: 1.8 against 4.6 million km2 becomes 1.8 against 4.5.
* Section 4.1: NSW-ACT 10.03 million becomes 8.35 million; Tasmania 223 thousand becomes 255 thousand. **Victoria is now marginally over capacity (about 101% to 104% of its capacity), so three states, not two, exceed capacity.**
* Section 4.2, Figures 1 and 2: regions over capacity, short term, 31 of 53 becomes 30. The maps are to be redrawn from the corrected values; the verbal conclusion has not been re-tested.

## 4. Lane 2017 (Population and Environment)

*Shared opening, then:*

**Statements that change**

* "Just over 40 million ... reasonably accurate" (section 3.1, abstract): **33.3 million**. The corroboration from exports of red meat and broadacre crops is weaker at the lower level.
* Table 2, short term: the eight capacities become 33,307,814 (Australia) and, for the states, 8.35, 5.34, 6.71, 1.78, 3.18, 0.25 and 0.03 million. The "existing population as a proportion" row is to be recomputed.
* Table 2, long term: capacities become **15,350,146** (Australia), 1,720,081, 640,649, 930,892, 790,425, 1,959,889, 46,394 and 5,473 for the states (was 9,431,487, 1,609,575, 539,589, 516,284, 830,042, 2,105,909, 24,414, 3,722). Queensland nearly doubles; Western Australia and South Australia fall. The proportions row is to be recomputed.
* Section 4.1: "only 13 regions are under-capacity" becomes **17**, and the explanation (biofuel, climate variability, organic production) is no longer led by biofuel.
* Section 4.1: "all states, with only the exception of Western Australia, are over capacity" in the long term: **Western Australia is also over capacity** (about 109% to 117%).
* Figure 4 and its text: "capacity only increases until the 7 percent mark of cropping land is reached" (9.5, 11.8, 14.2, 16.2 million at 4 to 7%) becomes **flat at 15.4 million from 4% to 10%**. With the correction, cropping land is not a long-term constraint, so the figure and the paragraph that describes it no longer hold.

---

## Not drafted

* **Lane and Dawes 2013 (Urban Ecosystems).** Affected (15% meat-eggs 39.5 becomes 32.2 million, vegan 80.6 becomes 86.1, regions 23.0 becomes 21.0, long term 9.4 becomes 14.9) but not among the three papers Murray named. The inflection of the red-meat sweep holds. Add a note if wanted.
* **Errors 3 to 6** (earlier settings behind the 2015 and 2017 tables, the dashboard textiles default, stale help text, 2011 state populations) have no agreed wording.
* **The submitted 2013 EMS manuscript** (worked example, Australia 42,834,167) is not in the published list; recompute only if it is resubmitted.

## Before sending

1. Check each statement and page number against the published version, not the accepted manuscript.
2. Decide whether the 2015 maps (Figures 1 and 2) are redrawn before the note goes out.
3. The 2015 and 2017 tables use regional populations (error 6); on the published state inputs the proportions differ slightly (`ERRATA.md`, 'Checked line by line').
