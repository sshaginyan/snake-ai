import sys
import glob
import torch
import pygame
import random
from game import Game
from food import Food
from snake import Snake
from collections import deque
from model import (LinearQNet, QTrainer)
from common import (Direction, SCREEN_HEIGHT, SCREEN_WIDTH)

LR = 1e-3
gamma = 0.9
MAX_MEMORY = 100_000
BATCH_SIZE = 1000

# TODO figure out where this is coming from `adam`?
#glob.glob("/home/adam/*.txt")
#model = torch.load("./model/model.pth") if len(glob.glob("./model/*.pth")) == 1 else LinearQNet(11, 256, 3)
model = LinearQNet(11, 256, 3)
trainer = QTrainer(model, lr=LR, gamma=gamma)
memory = deque(maxlen=MAX_MEMORY)

game = Game()
snake = Snake(game.screen)
food = Food(game.screen)

epsilon = 0
def next_move(old_state, n_games):
    epsilon = 80 - n_games
    move = [0] * 3
    
    if random.randint(0, 200) < epsilon:
        move[random.randint(0, 2)] = 1
    else:
        state_tensor = torch.tensor(old_state, dtype=torch.float)
        prediction = model(state_tensor)
        move_index = torch.argmax(prediction).item()
        move[move_index] = 1
    
    return move

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != Direction.DOWN:
                snake.direction = Direction.UP
            elif event.key == pygame.K_DOWN and snake.direction != Direction.UP:
                snake.direction = Direction.DOWN
            elif event.key == pygame.K_LEFT and snake.direction != Direction.RIGHT:
                snake.direction = Direction.LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != Direction.LEFT:
                snake.direction = Direction.RIGHT

    old_state = snake.get_state(food.cords)
    move = next_move(old_state, game.n_games)
    if move.index(1) == 2:
        snake.direction = Direction((snake.direction.value + 1) % 4)
    elif move.index(1) == 1:
        snake.direction = Direction((snake.direction.value - 1) % 4)
    snake._move(food.isFoodExists)
    new_state = snake.get_state(food.cords)
    trainer.train_step(old_state, move, game.reward, new_state, game.game_over)
    
    memory.append((old_state, move, game.reward, new_state, game.game_over))

    if len(memory) > BATCH_SIZE:
        mini_sample = random.sample(memory, BATCH_SIZE)        
    else:
        mini_sample = memory
    
    states, actions, rewards, next_states, dones = zip(*mini_sample)
    trainer.train_step(states, actions, rewards, next_states, dones)
    # game.score




    
    if(snake.head == food.cords):
        food.isFoodExists = False
        game.score += 1
        game.reward = 10
    elif snake.head.x >= SCREEN_WIDTH or snake.head.x < 0 or \
        snake.head.y >= SCREEN_HEIGHT or snake.head.y < 0 or \
        snake.head in snake.body[1:]:
        game.reward = -10
        game.game_over = True

    game.draw()
    snake.draw(food.isFoodExists)
    food.draw(snake.body)
    pygame.display.flip()
    pygame.time.Clock().tick(20)