#!/usr/bin/env python3

from pygame.locals import *
import pygame
import sys

from planar import Game
import planar.constants as constants
from planar.states.game import GameState
from planar.player import Player
from planar.level import Level, Block, Segment

if __name__ == "__main__":
    pygame.init()

    block = Block((3, 3), True, constants.DIRECTION_VERTICAL, [255, 10, 100])
    block.add_segment(Segment(0, 0, 0, 1))
    block.add_segment(Segment(0, 1, 0, 0))
    block2 = Block((3, 3), True, constants.DIRECTION_VERTICAL, [10, 255, 100])
    block2.add_segment(Segment(0, 0, 0, 3))
    level = Level((8, 8), [block, block2])
    level.add_player(Player(5, 5, 0, [66, 134, 244]))
    level.add_player(Player(5, 5, 1, [244, 83, 65]))

    menu_state = GameState(level)
    game = Game()
    game.push_state(menu_state)

    game.run()
