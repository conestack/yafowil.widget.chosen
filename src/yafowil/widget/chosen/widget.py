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
""Add-on blueprint `yafowil.widget.chosen
<http://github.com/bluedynamics/yafowil.widget.chosen/>`_ .
"""


factory.defaults['chosen.multivalued'] = True
factory.defaults['chosen.size'] = None
factory.defaults['chosen.default'] = []
factory.defaults['chosen.format'] = 'block'
factory.defaults['chosen.class'] = 'chosen'

# I don't know yet how to propagate them to chosen.
factory.defaults['chosen.api_click_test_action'] = None;
factory.defaults['chosen.api_activate_action'] = None;
factory.defaults['chosen.api_mouse_on_container'] = None;
factory.defaults['chosen.api_results_showing'] = None;
factory.defaults['chosen.api_result_highlighted'] = None;
factory.defaults['chosen.api_result_single_selected'] = None;
factory.defaults['chosen.api_allow_single_deselect'] = None;
factory.defaults['chosen.api_disable_search_threshold'] = None;
factory.defaults['chosen.api_disable_search'] = None;
factory.defaults['chosen.api_search_contains'] = None;
factory.defaults['chosen.api_choices'] = None;
factory.defaults['chosen.api_single_backstroke_delete'] = None;
factory.defaults['chosen.api_max_selected_options'] = None;

"""
    from abstract-chosen.coffee
    ---------------------------

  set_default_values: ->
    @click_test_action = (evt) => this.test_active_click(evt)
    @activate_action = (evt) => this.activate_field(evt)
    @active_field = false
    @mouse_on_container = false
    @results_showing = false
    @result_highlighted = null
    @result_single_selected = null
    @allow_single_deselect = if @options.allow_single_deselect? and @form_field.options[0]? and @form_field.options[0].text is "" then @options.allow_single_deselect else false
    @disable_search_threshold = @options.disable_search_threshold || 0
    @disable_search = @options.disable_search || false
    @search_contains = @options.search_contains || false
    @choices = 0
    @single_backstroke_delete = @options.single_backstroke_delete || false
    @max_selected_options = @options.max_selected_options || Infinity

"""
