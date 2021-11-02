import random

suit_names = ['Spade', 'Clubs', 'Diamonds', 'Hearts']

class Card(object):
#    suit = 0
#    value = 0
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def show(self):
        print('{} of {}'.format(self.value, self.suit))
        

class Deck(object):
    def __init__(self):
        self.cards = []
        self.create()
    
    def create(self):
        for suit in suit_names:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))
    
    def show(self):
        for card in self.cards:
            card.show()
    
    def shuffle(self):
        for i in range (len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()


class Player(object):
    def __init__(self):
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.draw())

    def show(self):
        for card in self.hand:
            card.show()
