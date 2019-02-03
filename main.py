#!/usr/bin/env python3

from pygame.locals import *
import pygame
import sys

from planar import Game
from planar.states.game import GameState
from planar.states.menu import MenuState
from planar.tests import *
from planar.states.editor import EditorState, load

if __name__ == "__main__":
    pygame.init()

    menu_state = GameState(load("Filename.txt"))
    game = Game()
    game.push_state(menu_state)

    game.run()
