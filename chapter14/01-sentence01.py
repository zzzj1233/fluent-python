import re

RE = re.compile("\w+")


class Sentence:

    def __init__(self, words):
        self._words = RE.findall(words)

    def __getitem__(self, idx):
        return self._words[idx]

    def __len__(self):
        return len(self._words)


if __name__ == '__main__':
    sentence = Sentence("hello world zzzj 1233 cjj")

    # 成功迭代
    for word in sentence:
        print(word)
