from copy import copy

l1 = [1, [2, 3], 4]

l2 = list(l1)

l3 = l1[:]

# 使用copy函数进行浅复制
l4 = copy(l1)

# True , 证明值完全相等
print(l1 == l2 == l3 == l4)

l1[1].append(9)

# [1, [2, 3, 9], 4]
print(l1)

# True
print(l1 == l2 == l3 == l4)

# [1, [2, 3, 9], 4]
print(l4)
