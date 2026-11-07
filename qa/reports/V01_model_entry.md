# V01 verification report: the model's own entry (Opus checker, read-only, blind to expected values), 2026-11-07

Requirement: for Australia on the three frozen releases 2025-mirror, 2025-fixed and 2025-improved, establish independently the short- and long-term capacities, the input lock, and the Monte Carlo 5th and 95th percentiles from the raw draws.

**R1 capacities: holds, all six.** Built files match the hashes in results/releases.json; the checker's own evaluation with the evaluator gives, to the person, 49,389,414 / 14,146,847 (mirror), 41,503,537 / 15,623,209 (fixed), 53,643,731 / 18,496,334 (improved), equal to results/<id>.csv and to the `base` column of the ranges files.

**R2 lock: holds for the listed files** (4, 6 and 13 input files; hashes recomputed with hashlib; lockDrift empty). Qualification below.

**R3 percentiles: holds, all twelve.** Draws files have 1,000 rows each, no missing values; linear-interpolation percentiles equal the ranges files exactly (p50 too); nearest-rank would differ by 6,000 to 27,000 at p5, so the method is identifiable.

**What the check could not catch (the checker's own statement).** The evaluation and the ranges come from the same evaluator and built model that produced the outputs, so an error in the evaluator, the build or the draws would appear on both sides and pass. The models were not rebuilt from the locked inputs and no draw was re-evaluated. A second, independent implementation (layer 3 of the plan) is still required for these numbers.

**Surprising (defects X027 to X029).**
1. The lock does not cover the release definitions a frozen release inherits (the chain 2025-diet to 2011 and the frozen release's own release.json carry patches and cell overrides and are not hashed): editing a patch in an upstream release.json would change a frozen release's result without lockDrift noticing.
2. results/releases.json says "current" for the three releases; their release.json files say "frozen" (the results index was generated before the freeze).
3. The built models on disk (2026-11-07) are newer than the results csvs (2026-11-03) and the draws (2026-11-04); the values agree exactly, but the draws were not necessarily made with the build on disk; and the draws' release is identified by file name and matching base, not by a recorded command.

Working files: scratchpad v01/ (drift.mjs, eval.mjs, pct.py).
