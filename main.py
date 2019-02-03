#!/usr/bin/env python3

from pygame.locals import *
import pygame
import sys

from game import Game

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
