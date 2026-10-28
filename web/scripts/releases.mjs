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

export const moduleFile = id => `methods/${id}/method.json`;
export const methodModule = id => { const m = read(moduleFile(id)); if (m.id !== id) throw new Error(`${moduleFile(id)} has id ${m.id}`); return m; };
const mergeOverrides = (a = {}, b = {}) => { const out = structuredClone(a); for (const [sheet, cells] of Object.entries(b)) out[sheet] = { ...(out[sheet] ?? {}), ...cells }; return out; };

/**
 * The release with `extends` resolved: own fields win, patches and errata are appended to the parent's.
 * `methods` lists method modules (methods/<id>/method.json): each is a set of workbook cell overrides, parameter patches and errata that can be applied
 * to any data set. A release inherits its parent's methods and adds its own; the overrides are applied, in order, on top of the model (and its own cell overrides)
 * of the nearest release that names a model, so the same module works on the 2011 and the 2025 data. A module's patches come after the parent's and before the release's own.
 */
export function resolveRelease(id, seen = []) {
  if (seen.includes(id)) throw new Error(`release ${id} extends itself`);
  const r = rawRelease(id); if (r.id !== id) throw new Error(`releases/${id}/release.json has id ${r.id}`);
  const p = r.extends ? resolveRelease(r.extends, [...seen, id]) : null;
  const inherited = p?.methods ?? [], added = (r.methods ?? []).filter(m => !inherited.includes(m)), methods = [...inherited, ...added];
  const baseModel = r.model ?? p?.baseModel;
  const mods = methods.map(methodModule);
  const model = baseModel && { ...baseModel, cellOverrides: mods.reduce((o, m) => mergeOverrides(o, m.cellOverrides), baseModel.cellOverrides ?? {}) };
  const modPatches = added.flatMap(m => methodModule(m).patches ?? []), modErrata = added.flatMap(m => methodModule(m).errata ?? []);
  if (!p) return { ...r, baseModel, methods, model };
  return { ...p, ...r, baseModel, methods, model, defaults: r.defaults ?? p.defaults, yieldMatrix: r.yieldMatrix ?? p.yieldMatrix,
    yieldOverrides: [...(p.yieldOverrides ?? []), ...(r.yieldOverrides ?? [])],
    patches: [...(p.patches ?? []), ...modPatches, ...(r.patches ?? [])], errata: [...modErrata, ...(r.errata ?? [])], parent: r.extends };
}

/** Every file a release reads, relative to the repository root. */
export function inputFiles(rel) {
  return [rel.model.file, rel.defaults.short, rel.defaults.long, ...(rel.yieldMatrix ? [rel.yieldMatrix.file] : []), ...(rel.yieldOverrides ?? []).map(o => o.file), ...(rel.methods ?? []).map(moduleFile)];
}
/** Hashes of the current files against the ones recorded in the release; returns the paths that differ. */
export function lockDrift(id) {
  const raw = rawRelease(id), rel = resolveRelease(id), bad = [];
  if (!raw.inputs) return ['(no inputs recorded)'];
  for (const f of inputFiles(rel)) if (raw.inputs[f] !== sha(f)) bad.push(f);
  for (const f of Object.keys(raw.inputs)) if (!inputFiles(rel).includes(f)) bad.push(`${f} (recorded but no longer used)`);
  return bad;
}
