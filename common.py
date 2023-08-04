from enum import Enum
from collections import namedtuple

BOX_SIZE = 25
BLACK = (0, 0, 0)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
Point = namedtuple("Point", ['x', 'y'])
Direction = Enum('Direction', ['UP', 'DOWN', 'LEFT', 'RIGHT'])