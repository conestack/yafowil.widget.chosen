from yafowil.base import factory
from yafowil.utils import entry_point
import os


resourcedir = os.path.join(os.path.dirname(__file__), 'resources')
js = [{
    'group': 'yafowil.widget.chosen.dependencies',
    'resource': 'chosen/chosen.jquery.js',
    'order': 20,
}, {
    'group': 'yafowil.widget.chosen.common',
    'resource': 'widget.js',
    'order': 21,
}]
default_css = [{
    'group': 'yafowil.widget.chosen.dependencies',
    'resource': 'chosen/chosen.css',
    'order': 20,
}, {
    'group': 'yafowil.widget.chosen.common',
    'resource': 'widget.css',
    'order': 21,
}]
bootstrap_css = [{
    'group': 'yafowil.widget.chosen.dependencies',
    'resource': 'chosen/chosen-bootstrap.css',
    'order': 20,
}, {
    'group': 'yafowil.widget.chosen.common',
    'resource': 'widget.css',
    'order': 21,
}]


@entry_point(order=10)
def register():
    from yafowil.widget.chosen import widget
    factory.register_theme('default', 'yafowil.widget.chosen',
                           resourcedir, js=js, css=default_css)
    factory.register_theme('bootstrap', 'yafowil.widget.chosen',
                           resourcedir, js=js, css=bootstrap_css)
