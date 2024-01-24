import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 128, 255)
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, font, font_size=36):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = font
        self.font_size = font_size
        self.current_color = self.color

    def draw(self, win):
        pygame.draw.rect(win, self.current_color, (self.x, self.y, self.width, self.height), border_radius=10)
        text_surf = self.font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        win.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        x, y = pos
        return (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height)
