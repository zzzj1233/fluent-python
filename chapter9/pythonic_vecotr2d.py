from array import array
import math


class Vecotr2d:
    typecode = 'd'

    """
        实现slots可以节省内存,主要是节省 __dict__所带来的内存开销
        
        且元素只能只有__slots__内定义的属性
    """
    __slots__ = ('__x', '__y')

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

        # AttributeError: 'Vecotr2d' object has no attribute '_Vecotr2d__z'
        # self.__z = self.x + self.y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    """
        只有实现了__hash__的类
        才可以放入set,或者作为dict的key
    """

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __repr__(self):
        return "{class_name}({x}, {y})".format(class_name=self.__class__.__name__, x=self.x, y=self.y)

    def __getitem__(self, position):
        return [self.x, self.y][position]

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.x == other.x and self.y == other.y

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, [self.x, self.y]))

    def __abs__(self):
        return math.sqrt(math.pow(self.x, self.x) + math.pow(self.y, self.y))
        # return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def formbytes(cls, bs):
        typecode = chr(bs[0])
        memv = memoryview(bs[1:]).cast(typecode)
        return cls(*memv)


vector = Vecotr2d(1, 2)
# 1.0
print(vector.x)
# 2.0
print(vector.y)

x, y = vector
# 1.0, 2.0
print(x, y)

# clone
v2 = eval(eval("repr(vector)"))

# True
print(v2 == vector)

# 可迭代
for item in v2:
    pass

# 可转换为字节
bs = bytes(v2)

print(abs(v2))

v3 = Vecotr2d.formbytes(bs)

# True
print(v3 == v2 == vector)

vecotr_set = {vector, v2, v3}
# 只有一个元素
print(vecotr_set)
