# Snake Game!
# Author: Logan Markley
# Last Updated: 7/28/2023
# Version: 1.0
# Date Started: 7/28/2023
# Desc: Using Clear Code's Youtube video "Learning pygame by creating Snake", the famous Snake game will be replicated

import pygame, sys


pygame.init()
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175,215,70))
    pygame.display.update()
    clock.tick(60)      # game never runs faster than 60 times per second to make the game consistent