from yafowil.base import (
    factory,
)
from yafowil.common import (
    select_extractor,
    generic_required_extractor,
    select_edit_renderer,
    select_display_renderer,
)
from yafowil.utils import (
    managedprops,
)


@managedprops('search_contains', 'new_values')
def chosen_edit_wrapper_renderer(widget, data):
    # add options
    chosen_options = [
        'new_values',
        'click_test_action',
        'activate_action',
        'mouse_on_container',
        'results_showing',
        'result_highlighted',
        'result_single_selected',
        'allow_single_deselect',
        'disable_search_threshold',
        'disable_search',
        'search_contains',
        'choices',
        'single_backstroke_delete',
        'max_selected_options',
    ]

    wrapper_attrs = {}
    for key in chosen_options:
        val = widget.attrs[key]
        if val is None: continue
        if val is True: val = 'true' # js-ify
        if val is False: val = 'false' # js-ify
        wrapper_attrs['data-%s' % key] = val

    wrapper_attrs['class'] = 'chosen-edit-wrapper'

    # return element (data.rendered) wrapped with chosen_edit_wrapper_renderer
    return data.tag('div', data.rendered, **wrapper_attrs)


factory.register(
    'chosen',
    extractors=[select_extractor, generic_required_extractor],
    edit_renderers=[select_edit_renderer, chosen_edit_wrapper_renderer],
    display_renderers=[select_display_renderer])


factory.doc['blueprint']['chosen'] = \
"""Add-on blueprint `yafowil.widget.chosen
<http://github.com/bluedynamics/yafowil.widget.chosen/>`_ .
"""


factory.defaults['chosen.multivalued'] = False
factory.defaults['chosen.size'] = None
factory.defaults['chosen.default'] = []
factory.defaults['chosen.format'] = 'block'
factory.defaults['chosen.class'] = 'chosen'

# TODO : docs
factory.defaults['chosen.new_values'] = None;
factory.defaults['chosen.click_test_action'] = None;
factory.defaults['chosen.activate_action'] = None;
factory.defaults['chosen.mouse_on_container'] = None;
factory.defaults['chosen.results_showing'] = None;
factory.defaults['chosen.result_highlighted'] = None;
factory.defaults['chosen.result_single_selected'] = None;
factory.defaults['chosen.allow_single_deselect'] = None;
factory.defaults['chosen.disable_search_threshold'] = None;
factory.defaults['chosen.disable_search'] = None;
factory.defaults['chosen.search_contains'] = None;
factory.defaults['chosen.choices'] = None;
factory.defaults['chosen.single_backstroke_delete'] = None;
factory.defaults['chosen.max_selected_options'] = None;
