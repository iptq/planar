import pygame
from pygame import Color

import planar.constants as constants
import planar.states as states

class GameState(states.State):
    def __init__(self, level):
        self.level = level

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.pop_state()

    def draw(self, screen):
        screen.fill(Color(100, 80, 100))

        scale = constants.SCREEN_WIDTH // (2 * self.level.dim[0] + 6)
        left, right = self.level.render(scale)

        yoff = constants.SCREEN_HEIGHT - (self.level.dim[1] + 4) * scale

        screen.blit(left, (2 * scale, yoff + 2 * scale))
        screen.blit(right, ((4 + self.level.dim[0]) * scale, yoff + 2 * scale))
