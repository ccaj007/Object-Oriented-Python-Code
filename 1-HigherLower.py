import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10' ,'Jack' ,'Queen' ,'King')

NCARDS = 8

# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

def suffle(deckListIn):
    deckListOut =  deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

# main code

print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower '
      'than the current card')
print('Getting it right adds 20 points; get it wrong and you lose 15 points')
print('you have 50 points to start')
print()

startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)



