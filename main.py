# Snake Game!
# Author: Logan Markley
# Last Updated: 7/30/2023
# Version: 1.5
# Latest Addition: Game Over States (out of bounds or hitting own body), and better input management
# Date Started: 7/28/2023
# Desc: Using Clear Code's Youtube video "Learning pygame by creating Snake", the famous Snake game will be replicated

import pygame, sys, random
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body = [Vector2(4,10), Vector2(3,10), Vector2(2,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x*cell_size, block.y*cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (183,191,122), block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        self.new_block = False

    def add_block(self):
        self.new_block = True

class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        # create a rectangle and draw it
        fruit_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size, cell_size, cell_size)      #Rect(x,y,w,h)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def randomize(self):
        # create a random x and y position
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)  # 2-d vector from pygame.math which stores the position of the fruit

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 140)   #this event is triggered every 150 ms

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1,0)

    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)      # game never runs faster than 60 times per second to make the game consistent