// Long-term capacity of Australia (release 2025-resilience) for each re-derived fuel figure of scenarios.csv (all of it biofuel, as in the long-term settings).
//   node analysis/fuel_sectors_2025/capacity.mjs OUT.csv          (needs the built data: cd web && node scripts/build-data.mjs)
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const d = new URL('../../web/public/data/2025-resilience/', import.meta.url).pathname;
const ev = new Evaluator(JSON.parse(fs.readFileSync(d + 'model.json'))), R = JSON.parse(fs.readFileSync(d + 'regions.json')).regions[1];
const run = f => Math.round(ev.evaluate(R, { ...R.land, ...R.presets.long, fuel: f, biofuel: 1, population: R.population }).capacity);
const rows = fs.readFileSync(new URL('./scenarios.csv', import.meta.url).pathname, 'utf8').trim().split(/\r?\n/).slice(1).map(l => l.split(','));
const out = ['scenario,litres_a_person_long_term,capacity'];
for (const r of rows) { const name = r[0].replace(/^"|"$/g, ''); out.push([`"${name}"`, r[3], run(+r[3])].join(',')); }
out.push(['"current default (253 L)"', 253, run(253)]);
fs.writeFileSync(process.argv[2], out.join('\n') + '\n'); console.log(out.join('\n'));
