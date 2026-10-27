// Capacity of release 2025-reserve against 2025-resilience, Australia and the seven state zones, short and long term.
//   node reserve_release.mjs OUT.csv          (needs the built data: cd web && node scripts/build-data.mjs)
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const dir = new URL('../../web/public/data/', import.meta.url).pathname;
const L = id => ({ m: JSON.parse(fs.readFileSync(`${dir}${id}/model.json`)), r: JSON.parse(fs.readFileSync(`${dir}${id}/regions.json`)).regions });
const a = L('2025-resilience'), b = L('2025-reserve'), ea = new Evaluator(a.m), eb = new Evaluator(b.m);
const run = (ev, R, k) => Math.round(ev.evaluate(R, { ...R.land, ...R.presets[k], population: R.population }).capacity);
const out = ['zone,short_resilience,short_reserve,long_resilience,long_reserve'];
for (const z of [1, 2, 15, 26, 40, 49, 56, 60]) out.push([z, run(ea, a.r[z], 'short'), run(eb, b.r[z], 'short'), run(ea, a.r[z], 'long'), run(eb, b.r[z], 'long')].join(','));
fs.writeFileSync(process.argv[2], out.join('\n') + '\n'); console.log(out.join('\n'));
