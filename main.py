from cards import Card
from cards import Deck
from cards import Player
import os



def main():
    str = ''

    os.system('clear')
    print('New BlackJack game')
    
    deck = Deck()
    deck.shuffle()
 #   deck.show()
    player = Player('Mike')
    player.draw(deck).draw(deck)

    player.show()
  
if __name__ == '__main__':
    main()


# 41302cb9-2410-472b-a901-2321916b0920
