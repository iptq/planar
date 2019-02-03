import pygame

import planar.constants

class Segment(object):
    def __init__(self, x, y, z, t):
        self.rx = x
        self.ry = y
        self.z = z

        # t is the type of the block
        # 0 = Full block
        #  /\
        # /21\
        # \34/
        #  \/
        self.t = t
        self.block = None

    def __iter__(self):
        x, y = self.position
        yield x
        yield y
        yield self.z

    @property
    def position(self):
        return (self.block.x + self.rx, self.block.y + self.ry)

    def render(self, cell_size, color, padding = 1):
        tile = pygame.Surface((cell_size, cell_size), pygame.SRCALPHA, 32)
        tile = tile.convert_alpha()
        a = padding
        b = cell_size - a - 1
        if self.t == 0:
            pygame.draw.rect(tile, color, [a, a, b - a + 1, b - a + 1], 0)
        elif self.t == 1:
            pygame.draw.polygon(tile, color, [[a, a], [a, b], [b, b]], 0)
        elif self.t == 2:
            pygame.draw.polygon(tile, color, [[a, b], [b, a], [b, b]], 0)
        elif self.t == 3:
            pygame.draw.polygon(tile, color, [[a, a], [b, a], [b, b]], 0)
        elif self.t == 4:
            pygame.draw.polygon(tile, color, [[a, a], [b, a], [a, b]], 0)
        return tile

class Block(object):
    def __init__(self, pos, movable, direction, color):
        self.x = pos[0]
        self.y = pos[1]
        self.segments = []
        self.movable = movable
        self.direction = direction
        self.color = color

    def add_segment(self, segment):
        segment.block = self
        self.segments.append(segment)

    def can_move(self, direction):
        # get direction of target
        dx, dy = direction
        target = (self.x + dx, self.y + dy, self.z)

        # is the target even in the map?
        if target[0] < 0 or target[0] >= self.level.dim[0] or target[1] < 0 or target[1] >= self.level.dim[1]:
            return None

        # check if there's anything at target
        occupants = self.level.cellmap.get(target)
        if occupants is None:
            # nothing there, we're good to go!
            return []

        return None

class Level(object):
    def __init__(self, dimensions, blocks):
        # (x, y)
        self.dim = dimensions
        self.cellmap = {}
        for block in blocks:
            for i, cell in enumerate(block.segments):
                coords = tuple(cell)
                if coords in self.cellmap:
                    # check if valid
                    self.cellmap[coords].append((block, i))
                else:
                    self.cellmap[coords] = [(block, i)]

        self.blocks = blocks
        self.players = []

    def add_player(self, player):
        player.level = self
        self.players.append(player)

    def render(self, cell_size, padding = 1):
        DEFAULT_TILE = pygame.Surface((cell_size, cell_size))
        pygame.draw.rect(DEFAULT_TILE, planar.constants.DEFAULT_TILE_COLOR, [1, 1, cell_size - 1, cell_size - 1], 0)
        layers = (pygame.Surface(tuple(cell_size * i + 1 for i in self.dim)),
                pygame.Surface(tuple(cell_size * i + 1 for i in self.dim)))
        for z in range(2):
            layer = layers[z]
            for x in range(self.dim[0]):
                for y in range(self.dim[1]):
                    layer.blit(DEFAULT_TILE, (x * cell_size, y * cell_size))
                    if (x, y, z) in self.cellmap:
                        for block, i in self.cellmap[(x, y, z)]:
                            segment = block.segments[i]
                            layer.blit(segment.render(cell_size - 1, block.color, padding), (x * cell_size + 1, y * cell_size + 1))


        for player in self.players:
            layers[player.z].blit(player.render(cell_size), (cell_size * player.x, cell_size * player.y))

        return layers
