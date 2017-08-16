from nider.core import Font

from nider.models import Paragraph
from nider.models import Content
from nider.models import Image


# TODO: change this fontpath to the fontpath on your machine
roboto_font_folder = '/home/ovd/.local/share/fonts/Roboto/'

para = Paragraph(text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 font=Font(roboto_font_folder + 'Roboto-Medium.ttf', 20),
                 text_width=49,
                 align='center',
                 color='#121212'
                 )

content = Content(para)

img = Image(content,
            width=500,
            height=500,
            fullpath='result.png'
            )

img.draw_on_bg('#efefef')
