import os
import warnings
import random

from contextlib import contextmanager

from PIL import Image
from PIL import ImageFont

from nider.colors import FLAT_UI_COLORS

from nider.exceptions import DefaultFontWarning
from nider.exceptions import FontNotFoundWarning


def get_font(fontfullpath, fontsize):
    '''Function to create a truetype ``PIL.ImageFont`` that provides fallbacks for invalid arguments

    Args:
        fontfullpath (str): path to the desired font.
        fontsize (int): size of the font.

    Returns:
        PIL.ImageFont: Default PIL ImageFont if ``fontfullpath`` is either unreachable or provided ``fontfullpath`` is ``None``.

    Raises:
        nider.exceptions.DefaultFontWarning: if ``fontfullpath`` is ``None``.
        nider.exceptions.FontNotFoundWarning: if ``fontfullpath`` does not exist.
    '''
    if fontfullpath is None:
        warnings.warn(DefaultFontWarning())
        font = ImageFont.load_default()
        font.is_default = True
    elif not os.path.exists(fontfullpath):
        warnings.warn(FontNotFoundWarning(fontfullpath))
        font = ImageFont.load_default()
        font.is_default = True
    else:
        font = ImageFont.truetype(fontfullpath, fontsize)
        font.is_default = False
    return font


def is_path_creatable(pathname):
    '''Function to check if the current user has sufficient permissions to create the passed
    pathname

    Args:
        pathname (str): path to check.

    Returns:
        bool: ``True`` if the current user has sufficient permissions to create the passed ``pathname``. ``False`` otherwise.
    '''
    # Parent directory of the passed path. If empty, we substitute the current
    # working directory (CWD) instead.
    dirname = os.path.dirname(pathname) or os.getcwd()
    return os.access(dirname, os.W_OK)


@contextmanager
def create_test_image():
    '''Context manager to yield a ``PIL.Image``'''
    try:
        image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
        image.save('test.png')
        yield
    finally:
        os.remove('test.png')


def get_random_texture():
    '''Returns the path to a random texture from the local ``nider/textures`` folder'''
    textures_folder = os.path.dirname(
        os.path.realpath(__file__)) + '/textures'
    texture = random.choice(os.listdir(textures_folder))
    texture_path = textures_folder + '/' + texture
    return texture_path


def get_random_bgcolor():
    '''Returns random flat ui color from ``nider.colors.colormap.FLAT_UI_COLORS``'''
    return random.choice(list(FLAT_UI_COLORS.values()))
