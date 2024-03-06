import sys
import time

import pygame

from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from sprites import Player


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Breakout")
        self._bg = None

        # sprite groups setup
        self.all_sprites = pygame.sprite.Group()

        self.player = Player(self.all_sprites)

    @property
    def bg(self):
        if self._bg is None:
            bg = pygame.image.load('graphics/other/bg.png').convert()
            scale_factor = WINDOW_WIDTH / bg.get_width()
            scaled_height = WINDOW_HEIGHT * scale_factor
            scaled_width = WINDOW_WIDTH * scale_factor
            self._bg = pygame.transform.scale(bg, (scaled_width, scaled_height))
        return self._bg

    def run(self):
        last_time = time.time()
        while True:
            # delta time
            dt = time.time() - last_time
            last_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.display_surface.blit(self.bg, (0, 0))

            # update the game
            self.all_sprites.update(dt)

            # draw the frame
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
