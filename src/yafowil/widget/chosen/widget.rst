chosen widget
=============

Features
--------

- renders select box with chosen css class and provides chosen resources.

Load requirements::

    >>> import yafowil.loader
    >>> import yafowil.widget.chosen

Test widget::

    >>> from yafowil.base import factory

Render widget::

    >>> widget = factory('chosen', 'multi', props={'required': True})
    >>> widget()
    u'<select class="chosen" id="input-multi" name="multi" required="required" />'

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

    >>> widget = factory('chosen',
    ...                  'multi',
    ...                  value=['foo', 'bar'],
    ...                  props={
    ...                      'vocabulary': [('foo', 'Foo'), ('bar', 'Bar')],
    ...                      'multivalued': True},
    ...                  mode='display')
    >>> widget()
    u'<ul class="display-chosen" 
    id="display-multi"><li>Foo</li><li>Bar</li></ul>'

    >>> widget = factory('chosen', 'multi', mode='display')
    >>> widget()
    u'<div class="display-chosen" id="display-multi"></div>'
