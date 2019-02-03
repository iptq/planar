class State(object):
    @property
    def transparent(self):
        return False

    def draw(self, _screen):
        raise NotImplementedError(f"draw() not implemented for {self.__class__}")
