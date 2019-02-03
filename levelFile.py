#Proof of concept level
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
])
#Tutorial Level 1
def testTut():
    return Level((3,8),[
    Block([1,4],[
        Segment(0,0,0,0),
        Segment(1,0,0,4)
    ], True, constants.DIRECTION_HORIZONTAL, [255, 10, 100]),
    Block([2,5],[
        Segment(0,0,0,2),
        Segment(0,1,0,0)
    ], True, constants.DIRECTION_VERTICAL, [105, 210, 50]),
    Block([0,4],[
        Segment(0,0,1,1),
        Segment(0,1,1,0)
    ], True, constants.DIRECTION_VERTICAL, [35, 150, 100]),
    Block([0,3],[
        Segment(0,0,0,0)
    ], False, constants, [0, 0, 0]),
    Block([2,2],[
        Segment(0,0,1,0)
    ], False, constants, [0, 0, 0]),
    Block([0,3],[
        Segment(0,0,1,3),
        Segment(1,0,1,0)
    ], True, constants.DIRECTION_HORIZONTAL, [25, 120, 10]),
], [
    Player(1, 7, 0, [66, 134, 244]),
    Player(1, 7, 1, [244, 83, 65])
])

#Tutorial Level 2
def testTut2():
    return Level
