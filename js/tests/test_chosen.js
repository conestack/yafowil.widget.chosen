import { ChosenWidget } from "../src/widget";

let _array_subscribers = {
    on_add: []
}

window.yafowil_array = {
    on_array_event: function(evt_name, evt_function) {
        _array_subscribers[evt_name] = evt_function;
    }
};

QUnit.module('chosen', hooks => {
    let el, wid, container;

    hooks.beforeEach(() => {
        container = $('<div class="container" />').appendTo('body');
        el = $('<select class="chosen" />').appendTo(container);
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

    QUnit.test('search field', assert => {
        let search_field = $('<div class="search-field" />').appendTo(container);
        let input = $('<input type="text"></input>').appendTo(search_field);
        el.on('chosen:updated', (e) => {
            assert.step('chosen updated');
        })

        el.data('new_values', true);
        el.data('multivalued', true);
        el.data('search_contains', true);
        el.data('vocabulary', ['foo', 'bar']);
        let wid = new ChosenWidget(el);

        assert.ok(wid);
        assert.deepEqual(wid.elem, el);

        // change_handle
        input.val('f').trigger('change');
        let opt = $('option', el);
        assert.strictEqual(opt.length, 1);
        assert.strictEqual(opt.val(), 'f');
        assert.verifySteps(['chosen updated']);

        input.val('').trigger('change');
        opt = $('option', el);
        assert.strictEqual(opt.length, 1);
        assert.verifySteps([]);

        input.val('f').trigger('change');
        opt = $('option', el);
        assert.strictEqual(opt.length, 1);
        assert.strictEqual(opt.val(), 'f');
        assert.verifySteps([]);

        // keyup_handle
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

    QUnit.test('init in array', assert => {
        el.attr('id', 'yafowil-TEMPLATE-array');

        // invoke array on_add - returns
        _array_subscribers['on_add'].apply(null, $('body'));
        wid = el.data('yafowil-chosen');
        assert.notOk(wid);

        // invoke array on_add
        el.attr('id', '');
        _array_subscribers['on_add'].apply(null, $('body'));
        wid = el.data('yafowil-chosen');
        assert.ok(wid);
    })
})


