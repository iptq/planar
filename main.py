#!/usr/bin/env python3

from pygame.locals import *
import pygame
import sys

from planar import Game
from planar.states.game import GameState
from planar.states.menu import MenuState
from planar.tests import *
from planar.states.editor import EditorState

if __name__ == "__main__":
    pygame.init()

    start_state = MenuState()
    if len(sys.argv) > 1:
        if sys.argv[1] == "editor":
            start_state = EditorState((5, 5))
    game = Game()
    game.push_state(start_state)

    game.run()
