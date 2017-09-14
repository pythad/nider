from nider.core import Font

from nider.models import Watermark

from nider.tools import add_watermark


# TODO: change this fontpath to the fontpath on your machine
roboto_fonts_folder = '/home/ovd/.local/share/fonts/Roboto/'

watermark = Watermark(text='COPYRIGHT',
                      font=Font(roboto_fonts_folder + 'Roboto-Medium.ttf', 20),
                      color='#111',
                      cross=True
                      )

add_watermark('bg.jpg', watermark, 'result.jpg')
