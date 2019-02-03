UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def is_flat_side(type, dir):
    return (type == 1 and (dir == DOWN or dir == LEFT)) \
        or (type == 2 and (dir == DOWN or dir == RIGHT)) \
        or (type == 3 and (dir == UP or dir == RIGHT)) \
        or (type == 4 and (dir == UP or dir == LEFT))

def is_normal(type, other):
    return (type == 1 and other != 3) or (type == 3 and other != 1) \
        or (type == 2 and other != 4) or (type == 4 and other != 2)

def can_move(grid, pos, dir, type, object):
    # object is the object doing the moving, so that a block does not check
    # collisions with itself
    target = (0,0,0)
    if dir == UP:
        target = (pos[0], pos[1]-1, pos[2])
    elif dir == DOWN:
        target = (pos[0], pos[1]+1, pos[2])
    elif dir == LEFT:
        target = (pos[0]-1, pos[1], pos[2])
    elif dir == RIGHT:
        target = (pos[0]+1, pos[1], pos[2])
    else:
        return "ERROR INVALID DIRECTION"

    segments = grid.get(target)
    if segments == None:
        return True

    for segment in segments:
        (x, y, z, t) = segments[0]
        (block, index) = segments[1]

        if object == block:
            #if the target cell is part of the block
            continue

        if not block.moveable:
            return False

        if type == 0 or is_flat_side(type, dir) or is_normal(type, t):
            #full block we are attempting to move
            if dir != block.direction:
                return False
            for cell in block.cells:
                pos = (cell.x, cell.y, cell.z)
                if not can_move(grid, pos, dir, cell.t, block)
                    return False

        elif type == 1:
            #gauranteed to be moving up or right into questionable block
            if dir == UP:
                for cell in block.cells:
                    pos = (cell.x, cell.y, cell.z)
                    if not can_move(grid, pos, RIGHT, cell.t, block):
                        return False
            if dir == RIGHT:
                for cell in block.cells:
                    pos = (cell.x, cell.y, cell.z)
                    if not can_move(grid, pos, UP, cell.t, block):
                        return False
        elif type == 2:
            #gauranteed to be moving up or left questionable block
            if dir == UP:
                for cell in block.cells:
                    pos = (cell.x, cell.y, cell.z)
                    if not can_move(grid, pos, LEFT, cell.t, block):
                        return False
            if dir == LEFT:
                for cell in block.cells:
                    pos = (cell.x, cell.y, cell.z)
                    if not can_move(grid, pos, UP, cell.t, block):
                        return False
        elif type == 3:
            #gauranteed to be moving down or left questionable block
            if dir == DOWN:
                for cell in block.cells:
                    pos = (cell.x, cell.y, cell.z)
                    if not can_move(grid, pos, LEFT, cell.t, block):
                        return False
            if dir == LEFT:
                for cell in block.cells:
                    pos = (cell.x, cell.y, cell.z)
                    if not can_move(grid, pos, DOWN, cell.t, block):
                        return False
        elif type == 4:
            #gauranteed to be moing down or right questionable block
            if dir == DOWN:
                for cell in block.cells:
                    pos = (cell.x, cell.y, cell.z)
                    if not can_move(grid, pos, RIGHT, cell.t, block):
                        return False
            if dir == RIGHT:
                for cell in block.cells:
                    pos = (cell.x, cell.y, cell.z)
                    if not can_move(grid, pos, DOWN, cell.t, block):
                        return False
