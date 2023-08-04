import pygame
import random
from common import (SCREEN_WIDTH, SCREEN_HEIGHT, BOX_SIZE, Point)

RED = (255, 0, 0)

class Food(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Food, self).__init__()
        self.isFoodExists = False
        self.food = pygame.Surface((BOX_SIZE, BOX_SIZE))
        self.food.fill(RED)
        self.screen = screen
        self.cords = Point(-1, -1)
    def _get_cords(self, snake_body):
        head = snake_body[0]
        food_cords = Point(head.x, head.y)
        while food_cords in snake_body:
            food_cords = Point(
                random.randrange(0, SCREEN_WIDTH - BOX_SIZE, BOX_SIZE),
                random.randrange(0, SCREEN_HEIGHT - BOX_SIZE, BOX_SIZE)
            )
        return food_cords
    def draw(self, snake_body):
        if not self.isFoodExists:
            self.isFoodExists = True
            self.cords = self._get_cords(snake_body)
            
        self.screen.blit(self.food, self.cords)