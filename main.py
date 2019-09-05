# Higher Card Game - project 1, a card deck is created, shuffled and dealt to the user and dealer. The higher card wins. Option to keep playing or exit at end of hand
import random
import time

card = ["1","2","3","4","5","6","7","8","9", "10","J","Q","K","A"]
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]

def BuildDeck():
    deck = []
    for i in range(len(card)):
        for ind in range(len(suit)):
            cardName = card[i] + " of " + suit[ind]
            deck.append(cardName)
    return deck

#randomizes the list of cards, simulating a shuffle
def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

#takes the card string and converts it to a number than can be compared
def getCardVal(card):
        
        card_numeric = card[0].isnumeric()
        
        if card_numeric == True:
                if card[1]  == 0:
                        cardVal = 10
                else:
                        cardVal = int(card[0])
        else:
                if card[0] == "J":
                        cardVal = 10
                elif card[0] == "Q":
                        cardVal = 11
                elif card[0] == "K":
                        cardVal = 12
                else:
                        cardVal = 13
        return int(cardVal)

#Introduction message to the user with a slight pause to give them time to read the rules of the game before the play loop starts
print("Welcome to higher card! Card values have the same value as regular playing cards.\nThe dealer will shuffle the deck and deal you and themselves a card. \nWhomever's card is higher wins.\n\n\n")
time.sleep(3)

keep_playing = "Y"
while keep_playing == "Y" or keep_playing == "y":

        deck = BuildDeck()

        newDeck = shuffleDeck(deck)
        
        print("\n\n\nA new hand is being dealt...\n\n\n")
        time.sleep(2)

        yourCard = deck[0]
        dealerCard = deck[1]

        print("Your card is:", yourCard, "\n")
        time.sleep(2)
        print("Dealers card is: ", dealerCard, "\n")
        time.sleep(3.5)

        card1val = getCardVal(yourCard)
        card2val = getCardVal(dealerCard)

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

