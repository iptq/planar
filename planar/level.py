import pygame

DIRECTION_HORIZONTAL = 0
DIRECTION_VERTICAL = 1

BLOCK_ALPHA = 200
DEFAULT_TILE_COLOR = [200, 200, 200]

class Player(object):
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.color = color

class Segment(object):
    def __init__(self, x, y, z, t):
        self.x = x
        self.y = y
        self.z = z

        # t is the type of the block
        # 0 = Full block
        #  /\
        # /21\
        # \34/
        #  \/
        self.t = t

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def render(self, cell_size, color, padding = 1):
        tile = pygame.Surface((cell_size, cell_size), pygame.SRCALPHA, 32)
        tile = tile.convert_alpha()
        tile.set_alpha(BLOCK_ALPHA)
        if self.t == 0:
            pygame.draw.rect(tile, color, [padding, padding, cell_size - padding, cell_size - padding], 0)
        elif self.t == 1:
            pygame.draw.polygon(tile, color, [[padding, padding], [padding, cell_size - padding], [cell_size - padding, cell_size - padding]], 0)
        elif self.t == 2:
            pygame.draw.polygon(tile, color, [[padding, cell_size - padding], [cell_size - padding, padding], [cell_size - padding, cell_size - padding]], 0)
        elif self.t == 3:
            pygame.draw.polygon(tile, color, [[padding, padding], [cell_size - padding, padding], [cell_size - padding, cell_size - padding]], 0)
        elif self.t == 4:
            pygame.draw.polygon(tile, color, [[padding, padding], [cell_size - padding, padding], [padding, cell_size - padding]], 0)
        return tile

class Block(object):
    def __init__(self, segments, movable, direction, color):
        self.segments = segments
        self.movable = movable
        self.direction = direction
        self.color = color

class Level(object):
    def __init__(self, dimensions, blocks, players):
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
        self.players = players

    def render(self, cell_size, padding = 1):
        DEFAULT_TILE = pygame.Surface((cell_size, cell_size))
        pygame.draw.rect(DEFAULT_TILE, DEFAULT_TILE_COLOR, [1, 1, cell_size - 1, cell_size - 1], 0)
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
                            layer.blit(segment.render(cell_size, block.color, padding), (x * cell_size, y * cell_size))
                        

        for player in self.players:
            layers[player.z].blit(player.render(cell_size), (player.x, player.y))

        return layers

    
