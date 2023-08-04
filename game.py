import sys
import pygame
from food import Food
from snake import Snake
from common import (SCREEN_WIDTH, SCREEN_HEIGHT, Direction, BLACK, WHITE)

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.snake = Snake(self.screen)
        self.food = Food(self.screen)
        self.score = 0
    def draw(self):
        self.screen.fill(BLACK)
        self.text = font.render("Score: " + str(self.score), True, WHITE)
        self.screen.blit(self.text, [0, 0])
    def over(self):
        pygame.quit()
        sys.exit()
    def collisions(self):
        if(self.snake.head == self.food.cords):
            self.food.isFoodExists = False
            self.score += 1
        elif self.snake.head.x >= SCREEN_WIDTH or self.snake.head.x < 0 or \
            self.snake.head.y >= SCREEN_HEIGHT or self.snake.head.y < 0 or \
            self.snake.head in self.snake.body[1:]:
            self.over()
    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != Direction.DOWN:
                        self.snake.direction = Direction.UP
                    elif event.key == pygame.K_DOWN and self.snake.direction != Direction.UP:
                        self.snake.direction = Direction.DOWN
                    elif event.key == pygame.K_LEFT and self.snake.direction != Direction.RIGHT:
                        self.snake.direction = Direction.LEFT
                    elif event.key == pygame.K_RIGHT and self.snake.direction != Direction.LEFT:
                        self.snake.direction = Direction.RIGHT

            self.collisions()    
            
            self.draw()
            self.snake.draw(self.food.isFoodExists)
            self.food.draw(self.snake.body)
            pygame.display.flip()
            pygame.time.Clock().tick(20)