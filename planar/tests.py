import planar.constants as constants
from planar.player import Player
from planar.level import Level, Block, Segment

def testshit():
    block = Block((4, 4), [
        Segment(0, 0, 0, 1),
        Segment(0, 1, 0, 0),
        Segment(0, 2, 0, 3)
    ], True, constants.DIRECTION_VERTICAL, [255, 10, 100])
    block2 = Block((4, 4), [
        Segment(0, 0, 0, 3),
        Segment(1, 0, 0, 0),
        Segment(1, 0, 1, 0),
        Segment(0, -1, 0, 2),
        Segment(1, -1, 0, 0)
    ], True, constants.DIRECTION_HORIZONTAL, [10, 255, 100])
    block3 = Block((4, 2), [
        Segment(0, 0, 0, 2),
        Segment(0, 1, 0, 4)
    ], True, constants.DIRECTION_VERTICAL, [25, 160, 10])
    block4 = Block((2, 2), [
        Segment(0, 0, 0, 3),
        Segment(1, 0, 0, 0),
        Segment(2, 0, 0, 4)
    ], True, constants.DIRECTION_HORIZONTAL, [200, 100, 10])
    block5 = Block((2, 2), [
        Segment(0, 0, 0, 1),
        Segment(0, 1, 0, 0)
    ], True, constants.DIRECTION_VERTICAL, [10, 10, 200])
    block6 = Block((2, 6), [
        Segment(0, 0, 0, 2),
        Segment(1, 0, 0, 0),
        Segment(2, 0, 0, 1)
    ], True, constants.DIRECTION_HORIZONTAL, [100, 200, 200])
    block7 = Block((2, 5), [
        #Segment(0, 0, 0, 0),
        Segment(0, 1, 0, 4)
    ], True, constants.DIRECTION_VERTICAL, [200, 200, 10])
    immovable = Block((0, 0), [
        Segment(0, 7, 0, 0),
        Segment(1, 7, 0, 0),
        Segment(2, 7, 0, 0),
        Segment(5, 2, 0, 0),
        Segment(6, 2, 0, 0),
        Segment(7, 2, 0, 0)
    ], True, constants.DIRECTION_BOTH, [0, 0, 0])
    return Level((8, 8), [block, block2, block3, block4, block5, block6, block7, immovable], [
        Player(6, 6, 0, [66, 134, 244]),
        Player(6, 6, 1, [244, 83, 65])
    ], [
        (0, 0, 0),
        (0, 0, 1)
    ])

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
    return Level((11,11),[
    Block([0,0],[
        Segment(2,0,0,0),
        Segment(4,0,0,0),
        Segment(6,0,0,0),
        Segment(8,0,0,0),
        Segment(10,0,0,0),
        Segment(0,2,0,0),
        Segment(2,2,0,0),
        Segment(4,2,0,0),
        Segment(6,2,0,0),
        Segment(8,2,0,0),
        Segment(10,2,0,0),
        Segment(0,4,0,0),
        Segment(2,4,0,0),
        Segment(4,4,0,0),
        Segment(6,4,0,0),
        Segment(8,4,0,0),
        Segment(10,4,0,0),
        Segment(0,6,0,0),
        Segment(2,6,0,0),
        Segment(4,6,0,0),
        Segment(6,6,0,0),
        Segment(8,6,0,0),
        Segment(10,6,0,0),
        Segment(0,8,0,0),
        Segment(2,8,0,0),
        Segment(4,8,0,0),
        Segment(6,8,0,0),
        Segment(8,8,0,0),
        Segment(10,8,0,0),
        Segment(0,10,0,0),
        Segment(2,10,0,0),
        Segment(4,10,0,0),
        Segment(6,10,0,0),
        Segment(8,10,0,0),
        Segment(10,10,0,0),
        Segment(2,0,1,0),
        Segment(4,0,1,0),
        Segment(6,0,1,0),
        Segment(8,0,1,0),
        Segment(10,0,1,0),
        Segment(0,2,1,0),
        Segment(2,2,1,0),
        Segment(4,2,1,0),
        Segment(6,2,1,0),
        Segment(8,2,1,0),
        Segment(10,2,1,0),
        Segment(0,4,1,0),
        Segment(2,4,1,0),
        Segment(4,4,1,0),
        Segment(6,4,1,0),
        Segment(8,4,1,0),
        Segment(10,4,1,0),
        Segment(0,6,1,0),
        Segment(2,6,1,0),
        Segment(4,6,1,0),
        Segment(6,6,1,0),
        Segment(8,6,1,0),
        Segment(10,6,1,0),
        Segment(0,8,1,0),
        Segment(2,8,1,0),
        Segment(4,8,1,0),
        Segment(6,8,1,0),
        Segment(8,8,1,0),
        Segment(10,8,1,0),
        Segment(0,10,1,0),
        Segment(2,10,1,0),
        Segment(4,10,1,0),
        Segment(6,10,1,0),
        Segment(8,10,1,0),
        Segment(10,10,1,0),
        Segment(7,7,0,0),
        Segment(7,7,1,0),
        Segment(5,5,0,0),
        Segment(5,5,1,0),
        Segment(3,1,0,0),
        Segment(3,1,1,0),
        Segment(1,5,0,0),
        Segment(1,5,1,0)
    ], False, constants.DIRECTION_HORIZONTAL, [0, 0, 0]),
    Block((9, 9), [
        Segment(0, 0, 0, 0),
        Segment(0, 0, 1, 0),
        Segment(0,-6, 0, 0),
        Segment(0, -6, 1, 0),
        Segment(0, -8, 0, 0),
        Segment(0, -8, 1, 0),
        Segment(-2, -6, 0, 0),
        Segment(-2, -6, 1, 0),
        Segment(-4,-8,0,0),
        Segment(-4,-8,1,0),
        Segment(-8,-6,0,0),
        Segment(-8,-6,1,0),
        Segment(-4,0,0,0),
        Segment(-4,0,1,0),
        Segment(-6,0,0,0),
        Segment(-6,0,1,0),
        Segment(-8,0,0,0),
        Segment(-8,0,1,0),
        Segment(-6,-2,0,0),
        Segment(-6,-2,1,0),

        Segment(-6,-6,0,0),
        Segment(-6,-6,1,0)
    ], True, constants.DIRECTION_HORIZONTAL, [255, 10, 100]),
    Block((9, 5), [
        Segment(0, 0, 0, 0),
        Segment(0, 0, 1, 0),
        Segment(0, 2, 0, 0),
        Segment(0, 2, 1, 0),
        Segment(-2, -4, 0, 0),
        Segment(-2, -4, 1, 0),
        Segment(-2,4,0,0),
        Segment(-2,4,1,0),
        Segment(-2,0,0,0),
        Segment(-2,0,1,0),
        Segment(-4,2,0,0),
        Segment(-4,2,1,0),
        Segment(-6,0,0,0),
        Segment(-6,0,1,0),
        Segment(-8,2,0,0),
        Segment(-8,2,1,0),
        Segment(-8,4,0,0),
        Segment(-8,4,1,0),
        Segment(-4,-2,0,0),
        Segment(-4,-2,1,0)
    ], True, constants.DIRECTION_VERTICAL, [25, 160, 10])
], [
    Player(9, 0, 0, [66, 134, 244]),
    Player(10, 9, 1, [244, 83, 65])
], [
    (0,0,0),
    (0,0,1)
])
