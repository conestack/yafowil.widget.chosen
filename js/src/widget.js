import $ from 'jquery';

export class ChosenWidget {

    static initialize(context) {
        $('select.chosen', context).each(function (event) {
            new ChosenWidget($(this));
        });
    }

    constructor(elem) {
        this.elem = elem;
        elem.chosen(elem.data());
        if (elem.data().new_values === true) {
            let change_handle = this.change_handle.bind(this)
            $('.search-field input', elem.parent()).on('change', change_handle);
        }
    }

    change_handle(evt) {
        evt.preventDefault();
        this.elem.append(`<option selected="selected">${$(evt.currentTarget).val()}</option>`);
        this.elem.trigger('chosen:updated');
    }
}

