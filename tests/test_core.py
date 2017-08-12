import unittest

from unittest import mock

from nider.core import Text
from nider.core import MultilineText
from nider.core import SingleLineTextUnit
from nider.core import MultilineTextUnit


class TestText(unittest.TestCase):

    def setUp(self):
        self.text_mock = mock.Mock()

    # Tests for text handling

    def test_setting_text(self):
        Text._set_text(self.text_mock, 'foo')
        self.assertEqual(self.text_mock.text, 'foo')

    def test_setting_font(self):
        self.text_mock.fontfullpath = 'foo/bar'
        self.text_mock.fontsize = 23
        Text._set_font(self.text_mock)
        self.assertIsNotNone(self.text_mock.font)

    def test_setting_decoration_with_color_provided(self):
        Text._set_decoration(self.text_mock, '#000', True, '#000')
        self.assertEqual(self.text_mock.color, (0, 0, 0))

    def test_setting_decoration_without_color(self):
        Text._set_decoration(self.text_mock, None, True, '#000')
        self.assertTrue(self.text_mock.auto_color)
        self.assertIsNone(self.text_mock.color)

    def test_setting_decoration_with_drop_shadow_and_shadowcolor(self):
        Text._set_decoration(self.text_mock, '#000', True, '#000')
        self.assertEqual(self.text_mock.drop_shadow, True)
        self.assertEqual(self.text_mock.shadowcolor, (0, 0, 0))

    def test_setting_decoration_with_drop_shadow_and_without_shadowcolor(self):
        Text._set_decoration(self.text_mock, '#000', True, None)
        self.assertEqual(self.text_mock.drop_shadow, True)
        self.assertTrue(self.text_mock.auto_shadowcolor, True)
        self.assertIsNone(self.text_mock.shadowcolor)

    def test_setting_decoration_without_drop_shadow(self):
        Text._set_decoration(self.text_mock, '#000', False, '#000')
        self.assertEqual(self.text_mock.color, (0, 0, 0))
        self.assertEqual(self.text_mock.drop_shadow, False)
        self.assertIsNone(self.text_mock.shadowcolor)


class TestMultilineText(unittest.TestCase):

    @mock.patch('nider.mixins.MultilineTextMixin.__init__')
    @mock.patch('nider.core.Text.__init__')
    def test_proper_inheritance(self,
                                T_mock,
                                MTM_mock):
        multiline_text = MultilineText(text='foo', fontfullpath='foo.ttf',
                                       fontsize=15, color='#000',
                                       drop_shadow=False, shadowcolor='#000',
                                       text_width=20, line_padding=5)
        T_mock.assert_called_once_with(multiline_text, text='foo',
                                       fontfullpath='foo.ttf', fontsize=15,
                                       color='#000',
                                       drop_shadow=False, shadowcolor='#000')
        MTM_mock.assert_called_once_with(multiline_text,
                                         text_width=20,
                                         line_padding=5)


class TestSingleLineTextUnit(unittest.TestCase):

    @mock.patch('nider.core.SingleLineTextUnit._set_height')
    @mock.patch('nider.mixins.AlignMixin.__init__')
    @mock.patch('nider.core.Text.__init__')
    def test_proper_inheritance(self, T_mock, AM_mock, _set_height_mock):

        unit = SingleLineTextUnit(text='foo',
                                  fontfullpath=None, fontsize=18,
                                  color='#000', drop_shadow=False,
                                  shadowcolor='#646464', align='center')
        T_mock.assert_called_once_with(unit, text='foo',
                                       fontfullpath=None, fontsize=18,
                                       color='#000', drop_shadow=False,
                                       shadowcolor='#646464'
                                       )
        AM_mock.assert_called_once_with(unit, align='center')

    def test_set_height(self):
        unit = SingleLineTextUnit('foo', None)
        # height of the default font
        self.assertEqual(unit.height, 11)


class TestMultilineTextUnit(unittest.TestCase):

    @mock.patch('nider.core.MultilineTextUnit._set_unit')
    @mock.patch('nider.mixins.AlignMixin.__init__')
    @mock.patch('nider.core.MultilineText.__init__')
    def test_proper_inheritance(self,
                                MT_mock,
                                AM_mock,
                                _set_unit_mock):
        unit = MultilineTextUnit(text='foo', fontfullpath='foo.ttf',
                                 fontsize=15, color='#000',
                                 drop_shadow=False, shadowcolor='#000',
                                 text_width=20, line_padding=5,
                                 align='center')
        MT_mock.assert_called_once_with(unit, text='foo',
                                        fontfullpath='foo.ttf', fontsize=15,
                                        color='#000',
                                        drop_shadow=False, shadowcolor='#000',
                                        text_width=20,
                                        line_padding=5)
        AM_mock.assert_called_once_with(unit, align='center')

    @mock.patch('nider.core.MultilineTextUnit._set_height')
    def test_set_unit(self, _set_height_mock):
        unit = MultilineTextUnit(text='Lorem imsup dolor si amet',
                                 fontfullpath=None,
                                 text_width=5)
        self.assertEqual(unit.wrapped_lines,
                         ['Lorem', 'imsup', 'dolor', 'si', 'amet'])

    def test_set_height(self):
        unit = MultilineTextUnit(text='Lorem imsup dolor si amet',
                                 fontfullpath=None,
                                 text_width=5,
                                 line_padding=6)
        self.assertEqual(unit.height, 79)


if __name__ == '__main__':
    unittest.main()
