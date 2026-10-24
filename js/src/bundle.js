import $ from 'jquery';
import { ChosenWidget, register_array_subscribers } from './widget.js';

export * from './widget.js';

$(() => {
    if (window.ts !== undefined) {
        ts.ajax.register(ChosenWidget.initialize, true);
    } else if (window.bdajax !== undefined) {
        bdajax.register(ChosenWidget.initialize, true);
    } else {
        ChosenWidget.initialize();
    }
    register_array_subscribers();
});
