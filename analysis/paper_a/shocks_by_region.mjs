// Paper A section 8: the regions under a bad year. For the 52 NRM regions and the Northern Territory (the 53 regions of movers.csv), corrected method, both vintages:
// capacity at drought return periods of 1 (average year), 5, 10, 20, 50 and 100 years, short-term settings, against the release's own population.
//   node analysis/paper_a/shocks_by_region.mjs OUT.csv      (repository root; needs the built data)
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const out = process.argv[2], base = new URL('../../web/public/data/', import.meta.url).pathname;
const rows = ['release,zone,name,kind,return_period,capacity,population'];
for (const id of ['2011-fixed-2', '2025-fixed']) {   // 2011-fixed-2: 2011-fixed with North East Vic's 2011 population corrected (error 8 of ERRATA.md); capacities are 2011-fixed's
  const model = JSON.parse(fs.readFileSync(`${base}${id}/model.json`)), regions = JSON.parse(fs.readFileSync(`${base}${id}/regions.json`)).regions, ev = new Evaluator(model);
  for (const [z, R] of Object.entries(regions)) {
    if (!(R.kind === 'region' || z === '60' || z === '1')) continue;
    for (const T of [1, 5, 10, 20, 50, 100]) {
      const cap = ev.evaluate(R, { ...R.land, ...R.presets.short, resilience: T, population: R.population }).capacity;
      rows.push([id, z, JSON.stringify(R.name), R.kind, T, Math.round(cap), R.population].join(','));
    }
  }
}
fs.writeFileSync(out, rows.join('\n') + '\n'); console.log(rows.length - 1, 'rows');
