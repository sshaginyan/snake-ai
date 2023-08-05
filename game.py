import sys
import pygame
from common import (SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE)

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.score = 0
        self.n_games = 0
    def draw(self):
        self.screen.fill(BLACK)
        self.text = font.render("Score: " + str(self.score), True, WHITE)
        self.screen.blit(self.text, [0, 0])
    def over(self):
        self.n_games += 1
        pygame.quit()
        sys.exit()