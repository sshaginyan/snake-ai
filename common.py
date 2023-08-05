from enum import Enum
from collections import namedtuple

BOX_SIZE = 25
BLACK = (0, 0, 0)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
Point = namedtuple("Point", ['x', 'y'])
Direction = Enum('Direction', ['UP', 'LEFT', 'DOWN', 'RIGHT'], start=0)
State = Enum('State', [
    'DAN_S', 'DAN_R', 'DAN_L', 'DIR_L', 'DIR_R',
    'DIR_U', 'DIR_D', 'FOO_L', 'FOO_R', 'FOO_U', 'FOO_D'
], start=0)