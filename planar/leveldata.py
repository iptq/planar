import planar.constants as constants
from planar.player import Player
from planar.level import Level, Block, Segment

def test1():
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
    block8 = Block((1, 5), [
        Segment(0, 0, 0, 0),
        Segment(1, 0, 0, 0),
        Segment(0, 0, 1, 0),
        Segment(1, 0, 1, 0)
    ], True, constants.DIRECTION_HORIZONTAL, [200, 10, 200])
    block9 = Block((1, 4), [
        Segment(0, 0, 0, 0),
        Segment(1, 0, 0, 0),
        Segment(0, 0, 1, 0),
        Segment(1, 0, 1, 0)
    ], True, constants.DIRECTION_HORIZONTAL, [10, 200, 255])
    immovable = Block((0, 0), [
        Segment(0, 7, 0, 0),
        Segment(1, 7, 0, 0),
        Segment(2, 7, 0, 0),
        Segment(5, 2, 0, 0),
        Segment(6, 2, 0, 0),
        Segment(7, 2, 0, 0)
    ], False, constants.DIRECTION_BOTH, [0, 0, 0])
    return Level((8, 8), [block, block2, block3, block4, block5, block6, block7, block8, block9, immovable], [
        Player(6, 6, 0, [66, 134, 244]),
        Player(6, 6, 1, [244, 83, 65])
    ], [
        (0, 0, 0),
        (0, 0, 1)
    ])

def test3():
    return Level((11,11),[
    Block([0,0],[
        #Segment(2,0,0,0),
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
        #Segment(2,0,1,0),
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

        Segment(-8,0,0,0),
        Segment(-8,0,1,0),
        Segment(-6,-2,0,0),
        Segment(-6,-2,1,0),

        Segment(-6,-6,0,0),
        Segment(-6,-6,1,0),
        Segment(-7,-9,1,0),
        Segment(-7,-9,0,0)
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
        Segment(-4,-2,1,0),
        Segment(-6,4,0,0),
        Segment(-6,4,1,0)
    ], True, constants.DIRECTION_VERTICAL, [25, 160, 10])
], [
    Player(9, 0, 0, [66, 134, 244]),
    Player(10, 9, 1, [244, 83, 65])
], [
    (0,0,0),
    (0,0,1)
])

def test2():
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

#Tutorial Level 1
def testTut():
    return Level((3,7),[
    Block([1,3],[
        Segment(0,0,0,0),
        Segment(1,0,0,4)
    ], True, constants.DIRECTION_HORIZONTAL, [255, 10, 100]),
    Block([2,4],[
        Segment(0,0,0,2),
        Segment(0,1,0,0)
    ], True, constants.DIRECTION_VERTICAL, [105, 210, 50]),
    Block([0,4],[
        Segment(0,0,1,1),
        Segment(0,1,1,0)
    ], True, constants.DIRECTION_VERTICAL, [35, 150, 100]),
    Block([0,2],[
        Segment(0,0,0,0)
    ], False, constants.DIRECTION_BOTH, [0, 0, 0]),
    Block([2,2],[
        Segment(0,0,1,0)
    ], False, constants.DIRECTION_BOTH, [0, 0, 0]),
    Block([0,3],[
        Segment(0,0,1,3),
        Segment(1,0,1,0)
    ], True, constants.DIRECTION_HORIZONTAL, [25, 120, 10]),
], [
    Player(1, 6, 0, [66, 134, 244]),
    Player(1, 6, 1, [244, 83, 65])
], [
    (1,0,0),
    (1,0,1)
])


#Tutorial Level 2
def testTut2():
    return Level((4,8),[
    Block([0,2],[
        Segment(0,0,0,0),
        Segment(3,0,0,0),
        Segment(0,2,0,0),
        Segment(3,2,0,0),
        Segment(0,0,1,0),
        Segment(3,0,1,0),
        Segment(0,2,1,0),
        Segment(3,4,0,0),
        Segment(0,4,1,0),
        Segment(3,4,1,0)
    ], False, constants.DIRECTION_HORIZONTAL, [0, 0, 0]),
    Block((1, 5), [
        Segment(0, 0, 0, 0),
        Segment(1, 0, 0, 4),
        Segment(0, 0, 1, 0),
        Segment(1, 0, 1, 4)
    ], True, constants.DIRECTION_HORIZONTAL, [255, 10, 100]),
     Block((1, 3), [
        Segment(0, 0, 0, 3),
        Segment(1, 0, 0, 0),
        Segment(0, 0, 1, 3),
        Segment(1, 0, 1, 0)
    ], True, constants.DIRECTION_HORIZONTAL, [255, 10, 100])
], [
    Player(1, 7, 0, [66, 134, 244]),
    Player(1, 7, 1, [244, 83, 65])
], [
    (0,0,0),
    (0,0,1)
])

levels = [testTut, testTut2, test1, test2, test3]
