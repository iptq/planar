#!/usr/bin/env python3

from pygame.locals import *
import pygame
import sys

from planar import Game
from planar.states.menu import MenuState

if __name__ == "__main__":
    pygame.init()
    game = Game(MenuState())
    game.run()
