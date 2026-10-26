// Release definitions: reads releases/<id>/release.json, resolves `extends`, and checks locked input hashes.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

export const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
export const sha = f => crypto.createHash('sha256').update(fs.readFileSync(path.join(root, f))).digest('hex');
const read = f => JSON.parse(fs.readFileSync(path.join(root, f), 'utf8'));

export const index = () => read('releases/index.json');
export const rawRelease = id => read(`releases/${id}/release.json`);

/** The release with `extends` resolved: own fields win, patches and errata are appended to the parent's. */
export function resolveRelease(id, seen = []) {
  if (seen.includes(id)) throw new Error(`release ${id} extends itself`);
  const r = rawRelease(id); if (r.id !== id) throw new Error(`releases/${id}/release.json has id ${r.id}`);
  if (!r.extends) return r;
  const p = resolveRelease(r.extends, [...seen, id]);
  return { ...p, ...r, model: r.model ?? p.model, defaults: r.defaults ?? p.defaults,
    yieldOverrides: [...(p.yieldOverrides ?? []), ...(r.yieldOverrides ?? [])],
    patches: [...(p.patches ?? []), ...(r.patches ?? [])], errata: [...(r.errata ?? [])], parent: r.extends };
}

/** Every file a release reads, relative to the repository root. */
export function inputFiles(rel) {
  return [rel.model.file, rel.defaults.short, rel.defaults.long, ...(rel.yieldOverrides ?? []).map(o => o.file)];
}
/** Hashes of the current files against the ones recorded in the release; returns the paths that differ. */
export function lockDrift(id) {
  const raw = rawRelease(id), rel = resolveRelease(id), bad = [];
  if (!raw.inputs) return ['(no inputs recorded)'];
  for (const f of inputFiles(rel)) if (raw.inputs[f] !== sha(f)) bad.push(f);
  for (const f of Object.keys(raw.inputs)) if (!inputFiles(rel).includes(f)) bad.push(`${f} (recorded but no longer used)`);
  return bad;
}
