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
playing = False
first = True
score = 0
pygame.init()
main_mixer = pygame.mixer.music
main_mixer.load("music/17 - Memory.mp3")
main_mixer.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playing = True
                first = False

    if playing:
        main_mixer.load("music/01 - Tank!.mp3")
        main_mixer.play()
        game = Game(screen)
        score = game.run()
        playing = False
        main_mixer.load("music/17 - Memory.mp3")
        main_mixer.play()

    if first:
        font = pygame.font.Font('font/retro.ttf', 25)
        text = font.render("Hello and welcome on my this terrible universe. ", True, (255, 255, 255))
        text2 = font.render("We need your help ! Proxima Z is attacked by aliens !", True, (255, 255, 255))
        text3 = font.render("Kill them all and don't let pass them ! Otherwise the people on the planet will die...", True, (255, 255, 255))
        font2 = pygame.font.Font('font/retro.ttf', 30)
        text4 = font2.render("For move use \"Z\",\"Q\",\"S\",\"D\" and use \"Space\" for shooting !", True, (255, 255, 255))
        text5 = font2.render("Press \"Enter\" beginning !", True, (255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(text, (300, 200))
        screen.blit(text2, (300, 230))
        screen.blit(text3, (300, 260))
        screen.blit(text4, (400, 800))
        screen.blit(text5, (700, 900))
        pygame.display.flip()
    else:
        font = pygame.font.Font('font/retro.ttf', 50)
        text = font.render("Your score is : %d" % score, True, (255, 255, 255))
        font2 = pygame.font.Font('font/retro.ttf', 60)
        text2 = font2.render("Press \"Enter\" for try again !", True, (255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(text, (700, 600))
        screen.blit(text2, (400, 700))
        pygame.display.flip()

    clock.tick(60)

# Quit game
pygame.quit()