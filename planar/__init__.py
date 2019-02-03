import sys

import pygame

import planar.constants
from planar.states.menu import MenuState

class Game(object):
    def __init__(self, start):
        size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        constants.GAME_FONT = pygame.freetype.Font("planar/font/ZCOOLKuaiLe-Regular.ttf", 72)

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
                for state in reversed(self.states):
                    state.draw(self.screen)
                    if not state.transparent:
                        break

            pygame.display.flip()
            pygame.display.update()

        pygame.quit()
        sys.exit()
