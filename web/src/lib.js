// Small helpers shared by the pages.
export function h(tag, attrs = {}, ...kids) {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v == null || v === false) continue;
    if (k === 'class') el.className = v;
    else if (k === 'html') el.innerHTML = v;                         // trusted content only: help text shipped with the site
    else if (k.startsWith('on')) el.addEventListener(k.slice(2), v);
    else if (k === 'dataset') Object.assign(el.dataset, v);
    else el.setAttribute(k, v === true ? '' : v);
  }
  for (const kid of kids.flat()) if (kid != null && kid !== false) el.append(kid.nodeType ? kid : document.createTextNode(String(kid)));
  return el;
}
const nf0 = new Intl.NumberFormat('en-AU', { maximumFractionDigits: 0 });
const nf1 = new Intl.NumberFormat('en-AU', { maximumFractionDigits: 1 });
export const fmt0 = v => (Number.isFinite(v) ? nf0.format(v) : '–');
export const fmt1 = v => (Number.isFinite(v) ? nf1.format(v) : '–');
export function compact(v) {
  if (!Number.isFinite(v)) return '–'; const a = Math.abs(v);
  if (a >= 1e6) return `${nf1.format(v / 1e6)}M`; if (a >= 1e3) return `${nf1.format(v / 1e3)}K`; return nf1.format(v);
}
export const debounce = (fn, ms) => { let t; return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); }; };
export function store(key, value) { try { if (value === undefined) return localStorage.getItem(key); localStorage.setItem(key, value); } catch { return null; } }
