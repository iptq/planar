import pygame
import time
from math import sin

from collections import deque
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

    def __repr__(self):
        return str(self)

    def segment_can_move(self, direction, by_player=False, depth=0, ignore=None):
        opposites = { 1: 3, 3: 1, 2: 4, 4: 2 }

        sx, sy = self.position
        curr = (sx, sy, self.z)

        # get direction of target
        dx, dy = direction
        target = (sx + dx, sy + dy, self.z)

        # is the target even in the map?
        if target[0] < 0 or target[0] >= self.block.level.dim[0] or target[1] < 0 or target[1] >= self.block.level.dim[1]:
            return None

        # if this block is immovable, return no
        if not self.block.movable:
            return None

        # if this block is a player, return no
        import planar.player as player
        if isinstance(self.block, player.Player) and not by_player:
            return None

        # first check if this is a triangle and if there's another triangle in this cell
        curr_occupants = self.block.level.cellmap.get(curr)
        if self.t != 0 and len(curr_occupants) == 2:
            other = None
            for (block, i) in curr_occupants:
                if self.block != block:
                    other = (block, i)
                    break
            assert other is not None

            # check if we're actually pushing in that direction
            all_directions = set([constants.LEFT, constants.DOWN, constants.RIGHT, constants.UP])
            directions = [0, constants.LEFT, constants.DOWN, constants.RIGHT, constants.UP, constants.LEFT]
            movements = {
                constants.DIRECTION_VERTICAL: set([constants.UP, constants.DOWN]),
                constants.DIRECTION_HORIZONTAL: set([constants.LEFT, constants.RIGHT]),
            }

            opposite = opposites[self.t]
            pushing_directions = set(directions[opposite:opposite + 2])
            # valid = all_directions - pushing_directions

            if direction in pushing_directions:
                intersection = pushing_directions.intersection(movements[other[0].direction])
                assert len(intersection) == 1
                new_direction = list(intersection)[0]

                res = other[0].block_can_move(new_direction, depth=depth+1, ignore=ignore)
                if res is None:
                    return None
                else:
                    res.update({other[0]: new_direction})
                    return res

        # check if there's anything at target
        occupants = self.block.level.cellmap.get(target)
        if occupants is None:
            # nothing there, we're good to go!
            return {}
        elif len(occupants) == 1:
            (occupant, i) = occupants[0]
            if occupant == ignore:
                return {}
            if self.block == occupant:
                return {}
            else:
                if self.t == 0:
                    # if this is a rectangle, then we can just push normally
                    res = occupant.block_can_move(direction, depth=depth+1, ignore=ignore)
                    if res is None:
                        return None
                    else:
                        res.update({occupant: direction})
                        return res
                else:
                    # check if the thing we're pushing into is a perfectly opposite triangle
                    seg = occupant.segments[i]
                    if seg.t == opposites[self.t]:
                        return {}
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

            if closer[0] == self.block:
                return {}

            res = closer[0].segments[closer[1]].segment_can_move(direction, depth=depth+1)
            if res is None:
                return None
            else:
                res.update({closer[0]: direction})
                return res

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
        self.min_x = min(s.rx for s in segments)
        self.max_x = max(s.rx for s in segments)
        self.min_y = min(s.ry for s in segments)
        self.max_y = max(s.ry for s in segments)
        self.movable = movable
        self.direction = direction
        self.color = color
        self.level = None
        self.is_player = False

    def add_segment(self, segment):
        segment.block = self
        for seg in self.segments:
            (seg.rx, seg.ry) = seg.position
        self.segments.append(segment)
        self.min_x = min(s.rx for s in self.segments) - self.x
        self.max_x = max(s.rx for s in self.segments) - self.x
        self.min_y = min(s.ry for s in self.segments) - self.y
        self.max_y = max(s.ry for s in self.segments) - self.y
        for seg in self.segments:
            seg.rx -= self.x
            seg.ry -= self.y

    def __str__(self):
        return "Block [" + ", ".join(map(str, self.segments)) + "]"

    def __repr__(self):
        return str(self)

    def block_can_move(self, direction, by_player=False, depth=0, ignore=None):
        if self.direction == constants.DIRECTION_HORIZONTAL and (direction == constants.UP or direction == constants.DOWN):
            return None
        if self.direction == constants.DIRECTION_VERTICAL and (direction == constants.LEFT or direction == constants.RIGHT):
            return None

        result = {}
        failed = False
        for segment in self.segments:
            res = segment.segment_can_move(direction, by_player=by_player, depth=depth+1, ignore=ignore)
            if res is None:
                failed = True
            else:
                result.update(res)

        if failed: return None
        result.update({self: direction})
        return result

    def render(self, cell_size, padding=1):
        layers = (pygame.Surface(((self.max_x - self.min_x + 1) * cell_size, (self.max_y - self.min_y + 1) * cell_size), pygame.SRCALPHA, 32),
            pygame.Surface(((self.max_x - self.min_x + 1) * cell_size, (self.max_y - self.min_y + 1) * cell_size), pygame.SRCALPHA, 32))
        for segment in self.segments:
            x = segment.rx - self.min_x
            y = segment.ry - self.min_y
            layer = layers[segment.z]
            layer.blit(segment.render(cell_size - 1, self.color, padding), (x * cell_size + 1, y * cell_size + 1))
        for layer in layers:
            pixels = pygame.surfarray.pixels3d(layer)
            stripe_dist = 10
            if self.movable:
                if self.direction == constants.DIRECTION_VERTICAL:
                    for x in range(0, len(pixels), stripe_dist):
                        for y in range(len(pixels[0])):
                            for i in range(3):
                                pixels[x][y][i] = 255
                elif self.direction == constants.DIRECTION_HORIZONTAL:
                    for y in range(0, len(pixels[0]), stripe_dist):
                        for x in range(len(pixels)):
                            for i in range(3):
                                pixels[x][y][i] = 255

        offset = ((self.x + self.min_x) * cell_size, (self.y + self.min_y) * cell_size)
        return ((layers[0], offset), (layers[1], offset))

class Level(object):
    def __init__(self, dimensions, blocks, players, goals):
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
            coords = player.position()
            if coords in self.cellmap:
                self.cellmap[coords].append((player, 0))
            else:
                self.cellmap[coords] = [(player, 0)]
        self.move_stack = deque()
        self.goals = goals

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

    @property
    def complete(self):
        for goal in self.goals:
            for player in self.players:
                if player.position() == goal:
                    break
            else:
                return False
        return True

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

        for block in self.blocks:
            renders = block.render(cell_size, padding)
            layers[0].blit(*renders[0])
            layers[1].blit(*renders[1])

        for goal in self.goals:
            for radius in reversed(range(cell_size // 5 * 2)):
                tile = pygame.Surface((cell_size, cell_size), pygame.SRCALPHA, 32)
                tile = tile.convert_alpha()
                pygame.draw.circle(tile, [round(127 * sin(radius / 8 + time.time() * 2)) + 128] * 3, [cell_size // 2, cell_size // 2], radius, 0)
                layers[goal[2]].blit(tile, (goal[0], goal[1]))

        for player in self.players:
            layers[player.z].blit(player.render(cell_size), (cell_size * player.x, cell_size * player.y))

        return layers

    def move_block(self, block, direction):
        for i, segment in enumerate(block.segments):
            location = tuple(segment)
            new_location = (location[0] + direction[0], location[1] + direction[1], location[2])
            if location not in self.cellmap:
                raise Exception('Moving segment that doesn\'t exist?!')
            self.cellmap[location].remove((block, i))
            if len(self.cellmap[location]) == 0:
                del self.cellmap[location]
            if new_location not in self.cellmap:
                self.cellmap[new_location] = [(block, i)]
            else:
                self.cellmap[new_location].append((block, i))
        block.x += direction[0]
        block.y += direction[1]

    def undo(self):
        if len(self.move_stack) == 0:
            return
        moves = self.move_stack.pop()
        for move in moves:
            object = move[0]
            direction = constants.opposite(move[1])
            if type(object) == Block:
                self.move_block(object, direction)
            else:
                #object is a player
                # object.force_move(direction)
                self.move_block(object, direction)

    def validate(self):
        for x, y, z in self.cellmap:
            l = self.cellmap[(x, y, z)]
            if len(l) == 0:
                raise Exception('empty cellmap entry exists!?')
            elif len(l) == 1:
                continue
            elif len(l) == 2:
                (b1, i1), (b2, i2) = l
                s1 = b1.segments[i1]
                s2 = b2.segments[i2]

                import planar.player as player
                if isinstance(s1, player.Player) or isinstance(s2, player.Player):
                    print('player exists with other segment', s1, s2)
                    return False
                if s1.t == 0 or s2.t == 0:
                    print('full segment exists with other segment', s1, s2)
                    return False
                if abs(s1.t - s2.t) != 2:
                    print('conflicting segments exist', s1.t, s2.t)
                    return False
                continue
            return False
        return True
