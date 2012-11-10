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
                    element.chosen();

                });

            }
        }
    });


})(jQuery);
