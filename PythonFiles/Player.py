SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 128, 255)
from PythonFiles.LevelUpScreen import LevelUpScreen
from PythonFiles.Button import Button
import pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
class Player:
    def __init__(self, x, y, size, speed, color):
        self.x = x
        self.y = y
        self.size = size
        self.exp = 0
        self.speed = speed
        self.color = color
        self.health = 3  # Player health
        self.max_health = 3
        self.level = 1
        self.kills = 0  # Number of enemy kills
        self.sprite = pygame.image.load("E:\Probabilitati\Joc\stupy.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (70, 90))
        self.enemy_respawn_rate = 1
        self.bullet_speed_multiplier = 0.8
        self.bullet_damage = 1
        self.double_bullets = True
        self.required_exp = 100

    def draw(self):
        screen.blit(self.sprite, (self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def get_hitbox(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw_health_bar(self):
        for i in range(self.max_health):
            if i < self.health:
                pygame.draw.rect(screen, RED, (10 + i * 30, 10, 20, 20))
            else:
                pygame.draw.rect(screen, WHITE, (10 + i * 30, 10, 20, 20), 2)

    def draw_exp_bar(self):
        self.required_exp = 100 * self.level  # Adjust as needed for game balance
        exp_ratio = self.exp / self.required_exp
        pygame.draw.rect(screen, GREEN, (555, SCREEN_HEIGHT - 30, 200 * exp_ratio, 20))
        font = pygame.font.SysFont(None, 24)
        exp_text = font.render(f'Level: {self.level}', True, WHITE)
        screen.blit(exp_text, (640, SCREEN_HEIGHT - 50))

    def gain_exp(self, amount):
        self.exp += amount
        self.required_exp = 100 * self.level  # Adjust as needed for game balance
        if self.exp >= self.required_exp:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.kills = 0
        self.exp = 0
        self.enemy_respawn_rate += 0.5

        level_up_screen = LevelUpScreen("../images/imagebackground.png")
        chosen_upgrade = level_up_screen.show(screen)

        if chosen_upgrade == 0:
            self.bullet_speed_multiplier += 0.5
        elif chosen_upgrade == 1:
            self.bullet_damage += 1
        elif chosen_upgrade == 2:
            self.double_bullets = True

    def show_upgrade_screen(self):
        buttons = [
            Button(100, SCREEN_HEIGHT // 2 - 100, 200, 50, "Speed", BLUE, RED),
            Button(100, SCREEN_HEIGHT // 2, 200, 50, "Damage", BLUE, RED),
            Button(100, SCREEN_HEIGHT // 2 + 100, 200, 50, "Double Bullets", BLUE, RED)
        ]
        upgrade_screen = True
        while upgrade_screen:
            screen.fill((0, 0, 0))
            mouse_pos = pygame.mouse.get_pos()

            for button in buttons:
                if button.is_clicked(mouse_pos):
                    button.current_color = button.hover_color
                else:
                    button.current_color = button.color
                button.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttons[0].is_clicked(mouse_pos):
                        self.bullet_speed_multiplier += 0.5
                        upgrade_screen = False
                    elif buttons[1].is_clicked(mouse_pos):
                        self.bullet_damage += 1
                        upgrade_screen = False
                    elif buttons[2].is_clicked(mouse_pos):
                        self.double_bullets = True
                        upgrade_screen = False

            pygame.display.flip()
