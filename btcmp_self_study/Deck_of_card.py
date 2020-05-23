from random import choice,shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit  = suit

    def __repr__(self):
        return f"{self.suit} of {self.value}"

    def some_card(self):
        self.suit,self.value = choice(list(self.val.items()))
        self.value = choice(self.value)
        return f'{self.suit} of {self.value}'

class Deck:
    def __init__(self):
        suits = ["Heart", "Diamonds", "Clubs", "Spaces"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]
        print(self.cards)

    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count,num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:] #[1,2,3,4,5,6] => [1,2,3] from back slices
        self.cards = self.cards[:-actual] #just updating deck cards
        return cards

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def deal_card(self):
        return self._deal(1)[0]

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)

d = Deck()
print(d.count())
print(d.shuffle())
hand = d.deal_hand(5)
print(hand)
card = d.deal_card()
print(card)
print(d.count())
print(d.cards)