import planar.constants as constants
from planar.player import Player
from planar.level import Level, Block, Segment

def test1():
    block = Block((3, 3), [
        Segment(0, 0, 0, 1),
        Segment(0, 1, 0, 0),
    ], True, constants.DIRECTION_VERTICAL, [255, 10, 100])
    block2 = Block((3, 3), [
        Segment(0, 0, 0, 3),
        Segment(1, 0, 0, 0),
    ], True, constants.DIRECTION_HORIZONTAL, [10, 255, 100])
    return Level((8, 8), [block, block2], [
        Player(5, 5, 0, [66, 134, 244]),
        Player(5, 5, 1, [244, 83, 65]),
    ])
