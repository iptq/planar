DIRECTION_HORIZONTAL = 0
DIRECTION_VERTICAL = 1

class Cell(object):
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

class Block(object):
    def __init__(self, cells, movable, direction):
        self.cells = cells
        self.movable = movable
        self.direction = direction

class Level(object):
    def __init__(self, objects):
        pass
