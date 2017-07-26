class MultilineTextMixin:

    def __init__(self, text_width, line_padding):
        self._set_text_width(text_width)
        self.line_padding = line_padding

    def _set_text_width(self, text_width):
        '''Sets text_width used in the child object'''
        if text_width > 0:
            self.text_width = text_width
        else:
            raise AttributeError(
                '{} text_width has to be an instance of int and > 0'.format(
                    self.__class__.__name__))
