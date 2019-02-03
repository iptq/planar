DIRECTION_HORIZONTAL = 0
DIRECTION_VERTICAL = 1
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def is_flat_side(celltype, direction):
    result = (celltype == 1 and (direction == DOWN or direction == LEFT)) \
        or (celltype == 2 and (direction == DOWN or direction == RIGHT)) \
        or (celltype == 3 and (direction == UP or direction == RIGHT)) \
        or (celltype == 4 and (direction == UP or direction == LEFT))
    print("Is flat: ", result)
    return result

def is_normal(celltype, other):
    result = (celltype == 1 and other != 3) or (celltype == 3 and other != 1) \
        or (celltype == 2 and other != 4) or (celltype == 4 and other != 2)
    print("Is normal: ", result)
    return result

def can_move(grid, pos, direction, celltype, object):
    # object is the object doing the moving, so that a block does not check
    # collisions with itself
    target = (0,0,0)
    if direction == UP:
        target = (pos[0], pos[1]-1, pos[2])
    elif direction == DOWN:
        target = (pos[0], pos[1]+1, pos[2])
    elif direction == LEFT:
        target = (pos[0]-1, pos[1], pos[2])
    elif direction == RIGHT:
        target = (pos[0]+1, pos[1], pos[2])
    else:
        return "ERROR INVALID DIRECTION"

    segments = grid.get(target)
    if segments != None:
        for segment in segments:
            cell = segment[0]
            (block, index) = segment[1]

            if object == block:
                #if the target cell is part of the block
                continue

            if celltype == 0 or is_flat_side(celltype, direction) or is_normal(celltype, cell.t):
                if not block.movable:
                    return False
                print("normal")
                #full block we are attempting to move
                if ((direction == LEFT or direction == RIGHT) and block.direction == DIRECTION_VERTICAL) \
                or ((direction == UP or direction == DOWN) and block.direction == DIRECTION_HORIZONTAL):
                    return False
                for cell in block.segments:
                    pos = (cell.x, cell.y, cell.z)
                    if not can_move(grid, pos, direction, cell.t, block):
                        return False

    if celltype == 0:
        # a square segment will never overlap with another
        return True

    #checking for segments that are in the same grid position and can be moved
    segments = grid.get(pos)
    if segments != None:
        for segment in segments:
            cell = segment[0]
            (block, index) = segment[1]
            if block == object:
                continue
            if not block.movable:
                return False
            if celltype == 1:
                #gauranteed to be moving up or right into questionable block
                if direction == UP:
                    for cell in block.segments:
                        pos = (cell.x, cell.y, cell.z)
                        if not can_move(grid, pos, RIGHT, cell.t, block):
                            return False
                if direction == RIGHT:
                    for cell in block.segments:
                        pos = (cell.x, cell.y, cell.z)
                        if not can_move(grid, pos, UP, cell.t, block):
                            return False
            elif celltype == 2:
                #gauranteed to be moving up or left questionable block
                if direction == UP:
                    for cell in block.segments:
                        pos = (cell.x, cell.y, cell.z)
                        if not can_move(grid, pos, LEFT, cell.t, block):
                            return False
                if direction == LEFT:
                    for cell in block.segments:
                        pos = (cell.x, cell.y, cell.z)
                        if not can_move(grid, pos, UP, cell.t, block):
                            return False
            elif celltype == 3:
                #gauranteed to be moving down or left questionable block
                if direction == DOWN:
                    for cell in block.segments:
                        pos = (cell.x, cell.y, cell.z)
                        if not can_move(grid, pos, LEFT, cell.t, block):
                            return False
                if direction == LEFT:
                    for cell in block.segments:
                        pos = (cell.x, cell.y, cell.z)
                        if not can_move(grid, pos, DOWN, cell.t, block):
                            return False
            elif celltype == 4:
                #gauranteed to be moing down or right questionable block
                if direction == DOWN:
                    for cell in block.segments:
                        pos = (cell.x, cell.y, cell.z)
                        if not can_move(grid, pos, RIGHT, cell.t, block):
                            return False
                if direction == RIGHT:
                    for cell in block.segments:
                        pos = (cell.x, cell.y, cell.z)
                        if not can_move(grid, pos, DOWN, cell.t, block):
                            return False
    return True
