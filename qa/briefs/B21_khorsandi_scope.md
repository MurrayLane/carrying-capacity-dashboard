# Builder brief B21: scope an eighth method test, Khorsandi et al. 2022 on Australian 2025 data (decision 24)

Scoping only: no run, no new analysis files. Write only `qa/reports/B21_khorsandi_scope.md`; use /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/b21 for working files; no git; no subagents; web fetch allowed to re-open the two papers; plain language; no time words; sizes as quick, small or session-size, never hours.

Read first: the Khorsandi section of `qa/reports/B17_reading.md`; then Khorsandi, Homayouni and van Oel 2022 (Science of the Total Environment 817: 153038, doi 10.1016/j.scitotenv.2022.153038) and Khorsandi, Bateni and van Oel 2023 (Heliyon 9: e15079, doi 10.1016/j.heliyon.2023.e15079), full text if reachable. Then the pattern of the existing method tests: `analysis/method_tests_2025/README.md` (the opening and one test section) and one script there, for how each test is built (inputs, the author's own figure as a fidelity check, the Australian reading).

Answer, with the evidence from the papers:
1. **The method, step by step**, as Khorsandi 2022 computes a capacity: the three bounds (suitable land, water for evapotranspiration, realistic yield through HANPP at 25% of NPP and 3,000 kcal a day), the nine scenarios and the four scales, and the 2023 simple formula. Every constant with its page.
2. **What the method needs** as data for Australia, and what the repository already holds: look at `data/sa2/` (there are GAEZ arable-share files by SA2 and land-type files), `web/public/data/<release>/`, and `analysis/SOURCES.md`. For each need say: on hand (file), derivable (from what), or to be obtained (name the public source: for example GAEZ v4 suitability, Bureau of Meteorology or ABS water accounts, MODIS or other NPP).
3. **The fidelity check**: which figure of theirs (Iran, 130.2 or 76.8 or 35.5 or 20.2 million) could be reproduced from public data, and what that would take.
4. **The Australian reading**: at which scales the test could run (nation, states, the 53 regions, SA2) to match the scale curve of the results paper, and what it would compare against.
5. **Where it differs from the thesis method** (resource-based land and diet balance): what it sees that the thesis method does not (water, suitability, an NPP ceiling) and what it does not see (the pairing of pasture and crops, a diet, weather).
6. **Size and risk**: quick, small or session-size for each of (a) the simple 2023 formula on data on hand, (b) the land-suitability bound, (c) the water bound, (d) the HANPP bound; what could make the test misleading for Australia (rangeland, irrigation, exports).
7. A recommendation in one paragraph: run it, run only the simple form, or catalogue only; with the reason.
