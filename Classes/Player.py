import pygame
from Classes.Shoot import Shoot


class Player(pygame.sprite.Sprite):

    def __init__(self):
        # Instantiate the sprite
        super().__init__()
        # Init can be modified here :
        self.x_size = pygame.display.get_window_size()[1]/14
        self.y_size = pygame.display.get_window_size()[1]/8
        self.speed = pygame.display.get_window_size()[0]/80
        # Add image to player and scale it
        self.image = pygame.image.load("images/spaceShip.png")
        self.image = pygame.transform.scale(self.image, (self.x_size, self.y_size))
        # Create a rect for player and place it in the center of display
        self.rect = self.image.get_rect()
        self.rect.x = (pygame.display.get_window_size()[0] / 2) - (self.x_size / 2)
        self.rect.y = (pygame.display.get_window_size()[1] / 2) - (self.y_size / 2)
        # Create limit border point
        self.border_left = 0
        self.border_right = pygame.display.get_window_size()[0] - self.x_size
        self.border_top = 0
        self.border_bottom = pygame.display.get_window_size()[1] - self.y_size
        # Init move variable
        self.velocity = [0, 0]
        # Init shoots
        self.all_shoots = pygame.sprite.Group()


    def move(self):
        # Create variable key
        keys = pygame.key.get_pressed()
        # Listen if "q" or "d" is pushed and associate to velocity the logic value for x move
        if keys[pygame.K_q] and self.rect.x > self.border_left and not keys[pygame.K_d]:
            self.velocity[0] = -1
        elif keys[pygame.K_d] and self.rect.x < self.border_right and not keys[pygame.K_q]:
            self.velocity[0] = 1
        else:
            self.velocity[0] = 0
        # Listen if "z" or "s" is pushed and associate to velocity the logic value for y move
        if keys[pygame.K_z] and self.rect.y > self.border_top and not keys[pygame.K_s]:
            self.velocity[1] = -1
        elif keys[pygame.K_s] and self.rect.y < self.border_bottom and not keys[pygame.K_z]:
            self.velocity[1] = 1
        else:
            self.velocity[1] = 0
        # Create movement with the result of pushed key.
        # For example if z is pushed, velocity = [0, -1]
        # We multiply by speed and create move -> move_ip(0, -5)
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shooting(self):
        self.all_shoots.add(Shoot(self))
