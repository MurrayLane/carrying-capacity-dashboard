// Extracts the data behind the "2011-thesis" release from the original modelling folder:
//   data/2011-thesis/defaults-short-term.csv, defaults-long-term.csv   the inputs used for the thesis runs (Results/Totals.xls)
//   data/2011-thesis/timber-yield-by-region.csv                        Yield row 138, per region (Results/21b.xls, June 2012 model)
//   baseline/thesis_totals_capacity.csv                                the capacities Totals.xls reports, the release's acceptance test
// Usage: MODELS_DIR=/path/to/Models node analysis/model_archive/extract_thesis_release.mjs   (from the repository root)
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', '..');
const XLSX = createRequire(path.join(root, 'web') + '/')('xlsx');
const models = process.env.MODELS_DIR; if (!models) throw new Error('set MODELS_DIR');
const tot = XLSX.read(fs.readFileSync(path.join(models, 'Results/Totals.xls')), { type: 'buffer' });
const nameCsv = Object.fromEntries(fs.readFileSync(path.join(root, 'data/2011/default-inputs-short-term.csv'), 'utf8').trim().split(/\r?\n/).slice(1).map(l => { const c = l.split(','); return [c[0], c.at(-1)]; }));
const HEAD = 'regionId,cropping,pasture,nonAg,infrastr1,nature1,resilience,food,meategg,redmeat,activity,recycling,losses,organic,irrigation,fuel,biofuel,fibre,fibreNat,fibreWool,timber,infrastr2,nature2,population,totalArea,regionName'.split(',');
const ROW = { cropping: 3, pasture: 5, nonAg: 7, infrastr1: 9, nature1: 11, resilience: 13, food: 14, meategg: 15, redmeat: 16, activity: 17, recycling: 18, losses: 19, organic: 20, irrigation: 21, fuel: 22, biofuel: 23, fibre: 24, fibreNat: 25, fibreWool: 26, timber: 27, infrastr2: 28, nature2: 29, population: 30, totalArea: 31 };
const caps = ['preset,regionId,capacity'];
for (const [sn, preset] of [['SHORTtotals', 'short'], ['LONGtotals', 'long']]) {
  const s = tot.Sheets[sn]; const at = (r, c) => s[XLSX.utils.encode_cell({ r, c })]?.v; const lines = [HEAD.join(',')];
  for (let c = 2; c < 80; c++) {
    const id = at(2, c); if (id == null || /Noosa/.test(at(1, c))) continue;       // column 62 is a custom Noosa Biosphere region, not one of the 60 zones
    const rid = Math.round(id);
    lines.push(HEAD.map(k => k === 'regionId' ? rid : k === 'regionName' ? nameCsv[rid] : at(ROW[k], c)).join(','));
    caps.push(`${preset},${rid},${at(35, c)}`);
  }
  fs.writeFileSync(path.join(root, 'data/2011-thesis', `defaults-${preset}-term.csv`), lines.join('\n') + '\n');
}
fs.writeFileSync(path.join(root, 'baseline/thesis_totals_capacity.csv'), caps.join('\n') + '\n');
const run = XLSX.read(fs.readFileSync(path.join(models, 'Results/21b.xls')), { type: 'buffer' }).Sheets.Yield;
const ty = ['regionId,timberYieldPerM2'];
for (let c = 7; c <= 66; c++) ty.push(`${c - 6},${run[XLSX.utils.encode_cell({ r: 137, c })].v}`);
fs.writeFileSync(path.join(root, 'data/2011-thesis/timber-yield-by-region.csv'), ty.join('\n') + '\n');
console.log('wrote data/2011-thesis (3 files) and baseline/thesis_totals_capacity.csv', caps.length - 1, 'cases');
