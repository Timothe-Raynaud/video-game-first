import pygame
from Classes.Player import Player


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

    def handling_events(self):
        # Create event for quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # Add movement of player
        self.player.move()

    def display(self):
        # Apply background
        self.screen.blit(self.background, (-550, -200))
        # Display player
        self.player.draw(self.screen)
        self.player.shooting(self.screen)
        # Refresh screen
        pygame.display.flip()

    def run(self):
        # Run loop
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)
