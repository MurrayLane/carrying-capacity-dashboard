// results/scenarios.csv: every named scenario of scenarios/scenarios.json for every zone and both presets, with the change from the reference scenario.
// A scenario is a release plus overrides of the settings of one or both presets (scenarios/scenarios.json).
// Usage: cd web && npm run build:data && node scripts/make-scenarios.mjs
import fs from 'node:fs';
import path from 'node:path';
import { root } from './releases.mjs';
import { Evaluator } from '../src/model/evaluator.js';
import { dataDir, PRESETS } from './results-lib.mjs';

const def = JSON.parse(fs.readFileSync(path.join(root, 'scenarios', 'scenarios.json'))), cache = {};
const load = id => cache[id] ??= { ev: new Evaluator(JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json')))), regions: JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions };
const run = s => {
  const { ev, regions } = load(s.release), out = new Map();
  for (const z of Object.values(regions).sort((a, b) => a.id - b.id)) for (const preset of PRESETS) {
    const p = { ...z.presets[preset], ...(s.settings?.[preset] ?? {}) }, r = ev.evaluate(z, { ...z.land, ...p, population: z.population });
    out.set(`${z.id}|${preset}`, { zone: z.id, name: z.name, kind: z.kind, preset, population: z.population, capacity: Math.round(r.capacity) });
  }
  return out;
};
const ref = run(def.scenarios.find(s => s.id === 'reference')), rows = [];
for (const s of def.scenarios) {
  const res = s.id === 'reference' ? ref : run(s);
  for (const [k, r] of res) { const b = ref.get(k).capacity; rows.push({ scenario: s.id, release: s.release, ...r, capacity_reference: b, change: r.capacity - b, change_pct: b ? +(100 * (r.capacity - b) / b).toFixed(2) : '' }); }
}
const cols = Object.keys(rows[0]), cell = v => /[",]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : v;
fs.writeFileSync(path.join(root, 'results', 'scenarios.csv'), [cols.join(','), ...rows.map(r => cols.map(c => cell(r[c])).join(','))].join('\n') + '\n');
console.log('scenarios.csv', rows.length, 'rows;', def.scenarios.map(s => s.id).join(', '));
for (const s of def.scenarios) { const a = rows.filter(r => r.scenario === s.id && r.zone === 1); console.log(s.id.padEnd(16), a.map(r => `${r.preset} ${(r.capacity / 1e6).toFixed(2)} (${r.change_pct}%)`).join('  ')); }
