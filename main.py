#!/usr/bin/env python3

from pygame.locals import *
import pygame
import sys

from planar import Game
from planar.states.game import GameState
from planar.tests import *

if __name__ == "__main__":
    pygame.init()

    menu_state = GameState(test2())
    game = Game()
    game.push_state(menu_state)

    game.run()
