# Checker brief V33: blind check of the North East Victoria correction (decision 84)

You are a blind checker. `qa/briefs/_checker_rules_results_wave.md` applies: tolerance first; one deliberate wrong value shown failing; the builder's report `qa/reports/B90_ne_vic_population.md` and its changed files opened only at the end. Plain language; no time words; no em dashes. No git; no subagents; no network. Write only `qa/reports/V33_ne_vic_check.md`.

Your own route: from the ABS 2011 source the sources register names for zone populations (or the SA2 ERP sum for the zone's SA2s from the stored cubes in `/home/user/carrying-capacity-models/data/abs_cubes/` and `data/sa2/`), derive North East Vic's 2011 population and Goulburn Broken's. Then, with the evaluator (`web/src/model/evaluator.js`) on the corrected 2011 release as it now stands, compute North East Vic's and Goulburn Broken's short- and long-term capacities and statuses, and the national over-capacity counts and the three "clean" flips, by your own script. Only then open B90's report and the changed files and compare: the population figure; every changed output cell; the list of claim rows B90 says move, with their before and after values. Say which Tier A rows move and by how much.

Report: tolerance; wrong-value example; your figures; the comparison; pass or fail per item; the register rows touched (none).
