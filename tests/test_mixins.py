import unittest

from unittest import mock

from nider.mixins import MultilineTextMixin
from nider.mixins import AlignMixin

from nider.exceptions import InvalidAlignException


class TestMultilineTextMixinInitializationMethods(unittest.TestCase):

    def setUp(self):
        self.mixin_mock = mock.Mock()

    def test_set_text_width_with_valid_config(self):
        MultilineTextMixin._set_text_width(self.mixin_mock, 20)
        self.assertEqual(self.mixin_mock.text_width, 20)

    def test_set_text_width_with_invalid_config(self):
        with self.assertRaises(AttributeError):
            MultilineTextMixin._set_text_width(self.mixin_mock, -1)


class TestMultilineTextMixin(unittest.TestCase):

    def setUp(self):
        self.mixin = MultilineTextMixin(20, 15)

    def test_line_padding(self):
        self.assertEqual(self.mixin.line_padding, 15)


class TestAlignMixinInitializationMethods(unittest.TestCase):

    def setUp(self):
        self.mixin_mock = mock.Mock()

    def test_set_align_with_valid_config(self):
        for align in ['right', 'center', 'left']:
            with self.subTest():
                AlignMixin._set_align(self.mixin_mock, align)
                self.assertEqual(self.mixin_mock.align, align)

    def test_align_with_invalid_config(self):
        with self.assertRaises(InvalidAlignException):
            AlignMixin._set_align(self.mixin_mock, align='bar')


if __name__ == '__main__':
    unittest.main()
