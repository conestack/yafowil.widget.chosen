# -*- coding: utf-8 -*-

from yafowil.base import factory

def get_example():
    part = factory(u'fieldset', name='yafowilwidgetmultiselect')
    part['text'] = factory('field:label:error:multiselect', props={
        'label': 'Enter some text (local, lorem ipsum)',
        'vocabulary': ('Weißburgunder', 'Welschriesling', 'Sauvingnon Blanc', 'Sämling', 'Scheurebe', 'Traminer', 'Morrilon', 'Muskateller')})
    return [{'widget': part, 'doc': 'TODO'}]
