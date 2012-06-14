from yafowil.base import (
    factory,
    fetch_value,
)
from yafowil.common import (
    generic_extractor,
    generic_required_extractor,
    select_edit_renderer,
)


def multiselect_display_renderer(widget, data):
    value = fetch_value(widget, data)
    if not value:
        value = ''
    return data.tag('div', value, **{'class': 'display-multiselect'})


factory.register(
    'multiselect',
    extractors=[generic_extractor, generic_required_extractor],
    edit_renderers=[select_edit_renderer],
    display_renderers=[multiselect_display_renderer])

factory.doc['blueprint']['multiselect'] = \
"""Add-on blueprint `yafowil.widget.multiselect
<http://github.com/bluedynamics/yafowil.widget.multiselect/>`_ .
"""

factory.defaults['multiselect.default'] = ''
factory.defaults['multiselect.readonly'] = None
factory.defaults['multiselect.multivalued'] = True
factory.defaults['multiselect.class'] = 'multiselect'
