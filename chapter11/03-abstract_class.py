from abc import abstractmethod, ABC
from collections import Sequence


class Animal(ABC):

    @abstractmethod
    def eat(self, fd):
        """
            吃东西
        """

    @abstractmethod
    def code(self, lanuage):
        """
            你使用什么语言?
        """


class Person(Animal):

    def eat(self, fd):
        if isinstance(fd, str):
            print("我吃 : {}".format(fd))
        elif isinstance(fd, Sequence):
            for (idx, f) in enumerate(fd):
                print("我吃第:{}个 : {}".format((idx + 1), f))
        else:
            return NotImplementedError

    def code(self, lanuage):
        if lanuage == "Python":
            return "Life is short,I choose python"
        elif lanuage == "Kotlin":
            return "fun main()"
        elif lanuage == "C":
            return "void main(void)"
        elif lanuage == "Javascript":
            return "function main()"
        else:
            return NotImplementedError


@Animal.register
class Monkey:
    def eat(self, fd):
        if fd != "Banana":
            print("the monkey refuse :{}".format(fd))
        else:
            print("tasty!")

    def code(self, lanuage):
        return "Monkey world"


if __name__ == '__main__':
    p: Animal = Person()
    m: Animal = Monkey()

    p.eat("Apple")
    m.eat("Apple")

    print(p.code("Python"))
    print(m.code("Dart"))

    # [<class '__main__.Monkey'>, <class 'object'>]
    print(Monkey.mro())
    # [<class '__main__.Person'>, <class '__main__.Animal'>, <class 'abc.ABC'>, <class 'object'>]
    print(Person.mro())