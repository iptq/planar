import pygame
from pygame import Color

import planar.states as states
from planar.states.game import GameState
from planar.level import Level, Block, Segment, Player

class LevelSelectState(states.State):
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.pop_state()
                elif event.key == pygame.K_1:
                    level = Level((10, 10), [
                        Block([
                            Segment(0, 0, 0, 1),
                            Segment(0, 1, 0, 0)
                        ], True, 0, [255, 10, 100])
                    ], [
                        Player(5, 5, 0, [66, 134, 244]),
                        Player(5, 5, 1, [244, 83, 65])
                    ])
                    self.game.push_state(GameState(level))

    def draw(self, screen):
        screen.fill(Color("black"))
