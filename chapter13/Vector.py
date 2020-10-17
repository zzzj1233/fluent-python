"""
    实现了运算符重载的Vector
"""
from collections.abc import Sequence
from itertools import zip_longest


class Vector:
    def __init__(self, items):
        self._items = tuple(items)

    def __repr__(self):
        return "Vector( {} )".format(self._items)

    def __neg__(self):
        return [-x for x in self._items]

    def __getitem__(self, item):
        return self._items[item]

    def __add__(self, other):
        if isinstance(other, Sequence):
            return self.__class__((x + y for (x, y) in zip_longest(self, other, fillvalue=0)))
        else:
            return NotImplemented

    def __radd__(self, other):
        return Vector.__add__(self, other)


if __name__ == '__main__':
    v = Vector([1, 3, 5])

    # Vector( (3, 7, 5) )
    print(v + [2, 4])
