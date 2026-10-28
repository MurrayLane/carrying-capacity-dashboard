// What changed carrying capacity between the 2011 data and the 2025 data, by cause, zone by zone (SCOPE.md D4).
// Usage: node decompose.mjs        (from this folder; needs the built data: cd ../../web && node scripts/build-data.mjs)
// Each cause alone is applied to the 2011 data (releases 2011-corrected and the five 2025 layers); "all" is release 2025-fuel (the tip of the 2025 chain: 2025-organic, then 2025-resilience, then 2025-fuel).
//   land          2025-land: cropping, pasture, reserve and total area, and the reserve share default
//   crop yields   the crop and derived rows of the Yield sheet (rows 4 to 94 and 106 to 137) of 2025-yields
//   livestock     the animal-product rows (95 to 105) of 2025-livestock
//   consumption   the short-term defaults of 2025-consumption except the organic share (meat and egg share, red meat share, fuel, biofuel, timber); the long-term settings are scenarios and do not change
//   organic       the E5 update of 2025-organic (organic share 7%, the baseline constant in Yield!E2 moved to match, new factors for five crops), on the 2011 data: nothing at the short-term defaults, but the long-term settings are 100% organic
//   population    does not enter capacity (checked: 2025-land and 2025-population give identical capacities); it changes whether a zone is over or under its capacity
//   resilience    the resilience table of 2025-resilience (ABS grain yields to 2024-25) on the 2011 data: only the long-term result, which uses 100 years
//   fuel          the long-term liquid fuel of 2025-fuel (210 L instead of 253), on the 2011 data: only the long-term result
// Writes capacity_by_cause.csv: both presets, all 60 zones.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const base = new URL('../../web/public/data/', import.meta.url).pathname;
const load = id => ({ model: JSON.parse(fs.readFileSync(base + id + '/model.json')), data: JSON.parse(fs.readFileSync(base + id + '/regions.json')) });
const A = load('2011-corrected'), L = load('2025-land'), P = load('2025-population'), Y = load('2025-yields'), S = load('2025-livestock'), C = load('2025-consumption'), O = load('2025-organic'), R = load('2025-resilience'), F = load('2025-fuel');
const rows = A.data.yieldRows, ev = new Evaluator(A.model), evO = new Evaluator(O.model), evF = new Evaluator(F.model); const mR = structuredClone(A.model); mR.sheets.resilience = R.model.sheets.resilience; const evR = new Evaluator(mR);
const cap = (reg, preset, e = ev) => e.evaluate(reg, { ...reg.land, ...reg.presets[preset], population: reg.population }).capacity;
const take = (target, source, pick) => { const r = structuredClone(target); rows.forEach((row, k) => { if (pick(row)) r.yield[k] = source.yield[k]; }); return r; };
const noOrg = (pc, pa) => ({ short: { ...pc.short, organic: pa.short.organic }, long: pc.long });
const orgOnly = pa => ({ short: { ...pa.short, organic: 0.07 }, long: pa.long });
const isCrop = r => (r >= 4 && r <= 94) || (r >= 106 && r <= 137), isAnimal = r => r >= 95 && r <= 105;
const out = ['zone,name,preset,capacity_2011,land_only,crop_yields_only,livestock_only,consumption_only,organic_update_only,resilience_update_only,fuel_update_only,all_2025,interaction,population_2011,population_2025,population_over_capacity_2011,population_over_capacity_2025'];
for (const z of Object.keys(A.data.regions)) for (const p of ['short', 'long']) {
  const a = A.data.regions[z], c0 = cap(a, p), cl = cap(L.data.regions[z], p), cy = cap(take(a, Y.data.regions[z], isCrop), p), cs = cap(take(a, S.data.regions[z], isAnimal), p), cc = cap({ ...a, presets: noOrg(C.data.regions[z].presets, a.presets) }, p), co = cap({ ...a, presets: orgOnly(a.presets) }, p, evO), cr = cap(a, p, evR), cf = cap({ ...a, presets: { short: a.presets.short, long: { ...a.presets.long, fuel: F.data.regions[z].presets.long.fuel } } }, p), ca = cap(F.data.regions[z], p, evF);
  const pop0 = a.population, pop1 = P.data.regions[z].population;
  out.push([z, `"${a.name}"`, p, ...[c0, cl, cy, cs, cc, co, cr, cf, ca].map(Math.round), Math.round(ca - c0 - (cl - c0) - (cy - c0) - (cs - c0) - (cc - c0) - (co - c0) - (cr - c0) - (cf - c0)), Math.round(pop0), Math.round(pop1), c0 ? (pop0 / c0).toFixed(3) : '', ca ? (pop1 / ca).toFixed(3) : ''].join(','));
}
fs.writeFileSync('capacity_by_cause.csv', out.join('\n') + '\n');
const show = (z, p) => out.find(l => l.startsWith(`${z},`) && l.includes(`,${p},`)).split(',').slice(-15);
for (const p of ['short', 'long']) { console.log(`\n${p}-term, Australia: 2011, land only, crop yields only, livestock only, consumption only, organic update only, resilience, fuel, all 2025, interaction, pop 2011, pop 2025, pop/capacity 2011, 2025`); console.log(show(1, p).join('  ')); }
