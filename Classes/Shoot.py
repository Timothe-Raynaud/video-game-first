import pygame


class Shoot(pygame.sprite.Sprite):

    def __init__(self, player):
        # Instantiate the sprite
        super().__init__()
        # Init can be modified here :
        self.speed = 20
        self.size = pygame.display.get_window_size()[0]/18
        # Add image to player and scale it
        self.image = pygame.image.load('images/shoot.png')
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        # Create a rect for player and place it in the center of display
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + (player.x_size / 2 - self.size / 2)
        self.rect.y = player.rect.y
        # Create player
        self.player = player


    def remove(self):
        self.player.all_shoots.remove(self)

    def move(self):
        # Movement of shoot
        self.rect.y -= self.speed
        # Delete shoot if is out of screen
        if self.rect.y < 0:
            self.remove()