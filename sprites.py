import pygame
from pygame.sprite import Sprite

from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Player(Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.display_surface = pygame.display.get_surface()
        self.image = pygame.Surface((WINDOW_WIDTH // 10, WINDOW_HEIGHT // 40))
        self.image.fill('red')

        # position
        self.rect = self.image.get_rect(midbottom=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 20))
        self.old_rect = self.rect.copy()
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.speed = 300

    def screen_constraint(self):
        print(self.rect.topleft)
        if self.position.x > (WINDOW_WIDTH - self.image.get_width()):
            self.position.x = (WINDOW_WIDTH - self.image.get_width())
        if self.position.x < 0:
            self.position.x = 0

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self, dt):
        self.input()
        self.screen_constraint()
        self.position.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.position.x)
