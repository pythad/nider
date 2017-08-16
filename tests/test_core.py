import unittest

from unittest import mock

from nider.core import Font
from nider.core import Outline
from nider.core import Text
from nider.core import MultilineText
from nider.core import SingleLineTextUnit
from nider.core import MultilineTextUnit


class TestFont(unittest.TestCase):

    def setUp(self):
        self.font_mock = mock.Mock()

    def test_setting_font(self):
        self.font_mock.path = 'foo/bar'
        self.font_mock.size = 23
        Font._set_font(self.font_mock)
        self.assertIsNotNone(self.font_mock.font)

    def test_initialization(self):
        font = Font()
        self.assertIsNotNone(font.font)


class TestOutline(unittest.TestCase):

    def setUp(self):
        self.outline_mock = mock.Mock()

    def test_setting_color_with_color_provided(self):
        Outline._set_color(self.outline_mock, '#000')
        self.assertEqual(self.outline_mock.color, (0, 0, 0))

    def test_setting_color_without_color(self):
        Outline._set_color(self.outline_mock, None)
        self.assertIsNone(self.outline_mock.color)

    def test_initialization(self):
        outline = Outline(2, '#111')
        self.assertEqual(outline.width, 2)
        self.assertEqual(outline.color, (17, 17, 17))


class TestText(unittest.TestCase):

    def setUp(self):
        self.text_mock = mock.Mock()

    # Tests for text handling

    def test_setting_text(self):
        Text._set_text(self.text_mock, 'foo')
        self.assertEqual(self.text_mock.text, 'foo')

    def test_setting_color_with_color_provided(self):
        Text._set_color(self.text_mock, '#000')
        self.assertEqual(self.text_mock.color, (0, 0, 0))

    def test_setting_color_without_color(self):
        Text._set_color(self.text_mock, None)
        self.assertIsNone(self.text_mock.color)

    def test_initialization(self):
        outline = Outline(2, '#111')
        text = Text('foo', Font(), '#000', outline)
        self.assertEqual(text.text, 'foo')
        self.assertIsNotNone(text.font)
        self.assertEqual(text.color, (0, 0, 0))
        self.assertEqual(text.outline, outline)


class TestMultilineText(unittest.TestCase):

    @mock.patch('nider.mixins.MultilineTextMixin.__init__')
    @mock.patch('nider.core.Text.__init__')
    def test_proper_inheritance(self,
                                T_mock,
                                MTM_mock):
        font = Font()
        multiline_text = MultilineText(text='foo', font=font,
                                       color='#000', outline=None,
                                       text_width=20, line_padding=5)
        T_mock.assert_called_once_with(multiline_text, text='foo',
                                       font=font,
                                       color='#000', outline=None)
        MTM_mock.assert_called_once_with(multiline_text,
                                         text_width=20,
                                         line_padding=5)


class TestSingleLineTextUnit(unittest.TestCase):

    @mock.patch('nider.core.SingleLineTextUnit._set_height')
    @mock.patch('nider.mixins.AlignMixin.__init__')
    @mock.patch('nider.core.Text.__init__')
    def test_proper_inheritance(self, T_mock, AM_mock, _set_height_mock):
        font = Font()
        unit = SingleLineTextUnit(text='foo',
                                  font=font,
                                  color='#000', outline=None, align='center')
        T_mock.assert_called_once_with(unit, text='foo',
                                       font=font,
                                       color='#000', outline=None
                                       )
        AM_mock.assert_called_once_with(unit, align='center')

    def test_set_height(self):
        unit = SingleLineTextUnit('foo', Font())
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
        font = Font()
        unit = MultilineTextUnit(text='foo', font=font,
                                 color='#000', outline=None,
                                 text_width=20, line_padding=5,
                                 align='center')
        MT_mock.assert_called_once_with(unit, text='foo',
                                        font=font,
                                        color='#000',
                                        outline=None,
                                        text_width=20,
                                        line_padding=5)
        AM_mock.assert_called_once_with(unit, align='center')

    @mock.patch('nider.core.MultilineTextUnit._set_height')
    def test_set_unit(self, _set_height_mock):
        unit = MultilineTextUnit(text='Lorem imsup dolor si amet',
                                 font=Font(),
                                 text_width=5)
        self.assertEqual(unit.wrapped_lines,
                         ['Lorem', 'imsup', 'dolor', 'si', 'amet'])

    def test_set_height(self):
        unit = MultilineTextUnit(text='Lorem imsup dolor si amet',
                                 font=Font(),
                                 text_width=5,
                                 line_padding=6)
        self.assertEqual(unit.height, 79)


if __name__ == '__main__':
    unittest.main()
