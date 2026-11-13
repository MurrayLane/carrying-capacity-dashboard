// results/scenarios.csv: every named scenario of scenarios/scenarios.json for every zone and both presets, with the change from the reference scenario.
// A scenario is a release plus overrides of the settings of one or both presets (scenarios/scenarios.json).
// Usage: cd web && npm run build:data && node scripts/make-scenarios.mjs                      (writes results/scenarios.csv, on the releases scenarios.json names)
//        node scripts/make-scenarios.mjs --release 2025-fixed                                    (writes results/scenarios_2025-fixed.csv: every scenario rebased on that release)
// With --release, a scenario on the base release of scenarios.json runs on the named release instead, with the same settings and yield scales; a scenario on a release
// that differs from the base only in its resilience table (the grain stores, 2025-store-1 and 2025-store-2) runs on the named release with that resilience table, and its
// release column says so, e.g. "2025-fixed (resilience table of 2025-store-1)". The reference is the named release at its defaults. Decision 86 (B91).
import fs from 'node:fs';
import path from 'node:path';
import { root, resolveRelease } from './releases.mjs';
import { Evaluator } from '../src/model/evaluator.js';
import { dataDir, PRESETS } from './results-lib.mjs';

const def = JSON.parse(fs.readFileSync(path.join(root, 'scenarios', 'scenarios.json'))), cache = {};
const ri = process.argv.indexOf('--release'), REBASE = ri > 0 ? process.argv[ri + 1] : null;
const modelOf = id => JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json')));
// resil: the release whose resilience table replaces the model's own (a grain store moved onto the rebased release)
const load = (id, resil = null) => cache[`${id}|${resil}`] ??= (() => {
  const m = modelOf(id); if (resil) m.sheets.resilience = modelOf(resil).sheets.resilience;
  return { ev: new Evaluator(m), regions: JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))) };
})();
// where a scenario runs: its own release, or with --release the rebased release (and, for a store, the store's resilience table)
const whereCache = {};
const where = s => whereCache[s.id] ??= whereOnce(s);
const whereOnce = s => {
  if (!REBASE || s.release === REBASE) return { id: s.release, resil: null, label: s.release };
  if (s.release === def.base) return { id: REBASE, resil: null, label: REBASE };
  const sm = modelOf(s.release), bm = modelOf(def.base), rm = modelOf(REBASE);
  const onlyResilience = resolveRelease(s.release).parent === def.base && Object.keys(bm.sheets).every(sh => sh === 'resilience' || JSON.stringify(sm.sheets[sh]) === JSON.stringify(bm.sheets[sh]))
    && JSON.stringify(JSON.parse(fs.readFileSync(path.join(dataDir(s.release), 'regions.json'))).regions) === JSON.stringify(JSON.parse(fs.readFileSync(path.join(dataDir(def.base), 'regions.json'))).regions);
  if (!onlyResilience) throw new Error(`scenario ${s.id}: release ${s.release} is not ${def.base} with another resilience table, so it cannot be moved onto ${REBASE}`);
  if (JSON.stringify(rm.sheets.resilience) !== JSON.stringify(bm.sheets.resilience)) throw new Error(`${REBASE} and ${def.base} have different resilience tables; a store table moved across would not be the same measure`);
  return { id: REBASE, resil: s.release, label: `${REBASE} (resilience table of ${s.release})` };
};
// yieldScale: [{ rows: [from, to] | [row, ...], factor }]: the regional yields of those Yield-sheet rows times the factor (a climate or productivity scenario)
const scaled = (z, s, yieldRows) => {
  if (!s.yieldScale?.length) return z;
  const y = z.yield.slice();
  for (const sc of s.yieldScale) for (const row of sc.rows.length === 2 && sc.rows[1] - sc.rows[0] > 1 ? Array.from({ length: sc.rows[1] - sc.rows[0] + 1 }, (_, i) => sc.rows[0] + i) : sc.rows) { const k = yieldRows.indexOf(row); if (k >= 0) y[k] *= sc.factor; }
  return { ...z, yield: y };
};
const run = s => {
  const w = where(s), { ev, regions: all } = load(w.id, w.resil), regions = all.regions, out = new Map();
  for (const z of Object.values(regions).sort((a, b) => a.id - b.id)) for (const preset of PRESETS) {
    const p = { ...z.presets[preset], ...(s.settings?.[preset] ?? {}) }, zz = scaled(z, s, all.yieldRows), r = ev.evaluate(zz, { ...z.land, ...p, population: z.population });
    out.set(`${z.id}|${preset}`, { zone: z.id, name: z.name, kind: z.kind, preset, population: z.population, capacity: Math.round(r.capacity) });
  }
  return out;
};
const ref = run(def.scenarios.find(s => s.id === 'reference')), rows = [];
for (const s of def.scenarios) {
  const res = s.id === 'reference' ? ref : run(s);
  for (const [k, r] of res) { const b = ref.get(k).capacity; rows.push({ scenario: s.id, release: where(s).label, ...r, capacity_reference: b, change: r.capacity - b, change_pct: b ? +(100 * (r.capacity - b) / b).toFixed(2) : '' }); }
}
const cols = Object.keys(rows[0]), cell = v => /[",]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : v;
const outFile = REBASE ? `scenarios_${REBASE}.csv` : 'scenarios.csv';
fs.writeFileSync(path.join(root, 'results', outFile), [cols.join(','), ...rows.map(r => cols.map(c => cell(r[c])).join(','))].join('\n') + '\n');
console.log(outFile, rows.length, 'rows;', def.scenarios.map(s => s.id).join(', '));
for (const s of def.scenarios) { const a = rows.filter(r => r.scenario === s.id && r.zone === 1); console.log(s.id.padEnd(16), a.map(r => `${r.preset} ${(r.capacity / 1e6).toFixed(2)} (${r.change_pct}%)`).join('  ')); }
