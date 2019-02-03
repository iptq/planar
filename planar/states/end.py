import pygame
from pygame import Color

import planar.states as states
import planar.constants as constants
import planar.states.levels
import planar.states.game

WHITE = Color(255, 255, 255)

class EndState(states.State):
    @property
    def transparent(self):
        return True

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.states = self.game.states[:1]
                elif event.key == pygame.K_SPACE:
                    self.game.pop_state()
                    self.game.pop_state()
                    if self.game.cur_level >= len(self.game.levels):
                        self.game.states = self.game.states[:1]
                    else:
                        self.game.push_state(planar.states.game.GameState(self.game.levels[self.game.cur_level]))

    def draw(self, screen):
        # draw background
        bg = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.SRCALPHA)
        bg.fill((0, 0, 0, 225))
        screen.blit(bg, (0, 0))

        # draw text
        text_surface, rect = constants.LARGE_FONT.render("level cleared" if self.game.cur_level < len(self.game.levels) else "all levels cleared", WHITE)
        screen.blit(text_surface, (constants.SCREEN_WIDTH / 2 - rect.width / 2, 100))
        text_surface, rect = constants.MED_FONT.render("space - continue   |   esc - main menu" if self.game.cur_level < len(self.game.levels) else "space - main menu", WHITE)
        screen.blit(text_surface, (constants.SCREEN_WIDTH / 2 - rect.width / 2, 300))
