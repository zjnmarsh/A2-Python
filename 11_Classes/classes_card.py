import random


class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.card_deck = []
        self.build()

    def build(self):
        for s in ['D','H','C','S']:
            for v in ['A','2','3','4','5','6','7','8','9','J','Q','K']:
                self.card_deck.append(Card(s,v))

    def show(self):
        for c in self.card_deck:
            c.show()

    def shuffle(self):
        for i in range(len(self.card_deck)):
            rand = random.randint(0,i)
            self.card_deck[i], self.card_deck[rand] = self.card_deck[rand], self.card_deck[i]

    def deal(self):
        return self.card_deck.pop()


deck = Deck()
deck.show()
deck.shuffle()
deck.show()
dealt_card = deck.deal()
dealt_card.show()

# JTT feedback:
# Nice use of built-in .show() method.
# What happens if you try to deal more than 52 cards? How could you implement something to handle that gracefully?
# Now go back and add some more docstrings to your methods to describe what each does.
