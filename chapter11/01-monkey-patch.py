import random
from chapter1.PokerCard import PokerCard

"""
    为PokerCard打补丁
"""

p = PokerCard()
# Card(no=2, suit='黑桃')
print(p[0])


def setitem(card, idx, value):
    card.cards[idx] = value


PokerCard.__setitem__ = setitem

random.shuffle(p)

# Card(no=10, suit='红桃') 
print(p[0])
