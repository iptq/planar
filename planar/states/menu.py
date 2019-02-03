import pygame
from pygame import Color

import planar.states
import planar.constants as constants

COLOR1 = Color(32, 32, 32)
COLOR2 = Color(36, 36, 36)
WHITE = Color(255, 255, 255)

class MenuState(planar.states.State):
    def __init__(self):
        pass

    def draw(self, screen):
        # draw background
        width = constants.SCREEN_WIDTH // 30
        for i in range(0, constants.SCREEN_WIDTH, width):
            color = [COLOR1, COLOR2][i % 2]
            pygame.draw.rect(screen, color, (i, 0, width, constants.SCREEN_HEIGHT), 0)

        # draw text
        text_surface, rect = constants.GAME_FONT.render("planar", WHITE)
        screen.blit(text_surface, (constants.SCREEN_WIDTH / 2 - rect.width / 2, 100))
