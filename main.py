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

    game = Game()
    game.push_state(MenuState())
    if len(sys.argv) > 1:
        if sys.argv[1] == "editor":
            game.push_state(EditorState((5, 5)))

    game.run()
