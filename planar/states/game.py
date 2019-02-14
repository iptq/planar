import pygame
import copy
from pygame import Color
from math import floor, ceil, sin, pi
from collections import defaultdict

import planar.constants as constants
import planar.states as states
from planar.states.end import EndState

class GameState(states.State):
    def __init__(self, level):
        self.original = copy.deepcopy(level)
        self.level = level

        self.transitioning = False
        self.animation_progress = 0
        self.move_success = None
        self.move_result = []
        self.original_positions = []
        self.keymap = defaultdict(bool)

    def update(self, events):
        self.game.clock.tick()
        if self.transitioning:
            dt = self.game.clock.get_time() / 1000 * 6
            if self.move_success:
                if self.animation_progress + dt >= 1:
                    for (block, d), (x, y) in zip(self.move_result, self.original_positions):
                        block.x = x
                        block.y = y
                        self.level.move_block(block, d)
                    self.level.move_stack.append(self.move_result)
                    self.transitioning = 0
                    self.animation_progress = 0
                    self.move_success = None
                    self.move_result = []
                    self.original_positions = []
                else:
                    self.animation_progress += dt
                    for block, d in self.move_result:
                        block.x += dt * d[0]
                        block.y += dt * d[1]
            else:
                if self.animation_progress + dt >= 1:
                    for (block, d), (x, y) in zip(self.move_result, self.original_positions):
                        block.x = x
                        block.y = y
                    self.transitioning = 0
                    self.animation_progress = 0
                    self.move_success = None
                    self.move_result = []
                    self.original_positions = []
                else:
                    self.animation_progress += dt
                    delta = sin(4 * pi * self.animation_progress) / (10 * self.animation_progress + 0.5) / 4
                    for (block, d), (x, y) in zip(self.move_result, self.original_positions):
                        if block.movable:
                            block.x = x + delta * d[0]
                            block.y = y + delta * d[1]
        else:
            if self.keymap[pygame.K_r]:
                self.level = copy.deepcopy(self.original)
            elif self.keymap[pygame.K_w]:
                self.move_success, self.move_result = self.level.players[0].try_move(constants.UP)
            elif self.keymap[pygame.K_a]:
                self.move_success, self.move_result = self.level.players[0].try_move(constants.LEFT)
            elif self.keymap[pygame.K_s]:
                self.move_success, self.move_result = self.level.players[0].try_move(constants.DOWN)
            elif self.keymap[pygame.K_d]:
                self.move_success, self.move_result = self.level.players[0].try_move(constants.RIGHT)
            elif self.keymap[pygame.K_i]:
                self.move_success, self.move_result = self.level.players[1].try_move(constants.UP)
            elif self.keymap[pygame.K_j]:
                self.move_success, self.move_result = self.level.players[1].try_move(constants.LEFT)
            elif self.keymap[pygame.K_k]:
                self.move_success, self.move_result = self.level.players[1].try_move(constants.DOWN)
            elif self.keymap[pygame.K_l]:
                self.move_success, self.move_result = self.level.players[1].try_move(constants.RIGHT)
            if self.move_success is not None:
                self.original_positions = [(i.x, i.y) for i, d in self.move_result]
                self.transitioning = True
                self.animation_progress = 0
                #print(self.move_result)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.pop_state()
                self.keymap[event.key] = True
                if not self.transitioning and (event.key == pygame.K_z or event.key == pygame.K_u):
                    self.level.undo()

            if event.type == pygame.KEYUP:
                self.keymap[event.key] = False

        if self.level.complete:
            self.game.cur_level += 1
            self.game.push_state(EndState())

    def draw(self, screen):
        screen.fill(Color(100, 80, 100))

        ratio = (2 * self.level.dim[0] + 6) / (self.level.dim[1] + 4)
        screen_ratio = constants.SCREEN_WIDTH / constants.SCREEN_HEIGHT
        if ratio > screen_ratio:
            scale = constants.SCREEN_WIDTH // (2 * self.level.dim[0] + 6)
            xoff = 0
            yoff = constants.SCREEN_HEIGHT / 2 - (self.level.dim[1] + 4) * scale / 2
        else:
            scale = constants.SCREEN_HEIGHT // (self.level.dim[1] + 4)
            xoff = constants.SCREEN_WIDTH / 2 - (2 * self.level.dim[0] + 6) * scale / 2
            yoff = 0

        left, right = self.level.render(scale)

        screen.blit(left, (xoff + 2 * scale, yoff + 2 * scale))
        screen.blit(right, (xoff + (4 + self.level.dim[0]) * scale, yoff + 2 * scale))
