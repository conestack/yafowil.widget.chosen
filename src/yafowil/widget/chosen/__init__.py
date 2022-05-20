from yafowil.base import factory
from yafowil.utils import entry_point
import os
import webresource as wr


resources_dir = os.path.join(os.path.dirname(__file__), 'resources')
choses_resources_dir = os.path.join(resources_dir, 'chosen')


##############################################################################
# Common
##############################################################################

# webresource ################################################################

scripts = wr.ResourceGroup(name='scripts')
scripts.add(wr.ScriptResource(
    name='chosen-js',
    depends='jquery-js',
    directory=choses_resources_dir,
    resource='chosen.jquery.js',
    compressed='chosen.jquery.min.js'
))
scripts.add(wr.ScriptResource(
    name='yafowil-chosen-js',
    depends='chosen-js',
    directory=resources_dir,
    resource='widget.js',
    compressed='widget.min.js'
))

common_styles = wr.StyleResource(
    name='yafowil-chosen-css',
    depends='chosen-css',
    directory=resources_dir,
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

default_styles = wr.ResourceGroup(name='styles')
default_styles.add(wr.StyleResource(
    name='chosen-css',
    directory=choses_resources_dir,
    resource='chosen.css',
    compressed='chosen.min.js'
))
default_styles.add(common_styles)

default_resources = wr.ResourceGroup(name='chosen-resources')
default_resources.add(scripts)
default_resources.add(default_styles)

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

bootstrap_styles = wr.ResourceGroup(name='styles')
bootstrap_styles.add(wr.StyleResource(
    name='chosen-css',
    directory=choses_resources_dir,
    resource='chosen-bootstrap.css'
))
bootstrap_styles.add(bootstrap_styles)

bootstrap_resources = wr.ResourceGroup(name='chosen-resources')
bootstrap_resources.add(scripts)
bootstrap_resources.add(bootstrap_styles)

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

    # Default
    factory.register_theme(
        'default', 'yafowil.widget.chosen', resources_dir,
        js=js, css=default_css, resources=default_resources
    )
    # Bootstrap
    factory.register_theme(
        'bootstrap', 'yafowil.widget.chosen', resources_dir,
        js=js, css=bootstrap_css, resources=bootstrap_resources
    )
