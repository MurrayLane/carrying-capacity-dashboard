// results/method_effects.csv: the effect of each improved-method module alone and together, on each data vintage, with their interaction (zone by zone, both presets).
// Modules are the `methods` of release 2025-improved; the 2011 vintage is 2011-corrected and the 2025 vintage 2025-mirror. The "both" column is checked against the built improved releases.
// Usage: cd web && npm run build:data && node scripts/make-method-effects.mjs
import fs from 'node:fs';
import path from 'node:path';
import { root, resolveRelease } from './releases.mjs';
import { evaluateComposed } from './results-lib.mjs';

const MODS = resolveRelease('2025-improved').methods, VINTAGES = [['2011', '2011-corrected', '2011-improved'], ['2025', '2025-mirror', '2025-improved']];
if (MODS.length !== 2) throw new Error('make-method-effects handles two modules; extend the combinations for more');
const [A, B] = MODS, rows = [];
for (const [vintage, base, improved] of VINTAGES) {
  const none = evaluateComposed(base, []), a = evaluateComposed(base, [A]), b = evaluateComposed(base, [B]), both = evaluateComposed(base, MODS), built = evaluateComposed(improved, []);
  for (const [k, r] of none) {
    if (both.get(k).capacity !== built.get(k).capacity) throw new Error(`${vintage} ${k}: modules applied in memory (${both.get(k).capacity}) differ from the built ${improved} (${built.get(k).capacity})`);
    const c0 = r.capacity, ca = a.get(k).capacity, cb = b.get(k).capacity, cab = both.get(k).capacity;
    rows.push({ vintage, zone: r.zone, name: r.name, kind: r.kind, preset: r.preset, population: r.population, capacity_base: c0, [`capacity_${A}`]: ca, [`capacity_${B}`]: cb, capacity_both: cab,
      [`effect_${A}`]: ca - c0, [`effect_${B}`]: cb - c0, effect_both: cab - c0, interaction: cab - c0 - (ca - c0) - (cb - c0) });
  }
}
const cols = Object.keys(rows[0]), cell = v => /[",]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : v;
fs.writeFileSync(path.join(root, 'results', 'method_effects.csv'), [cols.join(','), ...rows.map(r => cols.map(c => cell(r[c])).join(','))].join('\n') + '\n');
console.log('method_effects.csv', rows.length, 'rows;', MODS.join(', '));
