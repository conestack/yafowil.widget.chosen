/*
 * yafowil chosen widget
 *
 * Optional: bdajax
 */

if (typeof(window.yafowil) == "undefined") yafowil = {};

(function($) {

    $(document).ready(function() {
        // initial binding
        yafowil.chosen.binder();

        // add after ajax binding if bdajax present
        if (typeof(window.bdajax) != "undefined") {
            $.extend(bdajax.binders, {
                chosen_binder: yafowil.chosen.binder
            });
        }
    });

    $.extend(yafowil, {

        chosen: {

            binder: function(context) {

                $('select.chosen', context).each(function(event) {

                    var extra_keys = ['new_values'];
                    var elem = $(this);
                    var options = elem.data();

                    function make_options_extra(options, extra_keys) {
                        // cleanup api options object and move out extra options
                        var options_extra = {};
                        for (i = 0; i < extra_keys.length; i++) {
                            key = extra_keys[i];
                            options_extra[key] = options[key];
                            delete options[key];
                        }
                        return options_extra;
                    }
                    options_extra = make_options_extra(options, extra_keys);

                    elem.chosen(options);

                    if (options_extra.new_values===true) {
                        // TODO: do something like $(option_el).on('change', '.search-field', function ...
                        //       to allow more than one chosen instance on one
                        //       page
                        $(document).on('change', '.search-field input', function(e) {
                            // allow new values
                            // see http://harvesthq.github.com/chosen/
                            // http://stackoverflow.com/questions/7385246/allow-new-values-with-chosen-js-multiple-select
                            //
                            // TODO: try/test to bind also on keyup/enter
                            e.preventDefault();
                            ele = $(e.target);
                            sel = ele.closest('div.controls').find('select.chosen'); // TODO: can't this be simpler? getting "this" context from surrounding environment?
                            sel.append('<option selected="selected">' + ele.val() + '</option>');
                            sel.trigger('liszt:updated');
                            // TODO: doesn't work
                            // focus search-field
                            //tryout1
                            //ele.focus();
                            //tryout2
                            // rebuilt - so have to find search field again.
                            //sel.closest('div.controls').find('.czn-container .search-field input').focus();
                        });
                    }
                });
            }
        }
    });

})(jQuery);
