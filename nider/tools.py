from nider.models import Image
from nider.models import Content


def add_watermark(image_path, watermark, new_path=None,
                  image_enhancements=None, image_filters=None):
    '''Function to add watermarks to images

    Args:
        image_path (str): path of the image to which watermark has to be added.
        watermark (nider.models.Watermark): watermark object.
        new_path (str): path where the image has to be saved. **If set to None (default option), initial image will be overwritten.**
        image_enhancements (itarable): itarable of tuples, each containing a class from ``PIL.ImageEnhance`` that will be applied and factor - a floating point value controlling the enhancement. Check `documentation <http://pillow.readthedocs.io/en/latest/reference/ImageEnhance.html>`_ of ``PIL.ImageEnhance`` for more info about availabe enhancements.
        image_filters (itarable): itarable of filters from ``PIL.ImageFilter`` that will be applied. Check `documentation <http://pillow.readthedocs.io/en/latest/reference/ImageFilter.html>`_ of ``PIL.ImageFilter`` for more info about availabe filters.

    Raises:
        FileNotFoundError: if image file at path ``image_path`` cannot be found.
        nider.exceptions.ImageGeneratorException: if the current user doesn't have sufficient permissions to create the file at passed ``new_path``.
    '''
    if new_path is None:
        new_path = image_path
    content = Content(watermark=watermark)
    new_image = Image(content, fullpath=new_path)
    new_image.draw_on_image(image_path,
                            image_enhancements=image_enhancements,
                            image_filters=image_filters)
