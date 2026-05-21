# Task Description
# Make a french deck class that represents a standard 52 card deck

#Objectives
# 1. calling len() on it should return 52
# 2. indexing it with deck[0] should return the first card
# 3. slicing it with deck[:5] should return the first five cards
# 4. iterating over it with a for loop should yield every card in order
# 5. using in to check if a card is in the deck should work without you writing an explicit search
# 6. and calling repr() on a single card should show something readable like Card(rank='A', suit='spades') instead of a memory address.

from collections import namedtuple

Card = namedtuple("Card", ["rank", "suit"])

card = Card("A", "diamonds")

print(card.rank)
print(card.suit)


class FrenchDeck():
    
    ranks = [str(n) for n in list(range(2,11)) + list('AKQJ')]
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
    
    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, key):
        return self.cards[key]
    
deck = FrenchDeck()

#testing 

print(len(deck))
print(deck[0])
print(deck[:5])

for i in range(0, len(deck)):
    print(deck[i])
        
check = Card('11', 'hearts') in deck
print(check)

print(repr(deck[0]))