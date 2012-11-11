/*
 * yafowil chosen widget
 *
 * Optional: bdajax
 */

if (typeof(window['yafowil']) == "undefined") yafowil = {};

(function($) {

    $(document).ready(function() {
        // initial binding
        yafowil.chosen.binder();

        // add after ajax binding if bdajax present
        if (typeof(window['bdajax']) != "undefined") {
            $.extend(bdajax.binders, {
                chosen_binder: yafowil.chosen.binder
            });
        }
    });

    $.extend(yafowil, {

        chosen: {

            binder: function(context) {

                $('select.chosen', context).each(function(event) {

                    var id = $(this).attr('id');
                    var element = $('#' + id);
                    element.chosen({search_contains:true});

                    $(document).on('change','.search-field input',function(e){
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
                    });
                });

            }
        }
    });


})(jQuery);
