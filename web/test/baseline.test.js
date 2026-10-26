// Acceptance test for release 2011: the static site's evaluator must reproduce the original 2011 servlet.
// baseline/baseline_2011.json holds the servlet's output for all 120 default cases (60 zones x 2 presets).
import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { Evaluator } from '../src/model/evaluator.js';

const here = path.dirname(fileURLToPath(import.meta.url));
const read = p => JSON.parse(fs.readFileSync(path.resolve(here, p), 'utf8'));
const model = read('../public/data/2011/model.json'), { regions } = read('../public/data/2011/regions.json');
const baseline = read('../../baseline/baseline_2011.json');
const ev = new Evaluator(model);

const PERCENT = new Set(['food', 'meategg', 'redmeat', 'recycling', 'losses', 'organic', 'irrigation', 'biofuel', 'fibreNat', 'fibreWool', 'nature2']);
const FIELD = { inputAreasCropping: 'cropping', inputAreasPasture: 'pasture', inputAreasNonAg: 'nonAg', inputAreasBuilt: 'infrastr1', inputAreasNature: 'nature1',
  inputResilienceYears: 'resilience', inputFoodRatio: 'food', inputMeateggRatio: 'meategg', inputRedmeatRatio: 'redmeat', inputActivityLevel: 'activity',
  inputRecyclingRatio: 'recycling', inputLossesRatio: 'losses', inputOrganicRatio: 'organic', inputIrrigationRatio: 'irrigation', inputFuelTotal: 'fuel',
  inputBiofuelRatio: 'biofuel', inputFibreTotal: 'fibre', inputFibreNaturalRatio: 'fibreNat', inputFibreWoolRatio: 'fibreWool', inputTimber: 'timber',
  inputInfrastructure: 'infrastr2', inputNatureRatio: 'nature2', inputPopulation: 'population' };
// the servlet's own arithmetic: strip separators, divide percentages by 100
const toInputs = form => Object.fromEntries(Object.entries(FIELD).map(([f, k]) => { const v = parseFloat(String(form[f]).replace(/[^\d.\-]/g, '')); return [k, PERCENT.has(k) ? v / 100 : v]; }));
const close = (a, b) => Math.abs(a - b) <= Math.max(0.015, Math.abs(b) * 1e-9);   // the servlet prints two decimals

test('all 120 baseline cases match the original servlet', () => {
  let n = 0;
  for (const [key, c] of Object.entries(baseline.cases)) {
    const r = ev.evaluate(regions[c.regionId], toInputs(c.params)); n++;
    assert.ok(close(r.capacity, c.result.popcc), `${key}: capacity ${r.capacity} vs ${c.result.popcc}`);
    c.result.excess.forEach((e, i) => { assert.ok(close(r.excess[i][0], e[0]), `${key}: excess[${i}] km2`); assert.ok(close(r.excess[i][1], e[1]), `${key}: excess[${i}] %`); });
    c.result.requirements.forEach((q, i) => q.forEach((v, j) => assert.ok(close(r.requirements[i][j], v), `${key}: requirements[${i}][${j}] ${r.requirements[i][j]} vs ${v}`)));
  }
  assert.equal(n, 120);
});

test('the exact defaults the site starts from give the same capacity as the rounded values the 2011 page posted', () => {
  for (const c of Object.values(baseline.cases)) {
    const reg = regions[c.regionId]; const p = reg.presets[c.preset];
    const r = ev.evaluate(reg, { ...reg.land, ...p, population: reg.population });
    assert.ok(Math.abs(r.capacity - c.result.popcc) <= Math.max(0.02, c.result.popcc * 1e-6), `${c.preset} ${reg.name}: ${r.capacity} vs ${c.result.popcc}`);
  }
});
