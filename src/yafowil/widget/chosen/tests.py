from node.utils import UNSET
from yafowil.base import ExtractionError
from yafowil.base import factory
from yafowil.compat import IS_PY2
from yafowil.tests import fxml
from yafowil.tests import YafowilTestCase
import os
import unittest


if not IS_PY2:
    from importlib import reload


def np(path):
    return path.replace('/', os.path.sep)


class TestChosenWidget(YafowilTestCase):

    def setUp(self):
        super(TestChosenWidget, self).setUp()
        from yafowil.widget import chosen
        reload(chosen.widget)
        chosen.register()

    def test_edit_renderer(self):
        widget = factory(
            'chosen',
            name='CHOSEN',
            props={
                'required': True,
                'vocabulary': [('foo', 'Foo'), ('bar', 'Bar')],
            })
        self.checkOutput("""
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
        self.checkOutput("""
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
        self.checkOutput("""
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
        self.assertEqual(
            widget(),
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

    def test_resources(self):
        factory.theme = 'default'
        resources = factory.get_resources('yafowil.widget.chosen')
        self.assertTrue(resources.directory.endswith(np('/chosen/resources')))
        self.assertEqual(resources.path, 'yafowil-chosen')

        scripts = resources.scripts
        self.assertEqual(len(scripts), 2)

        self.assertTrue(
            scripts[0].directory.endswith(np('/chosen/resources/chosen'))
        )
        self.assertEqual(scripts[0].path, 'yafowil-chosen/chosen')
        self.assertEqual(scripts[0].file_name, 'chosen.jquery.min.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        self.assertTrue(scripts[1].directory.endswith(np('/chosen/resources')))
        self.assertEqual(scripts[1].path, 'yafowil-chosen')
        self.assertEqual(scripts[1].file_name, 'widget.min.js')
        self.assertTrue(os.path.exists(scripts[1].file_path))

        styles = resources.styles
        self.assertEqual(len(styles), 2)

        self.assertTrue(
            styles[0].directory.endswith(np('/chosen/resources/chosen'))
        )
        self.assertEqual(styles[0].path, 'yafowil-chosen/chosen')
        self.assertEqual(styles[0].file_name, 'chosen.min.css')
        self.assertTrue(os.path.exists(styles[0].file_path))

        self.assertTrue(styles[1].directory.endswith(np('/chosen/resources')))
        self.assertEqual(styles[1].path, 'yafowil-chosen')
        self.assertEqual(styles[1].file_name, 'widget.css')
        self.assertTrue(os.path.exists(styles[1].file_path))

        factory.theme = 'bootstrap3'
        resources = factory.get_resources('yafowil.widget.chosen')
        self.assertTrue(resources.directory.endswith(np('/chosen/resources')))
        self.assertEqual(resources.path, 'yafowil-chosen')

        scripts = resources.scripts
        self.assertEqual(len(scripts), 2)

        self.assertTrue(
            scripts[0].directory.endswith(np('/chosen/resources/chosen'))
        )
        self.assertEqual(scripts[0].path, 'yafowil-chosen/chosen')
        self.assertEqual(scripts[0].file_name, 'chosen.jquery.min.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        self.assertTrue(scripts[1].directory.endswith(np('/chosen/resources')))
        self.assertEqual(scripts[1].path, 'yafowil-chosen')
        self.assertEqual(scripts[1].file_name, 'widget.min.js')
        self.assertTrue(os.path.exists(scripts[1].file_path))

        styles = resources.styles
        self.assertEqual(len(styles), 2)

        self.assertTrue(
            styles[0].directory.endswith(np('/chosen/resources/chosen'))
        )
        self.assertEqual(styles[0].path, 'yafowil-chosen/chosen')
        self.assertEqual(styles[0].file_name, 'chosen-bootstrap.css')
        self.assertTrue(os.path.exists(styles[0].file_path))

        self.assertTrue(styles[1].directory.endswith(np('/chosen/resources')))
        self.assertEqual(styles[1].path, 'yafowil-chosen')
        self.assertEqual(styles[1].file_name, 'widget.css')
        self.assertTrue(os.path.exists(styles[1].file_path))


if __name__ == '__main__':
    unittest.main()
