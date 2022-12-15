import { ChosenWidget } from "../src/widget";

window.yafowil_array = undefined;

QUnit.test('test', assert => {
    let el = $('<select class="chosen" />').appendTo('body');
    let wid = new ChosenWidget(el);
    assert.ok(wid);

    el.remove();
    wid = null;
});