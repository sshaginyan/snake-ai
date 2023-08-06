import pygame
from enum import Enum
from common import (Direction, BOX_SIZE, Point, WHITE, SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_ORGIN)

State = Enum('State', [
    'DAN_S', 'DAN_R', 'DAN_L', 'DIR_L', 'DIR_R',
    'DIR_U', 'DIR_D', 'FOO_L', 'FOO_R', 'FOO_U', 'FOO_D'
], start=0)

class Snake(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Snake, self).__init__()
        # TODO bug can't add third box
        # TODO put this in common.py, but we have #block bug ^^^
        self.body = SNAKE_ORGIN.copy()
        self.direction = Direction.RIGHT
        self.screen = screen
        self.head = self.body[0]
        self.draw()
    def draw(self):
        block = pygame.Surface((BOX_SIZE, BOX_SIZE))
        block.fill(WHITE)
        self.screen.blits([(block, (cord.x, cord.y)) for cord in self.body])
    def move(self):
        if self.direction == Direction.RIGHT:
            self.body.insert(0, Point(self.head.x + BOX_SIZE, self.head.y))
        elif self.direction == Direction.DOWN:
            self.body.insert(0, Point(self.head.x, self.head.y + BOX_SIZE))
        elif self.direction == Direction.LEFT:
            self.body.insert(0, Point(self.head.x - BOX_SIZE, self.head.y))
        elif self.direction == Direction.UP:
            self.body.insert(0, Point(self.head.x, self.head.y - BOX_SIZE))
        self.head = self.body[0]
    def get_state(self, food):
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
        
        if food.cords.x < self.head.x:
            state[State.FOO_L.value] = 1
        elif food.cords.x > self.head.x:
            state[State.FOO_R.value] = 1
        if food.cords.y < self.head.y:
            state[State.FOO_U.value] = 1
        elif food.cords.y > self.head.y:
            state[State.FOO_D.value] = 1

        return state