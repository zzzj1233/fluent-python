import math
from array import array
from collections.abc import Iterable
from functools import reduce
from operator import xor


class Vector:
    typcode = "d"

    __quick_access_attrs = ['x', 'y', 'z', 'c']

    def __init__(self, items):
        _items = None
        if not isinstance(items, Iterable):
            _items = [items]
        else:
            _items = items

        self._items = array(self.typcode, _items)

    def __getattr__(self, attr):
        try:
            idx = self.__quick_access_attrs.index(attr)
            return self._items[idx]
        except ValueError:
            return super().__getattribute__(attr)

    def __setattr__(self, key, value):
        try:
            idx = self.__quick_access_attrs.index(key)
            self._items[idx] = value
        except ValueError:
            super().__setattr__(key, value)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self._items[index]
        elif isinstance(index, slice):
            return self.__class__(self._items[index])
        else:
            raise Exception("Unknow index type!")

    def __setitem__(self, idx, value):
        self._items[idx] = value

    """
        使用zip函数比较,可降低比较开销
    """

    def __eq__(self, other):
        if not len(self) == len(other):
            return False
        for x, y in zip(self, other):
            if x != y:
                return False
        return True

    """
        使对象可散列
    """

    def __hash__(self):
        hash_list = [hash(item) for item in self._items]
        return reduce(xor, hash_list)

    """
        使对象可以转换为字节数组
    """

    def __bytes__(self):
        return bytes([ord(self.typcode)]) + bytes(self._items)

    def __abs__(self):
        return math.sqrt(sum([item * item for item in self._items]))

    def __bool__(self):
        return bool(abs(self))

    def __repr__(self):
        return "Vector( {} )".format(self._items.tolist())

    def __str__(self):
        return repr(self)

    @classmethod
    def from_bytes(cls, bytes):
        if not bytes:
            raise Exception("bytes can‘t be empty!")
        typecode = chr(bytes[0])
        menv = memoryview(bytes[1:]).cast(typecode)
        return cls(menv)


v = Vector([1, 2, 3, 4])

# 返回的还是一个Vector对象
print(v[1:])

print(bool(v))

print(v)

# true
print(Vector.from_bytes(bytes(v)) == v)

"""
    寻找对象属性的顺序
    
    1. 去对象实例[父类]属性上找
    2. 去对象类[父类]属性上找
    3. 寻找对象的__getattr_魔术方法
    
    都没有找到则抛出异常
"""
print(v.x)
print(v.y)
print(v.z)
print(v.c)

# AttributeError
# print(v.v)

v.x = 999

# Vector( [999.0, 2.0, 3.0, 4.0] )
print(v)
