from stuff.level import Block, Cell
import collision

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

cell1 = Cell(0,0,0,0)
cell2 = Cell(1,0,0,0)

block1 = Block([cell1], True, "h")
block2 = Block([cell2], True, "h")

grid = {
  (0,0,0): [[cell1, (block1, 0)]],
  (1,0,0): [[cell2, (block2, 0)]]
}

print(collision.can_move(grid, (0,0,0), RIGHT, 0, block1))
