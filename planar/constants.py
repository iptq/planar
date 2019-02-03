import pygame
import pygame.freetype

GAME_FONT = None

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

DIRECTION_HORIZONTAL = 0
DIRECTION_VERTICAL = 1
DIRECTION_BOTH = 2

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

DEFAULT_TILE_COLOR = [200, 200, 200]

def opposite(direction):
    if direction == UP:
        return DOWN
    if direction == DOWN:
        return UP
    if direction == LEFT:
        return RIGHT
    if direction == RIGHT:
        return LEFT
