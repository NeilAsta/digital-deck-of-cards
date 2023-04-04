class Card:

    def __init__(self,suit,number):
        self._suit = suit
        self._number = number

    def __repr__(self):
        return self._number + " of " + self._suit

    @property
    def suit(self):
        return self._suit

    @property
    def number(self):
        return self._number
    
    
    @suit.setter
    def suit(self,suit):
        if suit in ["hearts","clubs","diamonds","spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @number.setter
    def number(self,number):
        valid = ["A"] + [str(n) for n in range(2,11)] + ["J", "Q", "K"]
        if number in valid:
            self._number=number
        else:
            print("That number isn't in a deck of cards")
            

#my_card = Card("hearts", "6")
#print(my_card)
#my_card.suit = "diamonds"
#print(my_card.suit)


class Deck:

    def __init__(self):
        self._cards = []
        self.populate()
        print(self._cards)


    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = ["A"] + [str(n) for n in range(2,11)] + ["J", "Q", "K"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    def populate2(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = ["A"] + [str(n) for n in range(2,11)] + ["J", "Q", "K"]
        cards = []
        for suit in suits:
            for number in numbers:
                cards.append(Card(suit, number))
        self._cards = cards


deck = Deck()
  

