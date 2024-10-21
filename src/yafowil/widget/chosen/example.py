# -*- coding: utf-8 -*-
from yafowil.base import factory

DOC_CHOSEN_DEPRECATION = """
.. raw:: html

    <div class="alert alert-info">
        <i class="bi bi-info-circle-fill"></i>
        This widget has a newer version available:
        <a class="link-offset-3"
           href="../++widget++yafowil.widget.select2/index.html">
            yafowil.widget.select2
        </a>
    </div>
    <div class="alert alert-warning">
        <i class="bi bi-exclamation-triangle-fill"></i>
        <strong>Deprecation Notice:</strong>
        yafowil.widget.chosen is 
        <strong>
            deprecated
        </strong>
        and will no longer receive support or further development.
    </div>
"""

DOC_CHOSEN_SINGLE = """
chosen
------

HarvestHQ Chosen widget in single selection mode.

.. code-block:: python

    vocab = sorted((u'Weißburgunder', u'Welschriesling',
                    u'Sauvingnon Blanc', u'Sämling', u'Scheurebe',
                    u'Traminer', u'Morrilon', u'Muskateller'))

    chosen = factory('#field:chosen', props={
        'label': 'Select some items',
        'required': 'Selection is required',
        'vocabulary': vocab,
        'multivalued': False,
    })
"""

DOC_CHOSEN_MULTI = """
HarvestHQ Chosen widget in multi selection mode.

.. code-block:: python

    chosen = factory('#field:chosen', props={
        'label': 'Select some items',
        'required': 'Selection is required',
        'vocabulary': vocab,
        'multivalued': True,
    })
"""

DOC_CHOSEN_MULTI_2 = """
HarvestHQ Chosen widget in multi selection, allow new values and search
substrings mode.
This one can be used as an autocomplete widget.

.. code-block:: python

    chosen = factory('#field:chosen', props={
        'label': 'Select some items',
        'required': 'Selection is required',
        'vocabulary': vocab,
        'multivalued': True,
        'search_contains': True,
        'new_values': True,
    })
"""


def get_example():
    vocab = sorted((u'Weißburgunder', u'Welschriesling',
                    u'Sauvingnon Blanc', u'Sämling', u'Scheurebe',
                    u'Traminer', u'Morrilon', u'Muskateller'))

    # single selection
    chosen_single = factory(u'fieldset', name='yafowil_chosen_single')
    chosen_single['text'] = factory('#field:chosen', props={
        'label': 'Select some items',
        'required': 'Selection is required',
        'vocabulary': vocab,
        'multivalued': False,
    })

    # multiple selection
    chosen_multi = factory(u'fieldset', name='yafowil_chosen_multi')
    chosen_multi['text'] = factory('#field:chosen', props={
        'label': 'Select some items',
        'required': 'Selection is required',
        'vocabulary': vocab,
        'multivalued': True,
    })

    # multiple selection, search substrings, allow new values
    chosen_multi2 = factory(u'fieldset', name='yafowil_chosen_multi2')
    chosen_multi2['text'] = factory('#field:chosen', props={
        'label': 'Select some items',
        'required': 'Selection is required',
        'vocabulary': vocab,
        'multivalued': True,
        'search_contains': True,
        'new_values': True,
    })

    return [{
        'widget': chosen_single,
        'doc': DOC_CHOSEN_SINGLE if factory.theme != 'bootstrap5'
               else DOC_CHOSEN_DEPRECATION + DOC_CHOSEN_SINGLE,
        'title': 'Single Selection',
    }, {
        'widget': chosen_multi,
        'doc': DOC_CHOSEN_MULTI,
        'title': 'Multi Selection',
    }, {
        'widget': chosen_multi2,
        'doc': DOC_CHOSEN_MULTI_2,
        'title': 'Multi Selection, New Values, Search Substrings',
    }]
