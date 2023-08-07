import pygame
from common import (SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE)

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

class Game:
    def __init__(self, n_games=0):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.score = 0
        self.n_games = n_games
        self.reward = 0
        self.over = False
    def draw(self):
        self.screen.fill(BLACK)
        score_text = font.render("Score: " + str(self.score), True, WHITE)
        self.screen.blit(score_text, [0, 0])