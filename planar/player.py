import pygame

import planar.level
import planar.constants as constants

class Player(planar.level.Block):
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.level = None

    def render(self, cell_size):
        tile = pygame.Surface((cell_size, cell_size), pygame.SRCALPHA, 32)
        tile = tile.convert_alpha()
        pygame.draw.circle(tile, self.color, [cell_size // 2, cell_size // 2], cell_size // 5 * 2, 0)
        return tile

    def try_move(self, direction):
        res = self.can_move(direction)
        if res is None:
            return

        # TODO: move all the other blocks
        for block, dir in res:
            dx, dy = dir
            block.x += dx
            block.y += dy

        dx, dy = direction
        self.x += dx
        self.y += dy
