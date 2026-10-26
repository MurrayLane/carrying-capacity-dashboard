import test from 'node:test';
import assert from 'node:assert/strict';
import { decodeState, encodeState, DEFAULT_STATE } from '../src/state.js';

test('an empty hash decodes to the default state, with no typed population', () => {
  const st = decodeState('', [1, 2, 3]);
  assert.equal(st.population, null);
  assert.equal(st.zone, 1);
  assert.deepEqual(st.land, {});
});

test('a typed population round-trips, including zero', () => {
  assert.equal(decodeState('#z=2&pop=1500', [1, 2]).population, 1500);
  assert.equal(decodeState('#z=2&pop=0', [1, 2]).population, 0);
  assert.equal(decodeState(`#${encodeState({ ...DEFAULT_STATE, population: 42 })}`, [1]).population, 42);
});

test('unknown zones fall back to Australia', () => {
  assert.equal(decodeState('#z=999', [1, 2]).zone, 1);
});
