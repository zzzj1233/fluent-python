"""
    1. 集合是无序的,基于dict实现的(没有value的dict)
    2. 集合和作为dict.key的元素必须实现__hash__和__eq__
    3. Python的集合可以很方便的取差集,交集,并集
    4. 如果初始化一个空集合 : set(),而不能使用{ }(这是dict)
"""

# 集合推导式
s1 = {i for i in range(0, 9, 3)}

s2 = {i for i in range(1, 9, 2)}

# {0, 3, 6}
print(s1)

# {1, 3, 5, 7}
print(s2)

# 并集: { 3 }
print(s1 & s2)

# 交集: {0, 1, 3, 5, 6, 7}
print(s1 | s2)

# 差集: {0, 6}
print(s1 - s2)