import sys

import pygame

import constants

class Game(object):
    def __init__(self):
        size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(size, 0, 32)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit()

class StateMachine(object):
    def __init__(self, start):
        self.states = [start]

class State(object):
    def __init__(self):
        pass
