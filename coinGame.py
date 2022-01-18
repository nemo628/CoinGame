import sys
from random import random


class Player:
    def __init__(self, name):
        self.__name = name
        self.coinOption = ""
        self.__numWins = 0

    def setCoinOption(self, opponent_flip):
        self.coinOption = "head" if opponent_flip == "tail" else "tail"

    def getRandCoinOption(self):
        self.coinOption = "head" if random() < 0.5 else "tail"
        return self.coinOption

    def didPlayerWin(self, winningFlip):
        if self.coinOption == winningFlip:
            # print(f"{self.name} win with the flip {self.coinOption}")
            self.__numWins += 1
            return True

    def getNumWins(self):
        return self.__numWins

    def getName(self):
        return self.__name


class Coin:
    def __init__(self):
        self.coinOption = ""

    def getCoinOption(self):
        self.coinOption = "head" if random() < 0.5 else "tail"
        return self.coinOption


class CoinGame:
    def __init__(self, player1Name, player2Name):
        self.player = list()
        self.player.append(Player(player1Name))
        self.player.append(Player(player2Name))
        self.coin = Coin()

    def startGame(self):
        randIdx = 0 if random() < 0.5 else 1
        playerPick = self.player[randIdx].getRandCoinOption()
        opponentIdx = 0 if randIdx == 1 else 1
        self.player[opponentIdx].setCoinOption(playerPick)

        winningFlip = self.coin.getCoinOption()
        self.player[0].didPlayerWin(winningFlip)
        self.player[1].didPlayerWin(winningFlip)


def getInputNames():
    while(True):
        try:
            player1Name, player2Name = input(
                "Enter names of participants of coin game: \n").split()

        except ValueError:
            print("Please provide two valid names separated by space")
            continue

        else:
            break

    return player1Name, player2Name


def getInputTurns():
    while(True):
        try:
            turns = int(
                input("Enter how many times do you want to play (space separated): \n"))
        except (ValueError, TypeError):
            continue
        else:
            break

    return turns


def main():
    player1Name, player2Name = "a", "b"  # getInputNames()
    turns = 4  # getInputTurns()
    game = CoinGame(player1Name, player2Name)
    for turn in range(turns):
        game.startGame()

    if game.player[0].getNumWins() > game.player[1].getNumWins():
        print(f"{game.player[0].getName()} wins.")

    elif game.player[0].getNumWins() < game.player[1].getNumWins():
        print(f"{game.player[1].getName()} wins.")

    else:
        print("It's a tie.")

    print(
        f"{game.player[0].getName()} wins {game.player[0].getNumWins()} times and {game.player[1].getName()} wins {game.player[1].getNumWins()} times")


if __name__ == '__main__':
    main()
