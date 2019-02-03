from level import Block, Segment
import collision

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

cell1 = Segment(1,0,0,4)
cell2 = Segment(1,0,0,2)
cell3 = Segment(1,1,0,0)

block1 = Block([cell1], True, "h", "red")
block2 = Block([cell2], True, "v", "red")
block3 = Block([cell3], True, "v", "red")

grid = {
  (1,0,0): [[cell1, (block1, 0)]],
  (1,0,0): [[cell2, (block2, 0)]],
  (1,1,0): [[cell3, (block3, 0)]]
}

print(collision.can_move(grid, (1,0,0), RIGHT, 4, block1))
