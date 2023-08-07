import pygame
from common import (SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, SNAKE_ORGIN, Direction)

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

class Game:
    def __init__(self):
        self.food = None
        self.snake = None
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.score = 0
        self.n_games = 0
        self.reward = 0
        self.game_over = False
        self.draw()
    def draw(self):
        self.screen.fill(BLACK)
        self.text = font.render("Score: " + str(self.score), True, WHITE)
        self.screen.blit(self.text, [0, 0])
    def reset(self):
        self.snake.body = SNAKE_ORGIN.copy()
        self.snake.head = self.snake.body[0]
        self.snake.direction = Direction.RIGHT
        self.score = 0
        self.n_games += 1
        self.game_over = False
        self.food.doesFoodExist = True
        self.food.move(self.snake)
    
    def detect_collisions(self):
        if self.food_collision():
            print("Food Collision @ ", self.food.cords)
            self.food.doesFoodExist = False
            self.score += 1
            self.reward = 10
        if self.wall_collision() or self.snake_collision():
            print("Wall Colliision @ ", self.snake.head) if self.wall_collision() else print("Snake Collision @ ", self.snake.head)
            self.reward = -10
            self.game_over = True
    def wall_collision(self):
        return self.snake.head.x == SCREEN_WIDTH or self.snake.head.x < 0 or self.snake.head.y >= SCREEN_HEIGHT or self.snake.head.y < 0
    def snake_collision(self):
        return self.snake.head in self.snake.body[1:]
    def food_collision(self):
        return self.snake.head == self.food.cords