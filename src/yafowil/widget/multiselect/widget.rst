multiselect widget
================

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

    >>> widget = factory('multiselect', 'rt', props={'required': True})
    >>> widget()
    u'<textarea class="multiselect" cols="80" id="input-rt" name="rt" required="required" rows="10"></textarea>'

Widget extraction::

    >>> request = {'rt': ''}
    >>> data = widget.extract(request)

No input was given::

    >>> data.errors
    [ExtractionError('Mandatory field was empty',)]

Empty string in extracted::

    >>> data.extracted
    ''

Widget extraction. Returns markup from tinymce::

    >>> request = {'rt': '<p>1</p>'}
    >>> data = widget.extract(request)
    >>> data.errors
    []

    >>> data.extracted
    '<p>1</p>'

    >>> widget(data)
    u'<textarea class="multiselect" cols="80" id="input-rt" name="rt" required="required" rows="10"><p>1</p></textarea>'

Display renderer::

    >>> widget = factory('multiselect', 'rt', value='<p>foo</p>', mode='display')
    >>> widget()
    u'<div class="display-multiselect"><p>foo</p></div>'

    >>> widget = factory('multiselect', 'rt', mode='display')
    >>> widget()
    u'<div class="display-multiselect"></div>'
