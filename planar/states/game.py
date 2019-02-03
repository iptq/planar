import pygame
import copy
from pygame import Color
from math import floor, ceil

import planar.constants as constants
import planar.states as states
from planar.states.end import EndState

class GameState(states.State):
    def __init__(self, level):
        self.original = copy.deepcopy(level)
        self.level = level

        self.transitioning = False
        self.animation_progress = 0
        self.move_result = []
        self.original_positions = []

    def update(self, events):
        self.game.clock.tick()
        if self.transitioning:
            dt = self.game.clock.get_time() / 1000 * 6
            if self.animation_progress + dt > 1:
                for (block, d), (x, y) in zip(self.move_result, self.original_positions):
                    block.x = x
                    block.y = y
                    self.level.move_block(block, d)
                self.level.move_stack.append(self.move_result)
                self.transitioning = 0
                self.animation_progress = 0
                self.move_result = []
                self.original_positions = []
            else:
                self.animation_progress += dt
                for block, d in self.move_result:
                    block.x += dt * d[0]
                    block.y += dt * d[1]
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.pop_state()
                if not self.transitioning:
                    if event.key == pygame.K_r:
                        self.level = copy.deepcopy(self.original)
                    elif event.key == pygame.K_w:
                        self.move_result = self.level.players[0].try_move(constants.UP)
                    elif event.key == pygame.K_a:
                        self.move_result = self.level.players[0].try_move(constants.LEFT)
                    elif event.key == pygame.K_s:
                        self.move_result = self.level.players[0].try_move(constants.DOWN)
                    elif event.key == pygame.K_d:
                        self.move_result = self.level.players[0].try_move(constants.RIGHT)
                    elif event.key == pygame.K_i:
                        self.move_result = self.level.players[1].try_move(constants.UP)
                    elif event.key == pygame.K_j:
                        self.move_result = self.level.players[1].try_move(constants.LEFT)
                    elif event.key == pygame.K_k:
                        self.move_result = self.level.players[1].try_move(constants.DOWN)
                    elif event.key == pygame.K_l:
                        self.move_result = self.level.players[1].try_move(constants.RIGHT)
                    if self.move_result:
                        self.original_positions = [(i.x, i.y) for i, d in self.move_result]
                        self.transitioning = True
                        self.animation_progress = 0
                    if event.key == pygame.K_z or event.key == pygame.K_u:
                        self.level.undo()

        if self.level.complete:
            self.game.cur_level += 1
            self.game.push_state(EndState())

    def draw(self, screen):
        screen.fill(Color(100, 80, 100))

        scale = constants.SCREEN_WIDTH // (2 * self.level.dim[0] + 6)
        left, right = self.level.render(scale)

        yoff = constants.SCREEN_HEIGHT / 2 - (self.level.dim[1] + 4) * scale / 2

        screen.blit(left, (2 * scale, yoff + 2 * scale))
        screen.blit(right, ((4 + self.level.dim[0]) * scale, yoff + 2 * scale))

        #print(self.level.players[0].position())
