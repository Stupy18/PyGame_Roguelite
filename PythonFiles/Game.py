import pygame
import random
from PythonFiles.Player import Player
from PythonFiles.Enemy import Enemy
from PythonFiles.Bullet import Bullet

class Game:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1280, 720
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Roguelite Game")

        self.bullet_cooldown = 1000  # Cooldown time in milliseconds
        self.last_bullet_time = pygame.time.get_ticks()

        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 128, 255)

        self.bullet_size = 30
        self.bullet_speed = 10
        self.bullets = []

        self.enemy_size = 40
        self.enemy_speed = 2
        self.enemies = []

        self.player = Player(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2, 50, 5, self.BLUE)
        self.score = 0

    def create_bullets(self, dx, dy):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_bullet_time >= self.bullet_cooldown:
            new_bullet_speed = self.bullet_speed * self.player.bullet_speed_multiplier
            bullet_x = self.player.x + self.player.size // 2 - self.bullet_size // 2
            bullet_y = self.player.y + self.player.size // 2 - self.bullet_size // 2

            # Create the main bullet
            self.bullets.append(
                Bullet(bullet_x, bullet_y, dx * new_bullet_speed, dy * new_bullet_speed, self.bullet_size, self.RED))

            # Create additional bullet if player has double_bullets upgrade
            if self.player.double_bullets:
                offset = 50
                if dx != 0:  # Horizontal movement
                    bullet_y_offset = bullet_y + offset
                    bullet_x_offset = bullet_x
                else:  # Vertical movement
                    bullet_y_offset = bullet_y
                    bullet_x_offset = bullet_x + offset

                self.bullets.append(
                    Bullet(bullet_x_offset, bullet_y_offset, dx * new_bullet_speed, dy * new_bullet_speed, self.bullet_size,
                           self.RED))
            self.last_bullet_time = current_time

    def spawn_enemy(self):
        x, y = random.choice([
            (random.randint(0, self.SCREEN_WIDTH), random.choice([-self.enemy_size, self.SCREEN_HEIGHT])),
            (random.choice([-self.enemy_size, self.SCREEN_WIDTH]), random.randint(0, self.SCREEN_HEIGHT))
        ])
        self.enemies.append(Enemy(x, y, self.enemy_size, self.enemy_speed, self.RED))

    def draw_ui(self):
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {self.score}', True, self.WHITE)
        self.screen.blit(score_text, (10, 40))
        self.player.draw_exp_bar()

    def update_game_state(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        # Enhanced bullet creation logic with upgrades
        if keys[pygame.K_w]:
            self.create_bullets(0, -1)  # Upward bullets
        elif keys[pygame.K_s]:
            self.create_bullets(0, 1)  # Downward bullets
        elif keys[pygame.K_a]:
            self.create_bullets(-1, 0)  # Leftward bullets
        elif keys[pygame.K_d]:
            self.create_bullets(1, 0)  # Rightward bullets

        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.off_screen():
                self.bullets.remove(bullet)
                continue
            for enemy in self.enemies[:]:
                if bullet.rect.colliderect(enemy.get_hitbox()):
                    self.bullets.remove(bullet)
                    enemy.health -= self.player.bullet_damage
                    if enemy.health <= 0:
                        self.enemies.remove(enemy)
                        self.player.gain_exp(10)
                        self.score += 1
                    break

        if random.randint(1, 100) <= self.player.enemy_respawn_rate:
            self.spawn_enemy()
        for enemy in self.enemies:
            enemy.move_towards_player(self.player)
            if enemy.get_hitbox().colliderect(self.player.get_hitbox()):
                self.player.health -= 1
                self.enemies.remove(enemy)
                if self.player.health <= 0:
                    print("Game Over")
                    return False

        return True

    def draw_game(self):
        if self.player.exp >= self.player.required_exp:
            self.player.level_up()
            self.player.show_upgrade_screen()

        self.screen.fill((0, 0, 0))  # Clear screen
        self.player.draw()
        self.player.draw_health_bar()
        self.player.draw_exp_bar()
        self.draw_ui()
        for bullet in self.bullets:
            bullet.draw()
        for enemy in self.enemies:
            enemy.draw()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.update_game_state():
                break

            self.draw_game()
            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()

# Usage example
if __name__ == "__main__":
    game = Game()
    game.run()
