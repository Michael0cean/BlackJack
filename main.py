import os
from cards import Card
from cards import Deck



def main():
    str = ''

    os.system('clear')
    
    deck = Deck()
    deck.shuffle()
    deck.show()
  
if __name__ == '__main__':
    main()


# 41302cb9-2410-472b-a901-2321916b0920
