import $ from 'jquery';

export class ChosenWidget {

    static initialize(context) {
        $('select.chosen', context).each(function (event) {
            new ChosenWidget($(this));
        });
    }

    constructor(elem) {
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
