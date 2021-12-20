""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
import random
from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def main():
  clearDeck()

  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)

  showDeck()
  showHand(PLAYER)
  showHand(COMP)


def clearDeck():
        for position in range(0, 52):
            cardLoc[position] = 0


def assignCard(NAME):
    import random
    position = random.randint(2, NUMCARDS - 1)
    cardLoc[position] = NAME
    if cardLoc[position] != 0:
        position = random.randint(2, NUMCARDS - 1)
    elif cardLoc[position] == 1:
        position = random.randint(position - 1, NUMCARDS - 1)
    elif cardLoc[position] == 2:
        position = random.randint(position - 1, NUMCARDS - 1)

"""
def assignCard(PLAYER):
    import random
    keepSwimming = True
    while keepSwimming:
        position = random.randint(0, NUMCARDS - 1)
        cardLoc[position] = PLAYER
        if cardLoc[position] != 0:
            position = random.randint(0, NUMCARDS - 1)
        if cardLoc[position] == 0:
            keepSwimming = False


def assignCard(COMP):
    import random
    keepSwimming = True
    while keepSwimming:
        position = random.randint(0, NUMCARDS - 1)
        cardLoc[position] = COMP
        if cardLoc[position] != 0:
            position = random.randint(0, NUMCARDS - 1)
        if cardLoc[position] == 0:
            keepSwimming = False

"""

def showDeck():
    cards = 0
    delta = 0
    gamma = 0
    print("Where are the cards located")
    print("#    card      location")
    while cards <= 51:
        Position = cardLoc[cards]
        if Position == 0:
            Zeta = "DECK"
        if Position == 1:
            Zeta = "PLAYER"
        if Position == 2:
            Zeta = "COMP"
        alpha = delta // 13
        beta = gamma % 13
        cards = cards + 1
        print("{}.   ".format(cards) + rankName[beta] + "  of  " + suitName[alpha] + " {}".format(Zeta))
        delta = delta + 1
        gamma = gamma + 1

"""
def showDeck():
    for i in range (0, 51):
        number = i
    for i in range (0, 51):
        alpha = [i%13]
    for i in range (0, 51):
        beta = [i//13]
    for i in range (0,3):
        delta = []
    cards = ("{}, {} of {}, {} \n" .format(number, rankName[alpha], suitName[beta], playerName[delta]))
    print("#, Card, Location")
    print(cards)
"""

def showHand(NAME):
    if NAME == PLAYER:
        cards = 0
        delta = 0
        gamma = 0
        alpha = 0
        beta = 0
        print("Display Player Hand: ")
        for cards in range(52):
            Position = cardLoc[cards]
            if Position == 1:
                alpha = delta//13
                beta = gamma%13
                print("{} ".format(rankName[beta] + "  of  " + suitName[alpha]))
            cards = cards + 1
            delta = delta + 1
            gamma = gamma + 1
    if NAME == COMP:
        cards = 0
        delta = 0
        gamma = 0
        alpha = 0
        beta = 0
        print("Display Computer Hand: ")
        for cards in range(52):
            Position = cardLoc[cards]
            if Position == 2:
                alpha = delta//13
                beta = gamma%13
                print("{} ".format(rankName[beta] + " of " + suitName[alpha]))
            cards = cards + 1
            delta = delta + 1
            gamma = gamma + 1
"""
def showHand(PLAYER):
    playerhand = []
    playerhand.append(assignCard(PLAYER))
    print("Display Player Hand: ")
    print(playerhand)

def showHand(COMP):
    comphand = []
    comphand.append(assignCard(COMP))
    print("Display Computer Hand: ")
    print(comphand)

"""

main()
