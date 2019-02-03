#!/usr/bin/env python3

from pygame.locals import *
import pygame
import sys

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        pygame.display.update()
