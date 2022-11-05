import pygame
from Classes.Game import Game

pygame.font.init()
# Initiate value of screen
windowWidth = 1920
windowHeight = 1080
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("This is a game !")
background = pygame.image.load('images/background.jpg')
clock = pygame.time.Clock()
running = True
playing = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playing = True

    if playing:
        pygame.init()
        game = Game(screen)
        score = game.run()
        playing = False

    font = pygame.font.Font(None, 100)
    text = font.render("Your score is : %d" % score, True, (255, 255, 255))
    font2 = pygame.font.Font(None, 110)
    text2 = font2.render("Presse \"Enter\" for try again !", True, (255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(text, (700, 600))
    screen.blit(text2, (400, 700))
    pygame.display.flip()
    clock.tick(60)

# Quit game
pygame.quit()