from collections import namedtuple
from collections import ChainMap

rgb = namedtuple('Color', ['R', 'G', 'B'])

# RGB : color mappings
BASIC_COLORS_RGB_TO_NAME = {
    rgb(255, 255, 255): ['white'],
    rgb(0, 0, 0): ['black'],
    rgb(255, 0, 0): ['red'],
    rgb(0, 255, 0): ['lime'],
    rgb(0, 0, 255): ['blue'],
    rgb(255, 255, 0): ['yellow'],
    rgb(0, 255, 255): ['cyan', 'aqua'],
    rgb(255, 0, 255): ['magenta', 'fuchsia'],
    rgb(192, 192, 192): ['silver'],
    rgb(128, 128, 128): ['gray'],
    rgb(128, 0, 0): ['maroon'],
    rgb(128, 128, 0): ['olive'],
    rgb(0, 128, 0): ['green'],
    rgb(128, 0, 128): ['purple'],
    rgb(0, 128, 128): ['teal'],
    rgb(0, 0, 128): ['navy'],

}

FLAT_UI_COLORS_RGB_TO_NAMES = {
    rgb(26, 188, 156): ['turquoise'],
    rgb(46, 204, 113): ['emerland'],
    rgb(52, 152, 219): ['peterriver'],
    rgb(155, 89, 182): ['amethyst'],
    rgb(52, 73, 94): ['wetasphalt'],
    rgb(22, 160, 133): ['greensea'],
    rgb(39, 174, 96): ['nephritis'],
    rgb(41, 128, 185): ['belizehole'],
    rgb(142, 68, 173): ['wisteria'],
    rgb(44, 62, 80): ['midnightblue'],
    rgb(241, 196, 15): ['sunflower'],
    rgb(230, 126, 34): ['carrot'],
    rgb(231, 76, 60): ['alizarin'],
    rgb(236, 240, 241): ['clouds'],
    rgb(149, 165, 166): ['concrete'],
    rgb(243, 156, 18): ['orange'],
    rgb(211, 84, 0): ['pumpkin'],
    rgb(192, 57, 43): ['pomegranate'],
    rgb(189, 195, 199): ['silver'],
    rgb(127, 140, 141): ['asbestos']
}

# color : RGB mappings
BASIC_COLORS = dict(
    (name.lower(), rgb)
    for rgb, names in BASIC_COLORS_RGB_TO_NAME.items()
    for name in names)

FLAT_UI_COLORS = dict(
    (name.lower(), rgb)
    for rgb, names in FLAT_UI_COLORS_RGB_TO_NAMES.items()
    for name in names)

# dictionary of all availabe colors
COLORS = dict(ChainMap(BASIC_COLORS, FLAT_UI_COLORS))
