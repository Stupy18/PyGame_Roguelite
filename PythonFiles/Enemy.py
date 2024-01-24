import math

import pygame
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Enemy:
    def __init__(self, x, y, size, speed, color):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color
        self.health = 3  # Enemy health
        self.sprite = pygame.image.load('E:\Probabilitati\Joc\linii.jpg').convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (70, 90))

    def draw(self):
        screen.blit(self.sprite, (self.x, self.y))

    def move_towards_player(self, player):
        dx, dy = player.x - self.x, player.y - self.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist  # Normalize
        self.x += dx * self.speed
        self.y += dy * self.speed

    def get_hitbox(self):
        return pygame.Rect(self.x, self.y, self.size * 2, self.size * 2)

    def hit(self):
        self.health -= 1
        return self.health <= 0

