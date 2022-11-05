import pygame
from Classes.Game import Game

# Initiate value of screen
windowWidth = 800
windowHeight = 800
screen = pygame.display.set_mode((windowWidth, windowHeight))

# Initiate game and run
pygame.init()
game = Game(screen)
game.run()

# Quit game
pygame.quit()
