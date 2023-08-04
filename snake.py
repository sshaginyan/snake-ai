import pygame
from common import (Direction, BOX_SIZE, Point)

# TODO seperate in different file
WHITE = (255, 255, 255)

class Snake(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Snake, self).__init__()
        # TODO bug can't add third box
        self.body = [Point(75, 25), Point(50, 25)]
        self.direction = Direction.RIGHT
        self.screen = screen
        self.head = self.body[0]
    def draw(self, isFoodExists):
        for cord in self.body:
            # TODO look into https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blits
            block = pygame.Surface((BOX_SIZE, BOX_SIZE))
            block.fill(WHITE)
            self.screen.blit(block, (cord.x, cord.y))
        self._move(isFoodExists)
    def _move(self, isFoodExists):
        head = self.body[0]
        if self.direction == Direction.RIGHT:
            self.body.insert(0, Point(head.x + BOX_SIZE, head.y))
        elif self.direction == Direction.DOWN:
            self.body.insert(0, Point(head.x, head.y + BOX_SIZE))
        elif self.direction == Direction.LEFT:
            self.body.insert(0, Point(head.x - BOX_SIZE, head.y))
        else:
            self.body.insert(0, Point(head.x, head.y - BOX_SIZE))
        self.head = self.body[0]
        if isFoodExists:
            self.body.pop()