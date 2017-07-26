class ImageGeneratorException(Exception):
    pass


class ImageGeneratorWarning(Warning):
    pass


class InvalidAlignException(ImageGeneratorException):
    def __init__(self, align_provided, available_aligns=None):
        if available_aligns is None:
            available_aligns = ['center', 'right', 'left']
        available_aligns_str = ' or '.join(available_aligns)
        super().__init__(
            "Align has to be set either to {}. You provided '{}'".format(available_aligns_str, align_provided))


class FontNotFoundWarning(ImageGeneratorWarning):
    def __init__(self, fontpath_provided):
        super().__init__(
            "Font {} hasn't been found. Default font has been set instead".format(fontpath_provided))


class DefaultFontWarning(ImageGeneratorWarning):
    def __init__(self):
        super().__init__(
            "Font hasn't been provided. Default font has been set instead")


class ImageSizeFixedWarning(ImageGeneratorWarning):
    def __init__(self):
        super().__init__(
            "Image size has been adjusted to the provided content size because the content took too much space")
