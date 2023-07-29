# Snake Game!
# Author: Logan Markley
# Last Updated: 7/28/2023
# Version: 1.1
# Latest Addition: added the Fruit class with randomly generated position on the board
# Date Started: 7/28/2023
# Desc: Using Clear Code's Youtube video "Learning pygame by creating Snake", the famous Snake game will be replicated

import pygame, sys, random
from pygame.math import Vector2

class Fruit:
    def __init__(self):
        # create a random x and y position
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)  # 2-d vector from pygame.math which stores the position of the fruit

    def draw_fruit(self):
        # create a rectangle and draw it
        fruit_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size, cell_size, cell_size)      #Rect(x,y,w,h)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
clock = pygame.time.Clock()

fruit = Fruit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175,215,70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)      # game never runs faster than 60 times per second to make the game consistent