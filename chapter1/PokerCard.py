from random import choice
from collections import namedtuple

nums = [i for i in range(2, 11)] + ["J", "O", "K", "A"]
suits = ["黑桃", "红桃", "梅花", "方块"]

Card = namedtuple("Card", ("no", "suit"))


class PokerCard:
    def __init__(self):
        self.cards = [Card(no, suit) for no in nums for suit in suits]

    def __getitem__(self, position):
        return self.cards[position]

    def __delitem__(self, index):
        del self.cards[index]

    def __setitem__(self, key, value):
        self.cards[key] = value

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return str(self.cards)


if __name__ == '__main__':
    poker_card = PokerCard()

    """
        {'no': 'O', 'suit': '黑桃'}
    """
    print(choice(poker_card)._asdict())

    poker_card[0] = Card(0, 0)

    """
        {'no': 0, 'suit': 0}
    """
    print(poker_card[0]._asdict())

    del poker_card[0]

    """
        after del
        {'no': 2, 'suit': '红桃'}
        51
    """
    print(poker_card[0]._asdict())
    print(len(poker_card))
