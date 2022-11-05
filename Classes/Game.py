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
            # For the event of type key down
            if event.type == pygame.KEYDOWN:
                # If is space we create a shoot
                if event.key == pygame.K_SPACE:
                    self.player.shooting()

    def update(self):
        # Add movement of player
        self.player.move()
        # Add movement of shoots
        for shoot in self.player.all_shoots:
            shoot.move()

    def display(self):
        # Apply background
        self.screen.blit(self.background, (-550, -200))
        # Display player
        self.player.draw(self.screen)
        self.player.all_shoots.draw(self.screen)
        # Refresh screen
        pygame.display.flip()

    def run(self):
        # Run loop
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)
