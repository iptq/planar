import json
import pygame

from planar.states.game import GameState
from planar import Game
import planar.tests
import planar.serial

if __name__ == "__main__":
    level = planar.tests.testshit()
    data = json.dumps(level, cls=planar.serial.GameEncoder, indent=2)

    level2 = json.loads(data, cls=planar.serial.GameDecoder)
    print(level2)

    pygame.init()

    # menu_state = EditorState((5,5))
    menu_state = GameState(level2)
    # menu_state = MenuState()
    game = Game()
    game.push_state(menu_state)

    game.run()
