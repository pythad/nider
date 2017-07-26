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
    '''Returns a PIL ImageFont object

    Attributes:
        fontfullpath (str): path to the desired font
        fontsize (int): size of the font
    '''
    if fontfullpath is None:
        warnings.warn(DefaultFontWarning())
        return ImageFont.load_default()
    elif not os.path.exists(fontfullpath):
        warnings.warn(FontNotFoundWarning(fontfullpath))
        return ImageFont.load_default()
    return ImageFont.truetype(fontfullpath, fontsize)


def is_path_creatable(pathname):
    '''
    `True` if the current user has sufficient permissions to create the passed
    pathname; `False` otherwise.
    '''
    # Parent directory of the passed path. If empty, we substitute the current
    # working directory (CWD) instead.
    dirname = os.path.dirname(pathname) or os.getcwd()
    return os.access(dirname, os.W_OK)


@contextmanager
def create_test_image():
    try:
        image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
        image.save('test.png')
        yield
    finally:
        os.remove('test.png')


def get_random_texture():
    '''Returns the path to a random texture from the local /textures folder'''
    textures_folder = os.path.dirname(
        os.path.realpath(__file__)) + '/textures'
    texture = random.choice(os.listdir(textures_folder))
    texture_path = textures_folder + '/' + texture
    return texture_path


def get_random_bgcolor():
    '''Returns random FLAT_UI_COLOR'''
    return random.choice(list(FLAT_UI_COLORS.values()))
