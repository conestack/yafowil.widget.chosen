# -*- coding: utf-8 -*-

from yafowil.base import factory

def get_example():
    part = factory(u'fieldset', name='yafowilwidgetmultiselect')
    part['text'] = factory('field:label:error:multiselect', props={
        'label': 'Enter some text (local, lorem ipsum)',
        'required': 'Selection is required',
        'vocabulary': sorted((u'Weißburgunder', u'Welschriesling',
                              u'Sauvingnon Blanc', u'Sämling', u'Scheurebe',
                              u'Traminer', u'Morrilon', u'Muskateller'))})
    return [{'widget': part, 'doc': 'TODO'}]
