import pygame
from pygame import Color

import planar.states as states

class LevelSelectState(states.State):
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.pop_state()

    def draw(self, screen):
        screen.fill(Color("black"))
