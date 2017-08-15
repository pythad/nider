import textwrap

from nider.utils import get_font

from nider.mixins import MultilineTextMixin
from nider.mixins import AlignMixin
from nider.colors.utils import color_to_rgb


class Outline:
    '''Base class for text's outline

    Attributes:
        width (int): width of the stroke.
        color (str): string that represents a color. Must be compatible with PIL.ImageColor color names.

    .. warning::

        Due to PIL limitations - core library used for drawing, nider doesn't support 'true' outlineі. That is why high width outlines will look rather ugly and we don't recommend usign outlines with width > 3.
    '''

    def __init__(self, width=2, color=None):
        self.width = width
        self._set_color(color)

    def _set_color(self, color):
        self.color = color_to_rgb(color) if color else None


class Text:
    '''Base class for the text

    Attributes:
        text (str): text used in the object.
        fontfullpath (str): path to the font used in the object.
        fontsize (int): size of the font.
        color (str): string that represents a color. Must be compatible with PIL.ImageColor.
        outline (nider.core.Outline): nider.core.Outline object that represents text's outline.
    '''

    def __init__(self, text, fontfullpath,
                 fontsize, color, outline):
        self._set_text(text)
        self.fontfullpath = fontfullpath
        self.fontsize = fontsize
        self._set_font()
        self._set_color(color)
        self.outline = outline

    def _set_text(self, text):
        '''Sets object's text data'''
        self.text = text

    def _set_font(self):
        '''Sets object's font'''
        self.font = get_font(self.fontfullpath, self.fontsize)

    def _set_color(self, color):
        '''Sets object's color and outline'''
        self.color = color_to_rgb(color) if color else None


class MultilineText(MultilineTextMixin, Text):
    '''Base class for the multiline text'''

    def __init__(self, text_width, line_padding, *args, **kwargs):
        MultilineTextMixin.__init__(
            self, text_width=text_width, line_padding=line_padding)
        Text.__init__(self, *args, **kwargs)


class SingleLineTextUnit(AlignMixin, Text):
    '''Base class for the single line text unit'''

    def __init__(self, text, fontfullpath=None,
                 fontsize=18, align='right',
                 color=None, outline=None
                 ):
        AlignMixin.__init__(self, align=align)
        Text.__init__(
            self, text=text, fontfullpath=fontfullpath, fontsize=fontsize,
            color=color, outline=outline
        )
        self._set_height()

    def _set_height(self):
        '''Sets unit\'s height'''
        _, self.height = self.font.getsize(self.text)


class MultilineTextUnit(AlignMixin, MultilineText):
    '''Base class for the multiline text unit'''

    def __init__(self, text,
                 fontfullpath=None, fontsize=18,
                 text_width=21, line_padding=6,
                 color=None, outline=None,
                 align='center'):
        AlignMixin.__init__(self, align=align)
        MultilineText.__init__(self, text=text,
                               fontfullpath=fontfullpath, fontsize=fontsize,
                               text_width=text_width, line_padding=line_padding,
                               color=color, outline=outline
                               )
        self._set_unit()

    def _set_unit(self):
        '''Sets a unit used in the image

        Sets textwraped unit's text that will be used in the image and also
        attachs header height to the obj instance
        '''
        self.wrapped_lines = textwrap.wrap(self.text, width=self.text_width)
        self._set_height()

    def _set_height(self):
        '''Sets unit's height used in the image

        Calculates unit's height by adding height of each line and its padding
        '''
        self.height = 0
        for line in self.wrapped_lines:
            _, h = self.font.getsize(line)
            self.height += h

        self.height += (len(self.wrapped_lines) - 1) * self.line_padding
