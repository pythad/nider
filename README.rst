=====
nider
=====

.. image:: https://img.shields.io/pypi/v/nider.svg
        :target: https://pypi.python.org/pypi/nider

.. image:: https://img.shields.io/travis/pythad/nider.svg
        :target: https://travis-ci.org/pythad/nider

.. image:: https://readthedocs.org/projects/nider/badge/?version=latest
        :target: https://nider.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/pythad/nider/shield.svg
     :target: https://pyup.io/repos/github/pythad/nider/
     :alt: Updates


Python package to add text to images, textures and different backgrounds


* Free software: MIT license
* Documentation: https://nider.readthedocs.io.

``nider`` is an approach to make generation of text based images simple yet flexible. Creating of an image is as simple as describing units you want to be rendered to the image and choosing a method that will be used for drawing.

************
Installation
************

.. code-block:: console

    $ pip install nider

********
Features
********

Drawing on a texture
====================

.. code-block:: python

    from nider.models import Content
    from nider.models import Header
    from nider.models import Linkback
    from nider.models import Paragraph
    from nider.models import TwitterPost

    # TODO: change this fontpath to the fontpath on your machine
    roboto = '/home/ovd/.local/share/fonts/Roboto/'

    header = Header(text='Your super interesting title!',
                    fontfullpath=roboto + 'Roboto-Bold.ttf',
                    fontsize=30,
                    text_width=40,
                    align='left',
                    color='#ededed'
                    )

    para = Paragraph(text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                     fontfullpath=roboto + 'Roboto-Medium.ttf',
                     fontsize=29,
                     text_width=65,
                     align='left',
                     color='#ededed'
                     )

    linkback = Linkback(text='foo.com | @username',
                        fontfullpath=roboto + 'Roboto-Bold.ttf',
                        fontsize=24,
                        color='#ededed'
                        )

    content = Content(para, header=header, linkback=linkback, padding=60)

    img = TwitterPost(content,
                      fullpath='result.png',
                      )

    # TODO: change this texture path to the texture path on your machine
    img.draw_on_texture('texture.png')


.. image:: https://github.com/pythad/nider/raw/master/examples/draw_on_texture_example/result.png
        :alt: Draw on texture example

Drawing on a solid color
========================

.. image:: https://github.com/pythad/nider/raw/master/examples/draw_on_bg_example/result.png
        :alt: Draw on background example
        :height: 500px
        :width: 500px

Drawing on an image
===================

.. image:: https://github.com/pythad/nider/raw/master/examples/draw_on_image_example/result.png
        :alt: Draw on image example


===================

Code used to generate featured images can be found `here <https://github.com/pythad/nider/tree/master/examples>`_