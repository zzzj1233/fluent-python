import re
from collections.abc import Iterable, Iterator

RE = re.compile("\w+")


class SentenceIteraotr(Iterator):
    def __init__(self, words):
        self._words = words
        self.index = 0

    def __next__(self):
        try:
            ret = self._words[self.index]
        except IndexError:
            raise StopIteration
        else:
            self.index += 1
            return ret

    def __iter__(self):
        return self


class Sentence(Iterable):

    def __init__(self, words):
        self._words = RE.findall(words)

    def __iter__(self) -> Iterator:
        return SentenceIteraotr(self._words)


if __name__ == '__main__':
    sentence = Sentence("hello world zzzj 1233 cjj")

    # 成功迭代
    for word in sentence:
        print(word)
