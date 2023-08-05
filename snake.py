import pygame
from enum import Enum
from common import (Direction, BOX_SIZE, Point, WHITE, SCREEN_HEIGHT, SCREEN_WIDTH, State)

class Snake(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Snake, self).__init__()
        # TODO bug can't add third box
        self.body = [Point(75, 25), Point(50, 25)]
        self.direction = Direction.RIGHT
        self.screen = screen
        self.head = self.body[0]
    def draw(self, isFoodExists):
        block = pygame.Surface((BOX_SIZE, BOX_SIZE))
        block.fill(WHITE)
        self.screen.blits([(block, (cord.x, cord.y)) for cord in self.body])
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
    def get_state(self, food_cords):
        state = [0] * len(State)
        
        if self.direction == Direction.LEFT:
            if Point(self.head.x - BOX_SIZE, self.head.y) in self.body or self.head.x == 0:
                state[State.DAN_S.value] = 1
            if Point(self.head.x, self.head.y - BOX_SIZE) in self.body or self.head.y == 0:
                state[State.DAN_R.value] = 1
            if Point(self.head.x, self.head.y + BOX_SIZE) in self.body or self.head.y == SCREEN_HEIGHT - BOX_SIZE:
                state[State.DAN_L.value] = 1
        if self.direction == Direction.RIGHT:
            if Point(self.head.x + BOX_SIZE, self.head.y) in self.body or self.head.x == SCREEN_WIDTH - BOX_SIZE:
                state[State.DAN_S.value] = 1
            if Point(self.head.x, self.head.y + BOX_SIZE) in self.body or self.head.y == SCREEN_HEIGHT - BOX_SIZE:
                state[State.DAN_R.value] = 1
            if Point(self.head.x, self.head.y - BOX_SIZE) in self.body or self.head.y == 0:
                state[State.DAN_L.value] = 1
        if self.direction == Direction.UP:
            if Point(self.head.x, self.head.y - BOX_SIZE) in self.body or self.head.y == 0:
                state[State.DAN_S.value] = 1
            if Point(self.head.x + BOX_SIZE, self.head.y) in self.body or self.head.x == SCREEN_WIDTH - BOX_SIZE:
                state[State.DAN_R.value] = 1
            if Point(self.head.x - BOX_SIZE, self.head.y) in self.body or self.head.x == 0:
                state[State.DAN_L.value] = 1
        if self.direction == Direction.DOWN:
            if Point(self.head.x, self.head.y + BOX_SIZE) in self.body or self.head.y == SCREEN_HEIGHT - BOX_SIZE:
                state[State.DAN_S.value] = 1
            if Point(self.head.x - BOX_SIZE, self.head.y) in self.body or self.head.x == 0:
                state[State.DAN_R.value] = 1
            if Point(self.head.x + BOX_SIZE, self.head.y) in self.body or self.head.x == SCREEN_WIDTH - BOX_SIZE:
                state[State.DAN_L.value] = 1
        
        if self.direction == Direction.UP:
            state[State.DIR_U.value] = 1
        elif self.direction == Direction.DOWN:
            state[State.DIR_D.value] = 1
        elif self.direction == Direction.LEFT:
            state[State.DIR_L.value] = 1
        elif self.direction == Direction.RIGHT:
            state[State.DIR_R.value] = 1
        
        if food_cords.x < self.head.x:
            state[State.FOO_L.value] = 1
        elif food_cords.x > self.head.x:
            state[State.FOO_R.value] = 1
        if food_cords.y < self.head.y:
            state[State.FOO_U.value] = 1
        elif food_cords.y > self.head.y:
            state[State.FOO_D.value] = 1

        return state