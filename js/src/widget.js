import $ from 'jquery';

export class ChosenWidget {
    static initialize(context) {
        $('select.chosen', context).each(function () {
            if (window.yafowil_array?.inside_template($(this))) {
                return;
            }
            new ChosenWidget($(this));
        });
    }

    constructor(elem) {
        elem.data('yafowil-chosen', this);
        this.elem = elem;
        const opts = elem.data();
        elem.chosen(opts);
        if (opts.new_values) {
            const input = $('.search-field input', elem.parent());
            input.on('change', this.change_handle.bind(this));
            input.on('keyup', this.keyup_handle.bind(this));
        }
    }

    change_handle(evt) {
        evt.preventDefault();
        const val = $(evt.currentTarget).val();
        if (!val) {
            return;
        }
        let ignore = false;
        $('option', this.elem).each(function () {
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
        const code = evt.keyCode || evt.which;
        if (code === 13) {
            this.change_handle(evt);
        }
    }
}

//////////////////////////////////////////////////////////////////////////////
// yafowil.widget.array integration
//////////////////////////////////////////////////////////////////////////////

function chosen_on_array_add(_inst, context) {
    ChosenWidget.initialize(context, true);
}

export function register_array_subscribers() {
    if (window.yafowil_array === undefined) {
        return;
    }
    window.yafowil_array.on_array_event('on_add', chosen_on_array_add);
}
