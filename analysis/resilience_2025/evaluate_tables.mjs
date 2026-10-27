// Long-term capacity of the 2025-organic release with each resilience table of tables.csv, at the long-term setting (100 years) and at 20 and 50 years.
//   node evaluate_tables.mjs OUT.csv          (needs the built data: cd web && node scripts/build-data.mjs)
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const d = new URL('../../web/public/data/2025-organic/', import.meta.url).pathname;
const model = JSON.parse(fs.readFileSync(d + 'model.json')), data = JSON.parse(fs.readFileSync(d + 'regions.json')).regions;
const ev = new Evaluator(model), sid = ev.hf.getSheetId('resilience');
const ROW = { 'Australia': 2, 'New South Wales': 3, 'Victoria': 4, 'Queensland': 5, 'South Australia': 6, 'Western Australia': 7, 'Tasmania': 8 };      // sheet rows 3 to 9 (0-based 2 to 8); the Northern Territory (row 10) copies South Australia
const lines = fs.readFileSync(new URL('./tables.csv', import.meta.url).pathname, 'utf8').trim().split(/\r?\n/).slice(1).map(l => l.split(','));
const methods = [...new Set(lines.map(l => l[1]))];
const ZONES = [1, 2, 15, 26, 40, 49, 56, 60], out = ['method,zone,years,capacity'];
const run = (z, years) => { const R = data[z]; return Math.round(ev.evaluate(R, { ...R.land, ...R.presets.long, resilience: years, population: R.population }).capacity); };
// the model's own table first, as a check
for (const z of ZONES) for (const y of [20, 50, 100]) out.push(['model table', z, y, run(z, y)].join(','));
for (const m of methods) {
  for (const l of lines.filter(l => l[1] === m)) { const row = ROW[l[0]]; for (let t = 1; t <= 150; t++) ev.hf.setCellContents({ sheet: sid, row, col: 1 + t }, [[+l[1 + t]]]); if (l[0] === 'South Australia') for (let t = 1; t <= 150; t++) ev.hf.setCellContents({ sheet: sid, row: 9, col: 1 + t }, [[+l[1 + t]]]); }
  for (const z of ZONES) for (const y of [20, 50, 100]) out.push([`"${m}"`, z, y, run(z, y)].join(','));
}
fs.writeFileSync(process.argv[2], out.join('\n') + '\n'); console.log('wrote', out.length - 1);
