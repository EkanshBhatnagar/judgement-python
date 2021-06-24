from enum import Enum
from itertools import product
from random import shuffle

class ranks(Enum):
    TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE = range(2, 15)

class suits(Enum):
    CLUBS,DIAMONDS,HEARTS,SPADES = range(1,5)

class Card(object):
    def __init__(self,suit,rank,in_deck=False, image=None):
        if rank in ranks and suit in suits:
            self.rank = rank
            self.suit = None
        else:
            self.rank = None
            self.suit = None

        self.in_deck = in_deck
        self.image = image
        self.x,self.y = 0,0
        self.horizontal = None
        self.vertical = None

        def __str__(self):
            return str(self.rank.name) + " of " +str(self.suit.name)

class CardStack(object):
    def __init_(self):
        self.cards = []

    def make_full_deck(self):
        self.cards = [Card(suit,rank, in_deck = True) for suit,rank in product(suits,ranks)]

    def __str__(self):
        return str([str(card) for card in self.cards])

    def deal(self,player_deck,num):
        for i in range(num):
            player_deck.cards.append(self.cards.pop())
    
    def deck_shuffle(self):
        shuffle(self.cards)


