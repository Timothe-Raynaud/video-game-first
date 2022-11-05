import pygame


class Shoot(pygame.sprite.Sprite):

    def __init__(self, x, y):
        # Instantiate the sprite
        super().__init__()
        # Init can be modified here :
        self.speed = 20
        self.size = 20
        # Add image to player and scale it
        self.image = pygame.image.load('images/shoot.png')
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        # Create a rect for player and place it in the center of display
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shooting(self, screen):
        pass