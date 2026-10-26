import { mountChrome } from './layout.js';
import { mountAbout } from './pages.js';
mountChrome('about.html');
mountAbout(document.getElementById('app'));
