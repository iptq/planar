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

def test2():
    block = Block((3, 3), [
        Segment(0, 0, 0, 1),
        Segment(0, 1, 0, 3),
    ], True, constants.DIRECTION_VERTICAL, [255, 10, 100])
    block2 = Block((3, 3), [
        Segment(0, 0, 0, 3),
        Segment(1, 0, 0, 0),
        Segment(1, 0, 1, 0),
    ], True, constants.DIRECTION_HORIZONTAL, [10, 255, 100])
    return Level((8, 8), [block, block2], [
        Player(5, 5, 0, [66, 134, 244]),
        Player(5, 5, 1, [244, 83, 65]),
    ])

def test3():
    return Level((8, 8), [
    Block([6,5],[
        Segment(0, -1, 0, 2),
        Segment(0, 0, 0, 0),
    ], True, constants.DIRECTION_VERTICAL, [255, 10, 100]),
    Block([6,3],[
        Segment(0, 0, 1, 4),
        Segment(-1, 0, 1, 0),
        Segment(0, 0, 0, 4),
        Segment(-1, 0, 0, 0),
        Segment(-2,0,0,2),
        Segment(-2,0,1,2)
    ], True, constants.DIRECTION_HORIZONTAL, [0, 255, 100]),
    Block([6,2],[
        Segment(0, 0, 1, 4),
        Segment(0, -1, 1, 0),
        Segment(0, 0, 0, 4),
        Segment(0, -1, 0, 0)
    ], True, constants.DIRECTION_VERTICAL, [20, 25, 100]),
    Block([7,4],[
        Segment(0,0,0,0),
        Segment(0,0,1,0),
        Segment(0,1,0,0),
        Segment(0,1,1,0),
        Segment(0,2,0,0),
        Segment(0,2,1,0),
        Segment(0,3,0,0),
        Segment(0,3,1,0)
    ], False, 0 , [0,0,0]),
    Block([3,5],[
        Segment(0,0,0,4),
        Segment(0,0,1,4),
        Segment(-1,0,0,0),
        Segment(-1,0,1,0),
        Segment(-2,0,0,0),
        Segment(-2,0,1,0)
    ], True, constants.DIRECTION_HORIZONTAL, [110,30,230]),
    Block([2,0],[
        Segment(0,0,0,0),
        Segment(0,0,1,0),
        Segment(0,1,0,0),
        Segment(0,1,1,0),
        Segment(0,2,0,0),
        Segment(0,2,1,0),
        Segment(0,3,0,0),
        Segment(0,3,1,0)
    ], False, 0 , [0,0,0]),
    Block([3,5],[
        Segment(0,0,0,2),
        Segment(0,1,0,0),
    ], True, constants.DIRECTION_VERTICAL, [240,50,60]),
    Block([3,3],[
        Segment(0,0,1,4),
        Segment(0,-1,1,0)
    ], True, constants.DIRECTION_VERTICAL, [120,220,20]),
    Block([4,4],[
        Segment(0,0,0,0),
        Segment(0,0,1,0),
        Segment(0,1,0,0),
        Segment(0,1,1,0),
        Segment(0,2,0,0),
        Segment(0,2,1,0),
        Segment(0,3,0,0),
        Segment(0,3,1,0)
    ], False, 0 , [0,0,0])
], [
    Player(5, 5, 0, [66, 134, 244]),
    Player(5, 5, 1, [244, 83, 65])
], [
    (0,0,0),
    (0,0,1)
])
