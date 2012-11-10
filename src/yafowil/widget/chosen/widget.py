from yafowil.base import factory
from yafowil.common import (
    select_extractor,
    generic_required_extractor,
    select_edit_renderer,
    select_display_renderer,
)


factory.register(
    'chosen',
    extractors=[select_extractor, generic_required_extractor],
    edit_renderers=[select_edit_renderer],
    display_renderers=[select_display_renderer])

factory.doc['blueprint']['chosen'] = \
"""Add-on blueprint `yafowil.widget.chosen
<http://github.com/bluedynamics/yafowil.widget.chosen/>`_ .
"""


factory.defaults['chosen.multivalued'] = True
factory.defaults['chosen.size'] = None
factory.defaults['chosen.default'] = []
factory.defaults['chosen.format'] = 'block'
factory.defaults['chosen.class'] = 'chosen'
