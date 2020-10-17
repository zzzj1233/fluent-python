from collections.abc import Reversible
from chapter1.PokerCard import PokerCard


def reverse_card(pocker_card):
    for card in pocker_card[::-1]:
        yield card


if __name__ == '__main__':
    card = PokerCard()
    PokerCard.__reverse__ = reverse_card

    for c in reversed(card):
        print(c)
