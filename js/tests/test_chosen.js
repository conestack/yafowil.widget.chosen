import {ChosenWidget} from "../src/widget.js";
import {register_array_subscribers} from "../src/widget.js";

QUnit.module('chosen', hooks => {
    let el, wid, container;
    let _array_subscribers = {
        on_add: []
    };

    hooks.beforeEach(() => {
        container = $('<div class="container" />').appendTo('body');
        el = $('<select class="chosen" />');
    });

    hooks.afterEach(() => {
        el.remove();
        container.empty().remove();
        wid = null;
    });

    QUnit.test('init', assert => {
        let wid = new ChosenWidget(el);
        assert.ok(wid);
        assert.deepEqual(wid.elem, el);
    });

    QUnit.module('search field', hooks => {
        let input;

        hooks.beforeEach((assert) => {
            el.appendTo(container);
            let search_field = $('<div class="search-field" />').appendTo(container);
            input = $('<input type="text"></input>').appendTo(search_field);
            el.on('chosen:updated', (e) => {
                assert.step('chosen updated');
            })
    
            el.data('new_values', true);
            el.data('multivalued', true);
            el.data('search_contains', true);
            el.data('vocabulary', ['foo', 'bar']);
            wid = new ChosenWidget(el);
        });

        QUnit.test('change_handle', assert => {
            assert.ok(wid);
            input.val('f').trigger('change');
            let opt = $('option', el);
            assert.strictEqual(opt.length, 1);
            assert.strictEqual(opt.val(), 'f');
            assert.verifySteps(['chosen updated']);

            // returns
            input.val('').trigger('change');
            opt = $('option', el);
            assert.strictEqual(opt.length, 1);
            assert.verifySteps([]);

            input.val('f').trigger('change');
            opt = $('option', el);
            assert.strictEqual(opt.length, 1);
            assert.strictEqual(opt.val(), 'f');
            assert.verifySteps([]);

            // ignores
            input.val('b').trigger('change');
            let opts = $('option', el);
            assert.strictEqual(opts.length, 2);
            assert.verifySteps(['chosen updated']);
        });

        QUnit.test('keyup_handle', assert => {
            assert.ok(wid);
            input.val('b');
            let keyup = $.Event('keyup');
            keyup.which = 13;
            input.trigger(keyup);
            assert.verifySteps(['chosen updated']);

            let keyup2 = $.Event('keyup');
            keyup2.which = 12;
            input.trigger(keyup2);
            assert.verifySteps([]);
        });
    });

    QUnit.test('register_array_subscribers', assert => {
        // return if window.yafowil === undefined
        register_array_subscribers();
        assert.deepEqual(_array_subscribers['on_add'], []);

        // patch yafowil_array
        window.yafowil_array = {
            on_array_event: function(evt_name, evt_function) {
                _array_subscribers[evt_name] = evt_function;
            }
        };
        register_array_subscribers();

        // create table DOM
        let table = $('<table />')
            .append($('<tr />'))
            .append($('<td />'))
            .appendTo('body');

        $('td', table).addClass('arraytemplate');
        el.appendTo($('td', table));

        // invoke array on_add - returns
        _array_subscribers['on_add'].apply(null, $('tr', table));
        wid = el.data('yafowil-chosen');
        assert.notOk(wid);
        $('td', table).removeClass('arraytemplate');

        // invoke array on_add
        el.attr('id', '');
        _array_subscribers['on_add'].apply(null, $('tr', table));
        wid = el.data('yafowil-chosen');
        assert.ok(wid);

        table.remove();
    });
})


