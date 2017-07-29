from PIL import ImageColor

from nider.colors import rgb


def color_to_rgb(color):
    return rgb(*ImageColor.getrgb(color))
