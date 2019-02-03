class State(object):
    def __init__(self, transparent=False):
        self.transparent = transparent

    def draw(self):
        raise NotImplementedError(f"draw() not implemented for {self.__class__}")
