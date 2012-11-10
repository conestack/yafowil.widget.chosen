# -*- coding: utf-8 -*-
from yafowil.base import factory


DOC_CHOSEN = """
chosen
------

chosen Widget using jQuery chosen plugin.

.. code-block:: python

    chosen = factory('#field:chosen', props={
        'label': 'Select some items',
        'required': 'Selection is required',
        'vocabulary': sorted((u'Weißburgunder', u'Welschriesling',
                              u'Sauvingnon Blanc', u'Sämling', u'Scheurebe',
                              u'Traminer', u'Morrilon', u'Muskateller'))})
"""

def chosen():
    part = factory(u'fieldset', name='yafowilwidgetchosen')
    part['text'] = factory('#field:chosen', props={
        'label': 'Select some items',
        'required': 'Selection is required',
        'vocabulary': sorted((u'Weißburgunder', u'Welschriesling',
                              u'Sauvingnon Blanc', u'Sämling', u'Scheurebe',
                              u'Traminer', u'Morrilon', u'Muskateller'))})
    return {'widget': part,
            'doc': DOC_CHOSEN,
            'title': 'chosen Widget'}


def get_example():
    return [chosen()]
