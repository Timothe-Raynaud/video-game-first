import random
import pygame


class Alien(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        # Init can be modified here :
        self.speed = pygame.display.get_window_size()[1]/140
        self.x_size = pygame.display.get_window_size()[1]/10
        self.y_size = pygame.display.get_window_size()[1]/14
        # Add image to player and scale it
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (self.x_size, self.y_size))
        self.rect = self.image.get_rect()
        self.x_origin = random.randint(0, pygame.display.get_window_size()[0] - self.x_size)
        self.rect.x = self.x_origin
        self.game = game

    def move(self):
        self.rect.y += self.speed

    def remove(self):
        self.game.all_aliens.remove(self)