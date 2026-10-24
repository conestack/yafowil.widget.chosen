import $ from 'jquery';
import { ChosenWidget } from '../src/widget.js';

// Capture the DOM ready callback of the bundle instead of letting jQuery run
// it once, so each registration branch can be exercised.
const ready_callbacks = [];
const orig_ready = $.fn.ready;
$.fn.ready = function (fn) {
    ready_callbacks.push(fn);
    return this;
};
const bundle = await import('../src/bundle.js');
$.fn.ready = orig_ready;

QUnit.module('bundle', (hooks) => {
    const orig_initialize = ChosenWidget.initialize;
    let initialized;

    hooks.beforeEach(() => {
        initialized = 0;
        ChosenWidget.initialize = () => {
            initialized++;
        };
    });
    hooks.afterEach(() => {
        ChosenWidget.initialize = orig_initialize;
        delete window.ts;
        delete window.bdajax;
    });

    QUnit.test('exports', (assert) => {
        assert.strictEqual(bundle.ChosenWidget, ChosenWidget);
        assert.strictEqual(typeof bundle.register_array_subscribers, 'function');
        assert.strictEqual(ready_callbacks.length, 1);
    });

    QUnit.test('register with ts', (assert) => {
        const registered = [];
        window.ts = {
            ajax: {
                register: (fn, instant) => {
                    registered.push([fn, instant]);
                },
            },
        };
        ready_callbacks[0]();
        assert.deepEqual(registered, [[ChosenWidget.initialize, true]]);
        assert.strictEqual(initialized, 0);
    });

    QUnit.test('register with bdajax', (assert) => {
        const registered = [];
        window.bdajax = {
            register: (fn, instant) => {
                registered.push([fn, instant]);
            },
        };
        ready_callbacks[0]();
        assert.deepEqual(registered, [[ChosenWidget.initialize, true]]);
        assert.strictEqual(initialized, 0);
    });

    QUnit.test('initialize without ts and bdajax', (assert) => {
        ready_callbacks[0]();
        assert.strictEqual(initialized, 1);
    });
});
