import webcolors

from nider.colors import rgb


def color_to_rgb(color):
    try:
        return rgb(*webcolors.hex_to_rgb(color))
    except TypeError:
        return rgb(*color)
