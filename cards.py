
class Card(object):
    suit = 0
    value = 0
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def show(self):
        print('{} of {}'.format(self.value, self.suit))
        
"""
class Deck(object):
    def __init__(self):


class Player(object):
    def __init__(self):
"""

