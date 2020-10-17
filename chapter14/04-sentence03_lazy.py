import re
from collections.abc import Iterable, Iterator

RE = re.compile("\w+")


class Sentence(Iterable):

    def __init__(self, words):
        self._words = words

    def __iter__(self) -> Iterator:
        # 懒正则解析
        for item in RE.finditer(self._words):
            yield item.group()


if __name__ == '__main__':
    sentence = Sentence("hello world zzzj 1233 cjj")

    # 成功迭代
    for word in sentence:
        print(word)
