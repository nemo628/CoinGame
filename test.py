# from time import sleep
import coinGame
import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
display_width = 720
display_height = 600

window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("coin_game")


white = (255, 255, 255)
gray = (120, 120, 86)


def homePage(screen):
    text_to_display = "Welcome to Coin Game"
    while True:
        for evt in pygame.event.get():
            if evt.type == QUIT:
                return
            if evt.type == KEYDOWN:
                if evt.key == K_RETURN:
                    return

        screen.fill(gray)
        font = pygame.font.Font(None, 40)
        block = font.render(text_to_display, True, white)
        rect = block.get_rect()
        rect.center = (display_width * 0.5, display_height *
                       0.4)  # screen.get_rect().center

        font2 = pygame.font.Font('freesansbold.ttf', 20)
        block2 = font2.render("(Press enter to continue)", True, white)
        rect2 = block2.get_rect()
        rect2.center = (display_width * 0.5, display_height * 0.6)

        screen.blit(block, rect)
        screen.blit(block2, rect2)
        pygame.display.flip()


def askName(screen, player_number=""):
    name = ""
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = f'Enter {player_number} player name: '
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_SPACE:
                    name = name + " "
                elif evt.key == K_RETURN:
                    return name
            elif evt.type == QUIT:
                return
        text_to_display = text + name
        screen.fill(gray)
        block = font.render(text_to_display, True, white)
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.update()
        clock.tick(60)


def showCoinImage(screen):
    coinImg1 = pygame.image.load('images/coin1.jpeg')
    screen.blit(coinImg1, (display_width * 0.3, display_height * 0.55))


def showPlayers(screen, name1, name2):
    playerImg1 = pygame.image.load('images/A.jpeg')
    playerImg2 = pygame.image.load('images/B.jpeg')
    screen.blit(playerImg1, (display_width * 0.10, display_height * 0.10))
    screen.blit(playerImg2, (display_width * 0.65, display_height * 0.10))


def game(name1, name2):
    run = True
    x = 50
    y = 50
    height = 20
    width = 25
    vel = 2
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

        window.fill(gray)
        showCoinImage(window)
        showPlayers(window, name1, name2)
        pygame.display.flip()


def main():
    homePage(window)
    name1 = askName(window, "first")
    name2 = askName(window, "second")
    print(f"Players are {name1} and {name2}")
    game(name1, name2)
    pygame.quit()


if __name__ == '__main__':
    main()
