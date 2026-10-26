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
