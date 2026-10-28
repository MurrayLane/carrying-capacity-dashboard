// results/method_effects.csv: the effect of each method module alone and in sequence, on each data vintage (zone by zone, both presets).
// The modules are the `methods` of release 2025-improved, in order: the corrections first (those of 2025-fixed), then the improvements. The base of each vintage is the published method
// (2011-corrected, 2025-mirror). Per module: its effect alone on the base, and the capacity after adding the modules up to and including it in order (so the steps add up to the total).
// "interaction" is the total effect less the sum of the effects alone. The sequence after the corrections is checked against the built fixed release, and after all of them against the built improved release.
// Usage: cd web && npm run build:data && node scripts/make-method-effects.mjs
import fs from 'node:fs';
import path from 'node:path';
import { root, resolveRelease } from './releases.mjs';
import { evaluateComposed } from './results-lib.mjs';

const CORR = resolveRelease('2025-fixed').methods, MODS = resolveRelease('2025-improved').methods;
if (MODS.slice(0, CORR.length).join() !== CORR.join()) throw new Error('the improved release must list the corrections first');
const VINTAGES = [['2011', '2011-corrected', '2011-fixed', '2011-improved'], ['2025', '2025-mirror', '2025-fixed', '2025-improved']], rows = [];
for (const [vintage, base, fixed, improved] of VINTAGES) {
  const none = evaluateComposed(base, []), alone = MODS.map(m => evaluateComposed(base, [m])), seq = MODS.map((_, i) => evaluateComposed(base, MODS.slice(0, i + 1)));
  const builtFixed = evaluateComposed(fixed, []), builtImproved = evaluateComposed(improved, []), after = seq[CORR.length - 1], all = seq[MODS.length - 1];
  for (const [k, r] of none) {
    if (after.get(k).capacity !== builtFixed.get(k).capacity) throw new Error(`${vintage} ${k}: corrections applied in memory differ from the built ${fixed}`);
    if (all.get(k).capacity !== builtImproved.get(k).capacity) throw new Error(`${vintage} ${k}: all modules applied in memory differ from the built ${improved}`);
    const row = { vintage, zone: r.zone, name: r.name, kind: r.kind, preset: r.preset, population: r.population, capacity_published: r.capacity };
    let sumAlone = 0;
    MODS.forEach((m, i) => { const ea = alone[i].get(k).capacity - r.capacity; sumAlone += ea; row[`effect_alone_${m}`] = ea; });
    MODS.forEach((m, i) => { row[`effect_step_${m}`] = seq[i].get(k).capacity - (i ? seq[i - 1].get(k).capacity : r.capacity); });
    row.capacity_corrected = after.get(k).capacity; row.capacity_improved = all.get(k).capacity; row.effect_total = all.get(k).capacity - r.capacity; row.interaction = row.effect_total - sumAlone;
    rows.push(row);
  }
}
const cols = Object.keys(rows[0]), cell = v => /[",]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : v;
fs.writeFileSync(path.join(root, 'results', 'method_effects.csv'), [cols.join(','), ...rows.map(r => cols.map(c => cell(r[c])).join(','))].join('\n') + '\n');
console.log('method_effects.csv', rows.length, 'rows;', MODS.join(', '));
