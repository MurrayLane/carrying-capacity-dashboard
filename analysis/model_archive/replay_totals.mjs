// Replays the thesis results workbook (Results/Totals.xls) through the site's evaluator.
// Usage: MODELS_DIR=/path/to/Models node replay_totals.mjs shipped|june
//   shipped  the model on the site (flat timber yield, Base!K348 = 0.5665)
//   june     the June 2012 variant behind the thesis: per-region timber yield from Results/21b.xls, Base!K348 = 0.3624
// Run from web/ after `npm run build:data` has written public/data/*.json.
import fs from 'fs';
import path from 'path';
import { createRequire } from 'module';
const web = new URL('../../web/', import.meta.url).pathname;
const XLSX = createRequire(web)('xlsx');
const { Evaluator } = await import(path.join(web, 'src/model/evaluator.js'));
const models = process.env.MODELS_DIR; if (!models) throw new Error('set MODELS_DIR');
const model = JSON.parse(fs.readFileSync(path.join(web, 'public/data/model.json')));
const { regions } = JSON.parse(fs.readFileSync(path.join(web, 'public/data/regions.json')));
const mode = process.argv[2] || 'shipped';
if (mode === 'june') {
  const run = XLSX.read(fs.readFileSync(path.join(models, 'Results/21b.xls')), { type: 'buffer', cellFormula: true });
  const y = run.Sheets.Yield;
  for (let c = 7; c <= 66; c++) regions[String(c - 6)].yield[134] = y[XLSX.utils.encode_cell({ r: 137, c })].v;   // Yield row 138, timber m3/ha
  model.sheets.Base.cells['347:10'] = 0.3624073982184083;                                                       // Base!K348
}
const tot = XLSX.read(fs.readFileSync(path.join(models, 'Results/Totals.xls')), { type: 'buffer' });
const ev = new Evaluator(model);
// Totals row index (0-based) -> input name
const ROWS = { 3: 'cropping', 5: 'pasture', 7: 'nonAg', 9: 'infrastr1', 11: 'nature1', 13: 'resilience', 14: 'food', 15: 'meategg', 16: 'redmeat', 17: 'activity', 18: 'recycling', 19: 'losses', 20: 'organic', 21: 'irrigation', 22: 'fuel', 23: 'biofuel', 24: 'fibre', 25: 'fibreNat', 26: 'fibreWool', 27: 'timber', 28: 'infrastr2', 29: 'nature2', 30: 'population' };
for (const sn of ['SHORTtotals', 'LONGtotals']) {
  const s = tot.Sheets[sn]; const at = (r, c) => s[XLSX.utils.encode_cell({ r, c })]?.v; const diffs = [];
  for (let c = 2; c < 70; c++) {
    const id = at(2, c), name = at(1, c); if (id == null || /Noosa/.test(name)) continue;   // column 62 is a custom Noosa Biosphere region, not one of the 60 zones
    const inputs = Object.fromEntries(Object.entries(ROWS).map(([r, k]) => [k, at(+r, c)]));
    const cap = at(35, c), got = ev.evaluate(regions[String(Math.round(id))], inputs).capacity;
    diffs.push([id, name, cap, got, (got - cap) / cap]);
  }
  const abs = diffs.map(d => Math.abs(d[4])).sort((a, b) => a - b);
  console.log(mode, sn, `${diffs.length} regions, median ${(abs[abs.length >> 1] * 100).toFixed(4)}%, max ${(abs.at(-1) * 100).toFixed(3)}%`);
}
