import sys

import pygame

import planar.constants
from planar.states.menu import MenuState
import planar.leveldata

class Game(object):
    def __init__(self):
        size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        constants.GAME_FONT = pygame.freetype.Font("planar/font/ZCOOLKuaiLe-Regular.ttf", 72)
        constants.LARGE_FONT = pygame.freetype.Font("planar/font/ZCOOLKuaiLe-Regular.ttf", 56)
        constants.MED_FONT = pygame.freetype.Font("planar/font/ZCOOLKuaiLe-Regular.ttf", 32)
        constants.SMALL_FONT = pygame.freetype.Font("planar/font/ZCOOLKuaiLe-Regular.ttf", 18)

        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(size, 0, 32)

        self.states = []

        self.levels = leveldata.levels
        self.cur_level = 5

    def push_state(self, state):
        state.game = self
        self.states.append(state)

    def pop_state(self):
        self.states.pop()

    def run(self):
        while self.running:
            # update all states
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    break

            if self.states:
                # update topmost state
                self.states[-1].update(events)

                # draw topmost state
                for i in reversed(range(len(self.states))):
                    if not self.states[i].transparent:
                        break
                for state in self.states[i:]:
                    state.draw(self.screen)

            pygame.display.flip()
            pygame.display.update()

        pygame.quit()
        sys.exit()
