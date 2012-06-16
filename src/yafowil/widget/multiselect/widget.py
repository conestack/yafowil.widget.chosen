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
