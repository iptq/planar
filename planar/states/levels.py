import pygame
from pygame import Color

import planar.states as states
from planar.states.game import GameState

class LevelSelectState(states.State):
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.pop_state()
                elif event.key == pygame.K_1:
                    self.game.push_state(GameState())

    def draw(self, screen):
        screen.fill(Color("black"))
