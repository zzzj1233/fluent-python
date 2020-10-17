from abc import abstractmethod
from collections import MutableSequence
from typing import overload, _T, Iterable


class PokerCard2(MutableSequence):

    def __len__(self) -> int:
        pass

    def insert(self, index: int, object: _T) -> None:
        pass

    def __getitem__(self, i: int) -> _T:
        pass

    def __setitem__(self, i: int, o: _T) -> None:
        pass

    def __delitem__(self, i: int) -> None:
        pass
