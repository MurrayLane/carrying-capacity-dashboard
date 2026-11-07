# Verifier brief V06: the commodity balance (Foran and Poldy 2002) on current data

You are an independent checker doing a second implementation. You receive the method's published description and the data, and nothing else. Do NOT open any file under `analysis/method_tests_2025/` except the data extracts named below, nor `qa/claims_register.csv`, `papers/`, `HANDOFF.md`, or `analysis/comparators_2025/`: they contain an earlier implementation and its results. If you open one by accident, say so.

Hard limits: read only inside /home/user/carrying-capacity-dashboard and /home/user/carrying-capacity-models; write only under /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/<brief id>/ (create it). No git changes, no subagents, no network. Plain language; no time words.

## Requirement
From Foran and Poldy (2002), Future Dilemmas, CSIRO Resource Futures Working Paper 02/01, chapter 2 (the full report: `/home/user/carrying-capacity-models/Comparators/Foran-Poldy-2002-Future-Dilemmas-full-report-02-01.pdf`, text extractable; see Table 1.1 for the population scenarios and Table 2.5 and its text for the food requirements, production and embodied feed grain), state the balance they computed and reproduce it from their own numbers. Then derive the requirement per person for grain, meat and fish in the base case, and apply it to current Australian production (cereals and meat from `analysis/method_tests_2025/fao_au_production_1997_2023.csv`, mean 2021-23; fish production from the food balance extract `analysis/method_tests_2025/fbs_au_world_2021_23.csv`) to give the people each commodity would feed on its own, with and without the embodied feed grain. Also check their 1997-98 production figures against the FAO values for 1997 and 1998 in the production file.

## Report format
Your reading of their balance; the per-person requirements; the people fed by grain (direct; with embodied feed grain), meat and fish on 2021-23 production; the 1997-98 check; every choice; what could be wrong; anything surprising.
