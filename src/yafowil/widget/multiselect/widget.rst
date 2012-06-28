multiselect widget
==================

Features
--------

- renders textarea with multiselect css class and provides a multiselect
  resources.

Load requirements::

    >>> import yafowil.loader
    >>> import yafowil.widget.multiselect

Test widget::

    >>> from yafowil.base import factory

Render widget::

    >>> widget = factory('multiselect', 'multi', props={'required': True})
    >>> widget()
    u'<input id="exists-multi" name="multi-exists" type="hidden" 
    value="exists" /><select class="multiselect" id="input-multi" 
    multiple="multiple" name="multi" required="required" />'

Widget extraction::

    >>> request = {'multi': []}
    >>> data = widget.extract(request)

    >>> data.errors
    [ExtractionError('Mandatory field was empty',)]

    >>> data.extracted
    []

    >>> request = {'multi': ['1']}
    >>> data = widget.extract(request)
    >>> data.errors
    []

    >>> data.extracted
    ['1']

Display renderer::

    >>> widget = factory('multiselect',
    ...                  'multi',
    ...                  value=['foo', 'bar'],
    ...                  props={'vocabulary': [('foo', 'Foo'), ('bar', 'Bar')]},
    ...                  mode='display')
    >>> widget()
    u'<ul class="display-multiselect" 
    id="display-multi"><li>Foo</li><li>Bar</li></ul>'

    >>> widget = factory('multiselect', 'multi', mode='display')
    >>> widget()
    u'<div class="display-multiselect" id="display-multi"></div>'
