import os
from yafowil.base import factory


# XXX: use fanstatic
resourcedir = os.path.join(os.path.dirname(__file__), 'resources')

js = [{
    'group': 'multiselect',
    'resource': 'multi-select/js/jquery.multi-select.js',
    'order': 20,
}, {
    'group': 'yafowil.widget.multiselect',
    'resource': 'widget.js',
    'order': 21,
}]

css = [{
    'group': 'multiselect',
    'resource': 'multi-select/css/multi-select.css',
    'order': 20,
}, {
    'group': 'yafowil.widget.multiselect',
    'resource': 'widget.css',
    'order': 21,
}]


def register():
    import widget
    factory.register_theme('default', 'yafowil.widget.multiselect',
                           resourcedir, js=js, css=css)