from nider.core import Font
from nider.core import Outline

from nider.models import Header
from nider.models import Paragraph
from nider.models import Linkback
from nider.models import Content
from nider.models import Image

from PIL import ImageFilter

# TODO: change this fontpath to the fontpath on your machine
roboto_font_folder = '/home/ovd/.local/share/fonts/Roboto/'

text_outline = Outline(2, '#121212')

header = Header(text='The first solar eclipse to cross America in 99 years is coming. To some, it’s an act of God.',
                font=Font(roboto_font_folder + 'Roboto-Bold.ttf', 33),
                text_width=40,
                align='left',
                color='#ededed',
                outline=text_outline,
                )

para = Paragraph(text='Tens of millions of people are expected to cram into a narrow path, from Oregon to the Carolinas, to see the remarkable event.',
                 font=Font(roboto_font_folder + 'Roboto-Medium.ttf', 29),
                 text_width=50,
                 align='left',
                 color='#ededed',
                 outline=text_outline,
                 )

linkback = Linkback(text='@washingtonpost',
                    font=Font(roboto_font_folder + 'Roboto-Bold.ttf', 20),
                    color='#ededed',
                    outline=text_outline,
                    )

content = Content(para, header, linkback)

img = Image(content,
            fullpath='result.png',
            width=1080,
            height=720
            )

# TODO: change this image path to the image path on your machine
img.draw_on_image('bg.png', image_filters=((ImageFilter.BLUR),))
