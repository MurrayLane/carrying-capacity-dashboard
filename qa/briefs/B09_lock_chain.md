# Builder brief B09: close the lock gap and refresh the results index

Rules: change only the files named here; read anything; no subagents; no network; plain language; do not run git. Repository root /home/user/carrying-capacity-dashboard. Standing decisions: the frozen releases' numbers must not change; if any result value changes at any step, stop and report it, do not "fix" it.

Edit: `web/scripts/releases.mjs` (the `inputFiles` function) so that the set of input files of a release also includes `releases/<id>/release.json` for the release itself and for every release in its `extends` chain (down to the root), and the `method.json` of every method module it uses if not already included. Read `lock-release.mjs` and `build-data.mjs` (the `lockDrift` check) first so the change fits them. Then:
1. From `web/`, run `node scripts/lock-release.mjs <id>` for each of `2011-corrected`, `2011-fixed`, `2011-improved`, `2025-mirror`, `2025-fixed`, `2025-improved`. Each release is already locked, so the script will refuse because the input set changed; that refusal is expected and is the one case where `--force` is right here (the releases were frozen today and have not been published). Use `--force` for exactly these six and report the new input count for each.
2. From `web/`, run `npm run results` (about a minute) so `results/releases.json` reflects the frozen status. Then run `git -C .. diff --stat results/` and report it. Every `results/*.csv` must be unchanged; if any csv differs, report the diff and stop.
3. From `web/`, run `npm test` and report the pass and fail counts.
Report: the diff of releases.mjs in words, the six new input counts, the results diff, the test counts, and anything surprising.
