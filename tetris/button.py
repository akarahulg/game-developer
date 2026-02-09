import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, action, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action
        self.hover_color = (min(color[0] + 30, 255), min(color[1] + 30, 255), min(color[2] + 30, 255))
        self.font = pygame.font.SysFont("Arial", font_size)
        self.hovered = False
    
    def update_hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.hovered = True
        else:
            self.hovered = False
        
    def draw(self, surface):
        self.current_color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(surface, self.current_color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.action()



    
