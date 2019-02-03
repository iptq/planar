import pygame

class TextBox:

    def __init__(self, x, y, w, h, text, color=[0,0,0]):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.txt_surface = self.font.render(text, True, self.color)

    def set_text(self,val):
        self.text = str(val)
        self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(50, self.txt_surface.get_width()+10)
        height = max(20, self.txt_surface.get_height()+5)
        self.rect.w = width
        self.rect.h = height

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
