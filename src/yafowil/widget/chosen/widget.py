from yafowil.base import factory
from yafowil.common import generic_required_extractor
from yafowil.common import select_display_renderer
from yafowil.common import select_edit_renderer
from yafowil.common import select_extractor
from yafowil.utils import data_attrs_helper
from yafowil.utils import managedprops


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

@managedprops(*chosen_options)
def chosen_edit_renderer(widget, data):
    custom_attrs = data_attrs_helper(widget, data, chosen_options)
    return select_edit_renderer(widget, data, custom_attrs=custom_attrs)

factory.register(
    'chosen',
    extractors=[select_extractor, generic_required_extractor],
    edit_renderers=[chosen_edit_renderer],
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
factory.doc['props']['chosen.new_values'] = \
"""Allow adding new values.
For: yafowil js integration.
Values: [True|False|None (default)].
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


