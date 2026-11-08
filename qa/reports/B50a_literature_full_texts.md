# B50a: five archived papers read in full

Papers read with the Read tool, every page, from `/home/user/carrying-capacity-models/Literature review/` (all five are PDFs per `file`). Registers searched: `qa/literature_register.csv` and `qa/claims_register.csv`, by first author, year, DOI and the quoted figures. Rows found: L075 (Hatfield-Dodds 2015), L076 (Bryan 2016), L085 (Giampietro and Saltelli 2014), L091 (Graymore, Sipe and Rickson 2010), L094 (Millar and Roots 2012); L086, L090, L098 and L073 mention these papers in passing. `qa/claims_register.csv` has no row citing any of the five. The outlines (`papers/A_results/OUTLINE.md`, `papers/B_methods/OUTLINE.md`, `SECTION7_DRAFT.md`, `DISCUSSION_MEASURES.md`) do not name any of the five; the only characterisations are the register `what_taken`, `used_by` and `notes` fields. No register was edited.

Archive hashes (sha256), for `local_path` and `sha256`:

| Row | File | sha256 |
|---|---|---|
| L076 | `Bryan2016_GEC_land_use_sustainability_Australia_2050.pdf` (23 pages) | 2d3da6f3ae67a93d9181e975900baf9ee2625a5cd9dfc3becfbc55c52ba83a2b |
| L075 | `Hatfield-Dodds2015_Nature_Australia_free_to_choose.pdf` (14 pages) | bea474146e1dcaa3c24397a58aeca82a349b3491a6d4b93bfb816e99fd5b07a6 |
| L091 | `Graymore_Sipe_Rickson2010_Sustaining_human_carrying_capacity.pdf` (10 pages) | 7fecca1f69b3789b77f0d79d621af74d0137ccbf19979b536db0056b74d72502 |
| L094 | `Millar_Roots2012_Changes_in_Australian_agriculture_and_land_use.pdf` (16 pages; page 16 is a copyright notice) | 9022b6f5b92762e75ca8746efea4f4ed257f411c779ecbeb793aa482dfbc7b39 |
| L085 | `Giampietro_Saltelli2014_Footprints_to_nowhere.pdf` (12 pages) | 4cc9713a88dc27dc87e11be89c658b3e3a06295e2bd4de2185a4492a4edff4a4 |

None of the five cites Lane (reference lists read in full, and a text search for "Lane" found nothing).

---

## 1. Bryan et al. 2016 (L076)

**(1) Citation as printed.** Bryan, B.A., Nolan, M., McKellar, L., Connor, J.D., Newth, D., Harwood, T., King, D., Navarro, J., Cai, Y., Gao, L., Grundy, M., Graham, P., Ernst, A., Dunstall, S., Stock, F., Brinsmead, T., Harman, I., Grigg, N.J., Battaglia, M., Keating, B., Wonhas, A., Hatfield-Dodds, S. 2016. "Land-use and sustainability under intersecting global change and domestic policy scenarios: Trajectories for Australia to 2050". Global Environmental Change 38: 130-152. DOI 10.1016/j.gloenvcha.2016.03.002 (printed p. 130). Open access, CC BY.

**(2) What it estimates.** Using the LUTO model, the authors run 648 scenarios (4 global outlooks x 3 domestic land-use policies x 3 productivity growth rates x 3 adoption hurdle rates x 3 climate models x 2 capacity-constraint settings) of land use on Australia's 85.3 Mha of intensive agricultural land, annually from 2013 to 2050 on a grid of about 1.1 km (pp. 130, 133). Each year each cell either stays in agriculture or moves to carbon plantings, environmental plantings, biofuels or bioenergy, whichever is most profitable under the scenario's carbon, oil, electricity and commodity prices (pp. 133-134). They report six indicators: economic returns, food and fibre production, emissions abatement, water use, biodiversity services and energy (p. 134). Under strong global abatement large areas, mainly beef grazing land in Queensland and New South Wales, go to plantings, yet crop output rises because of productivity growth and the conversion of the least productive land (pp. 139, 142, 147). The authors stress these are projections of possible futures, not forecasts (p. 148).

**(3) Method family.** Not a capacity method and no people-count. In the methods paper's terms it is closest to the integrated resource-flow (scenario model) family beside Foran and Poldy 2002: a partial-equilibrium land allocation model driven by global integrated-assessment outlooks. Its use is context for section 6 (yield basis, time frame, competition for land).

**(4) Register figures attributed to the paper.**

| Register text (L076 `what_taken`) | Where in the paper | Verdict |
|---|---|---|
| LUTO model of Australian agricultural land use | Abstract p. 130; section 2.2 p. 133 | Confirmed as printed |
| 2013 to 2050 | Abstract p. 130 ("2013-2050"); p. 133 | Confirmed as printed |
| 1.1 km grid | Abstract p. 130 ("1.1 km grid cells"); p. 133 ("~1.1 km (0.01°)") | Confirmed as printed |
| global and domestic policy scenarios | Abstract p. 130; sections 2.3 and 2.4 pp. 135-137 | Confirmed as printed |
| shift to carbon and environmental plantings and biofuels can occur without major effects on agricultural production under strong abatement incentives | Abstract p. 130; conclusion p. 148 | Confirmed with a difference: the paper's condition is "strong global abatement incentives complemented by biodiversity-focussed domestic land-use policy" (abstract), and the claim is that returns and ecosystem services rise "without major impacts on agricultural production"; the register drops the domestic-policy half of the condition |
| 26 GB data pack | Abstract p. 130 (doi 10.4225/08/5604A2E8A00CC) | Confirmed as printed |

**(5) Figures the registers lack that bear on Australia or on capacity.**
* Study area 85.3 Mha of intensive agricultural land; Table 1 (p. 133) gives 2006 areas, for example dryland winter cereals 17,990.4 kha, beef 32,491.6 kha, sheep 18,443.7 kha, dairy 2,019.5 kha dryland and 715.4 kha irrigated.
* "Around 60% of Australian agricultural production is exported" (p. 133).
* Agriculture is not allowed to expand into native vegetation (p. 133); productivity growth set at 0, 1.5 and 3.0% a year simple increase (p. 136).
* M3 Balanced by 2050: 38.1 Mha changes use; livestock grazing falls 30.1 Mha (-55.9%), crops and horticulture fall 5.3 Mha (-21.2%) (p. 139). L1 Balanced: grazing falls 37.7 Mha (-70.1%), crops and horticulture 9.7 Mha (-38.6%) (p. 139).
* Crops and horticulture output rises to 130.1 Mt (+59.9%) by 2050 under M3 Balanced (p. 142); 89.5 to 162.7 Mt across low to high productivity growth, cattle 15.5 to 24.2 million head and sheep 49.2 to 71.2 million head (p. 142). Fig. 11 (p. 144) starts crops and horticulture at about 80 Mt in 2013 (read from the chart).
* For section 6 these give a published Australian range for the yield trajectory to 2050 and for how much food land a carbon price could take. The paper also cites Grundy et al. 2016 (Agricultural Systems 142: 70-83, "Scenarios for Australian agricultural production and land use to 2050") as the LUTO paper on agriculture and food security; it is not in our registers and is the closer food comparator.

**(6) Cites Lane.** No.

**(7) Row updates for L076.**
* `read_or_reported`: read.
* `local_path`: `carrying-capacity-models/Literature review/Bryan2016_GEC_land_use_sustainability_Australia_2050.pdf`; `sha256` as above.
* `title`: add pages "38: 130-152" and the printed title capitalisation ("Trajectories for Australia to 2050").
* `what_taken`: "LUTO partial-equilibrium land-use model, 648 scenarios, 85.3 Mha of intensive agricultural land, annual, about 1.1 km grid, 2013 to 2050; with strong global abatement plus biodiversity-focussed domestic policy, plantings and biofuels raise returns and ecosystem services without major impacts on agricultural production; crops and horticulture 89.5 to 162.7 Mt in 2050 (130.1 Mt under M3 Balanced) as grazing land falls up to 70%; 26 GB data pack; no capacity figure."
* `notes`: replace the access history with "Full text read from the archive copy (open access, CC BY). Does not cite Lane."
* `used_by`: drop "5 (comparator)" (see the closing list) or say what it is compared on.

---

## 2. Hatfield-Dodds et al. 2015 (L075)

**(1) Citation as printed.** Hatfield-Dodds, S., Schandl, H., Adams, P.D., Baynes, T.M., Brinsmead, T.S., Bryan, B.A., Chiew, F.H.S., Graham, P.W., Grundy, M., Harwood, T., McCallum, R., McCrea, R., McKellar, L.E., Newth, D., Nolan, M., Prosser, I. and Wonhas, A. 2015. "Australia is 'free to choose' economic growth and falling environmental pressures". Nature 527 (5 November 2015): 49-53. DOI 10.1038/nature16065 (printed p. 49). The archive PDF has the article (pp. 49-53) and Extended Data Figs 1-9; the online Methods and Supplementary Information are not in it.

**(2) What it argues.** A new integrated multi-model framework built for the Australian National Outlook runs more than 20 scenarios of energy, water, food, land use, biodiversity, material flows and climate to 2050 (pp. 49-50). Economic growth is strong in all scenarios (GDP about tenfold over the 80 years to 2050, with a 2.9-fold rise in population), while environmental pressures "more than double, stabilize or fall markedly" (abstract, p. 50). Decoupling is possible but not automatic, and needs no change in societal values: collective policy choices, chiefly abatement incentives and land-sector markets, explain 46 to 94% of the differences in environmental performance (pp. 51-52). Strong abatement makes carbon plantings more profitable than beef and other agriculture over large areas (p. 52).

**(3) Method family.** Not a capacity method. Integrated multi-model scenario framework (CGE model MMRF, the global GIAM outlooks, energy model ESM, LUTO for land, water models), the integrated resource-flow family in the methods paper's terms. Context only.

**(4) Register figures attributed to the paper.**

| Register text (L075 `what_taken`) | Where in the paper | Verdict |
|---|---|---|
| Multi-model scenario outlook to 2050 | Abstract and p. 49 ("new integrated multi-model framework"; "more than 20 scenarios") | Confirmed as printed |
| (energy, water, food, land, biodiversity, materials, climate) | Abstract p. 49 ("energy-water-food nexus, rural land use (including biodiversity), material flows and climate change") | Confirmed as printed |
| environmental pressures could more than double, stabilise or fall markedly | Abstract p. 49 ("pressures are projected to more than double, stabilize or fall markedly by 2050") | Confirmed as printed |
| no evidence decoupling is automatic | Abstract p. 49; p. 51 | Confirmed as printed |
| no capacity figure taken | | Correct: the paper gives none |

**(5) Figures the registers lack.**
* Population assumed in all domestic scenarios: about 36 million in 2050 (Extended Data Fig. 8, read from the chart; the text gives the 2.9-fold rise since 1970, p. 50).
* Protein output of the intensive use zone, the paper's food indicator: about 6 Mt in 2013 rising to roughly 6 to 12 Mt by 2050 across scenarios (Fig. 2 p. 50; Extended Data Fig. 4d; chart readings, not printed values). Food grains about 40 Mt in 2013, about 25 to 90 Mt in 2050 (Extended Data Fig. 4e, chart). Crop area about 25 Mha and livestock area about 50 Mha in 2013 (Extended Data Fig. 4g, 4h, chart).
* Carbon plantings 29 to 59 Mha in 2050 (p. 50); up to 58 Mha, or 70% of the intensive-use zone, where carbon sequestration beats beef and agriculture (p. 52); native habitat up 25% (37 Mha) (p. 50).
* These bear on section 6: protein output in Mt could be turned into people fed on a stated diet, and the land figures bound how much food land a carbon price could take. Only the printed figures (29 to 59 Mha, 58 Mha, 70%, 37 Mha, 2.9-fold) should be quoted; the chart readings need the Supplementary Data.

**(6) Cites Lane.** No, in the printed reference list (refs 1-49). The online Methods carry further references ("references unique to these sections appear only in the online paper", p. 52) which the archive copy does not hold.

**(7) Row updates for L075.**
* `read_or_reported`: read.
* `local_path`: `carrying-capacity-models/Literature review/Hatfield-Dodds2015_Nature_Australia_free_to_choose.pdf`; `sha256` as above.
* `title`: printed title has quote marks, "Australia is 'free to choose' economic growth and falling environmental pressures"; add pages 49-53.
* `what_taken`: "Integrated multi-model outlook (more than 20 scenarios, 2050) for the Australian National Outlook; pressures more than double, stabilise or fall markedly; decoupling possible but not automatic and needs no change in values; collective policy choices explain 46 to 94% of differences; carbon plantings 29 to 59 Mha in 2050 (up to 58 Mha, 70% of the intensive-use zone); no capacity figure."
* `notes`: "Full text of the article and Extended Data read from the archive copy; online Methods and Supplementary Information not held. Does not cite Lane in the printed references." L090 (the CSIRO report) stays not reached.

---

## 3. Graymore, Sipe and Rickson 2010 (L091)

**(1) Citation as printed.** Graymore, M.L.M., Sipe, N.G., Rickson, R.E. 2010. "Sustaining Human Carrying Capacity: A tool for regional sustainability assessment". Ecological Economics 69: 459-468 (section "Methods"). DOI 10.1016/j.ecolecon.2009.08.016 (printed p. 459). Received 25 November 2008, accepted 14 August 2009, online 16 September 2009. The issue number (3) is not printed on the pages.

**(2) What it argues.** Following an earlier finding that five common assessment methods (including the ecological footprint) do not work at the regional scale, the authors build a regional sustainability model in which human activities place pressures on a region's carrying capacity, which rests on its resilience (pp. 460-461, Fig. 1). Since neither resilience nor carrying capacity can be measured exactly, they assess whether pressures exceed known or assumed sustainability thresholds instead (p. 461). The tool, SHCC, ranks fewer than 40 indicators on a four-point scale across population, equity and four major pressures (physical restructuring, overharvesting, waste residuals, introduced species), then averages them into dimension and overall ranks (Table 1 p. 463; pp. 464-466). It was tested on South East Queensland (18 local governments, 2.46 million people in 2001) and judged against an evaluation matrix, meeting six of eight criteria (Table 2 p. 464; p. 466).

**(3) Method family.** Pressure-against-threshold sustainability index (the register's "index" in section 4); not a people-count and not in the land and diet families. Shares the regional scale of the thesis's planning-oriented methods; it is a South East Queensland study.

**(4) Register figures attributed to the paper.**

| Register text (L091 `what_taken`) | Where | Verdict |
|---|---|---|
| Regional sustainability framework that scores human pressure on regional ecosystems | Abstract p. 459; section 4.1 p. 464 | Confirmed as printed |
| no people-count taken | | Correct: the paper gives none, and reports no SEQ scores, only the evaluation matrix |
| Ecological Economics 69(3): 459-468; online 2009, issue January 2010 | p. 459 | Volume, pages, DOI and online date confirmed; issue number and month not printed in the PDF |

**(5) Figures the registers lack.** No capacity figure. Table 1 (p. 463) sets population growth ranks (rank 1 at 1.4% or -1.4% a year; rank 4 at 0), a stable population "within the human carrying capacity of the region" as the target (p. 464), and thresholds such as remnant vegetation 10/20/50/80% and land modified 100/80/40/20%. SEQ population 2.46 million in 2001, expected to grow by about one million over 20 years (p. 463). Useful only as an example of the threshold (pressure) view of carrying capacity for section 2.

**(6) Cites Lane.** No.

**(7) Row updates for L091.**
* `read_or_reported`: read.
* `local_path`: `carrying-capacity-models/Literature review/Graymore_Sipe_Rickson2010_Sustaining_human_carrying_capacity.pdf`; `sha256` as above.
* `what_taken`: "Regional sustainability tool (SHCC): fewer than 40 indicators ranked 1 to 4 against sustainability thresholds across population, equity and four pressures, averaged to an overall rank; carrying capacity treated as not measurable, so pressure against thresholds stands in for it; tested on South East Queensland (2.46 million in 2001), no scores reported; no people-count."
* `notes`: "Full text read from the archive copy. Issue number not printed. Does not cite Lane."

---

## 4. Millar and Roots 2012 (L094)

**(1) Citation as printed.** Millar, J. and Roots, J. 2012. "Changes in Australian agriculture and land use: implications for future food security". International Journal of Agricultural Sustainability 10(1), February 2012: 25-39. DOI 10.1080/14735903.2012.646731 (printed p. 25).

**(2) What it argues.** The paper asks whether Australia can and should keep exporting food and feeding itself as farmland is lost, farmers age and leave, water is capped and the climate changes (pp. 25-26). It reviews land-use change (409 Mha of agricultural land in 2009 against 456 Mha in 2001), urban, lifestyle, conservation, forestry and mining uses, the farm workforce, and environmental limits (pp. 27-34). It concludes that in the short term Australia can keep exporting and feeding itself, "give or take minor import substitutions", but that longer-term food security is less certain because of climate, loss of productive land to urban sprawl and mining, skilled-labour shortages and under-investment in research (abstract; p. 36). It calls for a national land-use planning framework to protect productive land (p. 36).

**(3) Method family.** Qualitative review; no method of its own. It carries one export-inclusive count second-hand (PMSEIC 2010, below).

**(4) Register figures attributed to the paper.**

| Register text (L094 `what_taken`) | Where | Verdict |
|---|---|---|
| Qualitative review | whole paper | Confirmed |
| Australia keeps producing enough food in the short term | Abstract p. 25; conclusion p. 36 | Confirmed with a difference: the paper says enough "for domestic and export markets at least in the short term with import substitutions as required" |
| long-term threats are climate, urban and mining use of productive land, labour, R and D | Abstract p. 25; p. 36 | Confirmed as printed |

**(5) Figures the registers lack.**
* "Australia is food secure and produces enough food today to feed approximately 60 million people" (PMSEIC 2010, p. 1, quoted on p. 26); and "if our population grows to 35-40 million and climate change constrains food production, we can expect to see years where we will import more food than we export" (same, p. 26). The 60 million is an export-inclusive count that belongs beside the industry rows L011 and B163 in the register of estimates; it is quoted second-hand, so the PMSEIC report itself should be sought.
* 60% of agricultural production exported; farmers produce 93% of the domestic food supply (p. 26).
* Agriculture 409 Mha, 53% of land, 2009 (p. 27); 456 Mha in 2001 to 409 Mha in 2009, "a reduction of 5.9 million ha per year" (p. 27). The authors add that no national data show where the land went (p. 27), so this is not a rate of farmland loss to cities.
* At 5.9 Mha a year, agricultural land falls from 18 to 5 ha a person by 2050 (p. 34).
* Population to 2050: 35 million (abstract; p. 34, from 22.5 million) but 36 million in the introduction (p. 25, from 22 million in 2010); the paper is internally inconsistent here.
* Cites Poldy and Foran 2002 (CSIRO Resource Futures Working Paper 02/01) for 35 million by 2050 reducing what is left for trade (p. 35), and for dryland salinity 2.5 Mha, possibly 17 Mha by 2050 (p. 32).

**(6) Cites Lane.** No.

**(7) Row updates for L094.**
* `read_or_reported`: read.
* `local_path`: `carrying-capacity-models/Literature review/Millar_Roots2012_Changes_in_Australian_agriculture_and_land_use.pdf`; `sha256` as above.
* `what_taken`: "Qualitative review: Australia keeps producing enough for domestic and export markets in the short term, with import substitutions as required; long-term threats are climate, urban and mining use of productive land, skilled labour and research investment; quotes PMSEIC 2010 'enough food to feed approximately 60 million people' and imports exceeding exports in some years at 35 to 40 million; agricultural land 456 to 409 Mha 2001 to 2009."
* `notes`: "Full text read from the archive copy. Does not cite Lane. The 60 million is PMSEIC 2010 p. 1, quoted second-hand: candidate new row in the register of estimates (export-inclusive)."
* New row suggested: PMSEIC 2010, "Australia and food security in a changing world", Prime Minister's Science, Engineering and Innovation Council, Canberra; 60 million; `read_or_reported` reported (via Millar and Roots 2012 p. 26).

---

## 5. Giampietro and Saltelli 2014 (L085)

**(1) Citation as printed.** Giampietro, M. and Saltelli, A. 2014. "Footprints to nowhere". Ecological Indicators 46: 610-621. DOI 10.1016/j.ecolind.2014.01.030 (printed p. 610). Received 2 May 2013, accepted 21 January 2014.

**(2) What it argues.** The authors argue that the footprint's protocol (the "syntax") does not deliver what its narrative (the "semantics") claims: comparing what is taken with what nature could give at a reference state (abstract; section 3). Footprint and biocapacity are both measured on the same altered, present-day system using world-average yields and equivalence factors, so they have no external referent; biocapacity even rises with fertiliser and other intensification (pp. 614-617). Non-energy footprint and biocapacity are near equal by construction, so the planet's deficit is set by the carbon footprint, whose assumptions (sink side only, a flow equated with a stock, forests that absorb carbon forever, flat conversion factors) they find indefensible (sections 4.3 and 5, pp. 618-619). They conclude that the footprint gives a falsely reassuring 50% overshoot, encourages complacency, and cannot replace several non-equivalent indicators across scales (abstract; pp. 619-620).

**(3) Method family.** Critique of the ecological footprint family (section 2 and section 4 of the methods paper).

**(4) Register figures attributed to the paper.** The L085 `what_taken` was taken from the reply (L086); the text bears it out:

| Register text | Where | Verdict |
|---|---|---|
| argued not to answer the question it claims to | Abstract p. 610 ("lack of correspondence between the semantics ... and the syntax"); section 3 | Confirmed |
| laborious yet fragile | Abstract p. 610 ("the laboriousness of EF computation protocols contrasts with its ultimate fragility") | Confirmed as printed |
| overshoot driven by the carbon handling | Abstract p. 610; section 4.3 p. 618; Fig. 1 p. 612 | Confirmed |
| encouraging complacency | Abstract p. 610 ("reassuring and complacent"); p. 620 | Confirmed as printed |
| Ecological Indicators 46: 610-621 | p. 610 | Confirmed as printed |

**(5) Figures the registers lack.** No Australian content (no mention of Australia). Points that bear on our footprint builds: the production footprint is EF_P = P/Y_N x YF x EQF = P/Y_W x EQF, local production expressed at world-average yield (p. 614); the Netherlands' imported feed alone uses almost four times its own cropland (p. 617, citing van Vuuren et al. 1999); the GFN's 50% overshoot set against the nitrogen comparison, 100 Mt a year of fertiliser nitrogen plus 60 Mt from natural cycles, the fixation of 2.66 Earths (p. 620). The world-average-yield point supports the section 7 draft's statement that the footprint and HALF "use world-average productivity, so they cannot say what a region's own land feeds" and could be cited there.

**(6) Cites Lane.** No.

**(7) Row updates for L085.**
* `read_or_reported`: read.
* `local_path`: `carrying-capacity-models/Literature review/Giampietro_Saltelli2014_Footprints_to_nowhere.pdf`; `sha256` as above.
* `what_taken`: "Critique of the ecological footprint: the protocol does not match its narrative (no external referent, world-average yields and equivalence factors, biocapacity that rises with intensification); laborious yet fragile; the deficit is set by the carbon footprint, whose assumptions are indefensible; the 50% overshoot reassures and encourages complacency; argues for several non-equivalent indicators across scales."
* `notes`: "Full text read from the archive copy. No Australian content. Does not cite Lane. The further reply (Ecological Indicators 46: 260-263) not opened."
* L086 note: no change needed; its first link correctly names this paper's DOI.

---

## Characterisations in our outlines and registers that the text does not support

1. **L076 `used_by` "5 (comparator)"** and the L098 note "Bryan 2016 (L076) is the closer comparator": Bryan 2016 gives no people-count and no food capacity, so it cannot sit in section 5 as a comparator figure or a method run on the common data. It supports section 6 (yield trajectory, time frame, land taken by plantings). If a food comparator is wanted, Grundy et al. 2016 (Agricultural Systems 142: 70-83), which Bryan cites, is closer.
2. **L076 `what_taken`**: "without major effects on agricultural production under strong abatement incentives" leaves out the paper's second condition, a biodiversity-focussed domestic land-use policy (abstract).
3. **L094 `what_taken`**: "keeps producing enough food in the short term" omits "with import substitutions as required" (abstract) and that the claim covers export markets as well as domestic needs.
4. **L073 note (Khorsandi et al. 2022)** says Khorsandi "recommends local food production citing Graymore et al. 2010". Graymore 2010 is a regional pressure-index tool and says nothing about local food production; if our text ever carries that pairing forward, it should not be attributed to Graymore.
5. **L075 and L076 notes** say whether they cite Lane "cannot be told"; both can be told: neither does (L075 only for the printed references; the online Methods references are not in the archive copy).

No figure attributed to any of the five papers was found to be absent from the text. The outlines themselves make no claim about these five papers.
