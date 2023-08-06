from enum import Enum
from collections import namedtuple

BOX_SIZE = 25
BLACK = (0, 0, 0)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
Point = namedtuple("Point", ['x', 'y'])
Direction = Enum('Direction', ['UP', 'LEFT', 'DOWN', 'RIGHT'], start=0)
SNAKE_ORGIN = [Point(75, 25), Point(50, 25), Point(25, 25)]