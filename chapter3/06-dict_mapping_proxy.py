from types import MappingProxyType

"""
    1. 为dict创建一个proxy对象
    这个proxy对象是不可变的
    
    2. 一旦dict发生改变,proxy也会发生改变
"""

d = {"a": 1}

d_proxy = MappingProxyType(d)

# not support item assignment,未实现__getitem__
# d_proxy["b"] = 2

d["b"] = 2

# {'a': 1, 'b': 2}
print(d_proxy)
