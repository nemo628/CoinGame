# from time import sleep
from coin_game import Player, Coin
import pygame
from pygame.locals import *
from random import random

pygame.init()
clock = pygame.time.Clock()
display_width = 720
display_height = 600

window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("coin_game")


white = (255, 255, 255)
gray = (10, 10, 10)
green = (0, 255, 0)
red = (255, 0, 0)


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
                       0.4)

        font2 = pygame.font.Font('freesansbold.ttf', 20)
        block2 = font2.render("(Press enter to continue)", True, white)
        rect2 = block2.get_rect()
        rect2.center = (display_width * 0.5, display_height * 0.6)

        screen.blit(block, rect)
        screen.blit(block2, rect2)
        pygame.display.flip()


def askName(screen, player_number="the"):
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
                    return name.upper()
            elif evt.type == QUIT:
                return
        text_to_display = text + name.upper()
        screen.fill(gray)
        block = font.render(text_to_display, True, white)
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.update()
        # clock.tick(60)


def getPlayerChoice(screen, name):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = f'{name}! Enter your choice: '
    choice = ""
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    choice += evt.unicode
                elif evt.key == K_BACKSPACE:
                    choice = choice[:-1]
                elif evt.key == K_SPACE:
                    choice = choice + " "
                elif evt.key == K_RETURN:
                    return choice
            elif evt.type == QUIT:
                return choice
        text_to_display = text + choice.upper()
        screen.fill(gray)
        block = font.render(text_to_display, True, white)
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.update()
        # clock.tick(60)


def getPlayersChoice(player1, player2, name1, name2):
    idx = 0 if random() < 0.5 else 1
    if idx == 0:
        choice = getPlayerChoice(window, name1)
    else:
        choice = getPlayerChoice(window, name2)

    if choice == "":  # if player didn't choose anything
        choice == "head" if random() < 0.5 else "tail"
    else:
        choice = choice.lower()
        if choice[0] == 'h':
            choice = "head"
        elif choice[0] == 't':
            choice = "tail"
        else:
            choice == "head" if random() < 0.5 else "tail"
    print(f"choice is: {choice}")
    if idx == 0:
        player2.setCoinOption(choice)
        player1.setCoinOption(player2.coinOption)
    else:
        player1.setCoinOption(choice)
        player2.setCoinOption(player1.coinOption)


def showChoiceAndReturnRect(screen):
    coinImage = pygame.image.load('images/coin2.jpeg')
    b = screen.blit(coinImage, (display_width * 0.35, display_height * 0.10))
    return b


def showPlayers(screen, player1, player2, color1=white, color2=white):
    # print(f"choice is: {choice} and index is {idx}")
    playerImg1 = pygame.image.load('images/A.jpeg')
    playerImg2 = pygame.image.load('images/B.jpeg')

    text1 = f"{player1.getName()} takes {player1.coinOption.upper()}"
    font1 = pygame.font.Font('freesansbold.ttf', 20)
    block1 = font1.render(text1, True, color1)
    rect1 = block1.get_rect()
    rect1.center = (display_width * 0.20, display_height * 0.70)

    text2 = f"{player2.getName()} takes {player2.coinOption.upper()}"
    font2 = pygame.font.Font('freesansbold.ttf', 20)
    block2 = font2.render(text2, True, color2)
    rect2 = block2.get_rect()
    rect2.center = (display_width * 0.75, display_height * 0.70)

    screen.blit(playerImg1, (display_width * 0.10, display_height * 0.30))
    screen.blit(playerImg2, (display_width * 0.65, display_height * 0.30))
    screen.blit(block1, rect1)
    screen.blit(block2, rect2)
    # pygame.display.flip()


def tossCoinAndDeciceWinner(player1, player2):
    coin = Coin()
    winningFlip = coin.getCoinOption()
    print(f"winningFlip is:{winningFlip}")
    if player1.didPlayerWin(winningFlip):
        return 0
    else:
        return 1


def game(window, player1, player2):
    run = True
    x = 50
    y = 50
    height = 20
    width = 25
    vel = 2
    firstTimeClick = True
    color1 = white
    color2 = white
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if b.collidepoint(pos) and firstTimeClick:
                    # print("ready to toss")
                    winner = tossCoinAndDeciceWinner(player1, player2)
                    color1 = green if winner == 0 else red
                    color2 = green if winner == 1 else red
                    firstTimeClick = False

        window.fill(gray)
        b = showChoiceAndReturnRect(window)
        showPlayers(window, player1, player2, color1, color2)
        pygame.display.flip()


def main():
    homePage(window)
    name1 = askName(window, "first")
    name2 = askName(window, "second")
    player1 = Player(name1)
    player2 = Player(name2)
    getPlayersChoice(player1, player2, name1, name2)
    game(window, player1, player2)
    pygame.quit()


if __name__ == '__main__':
    main()
