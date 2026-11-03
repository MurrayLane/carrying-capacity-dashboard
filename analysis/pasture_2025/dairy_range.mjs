// Range for the dairy-good-land module (methods/dairy-good-land): capacity with each zone's dairy yield as observed on dairy farms (the module) and with the yield halved. The halved case stands for two limits of the
// observed figure that cannot be separated with the data in hand: the feed the farms buy in (50 to 62% of their feed energy is grown on the usable area, so counting the rest at the same yield roughly halves the yield)
// and the sample's farms being larger and more productive than the average farm (the states' milk per farm is about 55 to 65% of the sample's). Takes the built release and rescales Yield row 97. Writes results/dairy_range.csv.
//   cd web && node ../analysis/pasture_2025/dairy_range.mjs        (after npm run build:data)
import fs from 'node:fs'; import path from 'node:path';
import { root, methodModule } from '../../web/scripts/releases.mjs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const D = methodModule('dairy-good-land').dairyGoodLand, FACTORS = [['yield_as_observed', 1], ['yield_halved', 0.5]];
const out = [['release', 'preset', 'zone', 'name', 'population', ...FACTORS.map(f => f[0])]];
for (const id of ['2011-improved', '2025-improved']) {
  const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), RJ = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))), k = RJ.yieldRows.indexOf(D.yieldRow), ev = new Evaluator(model);
  for (const z of Object.values(RJ.regions).sort((a, b) => a.id - b.id)) for (const preset of ['short', 'long']) {
    const cap = f => { const y = z.yield.slice(); y[k] *= f; return ev.evaluate({ ...z, yield: y }, { ...z.land, ...z.presets[preset], population: z.population }).capacity; };
    out.push([id, preset, z.id, z.name, z.population, ...FACTORS.map(([, f]) => cap(f))]);
  }
}
fs.writeFileSync(path.join(root, 'results', 'dairy_range.csv'), out.map(r => r.map(v => typeof v === 'number' ? Math.round(v) : v).join(',')).join('\n') + '\n');
for (const r of out.slice(1).filter(r => [1, 2, 15, 26, 40, 49, 56, 60].includes(r[2]))) console.log(r[0], r[1], String(r[3]).padEnd(10), 'as observed', (r[5] / 1e6).toFixed(2), ' halved', (r[6] / 1e6).toFixed(2), ' pop', (r[4] / 1e6).toFixed(2));
