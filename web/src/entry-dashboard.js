import { mountChrome } from './layout.js';
import { mountDashboard } from './dashboard.js';
import { h } from './lib.js';
mountChrome('index.html');
const app = document.getElementById('app');
mountDashboard(app).catch(err => { console.error(err); app.replaceChildren(h('div', { class: 'fail' }, h('h2', {}, 'The dashboard could not start'), h('p', {}, String(err && err.message || err)), h('p', {}, 'Try reloading the page. If it keeps failing, report it on the repository.'))); });
