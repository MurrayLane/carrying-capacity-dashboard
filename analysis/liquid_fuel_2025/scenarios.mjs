// Long-term capacity of Australia (release 2025-resilience) for residual liquid fuel per person and the share of it grown as biofuel on the land.
//   node scenarios.mjs OUT.csv          (needs the built data: cd web && node scripts/build-data.mjs)
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const d = new URL('../../web/public/data/2025-resilience/', import.meta.url).pathname;
const ev = new Evaluator(JSON.parse(fs.readFileSync(d + 'model.json'))), R = JSON.parse(fs.readFileSync(d + 'regions.json')).regions[1];
const run = pre => Math.round(ev.evaluate(R, { ...R.land, ...R.presets.long, ...pre, population: R.population }).capacity);
const out = ['fuel_litres,biofuel_share,capacity'];
for (const f of [253, 500, 750, 837, 1000, 1250, 1500, 1694, 2000]) for (const b of [0, 0.1, 0.2, 0.3, 0.44, 0.5, 1]) out.push([f, b, run({ fuel: f, biofuel: b })].join(','));
fs.writeFileSync(process.argv[2], out.join('\n') + '\n'); console.log('wrote', out.length - 1);
// The model charges land only for the biofuel part of the fuel, so capacity depends on litres of biofuel per person (fuel x share); fuel with no biofuel costs no land in the model.
const lb = ['biofuel_litres_per_person,capacity'];
for (const b of [0, 100, 200, 253, 340, 365, 500, 750, 1000]) lb.push([b, run({ fuel: Math.max(b, 1), biofuel: b ? 1 : 0 })].join(','));
fs.writeFileSync(process.argv[2].replace('scenarios.csv', 'biofuel_litres.csv'), lb.join('\n') + '\n');
