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
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.value = 0
        self.aces = 0
  
    def draw(self, deck):
        card = deck.draw()
        self.hand.append(card)
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
        for card in self.hand:
            player_cards += card.pair()
        print('{} has [ {}] with value {}'.format(self.name, player_cards, self.value))       

    def hidden(self):
        player_cards = ''
        i = 0
        for card in self.hand:
            if i >= len(self.hand)-1:
                player_cards += '**'
            else:
                player_cards += card.pair()
            i+=1
#        print('{} has [ {}] with value {}'.format(self.name, player_cards, self.value))       
        print('{} has [ {}]'.format(self.name, player_cards))       

    def discard(self):
        return self.hand.pop()

# Chips class

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
    while True:
        ask = input('Would you like to hit or stand? Please, enter "h" or "s": ')

        if ask[0].lower() == 'h':
            hit(deck, player)
        elif ask[0].lower() == 's':
            print ('Player stands, Dealer is palying.')
            return False
        else:
            print('Sorry! I didn\'t understand that! Please, try again!')
            continue
        break
    return True

def play_again():
    while True:
        ask = input('Whould you like to play again? Type "y" or "n": ')
        if ask[0].lower() == 'y':
            return True
        elif ask[0].lower() == 'n':
            return False
        else:
            print('Sorry! I didn\'t understand that! Please, try again!')
            continue

### MAIN (Gameplay)

def main():
    str = ''

    os.system('clear')
    print('Welcome to BlackJack!')
    
    # Set up the player's chips 
    player_chips = Chips()

    while True:

        # Create a shuffle desk
        deck = Deck()
        deck.shuffle()
     #   deck.show()
 
        # Create a player and draw two cards
        player = Player('Mike')
        player.draw(deck).draw(deck)
      
        # Create a dealer and drow two cards (one hidden)
        dealer = Player('Dealer')
        dealer.draw(deck).draw(deck)

        # Ask player for bet
        take_bet(player_chips)

        # Show player and dealer cards 
        player.show()
        dealer.hidden()

        # Ask player to Hit or Stand
        while hit_or_stand(deck, player):            
            player.show()
            dealer.hidden()
            if player.value > 21:
                print('PLAYER BUSTS!')
                player_chips.lose()
                break

        if player.value <= 21:
            while dealer.value < 17:
                hit(deck, dealer)

        player.show()
        dealer.show()

        if dealer.value > 21:
            print('DEALER BUSTS!')
            player_chips.win()
        elif player.value > 21:
                print('PLAYER BUSTS!')
                player_chips.lose()
        elif dealer.value > player.value:
            print('DEALER WINS!')
            player_chips.lose()
        elif dealer.value < player.value:
            print('PLAYER WINS!')
            player_chips.win()
        else:
            print('DEALER WINS!')
            player_chips.lose()

        player_chips.show()
        
        if not play_again():
            break
 #   deck.show()

if __name__ == '__main__':
    main()


