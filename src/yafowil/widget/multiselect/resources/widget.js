/*
 * yafowil multiselect widget
 *
 * Optional: bdajax
 */

if (typeof(window['yafowil']) == "undefined") yafowil = {};

(function($) {

    $(document).ready(function() {
        // initial binding
        yafowil.multiselect.binder();

        // add after ajax binding if bdajax present
        if (typeof(window['bdajax']) != "undefined") {
            $.extend(bdajax.binders, {
                multiselect_binder: yafowil.multiselect.binder
            });
        }
    });

    $.extend(yafowil, {

        multiselect: {

            binder: function(context) {

                $('select.multiselect', context).each(function(event) {

                    var id = $(this).attr('id');
                    var element = $('#' + id);
                    element.multiSelect();

                });

            }
        }
    });


})(jQuery);
