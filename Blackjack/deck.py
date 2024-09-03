import random 
from card import suits,ranks,Card

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(rank,suit)
                self.deck.append(new_card)
                
    def shuffle_deck(self):
        return random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()