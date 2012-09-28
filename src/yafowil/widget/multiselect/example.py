# -*- coding: utf-8 -*-
from yafowil.base import factory


DOC_MULTISELECT = """
Multiselect
-----------

Multiselect Widget using jQuery multiselect plugin.

.. code-block:: python

    multiselect = factory('#field:multiselect', props={
        'label': 'Select some items',
        'required': 'Selection is required',
        'vocabulary': sorted((u'Weißburgunder', u'Welschriesling',
                              u'Sauvingnon Blanc', u'Sämling', u'Scheurebe',
                              u'Traminer', u'Morrilon', u'Muskateller'))})
"""

def multiselect():
    part = factory(u'fieldset', name='yafowilwidgetmultiselect')
    part['text'] = factory('#field:multiselect', props={
        'label': 'Select some items',
        'required': 'Selection is required',
        'vocabulary': sorted((u'Weißburgunder', u'Welschriesling',
                              u'Sauvingnon Blanc', u'Sämling', u'Scheurebe',
                              u'Traminer', u'Morrilon', u'Muskateller'))})
    return {'widget': part,
            'doc': DOC_MULTISELECT,
            'title': 'Multiselect Widget'}


def get_example():
    return [multiselect()]