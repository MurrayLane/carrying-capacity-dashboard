// The scenario lives in the URL hash, so a link is a saved scenario and Back undoes a change.
//   #r=2011-corrected&z=15&p=short&o=food:1.5,meategg:0.05&l=cropping:12000&pop=5400000
// r names the release (data and method) the scenario was made with, so a saved link always reproduces what it showed.
// o holds only the parameters the user changed (model units, so percentages are fractions); l and pop hold typed land and population.
import { PARAMS, LAND_KEYS } from './params.js';

export const DEFAULT_STATE = { release: null, zone: 1, preset: 'short', overrides: {}, land: {}, population: null };

const num = s => { if (s == null || s === '') return null; const v = Number(s); return Number.isFinite(v) ? v : null; };
const pairs = s => (s ? s.split(',').map(x => x.split(':')) : []);

export function encodeState(st) {
  const q = new URLSearchParams();
  if (st.release) q.set('r', st.release);
  q.set('z', st.zone); q.set('p', st.preset);
  const o = Object.entries(st.overrides).map(([k, v]) => `${k}:${+v.toPrecision(10)}`).join(',');
  if (o) q.set('o', o);
  const l = Object.entries(st.land).map(([k, v]) => `${k}:${Math.round(v)}`).join(',');
  if (l) q.set('l', l);
  if (st.population != null) q.set('pop', Math.round(st.population));
  return q.toString();
}

/** Links made before releases existed carry no r and were made against the 2011 data; an empty hash gets the current default. */
export const LEGACY_RELEASE = '2011';
export function releaseFromHash(hash, manifest) {
  const q = new URLSearchParams((hash || '').replace(/^#/, '')); const ids = manifest.releases.map(r => r.id); const r = q.get('r');
  if (r != null) { if (!ids.includes(r)) throw new Error(`This link was made with version "${r}", which this site does not have. Known versions: ${ids.join(', ')}.`); return r; }
  return [...q.keys()].length ? LEGACY_RELEASE : manifest.default;
}

export function decodeState(hash, validZones, release = null) {
  const q = new URLSearchParams((hash || '').replace(/^#/, ''));
  const st = { release, zone: 1, preset: 'short', overrides: {}, land: {}, population: null };
  const z = num(q.get('z')); if (z != null && validZones.includes(z)) st.zone = z;
  if (q.get('p') === 'long') st.preset = 'long';
  for (const [k, v] of pairs(q.get('o'))) {
    const p = PARAMS[k]; const x = num(v);
    if (p && x != null) st.overrides[k] = Math.min(Math.max(x, p.min / p.ratio), p.max / p.ratio);
  }
  for (const [k, v] of pairs(q.get('l'))) { const x = num(v); if (LAND_KEYS.includes(k) && x != null && x >= 0) st.land[k] = x; }
  const pop = num(q.get('pop')); if (pop != null && pop >= 0) st.population = pop;
  return st;
}

/** The inputs one zone is evaluated with: its own defaults, then the user's changes. Typed land and population apply to the selected zone only. */
export function inputsFor(region, st, selected) {
  const inputs = { ...region.land, ...region.presets[st.preset], population: region.population, ...st.overrides };
  if (selected) { Object.assign(inputs, st.land); if (st.population != null) inputs.population = st.population; }
  return inputs;
}
