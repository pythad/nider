import functools

from PIL import ImageColor

from colorthief import ColorThief

from nider.colors import rgb
from nider.colors import COLORS


def color_to_rgb(color):
    try:
        return rgb(*ImageColor.getrgb(color))
    except AttributeError as e:
        # assume that color is already an rgb tuple
        return rgb(*color)


def get_img_dominant_color(img_path):
    '''Finds img dominant color

    Using colorthief module finds image dominant color

    Attributes:
        img_path (str): path to an image to get a dominant color for
    Returns:
        Dominant rgb color for provided image
    '''
    color_thief = ColorThief(img_path)
    return rgb(*color_thief.get_color(quality=1))


def monochrome_color(color, invert=False):
    '''Generates a monochrome(black or white) color

    Generates a monochrome version of a color for a provided color

    Attributes:
        color (tuple(int, int, int)): Color to generate a monochrome one for
    Returns:
        Monochrome rgb color that can be either black or white
    '''
    color_luminance = 1 - (0.299 * color[0] + 0.587 *
                           color[1] + 0.114 * color[2]) / 255
    if invert:
        return COLORS['black'] if color_luminance < 0.5 else COLORS['white']
    return COLORS['black'] if color_luminance >= 0.5 else COLORS['white']


generate_opposite_color = functools.partial(monochrome_color, invert=True)


def blend(first, second, coefficient=0.5):
    '''Adds two colors

    Adds two colors with use of coefficient to determine which color
    has more power

    Attributes:
        coefficient (float): a 0 <= number <= 1 number that defines power of the first color
    Returns:
        rgb color - result of the blending
    '''
    first, second = color_to_rgb(first), color_to_rgb(second)
    r = int(coefficient * first.R + ((1 - coefficient) * second.R))
    g = int(coefficient * first.G + ((1 - coefficient) * second.G))
    b = int(coefficient * first.B + ((1 - coefficient) * second.B))
    return rgb(r, g, b)
