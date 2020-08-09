"""
    is 比较的是对象的内存地址

    == 会调用对象的__eq__方法
"""


class Testc:
    def __eq__(self, other):
        return True


t1 = Testc()
t2 = Testc()

# False
print(t1 is t2)

# True
print(t1 == t2)
