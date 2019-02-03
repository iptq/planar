DIRECTION_HORIZONTAL = 0
DIRECTION_VERTICAL = 1

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

class Block(object):
    def __init__(self, cells, movable, direction):
        self.cells = cells
        self.movable = movable
        self.direction = direction

class Level(object):
    def __init__(self, blocks):
        self.cellmap = {}
        for block in blocks:
            for cell in block.cells:
                coords = tuple(cell)
                if coords in cellmap:
                    # check if valid
                    cellmap[coords].append(block)
                else:
                    cellmap[coords] = [block]

        self.blocks = blocks
