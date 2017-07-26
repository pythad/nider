from nider.exceptions import InvalidAlignException


class AlignMixin:

    def __init__(self, align):
        self._set_align(align)

    def _set_align(self, align):
        '''Sets align for the child object'''
        possible_aligns = ['right', 'center', 'left']
        if align not in possible_aligns:
            raise InvalidAlignException(align)
        self.align = align
