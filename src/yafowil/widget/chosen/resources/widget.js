var yafowil_chosen = (function (exports, $) {
    'use strict';

    class ChosenWidget {
        static initialize(context) {
            $('select.chosen', context).each(function (event) {
                if (window.yafowil_array !== undefined &&
                    window.yafowil_array.inside_template($(this))) {
                    return;
                }
                new ChosenWidget($(this));
            });
        }
        constructor(elem) {
            elem.data('yafowil-chosen', this);
            this.elem = elem;
            let opts = elem.data();
            elem.chosen(opts);
            if (opts.new_values) {
                let input = $('.search-field input', elem.parent());
                input.on('change', this.change_handle.bind(this));
                input.on('keyup', this.keyup_handle.bind(this));
            }
        }
        change_handle(evt) {
            evt.preventDefault();
            let val = $(evt.currentTarget).val();
            if (!val) {
                return;
            }
            let ignore = false;
            $('option', this.elem).each(function() {
                if (this.value === val) {
                    ignore = true;
                }
            });
            if (ignore) {
                return;
            }
            this.elem.append(`<option selected="selected">${val}</option>`);
            this.elem.trigger('chosen:updated');
        }
        keyup_handle(evt) {
            let code = evt.keyCode || evt.which;
            if (code == 13) {
                this.change_handle(evt);
            }
        }
    }
    function chosen_on_array_add(inst, context) {
        ChosenWidget.initialize(context, true);
    }
    function register_array_subscribers() {
        if (window.yafowil_array === undefined) {
            return;
        }
        window.yafowil_array.on_array_event('on_add', chosen_on_array_add);
    }

    $(function() {
        if (window.ts !== undefined) {
            ts.ajax.register(ChosenWidget.initialize, true);
        } else if (window.bdajax !== undefined) {
            bdajax.register(ChosenWidget.initialize, true);
        } else {
            ChosenWidget.initialize();
        }
        register_array_subscribers();
    });

    exports.ChosenWidget = ChosenWidget;
    exports.register_array_subscribers = register_array_subscribers;

    Object.defineProperty(exports, '__esModule', { value: true });


    window.yafowil = window.yafowil || {};
    window.yafowil.chosen = exports;


    return exports;

})({}, jQuery);
