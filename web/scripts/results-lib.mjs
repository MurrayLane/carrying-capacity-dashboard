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

/**
 * The grid of the comparison: data vintage (2011, 2025) by method tier (published, corrected, improved; methods/README.md).
 * The change from the published 2011 result to the improved 2025 result is split along one path: first the corrections on the 2011 data, then the improvements on the 2011 data, then the data
 * (2011 to 2025) on the improved method. The other orders (and the data effect on the published and corrected methods) are in the columns too, so the dependence on the path can be read.
 */
export const CELLS = { p11: '2011-corrected', f11: '2011-fixed', i11: '2011-improved', p25: '2025-mirror', f25: '2025-fixed', i25: '2025-improved' };
export function comparison(byRelease) {
  const key = r => `${r.zone}|${r.preset}`, m = Object.fromEntries(Object.entries(CELLS).map(([k, id]) => [k, new Map(byRelease[id].map(r => [key(r), r]))]));
  const out = [];
  for (const [k, a] of m.p11) {
    const g = c => m[c].get(k).capacity, p25 = m.p25.get(k);
    out.push({ zone: a.zone, name: a.name, kind: a.kind, preset: a.preset, population_2011: a.population, population_2025: p25.population,
      capacity_2011_published: g('p11'), capacity_2011_corrected: g('f11'), capacity_2011_improved: g('i11'), capacity_2025_published: g('p25'), capacity_2025_corrected: g('f25'), capacity_2025_improved: g('i25'),
      correction_effect_2011_data: g('f11') - g('p11'), correction_effect_2025_data: g('f25') - g('p25'), improvement_effect_2011_data: g('i11') - g('f11'), improvement_effect_2025_data: g('i25') - g('f25'),
      data_effect_published: g('p25') - g('p11'), data_effect_corrected: g('f25') - g('f11'), data_effect_improved: g('i25') - g('i11'),
      total_change: g('i25') - g('p11'), step_corrections: g('f11') - g('p11'), step_improvements: g('i11') - g('f11'), step_data: g('i25') - g('i11') });
  }
  return out;
}
export const COMPARISON_COLUMNS = ['zone', 'name', 'kind', 'preset', 'population_2011', 'population_2025',
  'capacity_2011_published', 'capacity_2011_corrected', 'capacity_2011_improved', 'capacity_2025_published', 'capacity_2025_corrected', 'capacity_2025_improved',
  'correction_effect_2011_data', 'correction_effect_2025_data', 'improvement_effect_2011_data', 'improvement_effect_2025_data', 'data_effect_published', 'data_effect_corrected', 'data_effect_improved',
  'total_change', 'step_corrections', 'step_improvements', 'step_data'];
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
  const model = JSON.parse(fs.readFileSync(path.join(dataDir(baseId), 'model.json'))), rj = JSON.parse(fs.readFileSync(path.join(dataDir(baseId), 'regions.json'))), regions = rj.regions, yieldRows = rj.yieldRows;
  for (const id of mods) {
    const m = methodModule(id);
    for (const [sheet, cells] of Object.entries(m.cellOverrides ?? {})) for (const [a, v] of Object.entries(cells)) model.sheets[sheet].cells[decode(a)] = v;
    for (const p of m.patches ?? []) for (const z of Object.values(regions)) z.presets[p.preset][p.field] = p.value;
    for (const f of m.yieldFactors ?? []) { const k = yieldRows.indexOf(f.row); for (const [z, x] of Object.entries(f.zones)) regions[z].yield[k] *= x; }
  }
  const ev = new Evaluator(model), out = new Map();
  for (const z of Object.values(regions).sort((a, b) => a.id - b.id)) for (const preset of PRESETS)
    out.set(`${z.id}|${preset}`, { zone: z.id, name: z.name, kind: z.kind, preset, population: z.population, capacity: Math.round(ev.evaluate(z, { ...z.land, ...z.presets[preset], population: z.population }).capacity) });
  return out;
}
