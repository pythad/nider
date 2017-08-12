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

*******
Example
*******

Creating a simple image is as easy as

.. code-block:: python

    from nider.models import Content
    from nider.models import Header
    from nider.models import Linkback
    from nider.models import Paragraph
    from nider.models import Image

    header = Header('Your super interesting title!')
    para = Paragraph('Lorem ipsum dolor sit amet.')
    linkback = Linkback('foo.com | @username')
    content = Content(para, header, linkback, padding=60)

    img = Image(content, fullpath='result.png')

    img.draw_on_bg('#212121')

*********************
Drawn using ``nider``
*********************

On a textture
=============

.. image:: https://github.com/pythad/nider/raw/master/examples/draw_on_texture_example/result.png
        :alt: Draw on texture example

On a solid color
================

.. image:: https://github.com/pythad/nider/raw/master/examples/draw_on_bg_example/result.png
        :alt: Draw on background example
        :height: 500px
        :width: 500px

On an image
===========

.. image:: https://github.com/pythad/nider/raw/master/examples/draw_on_image_example/result.png
        :alt: Draw on image example


===================

Code used to generate featured images can be found `here <https://github.com/pythad/nider/tree/master/examples>`_