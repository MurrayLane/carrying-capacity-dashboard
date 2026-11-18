// What changed carrying capacity between the 2011 data and the 2025 data, on the CORRECTED tier (2011-fixed to 2025-fixed), by data layer, zone by zone (brief B76; Paper A section 4, gap 1 and N-A4 option (a)).
// Usage: node decompose_corrected.mjs        (from this folder; needs the built data, web/public/data, which this script checks is current; it does not need `npm run results`)
//        node decompose_corrected.mjs --order reverse | --order <the nine layers, comma-separated>     (B111: one other order; prints it and checks the sum, writes nothing)
//        node decompose_corrected.mjs --average [--jobs N]     (B111: every ordering, the Shapley value; writes capacity_by_cause_corrected_orders.csv and its README section; see orders() below)
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

/** A built release's model and regions with method modules applied in memory, the way resolveRelease and build-data apply them. `tweak` may edit the regions. */
function prepare(id, mods, tweak) {
  const model = read(id, 'model.json'), regions = read(id, 'regions.json').regions;
  for (const m of mods.map(methodModule)) {
    if (m.patches || m.dairyGoodLand || m.yieldFactors) throw new Error(`module ${m.id} has steps this script does not apply`);
    for (const [sheet, cells] of Object.entries(m.cellOverrides ?? {})) for (const [a, v] of Object.entries(cells)) model.sheets[sheet].cells[decode(a)] = v;
    if (m.statePopulationsFromRegions) for (const s of STATE_IDS) if (regions[s].children.length) regions[s].population = regions[s].children.reduce((t, c) => t + regions[c].population, 0);
  }
  if (tweak) tweak(regions);
  return { model, regions };
}
/** The same, evaluated: capacity of every zone and preset. */
function compose(id, mods, tweak) {
  const { model, regions } = prepare(id, mods, tweak);
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
// --order and --average (brief B111): other orders of the same nine layers and the all-orderings average; they write capacity_by_cause_corrected_orders.csv and their own README section
// and leave capacity_by_cause_corrected.csv and the section below untouched (see orders() at the end of this file)
if (process.argv.includes('--order') || process.argv.includes('--average')) { await orders(process.argv.slice(2)); process.exit(0); }
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
const after = at < 0 ? -1 : old.indexOf('\n## ', at + 1);   // a later section (B111's "Decomposition in every order") is kept as it is
fs.writeFileSync(readme, (at < 0 ? old.replace(/\n*$/, '\n') + '\n' : old.slice(0, at + 1)) + sec + (after < 0 ? '' : old.slice(after)));

// =====================================================================================================================================================================
// B111 (decision 101): the same nine layers in any order, in reverse, and averaged over every ordering (the Shapley value); land and livestock also as one layer.
//   node decompose_corrected.mjs --order reverse                  one order (forward, reverse, or the nine layers comma-separated, by column name, short name or release id);
//                                                                  prints Australia and the states and checks the sum; writes nothing
//   node decompose_corrected.mjs --average [--jobs 4]             every one of the 9! = 362,880 orderings, in all 60 zones and both presets (no sampling); writes
//                                                                  capacity_by_cause_corrected_orders.csv and the README section "Decomposition in every order"
// How: a layer is the set of inputs its release changes against the release before it in the chain (region inputs and yields from regions.json, workbook cells
// from model.json; the corrections are applied to every state as in the walk). Any subset of layers is the 2011 start with those changes applied in chain order,
// so the 2^9 = 512 subsets give every state any ordering passes through; an ordering's layer effect is the capacity after the layer minus the capacity before it.
// Three inputs are shared between layers and follow a stated rule: (1) non-agricultural land is the remainder of the total area, as make_defaults_2025.py builds it
// (total minus cropping, pasture, reserve and infrastructure, at least 0), with the 2025 total when the land layer is in and the 2011 total when it is not; (2) the
// short-term organic share belongs to the organic layer, as in the forward walk; (3) the eleven animal-product yield rows belong to livestock; without it they are
// the 2025-yields release's rewrite of the 2011 rows (6 significant figures, relative change below 1e-5). The script checks that every prefix of the forward
// order rebuilds the walk's release, input by input, and that the forward effects equal capacity_by_cause_corrected.csv to the person.
async function orders(argv) {
  const { Worker } = await import('node:worker_threads'), os = await import('node:os');
  const opt = f => { const i = argv.indexOf(f); return i < 0 ? null : argv[i + 1]; };
  const JOBS = Math.max(1, Math.floor(+(opt('--jobs') ?? Math.min(4, os.availableParallelism()))));
  const N = LAYERS.length, NAMES = LAYERS.map(([c]) => c), FULL = (1 << N) - 1, PRESETS = ['short', 'long'];
  const LAND = NAMES.indexOf('land_only'), LIVE = NAMES.indexOf('livestock_only'), COMB = 'land_and_livestock';
  const CHAIN = ['2011-corrected', ...LAYERS.map(([, id]) => id)];

  // ---- the layers as sets of input changes ----
  const prep = CHAIN.map(id => prepare(id, []));                       // raw built data of each chain release (no modules: the diffs are taken between releases)
  for (const p of prep) {
    if (JSON.stringify(p.model.meta) !== JSON.stringify(prep[0].model.meta)) throw new Error('model meta differs along the chain');
    for (const [s, sh] of Object.entries(p.model.sheets)) if (sh.rows !== prep[0].model.sheets[s].rows || sh.cols !== prep[0].model.sheets[s].cols) throw new Error(`sheet ${s} size differs along the chain`);
  }
  const leaves = (o, p, out) => { if (o !== null && typeof o === 'object') { for (const k of Object.keys(o)) leaves(o[k], [...p, k], out); } else out.set(JSON.stringify(p), o); return out; };
  const flatR = r => { const m = new Map(); for (const [z, reg] of Object.entries(r)) leaves(reg, [z], m); return m; };
  const flatM = m => { const o = new Map(); for (const [s, sh] of Object.entries(m.sheets)) for (const [k, v] of Object.entries(sh.cells)) o.set(JSON.stringify([s, k]), v); return o; };
  const same = (a, b) => a === b || (typeof a === 'object' && typeof b === 'object' && JSON.stringify(a) === JSON.stringify(b));
  const diff = (A, B) => { const d = new Map(); for (const k of new Set([...A.keys(), ...B.keys()])) if (!same(A.get(k), B.get(k))) d.set(k, B.get(k)); return d; };
  const FR = prep.map(p => flatR(p.regions)), FM = prep.map(p => flatM(p.model));
  const dR = NAMES.map((_, i) => diff(FR[i], FR[i + 1])), dM = NAMES.map((_, i) => diff(FM[i], FM[i + 1]));
  const isNonAg = k => k.endsWith('"land","nonAg"]'), isOrgShort = k => k.endsWith('"presets","short","organic"]'), isYield = k => JSON.parse(k)[1] === 'yield';
  for (const d of dR) for (const k of [...d.keys()]) if (isNonAg(k)) d.delete(k);                                   // rule (1): recomputed for every subset
  const CONS = NAMES.indexOf('consumption_only'), ORG = NAMES.indexOf('organic_update_only');
  for (const k of [...dR[CONS].keys()]) if (isOrgShort(k)) { if (dR[ORG].has(k)) throw new Error('organic share changed twice'); dR[ORG].set(k, dR[CONS].get(k)); dR[CONS].delete(k); }  // rule (2)
  const YLD = NAMES.indexOf('crop_yields_only');
  for (let i = 0; i < N; i++) for (let j = i + 1; j < N; j++) for (const [d, kind] of [[dR, 'region input'], [dM, 'workbook cell']]) {
    const both = [...d[i].keys()].filter(k => d[j].has(k));
    if (both.length && !(kind === 'region input' && i === YLD && j === LIVE && both.every(isYield))) throw new Error(`${NAMES[i]} and ${NAMES[j]} share ${both.length} ${kind}s, e.g. ${both[0]}`);
  }
  const corrCells = new Set(CORRECTIONS.map(methodModule).flatMap(m => Object.entries(m.cellOverrides ?? {}).flatMap(([s, c]) => Object.keys(c).map(a => JSON.stringify([s, decode(a)])))));
  for (const [i, d] of dM.entries()) for (const k of d.keys()) if (corrCells.has(k)) throw new Error(`${NAMES[i]} changes a corrected cell ${k}`);
  const parse = d => [...d].map(([k, v]) => [JSON.parse(k), v]);
  const RD = dR.map(parse), MD = dM.map(parse);
  const MODEL_MASK = MD.reduce((m, d, i) => m | (d.length ? 1 << i : 0), 0);
  const setPath = (o, p, v) => { for (const k of p.slice(0, -1)) o = o[k]; if (v === undefined) delete o[p.at(-1)]; else o[p.at(-1)] = v; };
  // totals for rule (1): 2011 is the sum of its five land types (as built); 2025 is the land layer's totalArea column
  const T11 = Object.fromEntries(Object.entries(prep[0].regions).map(([z, r]) => [z, r.land.cropping + r.land.pasture + r.land.nonAg + r.land.infrastr1 + r.land.nature1]));
  const landCsv = fs.readFileSync(path.join(root, resolveRelease('2025-land').defaults.short), 'utf8').trim().split('\n').map(l => l.split(','));
  const T25 = Object.fromEntries(landCsv.slice(1).map(r => [r[landCsv[0].indexOf('regionId')], +r[landCsv[0].indexOf('totalArea')]]));
  const nonAg = (L, T) => Math.max(0, T - L.cropping - L.pasture - L.infrastr1 - L.nature1);

  const start = prepare('2011-corrected', CORRECTIONS);                 // the walk's start: 2011-corrected with the corrections
  function regionsOf(mask) {
    const r = structuredClone(start.regions);
    for (let i = 0; i < N; i++) if (mask >> i & 1) for (const [[z, ...p], v] of RD[i]) setPath(r[z], p, v);
    for (const z of Object.keys(r)) r[z].land.nonAg = nonAg(r[z].land, mask >> LAND & 1 ? T25[z] : T11[z]);
    for (const m of CORRECTIONS.map(methodModule)) if (m.statePopulationsFromRegions) for (const s of STATE_IDS) if (r[s].children.length) r[s].population = r[s].children.reduce((t, c) => t + r[c].population, 0);
    return r;
  }
  function modelOf(mask) {
    const m = structuredClone(start.model);
    for (let i = 0; i < N; i++) if (mask >> i & 1) for (const [[s, k], v] of MD[i]) { if (v === undefined) delete m.sheets[s].cells[k]; else m.sheets[s].cells[k] = v; }
    return m;
  }
  // check: every prefix of the forward order rebuilds the walk's state exactly (inputs, yields and workbook cells), including the consumption step's organic share
  const tweakOf = i => LAYERS[i]?.[2];
  for (let k = 0; k <= N; k++) {
    const want = k === 0 ? start : prepare(CHAIN[k], CORRECTIONS, tweakOf(k - 1)), mask = (1 << k) - 1;
    if (JSON.stringify(regionsOf(mask)) !== JSON.stringify(want.regions)) throw new Error(`subset rebuild of ${CHAIN[k]}: region inputs differ`);
    if (JSON.stringify(modelOf(mask).sheets) !== JSON.stringify(want.model.sheets)) throw new Error(`subset rebuild of ${CHAIN[k]}: workbook differs`);
  }
  console.log(`layers as input sets: ${NAMES.map((n, i) => `${n} ${RD[i].length + MD[i].length}`).join(', ')}; the forward prefixes rebuild all ${N + 1} walk states exactly`);

  // ---- which orders ----
  const ALIAS = Object.fromEntries(LAYERS.flatMap(([c, id], i) => [[c, i], [c.replace(/_only$/, ''), i], [id, i]]));
  const parseOrder = s => {
    if (s === 'forward') return NAMES.map((_, i) => i);
    if (s === 'reverse') return NAMES.map((_, i) => N - 1 - i);
    const o = s.split(',').map(x => { if (!(x.trim() in ALIAS)) throw new Error(`--order: unknown layer ${x}; use ${Object.keys(ALIAS).join(', ')}`); return ALIAS[x.trim()]; });
    if (new Set(o).size !== N || o.length !== N) throw new Error('--order: give each of the nine layers once');
    return o;
  };
  const AVERAGE = argv.includes('--average'), ORDER = AVERAGE ? null : parseOrder(opt('--order') ?? 'forward');
  const prefixes = o => o.reduce((a, l) => [...a, a.at(-1) | 1 << l], [0]);
  const masks = AVERAGE ? [...Array(FULL + 1).keys()] : prefixes(ORDER);

  // ---- evaluate every needed state, each distinct (workbook, zone, inputs, yields) once ----
  const ZONES = Object.keys(start.regions).sort((a, b) => a - b), NC = ZONES.length * 2;     // cell ci = zone index * 2 + preset index
  const yieldId = new Map(), yields = [], groups = new Map(), slot = new Map();
  const capIdx = new Map();                                                                   // mask -> Int32Array(NC) of job indices within its group
  for (const mask of masks) {
    const r = regionsOf(mask), mk = mask & MODEL_MASK, ids = new Int32Array(NC);
    if (!groups.has(mk)) groups.set(mk, { jobs: [], keys: new Map() });
    const g = groups.get(mk);
    ZONES.forEach((z, zi) => {
      const yk = JSON.stringify(r[z].yield); if (!yieldId.has(yk)) { yieldId.set(yk, yields.length); yields.push(r[z].yield); }
      PRESETS.forEach((p, pi) => {
        const inputs = { ...r[z].land, ...r[z].presets[p], population: r[z].population }, y = yieldId.get(yk);
        const key = `${r[z].climateZone}|${y}|${JSON.stringify(inputs)}`;
        if (!g.keys.has(key)) { g.keys.set(key, g.jobs.length); g.jobs.push({ climateZone: r[z].climateZone, yieldId: y, inputs }); }
        ids[zi * 2 + pi] = g.keys.get(key);
      });
    });
    capIdx.set(mask, ids);
  }
  const total = [...groups.values()].reduce((t, g) => t + g.jobs.length, 0);
  console.log(`${masks.length} subsets x ${NC} zone-preset cells = ${masks.length * NC} capacities, ${total} distinct evaluations in ${groups.size} workbook variants, ${JOBS} worker(s)`);
  const results = new Map(), queue = [...groups.keys()].sort((a, b) => a - b), t0 = Date.now();
  const runOne = mk => new Promise((res, rej) => {
    const g = groups.get(mk), order = g.jobs.map((_, i) => i).sort((a, b) => g.jobs[a].yieldId - g.jobs[b].yieldId || a - b);
    const w = new Worker(new URL('decompose_orders_worker.mjs', import.meta.url));
    w.once('message', out => { const cap = new Float64Array(g.jobs.length); order.forEach((j, i) => { cap[j] = out[i]; }); results.set(mk, cap); w.terminate(); res(); });
    w.once('error', rej);
    w.postMessage({ model: modelOf(mk), jobs: order.map(j => g.jobs[j]), yields });
  });
  await Promise.all(Array.from({ length: Math.min(JOBS, queue.length) }, async () => { while (queue.length) await runOne(queue.shift()); }));
  console.log(`evaluated in ${((Date.now() - t0) / 1000).toFixed(0)} s`);
  const V = new Float64Array((FULL + 1) * NC).fill(NaN);                                      // V[mask * NC + ci]: unrounded capacity of the subset
  for (const mask of masks) { const ids = capIdx.get(mask), cap = results.get(mask & MODEL_MASK); for (let ci = 0; ci < NC; ci++) V[mask * NC + ci] = cap[ids[ci]]; }
  const v = (mask, ci) => V[mask * NC + ci];
  const walkOf = (o, ci) => { const pm = prefixes(o), eff = new Array(N); o.forEach((l, i) => { eff[l] = Math.round(v(pm[i + 1], ci)) - Math.round(v(pm[i], ci)); }); return eff; };

  // ---- the existing csv: the forward order must reproduce it to the person ----
  const oldCsv = fs.readFileSync(new URL('capacity_by_cause_corrected.csv', import.meta.url), 'utf8').trim().split('\n').map(l => l.match(/("[^"]*"|[^,]+)/g));
  const oldRow = Object.fromEntries(oldCsv.slice(1).map(r => [`${r[1]}|${r[3]}`, Object.fromEntries(oldCsv[0].map((c, i) => [c, r[i]]))]));
  const cellKey = ci => `${ZONES[ci >> 1]}|${PRESETS[ci & 1]}`;
  let fwdMismatch = 0;
  for (let ci = 0; ci < NC; ci++) {
    const o = oldRow[cellKey(ci)], ends = [Math.round(v(0, ci)) === +o.capacity_2011, Math.round(v(FULL, ci)) === +o.all_2025];
    if (masks.includes(FULL) || !ORDER) { if (!ends.every(Boolean)) fwdMismatch++; } else if (!ends[0]) fwdMismatch++;
    if (AVERAGE || ORDER.every((l, i) => l === i)) walkOf(NAMES.map((_, i) => i), ci).forEach((e, l) => { if (e !== +o[NAMES[l]]) fwdMismatch++; });
  }
  console.log(`against capacity_by_cause_corrected.csv (start, end${AVERAGE || ORDER.every((l, i) => l === i) ? ' and the nine forward effects' : ''}, ${NC} cells): ${fwdMismatch} mismatches`);
  if (fwdMismatch) { console.error('CHECK FAILED'); process.exit(1); }

  const label = ZONES.map(z => start.regions[z].name);
  if (!AVERAGE) {                                                                             // one order: print and check, write nothing
    console.log(`order: ${ORDER.map(l => NAMES[l]).join(' > ')}`);
    let bad = 0;
    for (let ci = 0; ci < NC; ci++) { const e = walkOf(ORDER, ci); if (e.reduce((t, x) => t + x, 0) !== Math.round(v(FULL, ci)) - Math.round(v(0, ci))) bad++; }
    console.log(`sum check (layers against the 2025 minus 2011 capacity, whole people, ${NC} cells): ${bad} failures`);
    for (const z of ['1', ...STATE_IDS.map(String)]) for (const [pi, p] of PRESETS.entries()) {
      const ci = ZONES.indexOf(z) * 2 + pi, e = walkOf(ORDER, ci);
      console.log(`${label[ZONES.indexOf(z)]} ${p}: ${NAMES.map((n, l) => `${n.replace(/_only$/, '')} ${e[l]}`).join(', ')}; land and livestock ${e[LAND] + e[LIVE]}`);
    }
    if (bad) process.exit(1);
    return;
  }

  // ---- every ordering ----
  // A game: players are bitmasks of layers; its value is v. mean = Shapley value by the subset formula; the enumeration of all n! orderings gives the sd, min and max
  // of each player's effect over the orderings and repeats the mean as a check. `pairs` adds the per-ordering sum of two players (land and livestock).
  const fact = n => (n <= 1 ? 1 : n * fact(n - 1));
  function game(players, pairs) {
    const n = players.length, nf = fact(n), w = Array.from({ length: n }, (_, s) => fact(s) * fact(n - s - 1) / nf);
    const toMask = sub => players.reduce((m, p, i) => (sub >> i & 1 ? m | p : m), 0);
    const SM = Array.from({ length: 1 << n }, (_, s) => toMask(s)), pc = s => { let c = 0; while (s) { c += s & 1; s >>= 1; } return c; };
    const K = n + pairs.length, mean = new Float64Array(NC * K), sq = new Float64Array(NC * K), sum = new Float64Array(NC * K);
    const mn = new Float64Array(NC * K).fill(Infinity), mx = new Float64Array(NC * K).fill(-Infinity);
    for (let ci = 0; ci < NC; ci++) {
      for (let i = 0; i < n; i++) { let t = 0; for (let s = 0; s < 1 << n; s++) if (!(s >> i & 1)) t += w[pc(s)] * (v(SM[s | 1 << i], ci) - v(SM[s], ci)); mean[ci * K + i] = t; }
      pairs.forEach(([a, b], j) => { mean[ci * K + n + j] = mean[ci * K + a] + mean[ci * K + b]; });
    }
    // Heap's algorithm over the orderings; each ordering's chain of subset masks is formed once and used for all 120 cells
    const perm = [...Array(n).keys()], c = new Array(n).fill(0), chain = new Int32Array(n + 1), x = new Float64Array(n);
    const visit = () => {
      let m = 0; for (let i = 0; i < n; i++) { chain[i] = m; m |= players[perm[i]]; } chain[n] = m;
      for (let ci = 0; ci < NC; ci++) {
        const b = ci * K;
        for (let i = 0; i < n; i++) x[perm[i]] = V[chain[i + 1] * NC + ci] - V[chain[i] * NC + ci];
        for (let i = 0; i < K; i++) {
          const e = i < n ? x[i] : x[pairs[i - n][0]] + x[pairs[i - n][1]], d = e - mean[b + i];
          sum[b + i] += e; sq[b + i] += d * d; if (e < mn[b + i]) mn[b + i] = e; if (e > mx[b + i]) mx[b + i] = e;
        }
      }
    };
    visit(); let i = 1, count = 1;
    while (i < n) { if (c[i] < i) { const j = i % 2 ? c[i] : 0; [perm[j], perm[i]] = [perm[i], perm[j]]; visit(); count++; c[i]++; i = 1; } else { c[i] = 0; i++; } }
    if (count !== nf) throw new Error(`enumerated ${count} orderings, expected ${nf}`);
    let worstMean = 0, worstEff = 0;
    for (let ci = 0; ci < NC; ci++) {
      for (let k = 0; k < K; k++) worstMean = Math.max(worstMean, Math.abs(sum[ci * K + k] / nf - mean[ci * K + k]));
      let t = 0; for (let k = 0; k < n; k++) t += mean[ci * K + k];
      worstEff = Math.max(worstEff, Math.abs(t - (v(FULL, ci) - v(0, ci))));
    }
    return { n, K, nf, mean, sd: sq.map(s => Math.sqrt(s / nf)), mn, mx, worstMean, worstEff };
  }
  const t1 = Date.now();
  const G9 = game(NAMES.map((_, i) => 1 << i), [[LAND, LIVE]]);
  const P8 = [(1 << LAND) | (1 << LIVE), ...NAMES.map((_, i) => i).filter(i => i !== LAND && i !== LIVE).map(i => 1 << i)];
  const N8 = [COMB, ...NAMES.filter((_, i) => i !== LAND && i !== LIVE)];
  const G8 = game(P8, []);
  console.log(`orderings enumerated: nine layers ${G9.nf}, eight (land and livestock as one) ${G8.nf}, in ${((Date.now() - t1) / 1000).toFixed(0)} s`);
  const TOLM = 1e-3;                                                                          // people: enumeration mean against the subset formula (sums of 362,880 terms)
  console.log(`checks: Shapley values add to 2025 minus 2011, worst ${G9.worstEff.toExponential(1)} (nine) and ${G8.worstEff.toExponential(1)} (eight) people (tolerance 1e-6); enumeration mean against the subset formula, worst ${G9.worstMean.toExponential(1)} and ${G8.worstMean.toExponential(1)} people (tolerance ${TOLM})`);
  if (G9.worstEff > 1e-6 || G8.worstEff > 1e-6 || G9.worstMean > TOLM || G8.worstMean > TOLM) { console.error('CHECK FAILED'); process.exit(1); }

  // forward and reverse in the eight-layer game: land and livestock enter together at land's place (first); reverse is that order backwards
  const walkPlayers = (pl, o, ci) => { let m = 0; const eff = new Array(pl.length); for (const p of o) { const m2 = m | pl[p]; eff[p] = Math.round(v(m2, ci)) - Math.round(v(m, ci)); m = m2; } return eff; };
  const F9 = NAMES.map((_, i) => i), R9 = [...F9].reverse(), F8 = P8.map((_, i) => i), R8 = [...F8].reverse();
  const COLS = ['layer', 'preset', 'forward', 'reverse', 'shapley_mean', 'shapley_sd', 'zone', 'zone_name', 'game', 'orderings', 'shapley_min', 'shapley_max'];
  const rows = [], rec = {};
  for (let ci = 0; ci < NC; ci++) {
    const z = ZONES[ci >> 1], p = PRESETS[ci & 1], nm = `"${label[ci >> 1]}"`, tot = Math.round(v(FULL, ci)) - Math.round(v(0, ci));
    const f9 = walkPlayers(NAMES.map((_, i) => 1 << i), F9, ci), r9 = walkPlayers(NAMES.map((_, i) => 1 << i), R9, ci), f8 = walkPlayers(P8, F8, ci), r8 = walkPlayers(P8, R8, ci);
    const add = (g, G, k, name, f, r, gname) => { const b = ci * G.K + k, row = { layer: name, preset: p, forward: f, reverse: r, shapley_mean: Math.round(G.mean[b]), shapley_sd: Math.round(G.sd[b]), zone: z, zone_name: nm, game: gname, orderings: G.nf, shapley_min: Math.round(G.mn[b]), shapley_max: Math.round(G.mx[b]), mean: G.mean[b] }; rows.push(row); (rec[`${z}|${p}|${gname}`] ??= {})[name] = row; };
    NAMES.forEach((name, k) => add(9, G9, k, name, f9[k], r9[k], 'nine_layers'));
    add(9, G9, N, COMB, f9[LAND] + f9[LIVE], r9[LAND] + r9[LIVE], 'nine_layers');
    const addTotal = (G, gname) => { const row = { layer: 'total_change', preset: p, forward: tot, reverse: tot, shapley_mean: tot, shapley_sd: 0, zone: z, zone_name: nm, game: gname, orderings: G.nf, shapley_min: tot, shapley_max: tot, mean: v(FULL, ci) - v(0, ci) }; rows.push(row); rec[`${z}|${p}|${gname}`].total_change = row; };
    addTotal(G9, 'nine_layers');
    N8.forEach((name, k) => add(8, G8, k, name, f8[k], r8[k], 'eight_layers_land_livestock_one'));
    addTotal(G8, 'eight_layers_land_livestock_one');
  }
  // sum checks in whole people: forward and reverse telescope exactly; the rounded Shapley values may differ from the total by rounding only (reported)
  let badWalk = 0, worstRound = 0;
  for (const [k, r] of Object.entries(rec)) {
    const names = k.endsWith('nine_layers') ? NAMES : N8, t = r.total_change.forward;
    for (const col of ['forward', 'reverse']) if (names.reduce((s, nme) => s + r[nme][col], 0) !== t) badWalk++;
    worstRound = Math.max(worstRound, Math.abs(names.reduce((s, nme) => s + r[nme].shapley_mean, 0) - t));
  }
  console.log(`sum check, whole people (${Object.keys(rec).length} zone-preset-game rows): forward and reverse ${badWalk} failures; rounded Shapley values against the total, worst ${worstRound} people (rounding)`);
  if (badWalk) { console.error('CHECK FAILED'); process.exit(1); }
  fs.writeFileSync(new URL('capacity_by_cause_corrected_orders.csv', import.meta.url), [COLS.join(','), ...rows.map(r => COLS.map(c => r[c]).join(','))].join('\n') + '\n');
  console.log(`wrote capacity_by_cause_corrected_orders.csv: ${rows.length} rows`);
  writeOrdersReadme({ rec, NAMES, N8, ZONES, label, start, popMovedZones: rows.filter(r => r.layer === 'infrastructure_land_only' && r.game === 'nine_layers' && (r.forward || r.reverse || r.shapley_min || r.shapley_max)).map(r => `${r.zone}|${r.preset}`), checks: { G9, G8, badWalk, worstRound, total, nmasks: masks.length } });
}

/** README.md section "Decomposition in every order", written from the numbers of orders(); replaces that section only. */
function writeOrdersReadme({ rec, NAMES, N8, ZONES, label, start, popMovedZones, checks }) {
  const sg = x => (x > 0 ? '+' : x < 0 ? '-' : '') + Math.abs(x).toLocaleString('en-AU'), n = x => x.toLocaleString('en-AU');
  const mil = x => Math.abs(x) < 5000 ? `${sg(Math.round(x))} people` : `${x < 0 ? '-' : '+'}${(Math.abs(x) / 1e6).toFixed(2)} million`;      // B123 (X130): an effect that rounds to 0.00 million is printed in people, "-7 people"

  const SHORTNAME = { land_only: 'land', infrastructure_land_only: 'infrastructure land', crop_yields_only: 'crop yields', livestock_only: 'livestock', consumption_only: 'consumption (diet composition without the organic share)',
    organic_update_only: 'organic update', resilience_update_only: 'resilience table', fuel_update_only: 'long-term liquid fuel', red_meat_mix_only: 'red meat mix of the diet', land_and_livestock: 'land and livestock together' };
  const nm = k => SHORTNAME[k] ?? k;
  // ---- the overlap, from the files themselves: livestock_zone.py's lines, and one zone's arithmetic (Avon, zone 50; Australia for the national ratio)
  const lz = fs.readFileSync(path.join(root, 'pipeline/yields/recent/livestock_zone.py'), 'utf8').split('\n');
  const lineOf = re => { const i = lz.findIndex(l => re.test(l)); if (i < 0) throw new Error(`livestock_zone.py: no line matches ${re}`); return i + 1; };
  const L13 = lineOf(/grazing land\s+the 2020-21 ABS grazing area of the zone \(the land layer's pasture\)/), L33 = lineOf(/pasture_km2 = .*data\/2025-land\/default-inputs-short-term\.csv/);
  const L87 = lineOf(/raw_pasture_ha = \{z: v \* 100/), L100 = lineOf(/b\['grazingHa'\] = raw_pasture_ha\[z\]/);
  const lsPy = fs.readFileSync(path.join(root, 'pipeline/yields/livestock.py'), 'utf8').split('\n');
  const lsLine = re => lsPy.findIndex(l => re.test(l)) + 1, LLAND = lsLine(/land=g\(z, 'grazingHa'\) \+ g\(z, 'hayHa'\)/), LMILK = lsLine(/out\['Dairy milk'\]\[z\] = 0\.0 if haD < 100 else milk \/ haD/);
  if (!LLAND || !LMILK) throw new Error('livestock.py: the land or milk line has moved');
  const arc = JSON.parse(fs.readFileSync(path.join(root, 'pipeline/yields/archive_livestock_inputs.json'), 'utf8')).years, yrs = Object.keys(arc);
  const csvOf = f => { const [h, ...ls] = fs.readFileSync(path.join(root, f), 'utf8').trim().split('\n').map(l => l.split(',')); return Object.fromEntries(ls.map(r => [r[h.indexOf('regionId')], Object.fromEntries(h.map((c, i) => [c, r[i]]))])); };
  const d11 = csvOf(resolveRelease('2011-corrected').defaults.short), d25 = csvOf(resolveRelease('2025-land').defaults.short);
  const yRows = read('2025-livestock', 'model.json').meta.yieldRows, MILK = yRows.indexOf(97);   // sheet row 97: Dairy milk (livestock_zone.py ROW: Sheep meat is row 95, then wool, milk, cattle meat)
  const yB = read('2025-yields', 'regions.json').regions, yA = read('2025-livestock', 'regions.json').regions;
  const ov = z => {
    const A11 = yrs.reduce((t, y) => t + arc[y].regions[z].grazingHa + arc[y].regions[z].hayHa, 0) / yrs.length, A25 = +d25[z].pasture * 100 + arc['2010'].regions[z].hayHa;
    const p11 = +d11[z].pasture, p25 = +d25[z].pasture, m0 = yB[z].yield[MILK], m1 = yA[z].yield[MILK];
    return { A11, A25, p11, p25, m0, m1, area: A11 / A25, land: p11 / p25, milk: m1 / m0, out: (m1 * p25) / (m0 * p11) };
  };
  const av = ov('50'), au = ov('1'), r50 = rec['50|short|nine_layers'], r50l = rec['50|long|nine_layers'];
  const natS = rec['1|short|nine_layers'], natL = rec['1|long|nine_layers'], n8S = rec['1|short|eight_layers_land_livestock_one'], n8L = rec['1|long|eight_layers_land_livestock_one'];
  // ---- tables
  const ROWS9 = [...NAMES, 'land_and_livestock'];
  const tbl = (p, r9, r8) => `| ${p === 'short' ? 'Short' : 'Long'} term, Australia, people | Forward | Reverse | All-orderings average | SD over orderings | Lowest to highest over orderings |
|---|---|---|---|---|---|
| Capacity 2011, corrected (\`2011-fixed\`): ${n(cap(p, 'capacity_2011'))}; 2025 (\`2025-fixed\`): ${n(cap(p, 'all_2025'))} | | | | | |
${ROWS9.map(k => { const r = r9[k]; return `| ${k === 'land_and_livestock' ? '**Land and livestock together** (sum of the two rows)' : nm(k)[0].toUpperCase() + nm(k).slice(1)} | ${sg(r.forward)} | ${sg(r.reverse)} | ${sg(r.shapley_mean)} | ${n(r.shapley_sd)} | ${sg(r.shapley_min)} to ${sg(r.shapley_max)} |`; }).join('\n')}
| **Land and livestock as one layer** (eight-layer average) | ${sg(r8.land_and_livestock.forward)} | ${sg(r8.land_and_livestock.reverse)} | ${sg(r8.land_and_livestock.shapley_mean)} | ${n(r8.land_and_livestock.shapley_sd)} | ${sg(r8.land_and_livestock.shapley_min)} to ${sg(r8.land_and_livestock.shapley_max)} |
| Total, 2025-fixed minus 2011-fixed | ${sg(r9.total_change.forward)} | ${sg(r9.total_change.reverse)} | ${sg(r9.total_change.shapley_mean)} | | |`;
  function cap(p, col) { const l = fs.readFileSync(new URL('capacity_by_cause_corrected.csv', import.meta.url), 'utf8').split('\n'), h = l[0].split(','), row = l.find(x => x.startsWith('corrected,1,') && x.includes(`,${p},`)).match(/("[^"]*"|[^,]+)/g); return +row[h.indexOf(col)]; }
  // ---- ranking on the average
  const rank = r => NAMES.filter(k => r[k].shapley_mean !== 0).sort((a, b) => Math.abs(r[b].shapley_mean) - Math.abs(r[a].shapley_mean));
  const rank8 = r => N8.filter(k => r[k].shapley_mean !== 0).sort((a, b) => Math.abs(r[b].shapley_mean) - Math.abs(r[a].shapley_mean));
  const list = (r, ks, oneLayer = false) => ks.map(k => `${oneLayer && k === 'land_and_livestock' ? 'land and livestock as one layer' : nm(k)} ${mil(r[k].shapley_mean)}`).join(', ');      // B123: in the long-term eight-layer order the combined layer is named "as one layer", not "together" (V37)
  const share = (r, k) => `${Math.round(100 * r[k].shapley_mean / r.total_change.shapley_mean)}%`;
  // ---- regions (the 52 NRM regions and the Northern Territory)
  const REG = ZONES.filter(z => start.regions[z].kind === 'region' || z === '60');
  const top = (r, ks, col) => ks.reduce((a, k) => (Math.abs(r[k][col]) > Math.abs(r[a][col]) ? k : a));
  const tally = (p, game, ks, col) => { const c = {}; for (const z of REG) { const t = top(rec[`${z}|${p}|${game}`], ks, col); c[t] = (c[t] ?? 0) + 1; } return Object.entries(c).sort((a, b) => b[1] - a[1]).map(([k, x]) => `${nm(k)} in ${x}`).join(', '); };
  const flips = (p, col) => REG.filter(z => { const r = rec[`${z}|${p}|nine_layers`]; return top(r, NAMES, col) !== top(r, NAMES, 'shapley_mean'); }).length;
  const spread = p => { let w = { d: -1 }; for (const z of REG) for (const k of NAMES) { const r = rec[`${z}|${p}|nine_layers`][k], d = Math.abs(r.forward - r.reverse); if (d > w.d) w = { d, z, k, r }; } return w; };
  const natSpread = (r, ks) => ks.reduce((a, k) => (Math.abs(r[k].forward - r[k].reverse) > Math.abs(r[a].forward - r[a].reverse) ? k : a));
  const ws = spread('short'), wl = spread('long'), nsS = natSpread(natS, NAMES), nsL = natSpread(natL, NAMES);
  const sec = `## Decomposition in every order (B111)

Written by \`decompose_corrected.mjs --average\` (brief B111, decision 101; R03a issues 2 and 4). The table for all 60 zones and both presets is \`capacity_by_cause_corrected_orders.csv\` (columns: layer, preset, forward, reverse, shapley_mean, shapley_sd, zone, then zone_name, game, orderings, shapley_min, shapley_max; people, whole numbers). \`capacity_by_cause_corrected.csv\` and the section above are unchanged; its forward walk is reproduced here to the person. \`node decompose_corrected.mjs --order reverse\` (or any order of the nine layers, comma-separated) prints one order and writes nothing.

**Land and livestock overlap.** The 2025 livestock yields are output divided by the 2025 land layer's grazing area: \`pipeline/yields/recent/livestock_zone.py\` line ${L13} ("the 2020-21 ABS grazing area of the zone (the land layer's pasture)"), line ${L33} (reads \`pasture\` from \`data/2025-land/default-inputs-short-term.csv\`), line ${L87} (km2 to ha) and line ${L100} (\`b['grazingHa'] = raw_pasture_ha[z]\`); \`pipeline/yields/livestock.py\` line ${LLAND} adds hay to it as the zone's grazing land and line ${LMILK} divides milk by the dairy share of that land. The 2011 rows divided each archive year's output by that year's grazing area (\`pipeline/yields/archive_livestock_inputs.json\`). One zone, Avon (zone 50): the land layer cuts its pasture from ${n(av.p11)} to ${n(av.p25)} km2 (2011 over 2025: ${av.land.toFixed(3)}), and the livestock denominator falls from ${n(Math.round(av.A11))} ha (five-year mean of grazing and hay, ${yrs[0]} to ${yrs.at(-1)} archive years) to ${n(Math.round(av.A25))} ha (2025 pasture plus the 2010 hay), a ratio of ${av.area.toFixed(3)}. The milk yield rises ${av.milk.toFixed(3)} times (sheet row 97, ${av.m0.toFixed(2)} to ${av.m1.toFixed(2)} g/m2), which is the area ratio ${av.area.toFixed(3)} times ${(av.milk / av.area).toFixed(3)}; milk yield times pasture, the land layer's area times the livestock layer's yield, changes only ${av.out.toFixed(3)} times. So at fixed 2011 yields the land layer's cut (Avon short term ${sg(r50.land_only.forward)} forward) is largely returned by the livestock layer (${sg(r50.livestock_only.forward)}); together ${sg(r50.land_and_livestock.forward)} (long term ${sg(r50l.land_only.forward)}, ${sg(r50l.livestock_only.forward)}, together ${sg(r50l.land_and_livestock.forward)}). For Australia the two ratios are ${au.land.toFixed(3)} (land layer pasture, ${n(au.p11)} to ${n(au.p25)} km2) and ${au.area.toFixed(3)} (livestock denominator). Where feedlot grain is part of a yield's land (cattle and sheep meat) or cropland binds, the area cancels only in part. This is why both layers are reported together below.

**Method.** A layer is the set of inputs its release changes against the release before it in the 2025 chain: region inputs and yields, and workbook cells. Any subset of the nine layers is the corrected 2011 start (\`2011-fixed\`) with those changes applied, so the ${checks.nmasks} subsets give every state that any ordering passes through, and each layer's effect in an ordering is the capacity after it minus the capacity before it. Three inputs are shared and follow a rule: non-agricultural land is the remainder of the total area (as \`pipeline/land/make_defaults_2025.py\` builds it), with the 2025 total when the land layer is in and the 2011 total when not; the short-term organic share belongs to the organic layer, as in the forward walk; the animal-product yield rows belong to livestock (without it they are the crop-yield release's 6-figure rewrite of the 2011 rows). Every one of the 9! = ${n(checks.G9.nf)} orderings is evaluated, in every zone and both presets: no sampling, so the regions use the same exact average as Australia. The all-orderings average is each layer's Shapley value (Kitagawa 1955 and Das Gupta 1993 use the same idea for two and more factors); the SD is the standard deviation of the layer's effect over the ${n(checks.G9.nf)} orderings, and the range its lowest and highest. Forward and reverse are the cumulative walk in chain order and in the opposite order, differences of rounded capacities, so they add up to the total to the person. Land and livestock are reported twice: as the sum of their two rows (per ordering, so it has its own SD), and as one layer in an eight-layer average over all 8! = ${n(checks.G8.nf)} orderings, entering at land's place (first) in the forward order. In the eight-layer average the other layers move a little: ${N8.filter(k => k !== 'land_and_livestock' && (n8S[k].shapley_mean !== natS[k].shapley_mean || n8L[k].shapley_mean !== natL[k].shapley_mean)).map(k => `${nm(k)} ${sg(n8S[k].shapley_mean)} short, ${sg(n8L[k].shapley_mean)} long`).join('; ')} (Australia; csv rows with game \`eight_layers_land_livestock_one\`).

${tbl('short', natS, n8S)}

${tbl('long', natL, n8L)}

**What accounts for the 2011 to 2025 change on the all-orderings average.**
* Short term, Australia, ${sg(natS.total_change.shapley_mean)} people: ${list(natS, rank(natS))}. The largest layer by the average is **${nm(rank(natS)[0])}** (${mil(natS[rank(natS)[0]].shapley_mean)}, ${share(natS, rank(natS)[0])} of the change). Land and livestock together account for ${mil(natS.land_and_livestock.shapley_mean)} (${share(natS, 'land_and_livestock')}; as one layer ${mil(n8S.land_and_livestock.shapley_mean)}); the consumption and red-meat-mix layers for ${mil(natS.consumption_only.shapley_mean + natS.red_meat_mix_only.shapley_mean)} (${Math.round(100 * (natS.consumption_only.shapley_mean + natS.red_meat_mix_only.shapley_mean) / natS.total_change.shapley_mean)}%; the consumption layer also carries the short-term fuel, biofuel and timber presets, so it is not wholly diet). With land and livestock as one layer the order is ${list(n8S, rank8(n8S))}.
* Long term, Australia, ${sg(natL.total_change.shapley_mean)} people: ${list(natL, rank(natL))}. The largest layer by the average is **${nm(rank(natL)[0])}** (${mil(natL[rank(natL)[0]].shapley_mean)}). Land and livestock together (the sum of the two rows) account for ${mil(natL.land_and_livestock.shapley_mean)} (as one layer ${mil(n8L.land_and_livestock.shapley_mean)}). With land and livestock as one layer the order is ${list(n8L, rank8(n8L), true)}.
* How much the order moves a layer, Australia: the largest gap between forward and reverse is ${nm(nsS)} in the short term (${sg(natS[nsS].forward)} forward, ${sg(natS[nsS].reverse)} reverse) and ${nm(nsL)} in the long term (${sg(natL[nsL].forward)}, ${sg(natL[nsL].reverse)}).
* Regions (the 52 NRM regions and the Northern Territory), largest layer by the average: short term ${tally('short', 'nine_layers', NAMES, 'shapley_mean')}; long term ${tally('long', 'nine_layers', NAMES, 'shapley_mean')}. With land and livestock as one layer: short term ${tally('short', 'eight_layers_land_livestock_one', N8, 'shapley_mean')}; long term ${tally('long', 'eight_layers_land_livestock_one', N8, 'shapley_mean')}. The forward walk names a different largest layer from the average in ${flips('short', 'forward')} regions short term and ${flips('long', 'forward')} long term; the reverse walk in ${flips('short', 'reverse')} and ${flips('long', 'reverse')}. The largest forward-reverse gap in any region is ${nm(ws.k)} in ${label[ZONES.indexOf(ws.z)]} short term (${sg(ws.r.forward)} against ${sg(ws.r.reverse)}) and ${nm(wl.k)} in ${label[ZONES.indexOf(wl.z)]} long term (${sg(wl.r.forward)} against ${sg(wl.r.reverse)}).
* Infrastructure land moves capacity in ${popMovedZones.length ? popMovedZones.join('; ') : 'no zone'} (zone|preset), in some ordering.

**Check.** The forward prefixes rebuild the ten walk states input by input; the forward effects, start and end equal \`capacity_by_cause_corrected.csv\` in all 120 zone-preset cells to the person; the ${n(checks.total)} distinct evaluations cover all ${checks.nmasks} subsets; forward and reverse add to the total to the person in every zone, preset and game (${checks.badWalk} failures); the averages add to the unrounded total with a worst residual of ${checks.G9.worstEff.toExponential(1)} people (nine layers) and ${checks.G8.worstEff.toExponential(1)} (eight), against a tolerance of 1e-6; the mean over the enumerated orderings equals the subset-formula Shapley value with a worst difference of ${Math.max(checks.G9.worstMean, checks.G8.worstMean).toExponential(1)} people (tolerance 1e-3); the rounded averages add to the rounded total within ${checks.worstRound} people (rounding only).
`;
  const readme = new URL('README.md', import.meta.url), old = fs.readFileSync(readme, 'utf8'), head = '\n## Decomposition in every order (B111)', at = old.indexOf(head);
  const after = at < 0 ? -1 : old.indexOf('\n## ', at + 1);
  fs.writeFileSync(readme, (at < 0 ? old.replace(/\n*$/, '\n') + '\n' : old.slice(0, at + 1)) + sec + (after < 0 ? '' : old.slice(after)));
  console.log('README.md: section "Decomposition in every order (B111)" written');
}
