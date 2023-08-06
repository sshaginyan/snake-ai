import pygame
import random
from common import (SCREEN_WIDTH, SCREEN_HEIGHT, BOX_SIZE, Point)

RED = (255, 0, 0)

class Food(pygame.sprite.Sprite):
    def __init__(self, screen, snake):
        super(Food, self).__init__()
        self.doesFoodExist = True
        self.screen = screen
        self.move(snake)
        
        
        self.food_surface = pygame.Surface((BOX_SIZE, BOX_SIZE))
        self.food_surface.fill(RED)
        self.draw()
    def move(self, snake):
        self.doesFoodExist = True
        self.cords = Point(snake.head.x, snake.head.y)
        while self.cords in snake.body:
            self.cords = Point(
                random.randrange(0, SCREEN_WIDTH - BOX_SIZE, BOX_SIZE),
                random.randrange(0, SCREEN_HEIGHT - BOX_SIZE, BOX_SIZE)
            )
    def draw(self):
        self.screen.blit(self.food_surface, self.cords)