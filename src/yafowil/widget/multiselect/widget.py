from yafowil.base import factory
from yafowil.common import (
    select_extractor,
    generic_required_extractor,
    select_edit_renderer,
    select_display_renderer,
)


factory.register(
    'multiselect',
    extractors=[select_extractor, generic_required_extractor],
    edit_renderers=[select_edit_renderer],
    display_renderers=[select_display_renderer])

factory.doc['blueprint']['multiselect'] = \
"""Add-on blueprint `yafowil.widget.multiselect
<http://github.com/bluedynamics/yafowil.widget.multiselect/>`_ .
"""


factory.defaults['multiselect.multivalued'] = True
factory.defaults['multiselect.size'] = None
factory.defaults['multiselect.default'] = []
factory.defaults['multiselect.format'] = 'block'
factory.defaults['multiselect.class'] = 'multiselect'

factory.defaults['multiselect.listing_tag'] = 'div'
factory.doc['props']['multiselect.listing_tag'] = """\
Desired rendering tag for selection if selection format is 'single'. Valid
values are 'div' and 'ul'.
"""

factory.defaults['multiselect.listing_label_position'] = 'inner-after'
factory.doc['props']['multiselect.listing_label_position'] = """\
Label position if format is 'single'. Behaves the same way as label widget
position property.
"""

factory.doc['props']['multiselect.vocabulary'] = """\
Vocabulary to be used for the selection list. Expects a dict-like or an
iterable or a callable which returns one of both first. An iterable can consist
out of strings or out of tuples with ``(key, value)``.
"""

factory.doc['props']['multiselect.disabled'] = """\
Disables the whole widget or single selections. To disable the whole widget
set the value to 'True'. To disable single selection pass a iterable of keys to
disable, i.e. ``['foo', 'baz']``. Defaults to False.
"""
