import sys

import planar.level as level
import planar.constants as constants

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption('test')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

lvl = level.Level((10, 10), [
    level.Block([
        level.Segment(0, 0, 0, 1)
    ], True, 0, [255, 10, 100])
], [])

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    screen.blit(background, (0, 0))
    renders = lvl.render(50, 2)
    screen.blit(renders[0], (0, 0))
    pygame.display.flip()
