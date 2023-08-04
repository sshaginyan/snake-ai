# import sys
# import pygame
# from game import Game
# from food import Food
# from snake import Snake

# from common import (Direction, SCREEN_HEIGHT, SCREEN_WIDTH)

# game = Game()
# snake = Snake(game.screen)
# food = Food(game.screen)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and snake.direction != Direction.DOWN:
#                 snake.direction = Direction.UP
#             elif event.key == pygame.K_DOWN and snake.direction != Direction.UP:
#                 snake.direction = Direction.DOWN
#             elif event.key == pygame.K_LEFT and snake.direction != Direction.RIGHT:
#                 snake.direction = Direction.LEFT
#             elif event.key == pygame.K_RIGHT and snake.direction != Direction.LEFT:
#                 snake.direction = Direction.RIGHT

#     if(snake.head == food.cords):
#         food.isFoodExists = False
#     elif snake.head.x >= SCREEN_WIDTH or snake.head.x < 0 or snake.head.y >= SCREEN_HEIGHT or snake.head.y < 0 or snake.head in snake.body[1:]:
#         game.over()

#     game.draw()
#     snake.draw(food.isFoodExists)
#     food.draw(snake.body)
#     pygame.display.flip()
#     pygame.time.Clock().tick(20)

from game import Game
Game().game_loop()