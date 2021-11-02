# from cards import Card
# from cards import Deck
#from cards import Player
import os
import random


suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
suit_signs = [ '\u2664', '\u2661', '\u2667', '\u2662']
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#card_names = ['Ace', '2', '3']
#card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



# suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

### CLASSES

# Card class 
class Card(object):
    def __init__(self, suit, rank):
        if suit in suits:
            self.suit = suits.index(suit)
        else:
            print('Wrong suit "{}" of the card ({}), acceptable only {}'.format(suit, rank, suits))
            exit(0)
        self.rank = rank
        if rank == 0:
            self.value = 11
        elif rank >= 9:
            self.value = 10
        else:
            self.value = self.rank+1
    
    def get_value(self):
        return self.value
    
    def show(self):
        print('CARD: {} of {} (value {})'.format(cards[self.rank], suits[self.suit], self.value))
    
    def pair(self):
        return cards[self.rank] + suit_signs[self.suit] + ' '
        

# Deck class

class Deck(object):
    def __init__(self):
        self.cards = []
        self.create()
    
    def create(self):
        for suit in suits:
            for rank in range(len(cards)):
                self.cards.append(Card(suit, rank))
    
    def show(self):
        full_deck = ''
        for card in self.cards:
            full_deck += card.pair()
        print('DECK:', full_deck)
    
    def shuffle(self):
        for i in range (len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()

# Player class

class Player(object):
    def __init__(self, name, dealer=False):
        self.hand = []
        self.name = name
        self.value = 0
        self.aces = 0
        self.dealer = dealer
  
    def draw(self, deck):
        card = deck.draw()
        self.hand.append(card)
        if not self.dealer:
            self.value += card.value
        if card.rank == 0:      # Ace
            self.aces +=1
        return self

    def adjustment(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -=1

    def show(self):
        player_cards = ''
        i = 0
        for card in self.hand:
            if self.dealer and i >= len(self.hand)-1:
                player_cards += '**'
            else:
                player_cards += card.pair()
            i+=1
        print('{} has [ {}] with value {}'.format(self.name, player_cards, self.value))       

    def discard(self):
        return self.hand.pop()

class Chips(object):
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win(self):
        self.total += self.bet

    def lose(self):
        self.total -= self.bet

    def show(self):
        print('Total: {}, Bet: {}'.format(self.total, self.bet))

### FUNCTIONS

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry! Please, type in a number: ')
        else:
            if chips.bet > chips.total:
                print('You bet ({}) can\'t exceed your total amount of chips ({})!'.format(chips.bet, chips.total))
            else: 
                break

def hit(deck, player):
    player.draw(deck)
    player.adjustment()

def hit_or_stand(deck, player):
    global playing

    while True:
        ask = input('Would you like to hit or stand? Please, enter "h" or "s": ')

        if ask[0].lower() == 'h':
            hit(deck, player)
        elif ask[0].lower == 's':
            print ('Player stands, Dealer is palying.')
            playing = False
        else:
            print('Sorry! I didn\'t understand that! Please, try again!')
            continue
        break

#    def show_some(player, dealer):


### MAIN

def main():
    str = ''

    os.system('clear')
    print('Welcome to BlackJack!')
    
    while True:
        deck = Deck()
        deck.shuffle()
        #deck.show()
 
        player = Player('Mike')
        player.draw(deck).draw(deck)
        player.show()

        dealer = Player('Dealer')
        dealer.draw(deck).draw(deck)
        dealer.hidden()

 #   deck.show()

if __name__ == '__main__':
    main()


