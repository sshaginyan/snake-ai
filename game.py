import pygame
from common import (SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, Point)

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.score = 0
        self.n_games = 0
        self.reward = 0
        self.game_over = False
    def draw(self):
        self.screen.fill(BLACK)
        self.text = font.render("Score: " + str(self.score), True, WHITE)
        self.screen.blit(self.text, [0, 0])
    def reset(self, snake):
        # TODO put this in common.py, but we have #block bug
        snake.body = [Point(75, 25), Point(50, 25), Point(25, 25)]
        self.score = 0
        self.n_games += 1