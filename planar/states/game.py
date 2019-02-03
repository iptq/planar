import pygame
import copy
from pygame import Color

import planar.constants as constants
import planar.states as states

class GameState(states.State):
    def __init__(self, level):
        self.original = copy.deepcopy(level)
        self.level = level

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.pop_state()

                elif event.key == pygame.K_r:
                    self.level = copy.deepcopy(self.original)
                elif event.key == pygame.K_w:
                    self.level.players[0].try_move(constants.UP)
                elif event.key == pygame.K_a:
                    self.level.players[0].try_move(constants.LEFT)
                elif event.key == pygame.K_s:
                    self.level.players[0].try_move(constants.DOWN)
                elif event.key == pygame.K_d:
                    self.level.players[0].try_move(constants.RIGHT)
                elif event.key == pygame.K_i:
                    self.level.players[1].try_move(constants.UP)
                elif event.key == pygame.K_j:
                    self.level.players[1].try_move(constants.LEFT)
                elif event.key == pygame.K_k:
                    self.level.players[1].try_move(constants.DOWN)
                elif event.key == pygame.K_l:
                    self.level.players[1].try_move(constants.RIGHT)
                elif event.key == pygame.K_z:
                    self.level.undo()

    def draw(self, screen):
        screen.fill(Color(100, 80, 100))

        scale = constants.SCREEN_WIDTH // (2 * self.level.dim[0] + 6)
        left, right = self.level.render(scale)

        yoff = constants.SCREEN_HEIGHT / 2 - (self.level.dim[1] + 4) * scale / 2

        screen.blit(left, (2 * scale, yoff + 2 * scale))
        screen.blit(right, ((4 + self.level.dim[0]) * scale, yoff + 2 * scale))
