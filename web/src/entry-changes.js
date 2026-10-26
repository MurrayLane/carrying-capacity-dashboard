import { mountChrome } from './layout.js';
import { mountChanges } from './pages.js';
mountChrome('changes.html');
mountChanges(document.getElementById('app'));
