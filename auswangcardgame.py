""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
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

#code above is the starter code given without any changes.

def clearDeck():
    #reset the deck by setting the positions to zero in the array
    for position in range(52):
        cardLoc[position] = 0

def assignCard(NAME):
    #randomize the cards assigned to player and computer
    import random
    #Loop, remember sentry, where it begins, where it ends, and where it changes
    keepSwimming = True
    while keepSwimming:
        position = random.randint(1, NUMCARDS - 1)
        if cardLoc[position] == 0:
            #position will be replaced to represent player computer or deck
            cardLoc[position] = NAME
            keepSwimming = False


def showDeck():
    cards = 0
    delta = 0
    gamma = 0
    print("Where are the cards located")
    print("#    card      location")
    #a deck of cards has 52 but counting starts at 0
    # Loop, remember sentry, where it begins, where it ends, and where it changes
    while cards <= 51:
        Position = cardLoc[cards]
        #as it loops each position, it'll locate where the array stored
        if Position == 0:
            #if the position is zero, it will be labeled for deck
            Zeta = "DECK"
        if Position == 1:
            #if the position is one, it will be labeled for player
            Zeta = "PLAYER"
        if Position == 2:
            #if the position is two, it will be labeled for computer
            Zeta = "COMP"
        #floor division to return as a whole value to give position in the list of suitName
        alpha = delta // 13
        #modulus to return remainder to give position in list of rankName
        beta = gamma % 13
        cards = cards + 1
        #the showdeck is printed as concatenatation to combine each piece collected in the loop
        print("{}:   ".format(cards) + rankName[beta] + "  of  " + suitName[alpha] + " {}".format(Zeta))
        #counters to keep track of the loop and to ensure it stops when it reaches a value equal to parameter
        delta = delta + 1
        gamma = gamma + 1
    # not necessary, but spaces out between each grouping for a more organized look.
    print("\n")


def showHand(NAME):
    #to display the hands of computer and player
    if NAME == PLAYER:
        cards = 0
        delta = 0
        gamma = 0
        alpha = 0
        beta = 0
        print("Display Player Hand: ")
        #looped based on the parameter of the amount of cards
        for card in range(52):
            Position = cardLoc[cards]
            #observes the position in the array to store anything but zeros and twos
            if Position == 1:
                #Floor division and modulus is used to translate integer position into words
                alpha = delta//13
                beta = gamma%13
                #concatenatation to combine each piece collected in the loop
                print("{} ".format(rankName[beta] + "  of  " + suitName[alpha]))
            #counter to keep track of the loop
            cards = cards + 1
            delta = delta + 1
            gamma = gamma + 1
        # not necessary, but spaces out between each grouping for a more organized look.
        print("\n")
    #if the position doesn't represent Player it will be Computer
    else:
        chips = 0
        delta = 0
        gamma = 0
        alpha = 0
        beta = 0
        print("Display Computer Hand: ")
        #looped based on the parameter of the amount of cards. (counting starts at zero)
        for chip in range(52):
            Position = cardLoc[chips]
            #observes the position in the array to store anything but ones and zeros
            if Position == 2:
                #Floor division and modulus is used to translate integer position into words
                alpha = delta//13
                beta = gamma%13
                #concatenatation to combine each piece collected in the loop
                print("{} ".format(rankName[beta] + " of " + suitName[alpha]))
            #counter to keep track of the loop
            chips = chips + 1
            delta = delta + 1
            gamma = gamma + 1
        #not necessary, but spaces out between each grouping for a more organized look.
        print("\n")


main()
