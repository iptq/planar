import pygame

import planar.constants as constants

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

    def __str__(self):
        x, y = self.position
        return "Segment[{}] ({}, {}, {})".format(self.t, x, y, self.z)

    def can_move(self, direction):
        sx, sy = self.position

        # get direction of target
        dx, dy = direction
        target = (sx + dx, sy + dy, self.z)

        # is the target even in the map?
        if target[0] < 0 or target[0] >= self.block.level.dim[0] or target[1] < 0 or target[1] >= self.block.level.dim[1]:
            return None

        # check if there's anything at target
        occupants = self.block.level.cellmap.get(target)
        if occupants is None:
            # nothing there, we're good to go!
            return []
        elif len(occupants) == 1:
            (occupant, i) = occupants[0]
            if self == occupant:
                return []
            else:
                print(str(self), str(occupant.segments[i]))
                if self.t == 0:
                    # if this is a rectangle, then we can just push normally
                    res = occupant.can_move(direction)
                    if res is None:
                        return None
                    else:
                        res.append((occupant, direction))
                        return res
                else:
                    # if this is a triangle, first we need to check if the current block has 2 occupants
                    curr_occupants = self.block.level.cellmap.get((sx, sy, self.z))
                    print("curr:", curr_occupants)
        elif len(occupants) == 2:
            ind = [constants.UP, constants.LEFT, constants.DOWN, constants.RIGHT].index(direction)
            closer_shapes = [1, 2, 3, 4, 1][ind:ind+2]
            closer = None
            farther = None
            for (occ, i) in occupants:
                if occ.segments[i].t in closer_shapes:
                    closer = (occ, i)
                else:
                    farther = (occ, i)
            assert closer is not None and farther is not None

            if closer == self.block:
                return []

            print("calling {}.can_move".format(closer[0]))
            # res = closer[0].can_move(direction)
            # print("result:", res)

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
    def __init__(self, pos, segments, movable, direction, color):
        self.x = pos[0]
        self.y = pos[1]
        self.segments = segments
        for segment in self.segments:
            segment.block = self
        self.movable = movable
        self.direction = direction
        self.color = color
        self.level = None

    def add_segment(self, segment):
        segment.block = self
        self.segments.append(segment)

    def __str__(self):
        return "Block [" + ", ".join(map(str, self.segments)) + "]"

    def can_move(self, direction):
        if self.direction == constants.DIRECTION_HORIZONTAL and (direction == constants.UP or direction == constants.DOWN):
            return None
        if self.direction == constants.DIRECTION_VERTICAL and (direction == constants.LEFT or direction == constants.RIGHT):
            return None

        result = []
        for segment in self.segments:
            print("calling {}.can_move".format(segment))
            x = segment.can_move(direction)
            if x is None:
                result = None
                break
            else:
                result.extend(x)

        return result

class Level(object):
    def __init__(self, dimensions, blocks, players):
        # (x, y)
        self.dim = dimensions
        self.cellmap = {}
        for block in blocks:
            block.level = self
            for i, cell in enumerate(block.segments):
                coords = tuple(cell)
                if coords in self.cellmap:
                    # check if valid
                    self.cellmap[coords].append((block, i))
                else:
                    self.cellmap[coords] = [(block, i)]

        self.blocks = blocks
        self.players = players
        for player in self.players:
            player.level = self

    def add_block(self, block):
        block.level = self
        self.blocks.append(block)
        for i, cell in enumerate(block.segments):
            coords = tuple(cell)
            if coords in self.cellmap:
                # check if valid
                self.cellmap[coords].append((block, i))
            else:
                self.cellmap[coords] = [(block, i)]

    def render(self, cell_size, padding = 1):
        DEFAULT_TILE = pygame.Surface((cell_size, cell_size))
        pygame.draw.rect(DEFAULT_TILE, constants.DEFAULT_TILE_COLOR, [1, 1, cell_size - 1, cell_size - 1], 0)
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

    def move_block(self, block, direction):
        for i, segment in enumerate(block.segments):
            location = tuple(segment)
            new_location = (location[0] + direction[0], location[1] + direction[1], location[2])
            if location not in self.cellmap:
                raise Exception('Moving segment that doesn\'t exist?!')
            print(self.cellmap[location])
            self.cellmap[location].remove((block, i))
            if len(self.cellmap[location]) == 0:
                del self.cellmap[location]
            if new_location not in self.cellmap:
                self.cellmap[new_location] = [(block, i)]
            else:
                self.cellmap[new_location].append((block, i))
        block.x += direction[0]
        block.y += direction[1]
