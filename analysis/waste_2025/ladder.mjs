// Capacity of Australia and four states for steps of avoidable food waste and recycling, short and long term (release 2025-fuel, the tip of the 2025 chain).
//   node analysis/waste_2025/ladder.mjs OUT.csv          (needs the built data: cd web && node scripts/build-data.mjs)
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const d = new URL('../../web/public/data/2025-fuel/', import.meta.url).pathname;
const ev = new Evaluator(JSON.parse(fs.readFileSync(d + 'model.json'))), D = JSON.parse(fs.readFileSync(d + 'regions.json')).regions;
const out = ['setting,zone,losses,recycling,capacity'];
for (const k of ['short', 'long']) for (const z of [1, 2, 15, 26, 49]) { const R = D[z];
  for (const l of [0.20, 0.14, 0.12, 0.09, 0.06, 0.03, 0]) for (const r of [0, 0.5, 1])
    out.push([k, z, l, r, Math.round(ev.evaluate(R, { ...R.land, ...R.presets[k], losses: l, recycling: r, population: R.population }).capacity)].join(',')); }
fs.writeFileSync(process.argv[2], out.join('\n') + '\n'); console.log('wrote', out.length - 1);
