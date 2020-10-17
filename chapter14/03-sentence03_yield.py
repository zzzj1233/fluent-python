import re
from collections.abc import Iterable, Iterator

RE = re.compile("\w+")


class Sentence(Iterable):

    def __init__(self, words):
        self._words = RE.findall(words)

    def __iter__(self) -> Iterator:
        for item in self._words:
            yield item


if __name__ == '__main__':
    sentence = Sentence("hello world zzzj 1233 cjj")

    # 成功迭代
    for word in sentence:
        print(word)
