# Card Game
import random
import time

card = ["1","2","3","4","5","6","7","8","9", "10","J","Q","K","A"]
suit = ["spades", "hearts", "clubs", "diamonds"]

def BuildDeck():
    deck = []
    for i in range(len(card)):
        for ind in range(len(suit)):
            cardName = card[i] + " of " + suit[ind]
            deck.append(cardName)
    return deck

def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

print("Welcome to higher card! Card values have the same value as regular playing cards.\nThe dealer will shuffle the deck and deal you and themselves a card. \nWhomever's card is higher wins.\n\n\n")
time.sleep(3)

keep_playing = "Y"
while keep_playing == "Y" or keep_playing == "y":

        deck = BuildDeck()

        newDeck = shuffleDeck(deck)
        
        print("\n\n\nA new hand is being dealt...\n\n\n")
        time.sleep(3)

        yourCard = deck[0]
        dealerCard = deck[1]

        print("Your card is:", yourCard, "\n\")
        time.sleep(2)
        print("Dealers card is: ", dealerCard, "\n")
        time.sleep(3)

        card1numeric = yourCard[0].isnumeric()
        card2numeric = dealerCard[0].isnumeric()

        if card1numeric == True:
                if yourCard[1]  == 0:
                        card1val = 10
                else:
                        card1val = int(yourCard[0])
        else:
                if yourCard[0] == "J":
                        card1val = 10
                elif yourCard[0] == "Q":
                        card1val = 11
                elif yourCard[0] == "K":
                        card1val = 12
                else:
                        card1val = 13

        if card2numeric == True:
                if dealerCard[1]  == 0:
                        card2val = 10
                else:
                        card2val = int(dealerCard[0])
        else:
                if dealerCard[0] == "J":
                        card2val = 10
                elif yourCard[0] == "Q":
                        card2val = 11
                elif yourCard[0] == "K":
                        card2val = 12
                else:
                        card2val = 13

        if int(card1val) == int(card2val):
                keep_playing = input("\n\n\nTie game! \nPlay again(Y/N>")
                if keep_playing == "Y" or keep_playing == "y":
                        pass
                else:
                        break
        elif int(card1val) > int(card2val):
                keep_playing = input("\n\n\n*****You WIN!***** \nYour card was higher than the dealer's card. \nPlay again (Y/N)?")
                if keep_playing == "Y" or keep_playing == "y":
                        pass
                else:
                        break
        else:
                keep_playing = input("\n\n\nYou loose :( \nYour card was lower than the dealer's card. \nPlay again (Y/N)?")
                if keep_playing == "Y" or keep_playing == "y":
                        pass
                else:
                        break

print("\n\n\nTHANK YOU FOR PLAYING!\n\n\n.................\n\n\nGoodbye :)\n\n\n")
exit()

