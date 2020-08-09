def test(a, b):
    a += b
    return a


"""
    int
"""
a = 1
b = 2
test(a, b)
# 1
print(a)

"""
    list    
    list的__iadd__魔术方法不会返回新的引用
    而是原地修改自身的值
"""
a1 = [1, 2]
a2 = [2, 3]

test(a1, a2)
# [1, 2, 3, 4]
print(a1)

"""
    tuple
    tuple的__iadd__魔术方法直接相加后返回新的引用,因为tuple是不可变的
"""

t1 = (1, 2)
t2 = (2, 3)
test(t1, t2)

# (1, 2)
print(t1)
