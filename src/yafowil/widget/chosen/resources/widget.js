(function (exports, $) {
    'use strict';

    class ChosenWidget {
        static initialize(context) {
            $('select.chosen', context).each(function (event) {
                new ChosenWidget($(this));
            });
        }
        constructor(elem) {
            this.elem = elem;
            let extra_keys = ['new_values'],
                options = elem.data(),
                options_extra = this.make_options_extra(options, extra_keys);
            elem.chosen(options);
            if (options_extra.new_values === true) {
                let change_handle = this.change_handle.bind(this);
                $(document).on('change', '.search-field input', change_handle);
            }
        }
        make_options_extra(options, extra_keys) {
            let options_extra = {};
            for (let key of extra_keys) {
                options_extra[key] = options[key];
                delete options[key];
            }
            return options_extra;
        }
        change_handle(evt) {
            evt.preventDefault();
            ele = $(evt.target);
            sel = ele.closest('div.controls').find('select.chosen');
            sel.append('<option selected="selected">' + ele.val() + '</option>');
            sel.trigger('liszt:updated');
        }
    }

    $(function() {
        if (window.ts !== undefined) {
            ts.ajax.register(ChosenWidget.initialize, true);
        } else {
            ChosenWidget.initialize();
        }
    });

    exports.ChosenWidget = ChosenWidget;

    Object.defineProperty(exports, '__esModule', { value: true });


    if (window.yafowil === undefined) {
        window.yafowil = {};
    }
    window.yafowil.chosen = exports;


    return exports;

})({}, jQuery);
//# sourceMappingURL=widget.js.map
