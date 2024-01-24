import pygame
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Bullet:
    def __init__(self, x, y, x_speed, y_speed, size, color):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.size = size
        self.color = color
        self.rect = pygame.Rect(x, y, size, size)
        self.sprite = pygame.image.load('E:\Probabilitati\Joc\dolar.png').convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (size, size))

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x  # Update rect position
        self.rect.y = self.y

    def draw(self):
        screen.blit(self.sprite, (self.x, self.y))

    def off_screen(self):
        return not (0 <= self.x <= SCREEN_WIDTH and 0 <= self.y <= SCREEN_HEIGHT)
