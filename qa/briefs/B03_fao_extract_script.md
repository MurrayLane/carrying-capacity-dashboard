# Builder brief

You are a builder helper. The coordinator (the main session) wrote this brief and will review your work, so do not try to decide what anything means.

Rules, no exceptions:
* Write only the file(s) named under "Write". Read anything else, change nothing else. Do not run git; the coordinator commits.
* Do not change any result, script or data file. Do not spawn subagents.
* Never invent. If you cannot establish a field, write `unknown` and list it in your report. Copy citations and titles exactly as you find them and record where you found them.
* Every row must rest on something you opened (a file, a page). A path in a row means the file exists: check it.
* Plain, specific notes. No time words (tonight, later, for now, not urgent).
* Repository root: /home/user/carrying-capacity-dashboard (public). The private archive is /home/user/carrying-capacity-models; refer to its files as `carrying-capacity-models/<path>`. Both exist on this machine.

Standing decisions you must not reopen: two papers only; the methods paper tests each method on Australian 2025 data and gives no reproduction gate; corrected values are assumed; the results paper gives 2011 as corrected only. Read `qa/CARD.md` and `qa/README.md` (the schemas) first.
Report format (your final message): (1) what you wrote and the row count; (2) every field or row you could not establish; (3) anything surprising or that looks wrong in the project's own documents; (4) rows a human should check first.

## Task B03: the missing FAO extract script

Write: `analysis/method_tests_2025/extract_fao_au_production.py` (new file) and, if and only if the regenerated file is byte-identical to the existing one, nothing else. Do NOT overwrite `analysis/method_tests_2025/fao_au_production_1997_2023.csv`. Write your regenerated copy to the scratchpad and compare with `cmp`.

The file `fao_au_production_1997_2023.csv` (header `Area,Item,Element,Year,Unit,Value`) was cut from the FAOSTAT bulk file `Production_Crops_Livestock_E_All_Data_(Normalized).csv`, which is unpacked at `/tmp/claude-0/fao/q/` on this machine (sha256 of the csv c4ff713e4b8e0f30eadf5a37632ede4faf95bb8e60c12becd16ef793b0cbac01; confirm it). The rule that produced it: Area is Australia, Element is Production, Item is one of `Cereals, primary`, `Meat, Total`, `Pulses, Total`, Year is one of 1997, 1998, 2021, 2022, 2023; columns in the order of the header. Follow the style and header docstring of `extract_fao_countries.py` in the same folder (usage line with the bulk file as an argument, source URL, FAO licence CC BY 4.0, file date 2025-12-23). Run it with `python3 -I`, passing paths as arguments. Report whether the output is byte-identical; if it is not, report the diff and do not guess at a fix.
