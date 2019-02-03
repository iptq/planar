import sys

import pygame

import planar.constants
from planar.states.menu import MenuState

class Game(object):
    def __init__(self):
        size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        constants.GAME_FONT = pygame.freetype.Font("planar/font/ZCOOLKuaiLe-Regular.ttf", 72)

        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(size, 0, 32)

        self.states = []

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
            for state in reversed(self.states):
                state.update(events)

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
