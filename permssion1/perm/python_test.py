from random import shuffle as rand_shuffle

class Card:
    ...

class DeckOfCards(Card):
    def __init__(self):
        self.deck = {
            "hearts":["A",2,3,4,5,6,7,8,9,10,"J","Q","K"],
            "diamond":["A",2,3,4,5,6,7,8,9,10,"J","Q","K"],
            "club":["A",2,3,4,5,6,7,8,9,10,"J","Q","K"],
            "spade":["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
        }
        self.deck_l = []

    def shuffle(self):
        for key,value in self.deck.items():
            rand_shuffle(value)
            self.deck[key] = value

    def deal(self,suit,card):
        cards = self.deck.get(suit)
        
        if cards:
            try:
                cards.remove(card)
                return "{} removed".format(card)
            except ValueError as e:
                return "Card already removed or not in deck"
            except Exception as e:
                return str(e)
        return "Suit not found"