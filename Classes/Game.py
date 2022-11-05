import random

import pygame
from Classes.Player import Player
from Classes.Alien import Alien


class Game:

    def __init__(self, screen):
        self.score = 0
        # Set name of window
        pygame.display.set_caption("This is a game !")
        # Instantiate all necessary
        self.screen = screen
        self.background = pygame.image.load('images/background.jpg')
        self.running = True
        self.clock = pygame.time.Clock()
        # Set shoot stats
        self.last_shoot_time = pygame.time.get_ticks()
        self.waiting_shoot = 300
        # Aliens
        self.waiting_alien = pygame.time.get_ticks() + 500
        self.all_aliens = pygame.sprite.Group()
        self.spawnAlien()
        self.is_alive = True;
        self.player = Player(self)
        pygame.font.init()
        self.font = pygame.font.Font(None, 50)


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
            if self.check_collision(shoot, self.all_aliens):
                shoot.remove()
                self.score += 1
        # Aliens move
        for alien in self.all_aliens:
            alien.move()

    def display(self):
        # Apply background
        self.screen.blit(self.background, (-200, 0))
        # Display player
        self.player.draw(self.screen)
        self.player.all_shoots.draw(self.screen)
        # Display aliens
        self.all_aliens.draw(self.screen)
        # Refresh screen
        self.text = self.font.render("Score : %d" % self.score, True, (255, 255, 255))
        self.screen.blit(self.text, (30, 30))
        pygame.display.flip()

    def spawnAlien(self):
        now = pygame.time.get_ticks()
        random_wait = random.randint(1000, 2500)
        if self.waiting_alien + random_wait < now:
            self.all_aliens.add(Alien(self))
            self.waiting_alien = now

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

    def run(self):
        # Run loop
        while self.running:
            self.spawnAlien()
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)
            if self.check_collision(self.player, self.all_aliens) or self.is_alive == False:
                self.running = False

