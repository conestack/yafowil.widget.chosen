from yafowil.base import factory
from yafowil.utils import entry_point
import os
import webresource as wr


resources_dir = os.path.join(os.path.dirname(__file__), 'resources')
chosen_resources_dir = os.path.join(resources_dir, 'chosen')

##############################################################################
# Common
##############################################################################

# webresource ################################################################

common_scripts = wr.ResourceGroup(name='yafowil-chosen-scripts')
common_scripts.add(wr.ScriptResource(
    name='chosen-js',
    depends='jquery-js',
    directory=chosen_resources_dir,
    path='yafowil-chosen/chosen',
    resource='chosen.jquery.js',
    compressed='chosen.jquery.min.js'
))
common_scripts.add(wr.ScriptResource(
    name='yafowil-chosen-js',
    depends='chosen-js',
    resource='widget.js',
    compressed='widget.min.js'
))

chosen_css = wr.StyleResource(
    name='yafowil-chosen-css',
    depends='chosen-css',
    resource='widget.css'
)

# B/C resources ##############################################################

js = [{
    'group': 'yafowil.widget.chosen.dependencies',
    'resource': 'chosen/chosen.jquery.js',
    'order': 20,
}, {
    'group': 'yafowil.widget.chosen.common',
    'resource': 'widget.js',
    'order': 21,
}]


##############################################################################
# Default
##############################################################################

# webresource ################################################################

default_resources = wr.ResourceGroup(
    name='yafowil-chosen-resources',
    directory=resources_dir,
    path='yafowil-chosen'
)
default_resources.add(common_scripts)
default_resources.add(wr.StyleResource(
    name='chosen-css',
    directory=chosen_resources_dir,
    path='yafowil-chosen/chosen',
    resource='chosen.css',
    compressed='chosen.min.css'
))
default_resources.add(chosen_css)

# B/C resources ##############################################################

default_css = [{
    'group': 'yafowil.widget.chosen.dependencies',
    'resource': 'chosen/chosen.css',
    'order': 20,
}, {
    'group': 'yafowil.widget.chosen.common',
    'resource': 'widget.css',
    'order': 21,
}]


##############################################################################
# Bootstrap
##############################################################################

# webresource ################################################################

bootstrap_resources = wr.ResourceGroup(
    name='yafowil-chosen-resources',
    directory=resources_dir,
    path='yafowil-chosen'
)
bootstrap_resources.add(common_scripts)
bootstrap_resources.add(wr.StyleResource(
    name='chosen-css',
    directory=chosen_resources_dir,
    path='yafowil-chosen/chosen',
    resource='chosen-bootstrap.css'
))
bootstrap_resources.add(chosen_css)

# B/C resources ##############################################################

bootstrap_css = [{
    'group': 'yafowil.widget.chosen.dependencies',
    'resource': 'chosen/chosen-bootstrap.css',
    'order': 20,
}, {
    'group': 'yafowil.widget.chosen.common',
    'resource': 'widget.css',
    'order': 21,
}]


##############################################################################
# Registration
##############################################################################

@entry_point(order=10)
def register():
    from yafowil.widget.chosen import widget  # noqa

    widget_name = 'yafowil.widget.chosen'

    # Default
    factory.register_theme(
        'default',
        widget_name,
        resources_dir,
        js=js,
        css=default_css
    )
    factory.register_resources('default', widget_name, default_resources)

    # Bootstrap
    factory.register_theme(
        ['bootstrap', 'bootstrap3'],
        widget_name,
        resources_dir,
        js=js,
        css=bootstrap_css
    )
    factory.register_resources(
        ['bootstrap', 'bootstrap3'],
        widget_name,
        bootstrap_resources
    )
