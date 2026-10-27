// Evaluates sensitivity variants on release 2025-organic.   node evaluate.mjs VARIANTS.json OUT.csv     (needs the built data: cd ../../web && node scripts/build-data.mjs)
// A variant: { id, group, label, matrix?: path to a yield matrix csv, presets?: {short:{}, long:{}}, zonePresets?: {zone:{short:{}, long:{}}}, land?: {zone:{field:value}}, modelCells?: {A1: value}, release?: id }
// Output: capacity of Australia and the seven state zones, short- and long-term, for the base (variant "base") and every variant.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const [specFile, outFile] = process.argv.slice(2);
const dataDir = new URL('../../web/public/data/', import.meta.url).pathname;
const load = id => ({ model: JSON.parse(fs.readFileSync(dataDir + id + '/model.json')), data: JSON.parse(fs.readFileSync(dataDir + id + '/regions.json')) });
const cache = {}; const rel = id => cache[id] ??= load(id);
const decode = a => { const m = a.match(/^([A-Z]+)(\d+)$/); let c = 0; for (const ch of m[1]) c = c * 26 + ch.charCodeAt(0) - 64; return `${+m[2] - 1}:${c - 1}`; };
const ZONES = [1, 2, 15, 26, 40, 49, 56, 60];
const spec = JSON.parse(fs.readFileSync(specFile));
const evCache = new Map();
const out = ['id,group,label,zone,preset,capacity'];
for (const v of [{ id: 'base', group: 'base', label: 'base (release 2025-organic)' }, ...spec]) {
  const R = rel(v.release ?? '2025-organic'); const regions = structuredClone(R.data.regions);
  if (v.matrix) {
    const lines = fs.readFileSync(v.matrix, 'utf8').trim().split(/\r?\n/), head = lines[0].split(',').slice(1).map(Number);
    for (const l of lines.slice(1)) { const c = l.split(','); const reg = regions[+c[0]]; head.forEach((row, i) => { reg.yield[R.data.yieldRows.indexOf(row)] = +c[i + 1]; }); }
  }
  let model = R.model;
  if (v.modelCells) { model = structuredClone(R.model); for (const [a, val] of Object.entries(v.modelCells)) model.sheets.Yield.cells[decode(a)] = val; }
  const key = JSON.stringify(v.modelCells ?? null) + (v.release ?? ''); if (!evCache.has(key)) evCache.set(key, new Evaluator(model)); const ev = evCache.get(key);
  for (const z of ZONES) {
    const r = regions[z]; const land = { ...r.land, ...(v.land?.[z] ?? {}) };
    for (const p of ['short', 'long']) {
      const preset = { ...r.presets[p], ...(v.presets?.[p] ?? {}), ...(v.zonePresets?.[z]?.[p] ?? {}) };
      out.push([v.id, v.group, `"${v.label}"`, z, p, Math.round(ev.evaluate(r, { ...land, ...preset, population: r.population }).capacity)].join(','));
    }
  }
}
fs.writeFileSync(outFile, out.join('\n') + '\n'); console.log('wrote', out.length - 1, 'rows');
