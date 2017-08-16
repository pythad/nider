from nider.core import Font
from nider.core import Outline

from nider.models import Content
from nider.models import Linkback
from nider.models import Paragraph
from nider.models import Image


# TODO: change this fontpath to the fontpath on your machine
roboto_font_folder = '/home/ovd/.local/share/fonts/Roboto/'

text_outline = Outline(1, '#121212')

para = Paragraph(text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
                 font=Font(roboto_font_folder + 'Roboto-Medium.ttf', 25),
                 text_width=35,
                 align='center',
                 color='#efefef',
                 outline=text_outline
                 )

linkback = Linkback(text='@foobar',
                    font=Font(roboto_font_folder + 'Roboto-Bold.ttf', 20),
                    color='#efefef',
                    outline=text_outline
                    )

content = Content(paragraph=para, linkback=linkback)

img = Image(content,
            fullpath='result.png',
            width=500,
            height=500
            )

# TODO: change this texture path to the texture path on your machine
img.draw_on_texture('texture.png')
