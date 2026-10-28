// Evaluates a built release for every zone and both presets: the one place the numbers of the dashboard's change pages and of the papers come from.
// Needs the built data (npm run build:data).
import fs from 'node:fs';
import path from 'node:path';
import { Evaluator } from '../src/model/evaluator.js';
import { root, index, resolveRelease, sha } from './releases.mjs';

export const dataDir = id => path.join(root, 'web', 'public', 'data', id);
export const PRESETS = ['short', 'long'];
export const COLUMNS = ['release', 'zone', 'name', 'kind', 'parent', 'preset', 'population', 'capacity', 'capacity_per_person', 'over_capacity', 'land_km2',
  'resilience', 'meategg', 'redmeat', 'losses', 'recycling', 'organic', 'fuel', 'biofuel'];

/** One row per zone and preset: the capacity (people) at the release's own defaults, the population it is set against, and the settings that drive the two presets. */
export function evaluateRelease(id) {
  const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions;
  const ev = new Evaluator(model), rows = [];
  for (const z of Object.values(regions).sort((a, b) => a.id - b.id)) for (const preset of PRESETS) {
    const p = z.presets[preset], out = ev.evaluate(z, { ...z.land, ...p, population: z.population });
    rows.push({ release: id, zone: z.id, name: z.name, kind: z.kind, parent: z.parent ?? '', preset, population: z.population, capacity: Math.round(out.capacity),
      capacity_per_person: z.population ? +(out.capacity / z.population).toFixed(4) : '', over_capacity: z.population > out.capacity ? 1 : 0, land_km2: Math.round(out.totalLand / 1e6),
      resilience: p.resilience, meategg: p.meategg, redmeat: p.redmeat, losses: p.losses, recycling: p.recycling, organic: p.organic, fuel: p.fuel, biofuel: p.biofuel });
  }
  return rows;
}
const cell = v => { const s = String(v); return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s; };
export const toCsv = rows => [COLUMNS.join(','), ...rows.map(r => COLUMNS.map(c => cell(r[c])).join(','))].join('\n') + '\n';

/** The two-by-two of the comparison: data vintage (2011, 2025) by method (thesis, improved), with the data effect, the method effect on each vintage and their interaction. */
export const CELLS = { c2011: '2011-corrected', c2011i: '2011-improved', c2025: '2025-mirror', c2025i: '2025-improved' };
export function comparison(byRelease) {
  const key = r => `${r.zone}|${r.preset}`, m = Object.fromEntries(Object.entries(CELLS).map(([k, id]) => [k, new Map(byRelease[id].map(r => [key(r), r]))]));
  const out = [];
  for (const [k, a] of m.c2011) {
    const b = m.c2011i.get(k), c = m.c2025.get(k), d = m.c2025i.get(k), cap = x => x.capacity;
    out.push({ zone: a.zone, name: a.name, kind: a.kind, preset: a.preset, population_2011: a.population, population_2025: c.population,
      capacity_2011: cap(a), capacity_2011_improved: cap(b), capacity_2025: cap(c), capacity_2025_improved: cap(d),
      data_effect: cap(c) - cap(a), method_effect_2011_data: cap(b) - cap(a), method_effect_2025_data: cap(d) - cap(c),
      interaction: (cap(d) - cap(c)) - (cap(b) - cap(a)), total_change: cap(d) - cap(a) });
  }
  return out;
}
export const COMPARISON_COLUMNS = ['zone', 'name', 'kind', 'preset', 'population_2011', 'population_2025', 'capacity_2011', 'capacity_2011_improved', 'capacity_2025', 'capacity_2025_improved',
  'data_effect', 'method_effect_2011_data', 'method_effect_2025_data', 'interaction', 'total_change'];
export const comparisonCsv = rows => [COMPARISON_COLUMNS.join(','), ...rows.map(r => COMPARISON_COLUMNS.map(c => cell(r[c])).join(','))].join('\n') + '\n';

export function releaseInfo(id) {
  const r = resolveRelease(id);
  return { id, label: r.label, status: r.status, extends: r.parent ?? null, methods: r.methods ?? [], vintage: r.vintage ?? null,
    model_sha256: sha(path.relative(root, path.join(dataDir(id), 'model.json'))), regions_sha256: sha(path.relative(root, path.join(dataDir(id), 'regions.json'))) };
}
export { index };

// ---- a built release with extra method modules applied in memory (the effect of one module alone) ------------------------------------------------------------------------
import { methodModule } from './releases.mjs';
const decode = a => { const m = a.match(/^([A-Z]+)(\d+)$/); let c = 0; for (const ch of m[1]) c = c * 26 + ch.charCodeAt(0) - 64; return `${+m[2] - 1}:${c - 1}`; };
/** Capacity of every zone and preset of the built release `baseId` with the method modules `mods` applied on top: the same overrides and patches the resolver applies. */
export function evaluateComposed(baseId, mods) {
  const model = JSON.parse(fs.readFileSync(path.join(dataDir(baseId), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(baseId), 'regions.json'))).regions;
  for (const id of mods) {
    const m = methodModule(id);
    for (const [sheet, cells] of Object.entries(m.cellOverrides ?? {})) for (const [a, v] of Object.entries(cells)) model.sheets[sheet].cells[decode(a)] = v;
    for (const p of m.patches ?? []) for (const z of Object.values(regions)) z.presets[p.preset][p.field] = p.value;
  }
  const ev = new Evaluator(model), out = new Map();
  for (const z of Object.values(regions).sort((a, b) => a.id - b.id)) for (const preset of PRESETS)
    out.set(`${z.id}|${preset}`, { zone: z.id, name: z.name, kind: z.kind, preset, population: z.population, capacity: Math.round(ev.evaluate(z, { ...z.land, ...z.presets[preset], population: z.population }).capacity) });
  return out;
}
