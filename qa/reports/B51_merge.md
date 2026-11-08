# B51: merge of the B50a and B50b readings into qa/literature_register.csv

Only `qa/literature_register.csv` was edited (CRLF line endings and all 12 columns kept; a read-and-rewrite test reproduced the original file byte for byte before any change). The B50b merge was added at the coordinator's request after the B50a merge.

## Part 1: B50a rows (status "self-checked (B50a full text)", read_or_reported "read")

L075: new what_taken as B50a gives (more than 20 scenarios; 46 to 94%; carbon plantings 29 to 59 Mha, up to 58 Mha, 70%). Old: "Multi-model scenario outlook to 2050 (energy, water, food, land, biodiversity, materials, climate); environmental pressures could more than double, stabilise or fall markedly; no evidence decoupling is automatic; no capacity figure taken". Title gained pages and the quote marks.

L076: old "LUTO model of Australian agricultural land use 2013 to 2050 on a 1.1 km grid under global and domestic policy scenarios; shift to carbon and environmental plantings and biofuels can occur without major effects on agricultural production under strong abatement incentives; 26 GB data pack". New: "LUTO partial-equilibrium land-use model, 648 scenarios, 85.3 Mha of intensive agricultural land, annual, about 1.1 km grid, 2013 to 2050; with strong global abatement incentives complemented by biodiversity-focussed domestic land-use policy, plantings and biofuels raise returns and ecosystem services without major impacts on agricultural production; crops and horticulture 89.5 to 162.7 Mt in 2050 (130.1 Mt under M3 Balanced) as grazing land falls up to 70%; 26 GB data pack; no capacity figure." The domestic-policy condition is in. used_by changed to "methods paper (section 4 (scenario model) and 6 (context: yield path, time frame, land taken by plantings))"; the section 5 comparator is gone. Title gained pages 130-152 and the printed capitalisation.

L085: old "Critique of the ecological footprint: argued not to answer the question it claims to, laborious yet fragile, overshoot driven by the carbon handling, and encouraging complacency (as summarised in the Goldfinger et al. reply)". New: "Critique of the ecological footprint: the protocol does not match its narrative (no external referent, world-average yields and equivalence factors, biocapacity that rises with intensification); laborious yet fragile; the deficit is set by the carbon footprint, whose assumptions are indefensible; the 50% overshoot reassures and encourages complacency; argues for several non-equivalent indicators across scales."

L091: old "Regional sustainability framework that scores human pressure on regional ecosystems; no people-count taken". New: "Regional sustainability tool (SHCC): fewer than 40 indicators ranked 1 to 4 against sustainability thresholds across population, equity and four pressures, averaged to an overall rank; carrying capacity treated as not measurable, so pressure against thresholds stands in for it; tested on South East Queensland (2.46 million in 2001), no scores reported; no people-count."

L094: old "Qualitative review: Australia keeps producing enough food in the short term; long-term threats are climate, urban and mining use of productive land, labour, R and D". New: "Qualitative review: Australia keeps producing enough food for domestic and export markets in the short term (covers exports, and allows import substitution as required); long-term threats are climate, urban and mining use of productive land, skilled labour and research investment; quotes PMSEIC 2010 'enough food to feed approximately 60 million people' and imports exceeding exports in some years at 35 to 40 million; agricultural land 456 to 409 Mha 2001 to 2009."

L073: note reworded to "and recommends local food production." (the Graymore 2010 and Lane 2014 pairing is dropped; the earlier sentence still records that it cites Lane 2014).

Rows added: L136 (placed right after L011): PMSEIC 2010, "Australia and food security in a changing world", about 60 million people, read_or_reported "reported (second-hand, Millar and Roots 2012 p. 26)", used by the methods paper section 4 catalogue, notes counts exports and the primary source (p. 1) is to be read before use. L135 (end of file): Grundy et al. 2016, Agricultural Systems 142: 70-83, journal article, unverified, "not read (lead from Bryan 2016)". Local paths and sha256 are as B50a gives them.

## Part 2: B50b rows (status "self-checked (B50b full text)", read_or_reported "read", local_path and sha256 from B50b)

L081: old "Reference healthy diet and targets for sustainable food production for about 10 billion people with no additional land; at least a 75% reduction of yield gaps; more than 50% cut in red meat and sugar and more than 100% rise in nuts, fruit, vegetables and legumes". New: B50b's text (2500 kcal/day, SSP2 9.2 billion, cropland 13 million km2, up to 10 billion and increasingly unlikely beyond, diet alone cuts cropland 0-2% p 472). Notes: scenario model with a reference diet; the EAT-Lancet 0 to 2% sentence added (supports diet as the lever for emissions, not cropland).

L120: old "Unchecked diet trends: about 80% rise in agricultural GHG by 2050 and more land clearing". New: "Income-dependent diet trends to 2050 give about an 80% rise in GHG from food production (2.27 to 4.1 Gt CO2-Ceq/yr, cradle to farm gate, excluding land clearing) and a median 590 Mha more cropland than 2009; Mediterranean, pescetarian and vegetarian diets need 370-740 Mha less (average 540); Australia is in economic Group A". Family: scenario model on an LCA footprint input.

L111: old "Global crop demand +100-110% by 2050; 1 billion ha cleared under current trends vs 0.2 billion with intensification". New: "+100% (calories) to +110% (protein) from 2005 to 2050; about 1 billion ha cleared by 2050 on the past trend vs about 0.2 billion with land-sparing intensification of under-yielding nations". Base year 2005; scenario model.

L115: old "Meta-analysis: 50-fold spread in impact between producers of the same product". New: "Meta-analysis of about 38,700 farms (119 countries, 40 products): impact varies up to 50-fold among producers of the same product; 65% of grass eaten by ruminants grows on land unsuitable for crops; no animal products cuts food's land use 76% (3.1 billion ha; arable 19%); Australian wheat belt in the bottom 15% for output per ha and GHG". Family: footprint.

L113: old "2050 crop demand may need +25-70% on current production, not a doubling". New: "2050 demand may need about +25-70% on 2014 production (base year 2014; cereals as the stand-in for total crop demand: +26% FAO-based, +68% Tilman-based), not a doubling; FAO's 60% is often misquoted as 70%". Family: concept review.

L101: old "Foundational foodshed-analysis framing paper; no number taken". New: "Commentary defining foodshed and foodshed analysis (from Hedden 1929) and arguing climate, energy and food-price pressures make the geography of supply a sustainability question; announces the 2009 New York State paper (ref 59); no number taken". Title gained "(Commentary)" and the full author list. Family: concept review, a commentary.

L077: only the note changed, appending that the same issue's pp 1-7 commentary (L101) cites this paper as in press.

Rows added in Part 2: none.

## Final count

136 data rows (134 before, plus L135 and L136), 137 lines with the header.
