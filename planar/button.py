import pygame

class Button:
    def __init__(self, x, y, w, h, text, callback, color=[255,0,0], val=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.txt_surface = self.font.render(text, True, self.color)
        self.callback = callback
        self.val = val

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.val != None:
                    self.callback(self.val)
                else:
                    self.callback()

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
