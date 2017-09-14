=====
Usage
=====

This article is a tutorial for ``nider`` package and at the same time it is a full reference of all ``nider`` models and possibilities.

***********
Image units
***********

There are three main units each ``nider.Image`` can consist of:

- header
- paragraph
- linkback

.. image:: images/available_units.png

Each of the units is represented by a class in ``nider.models``:

- :class:`nider.models.Header`
- :class:`nider.models.Paragraph`
- :class:`nider.models.Linkback`

``nider.models.Header``
=========================

.. autoclass:: nider.models.Header

Example
-------

.. code-block:: python

    from nider.core import Font
    from nider.core import Outline

    from nider.models import Header


    header = Header(text='Your super interesting title!',
                    font=Font('/home/me/.local/share/fonts/Roboto/Roboto-Bold.ttf', 30),
                    text_width=40,
                    align='left',
                    color='#ededed',
                    outline=Oultine(2, '#222')
                    )


``nider.models.Paragraph``
============================

This class has the same attribures and behaviour as :class:`nider.models.Header`.

.. autoclass:: nider.models.Paragraph

Example
-------

.. code-block:: python

    from nider.core import Font
    from nider.core import Outline

    from nider.models import Paragraph


    para = Paragraph(text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                     font=Font('/home/me/.local/share/fonts/Roboto/Roboto-Bold.ttf', 30),
                     text_width=65,
                     align='left',
                     color='#ededed'
                     outline=Oultine(1, '#000')
                     )


``nider.models.Linkback``
===========================

.. autoclass:: nider.models.Linkback

Example
-------

.. code-block:: python

    from nider.core import Font
    from nider.core import Outline

    from nider.models import Linkback


    linkback = Linkback(text='foo.com | @username',
                        font=Font('/home/me/.local/share/fonts/Roboto/Roboto-Bold.ttf', 30),
                        color='#ededed',
                        outline=Oultine(2, '#000')
                        )

------------

.. note::

    Parameters ``color`` and ``outline.color`` are optional for any unit. They can be generated automatically by ``nider``. ``nider`` analyzes background color of either a texture or of an image and chooses an opposite one to it. So if your image in mainly dark , white text color will be auto generated and set. The same applies to outline color.

    Although it's a nice feature for backgrounds you have no control over, we'd recommend to provide colors explicitly.

*************
Image content
*************

In order to aggregate all of the units together you need to create an instance of :class:`nider.models.Content` class.

``nider.models.Content``
==========================

.. autoclass:: nider.models.Content

Example
-------

.. code-block:: python

    from nider.models import Content
    from nider.models import Linkback
    from nider.models import Paragraph


    para = Paragraph(...)

    linkback = Linkback(...)

    content = Content(para, linkback=linkback, padding=60)


*********************
Initializing an image
*********************

After the content is prepared it's the right time to initialize an image. In ``nider`` a basic image is represented by ``nider.models.Image``.

``nider.models.Image``
========================

.. autoclass:: nider.models.Image

Example
-------

.. code-block:: python

    from nider.models import Content
    from nider.models import Image


    content = Content(...)

    img = Image(content,
                fullpath='example.png',
                width=500,
                height=500
                )

Social media images
-------------------

``nider`` comes with some pre-built models that can be used to generate images for some social networks. These are subclasses of ``nider.models.Image`` with changed size.

Instagram
^^^^^^^^^

 - :class:`nider.models.InstagramSquarePost` - 1080x1080 image
 - :class:`nider.models.InstagramPortraitPost` - 1080x1350 image
 - :class:`nider.models.InstagramLandscapePost` - 1080x566 image

Facebook
^^^^^^^^

 - :class:`nider.models.FacebookSquarePost` - 470x470 image
 - :class:`nider.models.FacebookLandscapePost` - 1024x512 image

Twitter
^^^^^^^

 - :class:`nider.models.TwitterPost` - 1024x512 image
 - :class:`nider.models.TwitterLargeCard` - 506x506 image

============

I highly recommend reading this `post <https://blog.bufferapp.com/ideal-image-sizes-social-media-posts>`_ if you are curious about what are the right image sizes for social media images.

********************
Drawing on the image
********************

Having an instance of ``nider.models.Image`` we are ready to create a real image.

``nider`` comes with 3 options of drawing your image:

 - ``Image.draw_on_texture`` - draws preinitialized image and its attributes on a texture.

 .. note::
     You don't need to create textured images by pasting texture mulpitle times in Photoshop or Gimp. ``nider`` takes care of filling image of any size with textrure you privide.

 - ``Image.draw_on_bg`` - Draws preinitialized image and its attributes on a colored background. nider uses a color you provide to fill the image and then draws the content.

 - ``Image.draw_on_image`` - Draws preinitialized image and its attributes on an image. Content will be drawn directly on the image you provide.


``Image.draw_on_texture``
=========================

.. automethod:: nider.models.Image.draw_on_texture

Example
-------

.. code-block:: python

    from nider.models import Content
    from nider.models import Image


    content = Content(...)

    img = Image(content,
                fullpath='example.png',
                width=500,
                height=500
                )

    img.draw_on_texture('example_texture.png')


Check the full example `here <https://github.com/pythad/nider/blob/master/examples/draw_on_texture_example/script.py>`_ .

============

``nider`` comes with a `huge bundle of textures <https://github.com/pythad/nider/tree/master/nider/textures>`_. As for now you need to copy them to your machine if you want to use any of them.

``Image.draw_on_bg``
====================

.. automethod:: nider.models.Image.draw_on_bg

Example
-------

.. code-block:: python

    from nider.models import Content
    from nider.models import Image


    content = Content(...)

    img = Image(content,
                fullpath='example.png',
                width=500,
                height=500
                )

    img.draw_on_bg('#efefef')

Check the full example `here <https://github.com/pythad/nider/blob/master/examples/draw_on_bg_example/script.py>`_ .

``Image.draw_on_image``
=======================

.. automethod:: nider.models.Image.draw_on_image

Examples
--------

.. code-block:: python

    from nider.models import Content
    from nider.models import Image


    content = Content(...)

    img = Image(content,
                fullpath='example.png',
                width=500,
                height=500
                )

    img.draw_on_image('example_bg.jpg')

Using filters and enhancements:

.. code-block:: python

    img.draw_on_image('example_bg.jpg',
                      image_enhancements=((ImageEnhance.Contrast, 0.75),
                                         (ImageEnhance.Brightness, 0.5)),
                      image_filters=((ImageFilter.BLUR),),
                      )

Check the full example `here <https://github.com/pythad/nider/blob/master/examples/draw_on_image_example/script.py>`_ .

============

That's it. After any of draw methods has been called and successfully completed the new image will be saved to ``Image.fullpath``.

*****************
Adding watermarks
*****************

``nider`` comes with built-in support for adding watermarks to your images.

First of all you need to create an instanse of :class:`nider.models.Watermark` class.

.. autoclass:: nider.models.Watermark


Example
=======

.. code-block:: python

    watermark = Watermark(text='COPYRIGHT',
                          font=Font('/home/me/.local/share/fonts/Roboto/Roboto-Bold.ttf'),
                          color='#111',
                          cross=True,
                          rotate_angle=-45,
                          opacity=0.35
                          )

============

After this you can either add watermark to you ``Content`` instance and draw watermark on ``nider`` generated images:

.. code-block:: python

    from nider.models import Content
    from nider.models import Image
    from nider.models import Watermark


    watermark = Watermark(...)

    content = Content(..., watermark=watermark)

    img = Image(content,
                fullpath='example.png',
                width=500,
                height=500
                )

    img.draw_on_bg('#efefef')

or you can add a watermark to an existing image using :func:`nider.tools.add_watermark`:

.. autofunction:: nider.tools.add_watermark

Example
=======

.. code-block:: python

    from nider.models import Watermark

    from nider.tools import add_watermark


    watermark = Watermark(...)
    add_watermark('path/to/my/img', watermark)
