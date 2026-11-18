# Referee report, third round: "Well-known carrying-capacity methods tested on common Australian data" (Paper B, methods)

Reviewer standpoint: quantitative modeller of food systems and land use, returning from round two (R04d). Read: my round-two report, `response_letter_round2.md`, and `paper_B_draft1.md` (drafter notes ignored), `supplementary.md` and `highlights.md`, concentrating on the sections the letter names.

## 1. Recommendation

**Minor revision.** The analyses I asked for now exist, and the text now reports them candidly; what remains is chiefly how the bridge's result is worded in the abstract and highlights, plus presentation gaps that block acceptance on their own.

## 2. Round-two major points

**M1 (constructed capacities). Partly answered; acceptable.** Sections 4.3, 4.5, 5.5 to 5.7 and 5.11 now say method by method that the capacity reading is this study's, and the letter's correction is fair: the footprint gives no count of people in its authors' hands. Closure for the energy balance alone (8.2%) is in Table S5. The fish reading stays in the base case, with a variant without it (5.9% and 40.9%); that is acceptable. One gap: the abstract still says "the aggregate methods give about 65 to 211 million" with no word that three of these are readings this study constructs.

**M2 (harmonisation). Partly answered.** Table S10 is the table I asked for; line (c) is run (14.7%, band 10% to 16%), and the abstract and 5.1 now say "a common land base and food balance", the model keeping its own layer. The population point was my error. The refusal to run the model on FAOSTAT is reasoned (zone-level ABS series against national totals) and I accept it, but S3.13 shows the cost: the meat inputs, "which set the output on the binding land", carry a thesis calibration (cattle x1.086, sheep x1.155) and "could not be compared because the ABS tables are not on disk". A one-input check (national beef and sheep meat from FAOSTAT in place of the calibrated ABS series) would not need the full layer.

**M3 (anchoring). Answered; text matches the letter.** Table 6 leads with spread measures, the method centre is defined (geometric mean), Table S5 gives the leave-out variants, and 5.11 says the line (b) closure is "mostly (about 87%) the productivity conversion of the footprint and HALF"; The 87% checks against S3.11. Highlight 2 is now plain.

**M4 (attribution). Partly answered.** The bridge (Table 7, panel B; S3.12) is exactly what I asked for and well done, including the honest note that requirement and waste cannot be separated. The protein-held variant (85.4 million) is run. But the conclusion drawn from it is stronger than the bridge supports (section 3 below).

**M5 (binding parameter). Partly answered; acceptable with the reason given.** My premise was partly wrong: pasture output is national meat output shared by DSE, so its window and calibration are drawn (S5). The ±20% illustration (33.4 to 49.5, factor 1.48) and the NHMRC range (1.78) now sit in Table 8 beside the 1.58, so the definitions-versus-settings ordering is no longer presented as built in. The drought point is fully answered: 5.8 gives the crop-only bound and says "the failure view does not cover the binding constraint". Not redrawing the Monte Carlo with pasture output is acceptable now that 6.11 places 1.58 below the NHMRC energy range and close to the pasture illustration.

**M6 (fidelity). Partly answered.** Daggers in Table 3 and section 8.6 name the failures. The authors were not contacted, and the letter still carries an unresolved bracket asking the author whether requests were sent; section 5.2 now reads "had not been consulted at the time of writing", which implies contact may follow. Declining the national footprint accounts is acceptable if 5.4 gives the reason the letter gives (no Australian row on the public platform, licence outside scope); the paper does not yet say it.

**M7 (independence). Partly answered; acceptable.** Table 9 is now the author's judgement, as I offered, with no rating claim in the abstract, and section 7.1 says "the table is not offered as a finding". The design choices are not rerun in a second method; panel B and section 7.7 (land base, 31% in the energy balance) partly cover this. Acceptable given the reframing.

**M8 (presentation). Partly answered; not acceptable for acceptance.** Regeneration notes and the mixed range are gone. Still open: Table 2 and Figures 1 to 3 are placeholders (Table 2 "to be built from a catalogue csv that does not exist"); the AI declaration and CRediT carry brackets; section 9.4 says the archive has no DOI; S3.14 and Table S15 still cite internal `qa/` paths. The letter itself contains two "[For the author: ...]" notes.

**M9 (literature). Partly answered.** Gerten et al. 2020 and Fader et al. 2013 are cited directly. "No copy held" is a reason about the author's library, not about the field; Mottet et al. 2017 on feed-food competition bears directly on the pasture argument and should be obtained. I would not hold acceptance on the rest.

## 3. New problems the revision introduced

1. **"Sufficient cause" outruns the bridge.** Section 5.14 states "The pairing is a sufficient cause of the gap, not shown to be the only one", and the abstract, highlight 4 ("The pasture-crop pairing is enough to close the gap to HALF"), 7.6 and 9.1 repeat it. The bridge says something different: in HALF's own currency the pooling rule is 6.3 of the 34.5 million (18%), and switched last (reverse column, if that is how it is ordered) it moves the model by only 5.4 million. The gap closes only when pasture-fed food is replaced at equal energy (variant 1, k = 91.3, protein falling to 81 g) or equal protein (k = 145.6). Sufficiency is therefore a property of the substitution rate, which is a diet assumption, not of the pairing alone.

2. **The target is on a different requirement basis.** HALF's 76.0 and the footprint's 64.8 to 117.0 divide by FAO supply (13.6 to 14.8 MJ with waste inside); the model and variant 1 use 8.0 MJ eaten with waste charged. On line (c), which the paper itself defines, HALF becomes about 115 million (76.0 x 1.512), and variant 1's 81.7 no longer reaches it. The "1.6 to 2.8 times the model" in highlight 3 and section 5.10 carries the same asymmetry.

3. **What the model's short term measures.** S5 now says pasture output is national meat output and that "a 20% error carries to capacity almost one for one". Together with the land-base factor of 1.09, this means the short-term reading is, to first order, current national pasture-fed output (exports included) divided by the diet's pasture-fed food a person. That would explain why the commodity balance's meat reading (40 to 41 million) sits on the model's 41.5. The paper should say so in 6.2, since it changes what "land carrying capacity" means for the binding constraint.

4. **Small inconsistencies.** S7 says "the model's two columns are one model read two ways", but Table 9 now has one model column. The letter's "14.7% of the 38.5% survives" misstates line (c), which closes 14.7% of the distance, not 14.7% of 38.5%.

## 4. Minor points still open

- Minor 2: the waste factor of 1.33 against a 1.14 ceiling remains untraced; waste is a ranked row in Table 8, so this should be explained or the row flagged.
- Minor 3: S4 says the doubling of pasture between 5% and 7.5% meat "has not been checked", yet the cliff in 6.5 rests on it.
- Minor 13: "balance" still names three different things in section 7.
- Minor 14: S3.11 gives 1,912 and 2,892 kcal without MJ.

## 5. Three changes before acceptance

1. In the abstract, highlight 4, sections 5.14, 7.6 and 9.1, replace "sufficient cause" and "enough to close the gap" with: "relaxing the pairing closes the gap to HALF when pasture-fed food is replaced at equal energy or protein (81.7 and 85.4 million); at HALF's own land exchange rate the pooling rule accounts for 18% of the gap."
2. In section 5.10, section 5.14 and highlight 3, add beside the 1.6 to 2.8 multiples the line (c) multiples (readings x 1.51), with one sentence that on a common requirement and waste HALF reads about 115 million, above variant 1.
3. Supply Table 2 and Figures 1 to 3, fill the AI declaration and CRediT brackets, deposit the archive with a DOI, and remove the `qa/` paths from S3.14 and Table S15.

## 6. Further round

Yes, one short round. The figures and Table 2 have never been seen by a referee, and the wording of the pairing result appears in the abstract and highlights, so I would want to read the final text; no new analysis is required beyond the optional meat-input check in M2.
