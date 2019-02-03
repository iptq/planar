import pygame
from pygame import Color

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
        layers = self.level.render(30)
        print(layers)
