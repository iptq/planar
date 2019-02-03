import pygame
from pygame import Color

import planar.states as states
import planar.constants as constants
import planar.states.levels

WHITE = Color(255, 255, 255)

class EndState(states.State):
    @property
    def transparent(self):
        return True

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.pop_state()
                elif event.key == pygame.K_p:
                    self.game.push_state(planar.states.levels.LevelSelectState())

    def draw(self, screen):
        # draw background
        pygame.draw.rect(screen, (0, 0, 0, 0.2), (0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), 0)

        # draw text
        text_surface, rect = constants.GAME_FONT.render("congratulations, you have won", WHITE)
        screen.blit(text_surface, (constants.SCREEN_WIDTH / 2 - rect.width / 2, 100))
