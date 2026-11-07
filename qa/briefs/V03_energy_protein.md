# Verifier brief V03: energy and protein balance (Henry and Godden 1995) on current Australian data

You are an independent checker doing a second implementation. You receive the method's published description and the data, and nothing else. Do NOT open any file under `analysis/method_tests_2025/` except the data extracts named below, nor `qa/claims_register.csv`, `papers/`, `HANDOFF.md`, or `analysis/comparators_2025/`: they contain an earlier implementation and its results. If you open one by accident, say so.

Hard limits: read only inside /home/user/carrying-capacity-dashboard and /home/user/carrying-capacity-models; write only under /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/<brief id>/ (create it). No git changes, no subagents, no network. Plain language; no time words.

## Requirement
(a) From Henry and Godden (1995), "A note on estimating Australia's sustainable population", Review of Marketing and Agricultural Economics 63(1): 97-103 (scanned: `/home/user/carrying-capacity-models/Comparators/Henry-and-Godden-1995-A-note-on-estimating-Australias-sustainable-population.pdf`; render pages with `pdftoppm -r 110 -png` and read them as images), state their recipe in your own words and reproduce their Table 5 figures for "contemporary excluding wool/cotton" from their own Table 2, Table 3 and Table 4 inputs.
(b) Apply the same recipe to current Australian production: the food energy and protein of domestic production (food products only; imports ignored; exports counted as food; feed, seed, non-food use, losses and processing removed), from the FAO food balance extract `analysis/method_tests_2025/fbs_au_world_2021_23.csv` (mean of 2021 to 2023; use FAO's own world food-supply kcal and protein per tonne of each item, from the World rows, as the energy and protein densities), scaled to Nix's 70 Mha over an in-use land figure you state, and divided by their consumption factors. Report people (million) on energy and on protein for: no scale-up; the 1990-91 in-use land (45.7 Mha) unchanged; and an in-use land of 1990-91 sown pasture (28.3 Mha) plus current cropping (31.65 Mha).
(c) State the total production energy (10^15 J) and protein (10^10 g) you obtain and the share from cereals.

## Report format
Your recipe; the reproduction of 109 and 96 (values and inputs); your three current-data readings on energy and protein; the totals; every choice you made (item list, densities, what counts as food); what could be wrong and how it would show; anything surprising.
