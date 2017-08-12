import unittest

from nider.colors import monochrome_color
from nider.colors import color_to_rgb
from nider.colors import COLORS


class TestMonochromeColor(unittest.TestCase):

    def test_main_functionality(self):
        self.assertEqual(monochrome_color((255, 255, 255)), COLORS['white'])
        self.assertEqual(monochrome_color((254, 254, 254)), COLORS['white'])
        self.assertEqual(monochrome_color((255, 112, 112)), COLORS['white'])
        self.assertEqual(monochrome_color((0, 0, 0)), COLORS['black'])
        self.assertEqual(monochrome_color((1, 1, 1)), COLORS['black'])
        self.assertEqual(monochrome_color((30, 0, 0)), COLORS['black'])


class TestColorToRgb(unittest.TestCase):

    def test_main_functionality(self):
        self.assertEqual(color_to_rgb('#000'), (0, 0, 0))
        self.assertEqual(color_to_rgb((0, 0, 0)), (0, 0, 0))


if __name__ == '__main__':
    unittest.main()
