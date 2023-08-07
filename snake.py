import pygame
from enum import Enum
from common import (Direction, BOX_SIZE, Point, WHITE, SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_ORGIN)

State = Enum('State', [
    'DAN_S', 'DAN_R', 'DAN_L', 'DIR_L', 'DIR_R',
    'DIR_U', 'DIR_D', 'FOO_L', 'FOO_R', 'FOO_U', 'FOO_D'
], start=0)

BLUE = (135, 206, 250)

class Snake(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Snake, self).__init__()
        self.body = SNAKE_ORGIN.copy()
        self.direction = Direction.RIGHT
        self.screen = screen
        self.head_cords = self.body[0]
        self.block_surface = pygame.Surface((BOX_SIZE, BOX_SIZE))
    def draw(self):
        self.block_surface.fill(BLUE)
        self.screen.blit(self.block_surface, (self.head_cords.x, self.head_cords.y))
        self.block_surface.fill(WHITE)
        self.screen.blits([(self.block_surface, (cord.x, cord.y)) for cord in self.body[1:]])
    def move(self):
        if self.direction == Direction.RIGHT:
            self.body.insert(0, Point(self.head_cords.x + BOX_SIZE, self.head_cords.y))
        elif self.direction == Direction.DOWN:
            self.body.insert(0, Point(self.head_cords.x, self.head_cords.y + BOX_SIZE))
        elif self.direction == Direction.LEFT:
            self.body.insert(0, Point(self.head_cords.x - BOX_SIZE, self.head_cords.y))
        elif self.direction == Direction.UP:
            self.body.insert(0, Point(self.head_cords.x, self.head_cords.y - BOX_SIZE))
        self.head_cords = self.body[0]
    def get_state(self, food):
        state = [0] * len(State)
        
        if self.direction == Direction.RIGHT:
            if Point(self.head_cords.x + BOX_SIZE, self.head_cords.y) in self.body or self.head_cords.x == SCREEN_WIDTH - BOX_SIZE:
                print("Danger @ STRAIGHT WALL")
                state[State.DAN_S.value] = 1
            if Point(self.head_cords.x, self.head_cords.y + BOX_SIZE) in self.body or self.head_cords.y == SCREEN_HEIGHT - BOX_SIZE:
                print("Danger @ RIGHT WALL")
                state[State.DAN_R.value] = 1
            if Point(self.head_cords.x, self.head_cords.y - BOX_SIZE) in self.body or self.head_cords.y == 0:
                print("Danger @ LEFT WALL")
                state[State.DAN_L.value] = 1
        if self.direction == Direction.LEFT:
            if Point(self.head_cords.x - BOX_SIZE, self.head_cords.y) in self.body or self.head_cords.x == 0:
                print("Danger @ STRAIGHT WALL")
                state[State.DAN_S.value] = 1
            if Point(self.head_cords.x, self.head_cords.y - BOX_SIZE) in self.body or self.head_cords.y == 0:
                print("Danger @ RIGHT WALL")
                state[State.DAN_R.value] = 1
            if Point(self.head_cords.x, self.head_cords.y + BOX_SIZE) in self.body or self.head_cords.y == SCREEN_HEIGHT - BOX_SIZE:
                print("Danger @ LEFT WALL")
                state[State.DAN_L.value] = 1
        if self.direction == Direction.UP:
            if Point(self.head_cords.x, self.head_cords.y - BOX_SIZE) in self.body or self.head_cords.y == 0:
                print("Danger @ STRAIGHT WALL")
                state[State.DAN_S.value] = 1
            if Point(self.head_cords.x + BOX_SIZE, self.head_cords.y) in self.body or self.head_cords.x == SCREEN_WIDTH - BOX_SIZE:
                print("Danger @ RIGHT WALL")
                state[State.DAN_L.value] = 1
            if Point(self.head_cords.x - BOX_SIZE, self.head_cords.y) in self.body or self.head_cords.x == 0:
                print("Danger @ LEFT WALL")
                state[State.DAN_R.value] = 1
        if self.direction == Direction.DOWN:
            if Point(self.head_cords.x, self.head_cords.y + BOX_SIZE) in self.body or self.head_cords.y == SCREEN_HEIGHT - BOX_SIZE:
                print("Danger @ STRAIGHT WALL")
                state[State.DAN_S.value] = 1
            if Point(self.head_cords.x - BOX_SIZE, self.head_cords.y) in self.body or self.head_cords.x == 0:
                print("Danger @ RIGHT WALL")
                state[State.DAN_R.value] = 1
            if Point(self.head_cords.x + BOX_SIZE, self.head_cords.y) in self.body or self.head_cords.x == SCREEN_WIDTH - BOX_SIZE:
                print("Danger @ LEFT WALL")
                state[State.DAN_L.value] = 1
        
        if self.direction == Direction.UP:
            state[State.DIR_U.value] = 1
        elif self.direction == Direction.DOWN:
            state[State.DIR_D.value] = 1
        elif self.direction == Direction.LEFT:
            state[State.DIR_L.value] = 1
        elif self.direction == Direction.RIGHT:
            state[State.DIR_R.value] = 1
        
        if food.cords.x < self.head_cords.x:
            state[State.FOO_L.value] = 1
        elif food.cords.x > self.head_cords.x:
            state[State.FOO_R.value] = 1
        if food.cords.y < self.head_cords.y:
            state[State.FOO_U.value] = 1
        elif food.cords.y > self.head_cords.y:
            state[State.FOO_D.value] = 1

        return state