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

model = torch.load("./model/model.pth") if len(glob.glob("./model/*.pth")) == 1 else LinearQNet(11, 256, 3)
trainer = QTrainer(model, lr=LR, gamma=gamma)
memory = deque(maxlen=MAX_MEMORY)
record = 0

pygame.init()
game = Game()
snake = Snake(game.screen)
food = Food(game.screen, snake)

epsilon = 0
def get_next_snake_move(current_state, n_games):
    epsilon = 80 - n_games
    move = [0] * 3
    
    if random.randint(0, 200) < epsilon:
        move[random.randint(0, 2)] = 1
    else:
        state_tensor = torch.tensor(current_state, dtype=torch.float)
        prediction = model(state_tensor)
        move_index = torch.argmax(prediction).item()
        move[move_index] = 1
    
    return move

def food_collision(snake, food):
    return snake.head_cords == food.cords
def wall_collision(snake):
    return snake.head_cords.x >= SCREEN_WIDTH or snake.head_cords.x < 0 or \
        snake.head_cords.y >= SCREEN_HEIGHT or snake.head_cords.y < 0
def snake_collision(snake):
    return snake.head_cords in snake.body[1:]

# index = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP and snake.direction != Direction.DOWN:
        #         snake.direction = Direction.UP
        #     elif event.key == pygame.K_DOWN and snake.direction != Direction.UP:
        #         snake.direction = Direction.DOWN
        #     elif event.key == pygame.K_LEFT and snake.direction != Direction.RIGHT:
        #         snake.direction = Direction.LEFT
        #     elif event.key == pygame.K_RIGHT and snake.direction != Direction.LEFT:
        #         snake.direction = Direction.RIGHT
    
    current_state = snake.get_state(food)
    snake_move = get_next_snake_move(current_state, game.n_games)
    
    if snake_move.index(1) == 1:
        snake.direction = Direction((snake.direction.value - 1) % 4)
    elif snake_move.index(1) == 2:
        snake.direction = Direction((snake.direction.value + 1) % 4)

    game.draw() 
    snake.move()
    
    if wall_collision(snake) or snake_collision(snake):
        print("Wall Colliision @ ", snake.head_cords) if wall_collision(snake) else print("Snake Collision @ ", snake.head_cords)
        game.reward = -10
        game.over = True
    elif food_collision(snake, food):
        print("Food Collision @ ", food.cords)
        game.score += 1
        game.reward = 10
        food.exists = False

    if food.exists:
        snake.body.pop()
    else:
        food.place(snake)
    
    snake.draw()
    food.draw()

    new_state = snake.get_state(food)
    trainer.train_step(current_state, snake_move, game.reward, new_state, game.over)
    memory.append((current_state, snake_move, game.reward, new_state, game.over))


    if game.over:
        game.over = False
        if len(memory) > BATCH_SIZE:
            mini_sample = random.sample(memory, BATCH_SIZE)        
        else:
            mini_sample = memory
        
        states, actions, rewards, next_states, overs = zip(*mini_sample)
        trainer.train_step(states, actions, rewards, next_states, overs)

        if game.score > record:
            record = game.score
            model.save()
            print("Game: ", game.n_games, " Score: ", game.score, "Record: ", record)
        
        game = Game(game.n_games)
        snake = Snake(game.screen)
        food = Food(game.screen, snake)
    
    #pygame.image.save(game.screen, "./images/" + str(index) + "-" + '-'.join([str(n)  for n in new_state]) + ".jpg")
    pygame.display.flip()
    pygame.time.Clock().tick(20)