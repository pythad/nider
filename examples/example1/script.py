from nider.core import Font
from nider.core import Outline

from nider.models import Content
from nider.models import Linkback
from nider.models import Paragraph
from nider.models import Image


# TODO: change this fontpath to the fontpath on your machine
roboto_font_folder = '/home/ovd/.local/share/fonts/Roboto/'

text_outline = Outline(2, '#121212')

para = Paragraph(text='“You\'ve gotta dance like there\'s nobody watching, love like you\'ll never be hurt, sing like there\'s nobody listening, and live like it\'s heaven on earth.”',
                 font=Font(roboto_font_folder + 'Roboto-Bold.ttf', 35),
                 text_width=30,
                 align='center',
                 color='#ededed',
                 outline=text_outline
                 )

linkback = Linkback(text='― William W. Purkey',
                    font=Font(roboto_font_folder + 'Roboto-Medium.ttf', 25),
                    color='#ededed',
                    outline=text_outline
                    )

content = Content(paragraph=para, linkback=linkback)

img = Image(content,
            fullpath='result.png',
            width=500,
            height=750
            )

# TODO: change this image path to the image path on your machine
img.draw_on_image('bg.jpg')
