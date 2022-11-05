import random
import pygame


class Alien(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.height_size = pygame.display.get_window_size()[1]
        self.speed = self.height_size/130 * (1 + (self.game.waiting_alien / 80000))
        self.x_size = self.height_size/10
        self.y_size = self.height_size/14
        # Add image to player and scale it
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (self.x_size, self.y_size))
        self.rect = self.image.get_rect()
        self.x_origin = random.randint(0, int(pygame.display.get_window_size()[0] - self.x_size))
        self.rect.x = self.x_origin

    def move(self):
        self.rect.y += self.speed
        # Delete shoot if is out of screen
        if self.rect.y > self.height_size:
            self.game.is_alive = False

