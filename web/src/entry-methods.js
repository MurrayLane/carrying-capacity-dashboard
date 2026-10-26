import { mountChrome } from './layout.js';
import { mountMethods } from './pages.js';
mountChrome('methods.html');
mountMethods(document.getElementById('app'));
