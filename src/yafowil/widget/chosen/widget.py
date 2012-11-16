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
    attr_value
)


@managedprops('search_contains', 'new_values')
def chosen_edit_wrapper_renderer(widget, data):
    # add options
    chosen_options = [
        'new_values',
        'allow_single_deselect',
        'disable_search_threshold',
        'disable_search',
        'search_contains',
        'single_backstroke_delete',
        'max_selected_options',
        'placeholder_text',
        'no_results_text',
    ]

    wrapper_attrs = {}
    for key in chosen_options:
        val = attr_value(key, widget, data)
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
factory.defaults['chosen.new_values'] = False;
factory.doc['props']['chosen.'] = \
"""Allow adding new values. [True|False]
"""

factory.defaults['chosen.allow_single_deselect'] = None;
factory.doc['props']['chosen.allow_single_deselect'] = \
"""Allow deselection of single elements.
"""

factory.defaults['chosen.disable_search_threshold'] = None;
factory.doc['props']['chosen.disable_search_threshold'] = \
"""Disable the threshold, when the search popup opens.
"""

factory.defaults['chosen.disable_search'] = None;
factory.doc['props']['chosen.disable_search'] = \
"""Disable search at all.
"""

factory.defaults['chosen.search_contains'] = None;
factory.doc['props']['chosen.search_contains'] = \
"""Search also for substrings. Allowed values [True|False|None]. When using
None or just not setting this value, the default of the Javascript widget is
used.
"""

factory.defaults['chosen.single_backstroke_delete'] = None;
factory.doc['props']['chosen.single_backstroke_delete'] = \
"""A single backstroke deletes the selected option.
"""

factory.defaults['chosen.max_selected_options'] = None;
factory.doc['props']['chosen.max_selected_options'] = \
"""Maximum number of selected options.
"""

factory.defaults['chosen.placeholder_text'] = None;
factory.doc['props']['chosen.placeholder_text'] = \
"""Placeholder text.
"""

factory.defaults['chosen.no_results_text'] = None;
factory.doc['props']['chosen.no_results_text'] = \
"""Text for no results.
"""


