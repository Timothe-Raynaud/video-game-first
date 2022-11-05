import random

import pygame
from Classes.Player import Player
from Classes.Alien import Alien


class Game:

    def __init__(self, screen):
        # Set name of window
        pygame.display.set_caption("This is a game !")
        # Instantiate all necessary
        self.screen = screen
        self.background = pygame.image.load('images/background.jpg')
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player()
        # Set shoot stats
        self.last_shoot_time = pygame.time.get_ticks()
        self.waiting_shoot = 300
        # Aliens
        self.waiting_alien = pygame.time.get_ticks() + 500
        self.all_aliens = pygame.sprite.Group()
        self.spawnAlien()

    def handling_events(self):
        # Create event for quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # For the event of type key down
            if event.type == pygame.KEYDOWN:
                # If is space we create a shoot and limit the spam
                now = pygame.time.get_ticks()
                if event.key == pygame.K_SPACE and self.last_shoot_time + self.waiting_shoot < now:
                    self.last_shoot_time = now
                    self.player.shooting()

    def update(self):
        # Add movement of player
        self.player.move()
        # Add movement of shoots
        for shoot in self.player.all_shoots:
            shoot.move()
        # Aliens move
        for alien in self.all_aliens:
            alien.move()

    def display(self):
        # Apply background
        self.screen.blit(self.background, (-550, 0))
        # Display player
        self.player.draw(self.screen)
        self.player.all_shoots.draw(self.screen)
        # Display aliens
        self.all_aliens.draw(self.screen)
        # Refresh screen
        pygame.display.flip()

    def spawnAlien(self):
        now = pygame.time.get_ticks()
        random_wait = random.randint(1000, 2500)
        if self.waiting_alien + random_wait < now:
            self.all_aliens.add(Alien(self))
            self.waiting_alien = now

    def run(self):
        # Run loop
        while self.running:
            self.spawnAlien()
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)
