// What changed carrying capacity between the 2011 data and the 2025 data, on the CORRECTED tier (2011-fixed to 2025-fixed), by data layer, zone by zone (brief B76; Paper A section 4, gap 1 and N-A4 option (a)).
// Usage: node decompose_corrected.mjs        (from this folder; needs the built data, web/public/data, which this script checks is current; it does not need `npm run results`)
//
// Method: a cumulative walk along the 2025 release chain. Each step is the release of that layer with the corrected tier's method modules (those of 2011-fixed:
// state-population-sum, biodiesel-yield, beef-carcase-yield) applied in memory, exactly as the release resolver applies them (cell overrides on the release's model;
// state populations set to the sum of their regions). A layer's effect is the capacity after it minus the capacity before it, so the layers telescope and add up
// to the corrected 2011-to-2025 change with no interaction term.
//   step 0  2011-corrected + corrections                     must equal 2011-fixed (checked)
//   land          2025-land: cropping, pasture, reserve and total area, the reserve share default
//   infrastructure land  2025-population: population, and the infrastructure land (population x 730 m2) and non-agricultural remainder that follow it. The population input
//                 itself moves no capacity (it is reported as a status change, not a cause); the infrastructure land moves capacity in one zone only (Northern and Yorke, which
//                 has no non-agricultural land to absorb it), so the step is kept as its own column, infrastructure_land_only, for the layers to add up
//   crop yields   2025-yields: the crop and derived rows of the Yield sheet (the animal rows are carried from 2011, rewritten at 6 significant figures: relative change below 1e-5)
//   livestock     2025-livestock: the animal-product rows
//   consumption   2025-consumption except the organic share (meat and egg share, red meat share, fuel, biofuel, timber; short term only)
//   organic       2025-organic: the organic share of 2025-consumption (7%) together with the E5 update (baseline constant Yield!E2 to 7%, new factors for five crops)
//   resilience    2025-resilience: the resilience table (long term only)
//   fuel          2025-fuel: the long-term liquid fuel (210 L)
//   red meat mix  2025-diet (layer 9): the split of red meat among beef, lamb, veal and pork (Base!V175:V178)
//   end           must equal 2025-fixed, evaluated from its own built data (checked: this is the sum check)
// Writes capacity_by_cause_corrected.csv: both presets, all 60 zones. The cause columns keep the names of capacity_by_cause.csv but hold each layer's CHANGE in capacity
// (people) in walk order, not a capacity with that cause alone; see README.md "Corrected-tier decomposition".
import fs from 'node:fs';
import path from 'node:path';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { root, sha, resolveRelease, methodModule } from '../../web/scripts/releases.mjs';

const dataDir = id => path.join(root, 'web', 'public', 'data', id);
const read = (id, f) => JSON.parse(fs.readFileSync(path.join(dataDir(id), f)));
// the built data must be current: every input file of every release used must hash as recorded when it was built
for (const id of ['2011-corrected', '2011-fixed', '2025-land', '2025-population', '2025-yields', '2025-livestock', '2025-consumption', '2025-organic', '2025-resilience', '2025-fuel', '2025-diet', '2025-fixed']) {
  const src = read(id, 'regions.json').source, stale = src.files.filter((f, i) => sha(f) !== src.sha256[i]);
  if (stale.length) throw new Error(`web/public/data/${id} is stale (${stale.join(', ')}): run cd ../../web && node scripts/build-data.mjs`);
}
const CORRECTIONS = resolveRelease('2011-fixed').methods;           // state-population-sum, biodiesel-yield, beef-carcase-yield
const END_METHODS = resolveRelease('2025-fixed').methods;           // biodiesel-yield, beef-carcase-yield (state-population-sum does nothing on the 2025 data: checked below)
const STATE_IDS = [2, 15, 26, 40, 49, 56, 60];
const decode = a => { const m = a.match(/^([A-Z]+)(\d+)$/); let c = 0; for (const ch of m[1]) c = c * 26 + ch.charCodeAt(0) - 64; return `${+m[2] - 1}:${c - 1}`; };

/** A built release with method modules applied in memory, the way resolveRelease and build-data apply them. `tweak` may edit the regions first. */
function compose(id, mods, tweak) {
  const model = read(id, 'model.json'), regions = read(id, 'regions.json').regions;
  for (const m of mods.map(methodModule)) {
    if (m.patches || m.dairyGoodLand || m.yieldFactors) throw new Error(`module ${m.id} has steps this script does not apply`);
    for (const [sheet, cells] of Object.entries(m.cellOverrides ?? {})) for (const [a, v] of Object.entries(cells)) model.sheets[sheet].cells[decode(a)] = v;
    if (m.statePopulationsFromRegions) for (const s of STATE_IDS) if (regions[s].children.length) regions[s].population = regions[s].children.reduce((t, c) => t + regions[c].population, 0);
  }
  if (tweak) tweak(regions);
  const ev = new Evaluator(model), cap = {};
  for (const z of Object.keys(regions)) for (const p of ['short', 'long']) cap[`${z}|${p}`] = ev.evaluate(regions[z], { ...regions[z].land, ...regions[z].presets[p], population: regions[z].population }).capacity;
  return { regions, cap };
}

const start = compose('2011-corrected', CORRECTIONS), ref11 = compose('2011-fixed', []);
const org2011 = start.regions[1].presets.short.organic;
const LAYERS = [
  ['land_only', '2025-land'],
  ['infrastructure_land_only', '2025-population'],
  ['crop_yields_only', '2025-yields'],
  ['livestock_only', '2025-livestock'],
  ['consumption_only', '2025-consumption', r => { for (const z of Object.values(r)) z.presets.short.organic = org2011; }],
  ['organic_update_only', '2025-organic'],
  ['resilience_update_only', '2025-resilience'],
  ['fuel_update_only', '2025-fuel'],
  ['red_meat_mix_only', '2025-diet'],
];
const walk = [start, ...LAYERS.map(([, id, tweak]) => compose(id, CORRECTIONS, tweak))];
const ref25 = compose('2025-fixed', []), ref25b = compose('2025-diet', END_METHODS);

// checks: the walk starts at 2011-fixed and ends at 2025-fixed (unrounded, every zone and preset); which zones the 2025-population step moves; the start populations are 2011-fixed's
const TOL = 1e-6;   // people, absolute, on unrounded capacities
const keys = Object.keys(start.cap); let worstStart = 0, worstEnd = 0, worstEndB = 0; const popMoved = [];
for (const k of keys) {
  worstStart = Math.max(worstStart, Math.abs(start.cap[k] - ref11.cap[k]));
  worstEnd = Math.max(worstEnd, Math.abs(walk.at(-1).cap[k] - ref25.cap[k]));
  worstEndB = Math.max(worstEndB, Math.abs(ref25b.cap[k] - ref25.cap[k]));
  if (Math.abs(walk[2].cap[k] - walk[1].cap[k]) > TOL) popMoved.push(`${k} ${Math.round(walk[2].cap[k] - walk[1].cap[k])}`);
}
// the population columns are read from 2011-fixed and 2025-fixed themselves; the walk's own end populations differ from 2025-fixed only where state-population-sum
// (a 2011-fixed module that 2025-fixed does not list) re-adds a 2025 state from its regions: Queensland, by 1 person of rounding. Capacity does not depend on it.
const popEnd = Object.keys(ref25.regions).filter(z => walk.at(-1).regions[z].population !== ref25.regions[z].population).map(z => `${z}: ${walk.at(-1).regions[z].population - ref25.regions[z].population}`);
for (const z of Object.keys(ref11.regions)) if (start.regions[z].population !== ref11.regions[z].population) throw new Error(`zone ${z}: start population differs from 2011-fixed`);

const COLS = ['tier', 'zone', 'name', 'preset', 'capacity_2011', 'land_only', 'infrastructure_land_only', 'crop_yields_only', 'livestock_only', 'consumption_only', 'organic_update_only', 'resilience_update_only', 'fuel_update_only', 'red_meat_mix_only',
  'all_2025', 'interaction', 'population_2011', 'population_2025', 'population_over_capacity_2011', 'population_over_capacity_2025', 'population_2011_over_capacity_2025'];
const out = [COLS.join(',')]; let worstSum = 0, failures = 0;
const ids = Object.keys(start.regions).sort((a, b) => a - b);
for (const z of ids) for (const p of ['short', 'long']) {
  const k = `${z}|${p}`, R = walk.map(w => Math.round(w.cap[k])), c0 = Math.round(ref11.cap[k]), c1 = Math.round(ref25.cap[k]);
  const step = i => R[i + 1] - R[i];                          // integer steps of rounded cumulative capacities: they telescope exactly
  const st = Object.fromEntries(LAYERS.map(([name], i) => [name, step(i)]));
  const residual = c1 - c0 - LAYERS.reduce((t, [name]) => t + st[name], 0);   // the sum check, in whole people; must be 0
  const unrounded = (ref25.cap[k] - ref11.cap[k]) - walk.slice(1).reduce((t, w, i) => t + (w.cap[k] - walk[i].cap[k]), 0);
  worstSum = Math.max(worstSum, Math.abs(unrounded)); if (residual !== 0 || Math.abs(unrounded) > TOL) failures++;
  const pop0 = ref11.regions[z].population, pop1 = ref25.regions[z].population;
  const row = { tier: 'corrected', zone: z, name: `"${start.regions[z].name}"`, preset: p, capacity_2011: c0, ...st, all_2025: c1, interaction: residual,
    population_2011: Math.round(pop0), population_2025: Math.round(pop1),
    population_over_capacity_2011: c0 ? (pop0 / ref11.cap[k]).toFixed(3) : '', population_over_capacity_2025: c1 ? (pop1 / ref25.cap[k]).toFixed(3) : '',
    population_2011_over_capacity_2025: c1 ? (pop0 / ref25.cap[k]).toFixed(3) : '' };   // the 2025 capacity against both populations: the status change population makes
  out.push(COLS.map(c => row[c]).join(','));
}
fs.writeFileSync(new URL('capacity_by_cause_corrected.csv', import.meta.url), out.join('\n') + '\n');
console.log(`start = 2011-fixed: worst |difference| ${worstStart.toExponential(2)} people; end = 2025-fixed: ${worstEnd.toExponential(2)}; 2025-diet + ${END_METHODS.join(' + ')} = 2025-fixed: ${worstEndB.toExponential(2)}`);
console.log(`walk end population against 2025-fixed (zone: difference): ${popEnd.join('; ') || 'none'}`);
console.log(`infrastructure land (2025-population step) moves capacity in: ${popMoved.join('; ') || 'no zone'}`);
console.log(`sum check (layers against 2025-fixed minus 2011-fixed, ${keys.length} zone-preset cells): rounded residual 0 required, unrounded worst ${worstSum.toExponential(2)} people (tolerance ${TOL}); failures ${failures}`);
if (failures || worstStart > TOL || worstEnd > TOL) { console.error('CHECK FAILED'); process.exit(1); }
for (const p of ['short', 'long']) console.log(p, out.find(l => l.startsWith(`corrected,1,`) && l.includes(`,${p},`)));

// ---- README.md: the section "Corrected-tier decomposition", written from the numbers above (replaces the section if present; write_readme.py rewrites the rest of the file and drops it, so run this script after write_readme.py)
const nat = Object.fromEntries(['short', 'long'].map(p => { const l = out.find(x => x.startsWith('corrected,1,') && x.includes(`,${p},`)).match(/("[^"]*"|[^,]+)/g); return [p, Object.fromEntries(COLS.map((c, i) => [c, l[i]]))]; }));
const n = v => Number(v).toLocaleString('en-AU'), sg = v => (v > 0 ? '+' : v < 0 ? '-' : '') + Math.abs(v).toLocaleString('en-AU');
const LABEL = { land_only: 'Land (2025-land: cropping, pasture, reserve and total area, reserve share)', infrastructure_land_only: 'Infrastructure land that follows population (2025-population)',
  crop_yields_only: 'Crop yields (2025-yields)', livestock_only: 'Livestock (2025-livestock: animal-product rows)', consumption_only: 'Consumption (2025-consumption, without the organic share)',
  organic_update_only: 'Organic update (organic share 7% and 2025-organic)', resilience_update_only: 'Resilience table (2025-resilience)', fuel_update_only: 'Long-term liquid fuel (2025-fuel)', red_meat_mix_only: 'Red meat mix of the diet (2025-diet, layer 9)' };
const layerSum = p => LAYERS.reduce((t, [c]) => t + +nat[p][c], 0);
const sec = `## Corrected-tier decomposition

Written by \`decompose_corrected.mjs\` (brief B76; Paper A section 4, gap 1, N-A4 option (a)); the full table, both presets and all 60 zones, is \`capacity_by_cause_corrected.csv\`. \`capacity_by_cause.csv\` above was made by \`decompose.mjs\` (Node), so this script is Node too; it reads the built data (\`web/public/data\`), checks that it is current against its source hashes, and needs neither \`npm run build:data\` nor \`npm run results\` when that check passes.

**Method.** A cumulative walk along the 2025 release chain on the corrected tier. It starts at 2011-corrected with the corrected tier's method modules applied (${CORRECTIONS.join(', ')}; this equals release \`2011-fixed\`) and adds the 2025 layers one at a time, in the order of the chain, each with the same modules applied: ${LAYERS.map(([, id]) => id).join(', ')}. The last step equals release \`2025-fixed\`. A layer's effect is the capacity after it minus the capacity before it, so the effects add up to the corrected change with nothing left over: there is no interaction term, but each effect depends on the order (a layer is measured on top of the layers before it). This differs from the table above, where each cause is applied alone to the 2011 data and the remainder is reported as an interaction. The consumption step leaves the short-term organic share at 2011's ${Math.round(org2011 * 100)}%; the organic step moves it to 7% together with the 2025-organic factors and baseline, as in the table above. The csv keeps the column names of \`capacity_by_cause.csv\` plus \`tier\`, but its cause columns hold each layer's change in capacity (people), not a capacity; it adds \`infrastructure_land_only\`, \`red_meat_mix_only\` and \`population_2011_over_capacity_2025\`; \`all_2025\` is the 2025-fixed capacity and \`interaction\` is the sum check residual (0 everywhere).

**Population is a status change, not a cause.** The population input does not enter capacity. The 2025-population layer also sets infrastructure land to population x 730 m2 with non-agricultural land as the remainder; that land moves capacity in one zone only (Northern and Yorke, which has no non-agricultural land: ${popMoved.join('; ')} people, zone|preset), and is the row "Infrastructure land" below. What population changes is whether a zone is over or under its capacity (people divided by capacity: above 1 is over capacity).

| Change in capacity, Australia, people | Short term | Long term |
|---|---|---|
| 2011, corrected (\`2011-fixed\`) | ${n(nat.short.capacity_2011)} | ${n(nat.long.capacity_2011)} |
${LAYERS.map(([c]) => `| ${LABEL[c]} | ${sg(+nat.short[c])} | ${sg(+nat.long[c])} |`).join('\n')}
| 2025, corrected (\`2025-fixed\`) | ${n(nat.short.all_2025)} | ${n(nat.long.all_2025)} |
| Sum of the layers | ${sg(layerSum('short'))} | ${sg(layerSum('long'))} |
| 2025-fixed minus 2011-fixed | ${sg(nat.short.all_2025 - nat.short.capacity_2011)} | ${sg(nat.long.all_2025 - nat.long.capacity_2011)} |

| Population (status, not a cause), Australia | Short term | Long term |
|---|---|---|
| People 2011 / people 2025 | ${n(nat.short.population_2011)} / ${n(nat.short.population_2025)} | ${n(nat.long.population_2011)} / ${n(nat.long.population_2025)} |
| 2011 people over 2011 capacity | ${nat.short.population_over_capacity_2011} | ${nat.long.population_over_capacity_2011} |
| 2011 people over 2025 capacity (same capacity, 2011 population) | ${nat.short.population_2011_over_capacity_2025} | ${nat.long.population_2011_over_capacity_2025} |
| 2025 people over 2025 capacity (same capacity, 2025 population) | ${nat.short.population_over_capacity_2025} | ${nat.long.population_over_capacity_2025} |

The state rows use \`2011-fixed\`'s state populations (the sum of their regions, module state-population-sum), so their 2011 ratios differ from the table above; the national population is the same.

**Check.** For every zone (national, the seven state groups and the 52 regions) and both presets, ${keys.length} cells: the start equals \`2011-fixed\` and the end equals \`2025-fixed\`, each evaluated from its own built data (largest unrounded difference ${worstStart.toExponential(1)} and ${worstEnd.toExponential(1)} people); the layers, in whole people, add to the rounded 2025-fixed minus 2011-fixed with a residual of exactly 0 (the \`interaction\` column), and unrounded with the largest residual ${worstSum.toExponential(1)} people against a tolerance of ${TOL} people. Result: ${failures ? `FAILED in ${failures} cells` : 'passed in all cells'}.
`;
const readme = new URL('README.md', import.meta.url), old = fs.readFileSync(readme, 'utf8'), at = old.indexOf('\n## Corrected-tier decomposition');
fs.writeFileSync(readme, (at < 0 ? old.replace(/\n*$/, '\n') : old.slice(0, at + 1)) + '\n' + sec);
