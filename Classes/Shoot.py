import pygame


class Shoot(pygame.sprite.Sprite):

    def __init__(self, player):
        # Instantiate the sprite
        super().__init__()
        # Init can be modified here :
        self.speed = 20
        self.size = 30
        # Add image to player and scale it
        self.image = pygame.image.load('images/shoot.png')
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        # Create a rect for player and place it in the center of display
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + (player.x_size / 2 - self.size / 2)
        self.rect.y = player.rect.y

    def move(self):
        self.rect.y -= self.speed