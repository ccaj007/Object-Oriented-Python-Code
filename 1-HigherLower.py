import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10' ,'Jack' ,'Queen' ,'King')

NCARDS = 8

# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

def shuffle(deckListIn):
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
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print(f'\nStarting card is: {currentCardRank} of {currentCardSuit}\n')

    for cardNumber in range (0,NCARDS):
        answer = input(f'Will the next card be higher or lower than the {currentCardRank} of {currentCardSuit}? (enter h or l)')
        answer = answer.lower()

        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardValue = nextCardDict['value']
        nextCardSuit = nextCardDict['suit']
        print(f'\nNext card is: {nextCardRank} of {nextCardSuit}\n')

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You guessed correctly, it was higher')
                score += 20
            else:
                print('Sorry it was not higher')
                score -=15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print('You guessed correctly, it was lower')
                score += 20
            else:
                print('Sorry it was not lower')
                score -=15
        else:
            print('\nYou have to guess h or l...')

        print(f'Your score is: {score}\n')
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

        goAgain = input('To play again, press ENTER, or "q" to quit: ')
        if goAgain.lower() == 'q':
            break
print('OK bye')




