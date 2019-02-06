import pygame

class Button:
    def __init__(self, x, y, w, h, text, callback, color=[0,0,0], val=None, right=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.opposite = [255-color[0], 255-color[1], 255-color[2]]
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.txt_surface = self.font.render(text, True, self.opposite)
        self.callback = callback
        self.val = val
        self.right = right

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if event.button == 1:
                    #left click
                    if self.val != None:
                        self.callback(self.val)
                    else:
                        self.callback()
                if event.button == 3:
                    #right click
                    if self.val != None:
                        self.right(self.val)
                    else:
                        self.right()

    def update(self):
        # Resize the box if the text is too long.
        width = max(50, self.txt_surface.get_width()+10)
        height = max(20, self.txt_surface.get_height()+5)
        self.rect.w = width
        self.rect.h = height

    def draw(self, screen):
        # Blit the text.
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
