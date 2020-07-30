"""
    复数Demo
"""


class Vecotr:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vecotr(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vecotr(self.x * other.x, self.y * other.y)

    # //
    def __truediv__(self, other):
        return Vecotr(self.x // other.x, self.y // other.y)

    # /
    def __floordiv__(self, other):
        return Vecotr(self.x / other.x, self.y / other.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __repr__(self):
        return "Vector(x = {} , y = {})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # >
    def __gt__(self, other):
        return self.x > other.x or self.y > other.y



v1 = Vecotr(2, 3)
v2 = Vecotr(2, 3)
v3 = v1 + v2

print(v3)
print(v1 * v2)
print(v1 / v2)
print(v1 // v2)
print(v1 == v2)

# 如果没有定义lt方法,则会调用gt
print(v1 < v3)
