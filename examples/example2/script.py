from nider.core import Font
from nider.core import Outline

from nider.models import Content
from nider.models import Header
from nider.models import Image


# TODO: change this fontpath to the fontpath on your machine
roboto_font_folder = '/home/ovd/.local/share/fonts/Roboto/'

text_outline = Outline(1, '#cdbb9f')

header = Header(text='Google bought a service that allows patients to undergo basic clinical tests at home using smartphones.',
                font=Font(roboto_font_folder + 'Roboto-Bold.ttf', 22),
                text_width=50,
                align='left',
                color='#000100',
                outline=text_outline
                )

content = Content(header=header)

img = Image(content,
            fullpath='result.png',
            width=600,
            height=314
            )

# TODO: change this image path to the image path on your machine
img.draw_on_image('bg.jpg')
