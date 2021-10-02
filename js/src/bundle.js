import $ from 'jquery';

import {ChosenWidget} from './widget.js';

export * from './widget.js';

$(function() {
    if (window.ts !== undefined) {
        ts.ajax.register(ChosenWidget.initialize, true);
    } else {
        ChosenWidget.initialize();
    }
});
