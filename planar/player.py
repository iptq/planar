import pygame

import planar.level as level
import planar.constants as constants

class Player(level.Block):
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.color = color
        self.level = None

        self.movable = True
        self.direction = constants.DIRECTION_BOTH
        self.is_player = True

        seg = level.Segment(0, 0, z, 0)
        seg.block = self
        self.segments = [seg]

    @property
    def z(self):
        return self.segments[0].z

    @z.setter
    def z(self, value):
        self.segments[0].z = value

    def position(self):
        return (self.x, self.y, self.z)

    def render(self, cell_size):
        tile = pygame.Surface((cell_size, cell_size), pygame.SRCALPHA, 32)
        tile = tile.convert_alpha()
        pygame.draw.circle(tile, self.color, [cell_size // 2, cell_size // 2], cell_size // 5 * 2, 0)
        return tile

    def try_move(self, direction):
        res = self.block_can_move(direction, by_player=True, ignore=self)
        if res is None:
            return None

        moves = [] #used for undo feature

        for block, d in res.items():
            self.level.move_block(block, d)
            moves.append( (block, d) )

        # moves.append( (self, direction) )
        # self.level.move_block(self, direction)
        # self.force_move(direction)
        self.level.move_stack.append(moves)

        movements = {
            constants.DIRECTION_VERTICAL: set([constants.UP, constants.DOWN]),
            constants.DIRECTION_HORIZONTAL: set([constants.LEFT, constants.RIGHT]),
        }
        for block, d in moves:
            if block.direction in movements and d not in movements[block.direction]:
                self.level.undo()
                return None
        else:
            if not self.level.validate():
                self.level.undo()
                return None
        self.level.undo()
        return moves
