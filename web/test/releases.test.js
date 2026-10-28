// Acceptance tests for the other releases, and the lock on every frozen release.
//   2011            baseline.test.js (the original servlet, 120 cases)
//   2011-corrected  differs from 2011 only in the patched default; its own results are locked in baseline/release_2011-corrected.csv
//   2011-thesis     reproduces the capacities in the thesis results workbook (baseline/thesis_totals_capacity.csv)
import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { Evaluator } from '../src/model/evaluator.js';
import { index, resolveRelease, lockDrift } from '../scripts/releases.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const read = p => JSON.parse(fs.readFileSync(path.resolve(here, p), 'utf8'));
const csv = p => fs.readFileSync(path.resolve(here, p), 'utf8').trim().split(/\r?\n/).slice(1).map(l => l.split(','));
const load = id => ({ model: read(`../public/data/${id}/model.json`), regions: read(`../public/data/${id}/regions.json`).regions });
const run = (rel, preset, id, ev) => { const reg = rel.regions[id]; return ev.evaluate(reg, { ...reg.land, ...reg.presets[preset], population: reg.population }).capacity; };
const near = (a, b, tol = 1e-6) => Math.abs(a - b) <= Math.max(0.02, Math.abs(b) * tol);

test('every release in the index exists, and every frozen release still has the inputs it was locked with', () => {
  const idx = index(); assert.ok(idx.order.includes(idx.default), 'the default release is not in the index');
  const dirs = fs.readdirSync(path.resolve(here, '../../releases'), { withFileTypes: true }).filter(d => d.isDirectory()).map(d => d.name).sort();
  assert.deepEqual([...idx.order].sort(), dirs, 'releases/ and releases/index.json disagree');
  for (const id of idx.order) {
    const rel = resolveRelease(id); assert.ok(['frozen', 'current'].includes(rel.status), `${id}: status`);
    if (rel.parent) assert.ok(idx.order.includes(rel.parent), `${id}: parent ${rel.parent} is not a release`);
    if (rel.status === 'frozen') assert.deepEqual(lockDrift(id), [], `release ${id} is frozen but its inputs changed; create a new release instead`);
  }
});

test('2011-corrected differs from 2011 only in the patched long-term textiles default', () => {
  const a = load('2011').regions, b = load('2011-corrected').regions; let changed = 0;
  for (const id of Object.keys(a)) {
    const x = structuredClone(a[id]), y = structuredClone(b[id]);
    if (x.presets.long.fibre !== y.presets.long.fibre) changed++;
    assert.equal(y.presets.long.fibre, 11.5); x.presets.long.fibre = 11.5;
    assert.deepEqual(y, x, `zone ${id} differs beyond the patch`);
  }
  assert.equal(changed, 60);
  assert.deepEqual(load('2011').model.sheets, load('2011-corrected').model.sheets, 'the method must be identical');
});

test('2011-corrected: short-term results equal the 2011 servlet, and all 120 results are locked', () => {
  const rel = load('2011-corrected'), ev = new Evaluator(rel.model), base = read('../../baseline/baseline_2011.json').cases;
  for (const c of Object.values(base)) if (c.preset === 'short') assert.ok(near(run(rel, 'short', c.regionId, ev), c.result.popcc), `short ${c.regionId}`);
  const locked = csv('../../baseline/release_2011-corrected.csv'); assert.equal(locked.length, 120);
  for (const [preset, id, cap] of locked) assert.ok(near(run(rel, preset, +id, ev), +cap, 1e-9), `${preset} ${id}: drifted from the locked result`);
});

test('2011-thesis reproduces all 120 capacities in the thesis results workbook', () => {
  const rel = load('2011-thesis'), ev = new Evaluator(rel.model), rows = csv('../../baseline/thesis_totals_capacity.csv'); assert.equal(rows.length, 120);
  for (const [preset, id, cap] of rows) { const got = run(rel, preset, +id, ev); assert.ok(near(got, +cap, 1e-6), `${preset} ${id}: ${got} vs ${cap}`); }
});

test('the three releases give different results where they should, and Australia agrees closely', () => {
  const e = id => { const r = load(id); return [r, new Evaluator(r.model)]; };
  const [r11, e11] = e('2011'), [rc, ec] = e('2011-corrected'), [rt, et] = e('2011-thesis');
  const s = (r, ev) => run(r, 'short', 1, ev), l = (r, ev) => run(r, 'long', 1, ev);
  assert.equal(s(r11, e11), s(rc, ec));                       // the correction touches only the long-term preset
  assert.notEqual(l(r11, e11), l(rc, ec));
  assert.ok(Math.abs(s(rt, et) / s(r11, e11) - 1) < 0.01);    // thesis and online agree to about 3% nationally
  assert.ok(Math.abs(l(rt, et) / l(r11, e11) - 1) < 0.05);
});

// ---- the 2025 data layers (SCOPE.md D7: one change per release) -----------------------------------------------------------
const LAND = ['cropping', 'pasture', 'nonAg', 'nature1'], POP = ['infrastr1', 'nonAg'];
const strip = (r, ks) => { const x = structuredClone(r); for (const k of ks) delete x.land[k]; return x; };

test('2025-land changes the land and the reserve share, and nothing else', () => {
  const a = load('2011-corrected').regions, b = load('2025-land').regions;
  for (const id of Object.keys(a)) {
    const x = strip(a[id], LAND), y = strip(b[id], LAND);
    for (const p of ['short', 'long']) { delete x.presets[p].nature2; delete y.presets[p].nature2; }
    assert.deepEqual(y, x, `zone ${id}: 2025-land differs beyond land and nature2`);
  }
  assert.deepEqual(load('2011-corrected').model.sheets, load('2025-land').model.sheets, 'the method must be identical');
});

test('2025-population changes population, infrastructure and the remainder, and nothing else', () => {
  const a = load('2025-land').regions, b = load('2025-population').regions;
  for (const id of Object.keys(a)) {
    const x = strip(a[id], POP), y = strip(b[id], POP); delete x.population; delete y.population;
    assert.deepEqual(y, x, `zone ${id}: 2025-population differs beyond population`);
  }
});

test('2025-yields changes yields only, and keeps every zone, row and sign', () => {
  const a = load('2025-population').regions, b = load('2025-yields').regions;
  for (const id of Object.keys(a)) {
    const x = structuredClone(a[id]), y = structuredClone(b[id]); assert.equal(y.yield.length, x.yield.length);
    assert.ok(y.yield.every(v => typeof v === 'number' && v >= 0), `zone ${id}: a yield is negative or not a number`);
    x.yield = y.yield = null; assert.deepEqual(y, x, `zone ${id}: 2025-yields differs beyond yields`);
  }
});

test('2025-livestock changes the eleven animal-product rows and nothing else', () => {
  const a = load('2025-yields'), b = load('2025-livestock'), rows = a.regions[1] && read('../public/data/2025-yields/regions.json').yieldRows;
  const animal = new Set([95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105]);
  for (const id of Object.keys(a.regions)) {
    const x = a.regions[id], y = b.regions[id];
    for (let k = 0; k < x.yield.length; k++) if (!animal.has(rows[k])) assert.equal(y.yield[k], x.yield[k], `zone ${id} row ${rows[k]} changed`);
    assert.ok(y.yield.every(v => typeof v === 'number' && v >= 0), `zone ${id}: a yield is negative`);
    const p = structuredClone(x), q = structuredClone(y); p.yield = q.yield = null; assert.deepEqual(q, p);
  }
});

test('2025-consumption changes the six short-term defaults named in its patches, to the values the proxy script computed, and nothing else', () => {
  const a = load('2025-livestock').regions, b = load('2025-consumption').regions;
  const proposed = read('../../data/2025/consumption_proxies.json').proposed, F = ['meategg', 'redmeat', 'fuel', 'biofuel', 'timber', 'organic'];
  assert.deepEqual(resolveRelease('2025-consumption').patches.filter(p => F.includes(p.field) && p.preset === 'short').map(p => [p.field, p.value]).sort(), F.map(f => [f, proposed[f]]).sort());
  for (const id of Object.keys(a)) {
    const x = structuredClone(a[id]), y = structuredClone(b[id]);
    for (const f of F) { assert.equal(y.presets.short[f], proposed[f]); delete x.presets.short[f]; delete y.presets.short[f]; }
    assert.deepEqual(y, x, `zone ${id}: 2025-consumption differs beyond the six defaults`);
  }
});

test('2025-organic changes only the baseline organic share and the factors of five crops; at the short-term defaults organic has no effect, and the 100% organic long-term result moves', () => {
  const a = load('2025-consumption'), b = load('2025-organic'), f = read('../../data/2025/organic_factors.json');
  assert.deepEqual(b.regions, a.regions, 'the data of 2025-organic is the data of 2025-consumption');
  const diff = []; const sa = a.model.sheets.Yield.cells, sb = b.model.sheets.Yield.cells;
  for (const k of Object.keys(sb)) if (sa[k] !== sb[k]) diff.push(k);
  assert.deepEqual(diff.length, 6, 'six Yield cells differ: E2 and five factors');
  const cell = (r, c) => sb[`${r - 1}:${c}`];
  assert.equal(cell(2, 4), '=Settings!B15-0.07');
  for (const v of Object.values(f.crops)) assert.equal(cell(v.yield_sheet_row, 6), v.factor_2025);
  assert.deepEqual(Object.keys(a.model.sheets).sort(), Object.keys(b.model.sheets).sort());
  const eva = new Evaluator(a.model), evb = new Evaluator(b.model);
  // at the baseline share the yield multiplier is 1: the short-term result equals that of 2025-consumption with the organic default at the old 2%
  for (const z of [1, 2, 26]) {
    const r = a.regions[z], withOld = eva.evaluate(r, { ...r.land, ...r.presets.short, organic: 0.02, population: r.population }).capacity;
    assert.ok(near(run(b, 'short', z, evb), withOld, 1e-9), `short-term zone ${z}: organic at the baseline should have no effect`);
  }
  assert.notEqual(run(b, 'long', 1, evb), run(a, 'long', 1, eva), 'the long-term (100% organic) result should move');
});

test('2025 layers: land sums, remainders are not negative, and the national results move the way the data says', () => {
  const e = id => { const r = load(id); return [r, new Evaluator(r.model)]; };
  const [r0, e0] = e('2011-corrected'), [r1, e1] = e('2025-land'), [r2, e2] = e('2025-population'), [r3, e3] = e('2025-yields');
  for (const r of [r1, r2, r3]) for (const z of Object.values(r.regions)) {
    assert.ok(z.land.nonAg >= 0, `zone ${z.id}: negative non-agricultural land`);
  }
  assert.equal(run(r1, 'long', 1, e1), run(r2, 'long', 1, e2));       // population does not enter the capacity
  assert.ok(run(r3, 'long', 1, e3) > run(r2, 'long', 1, e2), 'higher crop yields raise the long-term capacity');
  assert.ok(run(r1, 'short', 1, e1) < run(r0, 'short', 1, e0), 'less pasture lowers the short-term capacity');
});

test('2025-resilience changes only the resilience table; the short term is unchanged, the 100-year factor for Australia is unchanged, Western Australia and the 20-year factor move', () => {
  const a = load('2025-organic'), b = load('2025-resilience');
  assert.deepEqual(b.regions, a.regions, 'the data of 2025-resilience is the data of 2025-organic');
  assert.deepEqual(b.model.sheets.Yield, a.model.sheets.Yield); assert.deepEqual(b.model.sheets.Settings, a.model.sheets.Settings);
  const ra = a.model.sheets.resilience.cells, rb = b.model.sheets.resilience.cells; const changed = Object.keys(rb).filter(k => ra[k] !== rb[k]);
  assert.ok(changed.length > 0 && changed.length <= 1200, 'only cells of the 8 by 150 table differ');
  for (const k of changed) { const [r, c] = k.split(':').map(Number); assert.ok(r >= 2 && r <= 9 && c >= 2 && c <= 151, `cell ${k} is outside the table`); }
  const eva = new Evaluator(a.model), evb = new Evaluator(b.model);
  for (const z of [1, 2, 26, 49]) assert.equal(run(b, 'short', z, evb), run(a, 'short', z, eva), `short term, zone ${z}`);
  const at = (rel, ev, z, years) => { const r = rel.regions[z]; return ev.evaluate(r, { ...r.land, ...r.presets.long, resilience: years, population: r.population }).capacity; };
  assert.ok(near(at(b, evb, 1, 100), at(a, eva, 1, 100), 1e-5), 'Australia at 100 years is unchanged: the worst year in the record is still 1915');
  assert.ok(at(b, evb, 49, 100) < at(a, eva, 49, 100), 'Western Australia at 100 years is lower');
  assert.ok(at(b, evb, 1, 20) > at(a, eva, 1, 20), 'Australia at 20 years is higher (the recent good years)');
});

test('2025-resilience-loo is an alternate of 2025-resilience: only the resilience table differs, the short term is unchanged, the long term falls by 7% to 10%', () => {
  const a = load('2025-resilience'), b = load('2025-resilience-loo');
  assert.equal(resolveRelease('2025-resilience-loo').parent, '2025-resilience');
  assert.deepEqual(b.regions, a.regions, 'the data is the data of 2025-resilience');
  assert.deepEqual(b.model.sheets.Yield, a.model.sheets.Yield); assert.deepEqual(b.model.sheets.Settings, a.model.sheets.Settings);
  const eva = new Evaluator(a.model), evb = new Evaluator(b.model);
  for (const z of [1, 2, 26, 49]) assert.equal(run(b, 'short', z, evb), run(a, 'short', z, eva), `short term, zone ${z}`);
  for (const z of [1, 15, 26, 49]) { const r = run(b, 'long', z, evb) / run(a, 'long', z, eva); assert.ok(r > 0.88 && r < 0.95, `long term, zone ${z}: ratio ${r.toFixed(3)}`); }
});

test('2025-reserve is an alternate of 2025-resilience: three Settings formulas differ, a region whose reserve already meets the setting is unchanged, and the long term falls where the shortfall is taken from productive land', () => {
  const a = load('2025-resilience'), b = load('2025-reserve');
  assert.equal(resolveRelease('2025-reserve').parent, '2025-resilience');
  assert.deepEqual(b.regions, a.regions, 'the data is the data of 2025-resilience');
  assert.deepEqual(b.model.sheets.Yield, a.model.sheets.Yield); assert.deepEqual(b.model.sheets.resilience, a.model.sheets.resilience);
  const diff = Object.keys(b.model.sheets.Settings.cells).filter(k => a.model.sheets.Settings.cells[k] !== b.model.sheets.Settings.cells[k]);
  assert.equal(diff.length, 3, 'C55, D55 and E55 differ');
  const eva = new Evaluator(a.model), evb = new Evaluator(b.model);
  assert.ok(near(run(b, 'long', 15, evb), run(a, 'long', 15, eva), 1e-9), 'Victoria has no reserve shortfall: unchanged');
  const au = run(b, 'long', 1, evb) / run(a, 'long', 1, eva); assert.ok(au > 0.92 && au < 0.97, `Australia long term ratio ${au.toFixed(3)}`);
  for (const z of [2, 26]) assert.ok(run(b, 'long', z, evb) / run(a, 'long', z, eva) < 0.85, `zone ${z} long term should fall by more than 15%`);
  const sh = run(b, 'short', 1, evb) / run(a, 'short', 1, eva); assert.ok(sh > 0.98 && sh <= 1, `Australia short term ratio ${sh.toFixed(3)}`);
});

test('2025-fuel and its alternate 2025-fuel-ev change only the long-term liquid fuel; the short term is unchanged and the long term rises as the fuel falls', () => {
  const a = load('2025-resilience'), b = load('2025-fuel'), c = load('2025-fuel-ev');
  assert.equal(resolveRelease('2025-fuel').parent, '2025-resilience'); assert.equal(resolveRelease('2025-fuel-ev').parent, '2025-fuel');
  for (const [rel, litres] of [[b, 210], [c, 156]]) {
    for (const id of Object.keys(a.regions)) {
      const x = structuredClone(a.regions[id]), y = structuredClone(rel.regions[id]);
      assert.equal(y.presets.long.fuel, litres, `zone ${id}`); assert.equal(x.presets.long.fuel, 253); x.presets.long.fuel = litres;
      assert.deepEqual(y, x, `zone ${id} differs beyond the long-term fuel`);
    }
    assert.deepEqual(rel.model.sheets, a.model.sheets, 'the method is that of 2025-resilience');
  }
  const ea = new Evaluator(a.model), eb = new Evaluator(b.model), ec = new Evaluator(c.model);
  assert.equal(run(b, 'short', 1, eb), run(a, 'short', 1, ea)); assert.equal(run(c, 'short', 1, ec), run(a, 'short', 1, ea));
  const la = run(a, 'long', 1, ea), lb = run(b, 'long', 1, eb), lc = run(c, 'long', 1, ec);
  assert.ok(la < lb && lb < lc, `long term should rise as the fuel falls: ${la} ${lb} ${lc}`);
  assert.ok(lb > 13.5e6 && lb < 14.6e6, `2025-fuel Australia long term ${lb}`); assert.ok(lc > 16.5e6 && lc < 17.8e6, `2025-fuel-ev Australia long term ${lc}`);
});

test('2025-recycling-stage (line 2) changes only the recycling method and the short-term setting; with recycling off it equals 2025-fuel, with it on the long term is below the thesis credit', () => {
  const a = load('2025-fuel'), b = load('2025-recycling-stage');
  assert.equal(resolveRelease('2025-recycling-stage').parent, '2025-fuel'); assert.deepEqual(resolveRelease('2025-recycling-stage').methods, ['recycling-stage']);
  for (const id of Object.keys(a.regions)) {
    const x = structuredClone(a.regions[id]), y = structuredClone(b.regions[id]);
    assert.equal(x.presets.short.recycling, 0); assert.equal(y.presets.short.recycling, 1); x.presets.short.recycling = 1;
    assert.equal(x.presets.long.recycling, 1); assert.equal(y.presets.long.recycling, 1);
    assert.deepEqual(y, x, `zone ${id} differs beyond the short-term recycling setting`);
  }
  const ea = new Evaluator(a.model), eb = new Evaluator(b.model), land = (rel, k, rec, ev) => { const R = rel.regions[1]; return ev.evaluate(R, { ...R.land, ...R.presets[k], recycling: rec, population: R.population }).capacity; };
  for (const k of ['short', 'long']) assert.equal(Math.round(land(b, k, 0, eb)), Math.round(land(a, k, 0, ea)), `${k}: with recycling off the methods agree`);
  const l1a = land(a, 'long', 1, ea), l1b = land(b, 'long', 1, eb);
  assert.ok(l1b < l1a && l1b > land(a, 'long', 0, ea), `long term, recycling on: ${l1b} against thesis ${l1a}`);
  assert.ok(l1a > 13.9e6 && l1a < 14.2e6 && l1b > 12.5e6 && l1b < 13.0e6, `${l1a} ${l1b}`);
  const s = land(b, 'short', 1, eb); assert.ok(s > land(a, 'short', 0, ea) && s < land(a, 'short', 0, ea) + 0.3e6, `short term ${s}`);
});

test('method modules: a release names them, they apply to any data set, and a converted release builds exactly what it did before', () => {
  assert.deepEqual(resolveRelease('2025-reserve').methods, ['reserve-pro-rata']);
  assert.deepEqual(resolveRelease('2025-improved').methods, ['reserve-pro-rata', 'recycling-stage']); assert.deepEqual(resolveRelease('2011-improved').methods, ['reserve-pro-rata', 'recycling-stage']);
  assert.equal(resolveRelease('2011-improved').parent, '2011-corrected'); assert.equal(resolveRelease('2025-improved').parent, '2025-fuel');
  const res = load('2025-resilience'), rsv = load('2025-reserve'), rs = Object.keys(rsv.model.sheets.Settings.cells);
  const diff = Object.keys(rsv.model.sheets.Settings.cells).filter(k => rsv.model.sheets.Settings.cells[k] !== res.model.sheets.Settings.cells[k]);
  assert.equal(diff.length, 3, 'the reserve module changes three cells of Settings and nothing else'); assert.ok(rs.length > 0);
  for (const sh of Object.keys(res.model.sheets)) if (sh !== 'Settings') assert.deepEqual(rsv.model.sheets[sh], res.model.sheets[sh], `sheet ${sh}`);
  // the same modules on the other data set: only the method cells differ from the data set's own release
  const c = load('2011-corrected'), ci = load('2011-improved'); assert.deepEqual(Object.keys(ci.regions), Object.keys(c.regions));
  for (const id of Object.keys(c.regions)) { const x = structuredClone(c.regions[id]), y = structuredClone(ci.regions[id]); assert.equal(y.presets.short.recycling, 1); x.presets.short.recycling = 1; assert.deepEqual(y, x, `zone ${id}`); }
  const m = load('2025-mirror'), f = load('2025-fuel'); assert.deepEqual(m.model.sheets, f.model.sheets); assert.deepEqual(m.regions, f.regions);
});

test('results/ is current: the committed CSV of a release equals a fresh evaluation, and the two-by-two adds up', async () => {
  const { evaluateRelease, toCsv, comparison, CELLS } = await import('../scripts/results-lib.mjs');
  const dir = path.resolve(here, '../../results'), by = {};
  for (const id of Object.values(CELLS)) {
    by[id] = evaluateRelease(id);
    if (id === '2011-corrected' || id === '2025-improved') assert.equal(fs.readFileSync(path.join(dir, `${id}.csv`), 'utf8'), toCsv(by[id]), `results/${id}.csv is stale: run npm run results`);
  }
  const rows = comparison(by); assert.equal(rows.length, 120);
  for (const r of rows) assert.equal(r.total_change, r.data_effect + r.method_effect_2011_data + r.interaction, `zone ${r.zone} ${r.preset}`);
  const au = rows.find(r => r.zone === 1 && r.preset === 'short'); assert.ok(au.capacity_2011 > 40.3e6 && au.capacity_2011 < 40.6e6 && au.capacity_2025 > 47.9e6 && au.capacity_2025 < 48.1e6);
  const idx = JSON.parse(fs.readFileSync(path.join(dir, 'releases.json'), 'utf8')).releases.map(r => r.id); assert.deepEqual(idx, index().order, 'results/releases.json lists the releases of the index');
});

test('results/method_effects.csv: the effect of each improved-method module alone adds up with their interaction, and the two together are the improved releases', () => {
  const dir = path.resolve(here, '../../results'), rows = csv(path.join(dir, 'method_effects.csv')), cells = csv(path.join(dir, 'comparison_cells.csv'));
  assert.equal(rows.length, 240);                                              // vintage, zone, name, kind, preset, population, base, A, B, both, effA, effB, effBoth, interaction
  for (const r of rows) { const [base, a, b, both, ea, eb, eboth, inter] = r.slice(6).map(Number); assert.equal(ea, a - base); assert.equal(eb, b - base); assert.equal(eboth, both - base); assert.equal(inter, eboth - ea - eb); }
  const au = (v, p) => rows.find(r => r[0] === v && r[1] === '1' && r[4] === p), cc = (p) => cells.find(r => r[0] === '1' && r[3] === p);
  assert.equal(+au('2011', 'short')[9], +cc('short')[7]); assert.equal(+au('2025', 'long')[9], +cc('long')[9]);   // both = capacity_2011_improved / capacity_2025_improved
});
