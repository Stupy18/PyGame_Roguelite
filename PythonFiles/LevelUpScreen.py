import pygame

from PythonFiles.Button import Button
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 128, 255)

class LevelUpScreen:
    def __init__(self, background_image_path):
        self.background_image = pygame.image.load("E:\Probabilitati\Joc\images\imagebackground.png")
        self.font = pygame.font.SysFont("arial", 36)  # Create a font object
        self.buttons = [
            Button(100, SCREEN_HEIGHT // 2 - 100, 200, 50, "Speed", BLUE, RED, self.font),
            Button(100, SCREEN_HEIGHT // 2, 200, 50, "Damage", BLUE, RED, self.font),
            Button(100, SCREEN_HEIGHT // 2 + 100, 200, 50, "Double Bullets", BLUE, RED, self.font)
        ]

    def show(self, screen):
        running = True
        while running:
            screen.blit(self.background_image, (0, 0))
            title_surf = self.font.render("Level Up! Choose an Upgrade", True, BLUE)
            screen.blit(title_surf, (50, 50))

            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                button.draw(screen)
                if button.is_clicked(mouse_pos):
                    button.current_color = button.hover_color
                else:
                    button.current_color = button.color

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for index, button in enumerate(self.buttons):
                        if button.is_clicked(mouse_pos):
                            return index

            pygame.display.flip()
