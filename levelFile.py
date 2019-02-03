#Proof of concept level
lvl = level.Level((8, 8), [
    level.Block([6,5],[
        level.Segment(0, -1, 0, 2),
        level.Segment(0, 0, 0, 0),
    ], True, constants.DIRECTION_VERTICAL, [255, 10, 100]),
    level.Block([6,3],[
        level.Segment(0, 0, 1, 4),
        level.Segment(-1, 0, 1, 0),
        level.Segment(0, 0, 0, 4),
        level.Segment(-1, 0, 0, 0),
        level.Segment(-2,0,0,2),
        level.Segment(-2,0,1,2)
    ], True, constants.DIRECTION_HORIZONTAL, 0, [0, 255, 100]),
    level.Block([6,2],[
        level.Segment(0, 0, 1, 4),
        level.Segment(0, -1, 1, 0),
        level.Segment(0, 0, 0, 4),
        level.Segment(0, -1, 0, 0)
    ], True, constants.DIRECTION_VERTICAL, 0, [20, 25, 100]),
    level.Block([7,4],[
        level.Segment(0,0,0,0),
        level.Segment(0,0,1,0),
        level.Segment(0,1,0,0),
        level.Segment(0,1,1,0),
        level.Segment(0,2,0,0),
        level.Segment(0,2,1,0),
        level.Segment(0,3,0,0),
        level.Segment(0,3,1,0)
    ], False, 0 , [0,0,0]),
    level.Block([3,5],[
        level.Segment(0,0,0,4),
        level.Segment(0,0,1,4),
        level.Segment(-1,0,0,0),
        level.Segment(-1,0,1,0),
        level.Segment(-2,0,0,0),
        level.Segment(-2,0,1,0)
    ], False, 0 , [110,30,230]),
    level.Block([2,0],[
        level.Segment(0,0,0,0),
        level.Segment(0,0,1,0),
        level.Segment(0,1,0,0),
        level.Segment(0,1,1,0),
        level.Segment(0,2,0,0),
        level.Segment(0,2,1,0),
        level.Segment(0,3,0,0),
        level.Segment(0,3,1,0)
    ], False, 0 , [0,0,0]),
    level.Block([3,5],[
        level.Segment(0,0,0,2),
        level.Segment(0,1,0,0),
    ], False, 0 , [240,50,60]),
    level.Block([3,3],[
        level.Segment(0,0,1,4)
    ], True, constants.DIRECTION_VERTICAL, 0 , [120,220,20]),
    level.Block([4,4],[
        level.Segment(0,0,0,0),
        level.Segment(0,0,1,0),
        level.Segment(0,1,0,0),
        level.Segment(0,1,1,0),
        level.Segment(0,2,0,0),
        level.Segment(0,2,1,0),
        level.Segment(0,3,0,0),
        level.Segment(0,3,1,0)
    ], False, 0 , [0,0,0])
], [
    player.Player(5, 5, 0, [66, 134, 244]),
    player.Player(5, 5, 1, [244, 83, 65])
])

#Tutorial Level 1
lvl = level.Level((3,8),[
    level.Block([1,4],[
        level.Segment(0,0,0,0),
        level.Segment(1,0,0,4)
    ], True, constants.DIRECTION_HORIZONTAL, [255, 10, 100]),
    level.Block([2,5],[
        level.Segment(0,0,0,2),
        level.Segment(0,1,0,0)
    ], True, constants.DIRECTION_VERTICAL, [105, 210, 50]),
    level.Block([0,4],[
        level.Segment(0,0,1,1),
        level.Segment(0,1,1,0)
    ], True, constants.DIRECTION_VERTICAL, [35, 150, 100]),
    level.Block([0,3],[
        level.Segment(0,0,0,0)
    ], False, constants, [0, 0, 0]),
    level.Block([2,2],[
        level.Segment(0,0,1,0)
    ], False, constants, [0, 0, 0]),
    level.Block([0,3],[
        level.Segment(0,0,1,3),
        level.Segment(1,0,1,0)
    ], True, constants.DIRECTION_HORIZONTAL, [25, 120, 10]),
], [
    player.Player(1, 7, 0, [66, 134, 244]),
    player.Player(1, 7, 1, [244, 83, 65])
])