from enum import Enum
from collections import namedtuple

BOX_SIZE = 20
BLACK = (0, 0, 0)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WHITE = (255, 255, 255)
Point = namedtuple("Point", ['x', 'y'])
Direction = Enum('Direction', ['UP', 'LEFT', 'DOWN', 'RIGHT'], start=0)
SNAKE_ORGIN = [Point(BOX_SIZE*3, BOX_SIZE), Point(BOX_SIZE*2, BOX_SIZE), Point(BOX_SIZE, BOX_SIZE)]