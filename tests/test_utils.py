import unittest
import os

from unittest import mock

from nider.exceptions import FontNotFoundWarning

from nider.utils import get_font


class TestGetFont(unittest.TestCase):

    @mock.patch('PIL.ImageFont.load_default')
    def test_with_none_params(self, load_default_mock):
        get_font(fontfullpath=None, fontsize=None)
        self.assertTrue(load_default_mock.called)

    @mock.patch('PIL.ImageFont.load_default')
    def test_with_nonexistent_fontfullpath(self, load_default_mock):
        with self.assertWarns(FontNotFoundWarning):
            get_font(fontfullpath='foo/bar', fontsize=None)
        self.assertTrue(load_default_mock.called)

    @mock.patch('PIL.ImageFont.truetype')
    @mock.patch('os.path.exists')
    @mock.patch('PIL.ImageFont.load_default')
    def test_existent_font(self, load_default_mock,
                           path_exists_mock, truetype_mock):
        path_exists_mock.return_value = True
        return_mock = mock.MagicMock()
        truetype_mock.return_value = return_mock
        font = get_font(
            fontfullpath=os.path.abspath('/foo/bar/'),
            fontsize=15)
        self.assertTrue(font, return_mock)
        self.assertFalse(load_default_mock.called)


if __name__ == '__main__':
    unittest.main()
