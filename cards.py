import random

suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
suit_signs = [ '\u2664', '\u2661', '\u2667', '\u2662']
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'Q', 'K']
card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



# suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

class Card(object):
#    suit = 0
#    value = 0
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def show(self):
#        print('{} of {}'.format(self.value, self.suit))
        print('{} {} (value {})'.format(cards[self.value], self.suit, card_values[self.value]))
        

class Deck(object):
    def __init__(self):
        self.cards = []
        self.create()
    
    def create(self):
        for suit in suits:
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
    def __init__(self, name):
        self.hand = []
        self.name = name
    
    def draw(self, deck):
        self.hand.append(deck.draw())
        return self

    def show(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()
