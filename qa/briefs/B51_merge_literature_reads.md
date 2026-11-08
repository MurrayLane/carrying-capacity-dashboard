# Builder brief B51: merge the B50a reading into the registers

Edit only `qa/literature_register.csv` (keep line endings and all columns) and append to `qa/reports/B51_merge.md`. No git; no subagents; plain language. Source: `qa/reports/B50a_literature_full_texts.md` (its per-row updates: `read_or_reported` to "read", new `what_taken`, `notes`, `local_path`, sha256).

1. Apply the row updates for L075, L076, L085, L091 and L094 exactly as the report gives them; set `status` to `self-checked (B50a full text)`.
2. Fix the two characterisations the report found incomplete (L076: the condition includes "complemented by biodiversity-focussed domestic land-use policy"; L094: "enough food in the short term" covers export markets and allows import substitution) in those rows' `what_taken`.
3. Change L076's `used_by` from a section 5 comparator to section 6 context (yield path, time frame, land taken by plantings), and note Grundy et al. 2016 (Agricultural Systems 142: 70 to 83) as the closer food comparator in a new lead row (kind "journal article", status unverified, read_or_reported "not read (lead from Bryan 2016)").
4. Add a row for the PMSEIC 2010 estimate that Australia produces enough food for about 60 million people (quoted by Millar and Roots 2012, p. 26; counts exports), `read_or_reported` "reported (second-hand, Millar and Roots 2012 p. 26)", placed beside L011 and used by the methods paper's catalogue of estimates (section 4), with a note that the primary source (PMSEIC 2010, "Australia and food security in a changing world", p. 1) is to be read before use.
5. Fix the L073 note that pairs a local-food recommendation with Graymore 2010 (Graymore says nothing on local food production): reword to drop the pairing.
Report: the rows changed with old and new `what_taken`, the rows added, and the final row count.
