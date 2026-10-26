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

import { releaseFromHash, LEGACY_RELEASE } from '../src/state.js';
const manifest = { default: '2011-corrected', releases: [{ id: '2011-corrected' }, { id: '2011' }, { id: '2011-thesis' }] };

test('a link carries its release; links made before releases existed mean 2011; an empty hash gets the default', () => {
  assert.equal(releaseFromHash('#r=2011-thesis&z=3', manifest), '2011-thesis');
  assert.equal(releaseFromHash('#z=36&p=short', manifest), LEGACY_RELEASE);
  assert.equal(releaseFromHash('', manifest), '2011-corrected');
  assert.throws(() => releaseFromHash('#r=2031&z=3', manifest), /does not have/);
});

test('the release is written into every link and survives a round trip', () => {
  const st = decodeState('#r=2011-thesis&z=15&p=long', [1, 15], '2011-thesis');
  assert.equal(st.release, '2011-thesis');
  assert.match(encodeState(st), /^r=2011-thesis&z=15&p=long/);
  assert.equal(decodeState(`#${encodeState(st)}`, [1, 15], '2011-thesis').zone, 15);
});
