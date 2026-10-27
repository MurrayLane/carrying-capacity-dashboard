# Carrying Capacity Dashboard

An interactive estimate of how many people a region of Australia can support from its own
land, given choices about diet, waste, farming, fuel, fibre, timber, infrastructure and
nature reserve. Created by Murray Lane (thesis: https://eprints.qut.edu.au/67485/), first
published in 2011 with QUT. This repository is the maintained rebuild.

It is a static website: no server, no database. The Excel model is evaluated in the browser,
so it costs nothing to run and any scenario is a shareable link.

## How it works

- `model/model.xls` is the model: the workbook whose formulas do all the calculation.
- `data/2011/` holds the 2011 zone defaults (land use and population for 60 zones, short-term
  and long-term presets).
- `web/scripts/build-data.mjs` converts the workbook to `model.json` and the zone data to
  `regions.json` at build time, once per release. Each zone's yield vector is injected into the Yield sheet when
  that zone is evaluated.
- `web/src/model/` evaluates the workbook with HyperFormula in a Web Worker. Inputs go in
  Settings!B2:B25; results are read from B76 (carrying capacity), C84:D89 (excess land) and
  B91:E107 (land requirements).
- `releases/` holds the versions of the data and method. Each is frozen once published, so old links and citations reproduce
  exactly; see `releases/README.md`.
- `web/src/` is the interface (plain ES modules built with Vite). Scenario state lives in the
  URL hash.
- `baseline/` is the complete output of the original 2011 servlet for the 120 default cases.
  `web/test/baseline.test.js` replays every case through the browser evaluator and must match.
- `analysis/` holds the model audit, the yield conversion test and the irrigation review, each
  with its own README. Sources: `analysis/SOURCES.md`.
- `HANDOFF.md` is the current state, standing decisions and open items; start there when resuming.
- `SCOPE.md`, `DELIVERY.md` and `PUBLICATIONS.md` record the plan, the interface design and the
  planned papers.

## Build and test

Requires Node 22.

```bash
cd web
npm ci
npm test            # builds the data, then replays the 2011 baseline and the state tests
npm run dev         # local development server
npm run build       # production site in web/dist
```

## Publishing

`.github/workflows/pages.yml` tests, builds and deploys `web/dist` to GitHub Pages on every push
to `main`. Enable it once under Settings, Pages, Source: GitHub Actions.

## The original version

The Java servlet and Tomcat page that served the 2011 site are kept on the `legacy-java` branch.
The unmodified QUT snapshot is in history at commit `04a612e`.

## Licence

Code: MIT (`LICENSE`). Model workbook, data and results: CC BY 4.0 (`LICENSE-DATA.md`).
