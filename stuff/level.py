class Cell(object):
	def __init__(self, x, y, t):
		self.x = x
		self.y = y
		self.t = t

class Block(object):
	def __init__(self, cells, movable, direction):
		self.cells = cells
		self.movable = movable
		self.direction = direction

class Level(object):
	def __init__(self, objects):
		pass