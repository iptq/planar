import sys

import pygame

import constants

class Game(object):
    def __init__(self, start):
        size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        constants.GAME_FONT = pygame.freetype.Font("font/ZCOOLKuaiLe-Regular.ttf")

        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(size, 0, 32)

        self.states = [start]

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    self.running = False

            # draw topmost state
            if self.states:
                self.states[-1].draw()

            pygame.display.flip()
            pygame.display.update()

        pygame.quit()
        sys.exit()

class State(object):
    def __init__(self, transparent=False):
        self.transparent = transparent

    def draw(self):
        raise NotImplementedException(f"draw() not implemented for {self.__class__}")
