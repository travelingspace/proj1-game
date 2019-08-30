import random

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

deck = BuildDeck()

newDeck = shuffleDeck(deck)
for i in range(len(newDeck)):
        print(deck[i],"\n")

exit()