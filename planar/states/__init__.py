class State(object):
    def __init__(self, game=None):
        self.game = game

    @property
    def transparent(self):
        return False

    def update(self, events):
        raise NotImplementedError(f"update() not implemented for {self.__class__}")

    def draw(self, _screen):
        raise NotImplementedError(f"draw() not implemented for {self.__class__}")
