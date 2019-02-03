import sys

import level
import constants

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption('test')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

lvl = Level((10, 10), [], [])

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    screen.blit(background, (0, 0))
    map_layer = pygame.Surface(lvl.dim)
    pygame.display.flip()
