from node.utils import UNSET
from yafowil.base import ExtractionError
from yafowil.base import factory
from yafowil.compat import IS_PY2
from yafowil.tests import YafowilTestCase
from yafowil.tests import fxml
import yafowil.loader


if not IS_PY2:
    from importlib import reload


class TestChosenWidget(YafowilTestCase):

    def setUp(self):
        super(TestChosenWidget, self).setUp()
        from yafowil.widget.chosen import widget
        reload(widget)

    def test_edit_renderer(self):
        widget = factory(
            'chosen',
            name='CHOSEN',
            props={
                'required': True,
                'vocabulary': [('foo', 'Foo'), ('bar', 'Bar')],
            })
        self.check_output("""
        <select class="chosen" id="input-CHOSEN" name="CHOSEN"
                required="required">
          <option id="input-CHOSEN-foo" value="foo">Foo</option>
          <option id="input-CHOSEN-bar" value="bar">Bar</option>
        </select>
        """, fxml(widget()))

        widget = factory(
            'chosen',
            name='CHOSEN',
            value=['foo'],
            props={
                'vocabulary': [('foo', 'Foo'), ('bar', 'Bar')],
                'multivalued': True
            })
        self.check_output("""
        <div>
          <input id="exists-CHOSEN" name="CHOSEN-exists" type="hidden"
                 value="exists"/>
          <select class="chosen" id="input-CHOSEN" multiple="multiple"
                  name="CHOSEN">
            <option id="input-CHOSEN-foo" selected="selected"
                    value="foo">Foo</option>
            <option id="input-CHOSEN-bar"
                    value="bar">Bar</option>
          </select>
        </div>
        """, fxml('<div>{}</div>'.format(widget())))

    def test_display_renderer(self):
        widget = factory(
            'chosen',
            name='CHOSEN',
            value=['foo', 'bar'],
            props={
                'vocabulary': [('foo', 'Foo'), ('bar', 'Bar'), ('baz', 'Baz')],
                'multivalued': True
            },
            mode='display')
        self.check_output("""
        <ul class="display-chosen" id="display-CHOSEN">
          <li>Foo</li>
          <li>Bar</li>
        </ul>
        """, fxml(widget()))

        widget = factory(
            'chosen',
            name='CHOSEN',
            value='foo',
            mode='display')
        self.assertEqual(widget(),
            '<div class="display-chosen" id="display-CHOSEN">foo</div>'
        )

    def test_extraction(self):
        widget = factory(
            'chosen',
            name='CHOSEN',
            props={
                'required': True
            })
        request = {'CHOSEN': ''}
        data = widget.extract(request)
        self.assertEqual(data.name, 'CHOSEN')
        self.assertEqual(data.value, UNSET)
        self.assertEqual(data.extracted, '')
        self.assertEqual(
            data.errors,
            [ExtractionError('Mandatory field was empty')]
        )

        request = {'CHOSEN': '1'}
        data = widget.extract(request)
        self.assertEqual(data.name, 'CHOSEN')
        self.assertEqual(data.value, UNSET)
        self.assertEqual(data.extracted, '1')
        self.assertEqual(data.errors, [])


if __name__ == '__main__':
    unittest.main()                                          # pragma: no cover
